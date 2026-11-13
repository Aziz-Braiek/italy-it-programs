# Production comparison before monitoring

Production: `c6dff07bff8c7b12b872bcd90590145e0932404b`. Pre-monitoring branch tip: `900315e4ef87f8b4b874d5854809b040e3207ca5`. All of `e039301`, `d1d75fe`, `3fab14e`, `900315e` are ancestors.

Exact Git diff: **56 files changed, 300006 insertions(+), 616 deletions(-)**.

All 209 programme records and all 34 university records differ because the decision-support and applicant-route layers were added. No records were added/removed and the availability totals remain 47/159/3. Outside those added layers, the only record changes are:

- `legacy-007`: unresolved degree/language placeholders become null; status unchanged.
- `discovered-022`: leaked language sentinel becomes null; status unchanged.
- `politecnico-torino`: generic institution link replaces the bachelor-only admissions link.
- `tor-vergata`: institution admissions link replaces the Mechatronics-only link.

User-visible changes before monitoring: Italy-wide/all-fields wording; honest application/availability badges; historical deadline handling; corrected source presentation; eligibility/cost/logistics fields with sources and cycle labels; strict yes/no counts; typed tuition; optional browser-only applicant profiles; selected-route sorting/CSV/calendar and collapsed Other routes. Permanent dark mode already exists in production. No availability status was promoted.

## Exact changed-file list

- `A` `research/2026-11-13-rendered-review-resolution.md`
- `A` `research/applicant-profiles-2026-11/README.md`
- `A` `research/applicant-profiles-2026-11/baseline.json`
- `A` `research/applicant-profiles-2026-11/compiled-routes.json`
- `A` `research/applicant-profiles-2026-11/conflict-review.json`
- `A` `research/applicant-profiles-2026-11/national-rules.json`
- `A` `research/applicant-profiles-2026-11/priority-field-ledger.json`
- `A` `research/applicant-profiles-2026-11/priority-unverified-fields.json`
- `A` `research/applicant-profiles-2026-11/profile-examples.json`
- `A` `research/applicant-profiles-2026-11/record-outcomes.json`
- `A` `research/applicant-profiles-2026-11/report.md`
- `A` `research/applicant-profiles-2026-11/route-gap-ledger.json`
- `A` `research/applicant-profiles-2026-11/route-scope-audit.json`
- `A` `research/applicant-profiles-2026-11/summary.json`
- `A` `research/applicant-profiles-2026-11/tuition-spot-checks.json`
- `A` `research/applicant-profiles-2026-11/university-route-ledger.json`
- `A` `research/applicant-profiles-2026-11/verified-routes.json`
- `A` `research/decision-refinement-2026-11/baseline.json`
- `A` `research/decision-refinement-2026-11/priority-field-ledger.json`
- `A` `research/decision-refinement-2026-11/priority-unverified-fields.json`
- `A` `research/decision-refinement-2026-11/record-outcomes.json`
- `A` `research/decision-refinement-2026-11/report.md`
- `A` `research/decision-refinement-2026-11/review-notes.json`
- `A` `research/decision-refinement-2026-11/summary.json`
- `A` `research/decision-refinement-2026-11/tuition-spot-checks.json`
- `A` `research/decision-support-2026-11/README.md`
- `A` `research/decision-support-2026-11/additional-sources.json`
- `A` `research/decision-support-2026-11/coverage.json`
- `A` `research/decision-support-2026-11/field-ledger.json`
- `A` `research/decision-support-2026-11/record-outcomes.json`
- `A` `research/decision-support-2026-11/report.md`
- `A` `research/decision-support-2026-11/source-checks.json`
- `A` `research/decision-support-2026-11/source-conflicts.json`
- `A` `research/decision-support-2026-11/unverified-fields.json`
- `A` `research/decision-support-2026-11/verified-facts.json`
- `M` `research/programs-2027-2028.json`
- `A` `research/site-presentation.json`
- `M` `research/universities-2027-2028.json`
- `A` `scripts/applicant_profiles.py`
- `A` `scripts/build_applicant_profile_report.py`
- `A` `scripts/build_decision_refinement_report.py`
- `M` `scripts/build_research_data.py`
- `M` `scripts/build_site.py`
- `A` `scripts/capture_decision_sources.py`
- `A` `scripts/decision_support.py`
- `A` `scripts/site_data_cleanup.py`
- `A` `scripts/test_applicant_profiles.mjs`
- `M` `scripts/test_live_site.mjs`
- `M` `scripts/test_site.mjs`
- `A` `site/applicant-profile-view.js`
- `A` `site/applicant-profiles.js`
- `M` `site/site.css`
- `M` `site/site.js`
- `A` `tests/test_applicant_profiles.py`
- `A` `tests/test_decision_support.py`
- `M` `tests/test_static_site.py`
