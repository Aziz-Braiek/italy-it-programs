# Website audit findings — Italy University Tracker

**Baseline reviewed:** production site at `https://italy-it-programs.vercel.app/`, 10 November 2026
**Audit source:** “Italy University Tracker 2027-28: Website Audit,” prepared 10 November 2026
**Code baseline:** `d637c0c3e2cd793d60e3455d38510a8c95fca297` (`upgrade/2027-2028-research`)

The attached PDF was based on a static-only inspection. Findings below were checked against the live rendered application and source before implementation. “Confirmed” means the issue reproduces in the baseline; “not reproduced” means the specific claim did not hold in the test; “partially confirmed” separates a real gap from an inaccurate part of the claim.

## How the baseline was tested

- Fetched the production homepage directly: HTTP 200, 45,373 bytes. The returned HTML contains its title, hero, filters, metadata and loading placeholders, but no program or university names. The initial statistics are dashes, and both directories contain “Loading…” text.
- Opened the production URL in Microsoft Edge using a separate Playwright context. With JavaScript disabled, the title and heading remain but there are 0 program cards, 0 university cards and no statistics. With JavaScript enabled, the three research JSON requests succeed and render 23 program cards and 34 university cards; the displayed counts are 34 universities, 193 program records, 23 confirmed offers and 9 universities with confirmed date windows. No page or console errors occurred on this successful load.
- Aborted the program JSON request to simulate a load failure. The program area shows an error message, but it has no retry control and the university directory is cleared.
- Tested the language toggle: it switches the heading to Italian and back. Tested the program search: “Computer Science” narrows results. The filter change does not update the URL.
- Inspected keyboard interaction for a university disclosure: native `<details>/<summary>` opens with Enter. The visible page has 0 `aria-live` regions. Search has a programmatic label; each select has an `aria-label`, but the selects have no visible labels.
- Checked responsive layout at 390 × 844 and 1440 × 1000. Document and body widths equal the viewport at 390 px; there is no horizontal overflow. The mobile filter block is 291 px tall, wraps controls into rows and is not collapsible. The desktop filter bar is sticky; there is no Back to top link.
- Checked metadata and navigation in the rendered page and source: canonical URL, title, description, Open Graph type/url/title/description, `lang="en"`, robots.txt and sitemap.xml exist. The sitemap contains only the homepage. There is no `og:image`, Twitter card, JSON-LD, `<nav>` header or About/guide page. Footer anchors `#programs` and `#universities` point to existing section IDs.
- Opened the Italian language toggle and checked status chips’ computed foreground/background contrast. Sampled ratios were 8.55:1 or higher. Statuses are text-labeled.
- Checked all 454 source records (444 unique URLs) with HTTP HEAD requests, retrying access-denied/unsupported methods as a small ranged GET. Results: 204 returned 200, 138 returned 206, 1 returned 404, 1 returned 416, and 100 were inconclusive because of TLS-chain errors, timeouts or remote disconnections. The 416 was a range response for a PDF which is accessible in a browser. The confirmed 404 was Sapienza source `SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026`; `research/sources.json` now points to Sapienza’s replacement official PDF path. An HTTP failure caused by a site’s certificate or bot protection is not classified as a broken link.

## Findings matrix

### Critical problems and contradictions

