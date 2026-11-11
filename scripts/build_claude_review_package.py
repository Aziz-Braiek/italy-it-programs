#!/usr/bin/env python3
"""Package the saved research snapshot for an independent review in Claude Web.

This is a read-only consumer of research/. It preserves the original files and
adds self-contained university upload batches, issue indexes and preview links.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import re
import subprocess
import zipfile
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_URL = "https://italy-it-programs.vercel.app"
INPUT_NAMES = (
    "programs-2027-2028.json",
    "universities-2027-2028.json",
    "sources.json",
    "coverage-report.json",
    "claude-review-checklist.md",
    "claude-review-manifest.json",
    "2027-2028-final-report.md",
    "research-progress.json",
)
CORE_DATA_NAMES = (
    "programs-2027-2028.json", "universities-2027-2028.json",
    "sources.json", "coverage-report.json",
)
OPTIONAL_INPUT_NAMES = ("claude-review-handoff.md", "preview-verification-report.md", "preview-http-verification.json", "claude-review-target.json")
REVIEW_STATUSES = {
    "REQUIRES_VERIFICATION", "NOT_YET_PUBLISHED", "UNAVAILABLE",
    "CONFLICTING_SOURCES",
}


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8",
    ).strip()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def review_url(base: str | None, path: str) -> str | None:
    """Carry a deployment's optional share query to every cookie-free page URL."""
    if not base:
        return None
    parsed = urlsplit(base)
    return urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, ""))


class BodyTextParser(HTMLParser):
    """Extract static body content, including the expandable admissions facts."""

    VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
    BLOCK_TAGS = {
        "address", "article", "aside", "blockquote", "button", "dd", "details",
        "div", "dl", "dt", "fieldset", "figcaption", "figure", "footer", "form",
        "h1", "h2", "h3", "h4", "h5", "h6", "header", "hr", "li", "main",
        "nav", "ol", "p", "pre", "section", "summary", "table", "tbody", "td",
        "th", "thead", "tr", "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_body = False
        self.saw_body = False
        self.skip_depth = 0
        self.parts: list[str] = []
        self.anchors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "body":
            self.in_body = self.saw_body = True
        if not self.in_body:
            return
        attributes = dict(attrs)
        is_void = tag in self.VOID_TAGS
        if self.skip_depth:
            if not is_void:
                self.skip_depth += 1
            return
        inline_style = re.sub(r"\s+", "", attributes.get("style") or "").lower()
        classes = (attributes.get("class") or "").split()
        suppressed = (
            tag in {"script", "style", "template"}
            or "hidden" in attributes
            or attributes.get("aria-hidden") == "true"
            or "sr-only" in classes
            or "display:none" in inline_style
            or "visibility:hidden" in inline_style
            or (tag == "dialog" and "open" not in attributes)
        )
        if suppressed:
            if not is_void:
                self.skip_depth = 1
            return
        if tag in self.BLOCK_TAGS or tag == "br":
            self.parts.append("\n")
        if tag == "li":
            self.parts.append("- ")
        if tag == "a":
            self.anchors.append(attributes.get("href") or "")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if not self.in_body:
            return
        if self.skip_depth:
            if tag not in self.VOID_TAGS:
                self.skip_depth -= 1
            return
        if tag == "a" and self.anchors:
            href = self.anchors.pop()
            if href and href != "#":
                self.parts.append(f" [link: {href}] ")
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        if tag == "body":
            self.in_body = False

    def handle_data(self, data: str) -> None:
        if self.in_body and not self.skip_depth:
            text = re.sub(r"\s+", " ", data).strip()
            if text:
                self.parts.append(text + " ")

    def text(self) -> str:
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in "".join(self.parts).splitlines()]
        result = "\n".join(line for line in lines if line)
        if not self.saw_body or not result:
            raise ValueError("An included HTML page has no extractable body text")
        return result + "\n"


