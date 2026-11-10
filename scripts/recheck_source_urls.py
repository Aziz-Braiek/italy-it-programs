#!/usr/bin/env python3
"""Recheck official source URL reachability without treating failures as broken facts."""

from __future__ import annotations

import argparse
import concurrent.futures
import html.parser
import json
import re
import socket
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "research" / "sources.json"
USER_AGENT = "ItalyUniversityTrackerResearch/1.0 (official-source URL review)"
MAX_BYTES = 128 * 1024


class TitleParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.parts.append(data)


def decode_body(body: bytes, content_type: str | None) -> str:
    charset = "utf-8"
    if content_type:
        match = re.search(r"charset\s*=\s*['\"]?([^;'\" ]+)", content_type, re.I)
        if match:
            charset = match.group(1)
    try:
        return body.decode(charset, errors="replace")
    except LookupError:
        return body.decode("utf-8", errors="replace")


def classify(status: int | None, effective_url: str | None, original_url: str, error: str | None) -> str:
    if error:
        return "inconclusive"
    if status in (404, 410):
        return "broken"
    if status in (401, 403, 407, 429):
        return "access_limited"
    if status is None or status >= 500 or status < 200:
        return "inconclusive"
    if status >= 400:
        return "inconclusive"
    if effective_url and urllib.parse.urldefrag(effective_url)[0] != urllib.parse.urldefrag(original_url)[0]:
        return "redirected"
    return "accessible"


def request_once(url: str, is_pdf: bool) -> dict[str, Any]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/pdf,*/*;q=0.9" if is_pdf else "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cache-Control": "no-cache",
    }
    if is_pdf:
        headers["Range"] = "bytes=0-4095"
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=14) as response:
            body = response.read(MAX_BYTES)
            status = response.status
            final_url = response.geturl()
            content_type = response.headers.get("Content-Type")
            decoded = "" if is_pdf else decode_body(body, content_type)
            parser = TitleParser()
            if decoded:
                parser.feed(decoded)
            title = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()[:300] or None
            lower_body = decoded.lower()
            return {
                "http_status": status,
                "effective_url": final_url,
                "content_type": content_type,
                "content_length_header": response.headers.get("Content-Length"),
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
                "cache_control": response.headers.get("Cache-Control"),
                "age": response.headers.get("Age"),
                "x_vercel_cache": response.headers.get("x-vercel-cache"),
                "x_vercel_id": response.headers.get("x-vercel-id"),
                "location": response.headers.get("Location"),
                "observed_title": title,
                "pdf_signature": body.startswith(b"%PDF-") if is_pdf else None,
                "has_2027_marker": any(marker in lower_body for marker in ("2027/28", "2027-2028", "2027–2028", "2027/2028")) if not is_pdf else None,
                "bytes_read": len(body),
                "outcome": classify(status, final_url, url, None),
                "error": None,
            }
    except urllib.error.HTTPError as error:
        final_url = error.geturl()
        return {
            "http_status": error.code,
            "effective_url": final_url,
            "content_type": error.headers.get("Content-Type"),
            "content_length_header": error.headers.get("Content-Length"),
            "etag": error.headers.get("ETag"),
            "last_modified": error.headers.get("Last-Modified"),
            "cache_control": error.headers.get("Cache-Control"),
            "age": error.headers.get("Age"),
            "x_vercel_cache": error.headers.get("x-vercel-cache"),
            "x_vercel_id": error.headers.get("x-vercel-id"),
            "location": error.headers.get("Location"),
            "observed_title": None,
            "pdf_signature": None,
            "has_2027_marker": None,
            "bytes_read": 0,
            "outcome": classify(error.code, final_url, url, None),
            "error": None,
        }
    except (urllib.error.URLError, TimeoutError, socket.timeout, ssl.SSLError, OSError) as error:
        reason = getattr(error, "reason", error)
        return {
            "http_status": None,
            "effective_url": None,
            "content_type": None,
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": None,
            "age": None,
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": None,
            "pdf_signature": None,
            "has_2027_marker": None,
            "bytes_read": 0,
            "outcome": "inconclusive",
            "error": f"{type(reason).__name__}: {reason}"[:500],
        }


def check_source(source: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    url = source.get("url", "")
    is_pdf = ".pdf" in urllib.parse.urlparse(url).path.lower() or "pdf" in f"{source.get('source_type', '')} {source.get('title', '')}".lower()
    result = request_once(url, is_pdf)
    if result["outcome"] == "inconclusive" and result.get("http_status") is None:
        time.sleep(0.5)
        retry = request_once(url, is_pdf)
        retry["retried"] = True
        result = retry
    result["checked_at"] = date.today().isoformat()
    result["method"] = "GET with byte range for PDF sources" if is_pdf else "GET"
    return source["id"], result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offset", type=int, default=0, help="Offset into the unique source URL list")
    parser.add_argument("--limit", type=int, default=50, help="Unique URLs to check in this batch")
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--retry-inconclusive", action="store_true", help="Retry URLs whose latest check was inconclusive")
    args = parser.parse_args()

    sources = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    url_to_sources: dict[str, list[dict[str, Any]]] = {}
    for source in sources:
        url_to_sources.setdefault(source.get("url", ""), []).append(source)
    unique_urls = list(url_to_sources)
    if args.retry_inconclusive:
        selected_urls = [
            url for url, linked in url_to_sources.items()
            if any((source.get("url_check") or {}).get("outcome") == "inconclusive" for source in linked)
        ][: args.limit]
    else:
        selected_urls = unique_urls[args.offset: args.offset + args.limit]
    selected_sources = [source for url in selected_urls for source in url_to_sources[url]]
    if not selected_sources:
        raise SystemExit(f"No source URLs in offset={args.offset} limit={args.limit}; total unique URLs={len(unique_urls)}")

    representative = [url_to_sources[url][0] for url in selected_urls]
    result_by_id: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(check_source, source): source for source in representative}
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            source_id, result = future.result()
            result_by_id[source_id] = result
            if index % 10 == 0 or index == len(futures):
                print(f"checked {index}/{len(futures)} unique URLs", flush=True)

    result_by_url = {source["url"]: result_by_id[source["id"]] for source in representative}
    for source in selected_sources:
        source["url_check"] = result_by_url[source["url"]]
    SOURCES_PATH.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts: dict[str, int] = {}
    for result in result_by_url.values():
        counts[result["outcome"]] = counts.get(result["outcome"], 0) + 1
    print(json.dumps({
        "offset": args.offset,
        "unique_urls_checked": len(selected_urls),
        "source_records_updated": len(selected_sources),
        "total_unique_urls": len(unique_urls),
        "outcomes": counts,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
