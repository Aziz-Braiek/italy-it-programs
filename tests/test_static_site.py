from __future__ import annotations

import importlib.util
import json
import re
import unittest
from copy import deepcopy
from datetime import date
from unittest.mock import patch
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SPEC = importlib.util.spec_from_file_location("build_site", ROOT / "scripts" / "build_site.py")
BUILD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(BUILD)


def read(path: str) -> str:
    return (DIST / path).read_text(encoding="utf-8")


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict[str, str | None]]] = []
        self.text: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self._heading_level: int | None = None
        self._heading_text: list[str] = []
        self.anchors: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.tags.append((tag, values))
        if tag.startswith("h") and tag[1:].isdigit():
            self._heading_level = int(tag[1:])
            self._heading_text = []
        if tag == "a":
            self.anchors.append(values)

    def handle_endtag(self, tag: str) -> None:
        if self._heading_level and tag == f"h{self._heading_level}":
            self.headings.append((self._heading_level, "".join(self._heading_text).strip()))
            self._heading_level = None

    def handle_data(self, data: str) -> None:
        self.text.append(data)
        if self._heading_level:
            self._heading_text.append(data)


def parse(html: str) -> DocumentParser:
    parser = DocumentParser()
    parser.feed(html)
    return parser


class StaticSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not (DIST / "index.html").exists():
            BUILD.write_site()
        cls.programs = BUILD.PROGRAMS
        cls.universities = BUILD.UNIVERSITIES

    def test_homepage_has_real_content_in_initial_html(self) -> None:
        homepage = read("index.html")
        parsed = parse(homepage)
        cards = [attrs for tag, attrs in parsed.tags if tag == "article" and "program-card" in (attrs.get("class") or "")]
        universities = [attrs for tag, attrs in parsed.tags if tag == "article" and "university-card" in (attrs.get("class") or "")]
        self.assertEqual(len(cards), len(self.programs))
        self.assertEqual(len(universities), len(self.universities))
        page_text = "".join(parsed.text)
        for record in self.programs:
            self.assertIn(f'id="program-{record["id"]}"', homepage)
            self.assertIn(BUILD.public_text(record["program"]), page_text)
        for item in self.universities:
            self.assertIn(item["name"], [attrs.get("data-name") for attrs in universities])
        self.assertNotIn("Loading program records", homepage)
        self.assertNotIn("Loading university records", homepage)

    def test_static_output_has_no_data_fetch_dependency(self) -> None:
        javascript = (DIST / "assets" / "site.js").read_text(encoding="utf-8")
        self.assertNotRegex(javascript, r"\bfetch\s*\(")
        self.assertIn("need JavaScript", read("index.html"))
        self.assertIn("data-program-card", read("index.html"))
        self.assertIn("data-university-card", read("index.html"))

    def test_program_status_and_historical_evidence_are_labeled(self) -> None:
        homepage = read("index.html")
        cards = [attrs for tag, attrs in parse(homepage).tags if tag == "article" and "program-card" in (attrs.get("class") or "")]
        for status in ("CONFIRMED", "REQUIRES_VERIFICATION", "NOT_APPLICABLE"):
            self.assertEqual(
                sum(attrs.get("data-status") == status for attrs in cards),
                sum(program["overall_status"] == status for program in self.programs),
                f"homepage card status count matches the research data for {status}",
            )
        self.assertIn("Available for 2027/28", homepage)
        self.assertIn("Awaiting 2027/28 confirmation", homepage)
        self.assertIn("Earlier listing:", homepage)
        self.assertIn("Earlier evidence does not confirm a 2027/28 intake", read("programs/legacy-001/index.html"))
        not_applicable = next(p for p in self.programs if p["overall_status"] == "NOT_APPLICABLE")
        detail = read(f'programs/{not_applicable["id"]}/index.html')
        self.assertIn("Not offered for 2027/28", detail)
        self.assertIn('name="robots" content="noindex,follow"', detail)

    def test_confirmed_program_detail_and_university_pages_are_generated(self) -> None:
        for program in self.programs:
            path = DIST / "programs" / program["id"] / "index.html"
            self.assertTrue(path.is_file(), str(path))
        for university in self.universities:
            path = DIST / "universities" / university["id"] / "index.html"
            self.assertTrue(path.is_file(), str(path))
            content = path.read_text(encoding="utf-8")
            self.assertIn(university["name"], "".join(parse(content).text))
            self.assertIn('rel="canonical"', content)
        confirmed = next(p for p in self.programs if p["overall_status"] == "CONFIRMED")
        detail = read(f'programs/{confirmed["id"]}/index.html')
        self.assertIn('name="robots" content="index,follow,max-image-preview:large"', detail)
        self.assertIn(confirmed["program"], detail)
        self.assertIn("Official sources", detail)

    def test_only_source_supported_future_deadlines_are_used(self) -> None:
        for program in self.programs:
            candidates = BUILD.date_candidates(program)
            if program["overall_status"] != "CONFIRMED":
                self.assertEqual(candidates, [])
            for _, _, key in candidates:
                fact = program["facts"][key]
                self.assertEqual(fact["status"], "CONFIRMED")
                cycles = BUILD.record_source_cycles(fact.get("source_ids"))
                self.assertIn(BUILD.CURRENT_CYCLE, cycles)
            html = read(f'programs/{program["id"]}/index.html')
            if candidates:
                self.assertIn("Next confirmed date", html)
        self.assertIn('id="filter-deadline"', read("index.html"))
        self.assertIn('value="deadline"', read("index.html"))

    def test_confirmed_application_windows_are_all_available_for_calendar_export(self) -> None:
        program = next(p for p in self.programs if p["id"] == "legacy-020")
        candidates = BUILD.date_candidates(program)
        self.assertEqual(len(candidates), 3)
        homepage = parse(read("index.html"))
        card = next(attrs for tag, attrs in homepage.tags if tag == "article" and attrs.get("data-program-id") == "legacy-020")
        events = json.loads(card["data-deadlines"] or "[]")
        self.assertEqual([event["date"] for event in events], [candidate[0] for candidate in candidates])
        self.assertTrue(all(event["type"] == "window" for event in events))
        self.assertTrue(all(event["eligible"] for event in events))
        self.assertIn('id="top"', read("index.html"))
        self.assertIn('href="#top">Back to top', read("index.html"))

    def test_search_controls_urls_and_applicant_features_are_present(self) -> None:
        homepage = read("index.html")
        for control in ("search", "filter-level", "filter-university", "filter-city", "filter-language", "filter-field", "filter-status", "filter-deadline", "filter-tuition", "filter-scholarship", "sort-by"):
            self.assertIn(f'id="{control}"', homepage)
        for feature in ("data-favorite=", "data-compare=", "export-csv", "export-ics", "aria-live=\"polite\"", "id=\"compare-dialog\""):
            self.assertIn(feature, homepage)
        js = (DIST / "assets" / "site.js").read_text(encoding="utf-8")
        for behavior in ("history.replaceState", "localStorage", "text/calendar", "text/csv", "showModal", "Next confirmed application date"):
            self.assertIn(behavior, js)

    def test_dark_only_pages_do_not_depend_on_theme_preferences(self) -> None:
        homepage = read("index.html")
        self.assertIn('<html lang="en" data-theme="dark">', homepage)
        self.assertIn('<meta name="color-scheme" content="dark">', homepage)
        self.assertNotIn('id="theme-toggle"', homepage)
        self.assertNotIn('itu-tracker-theme-v2', homepage)
        for path in DIST.rglob("index.html"):
            document = path.read_text(encoding="utf-8")
            self.assertIn('data-theme="dark"', document, str(path))
            self.assertNotIn('id="theme-toggle"', document, str(path))
        css = (DIST / "assets" / "site.css").read_text(encoding="utf-8")
        self.assertIn('color-scheme: dark', css)
        self.assertNotIn('color-scheme: light', css)
        self.assertIn('--canvas: #111a26', css)
        javascript = (DIST / "assets" / "site.js").read_text(encoding="utf-8")
        self.assertNotIn('themeToLight', javascript)
        self.assertNotIn('itu-tracker-theme-v2', javascript)

    def test_seo_canonical_sitemap_and_robots(self) -> None:
        homepage = read("index.html")
        for token in ('name="description"', 'rel="canonical"', 'property="og:image"', 'name="twitter:card"', 'application/ld+json'):
            self.assertIn(token, homepage)
        self.assertIn('"@type": "Dataset"', homepage)
        self.assertNotIn('"@type": "Course"', homepage)
        sitemap = read("sitemap.xml")
        self.assertEqual(
            sitemap.count("<url>"),
            len(self.universities) + sum(program["overall_status"] == "CONFIRMED" for program in self.programs) + 5,
        )
        for university in self.universities:
            self.assertIn(f"/universities/{university['id']}/", sitemap)
        for program in self.programs:
            present = f"/programs/{program['id']}/" in sitemap
            self.assertEqual(present, program["overall_status"] == "CONFIRMED")
        robots = read("robots.txt")
        self.assertIn("Sitemap: https://italy-it-programs.vercel.app/sitemap.xml", robots)
        self.assertIn("Disallow: /data/", robots)
        self.assertTrue((DIST / "assets" / "social-card.png").is_file())

    def test_guide_scope_methodology_and_correction_link(self) -> None:
        guide = read("guide/index.html")
        for url in ("universitaly.it", "esteri.it", "cimea.it", "mur.gov.it", "inps.it", "poliziadistato.it"):
            self.assertIn(url, guide)
        for section in ("EU and non-EU routes", "CIMEA", "Declaration of Value", "ISEE", "residence-permit"):
            self.assertIn(section.lower(), guide.lower())
        about = read("about/index.html")
        self.assertIn("not a directory of all Italian universities", " ".join(parse(about).text))
        self.assertIn("not affiliated", about)
        self.assertIn("template=correction.yml", about)
        self.assertTrue((ROOT / ".github" / "ISSUE_TEMPLATE" / "correction.yml").is_file())
        methodology = read("methodology/index.html")
        self.assertIn("acceptance rates", methodology.lower())

    def test_accessible_structure_and_all_core_assets(self) -> None:
        homepage = read("index.html")
        parser = parse(homepage)
        self.assertTrue(any(tag == "nav" for tag, _ in parser.tags))
        self.assertTrue(any(tag == "main" and attrs.get("id") == "main" for tag, attrs in parser.tags))
        self.assertTrue(any(tag == "div" and attrs.get("aria-live") == "polite" for tag, attrs in parser.tags))
        self.assertEqual(sum(level == 1 for level, _ in parser.headings), 1)
        self.assertIn("Skip to content", homepage)
        for asset in ("site.css", "site.js", "favicon.png", "social-card.png"):
            self.assertTrue((DIST / "assets" / asset).is_file())
        css = (DIST / "assets" / "site.css").read_text(encoding="utf-8")
        self.assertIn("@media (max-width: 680px)", css)
        self.assertIn("focus-visible", css)
        self.assertIn("prefers-reduced-motion", css)

    def test_known_bad_sapienza_url_is_replaced_in_dataset(self) -> None:
        source = next(s for s in BUILD.SOURCES if s["id"] == "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026")
        self.assertTrue(source["url"].endswith("academic_requirements_movein_2026-2027_web.pdf"))
        self.assertNotIn("_web_1.pdf", source["url"])

    def test_scope_metadata_and_legacy_sort_name(self) -> None:
        home = read("index.html")
        self.assertIn("Italy University Tracker 2027/28 | International Programs", home)
        for path in ("index.html", "about/index.html", "methodology/index.html"):
            self.assertNotRegex(read(path), r"IT (?:degrees|programs|study)|information-technology study")
        self.assertIn("all fields", home)
        self.assertIn('value="availability"', home)
        self.assertNotIn('value="recommended"', home)
        self.assertIn("then university name, then program name", read("methodology/index.html"))

    def test_visible_sentinel_and_degree_link_lints(self) -> None:
        for text in ("REQUIRES_VERIFICATION", "NOT_YET_PUBLISHED", "Unresolved", "unresolved", "REQUIRES_<b>VERIFICATION</b>"):
            with self.assertRaises(ValueError, msg=text):
                BUILD.lint_visible_text(f"<p>{text}</p>")
        BUILD.lint_visible_text('<p data-status="REQUIRES_VERIFICATION">Not confirmed</p><script>const x="REQUIRES_VERIFICATION";</script>')
        for document in DIST.rglob("*.html"):
            BUILD.lint_visible_text(document.read_text(encoding="utf-8"), str(document))
        for level, wrong in (("MSc", "bachelor-s-degree-programmes"), ("BSc", "master-s-degree-programmes")):
            record = {"id": "lint-fixture", "level": {"value": level}}
            with self.assertRaises(ValueError):
                BUILD.lint_degree_link(record, f"https://example.edu/{wrong}/")
        BUILD.lint_degree_link({"id": "shared-parent", "level": {"value": "MSc"}}, "https://example.edu/bachelors-and-masters-degree-programs/second-cycle-degree-course/computer-engineering")

    def test_course_source_links_and_joint_degree_context(self) -> None:
        programs = {p["id"]: p for p in self.programs}
        url, label = BUILD.primary_official_link(programs["legacy-095"])
        self.assertIn("computer_science-93169", url)
        self.assertEqual(label, "Official program source")
        for p in self.programs:
            url, _ = BUILD.primary_official_link(p)
            BUILD.lint_degree_link(p, url)
            if p["university_id"] == "politecnico-torino" and BUILD.verified_or_previous(p, "level")[0] == "MSc":
                card = BUILD.program_card(p)
                self.assertIn("University master’s admissions page", card)
                self.assertNotIn("bachelor-s-degree-programmes", card)
        self.assertIn("Joint Polimi–Bocconi degree", read("programs/legacy-002/index.html"))
        self.assertIn("Bocconi administers", read("programs/legacy-002/index.html"))
        self.assertIsNone(programs["discovered-022"]["language"]["value"])
        self.assertIn("Language: Not confirmed", BUILD.program_card(programs["discovered-022"]))
        self.assertIn("Degree: Not confirmed", BUILD.program_card(programs["legacy-007"]))

    def test_application_badges_require_confirmed_scope_and_opening(self) -> None:
        record = {"id": "date-fixture", "overall_status": "CONFIRMED", "facts": {"application_windows": {"status": "CONFIRMED", "source_ids": ["SRC-PISA-CALL-2027"], "value": [{"start": "2026-11-01", "end": "2026-11-15", "eligible_group": "Non-EU abroad"}]}}}
        with patch.object(BUILD, "TODAY", date(2026, 11, 13)):
            self.assertIn("Applications open · Non-EU abroad", BUILD.application_badges(record))
            self.assertIn("Deadline known", BUILD.application_badges(record))
            with patch.object(BUILD, "TODAY", date(2026, 11, 15)):
                self.assertNotIn("Applications open", BUILD.application_badges(record), "unknown closing times must not imply an open round on its last day")
            del record["facts"]["application_windows"]["value"][0]["start"]
            self.assertNotIn("Applications open", BUILD.application_badges(record))
            self.assertIn("Deadline known", BUILD.application_badges(record))
            record["overall_status"] = "REQUIRES_VERIFICATION"
            self.assertNotIn("Program confirmed", BUILD.application_badges(record))
            self.assertNotIn("Applications open", BUILD.application_badges(record))
            record["overall_status"] = "CONFIRMED"
            record["facts"]["application_windows"].update(value=None, status="CONFLICTING_SOURCES")
            self.assertIn("need clarification", BUILD.application_badges(record))
            record["facts"]["application_windows"]["status"] = "NOT_YET_PUBLISHED"
            self.assertIn("Deadline not yet published", BUILD.application_badges(record))

    def test_previous_dates_never_feed_sort_or_calendar(self) -> None:
        record = deepcopy(next(p for p in self.programs if p["id"] == "legacy-011"))
        with patch.object(BUILD, "TODAY", date(2026, 11, 13)):
            historical = BUILD.previous_cycle_dates(record)
            self.assertIn("Previous cycle (estimate only, not a confirmed 2027/28 date)", historical)
            self.assertIn("2026-11-17", historical)
            self.assertIn("2026/27", historical)
            self.assertIn("EU applicants and non-EU applicants residing in Italy", historical)
            self.assertEqual(BUILD.date_candidates(record), [])
            self.assertEqual(BUILD.deadline_display(record), "")
            attrs = BUILD.program_data_attrs(record)
            self.assertIn('data-deadline=""', attrs)
            self.assertIn('data-deadlines="[]"', attrs)
            self.assertNotIn("2026-11-17", attrs)
            visa_applicant = next(p for p in self.programs if p["id"] == "legacy-058")
            self.assertIn("2026-04-30", BUILD.previous_cycle_dates(visa_applicant), "visa-applicant admissions are distinct from the later visa process")
            record["overall_status"] = "CONFIRMED"
            record["facts"]["application_deadline"] = {"value": {"date": "2026-11-12"}, "status": "CONFIRMED", "source_ids": ["SRC-PISA-CALL-2027"]}
            self.assertEqual(BUILD.previous_cycle_dates(record), "", "an expired current-cycle deadline is not a missing deadline")


if __name__ == "__main__":
    unittest.main(verbosity=2)
