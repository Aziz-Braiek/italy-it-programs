# Decision evidence refinement — 13 November 2026

Baseline: e039301. Availability remains 47 confirmed / 159 awaiting / 3 not offered. Original record review dates, application deadlines and calendar logic are unchanged. No production release.

## Before and after

Current-evidence counts include partial fields. Fully confirmed and Partly confirmed are shown separately below; they must not be conflated. Degree-structure labels describe sourced course structure and do not establish intake availability. Scholarship university counts mean at least one published applicable opportunity, not all programmes funded.

| Scope / field | Before current evidence | After current evidence | Fully confirmed | Partly confirmed | Degree structure | Not confirmed |
|---|---:|---:|---:|---:|---:|---:|
| program.duration | 29 | 29 | 29 | 0 | 16 | 18 |
| program.ects | 26 | 26 | 26 | 0 | 17 | 21 |
| program.prerequisites | 34 | 37 | 16 | 21 | 0 | 8 |
| program.english_requirement | 30 | 33 | 22 | 11 | 0 | 13 |
| program.admission_test | 7 | 10 | 1 | 9 | 0 | 37 |
| program.selection_method | 15 | 17 | 9 | 8 | 0 | 30 |
| program.minimum_grade | 2 | 21 | 3 | 18 | 0 | 26 |
| program.non_eu_seats | 1 | 1 | 1 | 0 | 0 | 46 |
| program.tuition | 9 | 9 | 8 | 1 | 0 | 27 |
| university.universitaly | 3 | 11 | 0 | 11 | 0 | 0 |
| university.documents | 7 | 9 | 0 | 9 | 0 | 2 |
| university.regional_dsu | 2 | 2 | 0 | 2 | 0 | 1 |
| university.visa_permit | 2 | 7 | 0 | 7 | 0 | 4 |
| university.scholarships | 4 | 4 | 1 | 3 | 0 | 2 |

Program denominator: 47. University denominator: 11. Previous-cycle-only counts and all source details are in summary.json and priority-field-ledger.json.

## Filter semantics and result counts

Default view contains only the 47 confirmed programme records. Including awaiting records currently gives the same four positive-filter totals. Conditional or applicant-dependent answers map to not confirmed for the binary filters. No English-certificate waiver is interpreted as a universal exemption. A published possible interview does not establish that a compulsory standardised exam exists or is absent.

| Filter | Before | After |
|---|---:|---:|
| no_test | 1 | 1 |
| certificate_required | 30 | 6 |
| tuition_documented | 9 | 9 |
| scholarship_documented | 17 | 17 |

Tuition/funding documented filters can include current partly confirmed facts only for the published amount/calculation/opportunity. The card names the remaining gaps. Older-cycle values are excluded. CSV keeps six provenance columns per field (value, cycle, URL, date, confirmation, missing components); historical values remain omitted. Degree-structure display does not make historical values eligible for export.

## Research findings and remaining limits

Added current country-of-qualification grade tables for Padua, Florence Software and the standard foreign-qualification Polimi MSc route; the Bologna/Bocconi joint route remains separate. Pisa department guidance now distinguishes the initial B2 statement from mandatory certification at Universitaly validation, rejecting MOI. Added scoped EAP documents/criteria and university-published standing document/permit guidance. The explicit two-year MUR procedure establishes Universitaly’s visa pre-enrolment requirement across the 11 hosts; most institution-specific deadlines remain unconfirmed. An undated recurring date is not promoted to a 2027/28 deadline.

No new 2027/28 tuition tariffs or non-EU quotas were established by the checked material. Polimi’s 2026/27 reserved-category maximum-fee rule is now shown as historical planning information, and never enters the current tuition filter. BBS formal calls remain forthcoming. Awaiting-program research was not extended this round: unresolved priority annual rules remain the more important gap.

## Conflicts

All nine saved conflicts/scope differences now appear on affected programme pages with official links and conservative handling, with compact card notes. Padua fees remain unconfirmed; HySET never becomes funded; differently stated Pisa historical fees are not merged; 28DIGITAL route calendars, document receipt years and award compatibility remain explicit. EAP changed: its university application page is now readable and explicitly says 24+6 credits, while its local requirements page says 18+6/TAPP. The narrower 24+6 online-route statement is published with the unresolved route distinction. One ambiguity entry was added for Florence Software: its published Cambridge B/C numerical bands overlap. The page now labels that language field Partly confirmed and asks for borderline-score clarification rather than repairing the bands. No application-deadline field was changed.

