"""Deterministic dependency registry. Reading a URL is never fact approval."""
import hashlib
import json
import re
import time
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import decision_support as D

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'research/monitoring'
URL_RE = re.compile(r'https?://[^\s<>"\u201c\u201d]+')
BACKGROUND = {'www.universitaly.it','universitaly-private.cineca.it','www.mur.gov.it','www.esteri.it','www.cimea.it'}


def read(path): return json.loads(path.read_text(encoding='utf-8'))
def write(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for attempt in range(12):
        try:tmp.replace(path);return
        except PermissionError:
            if attempt==11:raise
            time.sleep(min(.05*2**attempt,.5))
def canonical(url):
    p=urlsplit(url.strip())
    if p.scheme.lower() not in ('http','https') or not p.hostname or p.username or p.password:raise ValueError('Not a public HTTP source URL')
    host=p.hostname.lower();port=p.port
    netloc=host+(f':{port}' if port and port not in (80,443) else '')
    return urlunsplit((p.scheme.lower(),netloc,p.path or '/',p.query,''))
def sid(url):return hashlib.sha256(canonical(url).encode()).hexdigest()[:20]
def urls(value):
    if isinstance(value,str):
        for m in URL_RE.finditer(value):
            u=m.group().rstrip('.,;:')
            while u.endswith(')') and u.count(')')>u.count('('):u=u[:-1]
            try:yield canonical(u)
            except ValueError:pass
    elif isinstance(value,list):
        for v in value:yield from urls(v)
    elif isinstance(value,dict):
        for k,v in value.items():
            if k.startswith('http'):yield from urls(k)
            yield from urls(v)


def build():
    previous={r['url']:r for r in read(OUT/'registry.json')['urls']} if (OUT/'registry.json').exists() else {}
    programs=read(ROOT/'research/programs-2027-2028.json');universities=read(ROOT/'research/universities-2027-2028.json');ub={u['id']:u for u in universities}
    approved=read(ROOT/'research/sources.json')+read(D.RESEARCH/'additional-sources.json')
    sources={s['id']:s for s in approved};hosts={urlsplit(u).hostname for s in approved for u in urls(s.get('url',''))}
    for u in universities:
        for key in ('official_website','international_admissions_url','application_portal_url','contact_url'):hosts.update(urlsplit(x).hostname for x in urls(u.get(key,'')))
    roots={h[4:] if h.startswith('www.') else h for h in hosts if h}
    def official(host):return host in hosts or any(host.endswith('.'+r) for r in roots)
    captures={canonical(r['url']):r for r in read(D.RESEARCH/'source-checks.json')['responses']}
    registry={};excluded=set()
    def add(url,ref=None,gate=False,verified=None,file=None,source=None):
        try:url=canonical(url)
        except ValueError:return
        if not official(urlsplit(url).hostname):excluded.add(url);return
        cap=captures.get(url,{})
        stable=urlsplit(url).hostname in BACKGROUND or urlsplit(url).path=='/' or bool(re.search(r'general-guide|glossary|visa-guide|recognition-of-foreign',url,re.I))
        row=registry.setdefault(url,{'id':sid(url),'url':url,'university_ids':set(),'citations':{},'research_files':set(),'source_ids':set(),'last_verified':None,'content_fingerprint':None,'fingerprint_basis':'not yet monitored','tier':'C' if stable else 'B','gates':set(),'type':'PDF' if re.search(r'\.pdf(?:$|[/?])',url,re.I) or 'pdf' in cap.get('headers',{}).get('content-type','') else 'HTML','language':'not confirmed','last_known_final_url':cap.get('effective_url',url)})
        if cap.get('sha256'):
            row['content_fingerprint']=cap['sha256'];row['fingerprint_basis']='prior raw-response SHA-256; replaced by normalized monitoring fingerprint after baseline'
        if row['last_known_final_url']!=url:row['redirect_observed']=True
        if source:
            row['source_ids'].add(source['id'])
            if source.get('university_id') in ub:row['university_ids'].add(source['university_id'])
            if source.get('language'):row['language']=source['language']
        if file:row['research_files'].add(file)
        if verified and (not row['last_verified'] or verified>row['last_verified']):row['last_verified']=verified
        if ref:
            key=(ref['owner'],ref['record_id'],ref['field']);row['citations'][key]=ref;row['university_ids'].add(ref['university_id'])
            if gate:row['gates'].add(key);row['tier']='A'
            elif row['tier']!='A' and urlsplit(url).hostname not in BACKGROUND and ref['field'] not in ('official_website','contact_url'):row['tier']='B'
    for s in approved:add(s['url'],source=s,file='research/sources.json' if s['id'].startswith('SRC-') else 'research/decision-support-2026-11/additional-sources.json')
    def cite(record,owner,field,fact,gate=False):
        uid=record.get('university_id',record['id']);ref={'owner':owner,'record_id':record['id'],'university_id':uid,'field':field,'name':record.get('program',record.get('name'))}
        found=set(urls(fact));ids=set()
        def walk(x):
            if isinstance(x,dict):
                for k,v in x.items():
                    if k in ('source_ids','evidence_source_ids') and isinstance(v,list):ids.update(v)
                    else:walk(v)
            elif isinstance(x,list):
                for v in x:walk(v)
        walk(fact)
        for id in ids:
            if id in sources:found.add(canonical(sources[id]['url']))
        verified=fact.get('verified_date') if isinstance(fact,dict) else None
        if not verified and isinstance(fact,dict) and fact.get('status')=='CONFIRMED':verified=record.get('last_checked')
        for url in found:add(url,ref,gate,verified)
    hosts_priority={p['university_id'] for p in programs if p['overall_status']=='CONFIRMED'}
    for p in programs:
        priority=p['overall_status']=='CONFIRMED';awaiting=p['overall_status']=='REQUIRES_VERIFICATION'
        for key in ('level','language','field','availability_2027_2028'):cite(p,'program',key,p.get(key,{}),priority and p.get(key,{}).get('status')!='CONFIRMED')
        for key,f in p.get('facts',{}).items():cite(p,'program','facts.'+key,f,(priority and f.get('status')!='CONFIRMED') or (awaiting and bool(re.search(r'apply|admission|requirements|entry',key))))
        for key in D.PROGRAM_FIELDS:
            f=D.resolve(p,key,ub[p['university_id']]);cite(p,'program','decision_support.'+key,f,priority and (not D.is_current(f) or bool(f.get('missing_components'))))
        cite(p,'program','record_sources',{'source_ids':p.get('source_ids',[])})
        # Every awaiting lead's institution admissions page is an explicit gate.
        if awaiting:cite(p,'program','admissions_page',ub[p['university_id']].get('international_admissions_url',''),True)
    for u in universities:
        priority=u['id'] in hosts_priority
        for key in ('official_website','international_admissions_url','application_portal_url','contact_url'):cite(u,'university',key,u.get(key,''),priority and key=='international_admissions_url')
        for key,f in u.get('cycle_facts',{}).items():cite(u,'university','cycle_facts.'+key,f,priority and f.get('status')!='CONFIRMED')
        for key in D.UNIVERSITY_FIELDS:
            f=u['decision_support'][key];cite(u,'university','decision_support.'+key,f,priority and (not D.is_current(f) or bool(f.get('missing_components'))))
        for key,f in u['decision_support'].get('policies',{}).items():cite(u,'university','policies.'+key,f,priority and (not D.is_current(f) or bool(f.get('missing_components'))))
        for i,f in enumerate(u['decision_support'].get('scholarships',[])):cite(u,'university',f'scholarships.{i}',f,priority and (not D.is_current(f) or bool(f.get('missing_components'))))
    # Research-only references are retained with their file, not invented record links.
    for path in sorted((ROOT/'research').rglob('*')):
        if path.suffix not in ('.json','.md') or 'monitoring' in path.parts:continue
        for url in set(urls(read(path) if path.suffix=='.json' else path.read_text(encoding='utf-8'))):add(url,file=path.relative_to(ROOT).as_posix())
    rows=[]
    for url,row in sorted(registry.items()):
        row['university_ids']=sorted(row['university_ids']);row['university_names']=[ub[id]['name'] for id in row['university_ids']]
        row['citations']=[row['citations'][k] for k in sorted(row['citations'])]
        row['gates']=[{'owner':a,'record_id':b,'field':c} for a,b,c in sorted(row['gates'])]
        row['gated_record_count']=len({(r['owner'],r['record_id']) for r in row['gates']})
        row['source_ids']=sorted(row['source_ids']);row['research_files']=sorted(row['research_files']);row['official_basis']='Existing approved official-source registry or university-owned admissions dependency; no new research claim.'
        row['content_type']=row['type']
        if row.get('redirect_observed'):row['type']='redirect'
        old=previous.get(url,{})
        if old.get('fingerprint_basis')=='normalized monitoring text SHA-256':
            for key in ('content_fingerprint','fingerprint_basis','last_monitored','last_known_final_url','language','content_type','type'):row[key]=old.get(key,row.get(key))
        rows.append(row)
    manual=OUT/'additional-sources.json'
    if manual.exists():
        for r in read(manual):
            existing=next((item for item in rows if item['url']==canonical(r['url'])),None)
            if existing:
                refs={(c['owner'],c['record_id'],c['field']):c for c in existing['citations']+r['citations']};existing['citations']=list(refs.values())
                existing['gates']+= [g for g in r['gates'] if g not in existing['gates']]
                if r['tier']=='A':existing['tier']='A'
                existing['gated_record_count']=len({(g['owner'],g['record_id']) for g in existing['gates']})
            else:rows.append(r)
    result={'schema_version':1,'source_commit':'900315e','tiers':{'A':7,'B':30,'C':90},'urls':sorted(rows,key=lambda r:r['url']),'excluded_non_dependency_hosts':sorted(excluded)}
    write(OUT/'registry.json',result)
    return result


def validate(universities,programs,registry=None):
    registry=registry or read(OUT/'registry.json');known={r['url'] for r in registry['urls']};source_map={s['id']:s for s in read(ROOT/'research/sources.json')+read(D.RESEARCH/'additional-sources.json')}
    required=set()
    for record in universities+programs:
        required.update(urls(record))
        def refs(x):
            if isinstance(x,dict):
                for k,v in x.items():
                    if k in ('source_ids','evidence_source_ids') and isinstance(v,list):
                        for id in v:
                            if id in source_map:required.add(canonical(source_map[id]['url']))
                    else:refs(v)
            elif isinstance(x,list):
                for v in x:refs(v)
        refs(record)
    missing=required-known
    if missing:raise ValueError('Record source URLs missing from monitoring registry: '+', '.join(sorted(missing)))
    return [r['url'] for r in registry['urls'] if not r['citations']]


if __name__=='__main__':
    result=build();print(json.dumps({'urls':len(result['urls']),'tiers':dict(Counter(r['tier'] for r in result['urls'])),'types':dict(Counter(r['type'] for r in result['urls']))}))
