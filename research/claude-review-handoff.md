# Claude Web review handoff

Prepared 11 November 2026 for an independent audit in claude.ai.

The frozen research dataset is commit `3030be18494d5d0d9da81603b19868f1e138e02f`. It contains 34 universities, 209 program records and 700 source records. There are 39 programs with verified core details, 166 with 2027/28 availability pending and three recorded as not offered. The research remains an interim snapshot; a historical fact marked CONFIRMED is confirmed only for its labeled academic year.

- GitHub branch: https://github.com/Aziz-Braiek/italy-it-programs/tree/research/final-2027-2028-refresh
- Immutable review deployment: https://italy-it-programs-mx2hhwt08-azizbraaiek-7011s-projects.vercel.app
- Vercel deployment: `dpl_HbGjDyErocNAfXjNe8jFYUR4ZypG`, environment Preview, commit `3030be1`.
- Production baseline: `e6995e70e7fc4673a561af69fbb7fa14ea84491b`, deployed from `master`.

The deployment has a shareable link that requires no Vercel account and has no expiry. Use the complete link supplied with the review package. Its `_vercel_share` access query is intentionally excluded from this public repository. It grants access to this deployment only. Project-wide deployment protection remains enabled. The bare preview origin continues to require Vercel authentication.

## Files for the reviewer

Download and extract `claude-review-package.zip`. Begin with its `README.md` and `BATCH-INDEX.json`, then upload one JSON file from `upload-batches/` per university into Claude Web. The 34 batch files include every program exactly once, complete university records, all applicable source records, stable IDs, exact issue field paths, and links to the preview and official evidence. Shared sources are copied into each relevant batch. Every source record is included in at least one batch.

Use `review/claude-review-manifest-preview.json` and `review/claude-review-checklist-preview.md` from the package for website review. These derived copies include the share query on each page URL so a new reviewer session can open individual pages directly. `review/record-inventory.csv` lists every stable program/university ID and official source URL. The `full-snapshot/` directory preserves the complete saved datasets and documents byte-for-byte.

The issue index includes 1,921 fields marked unresolved or requiring verification, 26 classified source conflicts, one broken historical source, three inconclusive source checks and 13 redirects. These are review priorities, not a list of independently confirmed errors. Use the package's discrepancy response template to return a record ID, field path, current value, proposed correction, applicable academic year, evidence URL, verification date, confidence and severity for each finding.

Fresh browser access and HTTP clients with cookie support passed, but a separate content-fetch tool could not open the complete share URL. Its failure does not establish the cause or predict Claude Web's access. If Claude cannot fetch a preview page, upload the matching `website-snapshots/<university-id>.txt` alongside its university JSON. These files contain the displayed text of all 243 detail pages with stable IDs and page hashes. Exact HTML snapshots are also provided in `website-html/`; their LF-normalized SHA-256 hashes were matched against the live responses. This fallback allows comparison of the website's displayed content without weakening project security.

The largest university dataset JSON is approximately 0.60 MiB. The package README records exact output sizes. Upload the extracted files in manageable batches; the ZIP is the delivery container. Save each completed batch's findings before continuing. Preserve all stable IDs and distinguish a published 2027/28 first-year intake from teaching of an earlier cohort during 2027/28.

## Reproducing the package

From the repository root, run the following with the complete shareable URL provided privately to the reviewer:

```powershell
python scripts/build_claude_review_manifest.py
python scripts/build_claude_review_package.py --preview-url 'COMPLETE_SHAREABLE_PREVIEW_URL'
```

The outputs are `review-package/claude-review-package.zip`, its SHA-256 checksum, extracted batch files and inventories. Generated package files are ignored by Git because they contain the deployment's share link. Core research data is not modified by the packaging script. Regenerate after committing documentation so package provenance records a clean saved revision.

`claude-review-target.json` records the immutable deployment without its access query. The manifest generator derives the research dataset commit from the latest commit changing the four core data files and records their exact SHA-256 hashes. The package separately records its tooling/documentation commit; these revisions need not be identical when documentation changes without altering the frozen dataset.

## Verification and release boundary

The data build, data integrity audit, manifest build, static site build, 12 static-site tests, tracker UI tests and desktop/mobile browser tests passed. Regenerating the original snapshot produced no tracked data changes. All 209 program pages and 34 university pages exist in the saved build.

See `preview-verification-report.md` and `preview-http-verification.json` for live preview checks. Production remains on `e6995e7`; this research branch has not been promoted or merged into production. Review findings should be returned as proposed corrections for a separate implementation pass.
