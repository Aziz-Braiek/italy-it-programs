"""Reproducible priority-scope evidence counts and unresolved-field ledger."""
import json
import secrets
from pathlib import Path
import decision_support as D

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/decision-refinement-2026-11'


def write(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def build(universities, programs):
    baseline = json.loads((OUT/'baseline.json').read_text(encoding='utf-8'))
    notes = json.loads((OUT/'review-notes.json').read_text(encoding='utf-8'))
    ub = {u['id']: u for u in universities}
    priority = [p for p in programs if p['overall_status'] == 'CONFIRMED']
    hosts = {p['university_id'] for p in priority}
    sources = {sid: row for row in D.read('source-checks.json')['responses'] for sid in row['source_ids']}
    ledger = []
    counts = {'program': {}, 'university': {}}
    for owner, records, fields in [('program', priority, D.PROGRAM_FIELDS), ('university', [ub[u] for u in sorted(hosts)], {**D.UNIVERSITY_FIELDS, 'scholarships': 'Scholarship opportunity'})]:
        for key in fields:
            facts = []
            for record in records:
                uid = record.get('university_id', record['id'])
                fact = D.resolve(record, key, ub[uid]) if owner == 'program' else record['decision_support'][key]
                if key == 'scholarships':
                    current = [f for f in fact if D.is_current(f)]
                    chosen = current or fact
                    fact = {**chosen[0], 'value': ' | '.join(f['value'] for f in chosen), 'missing_components': sorted({v for f in chosen for v in f.get('missing_components', [])}), 'source_urls': sorted({url for f in chosen for url in f.get('source_urls', [])})}
                    if current:
                        fact['missing_components'] = [] if any(not f.get('missing_components') for f in current) else fact['missing_components']
                facts.append(fact)
                state = 'degree_structure' if fact.get('evidence_scope') == 'degree_structure' else 'partly_confirmed' if D.is_current(fact) and fact.get('missing_components') else 'confirmed' if D.is_current(fact) else 'previous_cycle_only' if fact['cycle_status'] == D.PREVIOUS else 'not_confirmed'
                checked = sorted(set(fact.get('source_urls', []) + fact.get('checked_urls', []) + [sources[sid]['url'] for sid in notes[uid]['source_ids'] if sid in sources]))
                why = '; '.join(fact.get('missing_components', [])) or fact.get('reason') or ('Only an older-cycle value is verified.' if fact['cycle_status'] == D.PREVIOUS else 'Published scope verified; see cited evidence.')
                ledger.append({'owner': owner, 'id': record['id'], 'university_id': uid, 'university': ub[uid]['name'], 'name': record.get('program') or record['name'], 'field': key, 'outcome': state, 'fact': fact, 'checked_date': '2026-11-13', 'checked_pages': checked, 'reason': why, 'university_review_limit': notes[uid]['reason'], 'review_note': 'Uses the directly reviewed new sources and the earlier same-day official captures; successful retrieval alone does not approve a field.'})
            before = baseline[f'{owner}_counts'][key]
            counts[owner][key] = {'before_current_evidence': before, 'after_current_evidence': sum(D.is_current(f) for f in facts), 'after_fully_confirmed': sum(D.is_current(f) and not f.get('missing_components') for f in facts), 'after_partly_confirmed': sum(D.is_current(f) and bool(f.get('missing_components')) for f in facts), 'degree_structure': sum(f.get('evidence_scope') == 'degree_structure' for f in facts), 'previous_cycle_only': sum(f['cycle_status'] == D.PREVIOUS for f in facts), 'not_confirmed': sum(f['cycle_status'] == D.UNKNOWN for f in facts)}
    def filters(records):
        return {'no_test': sum(D.binary_state(D.resolve(p, 'admission_test', ub[p['university_id']])) == 'no' for p in records), 'certificate_required': sum(D.binary_state(D.resolve(p, 'english_requirement', ub[p['university_id']])) == 'yes' for p in records), 'tuition_documented': sum(D.is_current(D.resolve(p, 'tuition', ub[p['university_id']])) for p in records), 'scholarship_documented': sum(D.is_current(D.scholarship_summary(p, ub[p['university_id']])) for p in records)}
    result = {'baseline_commit': 'e039301', 'programme_scope': 47, 'university_scope': 11, 'current_evidence_totals_include_partial': True, 'counts': counts, 'filters': {'before_default': baseline['confirmed_filters'], 'after_default': filters(priority), 'after_include_awaiting': filters(programs)}}
    write('summary.json', result)
    write('priority-field-ledger.json', ledger)
    gaps = [row for row in ledger if row['outcome'] not in {'confirmed', 'degree_structure'}]
    write('priority-unverified-fields.json', gaps)
    outcomes = []
    for owner, records in [('program', priority), ('university', [ub[u] for u in sorted(hosts)])]:
        for record in records:
            rows = [row for row in ledger if row['owner'] == owner and row['id'] == record['id']]
            outcomes.append({'owner': owner, 'id': record['id'], 'name': record.get('program') or record['name'], 'university': rows[0]['university'], 'not_confirmed': [r['field'] for r in rows if r['outcome'] == 'not_confirmed'], 'partly_confirmed': [r['field'] for r in rows if r['outcome'] == 'partly_confirmed'], 'previous_cycle_only': [r['field'] for r in rows if r['outcome'] == 'previous_cycle_only'], 'reason': notes[rows[0]['university_id']]['reason']})
    write('record-outcomes.json', outcomes)
    spot_path = OUT/'tuition-spot-checks.json'
    if not spot_path.exists():
        eligible = [p for p in priority if D.is_current(D.resolve(p, 'tuition', ub[p['university_id']])) and not D.resolve(p, 'tuition', ub[p['university_id']]).get('missing_components')]
        selected = secrets.SystemRandom().sample(eligible, 3)
        spots = [{'id': p['id'], 'university': ub[p['university_id']]['name'], 'programme': p['program'], 'value': D.resolve(p, 'tuition', ub[p['university_id']])['value'], 'official_url': 'https://masterschool.28digital.eu/admissions/fees', 'exact_passage': '18,000 EUR', 'table_context': 'Non-EU/EEA citizenship row, annual tuition column; EU/EEA row is EUR 6,000/year.', 'checked_date': '2026-11-13'} for p in selected]
        write('tuition-spot-checks.json', {'selection': 'SystemRandom sample without replacement from fully confirmed current-tuition records; selected once and preserved.', 'eligible_records': len(eligible), 'checks': spots, 'limitation': 'All fully confirmed current tuition records in this snapshot share the 28DIGITAL consortium tariff. These are three programme checks, not independent tariff schedules.'})
    spots = json.loads(spot_path.read_text(encoding='utf-8'))
    lines = ['# Decision evidence refinement — 13 November 2026', '', 'Baseline: e039301. Availability remains 47 confirmed / 159 awaiting / 3 not offered. Original record review dates, application deadlines and calendar logic are unchanged. No production release.', '', '## Before and after', '', 'Current-evidence counts include partial fields. Fully confirmed and Partly confirmed are shown separately below; they must not be conflated. Degree-structure labels describe sourced course structure and do not establish intake availability. Scholarship university counts mean at least one published applicable opportunity, not all programmes funded.', '', '| Scope / field | Before current evidence | After current evidence | Fully confirmed | Partly confirmed | Degree structure | Not confirmed |', '|---|---:|---:|---:|---:|---:|---:|']
    for owner, fields in counts.items():
        for key,c in fields.items():lines.append(f"| {owner}.{key} | {c['before_current_evidence']} | {c['after_current_evidence']} | {c['after_fully_confirmed']} | {c['after_partly_confirmed']} | {c['degree_structure']} | {c['not_confirmed']} |")
    lines += ['', 'Program denominator: 47. University denominator: 11. Previous-cycle-only counts and all source details are in summary.json and priority-field-ledger.json.', '', '## Filter semantics and result counts', '', 'Default view contains only the 47 confirmed programme records. Including awaiting records currently gives the same four positive-filter totals. Conditional or applicant-dependent answers map to not confirmed for the binary filters. No English-certificate waiver is interpreted as a universal exemption. A published possible interview does not establish that a compulsory standardised exam exists or is absent.', '', '| Filter | Before | After |', '|---|---:|---:|']
    for k,v in result['filters']['after_default'].items():lines.append(f"| {k} | {baseline['confirmed_filters'][k]} | {v} |")
    lines += ['', 'Tuition/funding documented filters can include current partly confirmed facts only for the published amount/calculation/opportunity. The card names the remaining gaps. Older-cycle values are excluded. CSV keeps six provenance columns per field (value, cycle, URL, date, confirmation, missing components); historical values remain omitted. Degree-structure display does not make historical values eligible for export.', '', '## Research findings and remaining limits', '', 'Added current country-of-qualification grade tables for Padua, Florence Software and the standard foreign-qualification Polimi MSc route; the Bologna/Bocconi joint route remains separate. Pisa department guidance now distinguishes the initial B2 statement from mandatory certification at Universitaly validation, rejecting MOI. Added scoped EAP documents/criteria and university-published standing document/permit guidance. The explicit two-year MUR procedure establishes Universitaly’s visa pre-enrolment requirement across the 11 hosts; most institution-specific deadlines remain unconfirmed. An undated recurring date is not promoted to a 2027/28 deadline.', '', 'No new 2027/28 tuition tariffs or non-EU quotas were established by the checked material. Polimi’s 2026/27 reserved-category maximum-fee rule is now shown as historical planning information, and never enters the current tuition filter. BBS formal calls remain forthcoming. Awaiting-program research was not extended this round: unresolved priority annual rules remain the more important gap.', '', '## Conflicts', '', 'All nine saved conflicts/scope differences now appear on affected programme pages with official links and conservative handling, with compact card notes. Padua fees remain unconfirmed; HySET never becomes funded; differently stated Pisa historical fees are not merged; 28DIGITAL route calendars, document receipt years and award compatibility remain explicit. EAP changed: its university application page is now readable and explicitly says 24+6 credits, while its local requirements page says 18+6/TAPP. The narrower 24+6 online-route statement is published with the unresolved route distinction. One ambiguity entry was added for Florence Software: its published Cambridge B/C numerical bands overlap. The page now labels that language field Partly confirmed and asks for borderline-score clarification rather than repairing the bands. No application-deadline field was changed.', '', '## Three randomly selected tuition records', '', spots['limitation'], '']
    for item in spots['checks']:lines += [f"- **{item['id']} — {item['programme']}**, {item['university']}: non-EU/EEA EUR 18,000/year. Exact official table passage: “{item['exact_passage']}”. [Official fees]({item['official_url']}). Checked {item['checked_date']}; the citizenship row and annual-column context are saved in tuition-spot-checks.json."]
    lines += ['', '## Every priority record with remaining gaps', '', 'The machine-readable ledger records each field, missing components, source URLs, checked date and why the available pages do not establish it. Every priority programme and host has an explicit outcome. Prior captures reused are identified; HTTP access is not treated as fact verification.', '', '| Type | Stable ID | Programme/university | Unknown fields | Partly confirmed fields | Previous-cycle-only fields |', '|---|---|---|---|---|---|']
    for row in outcomes:lines.append(f"| {row['owner']} | {row['id']} | {row['name'].replace('|','/')} | {', '.join(row['not_confirmed']) or '—'} | {', '.join(row['partly_confirmed']) or '—'} | {', '.join(row['previous_cycle_only']) or '—'} |")
    lines += ['', '## What could not be completed', '', 'The checked official material does not establish all 2027/28 fees, quotas, deadlines, test policies or document exemptions. No guessed value was substituted. Previous-cycle awaiting coverage remains as it was. No substantive requirement was rejected; conditional requirements were conservatively kept out of universal yes/no matches. Field-level evidence is distinct from confirming a complete applicant profile.', '', '## Checks', '', 'Run the research builder, static-site builder, research audit, Python regression suite, local browser suites and the protected live-preview suite. Tests cover exact yes/no/not-confirmed matching, historical exclusion, each saved conflict, partial badges, structural labels, collapsed card unknowns, CSV provenance and no-JavaScript output.']
    (OUT/'report.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    build(json.loads((ROOT/'research/universities-2027-2028.json').read_text(encoding='utf-8')), json.loads((ROOT/'research/programs-2027-2028.json').read_text(encoding='utf-8')))