| Audit recommendation / claim | Classification | Baseline finding and test |
|---|---|---|
| Pre-render university/program content; provide a no-JavaScript fallback | **CONFIRMED ISSUE** | Disabled-JavaScript browser and raw response both contain 0 records and only placeholders. |
| Add loading, error and retry behavior | **PARTIALLY CONFIRMED** | Loading placeholders are present. A forced JSON failure does clear the program loader and show an error, so it does not remain stuck forever; there is no retry action and the university grid is emptied. |
| Explain that 2027/28 details are still being published; give visitors useful context | **PARTIALLY CONFIRMED** | 23 core-verified 2027/28 offers are present after JavaScript loads, so the page is not empty for normal visitors. The 167 records requiring program-specific verification are mentioned, but there is no applicant-oriented publication context or calendar. |
| Replace internal research language with applicant language | **CONFIRMED ISSUE** | Live copy includes “Program research,” “unverified candidates,” “research leads,” “research checklist” and “All universities from the original tracker.” |
| Explain the “Italy IT” name and the limited 34-university scope | **PARTIALLY CONFIRMED** | The page title says Italy University Tracker and shows 34 universities, but does not explain that the selection follows the earlier tracker or that it is not a full inventory of Italy. Domain change is not warranted. |
| Remove or verify the Italian language switch | **NOT REPRODUCED** | It works: the main heading and interface change to Italian. The new design should retain the working control and keep its behavior clear. |
| Use consistent names for historical/pending records | **CONFIRMED ISSUE** | “Prior listings,” “unverified candidates,” “prior tracker entries” and “research leads” overlap in public copy. |
| Simplify overlapping record and field statuses | **PARTIALLY CONFIRMED** | Six record-status labels appear, while facts on the same record carry separate statuses. Detail fields preserve useful distinctions, but the public explanation blends record-level and field-level certainty. |
| Define “confirmed” and make the summary statistics unambiguous | **PARTIALLY CONFIRMED** | The values match the data after successful load, but “Offers confirmed” does not say it requires 2027/28 availability plus core name, level and language; “program records” mixes historical leads and new discoveries. |
| Standardize the academic-year format as 2027/28 | **CONFIRMED ISSUE** | Public copy mixes `2027–28`, `2027–2028` and `YYYY/YY`. |
| Show actual research progress rather than a permanent banner | **PARTIALLY CONFIRMED** | The notice dynamically reports 167 program records needing verification, so it is not a static banner. It does not say how many universities have been reviewed or explain the 34/34 research coverage. |

### Search, admissions information and applicant features

| Audit recommendation / claim | Classification | Baseline finding and test |
|---|---|---|
| Add filters for field, city/region, public/private, delivery mode | **CONFIRMED ISSUE** | The only filters are level, university, teaching language and record status. City and region exist in the research data; institution type and current delivery mode are not reliably represented, so those two filters must wait for sourced fields. |
| Filter by deadline/window, tests, scholarships and tuition | **CONFIRMED ISSUE** | These fields appear on some cards but cannot be used as filters. Only exact, cycle-supported information should drive these filters. |
| Cover single-cycle, PhD and other degree types | **PARTIALLY CONFIRMED** | The degree filter only offers BSc/MSc; the current 193-record dataset itself contains only BSc/MSc values. Other categories must not be added without verified records. |
| Sort by an upcoming confirmed deadline | **CONFIRMED ISSUE** | Only verification, university and program-name sorting are available. |
| Add an international application guide (visa, Universitaly, recognition, language/tests, fees/aid, residence permit) | **CONFIRMED ISSUE** | No guide exists; Universitaly is only a footer link. Some individual program cards contain requirements and fees, but not general step-by-step guidance. |
| Explain CIMEA, Declaration of Value, language tests, entrance exams, tuition and regional aid | **PARTIALLY CONFIRMED** | Some program-specific facts exist, but the site does not explain terms or distinguish general guidance from course-specific rules. |
| Add a glossary and FAQ | **CONFIRMED ISSUE** | Neither appears in the public page. |
| Add shortlist/favorites, comparison and CSV/calendar exports | **CONFIRMED ISSUE** | No such controls or local persistence exist. |
| Add publication alerts | **RECOMMENDED ENHANCEMENT** | No alert control exists. No notification service or explicit notification-consent workflow is configured, so alerts should remain deferred rather than be shown as nonfunctional controls. |
| Show a change log and per-record last-verified dates | **PARTIALLY CONFIRMED** | One global research date is visible. `last_checked` exists in the research JSON but is not shown on cards or university details; there is no public update log. |
| Add a correction-report route without an unmoderated backend | **CONFIRMED ISSUE** | No reporting path is present. The GitHub repository has an enabled Issues page, suitable for a moderated correction link and structured issue template. |
| Add an About page and explain editorial responsibility / non-affiliation | **CONFIRMED ISSUE** | The footer calls the site a research snapshot, but there is no About page, scope statement or non-affiliation statement. |
| Explain why there are 34 universities and what is excluded | **CONFIRMED ISSUE** | The live text says they are the original tracker universities but gives no selection method or coverage limitation. |

