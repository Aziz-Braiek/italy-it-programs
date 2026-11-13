# Applicant profiles and tuition rules

Baseline `d1d75fe`; phase 1 shipped separately in `3fab14e`. This research is for a preview, not a production release.

Canonical approvals are in `verified-routes.json` and `national-rules.json`. Route facts may reference existing programme/university policies in `../decision-support-2026-11/verified-facts.json`. `compiled-routes.json` and the review ledgers are derived, not additional approvals. A source being reachable, containing a year, or passing a technical test does not approve a fact.

`summary.json` and `report.md` compare field coverage with the saved `baseline.json`. `priority-field-ledger.json` includes every priority programme and university field. `route-gap-ledger.json` includes every category/origin combination for every priority programme/route field. `university-route-ledger.json` keeps university deadlines and recognition gaps separate from the national rule. `record-outcomes.json` lists all 47 priority programmes and 11 hosts, with reasons. Every missing value stays explicit.

The browser uses readable `applicant`, `qualification` and `degree-sought` parameters. Inputs are optional; exact nationality, permit, country, income, funding and language history are not collected. If those are needed to establish a route, its selected outcome remains Not confirmed. Historical rules never become a fallback. EU/EEA tuition evidence is not automatically Swiss evidence. Italian qualification is not an EU citizenship declaration.

Rebuild and verify from the repository root:

```text
python scripts/build_research_data.py
python scripts/build_site.py
python scripts/audit_research_data.py
python -m unittest discover -s tests
node scripts/test_site.mjs
node scripts/test_tracker_ui.mjs
node scripts/test_applicant_profiles.mjs
```

The browser tests use the existing local Playwright/Edge setup. `PROFILE_SITE_URL` runs the applicant-profile suite against a shareable preview URL; `SITE_URL` and `SCREENSHOT_DIR` configure the existing live-site suite. QA screenshots and captured source bodies stay in ignored `tmp/`; source metadata and hashes remain in the research files.

The independent-audit completeness check covers the saved earlier audit, not new factual verification. It rewrites its generation timestamps; preserve the prior audit when no substantive finding changed.
