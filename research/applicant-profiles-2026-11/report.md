# Applicant routes and tuition rules — 13 November 2026

Baseline: d1d75fe. Scope remains 209 programmes / 34 universities; 47 confirmed / 159 awaiting / 3 not offered. Preview only. No production promotion. The original record review dates and deadline facts are preserved.

## What changed

Phase 1 shipped first in 3fab14e: strict yes/no counts and covered/missing scope on every current partial field. The attached scope audit enumerates all 18 partly confirmed minimum-grade and 21 partly confirmed prerequisite records. Typed fee rules and explicit route mappings now drive an optional browser-only applicant profile. No route is inferred from prose deadline labels. National Universitaly requirements live once at national level; university deadlines stay separate.

## Before / after field counts

Each cell is **fully confirmed / partly confirmed / not currently confirmed**. The last component includes historical-only fields; their counts are shown separately. These counts describe the published scope, not complete eligibility for every individual applicant.

| Scope / field | Before F/P/N | After F/P/N | Historical-only before → after |
|---|---|---|---|
| program.duration | 29/0/18 | 29/0/18 | 0 → 0 |
| program.ects | 26/0/21 | 26/0/21 | 0 → 0 |
| program.prerequisites | 16/21/10 | 16/21/10 | 2 → 2 |
| program.english_requirement | 22/11/14 | 22/12/13 | 1 → 1 |
| program.admission_test | 1/9/37 | 1/9/37 | 0 → 0 |
| program.selection_method | 9/8/30 | 9/8/30 | 0 → 0 |
| program.minimum_grade | 3/18/26 | 3/18/26 | 0 → 0 |
| program.non_eu_seats | 1/0/46 | 1/0/46 | 0 → 0 |
| program.tuition | 8/1/38 | 8/2/37 | 11 → 11 |
| university.universitaly | 0/11/0 | 0/1/10 | 0 → 0 |
| university.documents | 0/9/2 | 0/9/2 | 0 → 0 |
| university.regional_dsu | 0/2/9 | 0/2/9 | 8 → 8 |
| university.visa_permit | 0/7/4 | 0/7/4 | 0 → 0 |
| university.scholarships | 1/3/7 | 1/3/7 | 5 → 5 |

Denominators: 47 programmes, 11 host universities. Degree-structure facts do not establish intake availability. Scholarship counts mean at least one scoped published opportunity. The Universitaly decrease removes the formerly duplicated national requirement from university-specific confirmation; it is not evidence that a national requirement disappeared.

Current tuition programme counts: fixed: **8**, band: **0**, rule-only: **2**, not confirmed: **37**. These are published-category counts, not a promise that all profiles have a confirmed fee. No current band was established. Historical ordinary Polimi band and Pisa contribution rule are excluded from confirmed filters and exported values.

## Three different university tuition checks

