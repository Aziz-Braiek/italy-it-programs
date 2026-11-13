"""Prevent monitoring page content from entering Git, CI exports or the site."""
import re
import subprocess
from pathlib import Path
from monitor_registry import ROOT,OUT,read

CONTENT_KEYS={'text','body','full_text','normalized_text','snapshot_text','diff','diff_excerpt','passage','passages','exact_passage','initial_keyword_hits','removed_passage','added_passage','context'}
PRIVATE_NAMES={'queue.md','report.md','baseline-results.json','top-priority-items.json','awaiting-keyword-observations.json'}
METADATA_FILES={'registry.json','registry-summary.json','registry-warnings.json','queue.json','archive.json','public-checks.json','baseline-summary.json','state-index.json','latest-run-summary.json','production-comparison.json','history-check.json','additional-sources.json','awaiting-keyword-flags.json'}


def validate_value(value,location='metadata'):
    if isinstance(value,dict):
        for key,item in value.items():
            if key in CONTENT_KEYS:raise ValueError(f'Content-bearing monitoring key is forbidden: {location}/{key}')
            if key=='keyword_flags' and (not isinstance(item,dict) or any(not isinstance(v,bool) for v in item.values())):raise ValueError('Keyword flags must be boolean, never passages')
            validate_value(item,location+'/'+key)
    elif isinstance(value,list):
        for i,item in enumerate(value):validate_value(item,location+'/'+str(i))


def validate_tracked(paths=None):
    if paths is None:paths=subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines()
    for name in paths:
        path=Path(name);parts=path.parts
        if name.startswith('research/monitoring/'):
            if any(part in ('private','snapshots','results','attempts','export') for part in parts) or path.name in PRIVATE_NAMES or path.suffix in ('.gz','.zip'):
                raise ValueError('Content-bearing monitoring file is tracked: '+name)
            if path.suffix=='.json' and path.name not in METADATA_FILES:raise ValueError('Unrecognized monitoring output is tracked: '+name)
            if path.suffix=='.json':validate_value(read(ROOT/path),name)
            if path.suffix=='.md' and re.search(r'^\s*>|```text',(ROOT/path).read_text(encoding='utf-8'),re.M):raise ValueError('Quoted monitoring content is tracked: '+name)
        elif path.name.endswith('.txt.gz') or ('snapshots' in parts and path.suffix in ('.txt','.html','.pdf')):
            raise ValueError('A normalized source snapshot is tracked: '+name)
    for name in METADATA_FILES:
        if (OUT/name).exists():validate_value(read(OUT/name),name)


def validate_history():
    commits=subprocess.check_output(['git','rev-list','900315e..HEAD'],cwd=ROOT,text=True).splitlines()
    for commit in commits:
        paths=subprocess.check_output(['git','diff-tree','--no-commit-id','--name-only','-r',commit],cwd=ROOT,text=True).splitlines()
        for name in paths:
            if not name.startswith('research/monitoring/'):continue
            p=Path(name)
            if any(part in ('private','snapshots','results','attempts','export') for part in p.parts) or p.name in PRIVATE_NAMES or p.suffix in ('.gz','.zip'):raise ValueError('Content-bearing monitoring file exists in branch history: '+name)
            content=subprocess.run(['git','show',commit+':'+name],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
            if not content.returncode and p.suffix=='.json':
                import json
                validate_value(json.loads(content.stdout),commit+':'+name)
    return len(commits)


if __name__=='__main__':
    validate_tracked();validate_history();print('Monitoring privacy lint passed: no tracked monitoring snapshots, passages or diffs in this round or its commits.')
