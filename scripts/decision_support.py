"""Evidence-backed applicant facts, separate from course availability and deadlines."""
from __future__ import annotations
import copy
import json
import re
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research/decision-support-2026-11"
CURRENT = "2027/28 confirmed"
PREVIOUS = "previous cycle (estimate only)"
UNKNOWN = "not confirmed"
PROGRAM_FIELDS = {
    "duration": "Degree duration", "ects": "ECTS credits",
    "prerequisites": "Prerequisite background and credits",
    "english_requirement": "English certificates and exemptions",
    "admission_test": "Admission test or exam", "selection_method": "Selection method",
    "minimum_grade": "Minimum grade", "non_eu_seats": "Non-EU seats", "tuition": "Tuition and calculation",
}
UNIVERSITY_FIELDS = {
    "universitaly": "Universitaly pre-enrolment",
    "documents": "Qualifications, recognition and documents",
    "regional_dsu": "Regional right-to-study body",
    "visa_permit": "University visa and permit guidance",
}
GAP_REASONS = {
    "duration": "Exact degree duration has not been established for a named applicable cycle; a standard duration is not assumed.",
    "ects": "Total programme ECTS have not been verified for a named cycle; individual module credits are not a programme total.",
    "prerequisites": "Required background and subject/sector-credit minima are not verified; a degree title or a recommended background is not sufficient to establish eligibility.",
    "english_requirement": "Applicable English certificate scores, acceptance and waivers are not verified. English teaching language alone does not establish a certificate policy.",
    "admission_test": "A named entrance test, exemption, date and remote modality have not been established. Silence is not a no-test exemption.",
    "selection_method": "A programme- and cycle-specific selection method has not been established by this review.",
    "minimum_grade": "The applicable degree/country GPA threshold has not been verified; no grade conversion or universal cut-off is invented.",
    "non_eu_seats": "A reserved non-EU/visa-applicant quota is not verified. A general intake limit is not treated as a non-EU quota.",
    "tuition": "A programme-applicable tuition amount/range/calculation for a named cycle is not established. Application fees are not tuition.",
    "universitaly": "The university/programme-specific Universitaly requirement and deadline have not been established for an applicable cycle.",
    "documents": "The applicable diploma/transcript, DoV/CIMEA alternatives, apostille/legalisation and translation rules have not been established; documents are not assumed interchangeable.",
    "regional_dsu": "The regional body and international/programme eligibility have not been established together for an applicable cycle.",
    "visa_permit": "Applicable university-published visa/permit instructions have not been verified. Generic national guidance is not substituted for a university rule.",
}


