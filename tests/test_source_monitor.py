"""Recorded offline fixtures only. No request goes to a university server."""
import copy
import json
import sys
import tempfile
import concurrent.futures
import unittest
from datetime import datetime,timedelta,timezone
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
import monitor_registry as R
import source_monitor as M
FIX=ROOT/'tests/fixtures/monitoring'
NOW=datetime(2026,11,13,12,tzinfo=timezone.utc)


class Clock:
    def __init__(self):self.value=0
    def now(self):return self.value
    def sleep(self,duration):self.value+=duration


class Response:
    def __init__(self,row):self.status_code=row['status'];self.headers=row.get('headers',{});self.body=(FIX/row['fixture']).read_bytes() if row.get('fixture') else row.get('body','').encode()
    def iter_content(self,size):yield self.body
    def close(self):pass


def source(path='/page'):
    url='https://university.example'+path
    return {'id':R.sid(url),'url':url,'tier':'A','type':'HTML','content_type':'HTML','language':'en','last_known_final_url':url,'university_ids':['fixture'],'university_names':['Fixture University'],'citations':[{'owner':'program','record_id':'fixture-001','university_id':'fixture','field':'deadline','name':'Fixture programme'}],'gates':[{'owner':'program','record_id':'fixture-001','field':'deadline'}]}


