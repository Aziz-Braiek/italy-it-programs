"""Polite read-only source checks. No admissions-data writes are performed."""
import argparse
import concurrent.futures
import difflib
import gzip
import hashlib
import io
import ipaddress
import json
import os
import re
import shutil
import subprocess
import threading
import time
import unicodedata
import calendar
from collections import Counter
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from itertools import zip_longest
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import requests
from monitor_registry import ROOT, OUT, canonical, sid, read, write

UA_TOKEN='ItalyUniversityTrackerSourceMonitor'
USER_AGENT=UA_TOKEN+'/1.0 (+https://github.com/Aziz-Braiek/italy-it-programs/issues)'
INTERVALS={'A':7,'B':30,'C':90}
KEYWORDS={
 '2027/28':r'(?<!\d)2027\s*[/–-]\s*(?:2028|28)(?!\d)',
 'bando':r'\bband[oi]\b', 'call for applications':r'\bcall(?:s)?\s+for\s+applications?\b',
 'deadline':r'\bdeadlines?\b','scadenza':r'\bscadenz[ae]\b','tuition':r'\btuition\b',
 'tasse':r'\btasse\b','contributo':r'\bcontribut[oi]\b','ISEE':r'\bISEE(?:U)?\b',
 'no. of places':r'\b(?:no\.?|number)\s+of\s+places\b','posti':r'\bposti\b'}
FAILURES={'broken','blocked'}
ACTIONABLE={'minor','substantive','new keyword hit','moved or redirected','broken','blocked'}
MAX_BYTES=8*1024*1024
MAX_TEXT=1024*1024


class NoAccountAuth(requests.auth.AuthBase):
    def __call__(self,request):return request


def utcnow():return datetime.now(timezone.utc)
def iso(value):return value.astimezone(timezone.utc).isoformat()
def parse_time(value):return datetime.fromisoformat(value.replace('Z','+00:00'))
def digest(text):return hashlib.sha256(text.encode('utf-8')).hexdigest()
def next_due(value,tier):
    t=parse_time(value)
    if tier=='A':return t+timedelta(days=7)
    months=1 if tier=='B' else 3;index=t.year*12+t.month-1+months;year,month=divmod(index,12);month+=1
    return t.replace(year=year,month=month,day=min(t.day,calendar.monthrange(year,month)[1]))


