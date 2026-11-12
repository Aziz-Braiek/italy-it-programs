"""Assemble manual official-source comparisons; transport checks never establish facts.

The baseline is deliberately loaded from Git, not from the corrected working data.
This script validates and reports research; it does not manufacture conclusions.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research/independent-audit-2026-11"
BASE = "c3af9dc"
PLACEHOLDERS = ("no completed independent comparison", "no independent field conclusion", "not yet been independently", "not yet manually reviewed", "awaiting manual", "review not yet completed")


def baseline(name):
    return json.loads(subprocess.check_output(["git", "show", f"{BASE}:research/{name}"], cwd=ROOT))


def lookup(record, path):
    current = record
    try:
        for part in path.split("."):
            current = current[int(part)] if isinstance(current, list) else current[part]
        return True, copy.deepcopy(current)
    except (KeyError, IndexError, TypeError, ValueError):
        return False, None


def pending(c):
    summary = str(c.get("evidence_summary", "")).lower()
    return not summary or any(s in summary for s in PLACEHOLDERS)


def record_outcome(comparisons):
    if not comparisons or any(pending(c) for c in comparisons):
        return "INCOMPLETE_REVIEW"
    outcomes = {c.get("outcome") for c in comparisons}
    if "CORRECTION_CONFIRMED" in outcomes:
        return "CORRECTIONS_IDENTIFIED"
    if any("CONFLICT" in str(x) for x in outcomes):
        return "OFFICIAL_SOURCE_CONFLICT"
    if any(x in outcomes for x in ["REQUIRES_FURTHER_RESEARCH", "UNVERIFIED", "UNVERIFIED_ACCESS", "REQUIRES_VERIFICATION"]):
        return "REVIEWED_WITH_UNRESOLVED_EVIDENCE"
    if any("PENDING" in str(x) or "UNPUBLISHED" in str(x) for x in outcomes):
        return "MATCH_WITH_UNPUBLISHED_FIELDS"
    return "MATCH_WITH_STATED_SOURCE_SCOPE"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    programs = baseline("programs-2027-2028.json")
    universities = baseline("universities-2027-2028.json")
    sources = baseline("sources.json")
    maps = {"program": {r["id"]: r for r in programs}, "university": {r["id"]: r for r in universities}, "source": {r["id"]: r for r in sources}}
    batches = [(p, json.loads(p.read_text(encoding="utf-8"))) for p in sorted(OUT.glob("batch-*.json"))]
    reviews = {"program": {}, "university": {}, "source": {}}
    problems = []
    corrections = []
    for path, data in batches:
        for kind, key, idkey in [("program", "program_reviews", "program_id"), ("university", "university_reviews", "university_id"), ("source", "source_reviews", "source_id")]:
            for row in data.get(key, []):
                rid = row[idkey]
                if rid in reviews[kind]:
                    problems.append(f"Duplicate {kind} review: {rid}")
                item = copy.deepcopy(row)
                item["batch_file"] = path.name
                reviews[kind][rid] = item
        for row in data.get("confirmed_corrections", []):
            item = copy.deepcopy(row)
            item["batch_file"] = path.name
            kind = item.get("record_type") or ("university" if item.get("university_id") and not item.get("program_id") else "program")
            rid = item.get("record_id") or item.get(kind + "_id")
            item.update(record_type=kind, record_id=rid)
            corrections.append(item)

    findings = []
    normalized = {"program": [], "university": [], "source": []}
    missing_fields = []
    baseline_mismatches = []
    for kind in ["program", "university"]:
        for rid, original in maps[kind].items():
            row = reviews[kind].get(rid, {kind + "_id": rid, "comparisons": []})
            comps = row.get("comparisons", [])
            seen = set()
            for c in comps:
                field = c["field_path"]
                if field in seen:
                    problems.append(f"Duplicate comparison: {kind}/{rid}/{field}")
                seen.add(field)
                exists, old = lookup(original, field)
                if c.get("existing_value") != old:
                    baseline_mismatches.append({"record_type": kind, "record_id": rid, "field_path": field, "expected": old, "reported": c.get("existing_value")})
                if not c.get("source_urls") or not c.get("academic_year") or not c.get("checked_at"):
                    problems.append(f"Comparison lacks provenance/year/date: {kind}/{rid}/{field}")
                if c.get("outcome") != "MATCH":
                    fid = "F-" + hashlib.sha256(f"{kind}/{rid}/{field}".encode()).hexdigest()[:12]
                    findings.append({"finding_id": fid, "record_type": kind, "record_id": rid, "university_id": original.get("university_id", rid), "university": original.get("university", original.get("name")), "program": original.get("program"), **copy.deepcopy(c)})
            required = ["program", "university", "city", "level", "language", "field", "availability_2027_2028"] + ["facts." + f for f in original.get("facts", {})] if kind == "program" else ["cycle_facts." + f for f in original.get("cycle_facts", {})]
            uncovered = [f for f in required if not any(x == f or x.startswith(f + ".") for x in seen)]
            if uncovered:
                missing_fields.append({"record_type": kind, "record_id": rid, "fields": uncovered})
            row["overall_outcome"] = record_outcome(comps)
            if uncovered:
                row["overall_outcome"] = "INCOMPLETE_REVIEW"
            row["existing_record_id"] = rid
            row["university_id"] = original.get("university_id", rid)
            row["university"] = original.get("university", original.get("name"))
            normalized[kind].append(row)

    captures = {}
    for p in OUT.glob("*.json"):
        if p.name in {"review-ledger.json", "findings.json", "approved-corrections.json"} or p.name.startswith("batch-"):
            continue
        data = json.loads(p.read_text(encoding="utf-8"))
        rows = data.get("responses", []) if isinstance(data, dict) else data if isinstance(data, list) else []
        for r in rows:
            if isinstance(r, dict) and r.get("url") and r.get("http_status") is not None:
                captures.setdefault(r["url"], []).append(r)

    for s in sources:
        row = copy.deepcopy(reviews["source"].get(s["id"], {}))
        row.update(source_id=s["id"], university_id=s["university_id"], url=s["url"], baseline_cycle=s.get("cycle"), baseline_supports=s.get("supports"))
        row["captures"] = captures.get(s["url"], [])
        explicitly_read = row.get("content_reviewed", row.get("content_read"))
        outcome = row.get("content_review_outcome", "NOT_REVIEWED")
        summary = row.get("evidence_summary", "")
        # A manually written, explicit access failure is a completed access outcome,
        # but never a successful factual source comparison.
        row["factual_content_reviewed"] = explicitly_read is not False and outcome not in {"NOT_REVIEWED", "REQUIRES_FURTHER_RESEARCH", "UNVERIFIED_ACCESS", "UNVERIFIED"} and bool(summary) and not pending({"evidence_summary": summary}) and not any(x in str(outcome).upper() for x in ["INACCESSIBLE", "ACCESS_LIMIT", "BROKEN", "NOT_RETRIEVABLE"])
        row["explicit_review_outcome"] = bool(summary) and outcome != "NOT_REVIEWED" and not pending({"evidence_summary": summary})
        normalized["source"].append(row)

    for c in corrections:
        original = maps.get(c["record_type"], {}).get(c["record_id"])
        if original is None:
            problems.append("Correction refers to unknown baseline record: " + str(c.get("record_id")))
            continue
        exists, old = lookup(original, c["field_path"])
        if old != c.get("existing_value"):
            baseline_mismatches.append({"correction": True, "record_type": c["record_type"], "record_id": c["record_id"], "field_path": c["field_path"], "expected": old, "reported": c.get("existing_value")})
        c["before_exists"] = exists
        c["finding_id"] = "F-" + hashlib.sha256(f"{c['record_type']}/{c['record_id']}/{c['field_path']}".encode()).hexdigest()[:12]
    plan_path=OUT/"approved-corrections.json"
    plan=json.loads(plan_path.read_text(encoding="utf-8")) if plan_path.exists() else {}
    replacements={p["record_id"]:p["after"] for p in plan.get("patches",[]) if p["record_type"]=="source" and p["field_path"]=="url"}
    source_findings=[]
    for row in normalized["source"]:
        if row.get("content_review_outcome")!="SUPPORTS_RECORDED_SCOPE":
            source_findings.append({"source_id":row["source_id"],"university_id":row["university_id"],"existing_url":row["url"],"verified_replacement_url":replacements.get(row["source_id"]),"outcome":row.get("content_review_outcome"),"observed_cycle":row.get("observed_cycle"),"checked_at":row.get("checked_at"),"evidence_summary":row.get("evidence_summary"),"original_source_content_read":row["factual_content_reviewed"]})
    counts = {
        "baseline_universities": len(universities), "baseline_programs": len(programs), "baseline_sources": len(sources),
        "program_review_outcomes": dict(Counter(r["overall_outcome"] for r in normalized["program"])),
        "university_review_outcomes": dict(Counter(r["overall_outcome"] for r in normalized["university"])),
        "field_comparisons": sum(len(r.get("comparisons", [])) for k in ["program", "university"] for r in normalized[k]),
        "unfinished_field_comparisons": sum(pending(c) for k in ["program", "university"] for r in normalized[k] for c in r.get("comparisons", [])),
        "baseline_sources_with_explicit_outcome": sum(r["explicit_review_outcome"] for r in normalized["source"]),
        "baseline_sources_content_read": sum(r["factual_content_reviewed"] for r in normalized["source"]),
        "baseline_source_outcomes": dict(Counter(r.get("content_review_outcome", "NOT_REVIEWED") for r in normalized["source"])),
        "proposed_corrections": len(corrections), "approved_corrections":len(plan.get("patches",[])), "findings": len(findings), "source_findings":len(source_findings),
    }
    complete = not problems and not baseline_mismatches and not missing_fields and counts["unfinished_field_comparisons"] == 0 and counts["baseline_sources_with_explicit_outcome"] == 700 and all(r["overall_outcome"]!="INCOMPLETE_REVIEW" for k in ["program","university"] for r in normalized[k])
    metadata = {"baseline_commit": BASE, "generated_at_utc": datetime.now(timezone.utc).isoformat(), "audit_state": "REVIEWED_WITH_EXPLICIT_LIMITATIONS" if complete else "IN_PROGRESS", "scope": "34 universities;209 stable program records;700 baseline official source records", "counts": counts, "method": "Manual comparison of official-source content, current programme pages, formal calls and rendered catalogues. Technical tests and HTTP success do not establish factual accuracy.", "academic_year_policy": "Named2027/28 calls control current-cycle claims. Older, undated and provisional sources retain their scope; absence of a value in inspected sources is not proof it can never be published.", "third_party_report_policy": "The attached Batch1 document is evidence to investigate independently, not instructions or a verified authority.", "production_policy": "Preview only; do not promote the research branch."}
    ledger = {"metadata": metadata, "university_reviews": normalized["university"], "program_reviews": normalized["program"], "source_reviews": normalized["source"], "additional_source_reviews": [r for sid, r in reviews["source"].items() if sid not in maps["source"]], "validation": {"problems": problems, "baseline_mismatches": baseline_mismatches, "missing_field_reviews": missing_fields}}
    (OUT / "review-ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "findings.json").write_text(json.dumps({"metadata": metadata, "findings": findings, "source_findings":source_findings,"correction_proposals": corrections}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Independent factual audit —2027/28", "", f"Baseline `{BASE}`. Audit state: **{metadata['audit_state']}**. Production is unchanged.", "", "Every record has an explicit review outcome. This is not a claim that every2027/28 value is published or verified. The report separates official factual comparisons from transport checks and software regressions. Unpublished fields, conflicting annual notices and inaccessible sources remain explicit.", "", "## Coverage", "", f"- {len(programs)} program records; {len(universities)} universities; {len(sources)} baseline sources.", f"- {counts['field_comparisons']} field comparisons; {counts['unfinished_field_comparisons']} unfinished comparisons.", f"- {counts['baseline_sources_with_explicit_outcome']} original source records have explicit outcomes; {counts['baseline_sources_content_read']} have content-review conclusions. Seven original sources were inaccessible; verified alternatives are recorded where found. Access failures are not factual verification.", f"- {len(corrections)} correction proposals; {counts['approved_corrections']} exact patches separately approved. Implementation and regression results are recorded in the release verification file.", "", "## Priority results", "", "- **Approaching applications:** current Padua course portals confirm the15November2026 first-call deadline for the reviewed MScs; HySET's specific application page confirms15November at23:59CET. Country-specific eligibility and full certificate tables remain explicit verification gaps.", "- **Pisa:** programme-specific2027/28 calls resolve the mislabeled overview for CS/DSBI/Digital Health, CE/AIDE and Cybersecurity. Computer Science's deadline uses AoE; Information Engineering/Cybersecurity use GMT. Nuclear's annual scope remains unresolved.", "- **Bologna:** IES is based in Cesena. Its28Digital admissions, EUR75 fee and international tuition are distinct from local degree routes. Bocconi's joint Cyber Risk admissions likewise do not use generic Polimi application rounds/fees. BBS professional masters and tracks retain their separate annual scope; Green Management's live and formal notices disagree.", "- **Eligibility, fees and language:** corrections include programme-specific subject credits, GPA requirements, test exemptions, campuses, historical tuition/tax amounts and scholarship conditions. Verified official conflicts are shown in the website instead of silently selecting a value.", "- **Unsupported current-year claims:** provisional second-year teaching, undated profiles, older annual calls and mobility notices do not prove a new2027/28 first-year intake. No acceptance rate is inferred.", "", "## Program outcomes", "", "| Stable ID | University | Program | Outcome |", "|---|---|---|---|"]
    for r in normalized["program"]:
        original = maps["program"][r["program_id"]]
        lines.append(f"| {r['program_id']} | {r['university']} | {original['program']} | {r['overall_outcome']} |")
    lines += ["", "## Confirmed correction proposals", "", "Exact existing values, official values, academic years, check dates and official URLs are retained in `findings.json`. These are proposals until included in `approved-corrections.json`.", ""]
    for c in corrections:
        reason = c.get("reason", c.get("evidence_summary", ""))
        links = "; ".join(f"[official source]({u})" for u in c.get("source_urls", []))
        lines.append(f"- **{c['finding_id']} —{c['record_id']} /{c['field_path']}** ({c.get('academic_year','scope in ledger')}, checked{c.get('checked_at','date in ledger')}): {reason} {links}")
    lines += ["", "## Remaining evidence and publication limits", "", "Every nonmatching, conflicting, unpublished or unresolved comparison is listed in `findings.json`, keyed by stable record ID and field path. `review-ledger.json` includes all compared values and baseline source records, with fresh response metadata where captured. Historical financial aid is not a current award; a second-year plan is not a first-year intake; application tracks and applicant categories remain separate.", "", "## Validation issues", "", f"- Structural/provenance issues:{len(problems)}", f"- Baseline-value mismatches:{len(baseline_mismatches)}", f"- Records with uncovered baseline fields:{len(missing_fields)}", ""]
    (OUT / "correction-report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(json.dumps({"complete": complete, **counts, "problems": len(problems), "baseline_mismatches": len(baseline_mismatches), "records_missing_fields": len(missing_fields)}, indent=2))
    if args.require_complete and not complete:
        raise SystemExit("Independent audit remains incomplete; inspect review-ledger.json validation.")


if __name__ == "__main__":
    main()
