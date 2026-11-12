#!/usr/bin/env python3
"""Build the public static website from the research JSON source of truth."""

from __future__ import annotations

import html
import importlib.util
import json
import re
import shutil
import struct
import sys
import zlib
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
BASE = "https://italy-it-programs.vercel.app"
TODAY = date.today()
CURRENT_CYCLE = "2027-2028"
sys.stdout.reconfigure(encoding="utf-8")


def read_json(name: str) -> Any:
    with (ROOT / "research" / name).open(encoding="utf-8") as handle:
        return json.load(handle)


PROGRAMS = read_json("programs-2027-2028.json")
UNIVERSITIES = read_json("universities-2027-2028.json")
SOURCES = read_json("sources.json")
UNIVERSITY_BY_ID = {item["id"]: item for item in UNIVERSITIES}
SOURCE_BY_ID = {item["id"]: item for item in SOURCES}
PROGRAMS_BY_UNIVERSITY: dict[str, list[dict[str, Any]]] = {}
for item in PROGRAMS:
    PROGRAMS_BY_UNIVERSITY.setdefault(item["university_id"], []).append(item)


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def public_text(value: Any) -> str:
    """Normalize current-year formatting without changing the research file."""
    text = str(value)
    return re.sub(r"2027(?:–|-|/)2028|2027–28", "2027/28", text)


