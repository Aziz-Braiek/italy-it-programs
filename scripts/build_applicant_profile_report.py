"""Reproduce field counts, explicit route outcomes and remaining research gaps."""
import json
from collections import Counter
from pathlib import Path
import applicant_profiles as A
import decision_support as D

ROOT = Path(__file__).resolve().parents[1]
OUT = A.RESEARCH
CHECKED = '2026-11-13'


def read(path): return json.loads(path.read_text(encoding='utf-8'))
def write(name, value): (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def count(facts):
    return {'fully_confirmed':sum(D.is_current(f) and not f.get('missing_components') for f in facts),
            'partly_confirmed':sum(D.is_current(f) and bool(f.get('missing_components')) for f in facts),
            'not_currently_confirmed':sum(not D.is_current(f) for f in facts),
            'previous_cycle_only':sum(f.get('cycle_status')==D.PREVIOUS for f in facts),
            'not_confirmed':sum(f.get('cycle_status')==D.UNKNOWN for f in facts)}


def build(universities, programs):
    data=A.compile_data(universities,programs)
    priority=[p for p in programs if p['overall_status']=='CONFIRMED']
    ub={u['id']:u for u in universities}; hosts=sorted({p['university_id'] for p in priority})
    notes=read(ROOT/'research/decision-refinement-2026-11/review-notes.json')
    sources={sid:r for r in D.read('source-checks.json')['responses'] for sid in r['source_ids']}
    before=read(OUT/'baseline.json')['counts']
    # Scope-wide checked pages are context, not evidence that every field is known.
    extra={'politecnico-milano':['PROFILE-BOCCONI-FEES-2027','PROFILE-BOCCONI-JOINT-2027'],
           'pisa':['PROFILE-PISA-UNIVERSITALY','PROFILE-PISA-ENGLISH-DEGREES','PROFILE-PISA-ENG-PDF-2027'],
           'trento':['PROFILE-28DIGITAL-LANGUAGE']}
    def checked_pages(uid, fact=None):
        fact=fact or {}
        return sorted(set(fact.get('source_urls',[])+fact.get('checked_urls',[])+[sources[sid]['url'] for sid in notes[uid]['source_ids']+extra.get(uid,[]) if sid in sources]))
    def uni_fact(u,key):
        f=u['decision_support'][key]
        if key!='scholarships':return f
        now=[r for r in f if D.is_current(r)]
        selected=now or f
        result={**selected[0], 'value':' | '.join(r['value'] for r in selected), 'source_urls':sorted({url for r in selected for url in r.get('source_urls',[])}),'missing_components':sorted({v for r in selected for v in r.get('missing_components',[])})}
        if now and any(not r.get('missing_components') for r in now):result['missing_components']=[]
        return result
    ledger=[]; counts={}
    for owner,records,fields in [('program',priority,D.PROGRAM_FIELDS),('university',[ub[u] for u in hosts],{**D.UNIVERSITY_FIELDS,'scholarships':'Scholarship opportunity'})]:
        counts[owner]={}
        for field in fields:
            facts=[]
            for r in records:
                uid=r.get('university_id',r['id']);f=D.resolve(r,field,ub[uid]) if owner=='program' else uni_fact(r,field);facts.append(f)
                state='partly_confirmed' if D.is_current(f) and f.get('missing_components') else 'fully_confirmed' if D.is_current(f) else 'previous_cycle_only' if f.get('cycle_status')==D.PREVIOUS else 'not_confirmed'
                ledger.append({'owner':owner,'id':r['id'],'name':r.get('program',r.get('name')),'university_id':uid,'university':ub[uid]['name'],'field':field,'outcome':state,'fact':f,'date_checked':CHECKED,'checked_pages':checked_pages(uid,f),'reason':'; '.join(f.get('missing_components',[])) or f.get('reason') or ('Only previous-cycle material establishes this value.' if not D.is_current(f) else 'Verified only within the stated source scope.'),'university_limit':notes[uid]['reason']})
            b=before[owner][field]
            counts[owner][field]={'before':{'fully_confirmed':b['after_fully_confirmed'],'partly_confirmed':b['after_partly_confirmed'],'not_currently_confirmed':b['previous_cycle_only']+b['not_confirmed'],'previous_cycle_only':b['previous_cycle_only'],'not_confirmed':b['not_confirmed']},'after':count(facts)}
    write('priority-field-ledger.json',ledger)
    write('priority-unverified-fields.json',[r for r in ledger if r['outcome']!='fully_confirmed'])
    # A complete compact 47 x 10 x 12 matrix: each unknown combination is explicit.
    route_ledger=[]
    for p in priority:
        uid=p['university_id']
        for field in A.FIELDS:
            alternatives=A.routes_for(data,p['id'],field)
            pages=sorted(set(checked_pages(uid)+[url for r in alternatives for url in (r if field=='tuition' else r['fact']).get('source_urls',[])]))
            outcomes=[]
            for cat in A.CATEGORIES:
                for origin in A.ORIGINS:
                    profile={'category':cat,'qualification':origin}
                    f=A.select(data,p['id'],field,profile)
                    outcomes.append({'category':cat,'qualification':origin,'outcome':'partly_confirmed' if D.is_current(f) and f.get('missing_components') else 'confirmed' if D.is_current(f) else 'not_confirmed','route_id':f.get('route_id'),'reason':f.get('reason') or '; '.join(f.get('missing_components',[])) or 'Only the selected published route is used.'})
            route_ledger.append({'id':p['id'],'programme':p['program'],'university_id':uid,'field':field,'review_date':CHECKED,'source_backed_route_ids':[r['id'] for r in alternatives],'checked_pages':pages,'university_review_limit':notes[uid]['reason'],'unverified_route_reason':'No source-backed match for every supplied input; no route is inferred from prose, citizenship, qualification origin or mere residence. Conditional permit/country/language criteria stay unresolved.','profile_outcomes':outcomes})
    write('route-gap-ledger.json',route_ledger)
    uni_ledger=[]
    for uid in hosts:
        u=ub[uid]
        uni_ledger.append({'id':uid,'university':u['name'],'national_rule_ref':'universitaly_requirement','university_universitaly_fact':u['decision_support']['universitaly'],'document_fact':u['decision_support']['documents'],'route_refs':data['universities'][uid]['routes'],'checked_pages':checked_pages(uid),'date_checked':CHECKED,'reason':notes[uid]['reason'],'limit':'A national portal requirement or visa deadline is not a university-specific pre-enrolment deadline. Recognition alternatives depend on the exact country/qualification; a broad origin region cannot determine DoV/CIMEA/translation substitutions.'})
    write('university-route-ledger.json',uni_ledger)
    outcomes=[]
    for owner,records in [('program',priority),('university',[ub[u] for u in hosts])]:
        for r in records:
            entries=[row for row in ledger if row['owner']==owner and row['id']==r['id']]
            outcomes.append({'owner':owner,'id':r['id'],'name':r.get('program',r.get('name')),'university':entries[0]['university'],'fully_confirmed':[x['field'] for x in entries if x['outcome']=='fully_confirmed'],'partly_confirmed':[x['field'] for x in entries if x['outcome']=='partly_confirmed'],'previous_cycle_only':[x['field'] for x in entries if x['outcome']=='previous_cycle_only'],'not_confirmed':[x['field'] for x in entries if x['outcome']=='not_confirmed'],'reason':notes[entries[0]['university_id']]['reason']})
    write('record-outcomes.json',outcomes)
    tuition=Counter();historical=Counter()
    for p in priority:
        rules=A.routes_for(data,p['id'],'tuition');now=[r for r in rules if D.is_current(r)]
        kind=next((r['type'] for r in now if r['type'] in ('fixed','band') and not r.get('partial_profile_coverage')),None) or ('rule-only' if any(r['type']=='rule-only' for r in now) else 'not confirmed')
        tuition[kind]+=1
        for kind_old in {r['type'] for r in rules if r.get('cycle_status')==D.PREVIOUS}:historical[kind_old]+=1
    checks=[
        {'university':'University of Bologna','id':'discovered-029','source_id':'SRC-UNIBO-GRENFIN-2027-CALL','cycle':'2027/28 confirmed','type':'rule-only','official_url':sources['SRC-UNIBO-GRENFIN-2027-CALL']['url'],'exact_passage':'consists of a fixed element of € 157.04','context':'PDF page 15, section 8.1: a variable ISEE element follows. EUR 157.04 is not the total annual fee. No published course maximum is inferred.','annual_amount':'Not confirmed'},
        {'university':'Politecnico di Milano','id':'legacy-001','source_id':'REFINE-POLIMI-FEES','cycle':'previous cycle (estimate only) — 2026/27','type':'band','official_url':sources['REFINE-POLIMI-FEES']['url'],'exact_passage':'the amount gradually increases up to a maximum of € 3,943.04','context':'The page identifies 2026/27. Published ordinary-degree band EUR 157.04–3943.04 for a 46–74 ECTS plan, income/credit rules; reserved non-EU foreign-degree MSc students without eligible awards pay the applicable maximum. Not a confirmed 2027/28 fee.','annual_amount':'2027/28 Not confirmed'},
        {'university':'University of Pisa','id':'legacy-052','source_id':'DEC-PISA-FEES','cycle':'previous cycle (estimate only) — 2026/27','type':'rule-only','official_url':sources['DEC-PISA-FEES']['url'],'exact_passage':'the maximum annual all-inclusive tuition fee for students enrolled within the standard duration of their programme is €2,900.','context':'The sentence explicitly says 2026-2027. This is a named contribution maximum, not a verified new-cycle total or a computed range; regional tax/stamp and differently stated lower examples remain distinct.','annual_amount':'2027/28 Not confirmed'},
    ]
    write('tuition-spot-checks.json',{'checked_date':CHECKED,'selection':'Three different universities; no shared 28DIGITAL tariff substitution.','checks':checks,'limitation':'Three independent current 2027/28 complete annual tariffs could not be established. Historical checks remain historical; no fabricated current amounts.'})
    conflicts=D.read('source-conflicts.json'); reviews=[]
    updates={'padua-fee-year-and-basis':'Rechecked: no current typed amount/band approved. Portal 2950 and older formal 2790/2990 have different year/basis; both sources remain visible.',
             'pisa-historical-tuition-bases':'Historical maximum component stored separately. No invented lower/upper band and no 2027/28 amount; university Universitaly page is also explicitly 2026/27.',
             'florence-cambridge-bands':'Unchanged published English-score ambiguity. This is an English requirement conflict, not evidence of a tuition conflict. No new-cycle tuition promoted.'}
    for c in conflicts:reviews.append({**c,'this_round_review':updates.get(c['id'],'Retained conservative route separation; see explicit route map. No original deadline or status changed.')})
    reviews += [
        {'id':'28digital-swiss-profile-scope','state':'scope_gap_not_a_source_contradiction','record_ids':['legacy-020']+[f'discovered-{i:03}' for i in range(13,20)],'sources':[sources['SRC-28DIGITAL-FEES-2027']['url'],sources['PROFILE-28DIGITAL-LANGUAGE']['url']],'handling':'EU/EEA fee row is not Swiss fee evidence. Swiss language exemptions cannot prove a tuition tier. Combined EU/EEA/CH profile amount remains Not confirmed.'},
        {'id':'joint-cyber-fee-coverage','state':'partial_fee_scope_not_a_source_contradiction','record_ids':['legacy-002'],'sources':[sources['PROFILE-BOCCONI-FEES-2027']['url'],sources['PROFILE-BOCCONI-JOINT-2027']['url']],'handling':'Bocconi publishes ordinary first-year 2027/28 MSc contribution EUR 19300. Full joint/partner charge is not independently established, so current model is rule-only, with the component named.'},
    ]
    write('conflict-review.json',reviews)
    examples=[]
    for pid in ['legacy-052','legacy-002','legacy-020']:
        for cat,origin in [('non-eu-abroad','non-eu'),('eu-eea-ch','non-eu'),('italian-qualification','italy')]:
            p={'category':cat,'qualification':origin};f=A.select(data,pid,'deadline',p);t=A.select(data,pid,'tuition',p)
            dates=sorted(e['date'] for e in f.get('events',[]) if e['date']>=CHECKED)
            examples.append({'id':pid,'profile':p,'next_deadline':dates[0] if dates else 'Not confirmed','deadline_source_urls':f.get('source_urls',[]),'tuition_type':t.get('type','not confirmed'),'annual_amount':t.get('amount','Not confirmed'),'tuition_source_urls':t.get('source_urls',[]),'tuition_reason':t.get('reason') or t.get('covered_scope')})
    write('profile-examples.json',examples)
    summary={'baseline_commit':'d1d75fe','checked_date':CHECKED,'scope':{'programs':209,'universities':34,'priority_programs':47,'priority_universities':11,'availability':{'confirmed':47,'awaiting':159,'not_offered':3}},'counts':counts,'tuition_current_program_counts':{k:tuition[k] for k in ('fixed','band','rule-only','not confirmed')},'tuition_historical_program_counts':dict(historical),'tuition_count_basis':'Per programme, at least one fully covered published current category; not all applicants. The current fixed total is the non-EU 28DIGITAL tariff. EU/EEA/CH combined profile tariff remains unresolved. No current band established.','national_rule':'Stored once; 1 partly confirmed university-specific Universitaly deadline, 10 unconfirmed in priority hosts.','route_matrix':{'program_field_rows':len(route_ledger),'profile_combinations_per_row':12,'explicit_outcomes':len(route_ledger)*12},'sources':{'unique_captured_urls':len(D.read('source-checks.json')['responses']),'original_source_registry_unchanged':759},'limits':['No new awaiting-program route research was approved; priority annual rules remain incomplete.','No exact citizenship/permit/country/income/language-history input; unresolved conditional combinations are not silently inferred.','The checked material did not establish three different current complete annual tuition amounts.','Existing record-level review dates, core statuses and original deadline facts remain unchanged.']}
    write('summary.json',summary)
    lines=['# Applicant routes and tuition rules — 13 November 2026','','Baseline: d1d75fe. Scope remains 209 programmes / 34 universities; 47 confirmed / 159 awaiting / 3 not offered. Preview only. No production promotion. The original record review dates and deadline facts are preserved.','','## What changed','','Phase 1 shipped first in 3fab14e: strict yes/no counts and covered/missing scope on every current partial field. The attached scope audit enumerates all 18 partly confirmed minimum-grade and 21 partly confirmed prerequisite records. Typed fee rules and explicit route mappings now drive an optional browser-only applicant profile. No route is inferred from prose deadline labels. National Universitaly requirements live once at national level; university deadlines stay separate.','','## Before / after field counts','','Each cell is **fully confirmed / partly confirmed / not currently confirmed**. The last component includes historical-only fields; their counts are shown separately. These counts describe the published scope, not complete eligibility for every individual applicant.','','| Scope / field | Before F/P/N | After F/P/N | Historical-only before → after |','|---|---|---|---|']
    for owner,fields in counts.items():
        for key,c in fields.items():
            b,a=c['before'],c['after'];fmt=lambda v:f"{v['fully_confirmed']}/{v['partly_confirmed']}/{v['not_currently_confirmed']}"
            lines.append(f"| {owner}.{key} | {fmt(b)} | {fmt(a)} | {b['previous_cycle_only']} → {a['previous_cycle_only']} |")
    lines += ['', 'Denominators: 47 programmes, 11 host universities. Degree-structure facts do not establish intake availability. Scholarship counts mean at least one scoped published opportunity. The Universitaly decrease removes the formerly duplicated national requirement from university-specific confirmation; it is not evidence that a national requirement disappeared.','','Current tuition programme counts: '+', '.join(f'{k}: **{tuition[k]}**' for k in ('fixed','band','rule-only','not confirmed'))+'. These are published-category counts, not a promise that all profiles have a confirmed fee. No current band was established. Historical ordinary Polimi band and Pisa contribution rule are excluded from confirmed filters and exported values.','','## Three different university tuition checks','']
    for c in checks:lines += [f"- **{c['university']} / {c['id']}** — {c['cycle']}, {c['type']}. Exact source passage: “{c['exact_passage']}”. {c['context']} [Official source]({c['official_url']})."]
    lines += ['', 'These are three different institutional checks, not three claimed current complete annual tariffs. Full 2027/28 amounts could not be established from the checked sources.','','## Same-program profile examples','','EU example below uses the requested combined EU/EEA/CH selector; where that category is broader than the fee source it stays unknown. Italian-qualification does not imply citizenship or residence.','','| Programme ID | Category / qualification origin | Next confirmed deadline | Current annual fee |','|---|---|---|---|']
    for e in examples:lines.append(f"| {e['id']} | {e['profile']['category']} / {e['profile']['qualification']} | {e['next_deadline']} | {e['annual_amount']} ({e['tuition_type']}) |")
    lines += ['', 'Pisa CS: non-EU abroad 1 February vs EU/EEA/CH 31 August, with no automatic Italian-qualification fallback. Joint Cyber uses its own Bocconi foreign/Italian qualification rounds, never the ordinary Polimi calendar. Bologna 28DIGITAL has three EU-category application sessions but only the first confirmed visa-applicant session. Tuition uses citizenship rather than qualification origin. Profile controls cannot determine Swiss tariff, exact residence-permit entitlement, country-specific GPA row or language waiver; these remain explicit gaps.','','## Complete remaining gaps and pages checked','','- `priority-field-ledger.json`: each of the 47 × 9 programme and 11 × 5 university field outcomes, with value, cycle, sources, date, missing components and reason.','- `route-gap-ledger.json`: 470 programme/field rows, each with all 12 category/origin combinations explicitly resolved or unconfirmed (5,640 outcomes). Source-backed route IDs point into `compiled-routes.json`; checked pages and unresolved reasons are retained. Contradictory Italian-category/non-Italy-origin combinations are intentionally unconfirmed.','- `university-route-ledger.json`: every priority host’s own Universitaly/document outcome, checked pages and recognition limits.','- `record-outcomes.json`: all 47 programmes and 11 universities, including every unknown/historical/partial field.','- `verified-routes.json`, `national-rules.json`: canonical manually approved evidence; `compiled-routes.json` is derived.','', 'Field-level checked URLs and host context pages are distinguished from approval: retrieval alone does not verify a fact. This round reuses explicitly cited same-day official captures and adds focused source checks, rather than claiming that every unchanged fact was newly verified.','','| Type | Stable ID | Record | Unknown | Partial | Historical |','|---|---|---|---|---|---|']
    for r in outcomes:lines.append(f"| {r['owner']} | {r['id']} | {r['name'].replace('|','/')} | {', '.join(r['not_confirmed']) or '—'} | {', '.join(r['partly_confirmed']) or '—'} | {', '.join(r['previous_cycle_only']) or '—'} |")
    lines += ['', '## University-specific limits','']
    for u in uni_ledger:lines.append(f"- **{u['university']}**: {u['reason']}")
    lines += ['', '## Conflicts and conservative readings','','Padua fees remain unconfirmed: the undated portal contribution and older formal tariff differ in year/basis. Pisa’s historical lower examples are not merged into a new range; its own Universitaly page is still 2026/27. Florence’s saved conflict concerns overlapping Cambridge English bands, not tuition; neither the band nor a new fee is invented. Both sides remain linked on affected pages. Existing Trento/consortium later-round calendar and receipt-year differences, Bologna route distinctions, HySET unfunded continuation and EAP local/online credit thresholds remain separate.','','New scope findings: the EU/EEA tariff does not establish Switzerland’s tariff; the Bocconi ordinary contribution does not independently establish the complete joint Cyber charge. These are scope gaps, not asserted source contradictions. `conflict-review.json` lists the exact official URLs and handling.','','## What remains incomplete / choices','','No prompt requirement was rejected. Unpublished data remain unknown rather than guessed. Awaiting programmes retain existing evidence and explicit empty route mappings; no additional awaiting-route claims were approved. The requested profile is deliberately coarse and cannot resolve every country/permit/funding/language condition. Three distinct current complete annual tariffs could not be verified; historical schedules are labelled as such. Programme availability was not promoted. No accounts, alerts, new universities, security weakening or production change.','','## Verification','','Run the research/site builders, research audit, original regression suites, Python profile guards and `scripts/test_applicant_profiles.mjs`. The profile suite exercises seven different programmes across every category, unknown combinations, URL round-trips, selected-route sorting and CSV/ICS, strict yes/no counts, no-JS full output and 320/390px open/collapsed selectors. Live preview checks repeat the browser flow. Passing these tests verifies behavior and provenance guards, not the truth of unpublished admissions data.']
    (OUT/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return summary


if __name__=='__main__':
    result=build(read(ROOT/'research/universities-2027-2028.json'),read(ROOT/'research/programs-2027-2028.json'))
    print(json.dumps(result['tuition_current_program_counts']))