### Navigation, SEO, accessibility and performance

| Audit recommendation / claim | Classification | Baseline finding and test |
|---|---|---|
| Add header navigation | **CONFIRMED ISSUE** | No semantic `<nav>` or header links; only footer links are present. |
| Verify `#programs` and `#universities` anchors | **NOT REPRODUCED** | Both IDs exist and match the footer links. |
| Add individual program/university URLs and preserve filters in shareable URLs | **CONFIRMED ISSUE** | There are no detail routes. Search changes the visible results but leaves the URL unchanged. |
| Add Back to top and sticky filters | **PARTIALLY CONFIRMED** | Desktop filters are already sticky; mobile CSS makes them relative. No Back to top link exists. |
| Add social sharing metadata and a social image | **PARTIALLY CONFIRMED** | Canonical, title, description and four Open Graph tags exist. `og:image` and Twitter-card tags do not. |
| Add suitable structured data | **CONFIRMED ISSUE** | No JSON-LD is present. Dataset-level metadata is appropriate; uncertain program entries should not receive misleading course schema. |
| Add a sitemap and robots configuration | **PARTIALLY CONFIRMED** | robots.txt points to a valid sitemap, but that sitemap only lists the homepage, not indexable university/program pages. |
| Set the HTML language | **NOT REPRODUCED** | The root is `<html lang="en">`; the working language toggle changes it to `it`. |
| Give decorative emoji accessible alternatives | **PARTIALLY CONFIRMED** | The language button has an accessible name; the warning icon is not marked decorative/hidden. |
| Ensure colored status chips also convey state in text | **ALREADY IMPLEMENTED** | Cards expose visible status words, not color alone. Status contrast was sampled at 8.55:1 or higher. Adding a small non-color icon is still a useful enhancement. |
| Announce loading/result updates with `aria-live` | **CONFIRMED ISSUE** | No element has an `aria-live` attribute; results and counts change without a live announcement. |
| Give university disclosures keyboard support and expanded state | **ALREADY IMPLEMENTED** | Native `<details>/<summary>` receives keyboard focus and opens with Enter. It does not set a manual `aria-expanded`, which native disclosure semantics do not require. |
| Add visible labels to filter controls | **PARTIALLY CONFIRMED** | Search has an associated visually hidden label and selects have `aria-label`s, so they are programmatically named; the select labels are not visible. |
| Verify status-chip contrast | **NOT REPRODUCED** | Sampled status combinations meet WCAG AA text contrast; measured ratios range from 8.55:1 to 9.88:1. |
| Use a collapsible mobile filter drawer | **PARTIALLY CONFIRMED** | There is no horizontal overflow and controls wrap, but the filter block occupies 291 px and is not collapsible. |
| Use one data fetch and one loading state | **PARTIALLY CONFIRMED** | Three JSON files are fetched in parallel through a single `Promise.all`, with one completion/error path. The page still has separate visible placeholders and the failure path loses the university directory. |
| Paginate/progressively render the 193 records | **CONFIRMED ISSUE** | Default view renders 23 cards. Selecting “Include unverified candidates” renders all records without pagination. |
| Put a short status legend near results and link to full methodology | **CONFIRMED ISSUE** | The explanations are at the bottom of the long page; no compact legend is beside the filters. |
| Simplify dense/defensive wording | **CONFIRMED ISSUE** | The explanatory copy uses internal workflow terminology and long qualification-heavy sentences. |
| Preserve source-linked evidence, honest unknowns and the no-inferred-acceptance-rate rule | **ALREADY IMPLEMENTED** | Program and university cards link to official sources; uncertainty and source conflicts are recorded; no acceptance-rate estimate is invented. Preserve this research approach. |

## URL-check detail