def website_snapshot_payloads(
    programs: list[dict[str, Any]], universities: list[dict[str, Any]],
    preview_url: str | None, snapshot_commit: str,
) -> tuple[dict[str, bytes], dict[str, str], dict[str, Any]]:
    """Include every detail page only after matching captured live HTML hashes."""
    dist = ROOT / "dist"
    if not dist.is_dir():
        raise ValueError("dist/ is missing. Run python scripts/build_site.py before building the Claude review package.")
    proof_path = ROOT / "research" / "preview-http-verification.json"
    if not proof_path.is_file():
        raise ValueError("research/preview-http-verification.json is missing; capture and save the live preview HTTP verification before packaging offline website snapshots.")
    proof = json.loads(proof_path.read_text(encoding="utf-8"))
    if proof.get("deployment_commit") != snapshot_commit:
        raise ValueError("Live preview verification commit does not match the saved research snapshot commit")
    if preview_url and urlsplit(preview_url).netloc != urlsplit(proof.get("preview_origin") or "").netloc:
        raise ValueError("Requested preview origin does not match the captured live preview verification")
    checks = {entry["path"]: entry for entry in proof.get("results", [])}
    if len(checks) != len(proof.get("results", [])):
        raise ValueError("Live preview verification contains duplicate paths")
    records = [
        *(('university', record, f"/universities/{record['id']}/") for record in universities),
        *(('program', record, f"/programs/{record['id']}/") for record in programs),
    ]
    payloads: dict[str, bytes] = {}
    page_entries: list[dict[str, Any]] = []
    texts_by_university: dict[str, list[str]] = {record["id"]: [] for record in universities}
    for record_type, record, path in records:
        uid = record["id"] if record_type == "university" else record["university_id"]
        local_path = dist / path.strip("/") / "index.html"
        if not local_path.is_file():
            raise ValueError(f"Missing detail HTML: {local_path}. Run python scripts/build_site.py.")
        html_bytes = local_path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest = sha256(html_bytes)
        check = checks.get(path)
        if not check or check.get("status") != 200 or not check.get("same_origin") or check.get("final_path") != path:
            raise ValueError(f"No successful exact-path live preview verification for {path}")
        if digest != check.get("sha256"):
            raise ValueError(f"Normalized-LF HTML hash differs from the captured live preview response for {path}: local={digest}; live={check.get('sha256')}. Rebuild or recapture verification; no page is skipped.")
        package_html_path = f"website-html{path}index.html"
        payloads[package_html_path] = html_bytes
        parser = BodyTextParser()
        parser.feed(html_bytes.decode("utf-8"))
        parser.close()
        page_url = review_url(preview_url, path)
        entry = {
            "record_type": record_type, "record_id": record["id"],
            "university_id": uid, "page_path": path, "page_url": page_url,
            "html_file": package_html_path, "html_sha256_lf": digest,
            "live_response_sha256": check["sha256"], "live_http_status": check["status"],
            "live_verified_at_utc": proof.get("checked_at_utc"),
            "text_file": f"website-snapshots/{uid}.txt",
        }
        page_entries.append(entry)
        texts_by_university[uid].append("\n".join([
            "=" * 72,
            f"RECORD TYPE: {record_type}", f"STABLE RECORD ID: {record['id']}",
            f"UNIVERSITY ID: {uid}", f"PAGE PATH: {path}",
            f"PREVIEW PAGE URL: {page_url or 'Pending preview share URL'}",
            f"HTML FILE: {package_html_path}", f"NORMALIZED-LF HTML SHA256: {digest}",
            f"MATCHING LIVE RESPONSE SHA256: {check['sha256']}",
            f"LIVE HTTP STATUS: {check['status']}; CHECKED AT UTC: {proof.get('checked_at_utc')}",
            "", "STATIC BODY TEXT (includes expandable admissions details; link targets appended):", "",
            parser.text(),
        ]))
    if len(page_entries) != len(programs) + len(universities):
        raise ValueError("Offline website snapshot page count is incomplete")
    text_paths = {uid: f"website-snapshots/{uid}.txt" for uid in texts_by_university}
    for uid, sections in texts_by_university.items():
        heading = "\n".join([
            "ITALY UNIVERSITY TRACKER — OFFLINE WEBSITE REVIEW SNAPSHOT",
            f"UNIVERSITY ID: {uid}", f"RESEARCH DATASET COMMIT: {snapshot_commit}",
            f"LIVE PREVIEW ORIGIN: {proof.get('preview_origin')}",
            "", "Every included HTML page matches the captured live response SHA256 after normalizing line endings to LF.",
            "Body text excludes scripts, styles, decorative/hidden UI and closed comparison dialogs. Expandable admissions facts are included in source order. HTML originals are preserved under website-html/.",
            "Browser and fresh HTTP requests verified the deployment-specific share link. A generic web fetcher could not open sample shared URLs; use this text plus the university JSON when Claude cannot fetch the preview.",
            "", "",
        ])
        payloads[text_paths[uid]] = (heading + "\n\n".join(sections)).encode("utf-8")
    website_metadata = {
        "html_pages": len(page_entries), "university_text_files": len(text_paths),
        "program_html_pages": len(programs), "university_html_pages": len(universities),
        "hash_normalization": "CRLF and CR converted to LF; no other HTML modifications",
        "verified_against": "full-snapshot/preview-http-verification.json",
        "verified_preview_origin": proof.get("preview_origin"),
        "live_checked_at_utc": proof.get("checked_at_utc"),
        "generic_fetcher_access": "Not verified; generic web fetcher could not open sample shared URLs despite successful browser and fresh cookie-jar HTTP checks",
    }
    payloads["website-snapshots/PAGE-INDEX.json"] = json_bytes({"metadata": website_metadata, "pages": page_entries})
    return payloads, text_paths, website_metadata