def plain(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return public_text(value)


def record_source_cycles(source_ids: list[str] | None) -> set[str]:
    return {
        SOURCE_BY_ID[source_id].get("cycle", "")
        for source_id in (source_ids or [])
        if source_id in SOURCE_BY_ID
    }


def field_is_current(value: Any) -> bool:
    if not isinstance(value, dict) or value.get("status") != "CONFIRMED" or not value.get("value"):
        return False
    return CURRENT_CYCLE in record_source_cycles(value.get("source_ids"))


def verified_or_previous(program: dict[str, Any], key: str) -> tuple[str, bool]:
    item = program.get(key) or {}
    if field_is_current(item):
        return plain(item.get("value")), True
    prior = program.get("previous_cycle_tags") or program.get("previous_tracker_tags") or {}
    if prior.get(key):
        return plain(prior[key]), False
    if item.get("value"):
        return plain(item["value"]), False
    return "", False


def record_status(status: str) -> tuple[str, str]:
    labels = {
        "CONFIRMED": ("Available for 2027/28", "confirmed"),
        "REQUIRES_VERIFICATION": ("Awaiting 2027/28 confirmation", "pending"),
        "CONFLICTING_SOURCES": ("Sources need review", "conflict"),
        "NOT_YET_PUBLISHED": ("2027/28 details not announced", "pending"),
        "UNAVAILABLE": ("No current offer found", "unavailable"),
        "NOT_APPLICABLE": ("Not offered for 2027/28", "unavailable"),
    }
    return labels.get(status, ("Status not confirmed", "pending"))


def status_label(status: str, current: bool = False) -> str:
    if status == "CONFIRMED":
        return "Confirmed for 2027/28" if current else "Confirmed in earlier evidence"
    return {
        "REQUIRES_VERIFICATION": "Not confirmed",
        "CONFLICTING_SOURCES": "Sources disagree",
        "NOT_YET_PUBLISHED": "Not yet announced",
        "UNAVAILABLE": "Unavailable",
        "NOT_APPLICABLE": "Not applicable",
    }.get(status, "Not confirmed")


def key_label(key: str) -> str:
    labels = {
        "application_windows": "Application dates",
        "application_windows_2027_2028": "Application dates",
        "application_deadline": "Application deadline",
        "application_fee": "Application fee",
        "application_fee_2027_2028": "Application fee",
        "tuition": "Tuition",
        "tuition_2027_2028": "Tuition",
        "scholarships": "Scholarships and benefits",
        "scholarships_2027_2028": "Scholarships and benefits",
        "program_specific_requirements_2027_2028": "Admission requirements",
        "previous_cycle_course_listing": "Earlier course listing",
        "previous_cycle_course_identity": "Earlier course name",
        "previous_cycle_program_requirements": "Earlier admission requirements",
        "previous_cycle_application_windows": "Earlier application dates",
        "previous_cycle_application_fee": "Earlier application fee",
        "previous_cycle_tuition": "Earlier tuition information",
        "previous_cycle_scholarships": "Earlier scholarship information",
        "previous_cycle_english_requirement": "Earlier language requirement",
        "previous_cycle_non_eu_admission": "Earlier non-EU admission guidance",
        "previous_cycle_international_admission": "Earlier international admission guidance",
        "available_places": "Places",
        "available_places_2027_2028": "Places",
        "requirements": "Admission requirements",
        "english_requirement": "Language requirement",
        "application_route": "How to apply",
        "academic_year_course_offering": "Course year information",
        "national_visa_application_deadline_2027_2028": "National visa framework",
    }
    if key in labels:
        return labels[key]
    return re.sub(r"_+", " ", key).strip().capitalize()


def source_links(source_ids: list[str] | None, label: str = "Open official source") -> str:
    chunks: list[str] = []
    used: set[str] = set()
    for source_id in source_ids or []:
        item = SOURCE_BY_ID.get(source_id)
        if not item or not item.get("url") or item["url"] in used:
            continue
        used.add(item["url"])
        chunks.append(
            f'<a href="{esc(item["url"])}" target="_blank" rel="noopener noreferrer">'
            f'{esc(item.get("title") or label)} <span aria-hidden="true">↗</span></a>'
        )
    return '<ul class="source-list">' + "".join(f"<li>{link}</li>" for link in chunks) + "</ul>" if chunks else ""


def all_program_source_ids(program: dict[str, Any]) -> list[str]:
    ids = list(program.get("source_ids") or [])
    for item in program.get("facts", {}).values():
        if isinstance(item, dict):
            ids.extend(item.get("source_ids") or [])
    return list(dict.fromkeys(ids))


def pretty_value(value: Any) -> str:
    if value is None or value == "":
        return '<span class="muted">No value recorded</span>'
    if isinstance(value, list):
        return "<ul>" + "".join(f"<li>{pretty_value(item)}</li>" for item in value) + "</ul>"
    if isinstance(value, dict):
        if any(k in value for k in ("start", "end", "date", "eligible_group")):
            parts = []
            period = " – ".join(esc(public_text(value[k])) for k in ("start", "end") if value.get(k))
            if value.get("date"):
                period = esc(public_text(value["date"]))
            if period:
                parts.append(f"<strong>{period}</strong>")
            for key, item in value.items():
                if key not in {"start", "end", "date"} and item not in (None, ""):
                    parts.append(f"<span>{esc(key.replace('_', ' ').capitalize())}: {esc(public_text(item))}</span>")
            return '<div class="value-lines">' + "".join(parts) + "</div>"
        return '<dl class="value-pairs">' + "".join(
            f"<dt>{esc(key.replace('_', ' ').capitalize())}</dt><dd>{pretty_value(item)}</dd>"
            for key, item in value.items()
            if item not in (None, "")
        ) + "</dl>"
    return esc(public_text(value))


def fact_status(fact: dict[str, Any], key: str) -> str:
    status = fact.get("status", "REQUIRES_VERIFICATION")
    if key.startswith(("previous_cycle", "historical", "prior_cycle")):
        if status=="CONFLICTING_SOURCES":
            return "Earlier-cycle information · sources disagree"
        if status=="REQUIRES_VERIFICATION":
            return "Earlier-cycle scope unverified"
        return "Earlier-cycle information"
    if status=="CONFIRMED" and (key.startswith("current_published_") or key in {"tuition_currently_displayed","scholarships_currently_displayed","current_foreign_student_fee_guidance"}):
        return "Published guidance · year unconfirmed"
    return status_label(status, current=CURRENT_CYCLE in record_source_cycles(fact.get("source_ids")))


def fact_cards(facts: dict[str, Any]) -> str:
    cards = []
    for key, fact in facts.items():
        if not isinstance(fact, dict) or key == "acceptance_rate":
            continue
        value = fact.get("value")
        notes = fact.get("notes")
        if value in (None, "", [], {}) and not notes:
            continue
        title = key_label(key)
        badge = fact_status(fact, key)
        body = f'<div class="fact-value">{pretty_value(value)}</div>' if value not in (None, "", [], {}) else ""
        note = f'<p class="fact-note">{esc(public_text(notes))}</p>' if notes else ""
        links = source_links(fact.get("source_ids"))
        cards.append(
            '<details class="fact-item"><summary>'
            f'<span>{esc(title)}</span><span class="mini-status">{esc(badge)}</span></summary>'
            f'<div class="fact-content">{body}{note}{links}</div></details>'
        )
    return "".join(cards) if cards else '<p class="muted">No program-specific admissions details are confirmed yet.</p>'


def date_candidates(program: dict[str, Any]) -> list[tuple[str, dict[str, Any], str]]:
    candidates = []
    if program.get("overall_status") != "CONFIRMED":
        return candidates
    for key in ("application_deadline", "application_windows", "application_windows_2027_2028"):
        fact = (program.get("facts") or {}).get(key)
        if not isinstance(fact, dict) or fact.get("status") != "CONFIRMED":
            continue
        if CURRENT_CYCLE not in record_source_cycles(fact.get("source_ids")):
            continue
        value = fact.get("value")
        values = value if isinstance(value, list) else [value]
        # Bocconi's joint degree has two different qualification routes. Keep
        # applicant labels when exporting its nested, independently verified rounds.
        if isinstance(value,dict) and "international_degree_rounds" in value:
            values=[]
            for route,label in [("international_degree_rounds","International bachelor's qualification —Bocconi standard application"),("italian_degree_dedicated_joint_rounds","Italian bachelor's qualification —dedicated joint-degree application")]:
                for window in value.get(route,[]):
                    values.append({**window,"eligible_group":label})
        for row in values:
            if not isinstance(row, dict):
                continue
            end = row.get("end") or row.get("date")
            if not end:
                continue
            try:
                date.fromisoformat(str(end)[:10])
            except ValueError:
                continue
            if date.fromisoformat(str(end)[:10]) < TODAY:
                continue
            candidates.append((str(end)[:10], row, key))
    return sorted(candidates, key=lambda entry: entry[0])


def deadline_display(program: dict[str, Any]) -> str:
    candidates = date_candidates(program)
    if not candidates:
        return ""
    end, window, _ = candidates[0]
    try:
        parsed = datetime.strptime(end, "%Y-%m-%d")
        formatted = f"{parsed.day} {parsed.strftime('%b %Y')}"
    except ValueError:
        formatted = end
    applies_to = window.get("eligible_group") or window.get("applies_to")
    suffix = f" ({applies_to})" if applies_to else ""
    return formatted + suffix


def has_current_fact(program: dict[str, Any], keys: tuple[str, ...]) -> bool:
    return any(
        isinstance((fact := (program.get("facts") or {}).get(key)), dict)
        and fact.get("status") == "CONFIRMED"
        and fact.get("value") not in (None, "", [], {})
        and CURRENT_CYCLE in record_source_cycles(fact.get("source_ids"))
        for key in keys
    )


def program_data_attrs(program: dict[str, Any]) -> str:
    uni = UNIVERSITY_BY_ID.get(program["university_id"], {})
    level, level_current = verified_or_previous(program, "level")
    language, language_current = verified_or_previous(program, "language")
    field, field_current = verified_or_previous(program, "field")
    deadline = date_candidates(program)
    date_value = deadline[0][0] if deadline else ""
    deadline_events = []
    seen_deadlines = set()
    for event_date, row, key in deadline:
        eligible = row.get("eligible_group") or row.get("applies_to") or ""
        event_type = "window" if key.startswith("application_windows") else "deadline"
        identity = (event_date, eligible, event_type)
        if identity in seen_deadlines:
            continue
        seen_deadlines.add(identity)
        deadline_events.append({"date": event_date, "eligible": eligible, "type": event_type})
    scholarship = has_current_fact(program, ("scholarships_2027_2028", "scholarships"))
    tuition = has_current_fact(program, ("tuition_2027_2028", "tuition"))
    return " ".join(
        f'data-{key}="{esc(value)}"'
        for key, value in {
            "program-card": "",
            "program-id": program["id"],
            "university": program.get("university_id", ""),
            "status": program.get("overall_status", ""),
            "level": level,
            "level-current": str(level_current).lower(),
            "language": language,
            "language-current": str(language_current).lower(),
            "field": field,
            "field-current": str(field_current).lower(),
            "city": program.get("city") or uni.get("city", ""),
            "region": uni.get("region", ""),
            "deadline": date_value,
            "deadlines": json.dumps(deadline_events, ensure_ascii=False, separators=(",", ":")),
            "tuition": "documented" if tuition else "pending",
            "scholarship": "documented" if scholarship else "pending",
            "search": " ".join(
                [program.get("program", ""), program.get("university", ""), program.get("city", ""),
                 uni.get("region", ""), field, level, language]
            ).lower(),
        }.items()
    )


def program_card(program: dict[str, Any], *, detailed: bool = False) -> str:
    uni = UNIVERSITY_BY_ID.get(program["university_id"], {})
    status_text, status_class = record_status(program.get("overall_status", ""))
    level, level_current = verified_or_previous(program, "level")
    language, language_current = verified_or_previous(program, "language")
    field, field_current = verified_or_previous(program, "field")
    is_confirmed = program.get("overall_status") == "CONFIRMED"
    summary = (
        "Official university evidence identifies this program for 2027/28. Check the university’s call for your applicant category, requirements and dates."
        if is_confirmed else
        "This program is awaiting confirmation of a new 2027/28 intake. Any earlier course information below is labeled with its cycle."
        if program.get("overall_status") != "NOT_APPLICABLE" else
        "The reviewed official information says this program will not be offered in 2027/28. Open the details and source before making plans."
    )
    if program.get("summary"):
        summary = public_text(program["summary"])
    if not is_confirmed and any(f.get("value") for f in (program.get("facts") or {}).values() if isinstance(f, dict)):
        # Avoid presenting historical profile values as current course facts.
        pass
    tags = []
    if level:
        tags.append(f'<span class="tag">{"Degree" if level_current else "Earlier listing"}: {esc(level)}</span>')
    if language:
        tags.append(f'<span class="tag">{"Language" if language_current else "Earlier listing"}: {esc(language)}</span>')
    if field:
        tags.append(f'<span class="tag">{"Field" if field_current else "Earlier listing"}: {esc(field)}</span>')
    deadline = deadline_display(program)
    if deadline:
        tags.append(f'<span class="tag tag-date">Next confirmed date: {esc(deadline)}</span>')
    header = (
        f'<div class="card-title-row"><div><p class="eyebrow">{esc(uni.get("name", program.get("university", "")))} · '
        f'{esc(program.get("city") or uni.get("city", ""))}</p><h3><a href="/programs/{quote(program["id"], safe="")}/">{esc(program.get("program", "Program title unavailable"))}</a></h3></div>'
        f'<span class="status status-{status_class}" data-status-copy="{esc(program.get("overall_status", ""))}">{esc(status_text)}</span></div>'
    )
    detail_content = f'<p class="card-summary">{esc(summary)}</p>'
    official = uni.get("international_admissions_url") or uni.get("official_website")
    if official:
        detail_content += f'<p class="official-link"><a href="{esc(official)}" target="_blank" rel="noopener noreferrer">University admissions page <span aria-hidden="true">↗</span></a></p>'
    if detailed:
        detail_content += (
            '<div class="detail-fields"><h2>Admissions information</h2>'
            '<p class="muted">Each item is labeled by status and source cycle. Earlier evidence does not confirm a 2027/28 intake.</p>'
            f'{fact_cards(program.get("facts", {}))}</div>'
            '<section class="detail-sources"><h2>Official sources</h2>'
            f'{source_links(all_program_source_ids(program))}</section>'
        )
        detail_content += '<div class="card-actions">'
        detail_content += f'<button class="small-button favorite-button" type="button" data-favorite="{esc(program["id"])}" aria-pressed="false">Save program</button>'
        detail_content += f'<button class="small-button compare-button" type="button" data-compare="{esc(program["id"])}" aria-pressed="false">Compare</button>'
        detail_content += '</div>'
    else:
        detail_content += f'<p class="last-checked">Last reviewed: {esc(program.get("last_checked") or "Date not recorded")}</p>'
        detail_content += '<div class="card-actions">'
        detail_content += f'<button class="small-button favorite-button" type="button" data-favorite="{esc(program["id"])}" aria-pressed="false">Save program</button>'
        detail_content += f'<button class="small-button compare-button" type="button" data-compare="{esc(program["id"])}" aria-pressed="false">Compare</button>'
        detail_content += '</div>'
    attrs = program_data_attrs(program)
    if detailed:
        attrs = attrs.replace('data-program-card="" ', "")
    return (
        f'<article class="program-card" id="program-{esc(program["id"])}" {attrs}>'
        f'{header}<div class="tag-row">{"".join(tags)}</div>{detail_content}</article>'
    )


def university_status_label(status: str) -> tuple[str, str]:
    if status == "CONFIRMED":
        return "2027/28 information found", "confirmed"
    if status == "NOT_YET_PUBLISHED":
        return "Some 2027/28 details not announced", "pending"
    return "Research in progress", "pending"


def university_card(university: dict[str, Any], *, detailed: bool = False) -> str:
    rows = PROGRAMS_BY_UNIVERSITY.get(university["id"], [])
    status_text, status_class = university_status_label(university.get("cycle_status", ""))
    status_key = "UNIVERSITY_CONFIRMED" if university.get("cycle_status") == "CONFIRMED" else "UNIVERSITY_PENDING"
    city_region = " · ".join(filter(None, [university.get("city"), university.get("region")]))
    official = university.get("official_website")
    admissions = university.get("international_admissions_url") or university.get("contact_url") or official
    status_note = university.get("research_summary") or "University admissions information is being reviewed against official sources."
    status_note = public_text(status_note)
    intro = (
        f'<div class="card-title-row"><div><p class="eyebrow">{esc(city_region)}</p><h3><a href="/universities/{quote(university["id"], safe="")}/">{esc(university.get("name", "University"))}</a></h3></div>'
        f'<span class="status status-{status_class}" data-status-copy="{status_key}">{esc(status_text)}</span></div>'
        f'<p class="card-summary">{len(rows)} program {"records" if len(rows) != 1 else "record"} in this tracker</p>'
    )
    links = '<div class="card-links">'
    if admissions:
        links += f'<a href="{esc(admissions)}" target="_blank" rel="noopener noreferrer">Admissions <span aria-hidden="true">↗</span></a>'
    if official:
        links += f'<a href="{esc(official)}" target="_blank" rel="noopener noreferrer">Official website <span aria-hidden="true">↗</span></a>'
    links += '</div>'
    if detailed:
        note = f'<p class="research-summary">{esc(status_note)}</p>'
        programs = '<section class="university-programs"><h2>Programs in this tracker</h2>'
        programs += '<div class="program-list">' + "".join(
            f'<article><a href="/programs/{quote(p["id"], safe="")}/">{esc(p.get("program", "Program"))}</a>'
            f'<span class="status status-{record_status(p.get("overall_status", ""))[1]}" data-status-copy="{esc(p.get("overall_status", ""))}">{esc(record_status(p.get("overall_status", ""))[0])}</span></article>'
            for p in sorted(rows, key=lambda item: (item.get("overall_status") != "CONFIRMED", item.get("program", "").casefold()))
        ) + '</div></section>'
        fact_rows = university.get("cycle_facts") or {}
        admissions_facts = '<section class="detail-fields"><h2>University-level admissions information</h2><div class="fact-grid">' + fact_cards(fact_rows) + '</div></section>'
        uni_sources = source_links(university.get("source_ids") or [sid for f in fact_rows.values() if isinstance(f, dict) for sid in f.get("source_ids", [])])
        fact_source_ids = list(university.get("source_ids") or [])
        for fact in fact_rows.values():
            if isinstance(fact, dict): fact_source_ids.extend(fact.get("source_ids") or [])
        sources_section = '<section class="detail-sources"><h2>Official sources</h2>' + source_links(list(dict.fromkeys(fact_source_ids))) + '</section>'
        intro += note + links + programs + admissions_facts + sources_section + f'<p class="last-checked">Last reviewed: {esc(university.get("last_checked") or "Date not recorded")}</p>'
    else:
        intro += links + f'<p class="last-checked">Last reviewed: {esc(university.get("last_checked") or "Date not recorded")}</p>'
    return f'<article class="university-card" data-university-card data-name="{esc(university.get("name", ""))}" data-city="{esc(university.get("city", ""))}" data-region="{esc(university.get("region", ""))}">{intro}</article>'


def nav() -> str:
    return '''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="nav-shell"><a class="brand" href="/" aria-label="Italy University Tracker home"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span><span>Italy University<br><strong>Tracker</strong></span></a><nav aria-label="Main navigation"><a href="/#programs" data-i18n="navPrograms">Programs</a><a href="/#universities" data-i18n="navUniversities">Universities</a><a href="/guide/" data-i18n="navGuide">Application guide</a><a href="/about/" data-i18n="navAbout">About</a></nav><button class="language-toggle" type="button" id="language-toggle" aria-label="Change language to Italian" aria-pressed="false">IT</button></div></header>'''


def footer() -> str:
    return '''<footer class="site-footer"><div class="footer-grid"><div><a class="brand footer-brand" href="/"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span><span>Italy University<br><strong>Tracker</strong></span></a><p>Independent research for international applicants exploring IT degrees in Italy.</p></div><div><h2 data-i18n="footerExplore">Explore</h2><a href="/#programs">Programs</a><a href="/#universities">Universities</a><a href="/guide/">Application guide</a></div><div><h2 data-i18n="footerAbout">About this site</h2><a href="/about/">Scope and disclaimer</a><a href="/methodology/">Methodology</a><a href="/updates/">Review updates</a><a href="https://github.com/Aziz-Braiek/italy-it-programs/issues/new?template=correction.yml&amp;title=Correction%3A" target="_blank" rel="noopener noreferrer">Report a correction ↗</a></div></div><p class="footer-note">This independent tracker is not affiliated with Italian universities or government agencies. It is a research aid, not an application or immigration portal. Always follow the official notice for your program and applicant category.</p><p class="back-to-top"><a href="#top">Back to top ↑</a></p></footer>'''


def global_tools() -> str:
    return '''<div id="compare-tray" class="compare-tray" hidden><span id="compare-tray-label">0 programs selected</span><button class="small-button" id="open-compare" type="button">Compare selected</button><button class="icon-button" id="clear-compare" type="button" aria-label="Clear comparison">×</button></div><dialog id="compare-dialog" aria-labelledby="compare-title"><div class="dialog-head"><h2 id="compare-title">Compare programs</h2><button class="icon-button" id="close-compare" type="button" aria-label="Close comparison">×</button></div><div id="compare-content"></div></dialog>'''


def page(title: str, description: str, body: str, *, path: str = "/", noindex: bool = False, dataset_schema: bool = False) -> str:
    canonical = BASE + path
    robots_meta = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    schema = ""
    if dataset_schema:
        payload = {
            "@context": "https://schema.org",
            "@type": "Dataset",
            "name": "Italy University Tracker 2027/28 program research",
            "description": "A source-linked research dataset of international IT program listings at 34 selected Italian universities. Availability is marked per record; pending historical leads are not shown as confirmed offers.",
            "inLanguage": "en",
            "dateModified": TODAY.isoformat(),
            "url": canonical,
        }
        schema = '<script type="application/ld+json">' + json.dumps(payload, ensure_ascii=False).replace("</", "<\\/") + '</script>'
    return f'''<!doctype html><html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><title>{esc(title)}</title><meta name="description" content="{esc(description)}">{robots_meta}<link rel="canonical" href="{esc(canonical)}"><link rel="icon" type="image/png" href="/assets/favicon.png"><meta property="og:type" content="website"><meta property="og:url" content="{esc(canonical)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:image" content="{BASE}/assets/social-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{BASE}/assets/social-card.png"><link rel="stylesheet" href="/assets/site.css"><script defer src="/assets/site.js"></script>{schema}</head><body id="top">{nav()}<main id="main">{body}</main>{footer()}{global_tools()}<div id="site-announcer" class="sr-only" role="status" aria-live="polite" aria-atomic="true"></div><noscript><style>.requires-js{{display:none!important}}</style></noscript></body></html>'''


def homepage() -> str:
    confirmed = sum(p.get("overall_status") == "CONFIRMED" for p in PROGRAMS)
    pending = sum(p.get("overall_status") == "REQUIRES_VERIFICATION" for p in PROGRAMS)
    last_reviewed = max((p.get("last_checked", "") for p in PROGRAMS), default="")
    reviewed_date = datetime.strptime(last_reviewed, "%Y-%m-%d") if last_reviewed else None
    reviewed_display = f"{reviewed_date.day} {reviewed_date.strftime('%b %Y')}" if reviewed_date else "Date not recorded"
    city_opts = sorted({p.get("city") or UNIVERSITY_BY_ID[p["university_id"]].get("city", "") for p in PROGRAMS if p.get("city") or UNIVERSITY_BY_ID.get(p["university_id"], {}).get("city")})
    region_opts = sorted({u.get("region", "") for u in UNIVERSITIES if u.get("region")})
    fields = sorted({(p.get("field") or {}).get("value", "") for p in PROGRAMS if (p.get("field") or {}).get("value")})
    filter_html = f'''<details class="filter-panel" id="filter-panel" open><summary>Filter and sort programs</summary><div class="filter-grid">
<label class="filter-control filter-search"><span>Search</span><input id="search" type="search" placeholder="Program, university, city, or field" autocomplete="off"></label>
<label class="filter-control"><span>Degree level</span><select id="filter-level"><option value="">Any level</option><option value="BSc">Bachelor’s (BSc)</option><option value="MSc">Master’s (MSc)</option></select></label>
<label class="filter-control"><span>University</span><select id="filter-university"><option value="">Any university</option>{''.join(f'<option value="{esc(u["id"])}">{esc(u["name"])}</option>' for u in sorted(UNIVERSITIES, key=lambda x:x["name"]))}</select></label>
<label class="filter-control"><span>City or region</span><input id="filter-city" list="location-options" placeholder="Type a city or region"><datalist id="location-options">{''.join(f'<option value="{esc(value)}">' for value in city_opts + region_opts)}</datalist></label>
<label class="filter-control"><span>Teaching language</span><select id="filter-language"><option value="">Any language</option><option value="English">English</option><option value="Italian">Italian</option><option value="Mixed">Italian / English</option><option value="Unknown">Not confirmed</option></select></label>
<label class="filter-control"><span>Field of study</span><input id="filter-field" list="field-options" placeholder="Type a field"><datalist id="field-options">{''.join(f'<option value="{esc(value)}">' for value in fields)}</datalist></label>
<label class="filter-control"><span>Program status</span><select id="filter-status"><option value="">All statuses</option><option value="CONFIRMED">Available for 2027/28</option><option value="REQUIRES_VERIFICATION">Awaiting confirmation</option><option value="NOT_APPLICABLE">Not offered</option></select></label>
<label class="filter-control"><span>Application dates</span><select id="filter-deadline"><option value="">Any date status</option><option value="known">Confirmed future date</option><option value="pending">No confirmed future date</option></select></label>
<label class="filter-control"><span>Tuition information</span><select id="filter-tuition"><option value="">Any</option><option value="documented">2027/28 amount documented</option><option value="pending">No confirmed amount</option></select></label>
<label class="filter-control"><span>Scholarship information</span><select id="filter-scholarship"><option value="">Any</option><option value="documented">2027/28 information documented</option><option value="pending">No confirmed details</option></select></label>
<label class="filter-control"><span>Sort by</span><select id="sort-by"><option value="recommended">Confirmed availability first</option><option value="deadline">Next confirmed deadline</option><option value="university">University name</option><option value="program">Program name</option></select></label>
<div class="filter-actions"><label class="check-control"><input id="include-pending" type="checkbox"><span>Show programs awaiting confirmation</span></label><button class="text-button" type="button" id="show-favorites" aria-pressed="false">Saved programs</button><button class="text-button" type="button" id="clear-filters">Clear filters</button></div>
</div></details>'''
    cards = "".join(program_card(program) for program in PROGRAMS)
    university_cards = "".join(university_card(university) for university in sorted(UNIVERSITIES, key=lambda u:u["name"]))
    body = f'''<section class="hero"><div class="hero-inner"><div class="hero-copy"><p class="eyebrow light">INTERNATIONAL STUDENTS · ACADEMIC YEAR 2027/28</p><h1>Find your next step<br><span>in Italy.</span></h1><p class="hero-lede">Explore source-linked IT degree information at a curated group of Italian universities. See what is confirmed for 2027/28 and what is still waiting for an official update.</p><div class="hero-actions"><a class="button button-primary" href="#programs">Explore programs <span aria-hidden="true">↓</span></a><a class="button button-ghost" href="#universities">Browse universities</a></div><p class="hero-reviewed">Latest program review: {esc(reviewed_display)}</p></div><div class="hero-card"><p class="eyebrow">AT A GLANCE</p><div class="hero-stat"><strong>{len(UNIVERSITIES)}</strong><span>selected universities<br><small>from the earlier tracker scope</small></span></div><div class="hero-stat"><strong>{len(PROGRAMS)}</strong><span>program records<br><small>historical leads and new finds</small></span></div><div class="hero-stat"><strong>{confirmed}</strong><span>available for 2027/28<br><small>official core details verified</small></span></div><div class="hero-stat"><strong>{pending}</strong><span>awaiting confirmation<br><small>not current admission offers</small></span></div></div></div><div class="hero-orbit" aria-hidden="true"></div></section>
<section class="notice-band" aria-labelledby="notice-title"><div class="notice-icon" aria-hidden="true">i</div><div><h2 id="notice-title">Many 2027/28 calls are still being published</h2><p>{pending} program entries are waiting for program-specific confirmation. Earlier course listings can help you decide what to investigate, but they do not confirm a new intake. We add a current-year status only when the cited official evidence supports it.</p></div><a href="/methodology/">How statuses work <span aria-hidden="true">→</span></a></section>
<section class="section directory-section" id="programs"><div class="section-heading"><div><p class="eyebrow">SEARCH THE TRACKER</p><h2>Programs</h2><p>Filter by degree, location and admissions information. Save options on this device or share a filtered search.</p></div><div class="directory-tools"><button class="small-button" type="button" id="export-csv">Download shortlist CSV</button><button class="small-button" type="button" id="export-ics">Add confirmed deadlines to calendar</button></div></div><div class="status-legend" aria-label="Program status legend"><span><i class="legend-dot dot-confirmed"></i><strong>Available:</strong> official 2027/28 program evidence found</span><span><i class="legend-dot dot-pending"></i><strong>Awaiting confirmation:</strong> current intake not confirmed</span><span><i class="legend-dot dot-unavailable"></i><strong>Not offered:</strong> official evidence says no 2027/28 intake</span></div>{filter_html}<p class="result-count" id="result-count" aria-live="polite" aria-atomic="true">{len(PROGRAMS)} program records. Turn on “Show programs awaiting confirmation” to include pending entries after filtering.</p><noscript><p class="noscript-note">All {len(PROGRAMS)} program records are included below with their status. Use your browser’s find command to search. Interactive filters, saved programs and comparison need JavaScript.</p></noscript><div class="program-grid" id="program-grid">{cards}</div><div class="pagination" id="pagination" aria-label="Program result pages"><button class="small-button" id="page-previous" type="button">Previous</button><span id="page-summary" aria-live="polite"></span><button class="small-button" id="page-next" type="button">Next</button></div></section>
<section class="section university-section" id="universities"><div class="section-heading"><div><p class="eyebrow">INSTITUTION DIRECTORY</p><h2>Universities in this tracker</h2><p>This is a selected set carried forward from the original tracker—not a complete list of Italian universities.</p></div></div><label class="university-search"><span>Search universities by name or location</span><input type="search" id="university-search" placeholder="Type a university, city, or region" autocomplete="off"></label><p class="result-count" id="university-count" aria-live="polite">{len(UNIVERSITIES)} universities</p><div class="university-grid" id="university-grid">{university_cards}</div><p class="empty-state" id="university-empty" hidden>No universities match this search.</p></section>
<section class="guide-cta"><div><p class="eyebrow light">PLAN WITH OFFICIAL SOURCES</p><h2>New to applying in Italy?</h2><p>Start with a plain-language guide to university calls, international procedures, documents, costs and arrival steps.</p></div><a class="button button-primary" href="/guide/">Read the application guide <span aria-hidden="true">→</span></a></section>'''
    return page("Italy University Tracker 2027/28 | International IT Programs", f"Explore {len(PROGRAMS)} source-linked program records at {len(UNIVERSITIES)} selected Italian universities. See what is confirmed for 2027/28, compare options and follow official admissions sources.", body, dataset_schema=True)


def guide_page() -> str:
    body = '''<section class="page-hero"><p class="eyebrow light">INTERNATIONAL APPLICANTS</p><h1>Application guide</h1><p>Use this overview to plan questions and find official starting points. Requirements vary by university, program, citizenship, country of residence and degree. Your university and consulate instructions control.</p></section>
<div class="content-layout"><article class="prose"><div class="callout"><strong>Start with the program’s official call.</strong> General national guidance cannot replace a course-specific admission notice. Ask the university which procedure applies to your qualification and applicant category.</div>
<h2 id="university-applications">1. University applications</h2><p>Check the program page and the international admissions office. Confirm the course name and degree level, eligibility, document format, language proof, tests, application fee, selection steps and deadlines. A university-wide calendar may not apply to every program or applicant group.</p><p><a href="https://www.universitaly.it/en/studenti-stranieri" target="_blank" rel="noopener noreferrer">Universitaly: procedures for international students, valid for 2026/27 and 2027/28 ↗</a></p>
<h2 id="eu-non-eu">2. EU and non-EU routes</h2><p>Citizenship, residence status and where you live can change the application and visa steps. In general, non-EU applicants living abroad who need a study visa use the university’s admissions procedure and then the Universitaly pre-enrolment process described by the university. Do not assume that one deadline or document list applies to everyone.</p><p><a href="https://www.esteri.it/en/ministero/sportello_info/domandefrequenti/studiare-in-italia/" target="_blank" rel="noopener noreferrer">Italian Ministry of Foreign Affairs: Study in Italy FAQ ↗</a> · <a href="https://www.universitaly.it/en/studenti-stranieri" target="_blank" rel="noopener noreferrer">Universitaly international student procedures ↗</a></p>
<h2 id="documents">3. Qualifications and documents</h2><p>The university assesses whether your previous qualification meets the entry rules for the chosen course. It may ask for translations, legalization or additional documents based on your country and the course. Ask before paying for a credential service.</p><p>A <strong>Declaration of Value (DoV)</strong> is an informational document issued through an Italian diplomatic mission; it is not itself a formal recognition decision. <strong>CIMEA comparability or verification statements</strong> may help an institution assess a foreign qualification, but they do not automatically grant admission or replace the university’s own requirements. Ask the university whether it needs a DoV, a CIMEA statement, both, or another document.</p><p><a href="https://www.esteri.it/en/temi/diplomazia_culturale/universita/riconoscimento_titoli_studio/" target="_blank" rel="noopener noreferrer">Foreign qualifications and the Declaration of Value — MAECI ↗</a> · <a href="https://www.cimea.it/EN/pagina-attestati-di-comparabilita-e-verifica-dei-titoli" target="_blank" rel="noopener noreferrer">CIMEA: comparability and verification services ↗</a></p>
<h2 id="language-tests">4. Language certificates and entrance tests</h2><p>Check the course’s current call for accepted language certificates, minimum scores, exemption rules and certificate validity dates. The same is true for entrance exams: format, registration, dates and exemptions are course-specific. Do not carry forward a previous year’s test or certificate rule without checking the current notice.</p>
<h2 id="costs">5. Tuition, ISEE and scholarships</h2><p>Tuition can depend on the institution, degree, income documents, citizenship and other conditions. Compare only amounts that share the same year and fee basis. Ask the university about the process for international income documentation and any tuition reduction.</p><p>Many right-to-study benefits—such as grants, housing or meals—are managed through regional authorities. Each regional call sets its own economic and merit rules, documents and deadlines. A scholarship page does not guarantee eligibility or funding.</p><p><a href="https://www.mur.gov.it/it/aree-tematiche/universita/sportello-digitale-unico/applying-tertiary-education-funding-such" target="_blank" rel="noopener noreferrer">Ministry of University and Research: public student funding ↗</a> · <a href="https://www.universitaly.it/borse-studio" target="_blank" rel="noopener noreferrer">Universitaly: scholarships and benefits directory ↗</a> · <a href="https://www.inps.it/it/it/dettaglio-scheda.it.schede-servizio-strumento.schede-servizi.Portale-unico-ISEE.html" target="_blank" rel="noopener noreferrer">INPS: ISEE portal ↗</a></p>
<h2 id="visa">6. Study visa and pre-enrolment</h2><p>If a visa is required, check the Italian consulate responsible for your place of residence and follow the relevant university instructions for Universitaly pre-enrolment. University validation supports the process; it does not guarantee a visa appointment or visa issuance. Start early and use current official instructions.</p><p><a href="https://www.universitaly.it/en/studenti-stranieri" target="_blank" rel="noopener noreferrer">Universitaly: entry, residence and enrolment procedures ↗</a> · <a href="https://vistoperitalia.esteri.it/" target="_blank" rel="noopener noreferrer">Visa for Italy: check requirements by nationality and purpose ↗</a></p>
<h2 id="arrival">7. After arrival</h2><p>Students who enter Italy on a study visa generally need to complete the residence-permit process after arrival. Follow the current instructions from the Italian Police and your university’s international office, and keep copies of the documents submitted.</p><p><a href="https://poliziadistato.it/articolo/225-Il_rilascio_del_permesso_di_soggiorno" target="_blank" rel="noopener noreferrer">Polizia di Stato: residence-permit process ↗</a></p>
<h2 id="glossary">Glossary</h2><dl class="glossary"><dt>CFU / ECTS</dt><dd>Credit units used to describe course workload. Italian CFU and ECTS are generally aligned, but check each call’s academic requirements.</dd><dt>CIMEA</dt><dd>The Italian information centre on academic mobility and equivalence. Its statements support qualification assessment; they are not a university admission decision.</dd><dt>Declaration of Value (DoV)</dt><dd>An informational document about a foreign qualification issued by an Italian diplomatic mission. It does not itself recognize the qualification.</dd><dt>ISEE</dt><dd>An indicator used in Italy to assess a household’s economic situation for certain benefits. Ask the university or regional authority which ISEE route and documents apply to international applicants.</dd><dt>Pre-enrolment</dt><dd>A process for some international applicants who need a visa, completed through Universitaly according to the university’s instructions.</dd></dl>
<h2 id="faq">Frequently asked questions</h2><details class="faq"><summary>Does a tracker status mean I can apply?</summary><p>No. It summarizes the evidence linked here. Apply only through the university’s official process and confirm your eligibility directly with that institution.</p></details><details class="faq"><summary>Does a previous-year course listing prove the program is open in 2027/28?</summary><p>No. The tracker labels earlier evidence as historical. A current intake is marked available only when cited official evidence supports 2027/28.</p></details><details class="faq"><summary>Does Universitaly validation guarantee a visa?</summary><p>No. The visa decision is made by the competent diplomatic-consular office. University validation does not guarantee an appointment or visa issuance.</p></details><details class="faq"><summary>Where can I find regional scholarships?</summary><p>Start with the official regional right-to-study call for the university’s region. Deadlines, eligibility, documents and awards differ by region and year.</p></details><p class="source-note">Guide checked 10 November 2026. Official procedures can change; follow the latest instructions from the relevant university, region, ministry and consulate.</p></article><aside class="contents-card"><h2>On this page</h2><a href="#university-applications">University applications</a><a href="#eu-non-eu">EU / non-EU routes</a><a href="#documents">Documents</a><a href="#language-tests">Language and tests</a><a href="#costs">Tuition and aid</a><a href="#visa">Visa</a><a href="#arrival">After arrival</a><a href="#glossary">Glossary</a><a href="#faq">FAQ</a></aside></div>'''
    return page("International Application Guide for Italy 2027/28 | Italy University Tracker", "Official starting points for international students applying to Italian universities: admissions, qualifications, language, costs, scholarships, visas and arrival steps.", body, path="/guide/")


def about_page() -> str:
    available_count = sum(program.get("overall_status") == "CONFIRMED" for program in PROGRAMS)
    body = '''<section class="page-hero"><p class="eyebrow light">ABOUT THE TRACKER</p><h1>A focused guide to IT study in Italy</h1><p>Independent, source-linked research to help international students explore selected IT degrees and find the university information that matters next.</p></section><article class="prose narrow"><h2>What is in scope?</h2><p>The tracker follows a curated group of 34 universities carried forward from an earlier information-technology program tracker. It is not a directory of all Italian universities, and it does not cover every degree, institution type or language of instruction in Italy.</p><p>The word “IT” refers to information-technology study. Program records include computing and adjacent technology fields represented in the underlying research data.</p><h2>What this site can and cannot tell you</h2><p>Program entries point to official sources and separate current-cycle evidence from earlier listings and information that is still pending. The count of 23 records marked available means official 2027/28 evidence was found for the core program details; it is not a count of admissions decisions or a promise that every applicant is eligible.</p><p>This site is not an application portal, university service, government service or immigration adviser. It is not affiliated with the listed universities or Italian government agencies. Universities and relevant public authorities make admissions, qualification, funding and visa decisions.</p><h2>How to report an issue</h2><p>Each correction report is submitted as a GitHub issue with the program or university, the suggested correction and an official source. Reports are reviewed before changes are made. Please do not submit private documents or sensitive personal information.</p><p><a class="button button-primary" href="https://github.com/Aziz-Braiek/italy-it-programs/issues/new?template=correction.yml&amp;title=Correction%3A" target="_blank" rel="noopener noreferrer">Report a correction ↗</a></p><p>For detailed status definitions, source handling and counting rules, read the <a href="/methodology/">methodology</a>.</p></article>'''
    body = body.replace("group of 34 universities", f"group of {len(UNIVERSITIES)} universities")
    body = body.replace("count of 23 records", f"count of {available_count} records")
    return page("About | Italy University Tracker 2027/28", "The Italy University Tracker covers a selected set of 34 Italian institutions and explains the scope and limits of its information.", body, path="/about/")


def methodology_page() -> str:
    status_counts = {
        "confirmed": sum(program.get("overall_status") == "CONFIRMED" for program in PROGRAMS),
        "pending": sum(program.get("overall_status") in {"REQUIRES_VERIFICATION", "NOT_YET_PUBLISHED"} for program in PROGRAMS),
        "conflicting": sum(program.get("overall_status") == "CONFLICTING_SOURCES" for program in PROGRAMS),
        "unavailable": sum(program.get("overall_status") == "UNAVAILABLE" for program in PROGRAMS),
        "not_offered": sum(program.get("overall_status") == "NOT_APPLICABLE" for program in PROGRAMS),
    }
    count_items = (
        f'<li><strong>{len(UNIVERSITIES)} universities:</strong> institutions in this curated tracker scope.</li>'
        f'<li><strong>{len(PROGRAMS)} program records:</strong> prior tracker leads plus newer discoveries; some may be historical or still awaiting confirmation.</li>'
        f'<li><strong>{status_counts["confirmed"]} available:</strong> records whose overall status is CONFIRMED for 2027/28 with official core evidence.</li>'
        f'<li><strong>{status_counts["pending"]} awaiting confirmation:</strong> records that still need current-cycle verification or a published call.</li>'
        f'<li><strong>{status_counts["conflicting"]} sources needing review:</strong> records with unresolved conflicts in official evidence.</li>'
        f'<li><strong>{status_counts["unavailable"]} without a current offer found:</strong> records with no current offer evidence.</li>'
        f'<li><strong>{status_counts["not_offered"]} not offered:</strong> records with official evidence that the program will not run in 2027/28.</li>'
    )
    body = '''<section class="page-hero"><p class="eyebrow light">TRANSPARENCY</p><h1>How to read the information</h1><p>The public wording is simpler than the underlying research codes, but every status remains tied to the source evidence and review date.</p></section><article class="prose narrow"><h2>Program status</h2><dl class="status-definitions"><dt><span class="status status-confirmed">Available for 2027/28</span></dt><dd>An official source supports the current-cycle program identity and core details. This does not mean a student has been admitted or that all applicant categories are eligible.</dd><dt><span class="status status-pending">Awaiting 2027/28 confirmation</span></dt><dd>The record is a candidate or earlier listing. Current first-year availability has not been confirmed. Do not treat historical course facts as current admission terms.</dd><dt><span class="status status-unavailable">Not offered for 2027/28</span></dt><dd>The reviewed official information says the program will not run for this cycle.</dd></dl><h2>Field-level information</h2><p>A program can be pending while a separate field—such as application dates or fees—is supported by current-cycle evidence. Each field shows whether it is confirmed for 2027/28, remains unconfirmed, has not yet been announced, or comes from earlier-cycle evidence. A date is sorted or exported only if the relevant fact is marked confirmed and supported by a 2027/28 source.</p><h2>Counts</h2><ul><li><strong>34 universities:</strong> institutions in this curated tracker scope.</li><li><strong>193 program records:</strong> prior tracker leads plus newer discoveries; some may be historical or still awaiting confirmation.</li><li><strong>23 available:</strong> records whose overall status is CONFIRMED for 2027/28 with official core evidence.</li><li><strong>167 awaiting confirmation:</strong> program records that do not yet have sufficient current-cycle evidence for the core program identity.</li></ul><p>Counts are record counts, not unique courses or admissions opportunities. Multiple tracks under a shared course may appear separately when official evidence distinguishes them.</p><h2>Sources and review dates</h2><p>Links go to official university, ministry or other cited pages. The source record notes its title, date accessed, cycle and the facts it supports. A “Last reviewed” date shows when that record was last checked; it does not mean every fact changed or that the page remains current after that date.</p><h2>Dates, fees and scholarships</h2><p>The site does not infer missing deadlines, tuition values, scholarship eligibility, acceptance rates or availability. Amounts and dates should be compared only when the same cycle, applicant group and fee basis apply. A university-wide deadline is not assumed to apply to every program.</p><h2>Research limits</h2><p>Coverage is partial. An unlisted program may exist; a missing deadline may have been published after the record was checked; and some official pages may be difficult to access or may change without notice. Please confirm directly with the university before applying.</p><p><a href="/updates/">View recent record review dates</a> · <a href="/about/">Read the site scope</a></p></article>'''
    body = body.replace("<li><strong>34 universities:</strong> institutions in this curated tracker scope.</li><li><strong>193 program records:</strong> prior tracker leads plus newer discoveries; some may be historical or still awaiting confirmation.</li><li><strong>23 available:</strong> records whose overall status is CONFIRMED for 2027/28 with official core evidence.</li><li><strong>167 awaiting confirmation:</strong> program records that do not yet have sufficient current-cycle evidence for the core program identity.</li>", count_items)
    return page("Methodology and Status Definitions | Italy University Tracker", "Definitions for confirmed, pending and unavailable program records, source cycles, dates, tuition and tracker statistics.", body, path="/methodology/")


def updates_page() -> str:
    reviewed = sorted(PROGRAMS, key=lambda p: p.get("last_checked") or "", reverse=True)[:30]
    rows = "".join(
        f'<tr><td>{esc(p.get("last_checked") or "—")}</td><td><a href="/programs/{quote(p["id"], safe="")}/">{esc(p.get("program", "Program"))}</a></td><td>{esc(p.get("university", ""))}</td><td><span class="status status-{record_status(p.get("overall_status", ""))[1]}">{esc(record_status(p.get("overall_status", ""))[0])}</span></td></tr>'
        for p in reviewed
    )
    body = f'''<section class="page-hero"><p class="eyebrow light">REVIEW ACTIVITY</p><h1>Recent record checks</h1><p>A review date tells you when a record was last checked. It is not a change history and does not guarantee that the university has not published something since then.</p></section><section class="section narrow table-section"><div class="table-scroll"><table><caption>30 most recently reviewed program records</caption><thead><tr><th scope="col">Last checked</th><th scope="col">Program</th><th scope="col">University</th><th scope="col">2027/28 status</th></tr></thead><tbody>{rows}</tbody></table></div><p>We do not yet have a reliable historical snapshot for every individual field, so this page shows review dates rather than claiming a record of changes. <a href="/methodology/">Read the source and status method.</a></p></section>'''
    audit_path=ROOT/"research/independent-audit-2026-11/review-ledger.json"
    if audit_path.exists():
        audit=json.loads(audit_path.read_text(encoding="utf-8"))["metadata"]
        counts=audit["counts"]
        audit_section=f'<section class="section narrow prose"><h2>Independent evidence audit</h2><p>The review covers {counts["baseline_programs"]} program records, {counts["baseline_universities"]} universities and {counts["baseline_sources"]} original official source records. The ledger compares stored values with official evidence and records each academic year, applicant route, source and check date. Unpublished fields, inaccessible evidence and conflicting notices remain explicit.</p><p>Review status: {esc(audit["audit_state"].replace("_"," ").lower())}.</p><ul><li><a href="/data/independent-audit/correction-report.md" download>Correction report</a></li><li><a href="/data/independent-audit/review-ledger.json" download>Complete review ledger (JSON)</a></li><li><a href="/data/independent-audit/findings.json" download>Structured findings (JSON)</a></li><li><a href="/data/independent-audit/independent-audit-review.zip" download>Complete audit and data package (ZIP)</a></li></ul></section>'
        body=body.replace('<section class="section narrow table-section">',audit_section+'<section class="section narrow table-section">')
        body=body.replace('We do not yet have a reliable historical snapshot for every individual field, so this page shows review dates rather than claiming a record of changes.','The independent audit ledger records the original values, official findings and corrections. This table lists recent program check dates.')
    return page("Research Review Updates | Italy University Tracker 2027/28", "Recent review dates for program records in the Italy University Tracker.", body, path="/updates/")


FONT_5X7 = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01111", "10000", "10000", "10000", "10000", "10000", "01111"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01111", "10000", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "J": ("00111", "00010", "00010", "00010", "10010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "10101", "01010"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00010", "00100", "01000", "11111"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "/": ("00001", "00010", "00010", "00100", "01000", "01000", "10000"),
    "·": ("00000", "00000", "00000", "00100", "00100", "00000", "00000"),
    " ": ("00000",) * 7,
}


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def save_png(path: Path, width: int, height: int, pixels: bytearray) -> None:
    rows = b"".join(b"\x00" + pixels[y * width * 3:(y + 1) * width * 3] for y in range(height))
    data = b"\x89PNG\r\n\x1a\n" + png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) + png_chunk(b"IDAT", zlib.compress(rows, 9)) + png_chunk(b"IEND", b"")
    path.write_bytes(data)


