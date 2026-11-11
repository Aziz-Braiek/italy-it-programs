# Independent review preview verification

Checked 11 November 2026, approximately 18:00–18:05 UTC.

## Frozen review snapshot

- Branch: `research/final-2027-2028-refresh`.
- Dataset/deployment commit: `3030be18494d5d0d9da81603b19868f1e138e02f`.
- Preview origin: https://italy-it-programs-mx2hhwt08-azizbraaiek-7011s-projects.vercel.app
- Vercel deployment ID: `dpl_HbGjDyErocNAfXjNe8jFYUR4ZypG`; status READY; target Preview (not Production).
- GitHub deployment ID: `7717485069`, environment Preview, success.
- Inventory: 209 program records, 34 university records, 700 source records.

The live preview is frozen to the dataset commit above. Later branch commits may add packaging, metadata and verification documentation while preserving this dataset and immutable deployment.

## External reviewer access

The ordinary preview URL redirects to Vercel login. A deployment-specific shareable link was created and verified without a Vercel account. The final link has no expiry; it remains valid until revoked. Its access query is supplied in the local review package and user handoff, rather than committed publicly.

The project retains Vercel Authentication with `ssoProtection.enabled=true` and `deploymentType=all_except_custom_domains`. Password and trusted-IP settings were read before and after sharing and are unchanged. No project-wide protection switch, domain exception, project automation bypass, production alias or production deployment was changed. Only this immutable preview has been shared.

A separate content-fetch tool returned an inaccessible/internal-error result for the root and `legacy-020` page with the complete share query. It supplied no HTTP response establishing the cause. Claude Web's own fetcher has not been tested. Fresh browser and cookie-enabled HTTP access are verified; access by every AI fetcher is not. The package therefore includes all 243 verified detail-page HTML snapshots and 34 university text snapshots for upload alongside the datasets when a fetcher cannot open the preview. Each HTML snapshot is checked against the captured live response hash after LF normalization.

## Saved-data and build checks

The data build, data audit, manifest generation and static build all passed. Regenerating the research snapshot at 3030be1 produced zero tracked changes. Manifest inventories cover every stable program, university and source ID; all linked source IDs resolve. All 209 program pages and 34 university pages exist locally.

- `python scripts/build_research_data.py` — pass.
- `python scripts/audit_research_data.py` — pass.
- `python scripts/build_claude_review_manifest.py` — pass; review provenance now identifies the research dataset commit separately from the production baseline.
- `python scripts/build_site.py` — pass; 209 program pages, 34 university pages, 78 indexable sitemap URLs. Pending program pages exist even though they are excluded from the indexable sitemap.
- `python -m unittest discover -s tests -p test_static_site.py` — 12 passed.
- `node scripts/test_tracker_ui.mjs` — pass.
- `node scripts/test_site.mjs` — pass, desktop and 390px mobile.

## Live HTTP checks

Every program and university detail page, plus the homepage, `/sitemap.xml` and `/robots.txt`, returned HTTP 200 on the preview origin: **246 passed, zero failed**. Each request began with a new cookie jar, the deployment share query, and no Vercel account credentials. The cookie jar follows the share-link redirect and accepts its scoped access cookie, as an external browser would.

Request headers were `Cache-Control: no-cache`, `Pragma: no-cache` and `User-Agent: ItalyTracker-Independent-Review-Verification/1.0`. The full path inventory, response headers, final paths and response SHA-256 hashes are in `preview-http-verification.json`. Response headers include `x-vercel-id`, `x-vercel-cache`, `age`, `cache-control`, `etag`, `content-length` and `content-type` where present. The share secret and cookies are excluded from this evidence file.

All 246 response hashes equal the local build hashes after converting local Windows CRLF line endings to LF. Raw hashes are also retained. No content, whitespace other than CRLF, dates, URLs or values were normalized. This accounts for the difference between the Windows local build and Linux Vercel build.

## Live browser checks

The existing live-site browser test passed in fresh browser contexts without a Vercel login. It verified the 209 program and 34 university cards in initial HTML, 39 core-confirmed programs in the interactive view, search, filters, sorting, favorites, comparison, CSV export, three confirmed calendar events, program and university pages, metadata, keyboard navigation, dark theme and 390px mobile layout. Screenshots were saved under ignored `tmp/claude-review-preview-qa/`.

Command: set `SITE_URL` to the complete shareable URL and `SCREENSHOT_DIR` to an ignored temporary directory, then run `node scripts/test_live_site.mjs`. Browser interaction checks and HTTP content checks establish that the deployment serves this saved snapshot; they do not independently establish the correctness of university admissions facts.

## Production preservation

Vercel still resolves https://italy-it-programs.vercel.app/ to production deployment `dpl_9qrszHqJoWi8BsMYFrLg1Q84Caxq`, commit `e6995e70e7fc4673a561af69fbb7fa14ea84491b`, branch `master`. Its homepage contains the existing 193 program cards and 34 university cards.

Before/after production homepage SHA-256 is unchanged: `79c61d9233ef944dbae521142d1eae994ff8113f4c54acdc0a20e9bd1b89e9a7`. The checked production response was HTTP 200 with ETag `"0a59b88b533f39618670309e59491435"`. No research release was promoted to production.

## Package checks

Independent package validation covers ZIP CRC, SHA-256 inventories, byte-identical saved research files, 34 self-contained university batches, all 209 program IDs exactly once, all 700 source records and cross-university source references. The derived checklist, manifest and inventory preserve the share query on individual page links. Website HTML snapshots are matched to the 243 live detail-page hashes and grouped into 34 text uploads. The issue index includes 1,921 unresolved/verification fields, 26 classified conflicts, one broken source, three inconclusive sources and 13 redirects. The final package must be regenerated after the handoff commit so provenance identifies the saved files.
