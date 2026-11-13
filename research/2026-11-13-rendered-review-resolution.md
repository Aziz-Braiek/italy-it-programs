# Rendered-page review: resolution and evidence

Checked 13 November 2026 (Europe/Rome). This is a focused source-link and presentation correction, not a new factual audit of every admission field. The existing independent-audit ledger and original evidence are preserved.

## Findings confirmed

- **Misleading scope:** the live title, hero, footer, structured description and About page incorrectly described an information-technology tracker. The intended scope is Italy and all fields. These surfaces now say international programs across all fields; no subject has been removed or hidden by a new default filter.
- **Politecnico di Torino MSc link mismatch:** program cards inherited the university's bachelor's calls URL. MSc cards now prefer the existing official course profile and also link the [master's admissions route](https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/master-s-degree-programmes). The university-level link now uses the [admissions index](https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment), which distinguishes degree levels. Existing source `SRC-POLITO-MSC-ADMISSIONS-2026` supports the master's route; this does not confirm a 2027/28 intake.
- **Tor Vergata Computer Science, `legacy-095`:** its primary link inherited Mechatronics admissions. It now uses the [official Computer Science profile](https://web.uniroma2.it/en/contenuto/computer_science-93169), source `SRC-ROMA2-COMPUTER-SCIENCE-MSC-2026`. This page describes a two-year Italian-taught LM-18 course and was modified 6 March 2025; it does not publish a 2027/28 call. The university-level fallback is the verified [general admissions page](https://web.uniroma2.it/en/percorso/admissions).
- **Generic card links:** the builder now prefers existing course-specific sources. Explicit source-ID overrides cover the verified exceptions and the CORES announcement. General fallbacks remain labeled “University admissions page”. The selected primary URL is checked against degree-specific path markers at build time. A shared catalogue path naming both bachelor's and master's degrees is not a contradiction when its child route specifies the correct level.
- **Leaked and missing values:** `discovered-022` had a literal `REQUIRES_VERIFICATION` language value. `legacy-007` had “Unresolved” language and “MSc lead unresolved” degree values. These are now null, with their unconfirmed statuses and original evidence retained. Degree/language placeholders read “Not confirmed”. The ambiguous campus/track qualifier on Sapienza `legacy-153` is also rendered as “Not confirmed”; its underlying identity is not guessed. Every generated HTML document is linted for visible sentinel strings and “Unresolved”; internal attributes and script contents are excluded.
- **Availability versus application timing:** core confirmation is now distinct from application badges. An open badge requires a confirmed intake and a confirmed, current-cycle round with both boundaries covering the Italian build date. A future deadline alone is insufficient. Applicant scope is retained. Unpublished, unconfirmed and conflicting dates remain distinct. Badges show their date of calculation and direct readers to the official call.
- **Earlier-cycle planning:** 68 records currently expose usable, source-linked earlier application dates. Each block uses the exact requested estimate-only label and retains original dates, evidence cycle and applicant context. No date is rolled forward. Universitaly/visa-process, enrolment, results, interview and document deadlines are excluded; admissions dates for visa applicants are retained from the extracted application-date list. Conflicting or unverified history remains in detailed evidence. Historical dates never enter `data-deadline` or `data-deadlines`, which drive sorting and calendar export.
- **Sort naming:** `recommended` was an undocumented URL value for the existing availability sort; there was no hidden personalized ranking. The canonical value is now `availability`; legacy `sort=recommended` links still work and normalize to the default URL. Methodology documents confirmed-first, then university, then program ordering.

## Findings rejected or qualified

- **Cyber Risk Strategy and Governance, `legacy-002`:** the Bocconi date is valid, not a wrong-university deadline. The [official joint-degree admissions page](https://www.unibocconi.it/en/applying-bocconi/master-science-and-ma-programs/application-and-admissions/joint-degree-programs-politecnico-di-milano) names Polimi and Bocconi, their joint admissions board, and standard 2027/28 MSc rounds for international qualifications. The [official round table](https://www.unibocconi.it/en/applying-bocconi/master-science-and-ma-programs/application-and-admissions/admissions) gives 30 October 2026–26 January 2027 for round II, closing at 15:00 Italian time. Italian qualifications have a separate joint-degree route. Dates and university association are retained; cards now explain the joint degree and Bocconi's application administration. Sources: `AUDIT-BOCCONI-CYBER-INTERNATIONAL-2027`, `AUDIT-BOCCONI-MSC-ROUNDS-2027`.
- **Noncomputing programs are outside scope:** rejected. “IT” meant Italy. Humanities, medicine, business, engineering and other fields remain together in the tracker.
- **Most records are empty:** pending records do contain historical facts, sources and explicit gaps. The current counts describe records, not 209 confirmed opportunities. The existing default excludes pending leads; no records were deleted to inflate apparent completeness.

## Unconfirmed information preserved

- All 209 stable program IDs, 34 university IDs and 759 source records are retained.
- Availability is unchanged: **47 confirmed, 159 awaiting, 3 not offered**.
- Every program and university `last_checked` value is unchanged. The presentation verification date is stored separately in `site-presentation.json`.
- CORES language, exact opening/deadline and formal intake confirmation remain pending. Its [official announcement](https://life.unige.it/index.php/presentazione-cores-mag2026) describes a planned early-2027 opening and 2027/28 start while the proposal was under evaluation; it does not supply a teaching language or exact application deadline.
- Tor Vergata Computer Science's 2027/28 intake remains pending; Polimi's generic Aerospace identity and language remain unconfirmed. Existing conflicting Polimi dates and all other unpublished fields remain unconfirmed.
- Selecting an existing official course link is not a claim that every linked course's admission terms were freshly verified. The detailed audit continues to state the scope and year of each source.

## Implementation and validation

- Builder and reproducible data cleanup: `scripts/build_site.py`, `scripts/build_research_data.py`, `scripts/site_data_cleanup.py`.
- Data/provenance: `research/site-presentation.json`, `research/programs-2027-2028.json`, `research/universities-2027-2028.json`; original audit files remain untouched.
- UI: `site/site.js`, `site/site.css`; permanent dark theme retained.
- Regression coverage: `tests/test_static_site.py`, `scripts/test_site.mjs`, `scripts/test_live_site.mjs`. Tests cover the visible-text and degree-link lints, link regressions, conservative application badges, historical-date exclusion and legacy sort URLs.
- Validation: research data audit; full static build with both lints; 22 Python regression tests; browser tests including all 209 records without JavaScript, 34 university cards, filters, comparison, CSV/calendar export, legacy sorting, dark mode and mobile overflow checks.

## Backlog — not implemented

1. Change alerts through RSS/email.
2. Applicant-profile filtering by citizenship, residence and qualification.
3. Expanded eligibility/cost summaries: prerequisite credits, English evidence, tests, selection, tuition, scholarships, Universitaly and document requirements.
4. Evaluate coverage of unibz (Bolzano), Bocconi as a separate institution, Luiss, Brescia, Sant'Anna and SNS.