def fill_rect(pixels: bytearray, width: int, height: int, box: tuple[int, int, int, int], color: tuple[int, int, int]) -> None:
    x0, y0, x1, y1 = box
    x0, y0, x1, y1 = max(0, x0), max(0, y0), min(width, x1), min(height, y1)
    row = bytes(color) * max(0, x1 - x0)
    for y in range(y0, y1):
        start = (y * width + x0) * 3
        pixels[start:start + len(row)] = row


def draw_bitmap_text(pixels: bytearray, width: int, height: int, x: int, y: int, text: str, scale: int, color: tuple[int, int, int]) -> None:
    cursor = x
    for character in text.upper():
        glyph = FONT_5X7.get(character, FONT_5X7[" "])
        for gy, row in enumerate(glyph):
            for gx, bit in enumerate(row):
                if bit == "1":
                    fill_rect(pixels, width, height, (cursor + gx * scale, y + gy * scale, cursor + (gx + 1) * scale, y + (gy + 1) * scale), color)
        cursor += 6 * scale


def generate_favicon() -> None:
    size = 64
    pixels = bytearray([255, 255, 255] * size * size)
    fill_rect(pixels, size, size, (4, 4, 23, 60), (0, 146, 70))
    fill_rect(pixels, size, size, (23, 4, 42, 60), (255, 255, 255))
    fill_rect(pixels, size, size, (42, 4, 60, 60), (206, 43, 55))
    save_png(OUT / "assets" / "favicon.png", size, size, pixels)


