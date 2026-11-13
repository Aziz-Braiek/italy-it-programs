# Applicant decision facts — 13 November 2026

Start with [report.md](report.md). This is a field-level research snapshot, not a claim that every applicant or programme has been fully verified.

- `verified-facts.json`: manually approved values, scoped university offers and shared policies. This is the editable source of truth for the decision layer.
- `source-checks.json`: fresh official responses and hashes. Retrieval does not establish a fact.
- `additional-sources.json`: additional university/programme/DSU references, including their official-source basis.
- `field-ledger.json`: explicit provenance and outcome for every modelled field.
- `unverified-fields.json`: missing values, reasons and pages checked.
- `record-outcomes.json`: all 209 programmes and 34 universities, with partial/incomplete research clearly distinguished.
- `coverage.json`: counts of current, previous-cycle and unknown facts per field.
- `source-conflicts.json`: competing source claims, scope differences and handling.

Program fields: duration, ECTS, prerequisites, English proof/tests/exemptions, entrance test, selection, minimum grade, non-EU seats and tuition. University fields: Universitaly, recognition/documents, regional DSU, university-published visa guidance and separately scoped scholarship offers. Shared fee/English rules are stored as university policies and referenced by programmes. Programme-specific scholarships and joint-route documents remain scoped within the university record.

Known facts use `value`, `cycle_status`, `academic_cycle`, `source_urls` and `verified_date`. Current facts additionally include `current_cycle_evidence` identifying a captured source with a detected 2027/28 or 2027–2029 annual context; captured-source hashes pin what was reviewed. Cross-source programme/cohort context is explicit where a central policy page is not independently year-labelled. A detected year is only a necessary metadata guard, not factual verification. Unknowns use the exact value `Not confirmed`, a null verification date, a reason and checked-page metadata. “Checked” is distinct from “verified”.

The public datasets embed the compiled decision layer on the appropriate programme/university records. Frozen legacy research observations are preserved unchanged for audit transparency and are not a second editable source for new decision facts. Original availability statuses, review dates and application-deadline facts are unchanged.

The 47 confirmed records and 11 host universities received the priority review. Eight awaiting Polito records have a partial previous-cycle requirements pass, and 44 additional awaiting profiles have directly checked previous-cycle duration/credit facts; the remaining 107 awaiting records and 23 awaiting-only universities have not completed this research pass. Three not-offered records remain unchanged. A missing field does not prove that the university has never published it.

Only current, source-supported facts enter confirmed filters and CSV values. Earlier values stay visibly labelled in the HTML/research evidence; CSV retains their cycle marker but replaces their value with `Not confirmed`. No new fact feeds the existing deadline sort or ICS export.

Reproduce with `python scripts/build_research_data.py`, then `python scripts/build_site.py`. The latter validates provenance and rendered filter flags. See the test commands and record-by-record outcomes in the report.

The refinement round adds structured `missing_components` (shown as Partly confirmed), `evidence_scope: degree_structure` with a specific course passage, exact three-state yes/no matching and visible conflict notes. Current-evidence totals include partial fields; see `../decision-refinement-2026-11/report.md` for full/partial and priority-scope before/after counts. Unknown card fields collapse into one linked line; detail pages preserve all fields. Historical values remain omitted from CSV values; CSV now also records confirmation and missing components.
