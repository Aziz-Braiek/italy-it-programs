#!/usr/bin/env python3
"""Build the Claude Browser review checklist and machine-readable manifest."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
AS_OF = "2026-11-10"
BASE_URL = "https://italy-it-programs.vercel.app"
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
    return {
        "id": source["id"],
        "title": source.get("title"),
        "url": source.get("url"),
        "source_type": source.get("source_type"),
        "cycle": source.get("cycle"),
        "accessed_at": source.get("accessed_at"),
        "evidence": source.get("evidence"),
        "supports": source.get("supports", []),
        "refresh_status": "pending",
        "refresh_checked_at": None,
        "refresh_http_status": None,
        "refresh_effective_url": None,
        "refresh_notes": None,
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
        "# Claude Browser independent review checklist",
        "",
        f"Prepared {AS_OF} for academic year 2027/28. Review each record against official university pages, calls, portals, regulations, and PDFs.",
        "",
        f"Snapshot inventory: {len(universities)} universities, {len(programs)} program records, {len(sources)} source records.",
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
            "review_page_url": f"{BASE_URL}/universities/{university['id']}/",
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
                "program_page_url": f"{BASE_URL}/programs/{program['id']}/",
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

    source_manifest = [source_to_summary(source) for source in sources]
    manifest = {
        "metadata": {
            "academic_year": "2027-2028",
            "prepared_at": AS_OF,
            "source_commit": "e6995e7",
            "branch": "research/final-2027-2028-refresh",
            "website": BASE_URL,
            "review_status": "in_progress",
            "counts": {"universities": len(universities), "programs": len(programs), "sources": len(sources)},
            "previous_snapshot_inconclusive_url_checks": "Approximately 100 checks were inconclusive in the previous audit; individual URL outcomes must be re-evaluated and recorded below.",
        },
        "universities": manifest_universities,
        "programs": manifest_programs,
        "sources": source_manifest,
        "previously_inconclusive_url_checks": [],
        "review_log": [],
    }
    (RESEARCH / "claude-review-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (RESEARCH / "claude-review-checklist.md").write_text("\n".join(checklist) + "\n", encoding="utf-8")
    print(f"Wrote review manifest with {len(universities)} universities, {len(programs)} programs, and {len(sources)} sources.")


if __name__ == "__main__":
    main()