The URL audit confirmed one dead source path, not a systemic link failure. `SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026` used a Sapienza PDF path that returned HTTP 404. Sapienza’s official admissions page links to the replacement file at `https://www.uniroma1.it/sites/default/files/field_file_allegati/academic_requirements_movein_2026-2027_web.pdf`; the replacement is recorded in `research/sources.json` and opens as a 130-page official PDF. The Roma Tre PDF that returned HTTP 416 to a ranged HEAD request opened successfully in a browser, so it was not classified as broken. Other non-success cases were inconclusive where requests failed TLS validation, timed out or were disconnected; do not rewrite those URLs without browser/source confirmation.

## Implementation order

1. Generate useful static HTML from the research JSON so content and statistics are present with JavaScript disabled; keep client-side behavior as progressive enhancement.
2. Reframe the homepage for applicants, clarify scope and counting rules, and simplify status labels without changing the underlying research statuses.
3. Add supported filters, confirmed-deadline sorting, pagination, shareable URLs, university/program pages, local favorites, comparison and exports.
4. Add the official-source application guide, About, Methodology, update dates and moderated correction link.
5. Expand SEO and accessibility, then validate desktop/mobile, data/source integrity and the Vercel preview before production promotion.

## Remaining audit limits

HTTP checks alone cannot prove that a source URL supports every fact attributed to it. 100 URL checks were inconclusive due to TLS, timeout or remote-disconnect behavior; those require a browser/source-page review before any data changes. The post-change audit must retest any baseline issue changed by implementation.

## V2 implementation verification

The generated build was checked after the implementation against the classifications above:

- **Initial rendering and JavaScript failure modes — resolved:** the first HTML response contains all 193 program records and 34 university cards. Edge/Playwright with JavaScript disabled confirms the content remains visible; the new site does not fetch its directory JSON at runtime, so the old loading/error/retry path no longer applies.
- **Broken Sapienza source — resolved:** the source record, research script constant and report references use the replacement official PDF path. The browser opens the replacement PDF.
- **Search and applicant controls — implemented:** status, location, field, degree, language, date, tuition-information and scholarship-information filters; sorting; pagination; URL-backed filters; local favorites; comparison; CSV; and calendar export are present. Calendar events are limited to source-supported current-cycle dates, retain applicant-group notes, and include all distinct future windows for a saved program.
- **Navigation and SEO — resolved:** header links, program/university detail URLs, canonical metadata, Open Graph and Twitter cards, Dataset JSON-LD, robots.txt and a sitemap with 62 indexable URLs are generated. Pending program pages are `noindex` and omitted from the sitemap.
- **Accessibility and responsive layout — improved:** visible filter labels, live result announcements, keyboard-operable controls, clear focus states, reduced-motion handling and collapsible mobile filters are present. Playwright found no horizontal overflow at 390 × 844; the visible Edge review checked the desktop homepage, filters/cards and a source-linked program detail page.
- **Directory rendering and asset size — measured:** homepage HTML is 399,895 bytes raw / 25,719 gzip; CSS 23,226 / 5,686 gzip; JavaScript 25,938 / 7,275 gzip; social image 7,452 / 2,460 gzip. These compressed figures were calculated locally; Vercel preview response headers still need checking.
- **Guide and scope — implemented:** the application guide, glossary, FAQ, About, Methodology, update-date page and moderated correction issue template are generated. The site still covers a selected set of 34 universities, not Italy as a whole.

Validation at this checkpoint: 11 static-site unit tests passed; the research-data audit passed with 34 universities, 193 program records, 23 confirmed offers and 454 sources; the legacy tracker UI regression suite passed; the new Edge/Playwright suite passed including JavaScript-off rendering, desktop search/filter/exports, three confirmed windows in calendar export, keyboard interaction and 390-pixel mobile overflow checks. The Vercel preview for the V2 commit remains to be deployed and verified before production promotion.

The language control translates interface labels; program names and source-derived admissions text remain in their source language. Tuition ranges remain unsorted because the current values do not share a reliable comparison basis. Alerts and a historical field-level change log remain deferred because there is no consent-backed notification system or complete snapshot history.
