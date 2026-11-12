# Independent official-source audit

This review compares the frozen `c3af9dc` research snapshot with official sources checked on 11–12 November 2026. It covers all 34 universities, 209 stable program IDs and 700 original source IDs. The attached Batch 1 report was treated as a set of claims to investigate independently.

Start with [the correction report](correction-report.md). [The full ledger](review-ledger.json) records existing values, official findings, URLs, check dates, academic years and explicit outcomes. [Structured findings](findings.json) include field discrepancies, source-scope issues, inaccessible original URLs and verified replacements. [The approved plan](approved-corrections.json) contains exact patches; [the approvals](review-approvals.json) pin manually reviewed batches by SHA-256.

There are 4,643 field comparisons and 278 approved field/source patches. Content was reviewed for 693 original source records. Seven original sources were inaccessible; alternatives are recorded where verified. A completed review outcome does not mean every 2027/28 field is published or factually resolved. Country-specific entry/GPA tables and complete language-certificate lists remain explicit gaps where they were not exhaustively verified. Historical, provisional and conflicting evidence is not promoted to a current admission offer.

The baseline narrative and user-supplied report are preserved under `input-evidence/`. Raw HTTP/PDF/browser captures are preserved locally under the ignored `tmp/independent-audit-2026-11/` directory; committed capture indexes retain response metadata and hashes. Existing work and archived records are retained.

To reproduce from this Git checkout, with Python and Node installed:

```text
python scripts/assemble_approved_audit_corrections.py
python scripts/build_independent_audit.py --require-complete
python scripts/build_research_data.py
python scripts/audit_research_data.py
python scripts/build_site.py
python -m unittest discover -s tests
node scripts/test_tracker_ui.mjs
node scripts/test_site.mjs
```

The factual conclusions are manual research. These commands validate coverage, exact baseline preconditions, data integrity and website behavior; they do not establish factual truth. Rebuilding the research data requires the `c3af9dc` Git object. Browser tests use the existing local Playwright installation and Microsoft Edge.

The website build produces `review-package/independent-audit-review.zip` and publishes the review files under the preview's `/data/independent-audit/` path. The ZIP includes the resulting datasets, ledger, findings, correction report, patch plan and file hashes. No production promotion is authorized for this release.
