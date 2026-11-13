"""Fresh captures for approved official URLs; fetching never verifies a fact."""
import argparse
import concurrent.futures
import json
import re
from pathlib import Path
import capture_independent_audit_sources as capture

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research/decision-support-2026-11"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("requests_file", type=Path)
    args = parser.parse_args()
    requested = json.loads(args.requests_file.read_text(encoding="utf-8"))
    index_path = OUT / "source-checks.json"
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    rows = {r["url"]: r for r in payload["responses"]}
    source_path = OUT / "additional-sources.json"
    sources = json.loads(source_path.read_text(encoding="utf-8")) if source_path.exists() else []
    by_id = {r["id"]: r for r in sources}
    pending = {}
    for item in requested:
        if not item.get("official_basis"):
            raise ValueError(f"Missing official-source basis: {item['url']}")
        by_id[item["id"]] = item
        if item["url"] in rows and rows[item["url"]].get("http_status") == 200:
            row = rows[item["url"]]
            row["source_ids"] = sorted(set(row["source_ids"] + [item["id"]]))
        else:
            pending.setdefault(item["url"], []).append(item["id"])
    capture.EVIDENCE = ROOT / "tmp/decision-support-2026-11-13"
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for n, result in enumerate(pool.map(capture.capture, pending.items()), 1):
            rows[result["url"]] = result
            if n % 10 == 0:
                print(f"Captured {n}/{len(pending)} additional official pages", flush=True)
    payload["responses"] = sorted(rows.values(), key=lambda r: r["url"])
    for row in payload["responses"]:
        path = ROOT / row.get("local_text_path", "missing")
        if path.is_file():
            text = re.sub(r"\s+", "", path.read_text(encoding="utf-8")).replace("–", "-").replace("—", "-")
            cycles = set()
            for year, end in re.findall(r"(20\d{2})[/-](20\d{2}|\d{2})", text):
                end_year = int(end) if len(end) == 4 else 2000 + int(end)
                if end_year == int(year) + 1:
                    cycles.add(f"{year}/{str(end_year)[-2:]}")
                elif end_year == int(year) + 2:
                    cycles.add(f"{year}–{end_year}")
            for year, end in re.findall(r"(?:A\.?Y\.?|A\.?A\.?|academicyear)(\d{2})/(\d{2})", text, re.I):
                if int(end) == int(year) + 1:
                    cycles.add(f"20{year}/{end}")
            row["academic_cycles_detected"] = sorted(cycles)
    index_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    source_path.write_text(json.dumps(list(by_id.values()), ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Saved {len(rows)} source responses; {len(by_id)} source references", flush=True)


if __name__ == "__main__":
    main()