def source_refs(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"source_id", "source_ids"}:
                refs = child if isinstance(child, list) else [child]
                found.update(ref for ref in refs if isinstance(ref, str) and ref.startswith("SRC-"))
            found.update(source_refs(child))
    elif isinstance(value, list):
        for child in value:
            found.update(source_refs(child))
    return found


def unresolved_facts(value: Any, path: str = "") -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    if isinstance(value, dict):
        if value.get("status") in REVIEW_STATUSES:
            found.append({
                "field_path": path or "$",
                "status": value["status"],
                "value": value.get("value"),
                "notes": value.get("notes"),
                "source_ids": value.get("source_ids", []),
            })
        for key, child in value.items():
            # A structured value can contain its own separately classified facts.
            if key in {"status", "notes", "source_ids"}:
                continue
            child_path = f"{path}.{key}" if path else key
            found.extend(unresolved_facts(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(unresolved_facts(child, f"{path}[{index}]"))
    return found


def preview_manifest(original: dict[str, Any], preview_url: str | None,
                     provenance: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(original)
    metadata = result.setdefault("metadata", {})
    metadata["original_manifest_source_commit"] = metadata.get("source_commit")
    metadata["original_manifest_website"] = metadata.get("website")
    metadata["source_commit"] = provenance["research_snapshot_commit"]
    metadata["packaged_from_commit"] = provenance["packaged_from_commit"]
    metadata["website"] = preview_url
    metadata["review_environment"] = "preview" if preview_url else "preview_url_pending"
    metadata["production_is_review_target"] = False

    def change_links(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in list(value.items()):
                if key in {"review_page_url", "program_page_url", "university_page_url"} and isinstance(child, str):
                    relative = urlsplit(child).path
                    value[key] = review_url(preview_url, relative)
                    value[key.removesuffix("_url") + "_path"] = relative
                else:
                    change_links(child)
        elif isinstance(value, list):
            for child in value:
                change_links(child)

    change_links(result)
    return result


def checklist_summary(entry: dict[str, Any] | None) -> dict[str, Any] | None:
    """Avoid repeating full source records and fact notes inside one upload."""
    if entry is None:
        return None
    keys = (
        "id", "review_page_url", "review_page_path", "program_page_url",
        "program_page_path", "university_page_url", "university_page_path",
        "existing_status", "existing_overall_status", "existing_last_checked",
        "refresh_status", "refresh_checked_at", "refresh_outcome",
    )
    result = {key: entry[key] for key in keys if key in entry}
    result["fields_needing_review"] = [
        {key: issue[key] for key in ("field", "status", "source_ids") if key in issue}
        for issue in entry.get("fields_needing_review", [])
    ]
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview-url", help="Immutable HTTPS Vercel preview URL")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "review-package")
    args = parser.parse_args()
    preview_url = args.preview_url if args.preview_url else None
    if preview_url:
        parsed = urlsplit(preview_url)
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password or parsed.fragment or parsed.path not in {"", "/"}:
            parser.error("--preview-url must be an HTTPS deployment origin, optionally with a share query, without a page path, credentials or fragment")
        preview_url = review_url(preview_url, "/")

    input_paths = [ROOT / "research" / name for name in INPUT_NAMES]
    input_paths.extend(ROOT / "research" / name for name in OPTIONAL_INPUT_NAMES if (ROOT / "research" / name).is_file())
    originals = {f"full-snapshot/{path.name}": path.read_bytes() for path in input_paths}
    programs = json.loads(originals["full-snapshot/programs-2027-2028.json"])
    universities = json.loads(originals["full-snapshot/universities-2027-2028.json"])
    sources = json.loads(originals["full-snapshot/sources.json"])
    coverage = json.loads(originals["full-snapshot/coverage-report.json"])
    original_manifest = json.loads(originals["full-snapshot/claude-review-manifest.json"])
    source_by_id = {source["id"]: source for source in sources}
    university_by_id = {university["id"]: university for university in universities}
    if len(source_by_id) != len(sources) or len(university_by_id) != len(universities):
        raise ValueError("Duplicate source or university IDs")
    program_ids = [program["id"] for program in programs]
    if len(set(program_ids)) != len(program_ids):
        raise ValueError("Duplicate program IDs")
    missing_refs = source_refs([programs, universities]) - source_by_id.keys()
    if missing_refs:
        raise ValueError(f"Unresolved source ID references: {sorted(missing_refs)}")
    unknown_universities = {p["university_id"] for p in programs} - university_by_id.keys()
    if unknown_universities:
        raise ValueError(f"Programs reference unknown universities: {sorted(unknown_universities)}")

    input_git_paths = [path.relative_to(ROOT).as_posix() for path in input_paths]
    snapshot_commit = git("log", "-1", "--format=%H", "--", *(f"research/{name}" for name in CORE_DATA_NAMES))
    tracked_inputs = set(git("ls-files", "--", *input_git_paths).splitlines())
    saved_inputs = tracked_inputs == set(input_git_paths) and not bool(git("diff", "--name-only", "HEAD", "--", *input_git_paths))
    provenance = {
        "branch": git("branch", "--show-current"),
        "packaged_from_commit": git("rev-parse", "HEAD"),
        "research_snapshot_commit": snapshot_commit,
        "research_snapshot_commit_utc": git("show", "-s", "--format=%cI", snapshot_commit),
        "research_inputs_match_saved_commit": saved_inputs,
        "github_repository": "https://github.com/Aziz-Braiek/italy-it-programs",
        "preview_url": preview_url,
        "production_url": PRODUCTION_URL,
        "production_is_review_target": False,
    }
    provenance["github_branch_url"] = f"{provenance['github_repository']}/tree/{quote(provenance['branch'], safe='/')}"
    metadata = {
        "schema_version": 1,
        "academic_year": "2027-2028",
        "research_as_of": coverage.get("as_of"),
        "provenance": provenance,
        "counts": {"universities": len(universities), "programs": len(programs), "sources": len(sources)},
        "review_state": "Independent review pending; the snapshot is not a completion claim",
    }
    website_payloads, website_text_paths, website_metadata = website_snapshot_payloads(
        programs, universities, preview_url, snapshot_commit,
    )
    metadata["website_snapshot"] = website_metadata

    issues: list[dict[str, Any]] = []
    for record_type, records in (("university", universities), ("program", programs)):
        for record in records:
            for issue in unresolved_facts(record):
                issues.append({
                    "record_type": record_type,
                    "record_id": record["id"],
                    "university_id": record["id"] if record_type == "university" else record["university_id"],
                    **issue,
                    "source_urls": [{"source_id": sid, "url": source_by_id[sid]["url"]} for sid in issue["source_ids"] if sid in source_by_id],
                })
    conflicts = [issue for issue in issues if issue["status"] == "CONFLICTING_SOURCES"]
    source_link_issues = [{
        "source_id": source["id"],
        "university_id": source.get("university_id"),
        "title": source.get("title"),
        "url": source.get("url"),
        "cycle": source.get("cycle"),
        "url_check": source.get("url_check"),
        "browser_check": source.get("browser_check"),
        "interpretation": "A request failure is not by itself proof of a broken link; inspect the stored method and response.",
    } for source in sources if (source.get("url_check") or {}).get("outcome") in {"broken", "inconclusive", "access_limited"}]
    redirects = [{
        "source_id": source["id"], "url": source.get("url"),
        "effective_url": source.get("url_check", {}).get("effective_url"),
        "checked_at": source.get("url_check", {}).get("checked_at"),
    } for source in sources if (source.get("url_check") or {}).get("outcome") == "redirected"]
    issue_index = {
        "metadata": metadata,
        "counts": {
            "unresolved_or_verification_required_fields": len(issues),
            "conflicting_fields": len(conflicts),
            "source_records_with_broken_inconclusive_or_limited_checks": len(source_link_issues),
            "redirected_source_records": len(redirects),
        },
        "known_conflicts": conflicts,
        "source_link_issues": source_link_issues,
        "redirects": redirects,
        "unresolved_fields": issues,
    }
    derived_manifest = preview_manifest(original_manifest, preview_url, provenance)
    payloads: dict[str, bytes] = dict(originals)
    if payloads.keys() & website_payloads.keys():
        raise ValueError("Duplicate payload paths between original research files and website snapshots")
    payloads.update(website_payloads)
    payloads["review/claude-review-manifest-preview.json"] = json_bytes(derived_manifest)
    if preview_url:
        checklist = originals["full-snapshot/claude-review-checklist.md"].decode("utf-8")
        page_paths = {
            *(f"/programs/{program['id']}/" for program in programs),
            *(f"/universities/{university['id']}/" for university in universities),
        }
        review_hosts = {
            urlsplit(PRODUCTION_URL).netloc,
            urlsplit(preview_url).netloc,
            urlsplit(original_manifest.get("metadata", {}).get("website") or "").netloc,
        }

        def rewrite_checklist_url(match: re.Match[str]) -> str:
            parsed = urlsplit(match.group(0))
            if parsed.netloc in review_hosts and parsed.path in page_paths | {"", "/"}:
                return review_url(preview_url, parsed.path or "/") or match.group(0)
            return match.group(0)

        checklist = re.sub(r"https?://[^\s<>\]\)]+", rewrite_checklist_url, checklist)
        checklist_links = [
            urlsplit(link) for link in re.findall(r"https?://[^\s<>\]\)]+", checklist)
            if urlsplit(link).netloc in review_hosts and urlsplit(link).path in page_paths
        ]
        if {link.path for link in checklist_links} != page_paths:
            raise ValueError("Preview checklist does not cover every university and program page")
        expected_preview = urlsplit(preview_url)
        if any(link.netloc != expected_preview.netloc or link.query != expected_preview.query for link in checklist_links):
            raise ValueError("Preview checklist page links lost the requested preview host or share query")
        checklist = f"<!-- Preview-specific copy. Original preserved under full-snapshot/. Research snapshot {snapshot_commit}. -->\n" + checklist
    else:
        checklist = "# Preview checklist pending\n\nRebuild this package with --preview-url after the preview is ready. The original production-linked checklist is preserved under full-snapshot/.\n"
    payloads["review/claude-review-checklist-preview.md"] = checklist.encode("utf-8")
    payloads["review/known-conflicts-broken-links-unresolved-fields.json"] = json_bytes(issue_index)
    issue_summary = [
        "# Known issues for independent review", "",
        f"{len(issues)} fact fields currently require verification or carry an unresolved status; {len(conflicts)} of these are classified CONFLICTING_SOURCES.",
        "The complete field values, notes and supporting URLs are in known-conflicts-broken-links-unresolved-fields.json and the relevant university upload batches.", "",
        "## Field status counts", "",
    ]
    issue_summary.extend(f"- {status}: {count}" for status, count in sorted(Counter(issue["status"] for issue in issues).items()))
    issue_summary.extend(["", "## Conflicting facts", ""])
    for issue in conflicts:
        issue_summary.append(f"- **{issue['record_id']}** / `{issue['field_path']}`: {issue.get('notes') or 'See structured issue record.'}")
        issue_summary.extend(f"  - `{source['source_id']}`: {source['url']}" for source in issue["source_urls"])
    issue_summary.extend(["", "## Broken, inconclusive or limited source checks", ""])
    for source in source_link_issues:
        check = source.get("url_check") or {}
        issue_summary.append(f"- **{source['source_id']}** — {check.get('outcome')} — {source['url']} (cycle: {source.get('cycle')}; checked: {check.get('checked_at')})")
        issue_summary.append(f"  - Method: {check.get('method')}; HTTP status: {check.get('http_status')}; details: {check.get('error') or 'See stored response and browser check.'}")
    issue_summary.extend(["", "An inconclusive request is not proof that a URL is broken. The broken historical URL is retained for provenance; check its use before proposing removal.", ""])
    payloads["review/known-issues-summary.md"] = "\n".join(issue_summary).encode("utf-8")
    payloads["review/discrepancy-response-template.json"] = json_bytes({
        "instructions": "Return one entry per claim or source problem. Preserve IDs and field paths. Do not guess unpublished 2027/28 terms.",
        "findings": [{
            "record_type": "program | university | source",
            "record_id": "stable ID from the uploaded batch",
            "university_id": "stable university ID",
            "field_path": "e.g. facts.application_deadline",
            "current_value": None,
            "proposed_value": None,
            "finding": "confirmed | discrepancy | unpublished | inaccessible | conflict",
            "academic_year": "2027-2028",
            "source_id": None,
            "official_source_url": None,
            "checked_at": "YYYY-MM-DD",
            "evidence": "Short explanation and the applicable academic year",
        }],
    })
    payloads["PACKAGE-METADATA.json"] = json_bytes({**metadata, "issue_counts": issue_index["counts"]})

    manifest_programs = {entry["id"]: entry for entry in derived_manifest.get("programs", [])}
    manifest_universities = {entry["id"]: entry for entry in derived_manifest.get("universities", [])}
    batches: list[dict[str, Any]] = []
    seen_program_ids: list[str] = []
    seen_source_ids: set[str] = set()
    for index, university in enumerate(universities, 1):
        uid = university["id"]
        university_programs = [program for program in programs if program["university_id"] == uid]
        referenced = source_refs([university, university_programs])
        relevant_sources = [source for source in sources if source["id"] in referenced or source.get("university_id") == uid]
        relevant_ids = {source["id"] for source in relevant_sources}
        if not referenced <= relevant_ids:
            raise ValueError(f"Batch {uid} is missing source records")
        batch_name = f"upload-batches/{index:02d}-{uid}.json"
        batch = {
            "metadata": {
                **metadata, "batch_number": index, "university_id": uid,
                "batch_counts": {"universities": 1, "programs": len(university_programs), "sources": len(relevant_sources)},
                "website_text_file": website_text_paths[uid],
                "review_instruction": "Review every program and university field against official sources. Preserve stable IDs, use field paths, and keep previous-cycle evidence labeled with its year. See discrepancy-response-template.json for return format.",
            },
            "university": university,
            "programs": university_programs,
            "sources": relevant_sources,
            "review_checklist": {
                "university": checklist_summary(manifest_universities.get(uid)),
                "programs": [checklist_summary(manifest_programs[program["id"]]) for program in university_programs if program["id"] in manifest_programs],
            },
            "known_conflicts": [issue for issue in conflicts if issue["university_id"] == uid],
            "source_link_issues": [issue for issue in source_link_issues if issue["source_id"] in relevant_ids],
            "unresolved_fields": [
                {key: issue[key] for key in ("record_type", "record_id", "field_path", "status", "source_ids")}
                for issue in issues if issue["university_id"] == uid
            ],
        }
        payloads[batch_name] = json_bytes(batch)
        batches.append({
            "batch_file": batch_name, "university_id": uid,
            "university": university["name"],
            "program_count": len(university_programs), "source_count": len(relevant_sources),
            "program_ids": [program["id"] for program in university_programs],
            "uncompressed_bytes": len(payloads[batch_name]),
            "preview_page_url": review_url(preview_url, f"/universities/{uid}/"),
            "website_text_file": website_text_paths[uid],
            "website_text_bytes": len(payloads[website_text_paths[uid]]),
        })
        seen_program_ids.extend(program["id"] for program in university_programs)
        seen_source_ids.update(relevant_ids)
    if Counter(seen_program_ids) != Counter(program_ids):
        raise ValueError("Program batch membership is incomplete or duplicated")
    if seen_source_ids != source_by_id.keys():
        raise ValueError(f"Source records missing from university batches: {sorted(source_by_id.keys() - seen_source_ids)}")
    payloads["BATCH-INDEX.json"] = json_bytes({"metadata": metadata, "batches": batches})

    csv_output = io.StringIO(newline="")
    writer = csv.writer(csv_output, lineterminator="\n")
    writer.writerow(["record_type", "record_id", "university_id", "name", "preview_page_url", "official_source_ids", "official_source_urls"])
    for record_type, records in (("university", universities), ("program", programs)):
        for record in records:
            uid = record["id"] if record_type == "university" else record["university_id"]
            path = f"/universities/{uid}/" if record_type == "university" else f"/programs/{record['id']}/"
            ids = sorted(source_refs(record))
            writer.writerow([record_type, record["id"], uid, record.get("name", record.get("program")), review_url(preview_url, path) or "", " | ".join(ids), " | ".join(source_by_id[sid]["url"] for sid in ids)])
    payloads["review/record-inventory.csv"] = csv_output.getvalue().encode("utf-8")

    max_batch_bytes = max(batch["uncompressed_bytes"] for batch in batches)
    lines = [
        "# Italy University Tracker — Claude Web review package", "",
        f"Research snapshot as of {coverage.get('as_of')}; academic year 2027/28.",
        f"Inventory: {len(universities)} universities, {len(programs)} program records, {len(sources)} source records.",
        f"Research snapshot commit: `{snapshot_commit}`.",
        f"Package built from branch `{provenance['branch']}` at `{provenance['packaged_from_commit']}`.",
        f"GitHub branch: {provenance['github_branch_url']}",
        f"Preview: {preview_url or 'Pending — rebuild with --preview-url before website review.'}", "",
        "## How to review in claude.ai", "",
        "1. Download and extract claude-review-package.zip on your computer.",
        "2. Start with this README and BATCH-INDEX.json. Upload one university JSON file from upload-batches/ at a time, or a few small files if your Claude account allows it. Each university batch contains its complete university/program records, official sources, review checklist and open issues.",
        "3. Upload the corresponding website-snapshots/<university-id>.txt alongside the university JSON, especially if Claude cannot fetch the protected preview. BATCH-INDEX.json maps each university to its text file. These texts contain the complete static body content of its university and program detail pages, stable IDs, shareable preview URLs and HTML SHA256 values. All 243 archived detail HTML files were checked against the captured live preview response hashes.",
        "4. Ask Claude to check every program in the uploaded batch against official university pages, calls, catalogues and PDFs, and compare the preview pages or the supplied page texts. Verify that a 2027/28 first-year intake is actually announced; teaching a previous cohort during 2027/28 is insufficient.",
        "5. Request results using review/discrepancy-response-template.json. Every finding must include the stable record ID, field path, applicable academic year, official evidence URL and check date. Keep pending details pending; do not invent admissions rules, fees or acceptance rates.",
        "6. Save each batch's returned findings, then continue with the next university. Review all files in BATCH-INDEX.json before concluding the audit.", "",
        f"There are {len(batches)} separate upload batches. The largest is {max_batch_bytes:,} bytes ({max_batch_bytes / 1024 / 1024:.2f} MiB) before compression. Upload the extracted JSON rather than relying on ZIP ingestion. Claude upload limits can vary by account; reduce the number of simultaneous batch uploads when needed.", "",
        "## Package contents", "",
        "- full-snapshot/: byte-for-byte copies of the complete saved datasets, coverage report, original checklist and manifest, research report and progress ledger.",
        "- upload-batches/: 34 self-contained university files. Programs occur in exactly one batch; shared source records may appear in several batches to preserve provenance.",
        "- website-snapshots/: 34 UTF-8 university text files and PAGE-INDEX.json. Each text contains its university page and all associated program pages, with stable record IDs, shareable page URLs and normalized HTML hashes.",
        "- website-html/: all 209 program and 34 university detail HTML files, normalized only to LF line endings; every SHA256 matches its captured live preview HTTP response. Asset-relative links are preserved in the HTML; the text files are the convenient upload fallback.",
        "- review/claude-review-manifest-preview.json and review/claude-review-checklist-preview.md: derived review copies pointing to the supplied preview. Original files may contain production links and older baseline commit metadata; their preserved bytes are for provenance. Use these preview copies and the batches for the website review.",
        "- review/known-conflicts-broken-links-unresolved-fields.json: all classified conflicts and unresolved facts, plus broken/inconclusive/limited source checks and redirects. A request failure alone does not establish that a source is broken.",
        "- review/known-issues-summary.md: readable conflict descriptions and source link problems, with stable record IDs and official URLs.",
        "- review/record-inventory.csv: stable university and program IDs, preview page URLs and official source IDs/URLs.",
        "- PACKAGE-METADATA.json, FILE-INVENTORY.json and SHA256SUMS.txt: provenance and SHA-256 checksums for the included files.", "",
        "## Review scope and cautions", "",
        "Deployment-specific share links were verified in a browser and in 246 fresh HTTP requests using separate cookie jars. A generic web fetcher could not open sampled shared URLs, so live access through Claude's fetcher remains unverified. Use the matched offline page texts when live fetching fails; this preserves project security settings.",
        f"The coverage report records {coverage.get('programs_fully_verified')} core-verified programs, {coverage.get('programs_availability_pending')} with 2027/28 availability pending, and {coverage.get('programs_not_offered_2027_2028')} marked not offered. This is an interim research snapshot, not a claim that every requested field is complete.",
        "Keep original historical cycle labels. CONFIRMED on a previous_cycle_* fact confirms only the stated historical fact. Review university-wide dates for applicability to each specific course and applicant category. Follow the source URL, check the document's academic year, and note official-source conflicts explicitly.",
        "The production site is outside this preview review. Do not ask a reviewer to change the repository or production deployment; return proposed corrections and evidence for a separate implementation pass.", "",
        "To reproduce: python scripts/build_claude_review_package.py --preview-url https://THE-IMMUTABLE-PREVIEW.vercel.app", "",
    ]
    payloads["README.md"] = "\n".join(lines).encode("utf-8")
    inventory = [{"path": name, "bytes": len(data), "sha256": sha256(data)} for name, data in sorted(payloads.items())]
    payloads["FILE-INVENTORY.json"] = json_bytes({
        "metadata": metadata,
        "scope": "All package payload files except FILE-INVENTORY.json and SHA256SUMS.txt, which are generated last to avoid self-referential checksums.",
        "files": inventory,
    })
    checksum_lines = [f"{sha256(data)}  {name}" for name, data in sorted(payloads.items())]
    payloads["SHA256SUMS.txt"] = ("\n".join(checksum_lines) + "\n").encode("utf-8")

    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    for name, data in payloads.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    zip_path = output / "claude-review-package.zip"
    stamp = datetime.fromisoformat(provenance["research_snapshot_commit_utc"]).astimezone(timezone.utc)
    zip_date = (max(1980, stamp.year), stamp.month, stamp.day, stamp.hour, stamp.minute, stamp.second)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payloads.items()):
            info = zipfile.ZipInfo(name, date_time=zip_date)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(zip_path) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"ZIP integrity check failed for {bad}")
        for name, data in payloads.items():
            if archive.read(name) != data:
                raise ValueError(f"ZIP payload mismatch: {name}")
        for name, data in originals.items():
            if archive.read(name) != data:
                raise ValueError(f"Original input bytes were changed: {name}")
    zip_sha = sha256(zip_path.read_bytes())
    (output / "claude-review-package.zip.sha256").write_text(f"{zip_sha}  {zip_path.name}\n", encoding="utf-8")
    print(json.dumps({
        "zip": str(zip_path), "zip_bytes": zip_path.stat().st_size,
        "zip_sha256": zip_sha, "counts": metadata["counts"],
        "upload_batches": len(batches), "largest_batch_bytes": max_batch_bytes,
        "website_snapshot": website_metadata,
        "largest_website_text_bytes": max(len(payloads[path]) for path in website_text_paths.values()),
        "issue_counts": issue_index["counts"],
        "source_record_url_check_outcomes": dict(Counter((source.get("url_check") or {}).get("outcome", "not_checked") for source in sources)),
        "research_snapshot_commit": snapshot_commit,
        "research_inputs_match_saved_commit": provenance["research_inputs_match_saved_commit"],
        "preview_url": preview_url,
        "validation": f"ZIP CRC and payload equality passed; original files byte-identical; all programs occur in exactly one university batch; all {len(sources)} source records and all referenced source IDs included in university batches; all {len(programs) + len(universities)} normalized-LF detail HTML hashes match captured live HTTP response hashes.",
    }, indent=2))


if __name__ == "__main__":
    main()