class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.net_patch=patch('requests.get',side_effect=AssertionError('Live network forbidden in tests'));self.net_patch.start();self.addCleanup(self.net_patch.stop)
        self.responses=R.read(FIX/'responses.json');self.clock=Clock();self.calls=[]
    def request(self,url,**kwargs):
        self.calls.append((url,self.clock.now(),kwargs))
        if url not in self.responses:raise M.requests.ConnectionError('Fixture DNS failure')
        return Response(self.responses[url])
    def fetcher(self,registry,state,**kwargs):return M.Fetcher(registry,state,request=self.request,gate=M.HostGate(self.clock.now,self.clock.sleep),**kwargs)
    def text(self,name):return M.extract((FIX/name).read_bytes(),'text/html')[0]

    def test_boilerplate_fingerprint_stability(self):
        self.assertEqual(self.text('page-v1.html'),self.text('page-boilerplate.html'))
        self.assertEqual(M.classify(self.text('page-v1.html'),self.text('page-boilerplate.html'))[0],'unchanged')
    def test_small_numeric_fee_edit_is_substantive(self):
        cls,hits,diff=M.classify(self.text('page-v1.html'),self.text('page-changed.html'))
        self.assertEqual(cls,'substantive');self.assertIn('18000',diff[0]['removed']);self.assertIn('19000',diff[0]['added']);self.assertTrue(diff[0]['context'])
    def test_new_cycle_keyword_and_minor_threshold(self):
        cls,hits,_=M.classify(self.text('page-v1.html'),self.text('page-new-cycle.html'));self.assertEqual(cls,'new keyword hit');self.assertIn('2027/28',hits)
        self.assertEqual(M.classify('word '*200+'Hello','word '*200+'Hi')[0],'minor')
    def test_redirects_are_followed_and_logged_but_target_fetched_once(self):
        f=self.fetcher([source('/moved'),source()],{},now=NOW)
        moved=f.fetch(source('/moved')['url']);direct=f.fetch(source()['url'])
        self.assertEqual(moved['final_url'],source()['url']);self.assertEqual(len(moved['redirects']),1);self.assertEqual(moved['text'],direct['text'])
        self.assertEqual(sum(u==source()['url'] for u,_,_ in self.calls),1)
    def test_robots_rate_and_user_agent(self):
        f=self.fetcher([source(),source('/private/a')],{},now=NOW)
        f.fetch(source()['url']);result=f.fetch(source('/private/a')['url'])
        self.assertEqual(result['class'],'broken');self.assertIn('robots disallow',result['error']);self.assertFalse(any('/private/' in u for u,_,_ in self.calls))
        self.assertGreaterEqual(self.calls[1][1]-self.calls[0][1],3)
        for _,_,args in self.calls:self.assertEqual(args['headers']['User-Agent'],M.USER_AGENT)
        rules=M.RobotsRules((FIX/'robots.txt').read_text());self.assertFalse(rules.allows('https://x.it/a?download=private'));self.assertTrue(rules.allows('https://x.it/private/public/a'))
    def test_robots_failure_and_wall_fail_closed_even_when_cached(self):
        self.responses['https://university.example/robots.txt']={'status':200,'body':'<html>CAPTCHA</html>'}
        f=self.fetcher([source()],{},now=NOW)
        for _ in range(2):
            with self.assertRaises(ValueError):f.fetch(source()['url'])
        self.assertFalse(any(u.endswith('/page') for u,_,_ in self.calls))
    def test_broken_blocked_dns_timeout_and_retry_after(self):
        f=self.fetcher([source('/gone'),source('/wall'),source('/busy'),source('/dns'),source('/login')],{},now=NOW)
        self.assertEqual(f.fetch(source('/gone')['url'])['class'],'broken')
        self.assertEqual(f.fetch(source('/wall')['url'])['class'],'blocked')
        self.assertEqual(f.fetch(source('/login')['url'])['class'],'blocked');self.assertFalse(any(u.endswith('/login') for u,_,_ in self.calls))
        r=f.fetch(source('/busy')['url']);self.assertIn('deferred',r['error']);self.assertEqual(sum(u.endswith('/busy') for u,_,_ in self.calls),1)
        with self.assertRaises(M.requests.ConnectionError):f.fetch(source('/dns')['url'])
        def timeout(*args,**kwargs):raise M.requests.Timeout('recorded timeout')
        f=self.fetcher([source()],{},now=NOW);f.request=timeout
        with self.assertRaises(M.requests.Timeout):f.fetch(source()['url'])
    def test_pdf_fixture_text_extraction(self):
        text,lang,kind=M.extract((FIX/'rules.pdf').read_bytes(),'application/pdf');self.assertEqual(kind,'PDF');self.assertIn('2027/28',text);self.assertIn('15 November',text)
    def test_cache_304_schedule_and_two_snapshot_retention(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp);registry={'urls':[source()]}
            first=M.run(registry,['A'],directory,now=NOW,fetcher_factory=self.fetcher);self.assertEqual(first['checked'],1)
            skipped=M.run(registry,['A'],directory,now=NOW+timedelta(days=1),fetcher_factory=self.fetcher);self.assertEqual(skipped['checked'],0);self.assertEqual(skipped['skipped_not_due'],1)
            self.responses[source()['url']]={'status':304}
            second=M.run(registry,['A'],directory,now=NOW+timedelta(days=7),fetcher_factory=self.fetcher);self.assertEqual(second['classes'],{'unchanged':1})
            self.assertEqual([args['headers'] for u,_,args in self.calls if u==source()['url']][-1]['If-None-Match'],'"fixture-v1"')
            self.responses[source()['url']]={'status':200,'fixture':'page-changed.html'};M.run(registry,['A'],directory,now=NOW+timedelta(days=14),fetcher_factory=self.fetcher)
            self.responses[source()['url']]={'status':200,'fixture':'page-new-cycle.html'};M.run(registry,['A'],directory,now=NOW+timedelta(days=21),fetcher_factory=self.fetcher)
            self.assertEqual(len(list((directory/'snapshots').glob('*.gz'))),2)
    def test_queue_create_resolve_archive_and_three_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp);registry={'urls':[source('/gone')]}
            for week in range(3):r=M.run(registry,['A'],directory,now=NOW+timedelta(days=week*7),fetcher_factory=self.fetcher)
            self.assertTrue(r['health_failed']);q=R.read(directory/'queue.json');self.assertEqual(len(q['open']),1);self.assertTrue(q['open'][0]['needs_new_url'])
            M.resolve_item(directory,q['open'][0]['id'],'no change needed','900315e',M.iso(NOW));self.assertEqual(R.read(directory/'queue.json')['open'],[])
            closed=R.read(directory/'archive.json')['closed'];self.assertEqual(closed[0]['resolution']['commit'],'900315e');self.assertIn('resolved_at',closed[0]['resolution'])
    def test_public_monitoring_date_is_not_review_date_or_private_content(self):
        r=source();state={'sources':{r['id']:{'last_attempt':M.iso(NOW),'last_change_detected':M.iso(NOW),'last_class':'substantive'}}}
        p={'id':'fixture-001','last_checked':'2026-11-01'};data=M.public_summary({'urls':[r]},state,[p],[])
        self.assertEqual(data['records']['program'][p['id']]['last_checked'],'2026-11-13');self.assertTrue(data['records']['program'][p['id']]['changes_detected']);self.assertEqual(p['last_checked'],'2026-11-01')
        self.assertFalse(any(s in json.dumps(data) for s in ['diff_excerpt','source_url','snapshots','queue']))
    def test_registry_coverage_and_missing_source_guard(self):
        u=R.read(ROOT/'research/universities-2027-2028.json');p=R.read(ROOT/'research/programs-2027-2028.json');reg=R.read(R.OUT/'registry.json');R.validate(u,p,reg)
        self.assertEqual(len(reg['urls']),len({r['url'] for r in reg['urls']}))
        awaiting={x['id'] for x in p if x['overall_status']=='REQUIRES_VERIFICATION'}
        gated={c['record_id'] for r in reg['urls'] if r['tier']=='A' for c in r['gates'] if c['owner']=='program'}
        self.assertTrue(awaiting<=gated)
        p=copy.deepcopy(p);p[0]['facts']['monitor_guard']={'value':'https://www.polimi.it/new-official-test-url'}
        with self.assertRaises(ValueError):R.validate(u,p,reg)

    def test_windows_atomic_writer_retries_and_checkpoints_recover(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'write.json';original=Path.replace;attempts=[]
            def transient(path,target):
                attempts.append(path)
                if len(attempts)<3:raise PermissionError('Recorded Windows reader lock')
                return original(path,target)
            with patch.object(Path,'replace',transient),patch.object(R.time,'sleep'):
                R.write(p,{'saved':True})
            self.assertEqual(R.read(p),{'saved':True});self.assertEqual(len(attempts),3)
            directory=Path(tmp);registry={'urls':[source()]}
            M.run(registry,['A'],directory,now=NOW,fetcher_factory=self.fetcher)
            (directory/'state.json').unlink();(directory/'queue.json').unlink()
            self.calls=[];r=M.run(registry,['A'],directory,now=NOW+timedelta(hours=1),fetcher_factory=self.fetcher)
            self.assertEqual(r['checked'],0);self.assertEqual(r['recovered_checkpoints'],1);self.assertEqual(self.calls,[])
            self.assertEqual(len(R.read(directory/'queue.json')['open']),1)

    def test_host_concurrency_one_and_two_seconds_after_response(self):
        starts=[];gate=M.HostGate(self.clock.now,self.clock.sleep)
        def request(i):
            def body():starts.append(self.clock.now());self.clock.sleep(.5)
            gate.run('https://university.example/'+str(i),body)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(request,range(8)))
        self.assertEqual(starts,sorted(starts));self.assertTrue(all(b-a>=2.5 for a,b in zip(starts,starts[1:])))

    def test_budget_defers_without_reserving_or_requesting(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=M.run({'urls':[source()]},['A'],tmp,now=NOW,fetcher_factory=self.fetcher,max_run_seconds=0)
            self.assertEqual(r['deferred_for_budget'],1);self.assertEqual(self.calls,[]);self.assertEqual(list((Path(tmp)/'attempts').glob('*.json')),[])

    def test_workflow_publishes_only_monitor_branch_and_blocks_vercel(self):
        import monitor_ci as C
        self.assertNotIn(C.BRANCH,C.PROTECTED);self.assertEqual(C.BRANCH,'monitoring/source-checks')
        self.assertTrue(all(p.startswith('research/monitoring/') or p=='vercel.json' for p in C.PUBLICATIONS))
        self.assertFalse(any('programs-2027' in p or 'universities-2027' in p for p in C.PUBLICATIONS))
        config=R.read(ROOT/'vercel.json');self.assertIs(config['git']['deploymentEnabled'][C.BRANCH],False)
        workflow=(ROOT/'.github/workflows/official-source-monitor.yml').read_text()
        self.assertNotIn('pull_request_target',workflow);self.assertNotIn('vercel --prod',workflow)
        for cron in ['17 5 * * 1','31 5 1 * *','43 5 1 1,4,7,10 *']:self.assertIn(cron,workflow)
        self.assertIn('monitor_ci.py publish',workflow);self.assertIn('Fail loudly',workflow)

    def test_public_build_has_dates_but_no_private_monitor_files(self):
        import monitor_public as P
        text=P.render({'records':{'program':{'fixture-001':{'last_checked':'2026-11-13','changes_detected':False,'checked_sources':1,'total_sources':2,'failed_sources':0,'baseline_only':True}}}},'program','fixture-001')
        self.assertIn('Official pages last checked:',text);self.assertIn('2026-11-13',text);self.assertNotIn('Last reviewed:',text)
        self.assertFalse((ROOT/'dist/data/monitoring/queue.json').exists())

    def test_metadata_only_runs_never_store_text_and_reuse_304_without_snapshot(self):
        from monitor_privacy import validate_value
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp);registry={'urls':[source()]}
            first=M.run(registry,['A'],directory,now=NOW,fetcher_factory=self.fetcher,metadata_only=True)
            self.assertFalse((directory/'snapshots').exists());self.assertFalse((directory/'queue.md').exists())
            for path in directory.rglob('*.json'):
                validate_value(R.read(path));self.assertNotIn('Applicants submit',path.read_text(encoding='utf-8'))
            self.responses[source()['url']]={'status':304}
            second=M.run(registry,['A'],directory,now=NOW+timedelta(days=7),fetcher_factory=self.fetcher,metadata_only=True)
            self.assertEqual(second['classes'],{'unchanged':1})
            self.responses[source()['url']]={'status':200,'fixture':'page-new-cycle.html'}
            changed=M.run(registry,['A'],directory,now=NOW+timedelta(days=14),fetcher_factory=self.fetcher,metadata_only=True)
            event=changed['events'][0];self.assertEqual(event['class'],'new keyword hit');self.assertTrue(event['flipped_keyword_flags']['2027/28']['after'])
            self.assertNotIn('diff',event);self.assertNotIn('initial_keyword_hits',event)
            for path in directory.rglob('*.json'):validate_value(R.read(path))

    def test_explicit_local_review_keeps_diff_only_in_ignored_paths(self):
        from monitor_privacy import validate_value
        with tempfile.TemporaryDirectory() as tmp:
            directory=Path(tmp);R.write(directory/'registry.json',{'urls':[source()]})
            with patch.object(M,'OUT',directory):
                first=M.review_source(source()['id'],directory,now=NOW,fetcher_factory=self.fetcher)
                self.assertFalse(R.read(first)['before_snapshot_available'])
                self.responses[source()['url']]={'status':200,'fixture':'page-changed.html'}
                second=M.review_source(source()['id'],directory,now=NOW+timedelta(hours=1),fetcher_factory=self.fetcher)
            review=R.read(second);self.assertTrue(review['before_snapshot_available']);self.assertIn('19000',review['diff'][0]['added']);self.assertIn('18000',review['diff'][0]['removed'])
            self.assertIn('private',second.parts);validate_value(R.read(directory/'queue.json'));validate_value(R.read(directory/'state.json'))
            self.assertTrue((directory/'queue.md').exists())

    def test_content_lint_rejects_tracked_reviews_and_non_boolean_flags(self):
        import monitor_privacy as P
        for path in ['research/monitoring/queue.md','research/monitoring/private/reviews/source.json','research/monitoring/snapshots/source.txt.gz','research/monitoring/baseline-results.json']:
            with self.assertRaises(ValueError):P.validate_tracked([path])
        for data in [{'diff_excerpt':['official words']},{'keyword_flags':{'2027/28':'a passage'}},{'normalized_text':'page text'}]:
            with self.assertRaises(ValueError):P.validate_value(data)

    def test_calendar_cadence_and_run_lock(self):
        self.assertEqual(M.next_due('2027-02-01T00:00:00+00:00','B').date().isoformat(),'2027-03-01')
        with tempfile.TemporaryDirectory() as tmp:
            with M.run_lock(Path(tmp)):
                with self.assertRaises(RuntimeError):
                    with M.run_lock(Path(tmp)):pass

    def test_robots_304_reuses_parsed_policy_without_stored_text(self):
        policy=M.RobotsRules((FIX/'robots.txt').read_text())
        state={'robots':{'https://university.example':{'checked_at':M.iso(NOW-timedelta(days=8)),'status':200,'etag':'"robots-v1"','policy':{'rules':policy.rules,'delay_seconds':policy.delay}}}}
        self.responses['https://university.example/robots.txt']={'status':304}
        f=self.fetcher([source()],state,now=NOW);r=f.fetch(source()['url']);self.assertIn('Master admissions',r['text'])
        self.assertNotIn('text',state['robots']['https://university.example'])
        self.assertEqual(self.calls[0][2]['headers']['If-None-Match'],'"robots-v1"')

    def test_artifact_export_rejects_content_even_if_not_tracked(self):
        from monitor_ci import validate_export
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);R.write(p/'state.json',{'schema_version':1,'sources':{}});validate_export(p)
            (p/'snapshot.txt').write_text('must not upload')
            with self.assertRaises(RuntimeError):validate_export(p)
            (p/'snapshot.txt').unlink();R.write(p/'state.json',{'normalized_text':'must not upload'})
            with self.assertRaises(ValueError):validate_export(p)

    def test_link_target_change_is_detected_from_hashes_without_passages(self):
        a=b'<main><p>Official applications and requirements are listed here.</p><a href="/call-2026.pdf">Call</a></main>'
        b=a.replace(b'2026',b'2027')
        ta,_,_,la=M.extract(a,'text/html',details=True);tb,_,_,lb=M.extract(b,'text/html',details=True)
        self.assertEqual(ta,tb);self.assertNotEqual(la,lb)
        self.assertEqual(M.classify_metadata({**M.content_metadata(ta),'link_fingerprint':la},{**M.content_metadata(tb),'link_fingerprint':lb})[0],'substantive')


if __name__=='__main__':unittest.main()
