#!/usr/bin/env python3
"""Audit invariants for the Italy University Tracker research data."""
import json
from collections import Counter
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "research"
VALID = {"CONFIRMED", "NOT_YET_PUBLISHED", "UNAVAILABLE", "REQUIRES_VERIFICATION", "CONFLICTING_SOURCES", "NOT_APPLICABLE"}

universities = json.loads((R / "universities-2027-2028.json").read_text(encoding="utf-8"))
programs = json.loads((R / "programs-2027-2028.json").read_text(encoding="utf-8"))
sources = json.loads((R / "sources.json").read_text(encoding="utf-8"))
coverage = json.loads((R / "coverage-report.json").read_text(encoding="utf-8"))
archive = json.loads((R / "archive" / "legacy-programs.json").read_text(encoding="utf-8-sig"))

assert len(universities) == 34, f"expected 34 universities, got {len(universities)}"
assert len({u["id"] for u in universities}) == len(universities), "duplicate university IDs"
assert len(programs) >= len(archive), "active program records dropped archived candidates"
assert len({p["id"] for p in programs}) == len(programs), "duplicate program IDs"
assert sum(p["discovery_source"] == "previous_tracker" for p in programs) == len(archive), "not all legacy listings are retained"
keys = [(p["university_id"], p["program"].casefold(), p["level"]["value"]) for p in programs]
assert len(set(keys)) == len(keys), "duplicate university/program/level records"
assert len({s["id"] for s in sources}) == len(sources), "duplicate source IDs"
source_ids = {s["id"] for s in sources}
source_by_id = {s["id"]: s for s in sources}
uni_ids = {u["id"] for u in universities}
for s in sources:
    assert date.fromisoformat(s["accessed_at"]) <= date.fromisoformat(coverage["as_of"]), f"source checked after snapshot date: {s['id']}"
assert {u["id"] for u in universities if u["source_ids"]} == uni_ids, "a university lacks an official source record"
assert all(p["university_id"] in uni_ids for p in programs), "program refers to an unknown university"
assert all(s.get("university_id") in uni_ids for s in sources), "source refers to an unknown university"

confirmed_programs = [p for p in programs if p["overall_status"] == "CONFIRMED"]
for p in programs:
    assert p["overall_status"] in VALID
    for key in ("level", "language", "field", "availability_2027_2028"):
        item = p[key]
        assert item["status"] in VALID, f"invalid field status: {p['program']} / {key}"
        if item["status"] == "CONFIRMED":
            assert item["source_ids"], f"confirmed field has no source: {p['program']} / {key}"
        assert all(sid in source_ids for sid in item.get("source_ids", [])), f"unknown source ID in {p['program']} / {key}"
    availability = p["availability_2027_2028"]
    if availability["status"] == "CONFIRMED":
        assert isinstance(availability["value"], bool), f"confirmed availability must be true or false: {p['program']}"
    else:
        assert availability["value"] is None, f"pending availability must be null, not interpreted as false: {p['program']}"
    if p.get("previous_cycle_tags"):
        tags = p["previous_cycle_tags"]
        assert tags.get("cycle") and tags["cycle"] != coverage["academic_year"], f"previous-cycle tags use the active academic year: {p['program']}"
        assert p["overall_status"] != "CONFIRMED", f"previous-cycle-only tags promoted the full program to current-cycle confirmed: {p['program']}"
        assert availability["status"] != "CONFIRMED", f"previous-cycle-only evidence confirms active-cycle availability: {p['program']}"
        for key in ("level", "language", "field"):
            assert tags.get(key) == p[key]["value"], f"previous-cycle tag mismatch: {p['program']} / {key}"
            assert p[key]["status"] != "CONFIRMED", f"previous-cycle-only tag is incorrectly confirmed for the active cycle: {p['program']} / {key}"
    if p["overall_status"] == "CONFIRMED":
        assert p["availability_2027_2028"]["status"] == "CONFIRMED"
        assert p["availability_2027_2028"]["value"] is True
        assert p["source_ids"], f"confirmed program has no source: {p['program']}"
        assert all(sid in source_ids for sid in p["source_ids"]), f"unknown source for {p['program']}"
    else:
        assert p["availability_2027_2028"]["value"] is not True or p["availability_2027_2028"]["status"] == "CONFIRMED"
        if p["availability_2027_2028"]["status"] == "CONFIRMED":
            assert p["source_ids"], f"cycle-confirmed program missing sources for unresolved fields: {p['program']}"
    if p["overall_status"] == "NOT_APPLICABLE":
        assert availability["status"] == "CONFIRMED" and availability["value"] is False, f"discontinued/not-offered record lacks a sourced false availability: {p['program']}"
    assert all(sid in source_ids for sid in p.get("source_ids", [])), f"unknown source for {p['program']}"
    for key, item in p.get("facts", {}).items():
        assert item["status"] in VALID, f"invalid field status: {p['program']} / {key}"
        if item["status"] == "CONFIRMED":
            assert item["source_ids"], f"confirmed field has no source: {p['program']} / {key}"
        assert all(sid in source_ids for sid in item.get("source_ids", [])), f"unknown source ID in {p['program']} / {key}"
        if key.startswith("previous_cycle_"):
            assert item.get("notes"), f"prior-cycle fact lacks a scope note: {p['program']} / {key}"
            assert all(source_by_id[sid].get("cycle") != coverage["academic_year"] for sid in item.get("source_ids", [])), f"prior-cycle fact cites an active-cycle source: {p['program']} / {key}"
    forbidden = {"tuition", "app_fee", "gpa_cat", "gpa_detail", "deadline_display", "deadline_iso", "tier", "acceptance_rate", "last_verified"}
    assert not (forbidden & p.keys()), f"legacy display fields leaked into active record: {p['program']}"

