# Official-source monitoring

Baseline: `900315e`. Production remains `c6dff07`. Monitoring never approves or edits an admissions fact, availability status, deadline, tuition, requirement or human review date.

## Privacy boundary

Git and GitHub Actions receive **non-content metadata only**: official URL dependencies, fingerprints, check dates, HTTP/cache metadata, failure counts/classes, affected records, boolean keyword flags and which flags flipped. Parsed robots allow/deny patterns and delay values are operational request-policy metadata. No university page text is retained by scheduled runs, uploaded as an artifact, committed, or included in the website.

`queue.json` and `archive.json` contain metadata only. Full normalized snapshots, source passages, before/after excerpts, local review output and `queue.md` are local and gitignored. The local baseline report, complete baseline responses, top-ten evidence and awaiting-program passages also remain ignored. `monitor_privacy.py` fails the website build if a monitoring snapshot/content file is tracked or metadata acquires a content-bearing key. It also rejects non-boolean keyword flags.

The inherited pre-monitoring research history already includes earlier approved research quotations. No monitoring snapshots, diff excerpts or keyword passages were committed in this round. Shared, already-published history has not been rewritten.

## Registry and cadence

`monitor_registry.py` deterministically extracts approved official dependencies from records, cited source IDs, inherited policies and research files. One canonical URL links to all citing records and fields. Tier A gates incomplete priority-program/host fields and awaiting-program admissions/requirements pages. Tier B covers other active course/call references. Tier C covers stable national/background guidance. A takes precedence when a source has multiple roles. Research-only URLs are retained and warned about, not silently deleted.

```console
python scripts/monitor_registry.py
python scripts/source_monitor.py plan --tiers A
python scripts/source_monitor.py run --tiers A --metadata-only
python scripts/source_monitor.py list
```

CLI monitoring always uses metadata-only persistence. The explicit flag makes the workflow’s policy visible. Automatic runs enforce a minimum seven days for A, one calendar month for B, and three calendar months for C. Manual dispatch does not bypass cadence. Durable reservations and per-source result checkpoints survive interrupted runs. A state-directory lock and Actions concurrency prevent overlapping runs.

Every source request uses the named monitor User-Agent with the repository issues contact URL, verified TLS, no account credentials or persistent cookies. Robots are checked before every source/redirect target; policy allows/denies, Crawl-delay and Request-rate are honoured. Each host handles one request at a time with at least two seconds after the preceding response. ETag/Last-Modified validators are reused. Redirects are logged; unapproved hosts, login walls and captchas are not bypassed. Transient errors retry at most twice with backoff; long Retry-After values defer checks.

## Change detection without remote text storage

Normalization removes navigation, cookie elements, headers/footers and unmistakable boilerplate while retaining admissions dates, numbers and tables. HTML and PDF text exists only in memory during scheduled checks. Normalized whole-page, sensitive-line and sampled-shingle hashes support unchanged/minor/substantive classification without retaining passages. Changes to sensitive numeric/requirements lines are conservative substantive flags. Keyword flags identify new tracked terms; the first baseline reports presence without claiming publication or applicability. These are review leads, not factual verification.

## Local review and resolution

An explicit local review is a human-triggered fetch, distinct from scheduled monitoring. It uses the same robots, TLS, account-free transport and per-host throttling. It updates source-check metadata only and never approves a record value. Do not run it automatically over the queue.

```console
python scripts/source_monitor.py review SOURCE_ID
python scripts/source_monitor.py resolve QUEUE_ITEM_ID --outcome "data updated" --commit REVIEWED_COMMIT_HASH
python scripts/source_monitor.py resolve QUEUE_ITEM_ID --outcome "no change needed" --commit REVIEWED_COMMIT_HASH
python scripts/source_monitor.py resolve QUEUE_ITEM_ID --outcome "source replaced" --commit REVIEWED_COMMIT_HASH
```

The review output is `private/reviews/SOURCE_ID.json`; last two distinct compressed local snapshots are under `snapshots/`. Exact before/after excerpts require a prior local snapshot. Hash-only CI history cannot reconstruct earlier text: if the local baseline is missing, the CLI says so and saves only the current snapshot. `queue.md` includes local review excerpts when available and must never be force-added to Git. A resolution requires an existing reviewed Git commit, date and explicit outcome; closed metadata stays in `archive.json`.

Add an official source explicitly, without approving admissions data:

```console
python scripts/source_monitor.py add-source OFFICIAL_URL --university UNIVERSITY_ID --program PROGRAM_ID --field FIELD_NAME --type HTML --tier A --official-basis "University-owned admission notice"
```

Repeat `--program` / `--field` for shared sources. Use `--type PDF` where appropriate. Rebuild the registry after approved dependency changes; the website build fails if a record cites an unregistered URL.

## GitHub Actions and bounded storage

The prepared workflow schedules A on Monday 05:17 UTC, B on day 1 monthly at 05:31 UTC, C on January/April/July/October day 1 at 05:43 UTC, plus tier-selectable dispatch. GitHub requires this workflow on default `master` before schedules/dispatch are active; this round does not merge or change master/production.

The workflow restores and exports **metadata only**, validated before upload. Artifacts retain metadata for 90 days; no snapshots or passages are uploaded. Compact state and open/closed metadata queues commit only to `monitoring/source-checks`. An explicit Vercel configuration disables deployments for that branch. The publisher allows only named monitoring metadata and the deployment guard; it never writes admissions datasets or a protected branch.

Limits: six workers, one per host; 8 MiB response; 150 PDF pages; 512 MiB total downloads per run; 60-minute fetch budget; 90-minute job timeout; 32 MiB metadata export cap. Explicit local snapshots are capped at 1 MiB normalized text each, two versions per URL, and a 128 MiB compressed local store. A >20% broken/blocked/unknown run fails visibly after saving safe results. Incomplete budgets fail visibly too. A failure never changes admissions data; after three consecutive source failures the queue marks that a new URL is needed.

## Public transparency

Only `public-checks.json` is copied to the site. Source-check dates, change flags, coverage and failure counts are separate from human factual review dates. Initial baselines cannot determine changes predating monitoring. Monitoring flags changes; nothing updates automatically. Queue items, hashes/flags review ledgers, full text and diffs are not shown on public pages.

## Verification and baseline limits

```console
python scripts/monitor_privacy.py
python -m unittest discover -s tests -p test_source_monitor.py
python scripts/build_research_data.py
python scripts/build_site.py
python scripts/audit_research_data.py
python -m unittest discover -s tests
node scripts/test_site.mjs
node scripts/test_tracker_ui.mjs
node scripts/test_applicant_profiles.mjs
```

Tests use stored synthetic fixtures and mocked transport, never live university servers. The real Tier A baseline attempted 517 URLs. It retained 377 normalized local text captures, 39 known broken/policy-denied checks and 34 blocked checks. A Windows checkpoint replacement failure left 67 HTTP outcomes unrecoverable and 176 successful captures without detailed headers/final-URL metadata. These are explicitly checker limitations, not asserted university failures. Nothing was re-fetched early. The writer now retries locks and saves independent per-URL checkpoints. The baseline health gate failed at 27.08%, including the unknown outcomes; it is not represented as green.
