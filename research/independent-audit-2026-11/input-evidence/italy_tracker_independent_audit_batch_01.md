# Italy University Tracker — Independent official-source audit, initial batch

**Audit date:** 11 November 2026  
**Target cycle:** 2027/28  
**Status:** Official-source fact check only. **NOT a completed website discrepancy audit:** the latest review ZIP / research JSON was not uploaded into this chat, and the GitHub branch and Vercel share preview could not be fetched here. Record IDs and published tracker values must be matched against the actual dataset before proposing edits.  
**Coverage in this batch:** 5 university-level source reviews (Padua, Bologna, Ca' Foscari Venice, Pisa, Messina), with selected programme-level facts. This does not count as auditing every course at those universities.

## 1. University of Padua — Department of Historical and Geographic Sciences and the Ancient World

- **Official source:** https://www.dissgea.unipd.it/en/en/international-students-202728-applications
- **2027/28 application rounds:** 15 Sep 2026–15 Nov 2026; 1 Dec 2026–1 Mar 2027; 1 Apr 2027–1 Jun 2027 (third call limited to EU applicants and non-EU applicants residing in Italy).
- The department explicitly states the dates apply to its degree programmes, including History; Classical Languages and Literatures and Ancient History; Historical Sciences; Landscape Studies; Religious Studies; Local Development; Mobility Studies. The department distinguishes Italian-taught from English-taught degrees.
- **Audit action:** Check exact deadlines and third-round applicant eligibility on each relevant tracker record. The first call closes on 15 November 2026, four days after this audit date. Do not generalise these departmental dates to all Padua degrees.

## 2. University of Bologna — Intelligent Embedded Systems

- **Official programme source:** https://corsi.unibo.it/magistrale/IngegneriaScienzeInformatiche/curriculum-intelligent-embedded-systems-28digital-track
- **Official programme admission source:** https://corsi.unibo.it/2cycle/ComputerScienceEngineering/how-to-enrol
- Intelligent Embedded Systems is an English-taught curriculum of the Computer Science and Engineering master's, with separate **local** and **28Digital** tracks and distinct admission procedures.
- The 28Digital track has **10 places** according to Bologna's admissions page. The local track has **15 places**.
- 28Digital 2027/28 application rounds: 30 Oct 2026–31 Jan 2027; 1 Feb–18 Apr 2027; 19 Apr–31 May 2027. The final round is restricted to EU/EEA/Swiss and non-EU applicants who do not require a study visa; the middle round has further non-EU restrictions.
- Minimum English proficiency for the Intelligent Embedded Systems curriculum is B2; refer to official requirements for accepted evidence.
- **Audit action:** Check that the tracker does not label the whole degree as English-only, conflate the two tracks, or attach a local-track €50 application fee to the 28Digital application without evidence.

## 3. Ca' Foscari University of Venice — Buddhism and Asian Religions

- **Official course:** https://www.unive.it/web/en/21007/home
- **Official admission:** https://www.unive.it/web/en/21002/admission-and-enrolment
- This is an English-taught, two-year, 120-credit LM-64 master's, planned active **from 2027/28**, at Venice; the programme is identified as open admission, subject to qualification and preparation checks.
- The official admission page states **2027/28 procedures and deadlines will be updated in March 2027**.
- **Audit action:** Mark the programme availability confirmed, but do not invent an application deadline. Check international-qualification procedures separately. Do not interpret 'open admission' as 'no eligibility assessment'.

## 4. University of Pisa — computer-related master's programmes

- **Official 2027/28 engineering call:** https://computer.ing.unipi.it/call-for-international-students/
- Applies to **MSc Computer Engineering** and **MSc Artificial Intelligence and Data Engineering** for applicants with non-Italian bachelor's qualifications.
- **Application deadline:** 1 Feb 2027 at 23:59 GMT, strict. **Fee:** €30 *per application*. A maximum of two MSc applications can be filed via that portal. **English:** B2 all four skills for visa applicants; the programme explicitly says a medium-of-instruction letter alone is insufficient. Required documents cannot be supplemented after the deadline.
- The engineering call says the **2027/28 tuition will be announced around June 2027**. The €290–€2,900 values given on that page are **2026/27 only** and cannot be carried forward as confirmed 2027/28 fees.
- **Official University of Pisa general English MSc admissions page:** https://www.unipi.it/en/education/registration/enrolment-and-registration/enrolment-for-international-students/masters-degree-held-in-english/
- **Important official-source inconsistency:** this general page labels its table 'Applications deadlines a. a. 2026-2027' while listing opening dates in November 2026 and deadlines in 2027 (e.g., Computer Science, Data Science and Business Informatics, Informatics for Digital Health). Treat the year label as inconsistent; do not use the page alone to assert the target academic year for every programme. Resolve against programme-specific 2027/28 calls.
- **Other official course:** https://www.unipi.it/en/education/courses/master-degree/data-science-and-business-informatics-wdb-lm-en/ confirms Data Science and Business Informatics is an English-taught master's, interclass LM-18 / LM-DATA, with B2 English and degree/credit prerequisites.
- **Audit action:** Compare two engineering MSc calls separately from the three Computer Science department records. Avoid globally transferring the engineering deadline/fee to unrelated programmes.

## 5. University of Messina — international applications

- **Official source:** https://international.unime.it/study-us/application-and-admission
- **2027/28 early-bird call:** 1–20 December 2026 for specified non-EU visa applicants already holding final academic documents, language evidence and DoV/CIMEA comparability evidence. This is not an unrestricted call for every international applicant.
- **Application fee:** €40 for up to two submissions across calls, non-refundable.
- The university distinguishes English-taught and Italian-taught application portals.
- **Audit action:** Ensure that the first call's applicant restrictions and the two-application fee structure are properly scoped. A university-wide application call is not proof of a new first-year intake for each individual programme.

## Next steps to make these actionable

1. Match each fact to the exact stable `program_id` and official-source record in `research/claude-review-manifest.json`, `research/programs-2027-2028.json` and `research/sources.json`.
2. For each field, record `tracker_value`, `official_value`, `cycle`, `official_source_url`, `checked_at`, and `outcome`: `MATCH`, `CORRECTION_CONFIRMED`, `SOURCE_CONFLICT`, `PENDING_ANNOUNCEMENT`, or `NO_COMPARISON_DATA`.
3. Never label a proposed correction `CORRECTION_CONFIRMED` unless the source and the actual latest tracker value were both examined.
4. Continue systematically through all 34 universities, all 209 programme records, and the 700 source records. Do not count the above source review as a full programme-by-programme audit.
5. Keep audit changes separate from research implementation, test all data updates, and deploy nothing until the comparison audit passes.
