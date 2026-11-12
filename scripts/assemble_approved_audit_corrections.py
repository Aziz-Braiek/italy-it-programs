"""Compile explicitly reviewed, hash-pinned batch proposals into exact patches.

Approval is a manual research decision in review-approvals.json, never a consequence
of successful HTTP requests, field matches or a passing software test.
"""
import copy
import hashlib
import json
from pathlib import Path
from build_independent_audit import BASE, OUT, baseline, lookup, pending


def assemble():
    approvals=json.loads((OUT/"review-approvals.json").read_text(encoding="utf-8"))
    maps={kind:{r["id"]:r for r in baseline(name)} for kind,name in [("program","programs-2027-2028.json"),("university","universities-2027-2028.json"),("source","sources.json")]}
    plan={"baseline_commit":BASE,"as_of":approvals["as_of"],"review_status":approvals["review_status"],"approval_method":approvals["method"],"approved_batch_hashes":[],"new_sources":[],"patches":[],"checked_records":[]}
    seen=set();source_map={};checked=set()
    for approval in approvals["batches"]:
        path=OUT/approval["file"]
        assert hashlib.sha256(path.read_bytes()).hexdigest()==approval["sha256"], "Reviewed batch changed: "+path.name
        plan["approved_batch_hashes"].append(approval)
        batch=json.loads(path.read_text(encoding="utf-8"))
        for s in batch.get("additional_official_sources",[])+batch.get("additional_source_records",[]):
            assert all(k in s for k in ["id","university_id","title","url","source_type","accessed_at","cycle","evidence","supports"]), "Incomplete official source record"
            record=copy.deepcopy(s)
            if record["cycle"]=="2027/28":record["cycle"]="2027-2028"
            if record["id"] in maps["source"]:raise ValueError("New source duplicates baseline ID")
            if record["id"] in source_map:assert source_map[record["id"]]==record, "Conflicting new source ID"
            source_map[record["id"]]=record
        for c in batch.get("confirmed_corrections",[]):
            kind=c.get("record_type") or ("university" if c.get("university_id") and not c.get("program_id") else "program")
            rid=c.get("record_id") or c.get(kind+"_id")
            path=c["field_path"]
            key=(kind,rid,path)
            assert key not in seen, "Duplicate approved patch: "+str(key)
            seen.add(key)
            exists,old=lookup(maps[kind][rid],path)
            assert old==c.get("existing_value"), "Incorrect baseline: "+str(key)
            after=c["replacement_value"] if "replacement_value" in c else c["official_value"]
            # Root's fully wrapped values are explicit; other batches must provide
            # complete replacements, rather than ambiguous descriptions of a merge.
            if approval["file"]!="batch-pisa-messina.json":assert "replacement_value" in c, "Missing exact replacement"
            assert c.get("source_urls") and c.get("academic_year") and c.get("checked_at"), "Missing correction provenance"
            fid="F-"+hashlib.sha256("/".join(key).encode()).hexdigest()[:12]
            plan["patches"].append({"record_type":kind,"record_id":rid,"field_path":path,"before_exists":exists,"before":old,"after":copy.deepcopy(after),"finding_id":fid,"verification_outcome":"CONFIRMED","source_urls":c["source_urls"],"academic_year":c["academic_year"],"checked_at":c["checked_at"],"reason":c.get("reason",c.get("evidence_summary")),"batch_file":approval["file"]})
        for kind in ["program","university"]:
            for r in batch.get(kind+"_reviews",[]):
                if any(pending(c) for c in r.get("comparisons",[])):continue
                rid=r[kind+"_id"]
                if (kind,rid) not in checked:
                    plan["checked_records"].append({"record_type":kind,"record_id":rid,"checked_at":r["checked_at"]});checked.add((kind,rid))
    plan["new_sources"]=list(source_map.values())
    source_ids=set(maps["source"])|set(source_map)
    def verify_ids(value):
        if isinstance(value,dict):
            if "source_ids" in value:assert set(value["source_ids"])<=source_ids, "Unknown source IDs: "+str(set(value["source_ids"])-source_ids)
            for child in value.values():verify_ids(child)
        elif isinstance(value,list):
            for child in value:verify_ids(child)
    for patch in plan["patches"]:
        verify_ids(patch["after"])
        if patch["field_path"]=="source_ids":assert set(patch["after"])<=source_ids
    (OUT/"approved-corrections.json").write_text(json.dumps(plan,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"patches":len(plan["patches"]),"new_sources":len(plan["new_sources"]),"checked_records":len(plan["checked_records"])},indent=2))


if __name__=="__main__":assemble()