for u in universities:
    assert u["research_stage"] == "PARTIALLY_RESEARCHED", "university incorrectly marked fully researched"
    assert u["cycle_status"] in VALID
    assert all(sid in source_ids for sid in u["source_ids"]), f"unknown university source ID: {u['name']}"
    for key, item in u.get("cycle_facts", {}).items():
        assert item["status"] in VALID
        if item["status"] == "CONFIRMED":
            assert item["source_ids"], f"confirmed university field has no source: {u['name']} / {key}"
        assert all(sid in source_ids for sid in item.get("source_ids", []))
        if key == "application_windows" and isinstance(item.get("value"), list):
            for window in item["value"]:
                if window.get("exact_dates") is False:
                    assert not window.get("start") and not window.get("end"), f"approximate window contains invented exact dates: {u['name']}"

assert coverage["program_records"] == len(programs)
assert coverage["universities_researched"] == len(universities)
assert coverage["universities_without_initial_official_source_outcome"] == sum(not u["source_ids"] for u in universities)
assert coverage["universities_fully_verified"] == 0
partial_program_review = sorted(u["id"] for u in universities if u["coverage"]["program_level_review"] == "partial")
not_started_program_review = sorted(u["id"] for u in universities if u["coverage"]["program_level_review"] == "not_started")
assert coverage["universities_with_program_level_research"] == len(partial_program_review)
assert coverage["university_ids_with_program_level_research"] == partial_program_review
assert coverage["universities_program_level_review_not_started"] == len(not_started_program_review)
assert coverage["university_ids_with_program_level_review_not_started"] == not_started_program_review
assert coverage["programs_fully_verified"] == len(confirmed_programs)
assert coverage["programs_cycle_availability_confirmed"] == sum(p["availability_2027_2028"]["status"] == "CONFIRMED" and p["availability_2027_2028"]["value"] is True for p in programs)
assert coverage["programs_availability_pending"] == sum(p["availability_2027_2028"]["status"] != "CONFIRMED" for p in programs)
assert coverage["programs_requiring_verification"] == sum(p["overall_status"] == "REQUIRES_VERIFICATION" for p in programs)
assert coverage["programs_not_offered_2027_2028"] == sum(p["overall_status"] == "NOT_APPLICABLE" for p in programs)
previous_cycle_only = sorted(p["id"] for p in programs if p.get("previous_cycle_tags") and p["availability_2027_2028"]["status"] != "CONFIRMED")
assert coverage["programs_supported_only_by_previous_cycle"] == len(previous_cycle_only)
assert coverage["program_ids_supported_only_by_previous_cycle"] == previous_cycle_only
assert coverage["source_records"] == len(sources)
conflicting_universities = {
    p["university_id"] for p in programs
    if any(f["status"] == "CONFLICTING_SOURCES" for f in p.get("facts", {}).values())
} | {
    u["id"] for u in universities
    if any(f["status"] == "CONFLICTING_SOURCES" for f in u.get("cycle_facts", {}).values())
}
assert coverage["universities_with_conflicting_sources"] == len(conflicting_universities)
assert coverage["university_ids_with_conflicting_sources"] == sorted(conflicting_universities)
assert coverage["universities_with_deadlines_or_calls_explicitly_not_yet_published"] == len(coverage["university_ids_with_deadlines_or_calls_explicitly_not_yet_published"])

print("DATA AUDIT PASSED")
print(f"universities={len(universities)}; legacy candidates={len(archive)}; program records={len(programs)}")
print(f"program offers confirmed={len(confirmed_programs)}; sources={len(sources)}")
print(f"verified levels={dict(Counter(p['level']['value'] for p in confirmed_programs))}")
