"""Bounded Actions artifact state; commits only to the dedicated monitor branch."""
import argparse
import io
import json
import os
import subprocess
import zipfile
from pathlib import Path
import requests
from monitor_registry import OUT,ROOT,read,write

BRANCH='monitoring/source-checks'
PROTECTED={'master','main','production','research/final-2027-2028-refresh'}
PUBLICATIONS=['research/monitoring/registry.json','research/monitoring/queue.json','research/monitoring/archive.json','research/monitoring/public-checks.json','research/monitoring/state-index.json','research/monitoring/latest-run-summary.json','vercel.json']
ARTIFACT='official-source-monitor-state'
MAX_ARCHIVE=160*1024*1024


def git(*args,check=True,env=None):return subprocess.run(['git',*args],cwd=ROOT,check=check,capture_output=True,text=True,env=env)


def restore():
    # Restore reviewed queue resolutions from the branch even if artifacts expired.
    ref='refs/remotes/origin/'+BRANCH
    git('fetch','origin',f'refs/heads/{BRANCH}:{ref}',check=False)
    for target in PUBLICATIONS:
        if not target.startswith('research/monitoring/') or target.endswith('registry.json'):continue
        r=git('show',ref+':'+target,check=False)
        if not r.returncode:(ROOT/target).write_text(r.stdout,encoding='utf-8')
    if (OUT/'state-index.json').exists():write(OUT/'state.json',read(OUT/'state-index.json'))
    token=os.environ.get('GITHUB_TOKEN');repo=os.environ.get('GITHUB_REPOSITORY')
    if not token or not repo:raise RuntimeError('Actions authentication required for artifact restore')
    headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
    response=requests.get(f'https://api.github.com/repos/{repo}/actions/artifacts',params={'name':ARTIFACT,'per_page':30},headers=headers,timeout=30);response.raise_for_status()
    artifacts=[a for a in response.json().get('artifacts',[]) if not a['expired'] and a.get('workflow_run',{}).get('head_repository_id')==a.get('workflow_run',{}).get('repository_id')]
    if not artifacts:
        print('No retained artifact: source cadence metadata and archived resolutions remain on the monitoring branch. Missing text establishes a new baseline.');return
    artifact=artifacts[0]
    if artifact['size_in_bytes']>MAX_ARCHIVE:raise RuntimeError('Monitoring artifact exceeds compressed size limit')
    data=requests.get(artifact['archive_download_url'],headers=headers,timeout=120);data.raise_for_status()
    archive=zipfile.ZipFile(io.BytesIO(data.content));infos=archive.infolist()
    if len(infos)>5000 or sum(i.file_size for i in infos)>256*1024*1024:raise RuntimeError('Artifact exceeds extraction limits')
    # Preserve queue resolutions read from the branch; the artifact supplies state/text.
    allowed={'state.json','latest-run.json','queue.json','archive.json'}
    for item in infos:
        path=Path(item.filename)
        if path.is_absolute() or '..' in path.parts:raise RuntimeError('Unsafe artifact path')
        if item.is_dir():continue
        if path.as_posix() not in allowed and (not path.parts or path.parts[0] not in ('attempts','results')):raise RuntimeError('Unexpected content in metadata-only artifact')
        payload=json.loads(archive.read(item))
        from monitor_privacy import validate_value
        validate_value(payload,path.as_posix())
        if path.name in ('queue.json','archive.json') and (OUT/path).exists():continue
        write(OUT/path,payload)
    print('Restored bounded monitoring state artifact; no admissions data imported.')


def prepare_publication():
    state=read(OUT/'state.json')
    import source_monitor as M
    from monitor_privacy import validate_value
    safe=M.metadata_state(state);validate_value(safe)
    write(OUT/'state-index.json',safe)
    run=read(OUT/'latest-run.json');write(OUT/'latest-run-summary.json',{k:v for k,v in run.items() if k!='events'})
    export=OUT/'export';export.mkdir(exist_ok=True)
    write(export/'state.json',safe)
    write(export/'latest-run.json',{**{k:v for k,v in run.items() if k!='events'},'events':[M.metadata_event(e) for e in run['events']]})
    for name in ('queue.json','archive.json'):write(export/name,M.queue_metadata(read(OUT/name)))
    for folder in ('attempts','results'):
        for path in (OUT/folder).glob('*.json'):
            data=read(path)
            if folder=='results':data={'event':M.metadata_event(data['event']),'state':{k:v for k,v in data['state'].items() if k in M.SOURCE_KEYS}}
            validate_value(data,path.name);write(export/folder/path.name,data)
    validate_export(export)
    if sum(p.stat().st_size for p in export.rglob('*') if p.is_file())>32*1024*1024:raise RuntimeError('Metadata export exceeds 32 MiB budget')


def validate_export(export):
    from monitor_privacy import validate_value
    for path in export.rglob('*'):
        if not path.is_file():continue
        relative=path.relative_to(export)
        if path.suffix!='.json' or (len(relative.parts)>1 and relative.parts[0] not in ('attempts','results')):raise RuntimeError('Non-metadata artifact member: '+str(relative))
        validate_value(read(path),str(relative))


def publish():
    if BRANCH in PROTECTED or not BRANCH.startswith('monitoring/'):raise RuntimeError('Unsafe monitoring branch')
    prepare_publication()
    from monitor_privacy import validate_tracked
    validate_tracked()
    previous=git('rev-parse','--verify','refs/remotes/origin/'+BRANCH,check=False)
    parent=previous.stdout.strip() if previous.returncode==0 else git('rev-parse','HEAD').stdout.strip()
    index=ROOT/'tmp/monitor-ci-index';index.parent.mkdir(exist_ok=True);index.unlink(missing_ok=True)
    env={**os.environ,'GIT_INDEX_FILE':str(index),'GIT_AUTHOR_NAME':'source-monitor[bot]','GIT_AUTHOR_EMAIL':'source-monitor@users.noreply.github.com','GIT_COMMITTER_NAME':'source-monitor[bot]','GIT_COMMITTER_EMAIL':'source-monitor@users.noreply.github.com'}
    git('read-tree',parent,env=env)
    # Include the deployment guard but never website/dataset implementation changes.
    guard=read(ROOT/'vercel.json')
    if guard.get('git',{}).get('deploymentEnabled',{}).get(BRANCH) is not False:raise RuntimeError('Vercel monitoring-branch deployment guard is missing')
    git('add','-f','--',*PUBLICATIONS,env=env)
    changed=git('diff','--cached','--name-only',parent,env=env).stdout.splitlines()
    if set(changed)-set(PUBLICATIONS):raise RuntimeError('Monitoring publication contains an unexpected file')
    if not changed:print('No monitoring metadata changed.');return
    tree=git('write-tree',env=env).stdout.strip()
    commit=git('commit-tree',tree,'-p',parent,'-m','Queue official source checks [skip ci]',env=env).stdout.strip()
    git('push','origin',commit+':refs/heads/'+BRANCH)
    print('Published monitoring metadata only to '+BRANCH+' at '+commit)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['restore','prepare','publish']);args=parser.parse_args()
    {'restore':restore,'prepare':prepare_publication,'publish':publish}[args.command]()
