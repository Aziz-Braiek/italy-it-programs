"""Apply only independently approved, evidence-linked corrections after legacy generation."""
from __future__ import annotations
import copy
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"research"/"independent-audit-2026-11"/"approved-corrections.json"


def baseline_source_records():
    if not PLAN.exists():
        return None
    # A corrected URL must not inherit the previous output's transport metadata.
    # Rebuild exact preconditions from the frozen input, rather than from output.
    return json.loads(subprocess.check_output(["git","show","c3af9dc:research/sources.json"],cwd=ROOT))


def audit_summary():
    if not PLAN.exists():
        return None
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    ledger_path=PLAN.parent/"review-ledger.json"
    metadata=json.loads(ledger_path.read_text(encoding="utf-8"))["metadata"] if ledger_path.exists() else {}
    return {"baseline_commit":plan["baseline_commit"],"as_of":plan["as_of"],"state":metadata.get("audit_state","IN_PROGRESS"),"counts":metadata.get("counts",{}),"approved_patches":len(plan["patches"]),"ledger":"independent-audit-2026-11/review-ledger.json","findings":"independent-audit-2026-11/findings.json","report":"independent-audit-2026-11/correction-report.md","production":"unchanged; preview review only"}


def report_lines(universities,programs,sources,coverage):
    summary=audit_summary()
    if not summary:
        return None
    rows=["# Italy University Tracker —2027/28 research report","",f"Snapshot checked **{coverage['as_of']}**. Independent factual audit: **{summary['state']}**. Production remains unchanged.","","The audit compares the frozen c3af9dc dataset with official calls, course profiles, applicant portals and annual regulations. Software tests and successful HTTP responses do not establish admissions facts. The full audit ledger records existing and official values, stable IDs, academic years, check dates, sources and explicit unresolved outcomes.","","## Current data","",f"- {len(universities)} universities and {len(programs)} stable program records; no original records removed.",f"- {len(sources)} source records, including independently located official evidence in addition to the700 baseline records.",f"- {coverage['programs_fully_verified']} offers have current-cycle core name, level, language and availability evidence. This is not full verification of every admissions field.",f"- {coverage['programs_availability_pending']} records still need new-entry availability confirmation;{coverage['programs_not_offered_2027_2028']} records are explicitly not offered.",f"- {summary['approved_patches']} independently approved field/source corrections are applied with exact baseline preconditions.","","## Audit evidence","","- [Complete review ledger](independent-audit-2026-11/review-ledger.json)","- [Structured findings and correction proposals](independent-audit-2026-11/findings.json)","- [Correction report and explicit limitations](independent-audit-2026-11/correction-report.md)","- [Applied correction plan](independent-audit-2026-11/approved-corrections.json)","","## Important source-scope results","","Pisa's general table mixes a2026/27 heading with2027 dates. Formal2027/28 calls independently establish CS/DSBI/Digital Health, Computer Engineering/AIDE and Cybersecurity. The Computer Science department's deadline uses AoE; Information Engineering/Cybersecurity use GMT. Nuclear's portal schedule remains recorded as a conflict until a named annual call establishes its scope. Messina's2027/28 Data Science units are provisional Year2 teaching for the2026/27 cohort; this does not establish a new first-year intake. University-wide medicine calls are excluded from its Data Science windows.","","Every university and program outcome, including Bologna's distinct local and joint application tracks, is recorded in the ledger. Historical fees and scholarships retain their actual year and are not promoted to2027/28. Conflicting official sources remain visible.","","The prior narrative is preserved in [the baseline report](independent-audit-2026-11/input-evidence/baseline-2027-2028-final-report-c3af9dc.md). It is historical input and does not override the new ledger.","","## Program status snapshot","","| Stable ID | University | Program | Core2027/28 status | Last checked |","|---|---|---|---|---|"]
    for p in programs:
        rows.append(f"| {p['id']} | {p['university']} | {p['program']} | {p['overall_status']} | {p.get('last_checked','')} |")
    rows += ["","All data remain subject to the official notice for the particular programme, applicant category and academic year. No acceptance rate is inferred from unrelated cohorts or approximate counts.",""]
    return rows

def apply(universities,programs,sources):
    if not PLAN.exists():
        return
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    if plan.get("baseline_commit")!="c3af9dc":
        raise ValueError("Independent correction plan has an unexpected baseline")
    # Legacy generators reuse nested fact objects across programme and university
    # records. Detach each record so a narrow patch cannot mutate another record
    # or invalidate its independently checked baseline precondition.
    universities[:]=[copy.deepcopy(record) for record in universities]
    programs[:]=[copy.deepcopy(record) for record in programs]
    sources[:]=[copy.deepcopy(record) for record in sources]
    maps={"program":{x["id"]:x for x in programs},"university":{x["id"]:x for x in universities},"source":{x["id"]:x for x in sources}}
    for source in plan.get("new_sources",[]):
        if source["id"] in maps["source"]:
            raise ValueError("New audit source ID already exists: "+source["id"])
        record=copy.deepcopy(source); sources.append(record); maps["source"][record["id"]]=record
    seen=set()
    for patch in plan.get("patches",[]):
        if patch.get("verification_outcome")!="CONFIRMED" or not patch.get("source_urls") or not patch.get("finding_id"):
            raise ValueError("A correction lacks independent confirmation/evidence")
        key=(patch["record_type"],patch["record_id"],patch["field_path"])
        if key in seen:
            raise ValueError("Duplicate audit patch: "+str(key))
        seen.add(key)
        current=maps[patch["record_type"]][patch["record_id"]]
        parts=patch["field_path"].split(".")
        for part in parts[:-1]:
            current=current[int(part)] if isinstance(current,list) else current[part]
        leaf=int(parts[-1]) if isinstance(current,list) else parts[-1]
        exists=isinstance(current,list) or leaf in current
        if exists!=patch.get("before_exists",True) or (exists and current[leaf]!=patch["before"]):
            raise ValueError("Audit correction precondition changed: "+str(key))
        current[leaf]=copy.deepcopy(patch["after"])
    for item in plan.get("checked_records",[]):
        record=maps[item["record_type"]][item["record_id"]]
        record["last_checked"]=item["checked_at"]