def generate_social_card() -> None:
    width, height = 1200, 630
    pixels = bytearray([244, 247, 250] * width * height)
    fill_rect(pixels, width, height, (42, 42, 1158, 588), (16, 35, 63))
    fill_rect(pixels, width, height, (875, 42, 1158, 588), (24, 60, 78))
    fill_rect(pixels, width, height, (920, 116, 958, 292), (0, 146, 70))
    fill_rect(pixels, width, height, (958, 116, 996, 292), (255, 255, 255))
    fill_rect(pixels, width, height, (996, 116, 1034, 292), (206, 43, 55))
    draw_bitmap_text(pixels, width, height, 100, 114, "INTERNATIONAL APPLICANTS", 4, (179, 207, 223))
    draw_bitmap_text(pixels, width, height, 100, 245, "FIND YOUR NEXT STEP", 8, (255, 255, 255))
    draw_bitmap_text(pixels, width, height, 100, 335, "IN ITALY", 8, (166, 220, 188))
    draw_bitmap_text(pixels, width, height, 102, 450, "2027/28 · ITALY UNIVERSITY TRACKER", 4, (229, 238, 245))
    save_png(OUT / "assets" / "social-card.png", width, height, pixels)


def write_site() -> None:
    root = ROOT.resolve()
    output = OUT.resolve()
    if not output.is_relative_to(root):
        raise RuntimeError(f"Refusing to clear output outside repository: {output}")
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "data").mkdir()
    for asset in ("site.css", "site.js"):
        shutil.copy2(ROOT / "site" / asset, OUT / "assets" / asset)
    for filename in ("programs-2027-2028.json", "universities-2027-2028.json", "sources.json"):
        shutil.copy2(ROOT / "research" / filename, OUT / "data" / filename)
    audit_dir=ROOT/"research/independent-audit-2026-11"
    if (audit_dir/"approved-corrections.json").exists():
        package_spec=importlib.util.spec_from_file_location("independent_review_package",ROOT/"scripts/build_independent_review_package.py")
        package_module=importlib.util.module_from_spec(package_spec)
        package_spec.loader.exec_module(package_module)
        package_module.build()
        destination=OUT/"data/independent-audit"
        destination.mkdir()
        for filename in ("correction-report.md","review-ledger.json","findings.json","approved-corrections.json"):
            shutil.copy2(audit_dir/filename,destination/filename)
        shutil.copy2(ROOT/"review-package/independent-audit-review.zip",destination/"independent-audit-review.zip")
    generate_social_card()
    generate_favicon()
    (OUT / "index.html").write_text(homepage(), encoding="utf-8")
    (OUT / "guide" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (OUT / "guide" / "index.html").write_text(guide_page(), encoding="utf-8")
    (OUT / "about" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (OUT / "about" / "index.html").write_text(about_page(), encoding="utf-8")
    (OUT / "methodology" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (OUT / "methodology" / "index.html").write_text(methodology_page(), encoding="utf-8")
    (OUT / "updates" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (OUT / "updates" / "index.html").write_text(updates_page(), encoding="utf-8")
    indexable_urls = ["/", "/guide/", "/about/", "/methodology/", "/updates/"]
    for university in UNIVERSITIES:
        path = f"/universities/{quote(university['id'], safe='')}/"
        body = f'<section class="page-hero"><p class="eyebrow light">{esc(university.get("city", ""))} · {esc(university.get("region", ""))}</p><h1>{esc(university.get("name", "University"))}</h1><p>Official admissions links, program records and source-linked information reviewed for the 2027/28 academic year.</p></section><section class="section detail-page">{university_card(university, detailed=True)}</section>'
        (OUT / "universities" / quote(university["id"], safe="") / "index.html").parent.mkdir(parents=True, exist_ok=True)
        (OUT / "universities" / quote(university["id"], safe="") / "index.html").write_text(page(f'{university["name"]} 2027/28 | Italy University Tracker', f'International admissions links and IT program records at {university["name"]} in {university.get("city", "Italy")}.', body, path=path), encoding="utf-8")
        indexable_urls.append(path)
    for program in PROGRAMS:
        path = "/programs/" + quote(program["id"], safe="") + "/"
        uni = UNIVERSITY_BY_ID.get(program["university_id"], {})
        level, current = verified_or_previous(program, "level")
        status_text, _ = record_status(program.get("overall_status", ""))
        subtitle = f'{uni.get("name", program.get("university", ""))} · {program.get("city") or uni.get("city", "")}'
        body = f'<section class="page-hero"><p class="eyebrow light">{esc(subtitle)}</p><h1>{esc(program.get("program", "Program"))}</h1><p>{esc(level + (" · verified for 2027/28" if current else " · earlier listing")) if level else "Degree level not confirmed"}</p><p><span class="status status-{record_status(program.get("overall_status", ""))[1]}" data-status-copy="{esc(program.get("overall_status", ""))}">{esc(status_text)}</span></p></section><section class="section detail-page">{program_card(program, detailed=True)}<p class="last-checked">Last reviewed: {esc(program.get("last_checked") or "Date not recorded")}</p><p><a href="/universities/{quote(program["university_id"], safe="")}/">See {esc(uni.get("name", "university"))} in the university directory</a></p></section>'
        noindex = program.get("overall_status") != "CONFIRMED"
        (OUT / "programs" / quote(program["id"], safe="") / "index.html").parent.mkdir(parents=True, exist_ok=True)
        (OUT / "programs" / quote(program["id"], safe="") / "index.html").write_text(page(f'{program.get("program", "Program")} · {uni.get("name", "University")} 2027/28', f'{status_text} — source-linked admissions information and official sources for {program.get("program", "this program")} at {uni.get("name", "the university")}.', body, path=path, noindex=noindex), encoding="utf-8")
        if not noindex:
            indexable_urls.append(path)
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /data/\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    sitemap_entries = "\n".join(f"  <url><loc>{BASE}{esc(url)}</loc></url>" for url in indexable_urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_entries}\n</urlset>\n', encoding="utf-8")
    print(f"Built {len(PROGRAMS)} program pages, {len(UNIVERSITIES)} university pages, and {len(indexable_urls)} sitemap URLs in {OUT}")


if __name__ == "__main__":
    write_site()