def read(name):
    return json.loads((RESEARCH / name).read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def source_evidence():
    return {row["url"]: row for row in read("source-checks.json")["responses"]}


def unknown(reason="Not yet verified from an applicable official source.", checked_urls=None, checked_at=None):
    return {"value": "Not confirmed", "cycle_status": UNKNOWN, "academic_cycle": None,
            "source_urls": [], "verified_date": None, "checked_urls": checked_urls or [],
            "checked_at": checked_at, "reason": reason}


def is_current(fact):
    return fact.get("cycle_status") == CURRENT and fact.get("academic_cycle") in {"2027/28", "2027-2028", "2027/2028", "2027–2029"} and fact.get("value") not in (None, "", "Not confirmed")


def binary_state(fact):
    """A conditional rule is not a universal yes or no for an unknown applicant."""
    answer = fact.get("answer")
    return answer if is_current(fact) and answer in {"yes", "no"} else UNKNOWN


def confirmation_label(fact):
    if fact.get("evidence_scope") == "degree_structure":
        return "Degree structure"
    if is_current(fact) and fact.get("missing_components"):
        return "Partly confirmed · 2027/28"
    return fact.get("cycle_status", UNKNOWN)


def conflicts_for(program_id):
    return [item for item in read("source-conflicts.json") if program_id in item.get("record_ids", [])]


def resolve(program, key, university):
    fact = program.get("decision_support", {}).get(key) or unknown()
    if "university_policy" in fact:
        policy = university.get("decision_support", {}).get("policies", {}).get(fact["university_policy"])
        if not policy:
            raise ValueError(f"Missing inherited policy: {program['id']} / {key}")
        return policy
    return fact


def scholarships(program, university):
    offers = university.get("decision_support", {}).get("scholarships") or [unknown()]
    applicable = [f for f in offers if not f.get("program_ids") or program["id"] in f["program_ids"]]
    return applicable or [unknown("No program-applicable scholarship call verified. Admission does not establish funding eligibility.", sorted({url for offer in offers for url in offer.get("source_urls", [])}), "2026-11-13")]


def scholarship_summary(program, university):
    offers = scholarships(program, university)
    current = [f for f in offers if is_current(f)]
    previous = [f for f in offers if f.get("cycle_status") == PREVIOUS]
    scoped_unknown = [f for f in offers if f.get("cycle_status") == UNKNOWN and program["id"] in f.get("program_ids", [])]
    if not current and scoped_unknown:
        return scoped_unknown[0]
    selected = current or previous
    if not selected:
        return offers[0]
    return {**selected[0], "value": " | ".join(f["value"] for f in selected),
            "source_urls": sorted({url for f in selected for url in f["source_urls"]}),
            "evidence_sha256": {url: sha for f in selected for url, sha in f.get("evidence_sha256", {}).items()},
            "missing_components": sorted({item for f in selected for item in f.get("missing_components", [])}),
            "answer": "yes" if current and any(f.get("answer") == "yes" for f in current) else "not confirmed"}


def apply(universities, programs):
    approved = read("verified-facts.json")
    checks = read("source-checks.json")["responses"]
    by_url = {row["url"]: row for row in checks}
    sources = {row["id"]: row for row in json.loads((ROOT / "research/sources.json").read_text(encoding="utf-8"))}
    hosts = {p["university_id"] for p in programs if p["overall_status"] == "CONFIRMED"}
    for kind, records, fields in (("universities", universities, UNIVERSITY_FIELDS), ("programs", programs, PROGRAM_FIELDS)):
        for record in records:
            ids = list(record.get("source_ids") or [])
            for f in (record.get("facts") or record.get("cycle_facts") or {}).values():
                ids += f.get("source_ids", [])
            urls = sorted({sources[sid]["url"] for sid in ids if sid in sources and sources[sid]["url"] in by_url})
            priority = record.get("overall_status") == "CONFIRMED" if kind == "programs" else record["id"] in hosts
            reason = ("Reviewed official material does not establish this field for a named applicable cycle. Check the linked pages and program call."
                      if priority else "Awaiting-record research is incomplete this round; no applicable official value has been approved for this field.")
            if record.get("overall_status") == "NOT_APPLICABLE":
                reason = "The programme is not offered in 2027/28. No new admissions decision facts are inferred for this record."
            defaults = {key: unknown(GAP_REASONS[key]+" "+reason, urls, "2026-11-13" if urls else None) for key in fields}
            if kind == "universities":
                defaults.update(scholarships=[unknown(reason, urls, "2026-11-13" if urls else None)], policies={})
            defaults.update(copy.deepcopy(approved.get(kind, {}).get(record["id"], {})))
            record["decision_support"] = defaults
    validate(universities, programs)
    write_reports(universities, programs)
    from build_decision_refinement_report import build
    build(universities, programs)


def validate_fact(fact, location):
    if "university_policy" in fact:
        return
    value = fact.get("value")
    known = value not in (None, "", "Not confirmed")
    label = fact.get("cycle_status")
    if label not in {CURRENT, PREVIOUS, UNKNOWN}:
        raise ValueError(f"Missing/invalid cycle label: {location}")
    if not known and value != "Not confirmed":
        raise ValueError(f"Unknown field must say Not confirmed: {location}")
    if known:
        if 'missing_components' in fact and (not isinstance(fact['missing_components'], list) or any(not isinstance(item, str) or not item.strip() for item in fact['missing_components'])):
            raise ValueError(f"Missing components must be named explicitly: {location}")
        if is_current(fact) and re.search(r"not confirmed|\bTBD\b|forthcoming|not yet published|not stated|does not specify|needs clarification|seek clarification", value, re.I) and not fact.get("missing_components"):
            raise ValueError(f"Partly resolved field lacks named missing components: {location}")
        if fact.get("evidence_scope") == "degree_structure":
            proof = fact.get("structure_evidence") or {}
            if proof.get("url") not in fact.get("source_urls", []) or not proof.get("passage"):
                raise ValueError(f"Degree structure lacks explicit official course evidence: {location}")
        if not fact.get("source_urls") or any(not urlsplit(url).scheme == "https" or not urlsplit(url).hostname for url in fact["source_urls"]):
            raise ValueError(f"Value without official source URL: {location}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fact.get("verified_date") or ""):
            raise ValueError(f"Value without verified date: {location}")
        if label == UNKNOWN:
            raise ValueError(f"Unconfirmed field must use the Not confirmed value: {location}")
        if not fact.get("academic_cycle"):
            raise ValueError(f"Value without academic cycle: {location}")
        if not re.fullmatch(r"20\d{2}(?:/(?:\d{2}|20\d{2})|[-–]20\d{2})", fact["academic_cycle"]):
            raise ValueError(f"Malformed academic cycle: {location}")
        if label == PREVIOUS and fact.get("academic_cycle") in {"2027/28", "2027-2028"}:
            raise ValueError(f"Previous-cycle value mislabelled: {location}")
        if label == CURRENT:
            evidence = fact.get("current_cycle_evidence") or {}
            if not is_current(fact) or not isinstance(evidence, dict) or evidence.get("url") not in fact["source_urls"] or "2027" not in evidence.get("cycle_marker", ""):
                raise ValueError(f"Confirmed field without 2027/28 evidence: {location}")
            captured = source_evidence().get(evidence["url"], {})
            if not {"2027/28", "2027–2029"}.intersection(captured.get("academic_cycles_detected", [])):
                raise ValueError(f"Confirmed field cites no captured current-cycle context: {location}")
        for url in fact["source_urls"]:
            captured = source_evidence().get(url, {})
            if not captured.get("sha256") or fact.get("evidence_sha256", {}).get(url) != captured["sha256"]:
                raise ValueError(f"Value lacks a matching reviewed-source hash: {location}")


def validate_filter_flags(program, university, tuition, scholarship, admission_test=None, english_certificate=None):
    facts = {"tuition": (tuition, resolve(program, "tuition", university)),
             "scholarship": (scholarship, scholarship_summary(program, university))}
    for key, (flag, fact) in facts.items():
        if flag == "documented":
            if not is_current(fact) or fact.get("evidence_scope") == "degree_structure":
                raise ValueError(f"Confirmed {key} filter without 2027/28 evidence: {program['id']}")
            validate_fact(fact, f"{program['id']}/{key} filter")
    for key, flag in (("admission_test", admission_test), ("english_requirement", english_certificate)):
        if flag is not None:
            fact = resolve(program, key, university)
            if flag not in {"yes", "no", UNKNOWN} or flag != binary_state(fact):
                raise ValueError(f"Unverified yes/no filter state: {program['id']}/{key}")
            if flag in {"yes", "no"}:
                validate_fact(fact, f"{program['id']}/{key} filter")


def validate(universities, programs):
    uni_by_id = {u["id"]: u for u in universities}
    for uni in universities:
        data = uni.get("decision_support", {})
        for key in UNIVERSITY_FIELDS:
            validate_fact(data.get(key, {}), f"{uni['id']}/{key}")
        for i, fact in enumerate(data.get("scholarships", [])):
            validate_fact(fact, f"{uni['id']}/scholarships/{i}")
        for key, fact in data.get("policies", {}).items():
            validate_fact(fact, f"{uni['id']}/policies/{key}")
    for program in programs:
        uni = uni_by_id[program["university_id"]]
        for key in PROGRAM_FIELDS:
            fact = resolve(program, key, uni)
            validate_fact(fact, f"{program['id']}/{key}")
            if fact.get("evidence_scope") == "degree_structure" and key not in {"duration", "ects"}:
                raise ValueError(f"Degree-structure label on a cycle-dependent field: {program['id']}/{key}")


def filter_state(fact):
    return "documented" if is_current(fact) else "pending"


def export_fact(fact):
    # Previous-cycle values are deliberately excluded from shortlist exports.
    if not is_current(fact):
        return {"value": "Not confirmed", "cycle_status": fact.get("cycle_status", UNKNOWN), "source_urls": [], "verified_date": "", "confirmation": "Degree structure (historical value omitted)" if fact.get('evidence_scope') == 'degree_structure' else "Not confirmed", "missing_components": []}
    return {**{key: fact.get(key, "") for key in ("value", "cycle_status", "source_urls", "verified_date")}, "confirmation": confirmation_label(fact), "missing_components": fact.get('missing_components', [])}


def write_reports(universities, programs):
    from collections import Counter
    uni_by_id = {u["id"]: u for u in universities}
    counts = {}
    gaps = []
    ledger = []
    for kind, records, fields in (("program", programs, PROGRAM_FIELDS), ("university", universities, UNIVERSITY_FIELDS)):
        for key in fields:
            tally = Counter()
            for record in records:
                fact = resolve(record, key, uni_by_id[record["university_id"]]) if kind == "program" else record["decision_support"][key]
                tally[fact["cycle_status"]] += 1
                row = {"record_type": kind, "id": record["id"], "name": record.get("program") or record.get("name"), "field": key, **fact}
                ledger.append(row)
                if fact["cycle_status"] == UNKNOWN or fact.get("missing_components"):
                    gaps.append(row)
            counts[f"{kind}.{key}"] = {label: tally[label] for label in (CURRENT, PREVIOUS, UNKNOWN)}
    tally = Counter()
    for uni in universities:
        for i, fact in enumerate(uni["decision_support"]["scholarships"]):
            tally[fact["cycle_status"]] += 1
            row = {"record_type": "university", "id": uni["id"], "name": uni["name"], "field": "scholarships", "offer_index": i, **fact}
            ledger.append(row)
            if fact["cycle_status"] == UNKNOWN or fact.get("missing_components"):
                gaps.append(row)
    counts["university.scholarship_offers"] = {label: tally[label] for label in (CURRENT, PREVIOUS, UNKNOWN)}
    outcomes = []
    hosts = {p["university_id"] for p in programs if p["overall_status"] == "CONFIRMED"}
    for kind, records in (("program", programs), ("university", universities)):
        for record in records:
            relevant = [row for row in ledger if row["record_type"] == kind and row["id"] == record["id"]]
            tally = Counter(row["cycle_status"] for row in relevant)
            priority = record.get("overall_status") == "CONFIRMED" if kind == "program" else record["id"] in hosts
            has_facts = tally[CURRENT] + tally[PREVIOUS] > 0
            state = "reviewed_with_field_gaps" if priority and has_facts else "reviewed_no_approved_values" if priority else "partial_previous_cycle_review" if has_facts else "awaiting_record_research_incomplete"
            if record.get("overall_status") == "NOT_APPLICABLE":
                state = "not_offered_no_admissions_research"
            outcomes.append({"record_type": kind, "id": record["id"], "name": record.get("program") or record["name"],
                             "priority_record": priority, "review_outcome": state,
                             "counts": {label: tally[label] for label in (CURRENT, PREVIOUS, UNKNOWN)},
                             "unconfirmed_fields": [row["field"] for row in relevant if row["cycle_status"] == UNKNOWN],
                             "partly_confirmed_fields": [row["field"] for row in relevant if is_current(row) and row.get("missing_components")],
                             "reason": "See the field ledger for precise missing components, publication limits, source conflicts and pages checked. Awaiting-only records without approved values have not completed the lower-priority research pass."})
    for name, value in (("coverage.json", counts), ("field-ledger.json", ledger), ("unverified-fields.json", gaps)):
        (RESEARCH / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (RESEARCH / "record-outcomes.json").write_text(json.dumps(outcomes, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    report = ["# Applicant decision layer — evidence and gaps", "", "Research snapshot: 13 November 2026 (Europe/Rome).",
              "", "Program availability, original record review dates and application-deadline facts are unchanged: 47 confirmed / 159 awaiting / 3 not offered; 209 programs and 34 universities.",
              "", "The 47 confirmed programs and their 11 host universities received the priority source review. Eight awaiting Polito records received older-cycle requirements; another 44 awaiting profiles received directly checked older-cycle duration/credit facts. The remaining awaiting-record research is incomplete; no blanket factual-completeness claim is made.",
              "", "Known values are manually approved in verified-facts.json, with official URLs, academic cycle, field verification date and captured-source hashes. Unknowns say Not confirmed. Passing software checks and a successful HTTP fetch are not factual verification.",
              "", "Current-cycle evidence totals include partly confirmed fields. The UI labels these Partly confirmed and names the missing components; they must not be read as fully resolved eligibility. Degree structure is displayed separately from intake confirmation. The priority-scope refinement report linked from the homepage separates before/after and full/partial counts.",
              "", "## Field counts across the full tracker", "", "Program-field rows each total 209; university-field rows each total 34. Scholarship offers are counted individually, including one explicit unknown placeholder for universities without an approved scheme.",
              "", "| Field | 2027/28 confirmed | Previous cycle only | Not confirmed |", "|---|---:|---:|---:|"]
    report += [f"| {key} | {value[CURRENT]} | {value[PREVIOUS]} | {value[UNKNOWN]} |" for key, value in counts.items()]
    checks = read("source-checks.json")["responses"]
    report += ["", "## Source coverage and limits", "", f"Freshly captured official URLs: {len(checks)}; HTTP 200 responses: {sum(r.get('http_status') == 200 for r in checks)}. Captures include university sites/application portals, official joint-program admissions and regional right-to-study bodies. A transport result alone does not approve a field.",
               "", f"Responses not established as readable by the capture client: {sum(r.get('transport_outcome') != 'accessible' for r in checks)}. Some sources initially failed through resets, TLS errors or timeouts; the EAP application page was subsequently recovered. Other old/broken, access-limited or unreadable sources remain explicit. HTTP 200 can also contain a soft error and does not establish readable admissions content. Successful alternatives were used only where applicable; TLS verification was not disabled. Each latest URL/outcome remains in source-checks.json.",
               "", "## Normalisation and UI", "", "University logistics, scholarship offers and shared fee/English policies live on university records. Program-specific values and policy references live on program records. Program cards resolve those references; they do not store copies of university logistics. Joint-program and applicant scopes are preserved. The older research observations remain frozen for audit transparency; public eligibility/cost sections use the new canonical decision fields.",
               "", "Cards show known tuition, English, test and funding facts with cycle/date/source labels; unknown fields collapse into one line. Detail pages retain every field and explicit source conflicts without JavaScript. Yes/no filters accept only the exact current, sourced binary state; conditional rules remain not confirmed for an unspecified applicant. Tuition/funding filters use only current, supported facts. A test's absence is not a no-test exemption. Degree structure never establishes intake or cost/test/funding rules.",
               "", "CSV adds value, cycle, official URL and verification date columns per decision field. Earlier-cycle values are replaced by Not confirmed while retaining their cycle label; historical amounts and requirements are not exported as actionable data. Existing deadline calculation and calendar logic are unchanged.",
               "", "## Conflicts and missing records", "", "See source-conflicts.json for exact competing claims, URLs and handling. The complete field-ledger.json includes every field outcome; unverified-fields.json lists each gap and pages checked. record-outcomes.json and the table below cover every program and university explicitly.",
               "", "## Record outcomes", "", "| Type | Stable ID | Program / university | Current | Previous | Unknown | Review outcome |", "|---|---|---|---:|---:|---:|---|"]
    report += [f"| {r['record_type']} | {r['id']} | {r['name'].replace('|', '/')} | {r['counts'][CURRENT]} | {r['counts'][PREVIOUS]} | {r['counts'][UNKNOWN]} | {r['review_outcome']} |" for r in outcomes]
    report += ["", "## Rebuild and validation", "", "Run python scripts/build_research_data.py, python scripts/build_site.py, python scripts/audit_research_data.py, python -m unittest discover -s tests, node scripts/test_site.mjs, and node scripts/test_tracker_ui.mjs. Use scripts/test_live_site.mjs for a protected preview after opening its deployment-specific share link.", "", "No new institutions, alerts or applicant-profile filtering were added. Production deployment is outside this release."]
    (RESEARCH / "report.md").write_text("\n".join(report)+"\n", encoding="utf-8")
