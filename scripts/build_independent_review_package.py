"""Package the factual audit and corrected data for a human reviewer."""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"research/independent-audit-2026-11"


def build():
    ledger=json.loads((AUDIT/"review-ledger.json").read_text(encoding="utf-8"))
    names=["programs-2027-2028.json","universities-2027-2028.json","sources.json","coverage-report.json","2027-2028-final-report.md"]
    files=[(ROOT/"research"/name,"data/"+name) for name in names]
    names=["review-ledger.json","findings.json","correction-report.md","approved-corrections.json","source-capture-index.json"]
    files += [(AUDIT/name,"audit/"+name) for name in names]
    for name in ["README.md","release-verification.json"]:
        if (AUDIT/name).exists():files.append((AUDIT/name,"audit/"+name))
    manifest={"baseline_commit":"c3af9dc","audit_state":ledger["metadata"]["audit_state"],"counts":ledger["metadata"]["counts"],"files":[{"path":name,"bytes":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()} for path,name in files]}
    dest=ROOT/"review-package/independent-audit-review.zip"
    dest.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(dest,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path,name in files:archive.write(path,name)
        archive.writestr("manifest.json",json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
        archive.writestr("README.md","# Independent Italy tracker audit\n\nStart with audit/correction-report.md. The complete comparison ledger covers stable IDs, original values, official values, URLs, dates and academic years. findings.json separates discrepancies, conflicts and unpublished fields. approved-corrections.json lists the exact implemented patches. Data files contain the resulting research snapshot.\n\nA completed review outcome does not mean every2027/28 field is published or verified. Inaccessible sources and conflicting notices remain explicit. Transport success and passing software tests are not factual verification. Production has not been changed.\n")
    with zipfile.ZipFile(dest) as archive:
        assert archive.testzip() is None
        for record in manifest["files"]:
            assert hashlib.sha256(archive.read(record["path"])).hexdigest()==record["sha256"]
    print(json.dumps({"path":str(dest),"bytes":dest.stat().st_size,"files":len(files)+2,"sha256":hashlib.sha256(dest.read_bytes()).hexdigest()},indent=2))


if __name__=="__main__":build()
