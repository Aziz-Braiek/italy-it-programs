from __future__ import annotations

import importlib.util
import json
import re
import unittest
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
        self.assertEqual(len(cards), 193)
        self.assertEqual(len(universities), 34)
        page_text = "".join(parsed.text)
        for record in self.programs:
            self.assertIn(f'id="program-{record["id"]}"', homepage)
            self.assertIn(record["program"], page_text)
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
        self.assertEqual(sum(p["overall_status"] == "CONFIRMED" for p in self.programs), 23)
        self.assertEqual(sum(p["overall_status"] == "REQUIRES_VERIFICATION" for p in self.programs), 167)
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

    def test_seo_canonical_sitemap_and_robots(self) -> None:
        homepage = read("index.html")
        for token in ('name="description"', 'rel="canonical"', 'property="og:image"', 'name="twitter:card"', 'application/ld+json'):
            self.assertIn(token, homepage)
        self.assertIn('"@type": "Dataset"', homepage)
        self.assertNotIn('"@type": "Course"', homepage)
        sitemap = read("sitemap.xml")
        self.assertEqual(sitemap.count("<url>"), 62)
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
