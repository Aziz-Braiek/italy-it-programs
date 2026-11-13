"""Allowlisted public check metadata. Queue, snapshots and diffs never enter dist."""
import json
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'research/monitoring/public-checks.json'
ALLOWED={'last_checked','changes_detected','checked_sources','total_sources','failed_sources','baseline_only'}


def load():
    if not PATH.exists():return {'schema_version':1,'records':{'program':{},'university':{}}}
    data=json.loads(PATH.read_text(encoding='utf-8'))
    for owner in ('program','university'):
        for record in data['records'][owner].values():
            if set(record)-ALLOWED:raise ValueError('Private monitoring data in public metadata')
    return data


def copy_public(destination):
    destination.write_text(json.dumps(load(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def render(data,owner,record_id):
    check=data.get('records',{}).get(owner,{}).get(record_id,{})
    date=check.get('last_checked') or 'Not checked yet';changed='yes' if check.get('changes_detected') else 'no'
    note=f"{check.get('checked_sources',0)} of {check.get('total_sources',0)} source dependencies checked; {check.get('failed_sources',0)} checks failed or were blocked."
    if check.get('baseline_only'):note+=' First baseline; changes before monitoring cannot be assessed.'
    elif not check.get('last_checked'):note+=' No monitoring baseline is available.'
    return f'<p class="last-checked source-checks">Official pages last checked: <time>{escape(date)}</time>. Changes detected since last review: <strong>{changed}</strong>. <small>{escape(note)} Monitoring flags changes; nothing updates automatically.</small></p>'