## Three randomly selected tuition records

All fully confirmed current tuition records in this snapshot share the 28DIGITAL consortium tariff. These are three programme checks, not independent tariff schedules.

- **discovered-017 — Cloud and Networking Infrastructure and HPC (CNIHPC) – 28DIGITAL track**, Università degli Studi di Trento: non-EU/EEA EUR 18,000/year. Exact official table passage: “18,000 EUR”. [Official fees](https://masterschool.28digital.eu/admissions/fees). Checked 2026-11-13; the citizenship row and annual-column context are saved in tuition-spot-checks.json.
- **discovered-015 — Fintech (FT) – 28DIGITAL Master’s track**, Università degli Studi di Trento: non-EU/EEA EUR 18,000/year. Exact official table passage: “18,000 EUR”. [Official fees](https://masterschool.28digital.eu/admissions/fees). Checked 2026-11-13; the citizenship row and annual-column context are saved in tuition-spot-checks.json.
- **discovered-016 — Human-Computer Interaction and Design with Extended Reality (HCID/XR) – 28DIGITAL track**, Università degli Studi di Trento: non-EU/EEA EUR 18,000/year. Exact official table passage: “18,000 EUR”. [Official fees](https://masterschool.28digital.eu/admissions/fees). Checked 2026-11-13; the citizenship row and annual-column context are saved in tuition-spot-checks.json.

## Every priority record with remaining gaps

The machine-readable ledger records each field, missing components, source URLs, checked date and why the available pages do not establish it. Every priority programme and host has an explicit outcome. Prior captures reused are identified; HTTP access is not treated as fact verification.

| Type | Stable ID | Programme/university | Unknown fields | Partly confirmed fields | Previous-cycle-only fields |
|---|---|---|---|---|---|
| program | legacy-001 | Computer Science and Engineering | duration, ects, admission_test, non_eu_seats | prerequisites, selection_method, minimum_grade | tuition |
| program | legacy-002 | Cyber Risk Strategy and Governance | ects, english_requirement, minimum_grade, non_eu_seats, tuition | prerequisites, admission_test, selection_method | — |
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
| university | bologna | Università di Bologna | visa_permit | universitaly, documents, regional_dsu | — |
| university | ca-foscari | Università Ca' Foscari Venezia | documents, visa_permit | universitaly | regional_dsu, scholarships |
| university | firenze | Università degli Studi di Firenze | — | universitaly, documents, visa_permit | regional_dsu, scholarships |
| university | napoli-federico-ii | Università degli Studi di Napoli Federico II | documents, regional_dsu, scholarships | universitaly, visa_permit | — |
| university | padova | Università degli Studi di Padova | visa_permit | universitaly, documents | regional_dsu, scholarships |
| university | pisa | Università di Pisa | — | universitaly, documents, regional_dsu, visa_permit, scholarships | — |
| university | politecnico-milano | Politecnico di Milano | — | universitaly, documents, visa_permit, scholarships | regional_dsu |
| university | politecnico-torino | Politecnico di Torino | visa_permit, scholarships | universitaly, documents | regional_dsu |
| university | tor-vergata | Università degli Studi di Roma Tor Vergata | — | universitaly, documents, visa_permit | regional_dsu, scholarships |
| university | torino | Università degli Studi di Torino | — | universitaly, documents, visa_permit | regional_dsu, scholarships |
| university | trento | Università degli Studi di Trento | — | universitaly, documents, visa_permit, scholarships | regional_dsu |

## What could not be completed

The checked official material does not establish all 2027/28 fees, quotas, deadlines, test policies or document exemptions. No guessed value was substituted. Previous-cycle awaiting coverage remains as it was. No substantive requirement was rejected; conditional requirements were conservatively kept out of universal yes/no matches. Field-level evidence is distinct from confirming a complete applicant profile.

## Checks

Run the research builder, static-site builder, research audit, Python regression suite, local browser suites and the protected live-preview suite. Tests cover exact yes/no/not-confirmed matching, historical exclusion, each saved conflict, partial badges, structural labels, collapsed card unknowns, CSV provenance and no-JavaScript output.