@contextmanager
def run_lock(directory):
    directory.mkdir(parents=True,exist_ok=True);path=directory/'run.lock'
    if path.exists() and time.time()-path.stat().st_mtime>3*3600:path.unlink()
    try:fd=os.open(path,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise RuntimeError('Another monitor owns this state directory; no network request was made.')
    try:
        with os.fdopen(fd,'w') as f:f.write(str(os.getpid()))
        yield
    finally:path.unlink(missing_ok=True)


class ContentParser(HTMLParser):
    """Keep content blocks; drop navigation/cookie/footer elements before hashing."""
    SKIP={'script','style','nav','footer','header','aside','noscript','svg','template','head'}
    BLOCK={'p','div','li','td','th','tr','h1','h2','h3','h4','section','article','br','dt','dd'}
    VOID={'br','hr','img','input','meta','link','source','wbr','area','base','embed','param','track'}
    def __init__(self):super().__init__(convert_charrefs=True);self.stack=[];self.skip=0;self.main=0;self.all=[];self.focus=[];self.links=[];self.main_links=[];self.language=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.language=a.get('lang')
        token=' '.join((a.get('id',''),a.get('class',''),a.get('role',''))).lower()
        skip=tag in self.SKIP or bool(re.search(r'cookie|consent-banner|breadcrumb|social-share|site-menu|navigation',token)) or 'hidden' in a or a.get('aria-hidden')=='true'
        main=tag=='main' or a.get('role')=='main'
        if tag not in self.VOID:self.stack.append((tag,skip,main));self.skip+=int(skip);self.main+=int(main)
        if tag=='a' and not self.skip and a.get('href') and not re.match(r'^(?:#|mailto:|tel:|javascript:)',a['href'],re.I):
            self.links.append(a['href'])
            if self.main:self.main_links.append(a['href'])
        if not self.skip and tag in self.BLOCK:self.emit('\n')
    def emit(self,text):self.all.append(text);self.focus.extend([text] if self.main else [])
    def handle_endtag(self,tag):
        index=next((i for i in range(len(self.stack)-1,-1,-1) if self.stack[i][0]==tag),None)
        if index is not None:
            for _,skip,main in self.stack[index:]:self.skip-=int(skip);self.main-=int(main)
            self.stack=self.stack[:index]
        if not self.skip and tag in self.BLOCK:self.emit('\n')
    def handle_data(self,text):
        if not self.skip:self.emit(text)
    def text(self):return ''.join(self.focus if len(''.join(self.focus).strip())>30 else self.all)


def normalize(text):
    lines=[]
    for line in unicodedata.normalize('NFKC',text).replace('\x00','').splitlines():
        line=re.sub(r'\s+',' ',line).strip()
        # Only unmistakable boilerplate; never strip an admissions date/fee line.
        if not line or re.match(r'^(?:copyright\b|©\s*20\d\d|all rights reserved|powered by\b)',line,re.I):continue
        if not lines or lines[-1]!=line:lines.append(line)
    return '\n'.join(lines)


def extract(body,content_type,details=False):
    if body.startswith(b'%PDF') or 'pdf' in content_type:
        from pypdf import PdfReader
        pdf=PdfReader(io.BytesIO(body));n=len(pdf.pages)
        if n>150:raise ValueError('PDF exceeds 150-page extraction limit; manual review required')
        result=(normalize('\n'.join(p.extract_text() or '' for p in pdf.pages)),None,'PDF')
        return (*result,None) if details else result
    parser=ContentParser();parser.feed(body.decode('utf-8',errors='replace'));result=(normalize(parser.text()),parser.language,'HTML')
    links=parser.main_links if len(''.join(parser.focus).strip())>30 else parser.links
    return (*result,digest('\n'.join(sorted(set(links))))) if details else result


def keyword_hits(text):
    found={}
    for name,pattern in KEYWORDS.items():
        m=re.search(pattern,text,re.I)
        if m:
            start=max(text.rfind('\n',0,m.start())+1,m.start()-160);end=text.find('\n',m.end())
            if end<0:end=len(text)
            found[name]=text[start:min(end,m.end()+240)].strip()
    return found


def content_metadata(text):
    tokens=text.split();shingles={' '.join(tokens[i:i+5]) for i in range(max(1,len(tokens)-4))}
    sensitive='\n'.join(line for line in text.splitlines() if re.search(r'\d|requir|prerequis|compulsory|optional|eligib|tuition|fee|deadline|scaden|tass|contribut|ISEE|seats|posti|language|English|certificat',line,re.I))
    hits=keyword_hits(text)
    return {'fingerprint':digest(text),'critical_fingerprint':digest(sensitive),'sample_fingerprints':sorted(digest(s)[:32] for s in shingles)[:128],'token_count':len(tokens),'keyword_flags':{k:k in hits for k in KEYWORDS}}


def classify_metadata(previous,current,threshold=.02):
    before=previous.get('keyword_flags',{});flipped={k:{'before':bool(before.get(k)),'after':v} for k,v in current['keyword_flags'].items() if bool(before.get(k))!=v}
    hits=[k for k,v in flipped.items() if v['after']]
    link_changed=previous.get('link_fingerprint') is not None and current.get('link_fingerprint') is not None and previous['link_fingerprint']!=current['link_fingerprint']
    if previous.get('fingerprint')==current['fingerprint'] and not link_changed:return 'unchanged',[],{}
    if not previous.get('fingerprint') and previous.get('last_class') in FAILURES:return 'substantive',[],{}
    if not previous.get('fingerprint'):return 'unchanged',[],{}
    if hits:return 'new keyword hit',hits,flipped
    a=set(previous.get('sample_fingerprints',[]));b=set(current['sample_fingerprints']);change=1-len(a&b)/len(a|b) if a|b else 1
    critical=link_changed or previous.get('critical_fingerprint')!=current['critical_fingerprint']
    return ('substantive' if critical or change>=threshold else 'minor'),[],flipped


def failure_kind(event):
    if event.get('result_unknown'):return 'checkpoint_incomplete'
    text=event.get('error','').lower()
    for needle,name in [('checkpoint','checkpoint_incomplete'),('robots disallow','robots_disallowed'),('robots','robots_unavailable'),('ssl','tls_failure'),('timeout','timeout'),('dns','dns_failure'),('captcha','access_blocked'),('login','access_blocked'),('redirect','redirect_review_required'),('exceed','size_limit'),('extract','text_extraction_failed')]:
        if needle in text:return name
    return 'http_'+str(event['status']) if event.get('status') else 'check_failed' if event.get('class') in FAILURES else None


SOURCE_KEYS={'last_attempt','last_success','fingerprint','link_fingerprint','critical_fingerprint','sample_fingerprints','token_count','keyword_flags','final_url','consecutive_failures','type','language','etag','last_modified','last_change_detected','last_class','retry_after_until','recovered_without_http_headers'}
EVENT_KEYS={'source_id','source_url','tier','checked_at','class','status','type','language','final_url','final_url_changed','redirects','fingerprint','link_fingerprint','keyword_flags','flipped_keyword_flags','new_keywords','baseline_established','consecutive_failures','result_unknown','http_metadata_recovered','recovery','content_change_class'}


def metadata_event(event):
    result={k:v for k,v in event.items() if k in EVENT_KEYS}
    if not result.get('keyword_flags') and event.get('initial_keyword_hits'):result['keyword_flags']={k:k in event['initial_keyword_hits'] for k in KEYWORDS}
    result['failure_kind']=event.get('failure_kind') or failure_kind(event)
    return result


def metadata_state(state):
    robots={}
    for origin,row in state.get('robots',{}).items():
        r={k:v for k,v in row.items() if k!='text'}
        if row.get('text'):
            rules=RobotsRules(row['text']);r['policy']={'rules':rules.rules,'delay_seconds':rules.delay}
        robots[origin]=r
    return {'schema_version':1,'sources':{id:{k:v for k,v in row.items() if k in SOURCE_KEYS} for id,row in state.get('sources',{}).items()},'robots':robots}


def compact_diff(old,new):
    a=old.splitlines();b=new.splitlines();result=[]
    matcher=difflib.SequenceMatcher(None,a,b,autojunk=False)
    for group in matcher.get_grouped_opcodes(1):
        removed=[];added=[];context=[]
        for tag,i,j,k,l in group:
            if tag in ('replace','delete'):removed.extend(a[i:j])
            if tag in ('replace','insert'):added.extend(b[k:l])
            if tag=='equal':context.extend(a[i:j])
        result.append({'removed':'\n'.join(removed)[:700],'added':'\n'.join(added)[:700],'context':'\n'.join(context)[:350]})
        if len(result)==3:break
    return result


def classify(old,new,threshold=.02):
    if old==new:return 'unchanged',[],[]
    hits=sorted(set(keyword_hits(new))-set(keyword_hits(old)))
    diff=compact_diff(old,new)
    if hits:return 'new keyword hit',hits,diff
    changed='\n'.join(p[k] for p in diff for k in ('added','removed'))
    # A one-digit fee, date, grade or quota edit must not be dismissed as minor.
    numeric=re.search(r'\d',changed) and (re.search(r'€|EUR|202[6-9]|\d[/-]\d|\b(?:deadline|scadenza|tuition|fee|tass|contribut|ISEE|CFU|ECTS|GPA|places|posti|minimum)\b',changed,re.I))
    ratio=1-difflib.SequenceMatcher(None,old.split(),new.split(),autojunk=False).ratio()
    return ('substantive' if numeric or ratio>=threshold else 'minor'),[],diff


class RobotsRules:
    """Longest-match Allow/Disallow, including * and $; stricter delay wins."""
    def __init__(self,text):
        self.groups=[];agents=[];rules=[];delay=0.;started=False
        for raw in text.splitlines()+['User-agent: __END__']:
            line=raw.split('#',1)[0].strip()
            if ':' not in line:continue
            key,value=[s.strip() for s in line.split(':',1)];key=key.lower()
            if key=='user-agent':
                if started:self.groups.append((agents,rules,delay));agents=[];rules=[];delay=0.;started=False
                agents.append(value.lower())
            elif agents:
                started=True
                if key in ('allow','disallow') and value:rules.append((key=='allow',value))
                if key=='crawl-delay':
                    try:delay=max(delay,float(value))
                    except ValueError:pass
                if key=='request-rate':
                    m=re.match(r'(\d+)\s*/\s*(\d+)',value)
                    if m and int(m[1]):delay=max(delay,int(m[2])/int(m[1]))
        token=UA_TOKEN.lower();matches=[(max((len(a) if a!='*' else 0 for a in agents if a=='*' or a in token),default=-1),rules,d) for agents,rules,d in self.groups]
        best=max((m[0] for m in matches),default=-1)
        self.rules=[r for score,rr,d in matches if score==best for r in rr];self.delay=max([2.]+[d for score,rr,d in matches if score==best])
    def allows(self,url):
        p=urlsplit(url);path=p.path+('?' +p.query if p.query else '');hits=[]
        for allow,pattern in self.rules:
            anchor=pattern.endswith('$');body=pattern[:-1] if anchor else pattern
            if re.match('^'+re.escape(body).replace(r'\*','.*')+('$' if anchor else ''),path):hits.append((len(body.replace('*','')),allow))
        return not hits or max(hits)[1]


class HostGate:
    def __init__(self,clock=time.monotonic,sleep=time.sleep):self.clock=clock;self.sleep=sleep;self.locks={};self.last={};self.delays={};self.guard=threading.Lock()
    def run(self,url,fn):
        host=urlsplit(url).hostname
        with self.guard:lock=self.locks.setdefault(host,threading.Lock())
        with lock:
            delay=max(2.,self.delays.get(host,2.));wait=self.last.get(host,-1e15)+delay-self.clock()
            if wait>0:self.sleep(wait)
            try:return fn()
            finally:self.last[host]=self.clock()


def safe_url(url):
    p=urlsplit(canonical(url));host=p.hostname
    if p.port not in (None,80,443) or host=='localhost' or host.endswith(('.local','.internal')):raise ValueError('Non-public source URL')
    try:
        if not ipaddress.ip_address(host).is_global:raise ValueError('Non-public address')
    except ValueError as exc:
        if 'Non-public' in str(exc):raise
    return canonical(url)


def blocked(body,url,status):
    sample=body[:250000].decode('utf-8',errors='ignore').lower()
    return bool(re.search(r'captcha|verify (?:that )?you are human|checking your browser|cf-chl-|just a moment\.\.\.|type=["\x27]password|login required|sign in to continue',sample)) or bool(re.search(r'/(?:login|signin|sso)(?:[/?]|$)',urlsplit(url).path,re.I))


class Fetcher:
    def __init__(self,registry,state,request=None,gate=None,now=None,max_requests_bytes=512*1024*1024):
        self.registry=registry;self.state=state;self.request=request or requests.get;self.gate=gate or HostGate();self.now=now or utcnow();self.lock=threading.Lock();self.robots_locks={};self.memo={};self.bytes=0;self.request_count=0;self.limit=max_requests_bytes
        self.allowed={urlsplit(r['url']).hostname for r in registry};self.roots={h[4:] if h.startswith('www.') else h for h in self.allowed}
    def trusted(self,url):
        host=urlsplit(safe_url(url)).hostname
        return host in self.allowed or any(host.endswith('.'+r) for r in self.roots)
    def once(self,url,headers):
        def send():
            with self.lock:
                if url in self.memo:return self.memo[url]
                if self.bytes>=self.limit:raise ValueError('Per-run download budget exhausted')
                self.request_count+=1
            response=self.request(url,headers={'User-Agent':USER_AGENT,'Accept':'text/html,application/pdf;q=0.9,*/*;q=0.1',**headers},auth=NoAccountAuth(),cookies={},timeout=(10,25),allow_redirects=False,stream=True)
            body=bytearray()
            try:
                for chunk in response.iter_content(65536):
                    body.extend(chunk)
                    with self.lock:
                        self.bytes+=len(chunk)
                        if self.bytes>self.limit:raise ValueError('Per-run download budget exhausted')
                    if len(body)>MAX_BYTES:raise ValueError('Response exceeds 8 MiB download limit')
                result={'status':response.status_code,'headers':{k.lower():v for k,v in response.headers.items()},'body':bytes(body),'url':url}
            finally:response.close()
            with self.lock:
                # Only normalized content is retained by the run; response memory is bounded.
                self.memo[url]=result
            return result
        return self.gate.run(url,send)
    def request_with_retry(self,url,headers):
        for attempt in range(3):
            try:
                result=self.once(url,headers)
                if result['status'] not in (429,500,502,503,504) or attempt==2:return result
                self.memo.pop(url,None)
                wait=2**(attempt+2);retry=result['headers'].get('retry-after')
                if retry:
                    try:wait=max(wait,float(retry))
                    except ValueError:
                        try:wait=max(wait,(parsedate_to_datetime(retry)-self.now).total_seconds())
                        except (TypeError,ValueError):pass
                if wait>120:return {**result,'retry_deferred':True,'retry_after_until':iso(self.now+timedelta(seconds=wait))}
            except requests.RequestException:
                if attempt==2:raise
                wait=2**(attempt+2)
            self.gate.sleep(wait)
    def rules(self,url):
        p=urlsplit(url);origin=f'{p.scheme}://{p.netloc}'
        with self.lock:lock=self.robots_locks.setdefault(origin,threading.Lock())
        with lock:
            cache=self.state.setdefault('robots',{}).get(origin)
            if cache and cache.get('retry_after_until') and self.now<parse_time(cache['retry_after_until']):raise ValueError('robots Retry-After is still in effect; fail closed')
            if cache and (self.now-parse_time(cache['checked_at'])).total_seconds()<7*86400:
                if cache['status'] not in (200,404,410) or cache.get('unusable'):raise ValueError('robots.txt unavailable; fail closed')
                if 'text' in cache:rules=RobotsRules(cache['text'])
                elif cache.get('policy'):
                    rules=RobotsRules('');rules.rules=cache['policy']['rules'];rules.delay=cache['policy']['delay_seconds']
                else:raise ValueError('Cached robots policy unavailable; fail closed until next scheduled check')
            else:
                current=origin+'/robots.txt'
                conditional={}
                if cache:
                    if cache.get('etag'):conditional['If-None-Match']=cache['etag']
                    if cache.get('last_modified'):conditional['If-Modified-Since']=cache['last_modified']
                for i in range(6):
                    r=self.request_with_retry(current,conditional)
                    if r['status'] in (301,302,303,307,308) and r['headers'].get('location'):
                        current=canonical(urljoin(current,r['headers']['location']))
                        if not self.trusted(current):raise ValueError('robots redirect to unapproved host')
                        continue
                    break
                if r['status']==304 and cache:
                    if 'text' in cache:r={**r,'status':cache['status'],'body':cache['text'].encode()}
                    elif cache.get('policy'):
                        with self.lock:self.state['robots'][origin]={**cache,'checked_at':iso(self.now)}
                        rules=RobotsRules('');rules.rules=cache['policy']['rules'];rules.delay=cache['policy']['delay_seconds']
                        self.gate.delays[p.hostname]=max(self.gate.delays.get(p.hostname,2),rules.delay)
                        return rules
                    else:raise ValueError('304 robots response without a usable parsed policy')
                text=r['body'].decode('utf-8',errors='replace') if r['status']==200 else ''
                with self.lock:self.state.setdefault('robots',{})[origin]={'checked_at':iso(self.now),'status':r['status'],'text':text[:250000],'etag':r['headers'].get('etag') or (cache or {}).get('etag'),'last_modified':r['headers'].get('last-modified') or (cache or {}).get('last_modified'),'retry_after_until':r.get('retry_after_until')}
                if r['status'] not in (200,404,410):raise ValueError('robots.txt unavailable; fail closed')
                if r['status']==200 and ('<html' in text.lower() or blocked(r['body'],current,r['status'])):
                    self.state['robots'][origin]['unusable']=True
                    raise ValueError('robots.txt returned a wall or HTML; fail closed')
                rules=RobotsRules(text)
            self.gate.delays[p.hostname]=max(self.gate.delays.get(p.hostname,2),rules.delay)
            return rules
    def fetch(self,url,conditional=None):
        current=safe_url(url);redirects=[]
        for hop in range(6):
            if not self.trusted(current):return {'class':'moved or redirected','error':'Redirect target is not an approved official host; review before following.','final_url':current,'redirects':redirects}
            if not self.rules(current).allows(current):return {'class':'broken','error':'robots disallow; no content request made','final_url':current,'redirects':redirects}
            if re.search(r'/(?:login|signin|sso)(?:[/?]|$)',urlsplit(current).path,re.I):return {'class':'blocked','error':'Login route; no bypass attempted','final_url':current,'redirects':redirects}
            conditional=conditional or {}
            headers={k:v for k,v in conditional.items() if not k.startswith('_')} if current==conditional.get('_final_url',url) else {}
            r=self.request_with_retry(current,headers)
            if r['status'] in (301,302,303,307,308) and r['headers'].get('location'):
                target=canonical(urljoin(current,r['headers']['location']));redirects.append({'from':current,'status':r['status'],'to':target});current=target;continue
            if r['status'] in (401,403) or blocked(r['body'],current,r['status']):return {'class':'blocked','error':'Captcha/login/access wall; no bypass attempted','status':r['status'],'final_url':current,'redirects':redirects}
            if r['status']==304:return {**r,'final_url':current,'redirects':redirects}
            if r['status']>=400:return {'class':'broken','error':f"HTTP {r['status']}"+('; Retry-After deferred' if r.get('retry_deferred') else ''),'status':r['status'],'final_url':current,'redirects':redirects,'retry_after_until':r.get('retry_after_until')}
            if not 200<=r['status']<300:return {'class':'broken','error':f"Unexpected HTTP {r['status']}",'final_url':current,'redirects':redirects}
            text,language,kind,link_fp=extract(r['body'],r['headers'].get('content-type',''),details=True)
            if not text:return {'class':'broken','error':'No extractable public text; manual review required','final_url':current,'redirects':redirects}
            return {**r,'body':None,'text':text,'language':language,'type':kind,'link_fingerprint':link_fp,'final_url':current,'redirects':redirects}
        return {'class':'broken','error':'Redirect limit exceeded','final_url':current,'redirects':redirects}


class Store:
    def __init__(self,path):
        self.path=Path(path);self.path.mkdir(parents=True,exist_ok=True);self.bytes=sum(p.stat().st_size for p in self.path.glob('*.gz'));self.lock=threading.Lock()
    def load(self,previous):
        files=previous.get('snapshots',[])
        if not files:return None
        p=self.path/files[-1]
        if not p.is_file():return None
        return gzip.decompress(p.read_bytes()).decode('utf-8')
    def keep(self,id,text,previous):
        encoded=text.encode('utf-8');truncated=len(encoded)>MAX_TEXT;text=encoded[:MAX_TEXT].decode('utf-8',errors='ignore')
        name=f'{id}-{digest(text)[:20]}.txt.gz';p=self.path/name
        with self.lock:
            if not p.exists():
                compressed=gzip.compress(text.encode(),compresslevel=9,mtime=0)
                if self.bytes+len(compressed)>128*1024*1024:raise ValueError('128 MiB compressed snapshot budget exhausted')
                p.write_bytes(compressed);self.bytes+=len(compressed)
            files=[x for x in previous.get('snapshots',[]) if x!=name]+[name]
            for old in files[:-2]:
                old_path=self.path/old
                if old_path.exists():self.bytes-=old_path.stat().st_size;old_path.unlink()
        return files[-2:],truncated


def priority(row):
    return (0 if row['tier']=='A' else 1 if row['tier']=='B' else 2,0 if row.get('new_keywords') or row.get('keyword_flags',{}).get('2027/28') or '2027/28' in row.get('initial_keyword_hits',{}) else 1,0 if row.get('needs_new_url') else 1,row['source_url'])


QUEUE_KEYS={'id','source_id','source_url','university_ids','universities','programs','affected_fields','tier','change_class','new_keywords','keyword_flags','flipped_keyword_flags','detected_at','last_seen_at','needs_new_url','suggested_action','failure_kind','baseline_observation','observation','resolution','result_unknown'}


def queue_metadata(payload):
    result={'schema_version':1}
    for group in ('open','closed'):
        if group not in payload:continue
        result[group]=[]
        for row in payload[group]:
            item={k:v for k,v in row.items() if k in QUEUE_KEYS}
            if row.get('initial_keyword_hits'):item['keyword_flags']={k:k in row['initial_keyword_hits'] for k in KEYWORDS};item['baseline_observation']=True
            item['programs']=group_programs(row.get('programs',[]))
            if row.get('error'):item['failure_kind']=failure_kind({'class':row['change_class'],'error':row['error'],'result_unknown':row.get('result_unknown')})
            result[group].append(item)
    return result


def group_programs(citations):
    grouped={}
    for c in citations:
        id=c['record_id'];row=grouped.setdefault(id,{'record_id':id,'university_id':c['university_id'],'name':c['name'],'fields':set()})
        row['fields'].update(c.get('fields',[]) or ([c['field']] if c.get('field') else []))
    return [{**r,'fields':sorted(r['fields'])} for _,r in sorted(grouped.items())]
def queue_item(source,event):
    event=metadata_event(event)
    return {'id':'q-'+digest(source['id']+'|'+event['class']+'|'+event.get('fingerprint',event.get('failure_kind') or 'baseline'))[:20],
      'source_id':source['id'],'source_url':source['url'],'university_ids':source['university_ids'],'universities':source['university_names'],
      'programs':group_programs([r for r in source['citations'] if r['owner']=='program']),'affected_fields':sorted({r['field'] for r in source['citations']}),
      'tier':source['tier'],'change_class':event['class'],'new_keywords':event.get('new_keywords',[]),'keyword_flags':event.get('keyword_flags',{}),'flipped_keyword_flags':event.get('flipped_keyword_flags',{}),
      'detected_at':event['checked_at'],'last_seen_at':event['checked_at'],'needs_new_url':event.get('consecutive_failures',0)>=3,
      'suggested_action':'replace broken link' if event.get('consecutive_failures',0)>=3 or event['class']=='broken' else 'review public access; do not bypass' if event['class']=='blocked' else 're-verify tuition' if any(event.get('keyword_flags',{}).get(k) for k in ['tuition','tasse','contributo','ISEE']) else 'check whether 2027/28 call is published',
      'failure_kind':event.get('failure_kind'),'baseline_observation':bool(event.get('baseline_established')),'observation':'Monitoring flags only; not evidence of applicability or factual review.'}


def render_queue(payload,path):
    lines=['# Source review queue','','Monitoring observations only. No record is automatically changed. Diffs are not published by the website.','']
    for item in sorted(payload['open'],key=priority):
        local=path.parent/'private/reviews'/(item['source_id']+'.json')
        if local.exists():
            review=read(local);item={**item,'diff_excerpt':review.get('diff',[]),'initial_keyword_hits':review.get('keyword_hits',{})}
        lines += [f"## {item['id']} — Tier {item['tier']} — {item['change_class']}",'',f"University: {', '.join(item['universities']) or 'National/background'}. Source: {item['source_url']}",f"Detected: {item['detected_at']}. Action: {item['suggested_action']}.",f"Fields: {', '.join(item['affected_fields'])}",item['observation'],'']
        for p in item.get('diff_excerpt',[]):lines += ['```text','Context: '+p['context'],'Removed: '+p['removed'],'Added: '+p['added'],'```','']
        if item.get('initial_keyword_hits'):lines += ['Initial observations: '+json.dumps(item['initial_keyword_hits'],ensure_ascii=False),'']
        if item.get('error'):lines += ['Check failure: '+item['error'],'']
    lines += [f"Open items: {len(payload['open'])}. Closed items are in archive.json."]
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')


def run(registry,tiers,state_dir=OUT,workers=6,now=None,threshold=.02,fetcher_factory=Fetcher,max_run_seconds=3600,metadata_only=False):
    now=now or utcnow();state_dir=Path(state_dir);state_dir.mkdir(parents=True,exist_ok=True)
    state=read(state_dir/'state.json') if (state_dir/'state.json').exists() else {'schema_version':1,'sources':{},'robots':{}}
    queue=queue_metadata(read(state_dir/'queue.json')) if (state_dir/'queue.json').exists() else {'schema_version':1,'open':[]}
    archive=queue_metadata(read(state_dir/'archive.json')) if (state_dir/'archive.json').exists() else {'schema_version':1,'closed':[]}
    by_id={r['id']:r for r in registry['urls']}
    recovered=0
    for path in (state_dir/'results').glob('*.json'):
        checkpoint=read(path);event=checkpoint['event'];id=event['source_id']
        if id not in by_id or state['sources'].get(id,{}).get('last_attempt','')>event['checked_at']:continue
        state['sources'][id]=checkpoint['state'];recovered+=1
        if event['class'] in ACTIONABLE or event.get('initial_keyword_hits') or (event.get('baseline_established') and any(event.get('keyword_flags',{}).values())):
            item=queue_item(by_id[id],event)
            if not any(q['id']==item['id'] for q in queue['open']+archive['closed']):queue['open'].append(item)
    if metadata_only:state=metadata_state(state)
    store=None if metadata_only else Store(state_dir/'snapshots');fetcher=fetcher_factory(registry['urls'],state,now=now);events=[];skipped=[]
    candidates=[r for r in registry['urls'] if r['tier'] in tiers]
    due=[];deferred=[];started=time.monotonic()
    for row in candidates:
        previous=state['sources'].get(row['id'],{})
        journal=state_dir/'attempts'/(row['id']+'.json')
        last_attempt=max(previous.get('last_attempt',''),read(journal).get('attempted_at','') if journal.exists() else '')
        if (last_attempt and now<next_due(last_attempt,row['tier'])) or (previous.get('retry_after_until') and now<parse_time(previous['retry_after_until'])):skipped.append(row['id'])
        else:due.append(row)
    by_host={}
    for row in due:by_host.setdefault(urlsplit(row['url']).hostname,[]).append(row)
    due=[row for batch in zip_longest(*by_host.values()) for row in batch if row]
    def check(row):
        if time.monotonic()-started>=max_run_seconds:return row,None,None
        previous=state['sources'].get(row['id'],{});event={'source_id':row['id'],'source_url':row['url'],'tier':row['tier'],'checked_at':iso(now)};p={**previous,'last_attempt':iso(now)}
        # Durable reservations prevent an interrupted run from re-fetching early.
        write(state_dir/'attempts'/(row['id']+'.json'),{'attempted_at':iso(now)})
        headers={}
        old=store.load(previous) if store else None
        if old is not None or (metadata_only and previous.get('fingerprint')):
            headers['_final_url']=previous.get('final_url',row['url'])
            if previous.get('etag'):headers['If-None-Match']=previous['etag']
            if previous.get('last_modified'):headers['If-Modified-Since']=previous['last_modified']
        try:
            r=fetcher.fetch(row['url'],headers);event.update({k:v for k,v in r.items() if k not in ('body','text','headers','url')})
            if r.get('retry_after_until'):p['retry_after_until']=r['retry_after_until']
            if r.get('class') in FAILURES:
                p['consecutive_failures']=previous.get('consecutive_failures',0)+1
            elif r.get('class'):
                p['consecutive_failures']=0
            else:
                text=old if r.get('status')==304 else r['text']
                if metadata_only:
                    if r.get('status')==304:
                        if not previous.get('fingerprint'):raise ValueError('304 without a known fingerprint')
                        current={k:v for k,v in previous.items() if k in ('fingerprint','link_fingerprint','critical_fingerprint','sample_fingerprints','token_count','keyword_flags')}
                    else:current={**content_metadata(text),'link_fingerprint':r.get('link_fingerprint')}
                    cls,hits,flipped=classify_metadata(previous,current,threshold)
                    event.update({'class':cls,'new_keywords':hits,'flipped_keyword_flags':flipped,'keyword_flags':current.get('keyword_flags',{}),'fingerprint':current['fingerprint'],'baseline_established':not bool(previous.get('fingerprint'))})
                    p.update(current)
                elif text is None:raise ValueError('304 without a usable snapshot; next scheduled check required')
                elif old is None:
                    event.update({'class':'unchanged','baseline_established':True,'initial_keyword_hits':keyword_hits(text),'diff':[],'new_keywords':[]})
                elif previous.get('fingerprint')==digest(text):
                    event.update({'class':'unchanged','new_keywords':[],'diff':[]})
                else:
                    cls,keywords,diff=classify(old,text,threshold);event.update({'class':cls,'new_keywords':keywords,'diff':diff})
                    if previous.get('snapshot_truncated'):
                        event['comparison_limited']='Previous snapshot was truncated; review full source.'
                        if cls=='unchanged':event['class']='substantive'
                if not metadata_only:event['fingerprint']=digest(text);p.update(content_metadata(text))
                prior_final=previous.get('final_url',row.get('last_known_final_url',row['url']));event['final_url_changed']=r['final_url']!=prior_final
                if r.get('redirects') and (event['final_url_changed'] or not previous):event['content_change_class']=event['class'];event['class']='moved or redirected'
                if not metadata_only:
                    snapshots,truncated=store.keep(row['id'],text,previous);event['snapshot_truncated']=truncated
                    p.update({'snapshots':snapshots,'snapshot_truncated':truncated,'keywords':keyword_hits(text)})
                p.update({'last_success':iso(now),'fingerprint':event['fingerprint'],'final_url':r['final_url'],'consecutive_failures':0,'recovered_without_http_headers':False,'type':r.get('type',previous.get('type',row.get('content_type',row['type']))),'language':r.get('language') or previous.get('language',row['language'])})
                for name,key in [('etag','etag'),('last-modified','last_modified')]:
                    if r.get('headers',{}).get(name):p[key]=r['headers'][name]
                # A baseline has no evidence of a temporal content change.
                if not event.get('baseline_established') and event['class'] in ACTIONABLE:p['last_change_detected']=iso(now)
        except Exception as exc:
            event.update({'class':'broken','error':f'{type(exc).__name__}: {str(exc)[:250]}'});p['consecutive_failures']=previous.get('consecutive_failures',0)+1
        event['consecutive_failures']=p.get('consecutive_failures',0);p['last_class']=event['class']
        if metadata_only:event=metadata_event(event);p={k:v for k,v in p.items() if k in SOURCE_KEYS}
        # Independent per-URL result survives a global checkpoint/file-lock failure.
        write(state_dir/'results'/(row['id']+'.json'),{'event':event,'state':p})
        return row,event,p
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures={pool.submit(check,row):row for row in due}
        for n,future in enumerate(concurrent.futures.as_completed(futures),1):
            row,event,p=future.result()
            if event is None:deferred.append(row['id']);continue
            events.append(event)
            with fetcher.lock:state['sources'][row['id']]=p
            if event['class'] in ACTIONABLE or event.get('initial_keyword_hits') or (event.get('baseline_established') and any(event.get('keyword_flags',{}).values())):
                item=queue_item(row,event)
                known=next((q for q in queue['open'] if q['id']==item['id']),None)
                if known:known['last_seen_at']=item['detected_at'];known['needs_new_url']=item['needs_new_url']
                elif not any(q['id']==item['id'] for q in archive['closed']):queue['open'].append(item)
            if n%10==0 or n==len(due):
                print(f"Checked {n}/{len(due)} Tier {','.join(tiers)} sources; last={event['class']}",flush=True)
            with fetcher.lock:write(state_dir/'state.json',metadata_state(state) if metadata_only else state)
            write(state_dir/'queue.json',queue)
    queue['open'].sort(key=priority);write(state_dir/'state.json',metadata_state(state) if metadata_only else state);write(state_dir/'queue.json',queue);write(state_dir/'archive.json',archive)
    if not metadata_only:render_queue(queue,state_dir/'queue.md')
    result={'run_at':iso(now),'tiers':tiers,'selected':len(candidates),'checked':len(events),'recovered_checkpoints':recovered,'skipped_not_due':len(skipped),'deferred_for_budget':len(deferred),'duration_seconds':round(time.monotonic()-started,2),'classes':dict(Counter(e['class'] for e in events)),'broken':sum(e['class']=='broken' for e in events),'blocked':sum(e['class']=='blocked' for e in events),'http_requests':fetcher.request_count,'downloaded_bytes':fetcher.bytes,'events':sorted(events,key=lambda e:e['source_url'])}
    result['failure_ratio']=(result['broken']+result['blocked'])/len(events) if events else 0;result['health_failed']=result['failure_ratio']>.2
    write(state_dir/'latest-run.json',result)
    return result


def resolve_item(directory,id,outcome,commit,resolved_at=None):
    if outcome not in ('data updated','no change needed','source replaced'):raise ValueError('Invalid resolution outcome')
    if not re.fullmatch(r'[a-f0-9]{7,40}',commit):raise ValueError('A reviewed commit hash is required')
    if subprocess.run(['git','cat-file','-e',commit+'^{commit}'],cwd=ROOT,capture_output=True).returncode:raise ValueError('Resolution commit does not exist in this checkout')
    queue=read(directory/'queue.json');archive=read(directory/'archive.json') if (directory/'archive.json').exists() else {'schema_version':1,'closed':[]}
    item=next((q for q in queue['open'] if q['id']==id),None)
    if not item:raise ValueError('Open item not found')
    item['resolution']={'resolved_at':resolved_at or iso(utcnow()),'outcome':outcome,'commit':commit}
    queue['open'].remove(item);archive['closed'].append(item);write(directory/'queue.json',queue);write(directory/'archive.json',archive);render_queue(queue,directory/'queue.md')


def review_source(source_id,directory=OUT,now=None,fetcher_factory=Fetcher):
    """Explicit human-triggered check. Full output is written only to ignored local paths."""
    registry=read(OUT/'registry.json');row=next((r for r in registry['urls'] if r['id']==source_id or r['url']==source_id),None)
    if not row:raise ValueError('Source is not in the official registry; add it explicitly first')
    now=now or utcnow();directory=Path(directory)
    with run_lock(directory):
        state=read(directory/'state.json') if (directory/'state.json').exists() else {'schema_version':1,'sources':{},'robots':{}}
        previous=state['sources'].get(row['id'],{});store=Store(directory/'snapshots')
        files=sorted(store.path.glob(row['id']+'-*.txt.gz'),key=lambda p:p.stat().st_mtime)
        local={'snapshots':[p.name for p in files]};old=store.load(local)
        headers={}
        if old is not None and digest(old)==previous.get('fingerprint'):
            headers['_final_url']=previous.get('final_url',row['url'])
            if previous.get('etag'):headers['If-None-Match']=previous['etag']
            if previous.get('last_modified'):headers['If-Modified-Since']=previous['last_modified']
        fetcher=fetcher_factory(registry['urls'],state,now=now)
        write(directory/'attempts'/(row['id']+'.json'),{'attempted_at':iso(now)})
        r=fetcher.fetch(row['url'],headers)
        result={'source_id':row['id'],'source_url':row['url'],'checked_at':iso(now),'local_review_only':True}
        p={**previous,'last_attempt':iso(now)}
        if r.get('class'):
            result.update({'class':r['class'],'error':r.get('error')});p['consecutive_failures']=previous.get('consecutive_failures',0)+int(r['class'] in FAILURES)
        else:
            text=old if r.get('status')==304 else r['text']
            if text is None:raise ValueError('No current local text; a diff cannot be reconstructed from hashes')
            current={**content_metadata(text),'link_fingerprint':r.get('link_fingerprint',previous.get('link_fingerprint'))};p.update(current)
            cls,hits,flipped=classify_metadata(previous,current)
            result.update({'class':cls,'fingerprint':current['fingerprint'],'keyword_flags':current['keyword_flags'],'new_keywords':hits,'flipped_keyword_flags':flipped,'keyword_hits':keyword_hits(text),'diff':compact_diff(old,text) if old is not None else [],'before_snapshot_available':old is not None,'note':'No previous local snapshot: current text only; no before passage is invented.' if old is None else 'Exact local before/after excerpts; no factual data update.'})
            store.keep(row['id'],text,local)
            p.update({'last_success':iso(now),'final_url':r['final_url'],'type':r.get('type',row['content_type']),'language':r.get('language') or row['language'],'consecutive_failures':0,'recovered_without_http_headers':False})
            for name,key in [('etag','etag'),('last-modified','last_modified')]:
                if r.get('headers',{}).get(name):p[key]=r['headers'][name]
        p['last_class']=result['class'];state['sources'][row['id']]=p
        write(directory/'state.json',metadata_state(state));write(directory/'private/reviews'/(row['id']+'.json'),result)
        queue=read(directory/'queue.json') if (directory/'queue.json').exists() else {'schema_version':1,'open':[]}
        if result['class']!='unchanged':
            item=queue_item(row,{**result,'consecutive_failures':p['consecutive_failures']})
            if not any(q['id']==item['id'] for q in queue['open']):queue['open'].append(item)
        write(directory/'queue.json',queue_metadata(queue));render_queue(queue,directory/'queue.md')
        return directory/'private/reviews'/(row['id']+'.json')


def public_summary(registry,state,programs,universities):
    result={'schema_version':1,'records':{'program':{},'university':{}},'explanation':'Monitoring checks sources and flags changes for human review. It never updates admissions data. First baselines cannot establish whether a change predated monitoring.'}
    for owner,records in [('program',programs),('university',universities)]:
        for record in records:
            cited=[r for r in registry['urls'] if any(c['owner']==owner and c['record_id']==record['id'] for c in r['citations'])]
            checked=[state.get('sources',{}).get(r['id'],{}) for r in cited];attempted=[r for r in checked if r.get('last_attempt')]
            date=max((r['last_attempt'] for r in attempted),default=None)
            changed=any(r.get('last_change_detected','')[:10]>=(record.get('last_checked') or '9999-99-99') for r in checked)
            result['records'][owner][record['id']]={'last_checked':date[:10] if date else None,'changes_detected':changed,'checked_sources':len(attempted),'total_sources':len(cited),'failed_sources':sum(r.get('last_class') in FAILURES for r in attempted),'baseline_only':bool(attempted) and not any(r.get('last_change_detected') for r in checked)}
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    fetch=sub.add_parser('run');fetch.add_argument('--tiers',nargs='+',choices=list(INTERVALS),default=['A']);fetch.add_argument('--state-dir',type=Path,default=OUT);fetch.add_argument('--workers',type=int,default=6);fetch.add_argument('--minor-threshold',type=float,default=.02);fetch.add_argument('--max-runtime-minutes',type=float,default=60);fetch.add_argument('--metadata-only',action='store_true',help='Always enabled for CLI monitoring; full text is available only through local review')
    listing=sub.add_parser('list');listing.add_argument('--state-dir',type=Path,default=OUT)
    close=sub.add_parser('resolve');close.add_argument('id');close.add_argument('--outcome',required=True,choices=['data updated','no change needed','source replaced']);close.add_argument('--commit',required=True);close.add_argument('--state-dir',type=Path,default=OUT)
    pub=sub.add_parser('public');pub.add_argument('--state-dir',type=Path,default=OUT)
    review=sub.add_parser('review');review.add_argument('source');review.add_argument('--state-dir',type=Path,default=OUT)
    plan=sub.add_parser('plan');plan.add_argument('--tiers',nargs='+',choices=list(INTERVALS),default=['A']);plan.add_argument('--state-dir',type=Path,default=OUT)
    add=sub.add_parser('add-source');add.add_argument('url');add.add_argument('--university',required=True);add.add_argument('--program',action='append',default=[]);add.add_argument('--field',action='append',required=True);add.add_argument('--type',choices=['HTML','PDF'],required=True);add.add_argument('--language',default='not confirmed');add.add_argument('--tier',choices=list(INTERVALS),default='A');add.add_argument('--official-basis',required=True)
    args=parser.parse_args();registry=read(OUT/'registry.json')
    if args.command=='run':
        if not 0<args.minor_threshold<=1 or not 0<args.max_runtime_minutes<=75:raise ValueError('Threshold must be (0,1], runtime (0,75] minutes')
        with run_lock(args.state_dir):result=run(registry,args.tiers,args.state_dir,max(1,min(args.workers,8)),threshold=args.minor_threshold,max_run_seconds=args.max_runtime_minutes*60,metadata_only=True)
        print(json.dumps({k:v for k,v in result.items() if k!='events'},indent=2));return 2 if result['health_failed'] or result['deferred_for_budget'] else 0
    if args.command=='list':
        queue=read(args.state_dir/'queue.json') if (args.state_dir/'queue.json').exists() else {'open':[]}
        for q in sorted(queue['open'],key=priority):print(f"{q['id']} Tier {q['tier']} {q['change_class']}: {q['source_url']}")
    if args.command=='plan':
        state=read(args.state_dir/'state.json') if (args.state_dir/'state.json').exists() else {'sources':{}};due=[];skipped=[]
        for row in registry['urls']:
            if row['tier'] not in args.tiers:continue
            journal=args.state_dir/'attempts'/(row['id']+'.json');last=max(state['sources'].get(row['id'],{}).get('last_attempt',''),read(journal).get('attempted_at','') if journal.exists() else '')
            p=state['sources'].get(row['id'],{});hold=p.get('retry_after_until') and utcnow()<parse_time(p['retry_after_until'])
            (skipped if hold or (last and utcnow()<next_due(last,row['tier'])) else due).append(row['url'])
        print(json.dumps({'due':len(due),'skipped_not_due':len(skipped),'urls_due':due},indent=2))
    if args.command=='resolve':resolve_item(args.state_dir,args.id,args.outcome,args.commit)
    if args.command=='review':print('Local-only review saved: '+str(review_source(args.source,args.state_dir)))
    if args.command=='public':
        state=read(args.state_dir/'state.json')
        write(OUT/'public-checks.json',public_summary(registry,state,read(ROOT/'research/programs-2027-2028.json'),read(ROOT/'research/universities-2027-2028.json')))
        for row in registry['urls']:
            monitored=state['sources'].get(row['id'],{})
            if monitored.get('fingerprint'):
                row.update({'content_fingerprint':monitored['fingerprint'],'fingerprint_basis':'normalized monitoring text SHA-256','last_monitored':monitored['last_attempt']})
                if not monitored.get('recovered_without_http_headers'):
                    row.update({'last_known_final_url':monitored['final_url'],'language':monitored['language'],'content_type':monitored['type'],'type':'redirect' if monitored['final_url']!=row['url'] else monitored['type']})
        write(OUT/'registry.json',registry)
    if args.command=='add-source':
        universities={u['id']:u for u in read(ROOT/'research/universities-2027-2028.json')};programs={p['id']:p for p in read(ROOT/'research/programs-2027-2028.json')}
        if args.university not in universities or any(id not in programs or programs[id]['university_id']!=args.university for id in args.program):raise ValueError('Unknown university/program combination')
        url=safe_url(args.url);refs=[{'owner':'program','record_id':id,'university_id':args.university,'name':programs[id]['program'],'field':field} for id in args.program for field in args.field]
        if not refs:refs=[{'owner':'university','record_id':args.university,'university_id':args.university,'name':universities[args.university]['name'],'field':field} for field in args.field]
        item={'id':sid(url),'url':url,'university_ids':[args.university],'university_names':[universities[args.university]['name']],'citations':refs,'gates':[{'owner':r['owner'],'record_id':r['record_id'],'field':r['field']} for r in refs] if args.tier=='A' else [],'gated_record_count':len(args.program) or 1,'research_files':['research/monitoring/additional-sources.json'],'source_ids':[],'last_verified':None,'content_fingerprint':None,'fingerprint_basis':'not yet monitored','last_known_final_url':url,'type':args.type,'content_type':args.type,'language':args.language,'tier':args.tier,'official_basis':args.official_basis}
        path=OUT/'additional-sources.json';extra=read(path) if path.exists() else [];extra=[r for r in extra if r['url']!=url]+[item];write(path,extra)
        import monitor_registry
        monitor_registry.build();print('Source added for monitoring only; no admissions field approved.')
    return 0


if __name__=='__main__':raise SystemExit(main())