- **University of Bologna / discovered-029** — 2027/28 confirmed, rule-only. Exact source passage: “consists of a fixed element of € 157.04”. PDF page 15, section 8.1: a variable ISEE element follows. EUR 157.04 is not the total annual fee. No published course maximum is inferred. [Official source](https://corsi.unibo.it/s/3394/p/en/enrolling-grenfin/avvisolm-grenfin-emjm-27-28_en-2-prot.pdf/@@download/file/AvvisoLM-GrEnFIn-EMJM-27-28_EN-2-PROT.pdf).
- **Politecnico di Milano / legacy-001** — previous cycle (estimate only) — 2026/27, band. Exact source passage: “the amount gradually increases up to a maximum of € 3,943.04”. The page identifies 2026/27. Published ordinary-degree band EUR 157.04–3943.04 for a 46–74 ECTS plan, income/credit rules; reserved non-EU foreign-degree MSc students without eligible awards pay the applicable maximum. Not a confirmed 2027/28 fee. [Official source](https://www.polimi.it/en/prospective-students/how-much-does-it-cost/laurea-laurea-magistrale-and-single-cycle-programmes).
- **University of Pisa / legacy-052** — previous cycle (estimate only) — 2026/27, rule-only. Exact source passage: “the maximum annual all-inclusive tuition fee for students enrolled within the standard duration of their programme is €2,900.”. The sentence explicitly says 2026-2027. This is a named contribution maximum, not a verified new-cycle total or a computed range; regional tax/stamp and differently stated lower examples remain distinct. [Official source](https://www.unipi.it/en/education/registration/enrolment-and-registration/enrolment-for-international-students/university-fees-and-scholarships/).

These are three different institutional checks, not three claimed current complete annual tariffs. Full 2027/28 amounts could not be established from the checked sources.

## Same-program profile examples

EU example below uses the requested combined EU/EEA/CH selector; where that category is broader than the fee source it stays unknown. Italian-qualification does not imply citizenship or residence.

| Programme ID | Category / qualification origin | Next confirmed deadline | Current annual fee |
|---|---|---|---|
| legacy-052 | non-eu-abroad / non-eu | 2027-02-01 | Not confirmed (not confirmed) |
| legacy-052 | eu-eea-ch / non-eu | 2027-08-31 | Not confirmed (not confirmed) |
| legacy-052 | italian-qualification / italy | Not confirmed | Not confirmed (not confirmed) |
| legacy-002 | non-eu-abroad / non-eu | 2027-01-26 | Not confirmed (rule-only) |
| legacy-002 | eu-eea-ch / non-eu | 2027-01-26 | Not confirmed (rule-only) |
| legacy-002 | italian-qualification / italy | 2027-05-25 | Not confirmed (rule-only) |
| legacy-020 | non-eu-abroad / non-eu | 2027-01-31 | 18000 (fixed) |
| legacy-020 | eu-eea-ch / non-eu | 2027-01-31 | Not confirmed (not confirmed) |
| legacy-020 | italian-qualification / italy | Not confirmed | Not confirmed (not confirmed) |

Pisa CS: non-EU abroad 1 February vs EU/EEA/CH 31 August, with no automatic Italian-qualification fallback. Joint Cyber uses its own Bocconi foreign/Italian qualification rounds, never the ordinary Polimi calendar. Bologna 28DIGITAL has three EU-category application sessions but only the first confirmed visa-applicant session. Tuition uses citizenship rather than qualification origin. Profile controls cannot determine Swiss tariff, exact residence-permit entitlement, country-specific GPA row or language waiver; these remain explicit gaps.

## Complete remaining gaps and pages checked

- `priority-field-ledger.json`: each of the 47 × 9 programme and 11 × 5 university field outcomes, with value, cycle, sources, date, missing components and reason.
- `route-gap-ledger.json`: 470 programme/field rows, each with all 12 category/origin combinations explicitly resolved or unconfirmed (5,640 outcomes). Source-backed route IDs point into `compiled-routes.json`; checked pages and unresolved reasons are retained. Contradictory Italian-category/non-Italy-origin combinations are intentionally unconfirmed.
- `university-route-ledger.json`: every priority host’s own Universitaly/document outcome, checked pages and recognition limits.
- `record-outcomes.json`: all 47 programmes and 11 universities, including every unknown/historical/partial field.
- `verified-routes.json`, `national-rules.json`: canonical manually approved evidence; `compiled-routes.json` is derived.

Field-level checked URLs and host context pages are distinguished from approval: retrieval alone does not verify a fact. This round reuses explicitly cited same-day official captures and adds focused source checks, rather than claiming that every unchanged fact was newly verified.

| Type | Stable ID | Record | Unknown | Partial | Historical |
|---|---|---|---|---|---|
| program | legacy-001 | Computer Science and Engineering | duration, ects, admission_test, non_eu_seats | prerequisites, selection_method, minimum_grade | tuition |
| program | legacy-002 | Cyber Risk Strategy and Governance | ects, minimum_grade, non_eu_seats | prerequisites, english_requirement, admission_test, selection_method, tuition | — |
| program | legacy-004 | High Performance Computing Engineering | duration, ects, admission_test, non_eu_seats | prerequisites, selection_method, minimum_grade | tuition |
| program | legacy-020 | Computer Science and Engineering — Intelligent Embedded Systems (28Digital track) | duration, ects, admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | legacy-023 | Global MBA in AI and Manufacturing (Bologna Business School) | admission_test, selection_method, minimum_grade, non_eu_seats | — | prerequisites, english_requirement, tuition |
| program | legacy-029 | Computer Engineering | admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | legacy-030 | Computer Science | admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | legacy-031 | Cybersecurity | admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | legacy-032 | Data Science | admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | legacy-033 | Information Engineering | non_eu_seats, tuition | prerequisites, admission_test, selection_method, minimum_grade | — |
| program | legacy-034 | Aerospace Engineering | admission_test, non_eu_seats, tuition | minimum_grade | — |
| program | legacy-037 | Physics of Data | admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | legacy-052 | Computer Science | duration, ects, admission_test, minimum_grade, non_eu_seats | english_requirement, selection_method | prerequisites, tuition |
| program | legacy-053 | Cybersecurity | duration, ects, non_eu_seats | english_requirement, admission_test | tuition |
| program | legacy-054 | Artificial Intelligence and Data Engineering | duration, ects, minimum_grade, non_eu_seats | english_requirement, admission_test | tuition |
| program | legacy-055 | Data Science and Business Informatics | duration, ects, prerequisites, admission_test, minimum_grade, non_eu_seats | english_requirement, selection_method | tuition |
| program | legacy-125 | Software: Science and Technology | duration, ects, non_eu_seats, tuition | english_requirement, admission_test, selection_method | — |
| program | legacy-161 | Ingegneria gestionale — Management Engineering English-taught track | admission_test, non_eu_seats, tuition | minimum_grade | — |
| program | discovered-001 | Informatics for Digital Health | duration, ects, prerequisites, admission_test, minimum_grade, non_eu_seats | english_requirement, selection_method | tuition |
| program | discovered-002 | History | duration, ects, english_requirement, admission_test, selection_method, non_eu_seats, tuition | minimum_grade | — |
| program | discovered-003 | Classical Languages and Literatures and Ancient History | duration, ects, english_requirement, admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-004 | Historical Sciences | duration, ects, english_requirement, admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-005 | Landscape Studies | duration, ects, english_requirement, admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-006 | Religious Studies | duration, ects, english_requirement, admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-007 | Local Development | duration, ects, admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-008 | Mobility Studies | duration, ects, admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-009 | Chemical Engineering | duration, ects, prerequisites, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats, tuition | — | — |
| program | discovered-010 | Mechatronics Engineering | selection_method, minimum_grade, tuition | prerequisites, english_requirement, admission_test | — |
| program | discovered-011 | Buddhism and Asian Religions | admission_test, minimum_grade, non_eu_seats, tuition | prerequisites, english_requirement | — |
| program | discovered-012 | Cultures Littéraires Européennes (CLE) Erasmus Mundus Joint Master's Degree | ects, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats, tuition | prerequisites | — |
| program | discovered-013 | Cyber Security (CSES) – 28DIGITAL Master’s track | admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | discovered-014 | Data Science (DSC) – 28DIGITAL Master’s track | admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | discovered-015 | Fintech (FT) – 28DIGITAL Master’s track | admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | discovered-016 | Human-Computer Interaction and Design with Extended Reality (HCID/XR) – 28DIGITAL track | admission_test, selection_method, minimum_grade, non_eu_seats | prerequisites | — |
| program | discovered-017 | Cloud and Networking Infrastructure and HPC (CNIHPC) – 28DIGITAL track | admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | discovered-018 | Intelligent Chips and Systems (ICS) – 28DIGITAL track | admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | discovered-019 | Artificial Intelligence with Affective Computing (AIAC) – 28DIGITAL track | admission_test, selection_method, minimum_grade, non_eu_seats | — | — |
| program | discovered-020 | Hydrogen Systems and Enabling Technologies (HySET Erasmus Mundus Joint Master) | non_eu_seats, tuition | english_requirement, admission_test | — |
| program | discovered-029 | Greening Energy Market and Finance (GrEnFIn Erasmus Mundus Joint Master) | minimum_grade, non_eu_seats | tuition | — |
| program | discovered-037 | Astrophysics and Cosmology | admission_test, selection_method, non_eu_seats, tuition | prerequisites, minimum_grade | — |
| program | discovered-038 | Economic Analysis and Policy | ects, minimum_grade, non_eu_seats, tuition | prerequisites, english_requirement, admission_test | — |
| program | discovered-039 | Computer Engineering | duration, ects, minimum_grade, non_eu_seats | english_requirement, admission_test | tuition |
| program | discovered-040 | Data Science and Business Analytics | prerequisites, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats, tuition | — | — |
| program | discovered-041 | Artificial Intelligence for Management | prerequisites, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats, tuition | — | — |
| program | discovered-042 | Finance – Entrepreneurial Finance | prerequisites, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats | — | tuition |
| program | discovered-043 | Finance – Finance and Artificial Intelligence | prerequisites, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats | — | tuition |
| program | discovered-044 | Marketing Management – Analytics and AI for Marketing | prerequisites, english_requirement, admission_test, selection_method, minimum_grade, non_eu_seats, tuition | — | — |
| university | bologna | Università di Bologna | universitaly, visa_permit | documents, regional_dsu | — |
| university | ca-foscari | Università Ca' Foscari Venezia | universitaly, documents, visa_permit | — | regional_dsu, scholarships |
| university | firenze | Università degli Studi di Firenze | universitaly | documents, visa_permit | regional_dsu, scholarships |
| university | napoli-federico-ii | Università degli Studi di Napoli Federico II | universitaly, documents, regional_dsu, scholarships | visa_permit | — |
| university | padova | Università degli Studi di Padova | universitaly, visa_permit | documents | regional_dsu, scholarships |
| university | pisa | Università di Pisa | universitaly | documents, regional_dsu, visa_permit, scholarships | — |
| university | politecnico-milano | Politecnico di Milano | universitaly | documents, visa_permit, scholarships | regional_dsu |
| university | politecnico-torino | Politecnico di Torino | universitaly, visa_permit, scholarships | documents | regional_dsu |
| university | tor-vergata | Università degli Studi di Roma Tor Vergata | — | universitaly, documents, visa_permit | regional_dsu, scholarships |
| university | torino | Università degli Studi di Torino | universitaly | documents, visa_permit | regional_dsu, scholarships |
| university | trento | Università degli Studi di Trento | universitaly | documents, visa_permit, scholarships | regional_dsu |

## University-specific limits

- **Università di Bologna**: GrEnFIn has a current formal call and is distinct from Bologna's 28DIGITAL, CLE and BBS tracks. BBS pages advertise 2027/28 but say the formal calls/applications are forthcoming; undated fees, test/waiver sections are not rolled forward. CLE's current page links older formal criteria. Ordinary UniBo tuition and DSU rules do not automatically apply to professional masters.
- **Università Ca' Foscari Venezia**: The 2027/28 Buddhism route confirms qualification/preparation assessment and B2 proof. Open access is not itself a no-test exemption. The central fee index and pre-enrolment deadline page remain 2026/27; their numerical tariff/deadline is not relabelled as 2027/28. The current scholarship announcement leaves its formal application route/deadline forthcoming.
- **Università degli Studi di Firenze**: The current Software page links an explicit country-grade annex and describes possible preparation/English interviews. It does not establish a reserved non-EU quota, a separate compulsory standardised exam or its date/modality. General pre-enrolment guidance lists 31 July without an academic year; it is not promoted to a confirmed 2027/28 deadline.
- **Università degli Studi di Napoli Federico II**: Chemical Engineering's 2027/28 notice announces pre-evaluation and says guidelines/precise dates will follow. Its linked international-candidates page does not supply the promised current programme eligibility/fee/quota regulation. General visa/insurance guidance and the national Universitaly requirement do not establish programme admission criteria.
- **Università degli Studi di Padova**: The country table explicitly covers 27/28 and separates Bachelor and Master columns. Programme profiles link this table but do not establish every programme-specific grade/test/selection/quota rule. Some formal calls/quota fields are TBD. Undated portal EUR 2,950 is not a verified 2027/28 tariff and differs from the 2026/27 contribution notice.
- **Università di Pisa**: The 2027 calls and department page establish applicant routes and B2 certification timing, but annual fees are determined separately (the call's numerical examples are 2026/27). Old teaching regulations do not automatically establish 2027/28 credit rules. Absence of a quota or exam statement is not a no-quota/no-test exemption.
- **Politecnico di Milano**: The central tariff and HPC-specific curricular page explicitly cover 2026/27, so they do not prove a 2027/28 tariff or subject-credit rule. The current standard MSc dossier/country tables support the stated rules, with programme scoring/test/quota details still not established. Bocconi's joint route is separate.
- **Politecnico di Torino**: HySET publishes 2027–29 eligibility, grade scoring and possible interviews, but does not establish a compulsory standardised exam or reserved non-EU quota. The dated continuation notice says funding is not secured. Its undated self-funded fee quotation is not promoted to the 2027 cohort. Ordinary Polito 2026/27 instructions are a different route.
- **Università degli Studi di Roma Tor Vergata**: Mechatronics has its own current call, B2/GRE conditions, quota and Universitaly date. The general admissions landing page does not add a 2027/28 fee schedule or complete country-specific recognition alternatives. Conditional GRE routes cannot become a universal yes/no test flag.
- **Università degli Studi di Torino**: The recovered current EAP application page states 24+6 credits; its local requirements page says 18+6 and TAPP. Present both by route and retain the unresolved applicability. The central fee schedule is 2026/27; the linked EPOG tariff page has no independently dated 2027/28 tariff. Its June 10 translation date omits a year.
- **Università degli Studi di Trento**: The seven tracks use 28DIGITAL consortium rules, not ordinary UniTrento tuition. Published dossier/language/fee rules do not establish a universal no-test exemption, numeric GPA minimum, selection weights or reserved non-EU quota. University and consortium calendars/documents contain route/year differences; exact recipient instructions need confirmation.

## Conflicts and conservative readings

Padua fees remain unconfirmed: the undated portal contribution and older formal tariff differ in year/basis. Pisa’s historical lower examples are not merged into a new range; its own Universitaly page is still 2026/27. Florence’s saved conflict concerns overlapping Cambridge English bands, not tuition; neither the band nor a new fee is invented. Both sides remain linked on affected pages. Existing Trento/consortium later-round calendar and receipt-year differences, Bologna route distinctions, HySET unfunded continuation and EAP local/online credit thresholds remain separate.

New scope findings: the EU/EEA tariff does not establish Switzerland’s tariff; the Bocconi ordinary contribution does not independently establish the complete joint Cyber charge. These are scope gaps, not asserted source contradictions. `conflict-review.json` lists the exact official URLs and handling.

## What remains incomplete / choices

No prompt requirement was rejected. Unpublished data remain unknown rather than guessed. Awaiting programmes retain existing evidence and explicit empty route mappings; no additional awaiting-route claims were approved. The requested profile is deliberately coarse and cannot resolve every country/permit/funding/language condition. Three distinct current complete annual tariffs could not be verified; historical schedules are labelled as such. Programme availability was not promoted. No accounts, alerts, new universities, security weakening or production change.

## Verification

Run the research/site builders, research audit, original regression suites, Python profile guards and `scripts/test_applicant_profiles.mjs`. The profile suite exercises seven different programmes across every category, unknown combinations, URL round-trips, selected-route sorting and CSV/ICS, strict yes/no counts, no-JS full output and 320/390px open/collapsed selectors. Live preview checks repeat the browser flow. Passing these tests verifies behavior and provenance guards, not the truth of unpublished admissions data.
