#!/usr/bin/env python3
"""Build the Claude Web review checklist and machine-readable manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
AS_OF = "2026-11-11"
BASE_URL = "https://italy-it-programs.vercel.app"
DATASET_FILES = ("programs-2027-2028.json", "universities-2027-2028.json", "sources.json", "coverage-report.json")
NEEDS_REVIEW = {"REQUIRES_VERIFICATION", "NOT_YET_PUBLISHED", "UNAVAILABLE", "CONFLICTING_SOURCES"}


def load(name: str) -> Any:
    return json.loads((RESEARCH / name).read_text(encoding="utf-8"))


def walk_facts(value: Any, path: str = "") -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    if isinstance(value, dict):
        status = value.get("status")
        if status in NEEDS_REVIEW:
            results.append({
                "field": path or "record",
                "status": status,
                "value": value.get("value"),
                "notes": value.get("notes"),
                "source_ids": value.get("source_ids", []),
            })
        for key, child in value.items():
            if key in {"value", "status", "notes", "source_ids"}:
                continue
            child_path = f"{path}.{key}" if path else key
            results.extend(walk_facts(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            results.extend(walk_facts(child, f"{path}[{index}]"))
    return results


def source_to_summary(source: dict[str, Any]) -> dict[str, Any]:
    browser_outcome = (source.get("browser_check") or {}).get("outcome")
    direct_outcome = (source.get("url_check") or {}).get("outcome")
    if browser_outcome == "accessible":
        refresh_status = browser_outcome
    elif direct_outcome in {"accessible", "redirected", "broken", "access_limited"}:
        refresh_status = direct_outcome
    else:
        refresh_status = browser_outcome or direct_outcome or "pending"
    return {
        "id": source["id"],
        "title": source.get("title"),
        "url": source.get("url"),
        "source_type": source.get("source_type"),
        "cycle": source.get("cycle"),
        "accessed_at": source.get("accessed_at"),
        "evidence": source.get("evidence"),
        "supports": source.get("supports", []),
        "refresh_status": refresh_status,
        "url_check": source.get("url_check"),
        "browser_check": source.get("browser_check"),
    }


def official_program_sources(program: dict[str, Any], source_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    linked = [source_by_id[sid] for sid in program.get("source_ids", []) if sid in source_by_id]

    def score(source: dict[str, Any]) -> int:
        text = f"{source.get('title', '')} {source.get('source_type', '')} {' '.join(source.get('supports', []))}".lower()
        points = 0
        for token, value in (("program", 6), ("course", 5), ("curriculum", 5), ("admission", 4), ("requirements", 3), ("catalog", 3), ("degree", 2)):
            if token in text:
                points += value
        if "university-level" in text or "international admissions" in text:
            points -= 3
        return points

    return sorted(linked, key=lambda source: (-score(source), source["id"]))


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return re.sub(r"\s+", " ", text).replace("|", "\\|")


def main() -> None:
    target_path = RESEARCH / "claude-review-target.json"
    review_target = json.loads(target_path.read_text(encoding="utf-8")) if target_path.exists() else {}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=review_target.get("preview_origin", BASE_URL), help="Deployment origin used for review page links")
    parser.add_argument("--output-dir", type=Path, default=RESEARCH, help="Directory for the generated checklist and manifest")
    args = parser.parse_args()
    base_url = args.base_url.rstrip("/")
    parsed = urlsplit(base_url)
    if parsed.scheme != "https" or not parsed.netloc or parsed.path or parsed.query or parsed.fragment:
        parser.error("--base-url must be an HTTPS origin without a path, query or fragment")
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    dataset_paths = [f"research/{name}" for name in DATASET_FILES]
    try:
        dataset_commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", *dataset_paths], cwd=ROOT, text=True).strip() or None
        dataset_dirty = bool(subprocess.check_output(["git", "status", "--porcelain", "--", *dataset_paths], cwd=ROOT, text=True).strip())
    except (OSError, subprocess.CalledProcessError):
        dataset_commit, dataset_dirty = None, None
    universities = load("universities-2027-2028.json")
    programs = load("programs-2027-2028.json")
    sources = load("sources.json")
    source_by_id = {source["id"]: source for source in sources}
    programs_by_university: dict[str, list[dict[str, Any]]] = {}
    for program in programs:
        programs_by_university.setdefault(program["university_id"], []).append(program)

    manifest_universities: list[dict[str, Any]] = []
    manifest_programs: list[dict[str, Any]] = []
    checklist: list[str] = [
        "# Claude Web independent review checklist",
        "",
        f"Prepared {AS_OF} for academic year 2027/28. Review each record against official university pages, calls, portals, regulations, and PDFs.",
        "",
        f"Snapshot inventory: {len(universities)} universities, {len(programs)} program records, {len(sources)} source records.",
        f"Research dataset commit: `{dataset_commit or 'not available in this checkout'}`. Review target: {base_url}. Production baseline commit: `e6995e7`.",
        "When reviewing an undeployed research snapshot, use the preview-specific checklist and manifest from the review package. The production website can contain older data.",
        "",
        "## Review rules",
        "",
        "- Treat each 2027/28 claim as cycle-specific; label prior-cycle evidence with its actual year.",
        "- Distinguish an offered program from a confirmed 2027/28 first-year intake and from a published application deadline.",
        "- Do not infer a missing deadline, fee, GPA requirement, scholarship, or acceptance rate.",
        "- For inaccessible sources, record the response and method; an automated failure alone does not prove a source is broken.",
        "- The `refresh_status` fields in the manifest begin as `pending` and should only be changed after review.",
        "",
        "## University and program checklist",
        "",
    ]

    for university in universities:
        university_programs = programs_by_university.get(university["id"], [])
        university_sources = [source_by_id[sid] for sid in university.get("source_ids", []) if sid in source_by_id]
        university_entry = {
            "id": university["id"],
            "name": university["name"],
            "city": university.get("city"),
            "region": university.get("region"),
            "website_url": university.get("official_website"),
            "admissions_url": university.get("international_admissions_url"),
            "application_portal_url": university.get("application_portal_url"),
            "review_page_url": f"{base_url}/universities/{university['id']}/",
            "existing_status": university.get("cycle_status"),
            "existing_research_stage": university.get("research_stage"),
            "existing_last_checked": university.get("last_checked"),
            "research_summary": university.get("research_summary"),
            "coverage": university.get("coverage", {}),
            "source_ids": university.get("source_ids", []),
            "source_urls": [source_to_summary(source) for source in university_sources],
            "program_ids": [program["id"] for program in university_programs],
            "refresh_status": "pending",
            "refresh_checked_at": None,
            "refresh_outcome": None,
        }
        manifest_universities.append(university_entry)

        checklist.extend([
            f"### {university['name']} ({university['city']}) — `{university['id']}`",
            "",
            f"- [ ] University outcome reviewed | Existing status: `{university.get('cycle_status')}` | Existing last checked: `{university.get('last_checked')}`",
            f"- [ ] University page: {university_entry['review_page_url']}",
            f"- [ ] Official website: {university.get('official_website') or 'not recorded'}",
            f"- [ ] Admissions page: {university.get('international_admissions_url') or 'not recorded'}",
            f"- [ ] Application portal: {university.get('application_portal_url') or 'not recorded'}",
            "- [ ] Recheck admissions routes, cycle notices, fees, scholarships, applicant eligibility, and source conflicts.",
            "",
        ])
        if university_sources:
            checklist.extend(["Official university-level sources:", ""])
            for source in university_sources:
                checklist.append(f"- [ ] `{source['id']}` — [{md_escape(source.get('title'))}]({source.get('url')}) (cycle: {md_escape(source.get('cycle'))}; checked in prior snapshot: {md_escape(source.get('accessed_at'))})")
            checklist.append("")

        for program in university_programs:
            linked_sources = official_program_sources(program, source_by_id)
            issues = walk_facts({
                "level": program.get("level"),
                "language": program.get("language"),
                "field": program.get("field"),
                "availability_2027_2028": program.get("availability_2027_2028"),
                "facts": program.get("facts", {}),
            })
            conflicts = [issue for issue in issues if issue["status"] == "CONFLICTING_SOURCES"]
            missing = [issue for issue in issues if issue["value"] is None and issue["status"] in NEEDS_REVIEW]
            entry = {
                "id": program["id"],
                "university_id": university["id"],
                "university": program.get("university"),
                "city": program.get("city"),
                "program": program.get("program"),
                "level": program.get("level"),
                "language": program.get("language"),
                "program_page_url": f"{base_url}/programs/{program['id']}/",
                "university_page_url": university_entry["review_page_url"],
                "official_program_source_urls": [source_to_summary(source) for source in linked_sources],
                "availability_2027_2028": program.get("availability_2027_2028"),
                "existing_overall_status": program.get("overall_status"),
                "existing_last_checked": program.get("last_checked"),
                "fields_needing_review": issues,
                "missing_fields": missing,
                "known_source_conflicts": conflicts,
                "source_ids": program.get("source_ids", []),
                "previous_cycle_tags": program.get("previous_cycle_tags"),
                "refresh_status": "pending",
                "refresh_checked_at": None,
                "refresh_outcome": None,
            }
            manifest_programs.append(entry)

            checklist.extend([
                f"#### {program.get('program')} — `{program['id']}`",
                "",
                f"- [ ] Review program and 2027/28 intake | Current status: `{program.get('overall_status')}` | Availability: `{program.get('availability_2027_2028', {}).get('status')}` | Last checked: `{program.get('last_checked')}`",
                f"- [ ] Program page: {entry['program_page_url']}",
                f"- [ ] University page: {entry['university_page_url']}",
                f"- [ ] Verify official name, university/campus, level, teaching language, new 2027/28 intake, eligibility, application windows and rounds, fee, tuition, entry/GPA/language requirements, tests, scholarships/aid, and official application/program URLs.",
            ])
            if linked_sources:
                checklist.append("Official linked sources to revisit:")
                for source in linked_sources:
                    checklist.append(f"- [ ] `{source['id']}` — [{md_escape(source.get('title'))}]({source.get('url')}) (cycle: {md_escape(source.get('cycle'))}; prior check: {md_escape(source.get('accessed_at'))})")
            else:
                checklist.append("- [ ] No official source is currently linked to this program; locate an individual course page or call.")
            if conflicts:
                checklist.append("Known source conflicts in current data:")
                for conflict in conflicts:
                    checklist.append(f"  - `{conflict['field']}` — {md_escape(conflict.get('notes'))}")
            if missing:
                checklist.append("Currently missing or unpublished fields:")
                for item in missing:
                    checklist.append(f"  - `{item['field']}` — `{item['status']}` — {md_escape(item.get('notes'))}")
            checklist.append("")

    unique_url_checks = {source.get("url"): source.get("url_check") for source in sources if source.get("url_check")}
    url_outcomes: dict[str, int] = {}
    for check in unique_url_checks.values():
        url_outcomes[check.get("outcome", "unknown")] = url_outcomes.get(check.get("outcome", "unknown"), 0) + 1
    checklist.extend([
        "## Source URL recheck results",
        "",
        f"Checked {len(unique_url_checks)} unique URLs representing {sum(1 for source in sources if source.get('url_check'))} source records on {AS_OF}. Unique URL outcomes: {url_outcomes}. HTTP 404/410 outcomes are listed as broken; TLS, timeout, and remote-disconnect cases remain inconclusive.",
        "",
        "### Redirected sources",
        "",
    ])
    for source in sources:
        check = source.get("url_check") or {}
        if check.get("outcome") == "redirected":
            checklist.append(f"- `{source['id']}` — [{md_escape(source.get('title'))}]({source.get('url')}) → {check.get('effective_url')} (HTTP {check.get('http_status')}).")
    checklist.extend(["", "### Inconclusive source URLs", ""])
    for source in sources:
        check = source.get("url_check") or {}
        browser_check = source.get("browser_check") or {}
        if check.get("outcome") in {"inconclusive", "access_limited"} and browser_check.get("outcome") != "accessible":
            note = browser_check.get("note") or check.get("error") or "No successful direct response was recorded."
            checklist.append(f"- `{source['id']}` — [{md_escape(source.get('title'))}]({source.get('url')}) — direct check inconclusive; {md_escape(note)}")
    checklist.append("")

    source_manifest = [source_to_summary(source) for source in sources]
    unique_checks = {source.get("url"): source.get("url_check") for source in sources if source.get("url_check")}
    outcomes: dict[str, int] = {}
    for check in unique_checks.values():
        outcomes[check.get("outcome", "unknown")] = outcomes.get(check.get("outcome", "unknown"), 0) + 1
    inconclusive_sources = [
        {
            "source_id": source["id"],
            "url": source.get("url"),
            "direct_http_outcome": (source.get("url_check") or {}).get("outcome"),
            "browser_outcome": (source.get("browser_check") or {}).get("outcome"),
            "direct_http_error": (source.get("url_check") or {}).get("error"),
            "note": (source.get("browser_check") or {}).get("note") or "Direct HTTPS validation remained inconclusive; do not classify this URL as broken without browser verification.",
        }
        for source in sources
        if (source.get("url_check") or {}).get("outcome") in {"inconclusive", "access_limited"}
        and (source.get("browser_check") or {}).get("outcome") != "accessible"
    ]
    redirected_sources = [
        {"source_id": source["id"], "url": source.get("url"), "effective_url": (source.get("url_check") or {}).get("effective_url")}
        for source in sources
        if (source.get("url_check") or {}).get("outcome") == "redirected"
    ]
    manifest = {
        "metadata": {
            "academic_year": "2027-2028",
            "prepared_at": AS_OF,
            "source_commit": dataset_commit,
            "source_commit_meaning": "Latest commit changing the four core research datasets; exact file hashes below identify this snapshot.",
            "dataset_has_uncommitted_changes": dataset_dirty,
            "dataset_sha256": {name: hashlib.sha256((RESEARCH / name).read_bytes()).hexdigest() for name in DATASET_FILES},
            "production_baseline_commit": "e6995e70e7fc4673a561af69fbb7fa14ea84491b",
            "production_website": BASE_URL,
            "branch": "research/final-2027-2028-refresh",
            "website": base_url,
            "review_environment": "production_baseline" if base_url == BASE_URL else "preview",
            "review_deployment": review_target if base_url == review_target.get("preview_origin") else None,
            "review_status": "in_progress",
            "counts": {"universities": len(universities), "programs": len(programs), "sources": len(sources)},
            "previous_snapshot_inconclusive_url_checks": "The prior audit reported approximately 100 inconclusive checks. This refresh rechecked every unique URL and preserves the response by source record below.",
            "current_url_audit": {
                "checked_at": AS_OF,
                "source_records": len(sources),
                "unique_urls_checked": len(unique_checks),
                "unique_url_outcomes": outcomes,
                "redirected_source_records": redirected_sources,
                "remaining_inconclusive_source_records": inconclusive_sources,
                "confirmed_404_or_410_source_records": [source["id"] for source in sources if (source.get("url_check") or {}).get("outcome") == "broken"],
            },
        },
        "universities": manifest_universities,
        "programs": manifest_programs,
        "sources": source_manifest,
        "previously_inconclusive_url_checks": inconclusive_sources,
        "review_log": [],
    }
    (output_dir / "claude-review-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output_dir / "claude-review-checklist.md").write_text("\n".join(checklist).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote review manifest with {len(universities)} universities, {len(programs)} programs, and {len(sources)} sources.")


if __name__ == "__main__":
    main()
