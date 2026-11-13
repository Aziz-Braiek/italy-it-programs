"""Presentation corrections applied after the frozen independent-audit patches.

These do not promote availability, infer a missing value, or refresh review dates.
The original ambiguous strings remain in the historical audit evidence.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def apply(universities, programs):
    config = json.loads((ROOT / "research/site-presentation.json").read_text(encoding="utf-8"))
    for university in universities:
        url = config["university_admissions"].get(university["id"])
        if url:
            university["international_admissions_url"] = url
    for program in programs:
        for key in ("level", "language", "field"):
            field = program.get(key) or {}
            value = field.get("value")
            if isinstance(value, str) and (re.fullmatch(r"[A-Z]+(?:_[A-Z]+)+", value) or re.search(r"\bunresolved\b", value, re.I)):
                field["value"] = None
                tags = program.get("previous_cycle_tags") or {}
                if key in tags:
                    tags[key] = None
