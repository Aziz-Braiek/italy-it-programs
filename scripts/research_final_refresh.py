"""Cycle-specific evidence found during the final 2027/28 refresh."""

from __future__ import annotations

from typing import Any, Callable


SOURCES = [
    {
        "id": "SRC-PADUA-ASTROPHYSICS-COURSE-PROFILE-2027",
        "university_id": "padova",
        "title": "Astrophysics and Cosmology – official degree profile",
        "url": "https://www.unipd.it/en/corsi-di-laurea/astrophysics-and-cosmology",
        "source_type": "Official University degree programme profile",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The current official University profile identifies Astrophysics and Cosmology as an English-taught two-year Master's Degree in Padua, open admission with requirements, in degree classes LM-17 R Physics and LM-58 R Sciences of the Universe. The current profile establishes identity and general course characteristics, while the separate Department notice supplies the named 2027/28 international call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.access", "program.degree_class"],
    },
    {
        "id": "SRC-PADUA-ASTROPHYSICS-2027-CALL",
        "university_id": "padova",
        "title": "Astrophysics and Cosmology – 2027/28 international application call and requirements",
        "url": "https://astrophysics-and-cosmology.dfa.unipd.it/masters-degree/application-and-admission-requirements/",
        "source_type": "Official Department programme and international admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The official Department page says the first international call is open for applicants with an international Bachelor's degree who seek entry in AY 2027/28 (October 2027), with a 15 November 2026 deadline. It also publishes course entry criteria of 24 ECTS in Physics and 24 ECTS in Mathematics and committee assessment/interview details, but those criteria are not explicitly labelled for 2027/28. Official search results exposed the page content, but direct content retrieval and the fresh HTTP check were inconclusive on 11 November; do not classify the URL as broken. The page also contains prior-cycle 2026/27 information, which is not treated as current-cycle evidence.",
        "supports": ["program.availability_2027_2028", "program.application_deadline", "program.applicant_scope", "program.admission_requirements"],
    },
    {
        "id": "SRC-PADUA-PHYSICS-DATA-PROFILE",
        "university_id": "padova",
        "title": "Physics of Data – official degree profile",
        "url": "https://www.unipd.it/en/corsi-di-laurea/physics-data",
        "source_type": "Official degree programme profile",
        "accessed_at": "2026-11-10",
        "cycle": "general",
        "evidence": "Identifies Physics of Data as an English-taught Master's Degree (LM-17 R, Physics), open admission with requirements, in Padua, with a two-year duration.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.access"],
    },
    {
        "id": "SRC-PADUA-PHYSICS-DATA-REQUIREMENTS",
        "university_id": "padova",
        "title": "Physics of Data – admission requirements",
        "url": "https://pod.dfa.unipd.it/requirement/",
        "source_type": "Official programme requirements page",
        "accessed_at": "2026-11-10",
        "cycle": "general",
        "evidence": "The programme requires a Bachelor's degree or equivalent (minimum three years) with demonstrated Physics and Mathematics skills, and English at B2 CEFR or equivalent. The page says applicants with international degrees must follow the applicable admission call; the general wording about publication in June is not used as the 2027/28 international call timing.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement"],
    },
    {
        "id": "SRC-PADUA-PHYSICS-DATA-2027-CALL",
        "university_id": "padova",
        "title": "Physics of Data – 2027/28 first call for international students",
        "url": "https://pod.dfa.unipd.it/the-first-call-for-international-students/",
        "source_type": "Official programme admission announcement",
        "accessed_at": "2026-11-10",
        "cycle": "2027-2028",
        "evidence": "The 2 October 2026 announcement names Physics of Data, invites applicants with an international Bachelor's degree (including candidates graduating by July 2027) for entry in AY 2027/28, and gives 15 November 2026 as the first-call deadline. It does not specify the opening date, later application rounds, application fee, or 2027/28 course-specific requirements.",
        "supports": ["program.availability", "program.application_deadline", "program.eligible_group"],
    },
    {
        "id": "SRC-PADUA-SCIENCE-MSC-CATALOGUE-2026",
        "university_id": "padova",
        "title": "Master's degree courses of the School of Science – AY 2026/27",
        "url": "https://www.unipd.it/en/node/79192",
        "source_type": "Official School of Science admissions and programme inventory",
        "accessed_at": "2026-11-10",
        "cycle": "2026-2027",
        "evidence": "The 2026/27 School of Science catalogue explicitly includes Physics of Data among its Master's courses and links the annual admission notice. This establishes the prior-cycle listing only; the separate programme announcement is the evidence for 2027/28 international intake.",
        "supports": ["program.previous_cycle_course_listing"],
    },
    {
        "id": "SRC-PADUA-STUDY-ENGLISH-APPLY-2027",
        "university_id": "padova",
        "title": "Study in English – How to apply",
        "url": "https://www.unipd.it/en/studiare-inglese-come-fare-domanda",
        "source_type": "Official international application procedure",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "For English-taught degrees other than Medicine and Surgery, applicants use apply.unipd.it, may apply to up to two courses, and normally pay a non-refundable €60 application fee. The English procedure page contains a malformed 2027/28 Call Two date (1 December 2027–1 March 2027); the official Italian rendering gives 1 December 2026–1 March 2027. Use the Italian page for call windows and retain this English page only as evidence of the English applicant route, fee and the translation discrepancy.",
        "supports": ["university.application_route", "university.application_fee", "program.application_fee_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-GRENFIN-2027-PROFILE",
        "university_id": "bologna",
        "title": "Greening Energy Market and Finance – official degree profile",
        "url": "https://corsi.unibo.it/2cycle/GreeningEnergyMarketFinance",
        "source_type": "Official degree programme profile",
        "accessed_at": "2026-11-10",
        "cycle": "2027-2028",
        "evidence": "The profile identifies Greening Energy Market and Finance as a two-year second-cycle degree, LM-16 Finance, taught entirely in English in Bologna, with three tracks and mobility at partner universities Ludwig-Maximilians-Universität München and Université Paris Dauphine.",
        "supports": ["program.name", "program.level", "program.language", "program.field", "program.location", "program.duration", "program.mobility"],
    },
    {
        "id": "SRC-UNIBO-GRENFIN-2027-CALL",
        "university_id": "bologna",
        "title": "Greening Energy Market and Finance – AY 2027/28 admission notice",
        "url": "https://corsi.unibo.it/s/3394/p/en/enrolling-grenfin/avvisolm-grenfin-emjm-27-28_en-2-prot.pdf/@@download/file/AvvisoLM-GrEnFIn-EMJM-27-28_EN-2-PROT.pdf",
        "source_type": "Official 2027/28 programme admission notice PDF",
        "accessed_at": "2026-11-10",
        "cycle": "2027-2028",
        "evidence": "The 18-page AY 2027/28 call confirms the Erasmus Mundus joint Master's, up to 51 places, application dates 14 October 2026–7 January 2027 at 11:00 CET, a first-cycle degree in specified fields, English B2, a 100-point selection with 60-point eligibility threshold and interview for candidates scoring at least 80, and up to 18 full Erasmus Mundus scholarships of €1,400 gross/month. It describes self-funded University tuition as €157.04 fixed plus an ISEE-variable amount up to a programme-specific maximum, but does not state that maximum or a programme application fee.",
        "supports": ["program.availability", "program.application_windows", "program.application_deadline", "program.requirements", "program.application_route", "program.seats", "program.tuition", "program.scholarships"],
    },
    {
        "id": "SRC-UNIBO-AI-PROFILE-2026",
        "university_id": "bologna", "title": "Artificial Intelligence – official degree profile",
        "url": "https://corsi.unibo.it/2cycle/artificial-intelligence/",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: identifies an English-taught two-year MSc in Bologna, classes LM-18/LM-32, open access with a skills assessment, and the Department of Computer Science and Engineering (DISI). The profile does not name a 2027/28 intake.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-AI-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Artificial Intelligence – 2026/27 admission requirements and call",
        "url": "https://corsi.unibo.it/2cycle/artificial-intelligence/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: the current enrolment page links the 2026/27 call and describes degree-background, English B2, Italian-language and personal-preparation assessment requirements. No 2027/28 call or named intake is linked on the reviewed page.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-DHDK-PROFILE-2026",
        "university_id": "bologna", "title": "Digital Humanities and Digital Knowledge – official degree profile",
        "url": "https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge/",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: identifies Digital Humanities and Digital Knowledge as an English-taught second-cycle programme in Bologna, LM-43, open access with an assessment, under the Department of Classical Philology and Italian Studies (FICLIT). This current profile does not name a 2027/28 intake.",
        "supports": ["program.name", "program.level", "program.language", "program.location"],
    },
    {
        "id": "SRC-UNIBO-DHDK-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Digital Humanities and Digital Knowledge – 2026/27 admission page",
        "url": "https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: links only the expired 2026/27 call and describes the current admission summary. The current programme page contains no 2027/28 call or named intake.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-BA-CURRICULUM-2026",
        "university_id": "bologna", "title": "Business Analytics – current official curriculum profile",
        "url": "https://corsi.unibo.it/2cycle/BusinessAnalytics/overview",
        "source_type": "Official curriculum profile", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "The live official profile identifies Business Analytics as an English-language curriculum within the two-year Second Cycle Degree in Statistics, Economics and Business (LM-82), taught in Bologna; it is not a separate degree programme. It says all courses in the curriculum are taught in English and the parent degree is open access. The current page has no 2027/28 marker or cycle-specific admissions call, so it supports identity, language, location and curriculum structure only, not new-entry availability or annual admission terms.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.program_type"],
    },
    {
        "id": "SRC-UNIBO-BA-CURRICULUM-PARENT-2026",
        "university_id": "bologna", "title": "Statistics, Economics and Business – current parent degree profile",
        "url": "https://corsi.unibo.it/2cycle/StatisticsEconomicsBusiness",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "The live official parent profile lists Statistics, Economics and Business as the Bologna LM-82 second-cycle degree, with Italian and English delivery and Business Analytics among its curricula. It describes the programme as open access. The current profile has no 2027/28 marker or programme-specific admission dates and does not confirm a new cohort for that cycle.",
        "supports": ["program.parent_degree", "program.program_type", "program.language"],
    },
    {
        "id": "SRC-UNIBO-MES-PROFILE-2026",
        "university_id": "bologna", "title": "Mechanical Engineering for Sustainability – official degree profile",
        "url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: identifies Mechanical Engineering for Sustainability as an English-taught LM-33 MSc in Forlì, open access with assessment of personal competencies, in the Department of Industrial Engineering (DIN). The profile does not name a 2027/28 new-entry intake.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-MES-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Mechanical Engineering for Sustainability – 2026/27 admission page",
        "url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: links the 2026/27 call and displays current course/admission requirements. No 2027/28 new-entry call is linked. The generic page says Italian B2 is also required, while the named 2026/27 call's language section specifies English B2; keep that discrepancy visible and verify the next call.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-MES-CALL-2026",
        "university_id": "bologna", "title": "Mechanical Engineering for Sustainability – 2026/27 admission call",
        "url": "https://corsi.unibo.it/s/3427/p/en/programma-enrolment-new/bando-lm-aerospace_ita_2025-26-def-1.pdf/@@download/file/Bando%20LM%20MES%2026-27_ENG.pdf",
        "source_type": "Official 2026/27 admission call PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 24-page call explicitly names Mechanical Engineering for Sustainability, LM-33, course code 6720, for AY 2026/27. It gives three applicant-group-specific selection intakes, entry-credit and English B2 requirements, interview procedures, and the annual ISEE-based tuition framework. The current 2026/27 call is historical evidence and does not confirm 2027/28 availability or terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_program_requirements", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-UNIBO-MES-NOTICE-BOARD-2026",
        "university_id": "bologna", "title": "Mechanical Engineering for Sustainability – current notice board",
        "url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli/notice-board",
        "source_type": "Official degree programme notice board", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Checked 11 November 2026: the board lists an AY 2027/28 Overseas mobility call for current first- and second-year students, not an incoming first-year admission call. The admissions page separately links only the 2026/27 programme call; do not treat the mobility notice as 2027/28 new-entry confirmation.",
        "supports": ["program.cycle_marker_scope", "program.mobility_not_admission"],
    },
    {
        "id": "SRC-UNIBO-CLABE-PROFILE-2026",
        "university_id": "bologna", "title": "Business and Economics (CLaBE) – official degree profile",
        "url": "https://corsi.unibo.it/1cycle/CLaBE/Presentation",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: identifies CLaBE as a three-year first-cycle degree taught entirely in English and open to Italian and international students; the profile directs applicants to the annual official call.",
        "supports": ["program.name", "program.level", "program.language", "program.location"],
    },
    {
        "id": "SRC-UNIBO-CLABE-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Business and Economics (CLaBE) – current admission page",
        "url": "https://corsi.unibo.it/1cycle/CLaBE/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: links only the expired 2026/27 selection call and gives a current selection summary, including a 190-place cap (special-programme places included), a SAT entrance test and matriculation information for the 2026/27 cohort. It does not link a 2027/28 incoming-student call.",
        "supports": ["program.previous_cycle_application_route", "program.previous_cycle_seats", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIBO-CLABE-CALL-2026",
        "university_id": "bologna", "title": "Business and Economics (CLaBE) – 2026/27 admission call (English translation)",
        "url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clabe/clabe-clame-call-for-applications-2025_26-1.pdf/@@download/file/CLABE-CLAME%20Call%20for%20Applications%202025_26%20(1).pdf",
        "source_type": "Official English translation of 2026/27 admission call PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 21-page English translation names Business and Economics (CLaBE), code 6609, L-18, for AY 2026/27. It gives two regular SAT selection intakes plus a possible third, 177 regular places plus 13 special-programme places, a €20 non-refundable application fee, secondary-school eligibility and at least B2 English. The Italian call prevails for legal interpretation. Historical evidence only; it does not confirm the 2027/28 call or terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_admission", "program.previous_cycle_application_fee", "program.previous_cycle_seats"],
    },
    {
        "id": "SRC-UNIBO-CLABE-NOTICE-BOARD-2026",
        "university_id": "bologna", "title": "Business and Economics (CLaBE) – current notice board",
        "url": "https://corsi.unibo.it/1cycle/CLaBE/notice-board",
        "source_type": "Official degree programme notice board", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Checked 11 November 2026: the board's 2027/28 Overseas reference is a study-mobility call for current students, not a first-year CLaBE admission call. The admission page separately links only its expired 2026/27 call.",
        "supports": ["program.cycle_marker_scope", "program.mobility_not_admission"],
    },
    {
        "id": "SRC-UNIBO-CLEF-PROFILE-2026",
        "university_id": "bologna", "title": "Economics and Finance (CLEF) – official degree profile",
        "url": "https://corsi.unibo.it/1cycle/EconomicsFinance/overview",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. Confirms Economics and Finance is an international, entirely English-taught three-year Bologna bachelor's degree in class L-33, with restricted access and 130 places currently displayed. The profile says selection criteria and admissions are published yearly; its 130-place statement is not explicitly labelled 2027/28.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-UNIBO-CLEF-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Economics and Finance – 2026/27 admission notice",
        "url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clef/bando-clef-etac_a-a-2026-2027.pdf/@@download/file/Bando%20CLEF%20-ETAC_a.a.%202026-2027.pdf",
        "source_type": "Official programme admission notice", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The official 2026/27 call identifies CLEF as course code 6646, L-33 R, with 130 total places, two ordinary SAT selections, a possible extra selection, a €20 non-refundable application fee, upper-secondary eligibility, Digital SAT, and English B2. Historical evidence only; the current enrolment page links no 2027/28 intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_admission", "program.previous_cycle_seats", "program.previous_cycle_application_fee"],
    },
    {
        "id": "SRC-UNIBO-CLEF-ENROLMENT-2026",
        "university_id": "bologna", "title": "Economics and Finance (CLEF) – current enrolment and admissions page",
        "url": "https://corsi.unibo.it/1cycle/EconomicsFinance/how-to-enrol",
        "source_type": "Official degree programme admission page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The page links the expired 2026/27 Italian and English calls and an expired extra-selection notice, and shows current 2026 ISEE tuition instructions; it does not link or announce a 2027/28 new-entry call. The displayed 2027/28 references elsewhere on the page are not a new-entry call.",
        "supports": ["program.current_admission_route", "program.cycle_marker_scope", "program.tuition_context"],
    },
    {
        "id": "SRC-UNIBO-CLEF-NOTICE-BOARD-2026",
        "university_id": "bologna", "title": "Economics and Finance (CLEF) – current notice board",
        "url": "https://corsi.unibo.it/1cycle/EconomicsFinance/notice-board",
        "source_type": "Official degree programme notice board", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The board lists a 2027/28 Overseas study-mobility call for enrolled/current students; this is not a CLEF first-year admissions call.",
        "supports": ["program.cycle_marker_scope", "program.mobility_not_admission"],
    },
    {
        "id": "SRC-UNIBO-CLEF-EXTRA-INTAKE-2026",
        "university_id": "bologna", "title": "CLEF – 2026/27 extra-selection notice",
        "url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clef/notice-of-extra-selection-process_etac-clef-2026-2027.pdf/@@download/file/Notice%20of%20extra%20selection%20process_ETAC-CLEF%202026-2027.pdf",
        "source_type": "Official programme extra-selection notice PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The two-page notice, dated 2 September 2026, confirms an extra selection to fill remaining 2026/27 positions and identifies six CLEF places for Italian/EU/equivalent applicants and non-EU applicants abroad who compete in the EU quota. It does not itself give application opening or closing dates.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_seats"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-PROFILE-2026",
        "university_id": "bologna", "title": "Medicine and Surgery – English-taught single-cycle course profile",
        "url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery/overview",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. Identifies the Bologna English-taught six-year single-cycle LM-41 degree with national restricted access; the cycle-specific 2026/27 University catalogue lists 160 places.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.access"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-CATALOGUE-2026",
        "university_id": "bologna", "title": "Medicine and Surgery – 2026/27 University course catalogue entry (code 6264)",
        "url": "https://www.unibo.it/en/study/first-and-single-cycle-degree/programme/2026/6264",
        "source_type": "Official University of Bologna course catalogue", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The AY 2026/27 entry identifies course code 6264, six years, Bologna campus, English delivery, LM-41 R and national restricted access with 160 places.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_seats"],
    },
    {
        "id": "SRC-UNIBO-MED-IT-PROFILE-2026",
        "university_id": "bologna", "title": "Medicina e chirurgia – Italian-taught single-cycle course profile",
        "url": "https://corsi.unibo.it/magistralecu/MedicinaChirurgia",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The profile identifies Medicine and Surgery as an Italian-taught, six-year Bologna LM-41 national-access single-cycle degree; the 2026/27 catalogue entry lists course code 6733 and 435 places.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-MED-IT-CATALOGUE-2026",
        "university_id": "bologna", "title": "Medicina e chirurgia – 2026/27 University catalogue entry (code 6733)",
        "url": "https://www.unibo.it/it/studiare/lauree-e-lauree-magistrali-a-ciclo-unico/corso/2026/6733",
        "source_type": "Official University of Bologna course catalogue", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The 2026/27 catalogue identifies course 6733 as a six-year Bologna-campus Italian LM-41 R degree with national restricted access and 435 places.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_available_places"],
    },
    {
        "id": "SRC-UNIBO-MED-IT-OPEN-SEMESTER-2026",
        "university_id": "bologna", "title": "University of Bologna – 2026/27 open-semester registration, fees and exam guidance",
        "url": "https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/iscrizioni-al-semestre-aperto",
        "source_type": "Official University of Bologna open-semester guidance", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The 2026/27 page expressly scopes the open-semester route to Italian-language Medicine, Dentistry and Veterinary Medicine; it specifies Universitaly registration by 3 August 2026, Bologna Student Online registration by 6 August, the €250 flat contribution and the two national exam dates. It does not establish the 2027/28 procedure.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_application_route", "program.previous_cycle_application_fee", "program.previous_cycle_admissions_route_scope"],
    },
    {
        "id": "SRC-UNIBO-BBS-AI-MFG-2027",
        "university_id": "bologna", "title": "Global MBA in AI and Manufacturing – 2027/28 admissions schedule",
        "url": "https://www.bbs.unibo.it/en/global-mba/ai-and-manufacturing-2/",
        "source_type": "Official Bologna Business School programme page", "accessed_at": "2026-11-10", "cycle": "2027-2028",
        "evidence": "The official BBS page states applications for AY 2027/28 open in December 2026, selection begins February 2027, and the programme starts September 2027. It describes a 12-month full-time English-language Global MBA and identifies AI and Manufacturing as the track; it is not a standard two-year Laurea Magistrale.",
        "supports": ["program.availability", "program.name", "program.level", "program.language", "program.application_windows", "program.program_type"],
    },
    {
        "id": "SRC-UNIBO-BBS-GREEN-MGMT-2026",
        "university_id": "bologna", "title": "Business Management – Green Management and Sustainable Businesses – BBS course and current application information",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/business-management-green-management-and-sustainable-businesses/",
        "source_type": "Official Bologna Business School programme and application page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Identifies the exact track as Business Management – Green Management and Sustainable Businesses, within BBS's first-level Professional Master in Business Management, not a separate Laurea Magistrale. Current page facts: full-time on-campus, English, 12 months, 60 CFU/ECTS; BBS states 1,500 learning hours (360 lecture, 540 independent study, 600 internship) and collaboration with the University of Bologna Department of Management (DISA). Its current displayed calendar gives a last application date of 16 November 2026, selection on 18–19 November, enrollment by 1 December, crash courses from 9 December, and classes starting 7 January 2027, but does not label the academic-year cycle; these dates are not used as 2027/28 deadlines. The page displays a current €13,800 tuition, €60 selection fee, partial €3,000/€5,000 awards, Bachelor's degree and B2 English requirements, and aptitude/English tests plus interview. It contains no 2027/28 marker or call; these current facts are not promoted to the new cycle.",
        "supports": ["program.name", "program.level", "program.language", "program.program_type", "program.previous_cycle_application_windows", "program.current_published_calendar", "program.current_published_tuition", "program.current_published_scholarships", "program.current_published_requirements"],
    },
    {
        "id": "SRC-UNIBO-GESTIONALE-BSC-2026",
        "university_id": "bologna", "title": "Ingegneria gestionale – Bologna bachelor's profile",
        "url": "https://corsi.unibo.it/laurea/IngegneriaGestionale",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the Italian-taught Bologna bachelor's degree in Management Engineering, class L-9, with locally restricted admission and TOLC-I selection.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-ECON-COMMERCIO-2026",
        "university_id": "bologna", "title": "Economia e commercio – official degree profile at Forlì",
        "url": "https://corsi.unibo.it/laurea/EconomiaCommercio",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The course is a University of Bologna bachelor's degree taught at Forlì, not Bologna; the tracker campus needs correction. The current profile gives the course identity and location.",
        "supports": ["program.name", "program.level", "program.language", "program.location"],
    },
    {
        "id": "SRC-UNIBO-MED-IT-ENROL-2026",
        "university_id": "bologna", "title": "Medicina e chirurgia – Italian course admission procedure",
        "url": "https://corsi.unibo.it/magistralecu/MedicinaChirurgia/iscriversi-al-corso",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The current page describes the Italian course's 2026/27 open-semester route, admission qualification, language-related international steps, exam timing and national ranking; no new 2027/28 incoming-student call is posted.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_route", "program.cycle_marker_scope"],
    },
    {
        "id": "SRC-UNIBO-MED-IT-CALL-2026",
        "university_id": "bologna", "title": "Medicina e chirurgia – 2026/27 post-semester admission call (Bologna campus)",
        "url": "https://corsi.unibo.it/s/3317/p/it/iscriversi-al-corso-requisiti-tempi-e-modalita/bando-medicina-odontoiatria-veterinaria-2026-2027.pdf/@@download/file/Bando%20medicina%2C%20odontoiatria%2C%20veterinaria%202026-2027.pdf",
        "source_type": "Official University of Bologna post-semester admissions call PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 with a valid PDF signature on 11 November 2026. The 2026/27 call covers Medicine in Bologna, Forlì and Ravenna after the open semester. For Bologna it lists 425 Italian/EU/equivalent seats plus 10 non-EU-resident-abroad seats, specifies qualifying secondary credentials and B2 English, gives the December 2026 and January 2027 exams and 22 January ranking, and describes the national ranking and enrolment/credit-recovery procedures. These are historical cohort terms, not a 2027/28 call.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_available_places", "program.previous_cycle_admission_requirements", "program.previous_cycle_application_windows", "program.previous_cycle_test_scoring", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-MUR-ITALIAN-MED-OPEN-SEMESTER",
        "university_id": "bologna", "title": "MUR – national access rules for Italian-language Medicine",
        "url": "https://www.mur.gov.it/it/aree-tematiche/universita/lofferta-formativa-titoli-rilasciati/accesso-programmato-cose",
        "source_type": "Official Ministry of University and Research policy page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. MUR says the Italian-language LM-41, LM-46 and LM-42 courses have used the open-semester model from AY 2025/26, with free first-semester access followed by standardized exams and a national ranking; seats are determined annually. This national overview does not confirm a Bologna 2027/28 course intake or its terms.",
        "supports": ["program.previous_cycle_admissions_route_scope", "program.cycle_marker_scope"],
    },
    {
        "id": "SRC-UNIBO-LAW-2026",
        "university_id": "bologna", "title": "Giurisprudenza – Bologna single-cycle degree profile and 2026/27 regulation",
        "url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/esplora-il-corso",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The programme profile identifies the five-year Italian-taught Bologna Giurisprudenza single-cycle degree and states free access with TOLC-SU knowledge assessment; its details are cycle-scoped and do not confirm a 2027/28 first-year call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration"],
    },
    {
        "id": "SRC-UNIBO-LAW-CATALOGUE-2026",
        "university_id": "bologna", "title": "Giurisprudenza – 2026/27 University catalogue entry (code 6827)",
        "url": "https://www.unibo.it/it/studiare/lauree-e-lauree-magistrali-a-ciclo-unico/corso/2026/6827",
        "source_type": "Official University of Bologna course catalogue", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The AY 2026/27 entry identifies course code 6827, five years, Bologna campus, Italian delivery and class LMG/01 R; access is free with TOLC-SU.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_requirements"],
    },
    {
        "id": "SRC-UNIBO-LAW-ENROLMENT-2026",
        "university_id": "bologna", "title": "Giurisprudenza Bologna – current enrolment and TOLC-SU page",
        "url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/iscriversi-al-corso",
        "source_type": "Official degree programme admissions page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The course page lists the 2026/27 enrolment route and requirements, describes the TOLC-SU content, links the 2026/27 admission notice and displays 2026 ISEE tuition guidance. It contains no 2027/28 course call.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_application_route", "program.previous_cycle_test_scoring", "program.previous_cycle_tuition", "program.cycle_marker_scope"],
    },
    {
        "id": "SRC-UNIBO-LAW-OFA-2026",
        "university_id": "bologna", "title": "Giurisprudenza Bologna – TOLC-SU OFA and completion guidance",
        "url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/ofa",
        "source_type": "Official degree programme OFA page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. For the 2026/27 cycle, a TOLC-SU result below the call's 20/50 threshold assigns an OFA but does not bar enrolment; from 2026/27 the OFA is fulfilled through the Department alignment course and final assessment by 31 March 2028.",
        "supports": ["program.previous_cycle_test_scoring", "program.previous_cycle_additional_learning_requirement"],
    },
    {
        "id": "SRC-UNIBO-COMMUNICATION-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – Bologna bachelor's profile",
        "url": "https://corsi.unibo.it/laurea/ScienzeComunicazione",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The profile describes the Italian-taught Bologna three-year bachelor's degree in Communication Sciences, class L-20 R, with restricted admission; the current course material is labelled 2026/27 and does not announce 2027/28 intake.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-MSC-2026",
        "university_id": "bologna", "title": "Ingegneria informatica – Bologna MSc profile and admission page",
        "url": "https://corsi.unibo.it/magistrale/ingegneriainformatica/index.html",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. Confirms the Bologna LM-32 Master's with open access and two curricula, Ingegneria dei sistemi informatici and Ubiquitous Systems and Networks; the University lists Italian and English as languages overall. Current profile and study-plan markers are for 2026/27 and do not announce 2027/28 entry.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Ingegneria informatica – 2026/27 admission requirements",
        "url": "https://corsi.unibo.it/magistrale/ingegneriainformatica/iscriversi-al-corso",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. Provides the 2026/27 eligible degree classes and subject-credit routes, 165-CFU rule for current undergraduates, English B2 requirement, and links the current year's call and assessment guide; no 2027/28 notice is posted.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-CATALOGUE-2026",
        "university_id": "bologna", "title": "Ingegneria informatica – 2026/27 University course catalogue entry",
        "url": "https://www.unibo.it/it/studiare/lauree-magistrali/corso/2026/6719",
        "source_type": "Official University course catalogue entry", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The catalogue labels the entry 2026/27, course code 6719, Bologna, LM-32 Computer Engineering, Italian and English, and open access; it does not establish 2027/28 first-year admission.",
        "supports": ["program.previous_cycle_course_listing", "program.availability_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-CALL-2026",
        "university_id": "bologna", "title": "Engineering Master's programmes – 2026/27 admission notice (includes Ingegneria informatica)",
        "url": "https://corsi.unibo.it/s/3387/p/it/iscriversi-nuova-13/avviso-lm-a-libero-accesso-2025-26.pdf/@@download/file/Avviso%20ammissioni%202026-2027_nuovi%20intakes.pdf",
        "source_type": "Official University multi-course admission notice PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026 with a valid PDF signature (616,454 bytes). The 2026/27 notice expressly includes course 6719 and sets four dated application intakes, committee review of curricular and language eligibility and personal preparation, enrollment dates and ISEE-based tuition structure; these dates and requirements are historical only.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_windows", "program.previous_cycle_application_route", "program.previous_cycle_program_requirements", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-ACCESS-GUIDE-2026",
        "university_id": "bologna", "title": "Ingegneria informatica – official access and personal-preparation assessment guide",
        "url": "https://corsi.unibo.it/s/3387/p/it/iscriversi-nuova-13/informativa-sulle-modalita-di-accesso.pdf/@@download/file/INFORMATIVA%20SULLE%20MODALITA%20DI%20ACCESSO.pdf",
        "source_type": "Official course access and assessment guide PDF", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026 with a valid PDF signature (471,943 bytes). The 2026/27 admissions page currently links this guide; the PDF itself is not cycle-labelled. It specifies qualifying degree classes, subject-credit thresholds for other degrees, the personal-preparation assessment by final degree mark and subject credits, English B2, and a required pre-assessment workbook; confirm against the next cycle's call.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_personal_preparation"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-DOUBLE-DEGREE-2026",
        "university_id": "bologna", "title": "Ubiquitous Systems and Networks – 2026/27 double-degree selection call",
        "url": "https://corsi.unibo.it/s/3387/p/it/iscriversi-nuova-13/call-for-admission-to-join-the-double-degree-program.pdf/@@download/file/CALL%20FOR%20ADMISSION%20TO%20JOIN%20THE%20DOUBLE%20DEGREE%20PROGRAM.pdf",
        "source_type": "Official University double-degree selection call PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026 with a valid PDF signature (238,447 bytes). This separate call offers at most five double-degree places to students already admitted to course 6719 in the first or second 2026/27 intake; the successful students spend the second year at Université Côte d’Azur. It is a supplementary mobility selection, not the general course admission call or a 2027/28 intake notice.",
        "supports": ["program.previous_cycle_double_degree", "program.availability_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-BA-BBS-2026",
        "university_id": "bologna", "title": "Business Analytics and Data Science – BBS professional-master classification",
        "url": "https://www.bbs.unibo.it/en/professional-masters-programs/",
        "source_type": "Official Bologna Business School programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists Data Science & Business Analytics among BBS professional masters (one-year programmes); confirms the legacy name is not a separate Bologna Laurea Magistrale. The university degree course with a similar Business Analytics label is a curriculum under Statistics, Economics and Business.",
        "supports": ["program.program_type", "program.corrected_identity"],
    },
    {
        "id": "SRC-UNIBO-GIURISPRUDENZA-REG-2026",
        "university_id": "bologna", "title": "Giurisprudenza – 2026/27 Bologna degree regulation",
        "url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/il-corso/all-e-regolamento-parte-normativa-26-27.pdf",
        "source_type": "Official programme regulation PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 with a valid PDF signature on 11 November 2026. The regulation names the Bologna single-cycle course code 6827, LMG/01 R, Italian delivery and free access with TOLC knowledge verification for students enrolling in AY 2026/27; failed verification leads to an OFA.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_requirements", "program.previous_cycle_additional_learning_requirement"],
    },
    {
        "id": "SRC-UNIBO-LAW-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Giurisprudenza – 2026/27 admission notice and TOLC-SU deadlines",
        "url": "https://corsi.unibo.it/s/3394/p/it/iscriversi-nuova-4/avviso-tolc-25-26.pdf/@@download/file/AVVISO%20IMMA%2026_27.pdf",
        "source_type": "Official University of Bologna admissions notice PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 with a valid PDF signature on 11 November 2026. The notice explicitly lists Bologna Giurisprudenza code 6827, required TOLC-SU, free-access enrollment periods (22 July–24 September without late fee; 25 September–24 October with €30 late fee; 25 October–19 November with €150 late fee), foreign qualification and international-student procedures, and an OFA threshold below 20/50. TOLC test registration is paid to CISIA; the notice does not state the test fee amount. These terms are for AY 2026/27 only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_application_route", "program.previous_cycle_admission_requirements", "program.previous_cycle_test_scoring", "program.previous_cycle_application_fee"],
    },
    {
        "id": "SRC-UNIBO-AI-MFG-2026-27-MASTER",
        "university_id": "bologna", "title": "AI and Manufacturing – Global MBA official course entry",
        "url": "https://www.unibo.it/en/study/phd-professional-masters-specialisation-schools-and-other-programmes/professional-master/2026-2027/global-master-in-business-administration-4",
        "source_type": "Official University of Bologna professional-master course entry", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Classifies Global Master in Business Administration as a first-level professional master's programme, organised with BBS, and lists AI and Manufacturing as one of its concentrations.",
        "supports": ["program.program_type", "program.previous_cycle_course_listing"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-2026-CALL",
        "university_id": "bologna", "title": "Medicine and Surgery – English course admission information",
        "url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery",
        "source_type": "Official degree programme landing page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. Identifies the Bologna English-taught LM-41 programme and national restricted access; the separate current enrolment page links only expired 2026/27 call documents and no 2027/28 call.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-ENROLMENT-2026",
        "university_id": "bologna", "title": "Medicine and Surgery – English programme current enrolment page",
        "url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery/how-to-enrol",
        "source_type": "Official degree programme admission page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The page identifies the posted admissions material as 2026/27 and links the expired IMAT call. It contains no 2027/28 English-entry call.",
        "supports": ["program.current_admission_route", "program.cycle_marker_scope", "program.mobility_not_admission"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-IT-CALL-2026",
        "university_id": "bologna", "title": "Medicine and Surgery in English – 2026/27 official Italian admission call",
        "url": "https://corsi.unibo.it/s/3317/p/en/enrolling-1/bando-medicine-and-surgery-2024-2025-1.pdf/@@download/file/BANDO%20MEDICINE%20AND%20SURGERY%20%2B%20VETERINARY%20MEDICINE%202026-2027.pdf",
        "source_type": "Official 2026/27 admission call PDF (Italian original)", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The Italian call governs the 2026/27 IMAT procedure: test registration on Universitaly 26 August–9 September 2026, test on 29 September, 140 places in the EU/equivalent national quota and 20 in the non-EU-resident-abroad local quota, with the stated exam scoring and eligibility rules. It does not establish 2027/28 admission.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_admission", "program.previous_cycle_seats", "program.previous_cycle_gpa_requirement", "program.previous_cycle_application_fee"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-CALL-SUMMARY-2026",
        "university_id": "bologna", "title": "Medicine and Surgery in English – 2026/27 call English summary",
        "url": "https://corsi.unibo.it/s/3317/p/en/enrolling-1/abstract-2024-2025-3.pdf/@@download/file/ABSTRACT%202026-2027%20%283%29.pdf",
        "source_type": "Official English-language summary of 2026/27 admission call", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The official English summary makes 2026/27 IMAT rules readable, but explicitly says the Italian call prevails in legal controversies. Used as a navigation aid only; cite the Italian original for legal terms.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_application_route", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-LANGUAGE-ANNEX-2026",
        "university_id": "bologna", "title": "Medicine and Surgery – 2026/27 call English-certificate list",
        "url": "https://corsi.unibo.it/s/3317/p/en/enrolling-1/allegato-2-certificazioni-linguistiche.pdf/@@download/file/Allegato%202%20-%20Certificazioni%20linguistiche.pdf",
        "source_type": "Official attached English-language certificate table PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The attachment lists accepted B2-or-higher English certificates, including IELTS 5.5–6.5, TOEFL 87–109, Cambridge First (FCE) and Trinity ISE II; the 2026/27 call says a year of English-medium schooling is automatically treated as certificate possession. The call makes certificate possession optional in registration and uses it as a tie-breaker; it is not stated as a universal prerequisite for sitting IMAT.",
        "supports": ["program.previous_cycle_english_requirement", "program.previous_cycle_language_certificate_options"],
    },
    {
        "id": "SRC-MUR-IMAT-2026-DECREE",
        "university_id": "bologna", "title": "MUR – 2026/27 decree for English-language Medicine and IMAT (DM 1005/2026)",
        "url": "https://www.mur.gov.it/it/atti-e-normativa/decreto-ministeriale-n-1005-del-06-08-2026",
        "source_type": "Official Ministry of University and Research decree page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. MUR identifies DM 1005 of 6 August 2026 as the 2026/27 ministerial decree governing admission to English-language Medicine courses, including IMAT format and available places. It is annual evidence only and does not establish 2027/28 rules.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_windows", "program.cycle_marker_scope"],
    },
    {
        "id": "SRC-UNIBO-MED-OPEN-SEMESTER-2026",
        "university_id": "bologna", "title": "University of Bologna – 2026/27 open-semester procedures for Italian-language Medicine",
        "url": "https://www.unibo.it/en/study/enrolment-fees-and-other-procedures/enrolment-in-combined-bachelors-and-masters-degree-programmes-in-medicine-and-surgery-dentistry-and-orthodontics%2C-veterinary-medicine",
        "source_type": "Official University open-semester guidance", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The page expressly scopes the 2026/27 open-semester route to Italian-taught Medicine, Dentistry and Veterinary Medicine. The English-taught Medicine course is governed by its separate 2026/27 IMAT call; this distinction does not determine the unannounced 2027/28 procedure.",
        "supports": ["program.cycle_marker_scope", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIBO-TUITION-PAGE-2026",
        "university_id": "bologna", "title": "University of Bologna – 2026/27 tuition framework and exemptions",
        "url": "https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/tasse-e-contributi",
        "source_type": "Official University tuition and exemption page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The 2026/27 fee framework states a fixed €157.04 amount plus an ISEE-dependent course contribution, and points students in restricted-entry courses to their course call for due dates. The separate open-semester fees on the page apply to Italian-taught medicine courses, not this English-taught IMAT programme.",
        "supports": ["program.previous_cycle_tuition", "program.tuition_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-TUITION-TABLE-2026",
        "university_id": "bologna", "title": "University of Bologna – 2026/27 maximum course tuition table",
        "url": "https://www.unibo.it/it/allegati/Tabellaimportimassimi2627.pdf/@@download/file/Tabella%20importi%20massimi%202026-2027.pdf",
        "source_type": "Official University fee schedule PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The official table lists 2026/27 programme code 6264 Medicine and Surgery with a maximum comprehensive contribution of €3,315, excluding regional study tax, stamp duty and insurance; the fixed €157.04 fee is specified on the linked fee framework page.",
        "supports": ["program.previous_cycle_tuition", "program.tuition_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-ECONOMIA-COMMERCIO-LOCATION-2026",
        "university_id": "bologna", "title": "Economia e commercio – official Forlì campus course page",
        "url": "https://corsi.unibo.it/laurea/EconomiaCommercio/sedute-di-laurea",
        "source_type": "Official degree-course page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The official course page identifies Economia e commercio as a University of Bologna degree based at Forlì, not Bologna.",
        "supports": ["program.location", "program.corrected_identity"],
    },
    {
        "id": "SRC-UNIBO-REGULAR-COURSES-2026",
        "university_id": "bologna", "title": "University of Bologna regular degree course catalogue",
        "url": "https://corsi.unibo.it/",
        "source_type": "Official degree programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official course-system root used to distinguish Laurea and Laurea Magistrale degree courses from professional masters delivered in cooperation with BBS.",
        "supports": ["program.program_type", "program.corrected_identity"],
    },
    {
        "id": "SRC-UNIBO-CLABE-PROGRAM-CODE-2026",
        "university_id": "bologna", "title": "Business and Economics – official course code and programme profile",
        "url": "https://corsi.unibo.it/1cycle/CLaBE/prospects",
        "source_type": "Official degree programme page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Checked 11 November 2026: identifies the active Business and Economics degree (CLaBE), tells prospective students to use code 6609, and distinguishes the code assigned after enrolment; verifies course identity without confirming 2027/28 entry.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing"],
    },
    {
        "id": "SRC-UNIBO-DHDK-CALL-2026",
        "university_id": "bologna", "title": "Digital Humanities and Digital Knowledge – AY 2026/27 admission call",
        "url": "https://corsi.unibo.it/s/3391/p/en/digital-humanities-and-digital-knowledge-dhdk/call-dhdk-2026.pdf/@@download/file/Call%20DHDK%202026.pdf",
        "source_type": "Official programme admission notice PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 24-page notice explicitly names the degree for AY 2026/27. It specifies three expired application rounds, an online interview, curricular-credit and English B2 requirements, and the 2026/27 tuition structure; it is historical evidence only and does not establish 2027/28 availability or terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIBO-COMM-ADMISSION-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – 2026/27 admissions page",
        "url": "https://corsi.unibo.it/laurea/ScienzeComunicazione/iscriversi-al-corso",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The 2026/27 page describes the TOLC-SU format, 20 EUR application contribution, and links the expired annual call and extraordinary-selection notice; it does not announce 2027/28 terms.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_route", "program.previous_cycle_test_scoring"],
    },
    {
        "id": "SRC-UNIBO-COMM-CATALOGUE-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – 2026/27 University course catalogue entry",
        "url": "https://www.unibo.it/it/studiare/lauree-e-lauree-magistrali-a-ciclo-unico/corso/2026/6620",
        "source_type": "Official University course catalogue entry", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026. The catalogue labels the entry 2026/27, course code 6620, three years, Bologna, Italian, class L-20 R, local restricted access by TOLC-SU, with 600 places; it does not establish a 2027/28 intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_places", "program.availability_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-COMM-CALL-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – 2026/27 admission call",
        "url": "https://corsi.unibo.it/s/3391/p/it/iscriversi-11/bando-scienze-della-comunicazione-a-a-2025-2026.pdf/@@download/file/BANDO%20SCIENZE%20DELLA%20COMUNICAZIONE%2026_27%20firmato.pdf",
        "source_type": "Official programme admission notice PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026 with a valid PDF signature (1,062,159 bytes). The 45-page 2026/27 call sets two ordinary TOLC-SU selections, their dated deadlines and ranking rules, a 26/50 first-round eligibility threshold, no minimum score in later rounds, a 20 EUR University selection contribution, OFA rules, and course tuition framework; these are historical terms only.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_windows", "program.previous_cycle_places", "program.previous_cycle_test_scoring", "program.previous_cycle_program_requirements", "program.previous_cycle_application_fee", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-UNIBO-COMM-EXTRA-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – 2026/27 extraordinary selection notice",
        "url": "https://corsi.unibo.it/s/3391/p/it/iscriversi-11/avviso-selezione-straordinaria-scienze-della-comunicazione-1.pdf/@@download/file/Avviso%20selezione%20straordinaria%20SCIENZE%20DELLA%20COMUNICAZIONE.pdf",
        "source_type": "Official programme extraordinary-selection notice PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Fresh no-cache GET returned HTTP 200 on 11 November 2026 with a valid PDF signature (352,704 bytes). The notice explicitly applies to AY 2026/27 and lists 156 remaining places for course 6620 after ordinary selections; it refers back to the 2026/27 call for dates and selection rules and is not evidence of a 2027/28 intake.",
        "supports": ["program.previous_cycle_places", "program.previous_cycle_application_windows", "program.availability_2027_2028"],
    },
    {
        "id": "SRC-UNIBO-LAW-COURSE-2026",
        "university_id": "bologna", "title": "Giurisprudenza – 2026/27 programme regulation",
        "url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/il-corso/all-e-regolamento-parte-normativa-26-27.pdf",
        "source_type": "Official programme regulation", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official regulation identifies a five-year single-cycle law degree (LMG/01 R), demonstrating the legacy MSc classification is incorrect.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing"],
    },
    {
        "id": "SRC-PADOVA-ENGLISH-MSC-CATALOGUE-2026",
        "university_id": "padova", "title": "Padua official English-taught Master's programme catalogue",
        "url": "https://www.unipd.it/en/corsi-laurea-magistrale-lingua-inglese",
        "source_type": "Official programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official catalogue lists the active English-taught Master's programmes and identifies which entries are standalone degrees versus English-taught curricula of Italian-language degrees. It also labels proposed 2027/28 programmes as pending approval.",
        "supports": ["program.previous_cycle_course_listing", "program.program_type"],
    },
    {
        "id": "SRC-PADOVA-ENG-MSC-ADMISSIONS-2026",
        "university_id": "padova", "title": "School of Engineering Master's admission inventory – AY 2026/27",
        "url": "https://www.unipd.it/en/ammissioni-ing-magistrali",
        "source_type": "Official programme admission inventory", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the School of Engineering's English-taught 2026/27 Master's degrees, including Aerospace Engineering, Computer Engineering, and the English-taught Management Engineering track. The page distinguishes Italian-degree and international-qualification procedures.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-PADOVA-COMPUTER-ENGINEERING-2026",
        "university_id": "padova", "title": "Computer Engineering – official English-taught degree listing",
        "url": "https://www.unipd.it/en/corsi-laurea-magistrale-lingua-inglese",
        "source_type": "Official degree programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The official English-MSc catalogue lists Computer Engineering under the School of Engineering; annual admission page lists it in the 2026/27 offer. A separate 2027/28 intake call was not verified.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-PADOVA-COMPUTER-SCIENCE-2026",
        "university_id": "padova", "title": "Computer Science – official School of Science catalogue",
        "url": "https://www.scienze.unipd.it/en/courses/how-to-apply/",
        "source_type": "Official School of Science degree and admission catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the English-taught Computer Science Master's course and its School application route; the page's deadline is for the then-current cycle and is not copied to 2027/28.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-PADOVA-CYBERSECURITY-2026",
        "university_id": "padova", "title": "Cybersecurity – official 2026/27 Master's course and admissions page",
        "url": "https://cybersecurity.math.unipd.it/study-plan/",
        "source_type": "Official interdepartmental degree programme page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the English-taught two-year Cybersecurity Master's, admission requirements, access route and non-EU places for 2026/27; no 2027/28 call is shown.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_application_windows"],
    },
    {
        "id": "SRC-PADOVA-DATA-SCIENCE-2026",
        "university_id": "padova", "title": "Data Science – official degree profile and 2026/27 admission page",
        "url": "https://datascience.math.unipd.it/admission/",
        "source_type": "Official degree programme and admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Names the Master's in Data Science, describes 2026/27 entry thresholds and international selection, B2 English, and a 50-place cap for non-EU applicants residing abroad. These are historical, not 2027/28 facts.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_seats"],
    },
    {
        "id": "SRC-PADOVA-AEROSPACE-MSC-2026",
        "university_id": "padova", "title": "Aerospace Engineering – official Master's programme profile",
        "url": "https://academics.dii.unipd.it/aerospaceengineering/msc-degree-in-aerospace-engineering/",
        "source_type": "Official department degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the two-year Aerospace Engineering MSc with aeronautics and space curricula; School of Engineering admission inventory lists it among English courses for 2026/27.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_curricula"],
    },
    {
        "id": "SRC-PADOVA-INFORMATION-ENGINEERING-BSC-2026",
        "university_id": "padova", "title": "Information Engineering – official degree profile",
        "url": "https://www.unipd.it/en/corsi-di-laurea/information-engineering",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the three-year English-taught BSc in Padua, class L-8 R, with limited admission; the 2026/27 admission page supplies annual selection information.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-PSYCHOLOGICAL-SCIENCE-BSC-2026",
        "university_id": "padova", "title": "Psychological Science – current Padua English BSc profile",
        "url": "https://www.unipd.it/corsi-di-laurea/psychological-science",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The current official profile identifies the English-taught three-year BSc in Psychological Science, class L-24 R, in Padua with restricted admission. It is the current English programme corresponding to the legacy English-language lead, not proof of a 2027/28 call.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-PADOVA-MEDICINE-2026",
        "university_id": "padova", "title": "Medicine and Surgery – current English single-cycle degree admissions guide",
        "url": "https://www.unipd.it/en/studiare-inglese-come-fare-domanda",
        "source_type": "Official international admissions guide", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Confirms Medicine and Surgery is a limited-access English-taught single-cycle degree with annual places and IMAT/Universitaly process set by ministerial call; the legacy bachelor's label is not the Italian degree level.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-PADOVA-PSYCHOLOGY-MSC-2026",
        "university_id": "padova", "title": "Padua Italian-taught psychology Master's admissions catalogue – AY 2026/27",
        "url": "https://www.unipd.it/ammissioni-psi-magistrali-linguaitaliana",
        "source_type": "Official School of Psychology admission catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the 2026/27 Italian-taught Master's programs including Clinical Psychology and Developmental and Educational Psychology and links the annual admission call; no 2027/28 selection was confirmed.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-PADOVA-CLINICAL-PSYCHOLOGY-2026",
        "university_id": "padova", "title": "Psicologia clinica – official current degree profile",
        "url": "https://www.unipd.it/corsi-di-laurea/psicologia-clinica",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the two-year Italian-taught MSc in Clinical Psychology (LM-51 R), Padua, restricted admission.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-PSYCHOLOGY-CALL-2026",
        "university_id": "padova", "title": "Italian-taught Psychology Master's admission call – AY 2026/27",
        "url": "https://wwwassets.unipd.it/sites/default/files/2026-07/2026_Bando_LM_PsicologiaItaliano.pdf",
        "source_type": "Official University of Padua admission call PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 2026/27 call covers Psicologia clinica and gives its EU/equivalent quota, separate quota for non-EU applicants residing abroad, eligibility requirements, curricular and English-language thresholds, ranking formula, application charge, Uniweb dates and enrollment schedule. Historical evidence only; it does not establish 2027/28 terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_available_places", "program.previous_cycle_admission_requirements", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_entrance_test", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026",
        "university_id": "padova", "title": "Italian-taught Psychology Master's call for non-EU applicants abroad – AY 2026/27",
        "url": "https://wwwassets.unipd.it/sites/default/files/pdf_imported_files/nonUE_LM%20Psicologia_0.pdf",
        "source_type": "Official Global Engagement Office admission call PDF", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The separate 2026/27 international call assigns Psicologia clinica 9 places, including 2 Marco Polo places, and states the 7 January–7 March application window, €60 non-refundable pre-enrolment contribution, qualification, language and subject-background requirements and selection process. Historical evidence only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_available_places", "program.previous_cycle_admission_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_italian_requirement", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee"],
    },
    {
        "id": "SRC-PADOVA-REGIONAL-SCHOLARSHIP-2026",
        "university_id": "padova", "title": "Regional scholarship eligibility and 2026/27 call page",
        "url": "https://www.unipd.it/servizi/supporto-studio/borse-premi-studio/borse-studio-alloggi-sussidi-straordinari",
        "source_type": "Official University of Padua regional student-aid page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 2026/27 regional scholarship call is open to eligible Laurea Magistrale students and is competitive, with economic and merit requirements, ISEE/ISPE limits and a 30 September 2026 application step. The reviewed page links the 2026/27 call only; no 2027/28 award or deadline is established.",
        "supports": ["program.previous_cycle_scholarships", "program.scholarships_2027_2028"],
    },
    {
        "id": "SRC-PADOVA-DEVELOPMENTAL-PSYCHOLOGY-2026",
        "university_id": "padova", "title": "Psicologia dello sviluppo e dell'educazione – official current degree profile",
        "url": "https://psicologia.unipd.it/offerta-didattica/lauree-magistrali?key=PS2975&ordinamento=2025&tipo=LM",
        "source_type": "Official School of Psychology degree profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the two-year Italian-taught MSc in Developmental and Educational Psychology (LM-51 R) in Padua with restricted admission; the displayed page includes place counts, subject to annual call confirmation.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-MANAGEMENT-ENGINEERING-2026",
        "university_id": "padova", "title": "Ingegneria gestionale – official Master's course profile",
        "url": "https://www.unipd.it/corsi-di-laurea-magistrali/ingegneria-gestionale",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the two-year MSc in Management Engineering at Vicenza and lists Italian and English teaching; the official School of Engineering 2026/27 access page calls Management Engineering an English-taught study track. The legacy Padua campus and English-only label require correction to track/campus scope.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_location"],
    },
    {
        "id": "SRC-PADOVA-AGRICULTURAL-SCIENCES-2026",
        "university_id": "padova", "title": "Scienze e tecnologie agrarie – official programme profile",
        "url": "https://www.unipd.it/de/node/79184",
        "source_type": "Official degree programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The official 2026/27 Master's admission inventory lists Scienze e tecnologie agrarie among Italian-taught open-access-with-requirements MSc programmes at the School of Agriculture and Veterinary Medicine; it distinguishes English-taught Sustainable Agriculture as a separate degree.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-PADOVA-MOLECULAR-BIOLOGY-BSC-2026",
        "university_id": "padova", "title": "Biologia Molecolare – official bachelor's degree profile",
        "url": "https://biologia-molecolare.biologia.unipd.it/index.php?id=170",
        "source_type": "Official Department of Biology degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies Biologia Molecolare as a three-year first-cycle degree, class L-13, with restricted admission. A distinct second-cycle Molecular Biology programme also exists, so level must be matched to this Italian-titled legacy candidate.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-COMPUTER-ENGINEERING-BSC-2026",
        "university_id": "padova", "title": "Ingegneria informatica – official bachelor's degree profile",
        "url": "https://www.unipd.it/corsi-di-laurea/ingegneria-informatica",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the three-year Italian-taught Padua bachelor's in Computer Engineering, class L-8 R, with programmed admission.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-COGNITIVE-PSYCHOLOGY-BSC-2026",
        "university_id": "padova", "title": "Scienze psicologiche cognitive e psicobiologiche – official bachelor's profile",
        "url": "https://www.unipd.it/corsi-di-laurea/scienze-psicologiche-cognitive-e-psicobiologiche",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the three-year Italian-taught bachelor's in Scienze psicologiche cognitive e psicobiologiche, class L-24 R, at Padua with restricted admission.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-PSYCHOLOGY-MSC-FULL-2026",
        "university_id": "padova", "title": "School of Psychology Master's programmes – active official catalogue",
        "url": "https://www.psicologia.unipd.it/offerta-didattica/corsi-di-laurea-magistrale?tipo=LM",
        "source_type": "Official School of Psychology programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The School catalogue lists active Master's programmes and states the academic year of the displayed offer; use programme-specific pages and annual calls for exact entry criteria.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-PADOVA-AGRARIAN-MSC-COURSES-2026",
        "university_id": "padova", "title": "School of Agriculture and Veterinary Medicine active Master's courses – AY 2026/27",
        "url": "https://www.agrariamedicinaveterinaria.unipd.it/corsi/corsi-di-laurea-magistrale",
        "source_type": "Official School of Agriculture degree inventory", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists Scienze e tecnologie agrarie among the active 2026/27 Master's degrees, alongside Sustainable Agriculture as a distinct English-taught course.",
        "supports": ["program.previous_cycle_course_listing", "program.program_type"],
    },
    {
        "id": "SRC-PADOVA-MANAGEMENT-ENGINEERING-COURSE-2026",
        "university_id": "padova", "title": "Ingegneria gestionale – official course profile and campus",
        "url": "https://www.unipd.it/corsi-di-laurea-magistrali/ingegneria-gestionale",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the two-year MSc in Vicenza with Italian and English teaching; the School of Engineering inventory identifies Management Engineering as an English-taught study track within the degree.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_location", "program.previous_cycle_language", "program.program_type"],
    },
    {
        "id": "SRC-PADOVA-MOLECULAR-BIOLOGY-BSC-ADMISSION-2026",
        "university_id": "padova", "title": "Biologia Molecolare – 2026/27 School of Science bachelor's admissions",
        "url": "https://www.scienze.unipd.it/come-iscriversi-l-2627/",
        "source_type": "Official School of Science admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists Biologia Molecolare among 2026/27 restricted-entry bachelor's courses and describes the TOLC-based annual selection process.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-PADOVA-SCIENCE-MSC-2026",
        "university_id": "padova", "title": "School of Science English Master's admission catalogue – AY 2026/27",
        "url": "https://www.scienze.unipd.it/en/courses/english-language/master-degree/2627/",
        "source_type": "Official School of Science admission catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official School page explicitly labels academic year 2026/27 and includes current programme details for Computer Science and related English Master's courses. This is not confirmation of 2027/28 first-year intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIPI-MSC-CATALOGUE-2026",
        "university_id": "pisa", "title": "University of Pisa official Master's degree catalogue",
        "url": "https://www.unipi.it/didattica/corsi/lauree-magistrali/",
        "source_type": "Official degree programme catalogue", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official catalogue includes course-level summaries and current access/language information for Pisa Master's degrees; individual course facts must be read from their own profile and admission sources.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.program_type"],
    },
    {
        "id": "SRC-UNIPI-CYBERSECURITY-2026",
        "university_id": "pisa", "title": "Cybersecurity – official two-year English MSc admission page",
        "url": "https://cysec.unipi.it/?page_id=253",
        "source_type": "Official degree programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Explicitly distinguishes the English two-year Laurea Magistrale in Cybersecurity from a separate one-year professional Master in Cybersecurity; reviewed for the programme admission route and international applicant guidance.",
        "supports": ["program.corrected_identity", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIPI-AIDE-2026",
        "university_id": "pisa", "title": "Artificial Intelligence and Data Engineering – official English programme profile",
        "url": "https://computer.ing.unipi.it/en/masters-degree-in-artificial-intelligence-and-data-engineering/",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the LM-32 MSc, with required courses taught in English and free-choice units in English or Italian; Italian is not needed to complete the degree. Profile does not publish 2027/28 call dates.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_level"],
    },
    {
        "id": "SRC-UNIPI-BIONICS-2026",
        "university_id": "pisa", "title": "Bionics Engineering – official Pisa Master's profile",
        "url": "https://www.unipi.it/didattica/corsi/lauree-magistrali/bionics-engineering-wber-lm/",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists Bionics Engineering as a two-year LM-21 R programme in Pisa, English language, locally restricted access, with Neural Engineering and Biorobotics curricula.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access", "program.previous_cycle_curricula"],
    },
    {
        "id": "SRC-UNIPI-NUCLEAR-2026",
        "university_id": "pisa", "title": "Nuclear Engineering – official course identity in Pisa degree documentation",
        "url": "https://nucleare.ing.unipi.it/images/files/SUA_2023.pdf",
        "source_type": "Official programme self-assessment document", "accessed_at": "2026-11-10", "cycle": "2023-2024",
        "evidence": "Identifies Nuclear Engineering as an English-taught LM-30 MSc in the Pisa School of Engineering. This is historical course identity evidence only; current activation and 2027/28 entry remain unverified.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-UNINA-COMPUTER-SCIENCE-2025",
        "university_id": "napoli-federico-ii", "title": "Computer Science – official programme overview",
        "url": "https://informatica.dieti.unina.it/index.php/en/degree-programs/degree-programs-overview",
        "source_type": "Official Department of Information Technology degree catalogue", "accessed_at": "2026-11-10", "cycle": "2025-2026",
        "evidence": "The Department page, last updated 22 October 2025, identifies a two-year MSc in Computer Science and states that lectures are mostly in Italian. The historical tracker label 'English' is inaccurate; this evidence is for course identity/language only and no 2027/28 offer is established.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-UNINA-DATA-SCIENCE-GUIDE-2026",
        "university_id": "napoli-federico-ii", "title": "Data Science – 2026/27 official student guide",
        "url": "https://www.orientamento.unina.it/corsidistudio/data-science-eng/",
        "source_type": "Official University orientation and degree profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The guide states it is updated 2026/27 and identifies a two-year English-taught Master's in Data Science (LM-DATA/LM-91) in Naples. It does not establish 2027/28 first-year admission.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-UNINA-DATA-SCIENCE-ADMISSIONS-2026",
        "university_id": "napoli-federico-ii", "title": "Data Science – official admission requirements",
        "url": "https://data-science.dieti.unina.it/index.php/studying-with-us/information-to-apply",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "States curricular requirements (bachelor's in a scientific/economic discipline and at least 30 CFU in relevant areas, including computing) and English B2. These are current page requirements and must be reconfirmed against a 2027/28 notice.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement"],
    },
    {
        "id": "SRC-UNINA-MOVE-2026",
        "university_id": "napoli-federico-ii", "title": "Autonomous Vehicle Engineering (MOVE) – 2026/27 course and admissions page",
        "url": "https://move.dii.unina.it/",
        "source_type": "Official degree programme and admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Names the Master's Degree in Autonomous Vehicle Engineering and explicitly identifies the 2026/27 international application deadline as 15 June 2026 via Universitaly. It is prior-cycle evidence and not a 2027/28 deadline.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNINA-MOVE-PROFILE-2025",
        "university_id": "napoli-federico-ii", "title": "Autonomous Vehicle Engineering – official programme brochure",
        "url": "https://www.dii.unina.it/source/brochures-cds/magistrale/MOVE_eng.pdf",
        "source_type": "Official Department of Industrial Engineering programme brochure", "accessed_at": "2026-11-10", "cycle": "2020-2021",
        "evidence": "Identifies MOVE as a Laurea Magistrale/Master of Science and explains the autonomous systems engineering subject; this brochure is dated July 2020 and used for historical course identity only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.program_type"],
    },
    {
        "id": "SRC-UNINA-INDUSTRIAL-BIOENGINEERING-2026",
        "university_id": "napoli-federico-ii", "title": "Industrial Bioengineering – 2026/27 official student guide",
        "url": "https://www.orientamento.unina.it/corsidistudio/industrial-bio-engineering/",
        "source_type": "Official University orientation and degree profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The guide is updated 2026/27 and identifies the two-year LM-21 MSc as taught in English, at the Department of Chemical, Materials and Production Engineering in Naples; it gives B2 English and admission assessment context.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement"],
    },
    {
        "id": "SRC-UNINA-ECONOMICS-FINANCE-2026",
        "university_id": "napoli-federico-ii", "title": "Economics and Finance (LMEF) – official English Master's profile",
        "url": "https://www.orientamento.unina.it/corsidistudio/economics-and-finance-eng/",
        "source_type": "Official University orientation and degree profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies Economics and Finance (LMEF) as a two-year English-taught Master's in Naples, class LM-56. It distinguishes the degree programme from separate post-graduate University Master courses also called Economics and Finance.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-UNINA-ECONOMICS-FINANCE-DEPT-2026",
        "university_id": "napoli-federico-ii", "title": "Economics and Finance – Department of Economics and Statistics degree list",
        "url": "https://www.dises.unina.it/en_GB/il-dipartimento/presentazione",
        "source_type": "Official Department degree inventory", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the English Master's Degree in Economics and Finance (LMEF) separately from Economics and Finance postgraduate university Master's programmes.",
        "supports": ["program.corrected_identity", "program.program_type"],
    },
    {
        "id": "SRC-UNINA-INTERNATIONAL-RELATIONS-2026",
        "university_id": "napoli-federico-ii", "title": "International Relations (English) – official degree guide",
        "url": "https://www.orientamento.unina.it/corsidistudio/international-relations-eng/",
        "source_type": "Official University orientation and degree profile", "accessed_at": "2026-11-10", "cycle": "2024-2025",
        "evidence": "Identifies a two-year English-taught MSc in International Relations (LM-52) in Naples, with B2 English and social-sciences background requirements. The course page's detailed study-plan years are 2024/25, so current entry rules and 2027/28 availability remain unconfirmed.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_program_requirements"],
    },
    {
        "id": "SRC-UNINA-QUANTUM-2025",
        "university_id": "napoli-federico-ii", "title": "Quantum Science and Engineering – official course guide",
        "url": "https://www.orientamento.unina.it/corsidistudio/quantum-science-and-engineering/",
        "source_type": "Official University orientation and degree profile", "accessed_at": "2026-11-10", "cycle": "2025-2026",
        "evidence": "The guide identifies QS&E as a two-year English-taught Master's, LM-44, with open admission and subject-credit requirements plus B2 English. The page says its current guide is for 2025/26; this does not establish 2026/27 or 2027/28 new-entry availability.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_program_requirements"],
    },
    {
        "id": "SRC-UNINA-QUANTUM-PROFILE-2025",
        "university_id": "napoli-federico-ii", "title": "Quantum Science and Engineering – official programme and course links",
        "url": "https://www.qst.unina.it/index.php/education/",
        "source_type": "Official University project and programme page", "accessed_at": "2026-11-10", "cycle": "general",
        "evidence": "Names the Master Degree in Quantum Science and Engineering and links to the official Physics and course websites. This verifies programme identity, not its 2027/28 intake.",
        "supports": ["program.previous_cycle_course_listing", "program.program_type"],
    },
    {
        "id": "SRC-UNINA-ARCH-HERITAGE-2025",
        "university_id": "napoli-federico-ii", "title": "Architecture and Heritage – official course catalogue and admission rules",
        "url": "https://www.corsi.unina.it/DB2/home",
        "source_type": "Official degree programme catalogue", "accessed_at": "2026-11-10", "cycle": "2024-2025",
        "evidence": "The official course catalogue identifies Architecture and Heritage as an English-named course; the Department of Architecture regulation describes an English-taught LM-4 Master's and lists relevant curricular entry requirements. No 2027/28 intake notice was found.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_program_requirements"],
    },
    {
        "id": "SRC-UNINA-ARCH-HERITAGE-REG-2024",
        "university_id": "napoli-federico-ii", "title": "Architecture and Heritage – official didactic regulation",
        "url": "https://www.diarc.archer.unina.it/images/ARCHER_2024-25_DidacticRegulations_CdS_ENGL_2023_SA_DM96_v6.pdf",
        "source_type": "Official programme regulation PDF", "accessed_at": "2026-11-10", "cycle": "2024-2025",
        "evidence": "Regulation names Architecture and Heritage as an LM-4 Master's course taught in English, with English B2 and Italian knowledge requirements for international students. It is a 2024/25 regulation and is not used as 2027/28 admission evidence.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_program_requirements"],
    },
    {
        "id": "SRC-UNINA-MED-ENGLISH-2025",
        "university_id": "napoli-federico-ii", "title": "Medicine and Surgery in English – official single-cycle degree regulation",
        "url": "https://www.medicina.unina.it/pdf/P11/SMA-2024.pdf",
        "source_type": "Official degree programme regulation", "accessed_at": "2026-11-10", "cycle": "2025-2026",
        "evidence": "The 2025/26 regulation identifies Medicine and Surgery in English as a six-year single-cycle LM-41 Master's, not a standalone BSc. Annual national admission criteria and places must be checked in the next ministerial call.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-UNINA-MED-ENGLISH-2026",
        "university_id": "napoli-federico-ii", "title": "Federico II 2026/27 healthcare-course semester-filter announcement",
        "url": "https://www.unina.it/en/w/semestre-filtro-2026/27-al-via-le-lezioni-per-i-corsi-di-area-sanitaria",
        "source_type": "Official University announcement", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The 2026/27 announcement identifies Medicine and Surgery (LM-41) among the University healthcare programmes under the national filter-semester process. It confirms current-cycle programme activity, not the 2027/28 annual call.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNINA-CIVIL-ENV-BSC-2026",
        "university_id": "napoli-federico-ii", "title": "Civil and Environmental Engineering BSc – official 2026/27 admission page",
        "url": "https://www.civil-environmental.unina.it/admission/",
        "source_type": "Official degree programme and admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies an English-taught three-year BSc in Civil and Environmental Engineering, class L-7 R, at Federico II. The page describes 2026 admission schedule, CEnT-S/SAT routes, B2 English and non-EU Universitaly pre-admission; those deadlines are historical and not 2027/28.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_admission", "program.previous_cycle_english_requirement"],
    },
    {
        "id": "SRC-UNIFI-ARCHITECTURE-MSC-2026",
        "university_id": "firenze", "title": "Architecture – official degree profile and 2026/27 study plan",
        "url": "https://www.unifi.it/en/study-us/degree-programs/second-cycle-degree/architecture",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 2026/27 profile identifies a two-year Florence MSc, class LM-4-R, whose general programme is listed in Italian and English. The English legacy record corresponds to its Architectural Design/iCAD curriculum, not to a separate degree or an all-English parent programme.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.program_type", "program.location"],
    },
    {
        "id": "SRC-UNIFI-ARCH-ICAD-2026",
        "university_id": "firenze", "title": "Architectural Design (iCAD) – official English curriculum and admission page",
        "url": "https://www.icad.unifi.it/vp-238-presentation.html",
        "source_type": "Official degree curriculum profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The School of Architecture identifies Architectural Design (iCAD) as the English-taught curriculum of the two-year Master's in Architecture in Florence. Its dedicated admission page requires English proficiency and evaluates prior qualifications; details need annual recheck.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_program_requirements"],
    },
    {
        "id": "SRC-UNIFI-FINANCE-RISK-MSC-2026",
        "university_id": "firenze", "title": "Finance and Risk Management – official degree profile and 2026/27 plan",
        "url": "https://www.unifi.it/en/study-us/degree-programs/second-cycle-degree/finance-and-risk-management",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Identifies the two-year Florence MSc Finance and Risk Management, class LM-16-R, taught in English, unrestricted access; the linked study plan is for 2026/27. This confirms course identity only, not the 2027/28 intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access", "program.location"],
    },
    {
        "id": "SRC-UNIFI-FINANCE-RISK-ADMISSION-2026",
        "university_id": "firenze", "title": "Finance and Risk Management – official admission requirements",
        "url": "https://www.frm.unifi.it/p107.html",
        "source_type": "Official degree programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Lists quantitative, statistics and social-science preparation, English B2, and degree-background/grade conditions for admission. Treat these as current programme guidance; the 2027/28 rules must be checked against its annual documentation.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement"],
    },
    {
        "id": "SRC-UNIFI-ECON-DEV-MSC-2026",
        "university_id": "firenze", "title": "Economics and Development – official degree profile and 2026/27 plan",
        "url": "https://www.unifi.it/en/study-us/degree-programs/second-cycle-degree/economics-and-development",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Identifies a two-year English-taught MSc in Florence, class LM-56-R, unrestricted access, with Economics and Development Economics curricula. The page links 2026/27 study plans and is not a 2027/28 intake notice.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access", "program.location", "program.curricula"],
    },
    {
        "id": "SRC-UNIFI-GEOENGINEERING-MSC-2026",
        "university_id": "firenze", "title": "Geoengineering – official degree profile and 2026/27 study plan",
        "url": "https://www.unifi.it/en/study-us/degree-programs/second-cycle-degree/geoengineering",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Identifies the two-year English-taught Florence MSc Geoengineering, class LM-35-R, 120 ECTS, unrestricted access. The 2026/27 profile gives prior-degree, curricular-credit and personal-preparation criteria, including English B2; these are not asserted as 2027/28 terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.location"],
    },
    {
        "id": "SRC-UNIFI-GEOENGINEERING-ENROLMENT-2026",
        "university_id": "firenze", "title": "Geoengineering – 2026/27 official enrollment instructions",
        "url": "https://www.ing-gem.unifi.it/p143.html",
        "source_type": "Official programme enrollment page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "States that 2026/27 enrollment dates are July 1 to December 18, 2026 (ordinary deadline), with a late-enrollment period and separate conditional-enrollment rule. These dates apply only to 2026/27 and must not be shown as 2027/28 deadlines.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIFI-URBAN-PLANNING-MSC-2026",
        "university_id": "firenze", "title": "Urban and Regional Planning and Design for Sustainability – official profile",
        "url": "https://www.unifi.it/en/study-us/degree-programs/second-cycle-degree/urban-and-regional-planning-and-design-sustainability",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 2026/27 profile identifies the two-year LM-48-R degree in Prato, with Italian and English delivery and a curriculum named Urban and Regional Planning and Design for Sustainability taught in English. The previous tracker collapsed the parent degree and English curriculum into one record.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.program_type", "program.location"],
    },
    {
        "id": "SRC-UNIFI-URBAN-PLANNING-ADMISSION-2025",
        "university_id": "firenze", "title": "Urban and Regional Planning and Design for Sustainability – official admission information",
        "url": "https://www.clurpd.unifi.it/vp-173-enrolment.html",
        "source_type": "Official degree programme admission page", "accessed_at": "2026-11-11", "cycle": "2025-2026",
        "evidence": "The programme page describes eligible planning/architecture backgrounds, comparative evaluation for other degrees, and English B2. The page is older than the 2026/27 catalogue; these criteria are historical course-level guidance, not certified as current-cycle policy.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement"],
    },
    {
        "id": "SRC-UNIFI-RISE-MSC-2026",
        "university_id": "firenze", "title": "International Relations and European Studies – official 2026/27 course profile",
        "url": "https://www.unifi.it/en/study-us/degree-programs/second-cycle-degree/international-relations-and-european-studies",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Identifies the two-year Florence interclass MSc LM-52-R/LM-90-R. The general profile lists Italian as the programme language; students may select an English-only study pathway, so the record is not described as an English-only degree by default.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.program_type", "program.location"],
    },
    {
        "id": "SRC-UNIFI-RISE-ENGLISH-PATHWAY-2026",
        "university_id": "firenze", "title": "RISE – English-only study pathway and 2026/27 study plan",
        "url": "https://www.rise.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=540",
        "source_type": "Official degree programme pathway page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Students can choose exclusively Italian, exclusively English, or mixed-language courses. Completion of coursework entirely in English may receive an endorsement in the Diploma Supplement. This is an optional pathway within the interclass degree.",
        "supports": ["program.previous_cycle_language", "program.program_type"],
    },
    {
        "id": "SRC-UNIFI-RISE-ADMISSION-2026",
        "university_id": "firenze", "title": "RISE – 2026/27 admission requirements for non-Italian degrees",
        "url": "https://www.rise.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=435",
        "source_type": "Official degree programme admission page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 2026/27 page requires a three-year degree or equivalent and sets a cumulative GPA threshold of 80/100 for applicants with non-Italian degrees; application timing is governed by the live DreamApply platform. Do not carry these criteria into 2027/28 without the new page or call.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIFI-SUSBUS-BSC-2026",
        "university_id": "firenze", "title": "Sustainable Business for Societal Challenges – official degree profile",
        "url": "https://www.unifi.it/en/study-us/degree-programs/first-cycle-degree/sustainable-business-societal-challenges",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Identifies a three-year Florence English-taught first-cycle degree, class L-18-R, blended delivery, restricted access. The current catalogue profile is distinct from the annual 2026/27 call and does not establish 2027/28 availability.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access", "program.location"],
    },
    {
        "id": "SRC-UNIFI-SUSBUS-CALL-2026",
        "university_id": "firenze", "title": "Sustainable Business for Societal Challenges – official 2026/27 admission calls",
        "url": "https://www.unifi.it/en/node/9897",
        "source_type": "Official University call and ranking page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The 2026/27 page reports a limited-access L-18 call, with 250 places and first/second/third rounds. It gives prior-cycle deadlines (11 May, 24 August, 24 September 2026), testing dates and EU restrictions on later rounds; none are 2027/28 dates.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_places", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-ROMA2-COMPUTER-SCIENCE-MSC-2026",
        "university_id": "tor-vergata", "title": "Computer Science – official Tor Vergata MSc catalogue entry",
        "url": "https://web.uniroma2.it/en/contenuto/computer_science-93169",
        "source_type": "Official University course catalogue", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "Identifies the two-year LM-18 Computer Science MSc, taught in Italian, with open access subject to curriculum evaluation. The legacy English-language tag is incorrect; the record is not a fully English-taught degree.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_access", "program.location"],
    },
    {
        "id": "SRC-ROMA2-COMPUTER-SCIENCE-REGULATIONS-2026",
        "university_id": "tor-vergata", "title": "Computer Science – official Master's regulations",
        "url": "https://informatica.uniroma2.it/en/home/magistrale/il-corso/regulations/",
        "source_type": "Official degree programme regulation", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The regulation confirms LM-18, two years/120 ECTS, no restricted places, case-by-case curriculum requirements, and the degree programme's academic structure. It provides current course rules but does not announce the 2027/28 first-year intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-POLITO-MATHEMATICAL-ENGINEERING-PROFILE-2026",
        "university_id": "politecnico-torino", "title": "Mathematical Engineering – official programme profile",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/mathematical-engineering",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The current profile identifies a two-year LM-44 Master's programme at the Main Campus, with uncapped admission subject to requirements. The displayed profile is for 2026/27 and lists Italian as the language; it is not proof of the 2027/28 language or admission rules.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_level", "program.previous_cycle_language", "program.previous_cycle_location", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-POLITO-MATHEMATICAL-ENGINEERING-ENGLISH-TRACK-2027",
        "university_id": "politecnico-torino", "title": "Mathematical Engineering – planned English study track from 2027/28",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/mathematical-engineering/guidelines",
        "source_type": "Official programme curriculum information", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The official page says an entirely English-taught track is planned from 2027/28, with Scientific Computing & HPC and Cryptography & Cybersecurity specializations. It explicitly says the track is pending approval and may change.",
        "supports": ["program.planned_2027_2028_english_track", "program.language"],
    },
    {
        "id": "SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027",
        "university_id": "politecnico-torino", "title": "Mathematical Engineering scholarships for foreign-degree students – AY 2027/28",
        "url": "https://www.polito.it/en/education/services-and-life-at-politecnico/right-to-education-and-tuition-fees/scholarships-and-awards?tipo_borsa=S",
        "source_type": "Official programme-specific scholarship call", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The official call announces three gross €16,000 scholarships for students with a suitable foreign first-cycle qualification who submit a 2027/28 admission application, are assessed eligible/admitted, and enroll for the first time in Mathematical Engineering in 2027/28. Scholarship applications run 14 October 2026–29 January 2027; these are scholarship dates, not the degree admission deadline. The call does not establish approval of the planned English track.",
        "supports": ["program.availability", "program.scholarships", "program.scholarship_application_window"],
    },
    {
        "id": "SRC-POLIMI-28DIGITAL-APPLICATIONS-2027",
        "university_id": "politecnico-milano", "title": "28DIGITAL – Polimi entry applications for AY 2027/28",
        "url": "https://www.mastereit.polimi.it/international-applications/",
        "source_type": "Official joint-degree admissions page", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The official 28DIGITAL page says applications are open for September 2027 entry and names Polimi's local MSc options as Computer Science and Engineering (T2A) or High Performance Computing Engineering. Candidates must also submit a separate Polimi application; the 28DIGITAL offer assigns entry/exit universities based on preferences and assessment. For applicants with a degree from outside Italy, Polimi calls are 1 Oct–1 Dec 2026, 12 Jan–25 Feb 2027, and 1–18 Mar 2027 (the additional call is limited to EEA and non-EU residents in Italy); the local application fee is €50 through 1 Dec or €150 from 2 Dec. For degrees from Italy, the local application is invited in July–August 2027, with exact dates to be published in spring. The first 28DIGITAL period deadline is 31 Jan 2027; later periods depend on available places.",
        "supports": ["program.availability", "program.application_route", "program.application_windows", "program.application_fee", "program.language_requirement"],
    },
    {
        "id": "SRC-PADUA-ENGLISH-DEGREES-PROPOSED-2027",
        "university_id": "padova", "title": "Degree programmes held in English – proposed 2027/28 BSc and MSc additions",
        "url": "https://www.unipd.it/en/corsi-laurea-lingua-inglese",
        "source_type": "Official English-language course catalogue", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The English-degree catalogue lists three new 2027/28 Bachelor's proposals (Management, Finance and Business Analytics; Food Safety for Global Health; Innovative Technologies in Agriculture), each marked 'to be approved'. In the School of Science English Master's list, Data Analytics and Decision Support is marked as a new 2027/28 programme 'to be approved', and Statistical Sciences is also marked 'to be approved'. These are proposed entries, not confirmation of final approval, first-year intake, or course-specific admission terms.",
        "supports": ["program.planned_course_listing", "program.planned_level", "program.planned_language", "program.approval_status"],
    },
    {
        "id": "SRC-PADUA-STATISTICAL-SCIENCE-PROFILE-2027",
        "university_id": "padova", "title": "Statistical Science – Department programme profile and projected start",
        "url": "https://www.stat.unipd.it/en/statistical-science",
        "source_type": "Official department programme profile", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The Department profile describes a two-year English-taught Master's programme, 120 ECTS, full-time and on campus, and gives an expected start date of 27 September 2027. The University English Master's catalogue separately marks Statistical Sciences as 'to be approved'; the Department's projected start is therefore treated as a plan, not proof of approval or a confirmed 2027/28 intake. No application-call link was present in the fetched page HTML.",
        "supports": ["program.proposed_course_identity", "program.proposed_level", "program.proposed_language", "program.proposed_duration", "program.proposed_ects", "program.projected_start_date"],
    },
    {
        "id": "SRC-PADUA-STATISTICAL-SCIENCE-ENTRY-REQUIREMENTS",
        "university_id": "padova", "title": "Statistical Science – Department entry-requirements page",
        "url": "https://www.stat.unipd.it/en/statistical-science/entry-requirements",
        "source_type": "Official department entry-requirements page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "The page gives preliminary-looking entry criteria, including subject-credit and 85/110 thresholds for Italian-degree applicants, B2 English and a three-year Bachelor's degree; its international-applicant section does not provide a complete course-specific checklist. It is not labelled for AY 2027/28, and the degree proposal remains marked 'to be approved' in the University catalogue. Do not use these criteria as confirmed 2027/28 rules.",
        "supports": ["program.proposed_admission_requirements", "program.proposed_language_requirement"],
    },
    {
        "id": "SRC-PADUA-ARQUS-PHYSICS-TECH-2026",
        "university_id": "padova", "title": "Arqus joint Bachelor's Programme in Physics for Technology – development agreement",
        "url": "https://www.unipd.it/en/arqus/news/rettrice-partecipa-consiglio-rettori-alleanza-europea-arqus",
        "source_type": "Official University and Arqus programme-development announcement", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "Padua reports a signed consortium agreement to develop a joint Bachelor's programme in Physics for Technology with the University of Granada, Vilnius University and the University of Wroclaw. The announcement does not give a launch academic year, teaching language, admission call, or approval/accreditation outcome; the current English-degree catalogue does not list this programme.",
        "supports": ["program.proposed_course_identity", "program.planned_level", "program.partnership"],
    },
    {
        "id": "SRC-PADUA-STUDY-ENGLISH-APPLY-ITALIAN-2027",
        "university_id": "padova", "title": "Studiare in inglese – Come fare domanda (official Italian procedure)",
        "url": "https://www.unipd.it/studiare-inglese-come-fare-domanda",
        "source_type": "Official Italian-language international application procedure", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The legally authoritative Italian page states that, for English-taught degrees other than Medicine and Surgery, applicants use apply.unipd.it, may apply to at most two courses, and pay a non-refundable €60 pre-enrolment fee (with a CEnT-S exception). For unlimited-place courses it lists Call 1: 15 September–15 November 2026; Call 2: 1 December 2026–1 March 2027; Call 3: 1 April–1 June 2027, only for EU citizens and non-EU citizens resident in Italy. For limited-place courses it lists 7 January–7 March 2027 for non-EU citizens abroad and 15 March–7 April 2027 for English-taught programmes for EU/EU-equated applicants, with course-specific exceptions. This is University procedure by admission type; it does not prove an unapproved programme is included or replace an individual course call.",
        "supports": ["university.application_windows", "university.application_route", "university.application_fee", "university.applicant_categories", "university.required_documents"],
    },
    {
        "id": "SRC-PADUA-INTL-EXCELLENCE-2027-BOARD",
        "university_id": "padova", "title": "2027/28 Padua International Excellence Scholarship – Board allocation announcement",
        "url": "https://www.unipd.it/node/93348",
        "source_type": "Official Board of Administration announcement", "accessed_at": "2026-11-11", "cycle": "2027-2028",
        "evidence": "The Board of Administration announcement for 29 September 2026 states that the University allocates €1,432,200 for the 2027/28 Padua International Excellence Scholarship edition, with up to 76 awards for the highest-ranked candidate of each English-taught degree/curriculum, including newly activated programmes. Each award is €8,000 gross per year plus exemption from university tuition fees; the release specifically says renewal for second and third year applies to Bachelor's and single-cycle cohorts. The annual call still determines detailed eligibility, selection, award retention and final course-level coverage.",
        "supports": ["university.scholarships_2027_2028", "program.scholarship_scheme_2027_2028", "scholarship.total_awards", "scholarship.amount", "scholarship.fee_exemption", "scholarship.scope"],
    },
    {
        "id": "SRC-PADUA-INTL-EXCELLENCE-PROGRAMME",
        "university_id": "padova", "title": "Padua International Excellence Scholarship Programme – general terms and call status",
        "url": "https://www.unipd.it/en/padua-international-excellence-scholarship-programme",
        "source_type": "Official international scholarship programme page", "accessed_at": "2026-11-11", "cycle": "general",
        "evidence": "The official page describes the general scheme as up to 76 awards for international students in English-taught Bachelor's, Master's and single-cycle degrees, €8,000 gross per year plus fee exemption (regional fee and stamp duty remain payable), max two years for Master's and three for Bachelor's/single-cycle programmes. It gives general eligibility guidance (non-Italian citizen except dual nationality, foreign qualification, not resident in Italy at application, apply to an English-taught programme), says first-call candidates are prioritized with second-call awards only exceptionally, and states that the 2027/28 call details are expected in November 2026. The page also links a 2026/27 call; use the separate Board source for cycle-specific 2027/28 allocation and the forthcoming annual call for definitive terms.",
        "supports": ["university.scholarship_scheme_terms", "university.scholarship_eligibility", "university.scholarship_call_status"],
    },
    {
        "id": "SRC-PADUA-TUITION-2026",
        "university_id": "padova", "title": "Student fees – 2026/27 fee notice and published tariff guidance",
        "url": "https://www.unipd.it/en/contribuzione-studentesca",
        "source_type": "Official student fees page", "accessed_at": "2026-11-11", "cycle": "2026-2027",
        "evidence": "The latest linked annual tuition notice is for 2026/27. The page says degree-program fees range from €0 to approximately €3,000/year, first-year initial instalment €208 (including €192 regional tax and €16 stamp duty), subsequent-year initial instalment €588 including €380 contribution, with remaining amounts varying by programme and personal/financial circumstances. It also gives 2026/27 fixed fees for non-EU citizens whose household is outside Italy: €2,790 / €930 low-HDI Group A and €2,990 / €996.66 low-HDI Group B. It does not publish a 2027/28 annual tuition notice on the reviewed page; do not carry any 2026/27 amount forward.",
        "supports": ["university.previous_cycle_tuition", "university.tuition_2027_2028_publication_status", "university.non_eu_tuition_2026_2027"],
    },
    {
        "id": "SRC-PADUA-STUDENT-AWARDS-CYBERSECURITY-2026",
        "university_id": "padova",
        "title": "Padua student study awards – Cybersecurity existing-student award, Fourth Edition 2026",
        "url": "https://www.unipd.it/en/node/93620",
        "source_type": "Official University student-awards page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2028",
        "evidence": "The University lists two awards of €11,280 each for high-achieving students in the final two years of the MSc in Cybersecurity, paid in two annual instalments for 2026/27 and 2027/28, with an application deadline of 18 March 2027. Because payments begin in 2026/27 and eligibility is for students in the final two years, this is an award for the existing cohort and not a scholarship for students newly entering in 2027/28. The same page lists Computer Engineering awards tied to students entering in 2025/26; those are not carried forward as 2027/28 entrant funding.",
        "supports": ["program.current_student_award", "program.previous_cycle_scholarships", "program.scholarship_scope"],
    },
    {
        "id": "SRC-UNITO-EAP-PROFILE-2027",
        "university_id": "torino",
        "title": "Economic Analysis and Policy – official University of Turin degree profile",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/economic-analysis-and-policy",
        "source_type": "Official University degree programme profile",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The current official UniTo profile lists Economic Analysis and Policy as an English-taught, two-year, free-access Master's degree in LM-56 R Economics, based in Turin. It states the local course admission requirements as 18 CFU in economics and 6 CFU in statistics and describes a preliminary curricular evaluation followed by a 15-minute Zoom TAPP interview. This conflicts with the 24-ECTS economics threshold stated on the current EPOG application page and the EAP-specific application checklist; preserve the discrepancy and do not treat the local profile threshold as resolving the joint-master call requirements.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.access", "program.degree_class", "program.admission_requirements_conflict"],
    },
    {
        "id": "SRC-UNITO-EAP-APPLICATION-2027",
        "university_id": "torino",
        "title": "Economic Analysis and Policy – 2027/28 cohort application instructions",
        "url": "https://www.eap.unito.it/do/home.pl/View?doc=how_to_apply.html",
        "source_type": "Official University of Turin programme application page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The official programme application page identifies the 2027–2028 cohort and says applicants apply online through the EPOG website. Its application-document checklist requires a prior degree of at least 180 ECTS, transcripts showing a minimum of 24 ECTS in economics and 6 ECTS in statistics/econometrics, English proficiency, a statement of purpose up to 500 words, two recommendation letters, and a passport. Erasmus Mundus scholarship applicants must also provide recent proof of residence. This page agrees with the consortium's 24-ECTS economics rule and conflicts with the 18-CFU figure on UniTo's central degree profile.",
        "supports": ["program.availability_2027_2028", "program.application_route", "program.admission_requirements", "program.application_documents", "program.scholarship_eligibility"],
    },
    {
        "id": "SRC-EPOG-ADMISSION-2027",
        "university_id": "torino",
        "title": "EPOG-JM 2027–2029 consortium admission call",
        "url": "https://www.epog.eu/admission-and-scholarships/admission/",
        "source_type": "Official Erasmus Mundus joint-master consortium admission page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2029",
        "evidence": "The live EPOG-JM page confirms the two-year 2027–2029 cohort application is open and closes 27 January 2027 at 13:00 Europe/Paris. It requires a Bachelor's or equivalent degree of at least 180 ECTS, 24 ECTS in economics and 6 ECTS in statistics/econometrics, English at CEFR C1 or the listed equivalent scores, and a clear motivation for the programme; applicants may be interviewed in March 2027, with results expected by end of March. The consortium call serves multiple partner pathways; the separate degree-policy page shows that the University of Turin award is available only for specified pathway combinations.",
        "supports": ["program.availability_2027_2028", "program.application_windows", "program.application_route", "program.program_specific_requirements_2027_2028", "program.english_language_requirement_2027_2028", "program.selection_process"],
    },
    {
        "id": "SRC-EPOG-APPLICATION-PLATFORM-2027",
        "university_id": "torino",
        "title": "EPOG online application platform – 2027–2029 campaign",
        "url": "https://application.epog.eu/",
        "source_type": "Official joint-master application platform",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2029",
        "evidence": "The consortium's live application platform lists the EPOG-JM two-year programme for 2027–2029 with a closing time of 27 January 2027 at 13:00 Europe/Paris. This independently confirms the current call and application deadline. The platform page does not state an application fee.",
        "supports": ["program.application_route", "program.application_windows", "program.application_fee_2027_2028"],
    },
    {
        "id": "SRC-EPOG-SCHOLARSHIPS",
        "university_id": "torino",
        "title": "EPOG-JM Erasmus Mundus scholarship terms",
        "url": "https://www.epog.eu/admission-and-scholarships/scholarships/",
        "source_type": "Official Erasmus Mundus joint-master scholarship page",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The official page states that the EPOG Erasmus Mundus scholarship covers tuition and required health/accident insurance and provides €1,400 per month during both academic years. It says applicants of any nationality can be eligible if they meet the academic criteria, except people who previously held an EMJM scholarship; holders cannot combine it with another EU-funded scholarship for the same course. It does not state the number or 2027–2029 allocation of awards, so the scheme terms are recorded separately from a confirmed cohort award count.",
        "supports": ["program.scholarships_2027_2028", "program.scholarship_amount", "program.scholarship_eligibility", "program.scholarship_scope"],
    },
    {
        "id": "SRC-EPOG-TUITION-FEES",
        "university_id": "torino",
        "title": "EPOG-JM programme tuition and fee policy",
        "url": "https://www.epog.eu/admission-and-scholarships/tuition-fees/",
        "source_type": "Official Erasmus Mundus joint-master tuition page",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The current consortium page lists a €1,000/year fee including health/accident insurance for students with personal income below €26,400/year, a possible full €9,600/year fee above that threshold, and a complete fee waiver for Erasmus Mundus scholarship holders; non-scholarship students may request a full or partial waiver. The page is not explicitly cycle-labelled for 2027–2029, so retain these as current published general terms requiring cohort-specific confirmation rather than asserting a settled 2027/28 tuition amount.",
        "supports": ["program.tuition_2027_2028", "program.application_fee_2027_2028", "program.scholarship_fee_waiver"],
    },
    {
        "id": "SRC-EPOG-DEGREE-POLICY",
        "university_id": "torino",
        "title": "EPOG-JM degree-awarding and mobility pathways",
        "url": "https://www.epog.eu/outcomes/degree-policy/",
        "source_type": "Official Erasmus Mundus joint-master degree policy",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The EPOG degree policy confirms that the two-year 120-ECTS programme awards joint or multiple degrees based on the institutions attended in year one and year two. Its award matrix lists University of Turin's Master's in Economic Analysis and Policy for Major A and Minor C2 pathway combinations only. This is a multi-partner joint programme; a Turin degree is conditional on the selected pathway and mobility, not guaranteed for every EPOG applicant.",
        "supports": ["program.joint_degree_pathways", "program.mobility", "program.degree_award"],
    },
    {
        "id": "SRC-UNIPI-INFO-ENG-2027-CALL",
        "university_id": "pisa",
        "title": "Department of Information Engineering – 2027/28 international MSc admission call",
        "url": "https://computer.ing.unipi.it/call-for-international-students/",
        "source_type": "Official department admission call and requirements page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The Department's current call explicitly invites applicants holding foreign qualifications for 2027/28 entry to two English-taught MSc programs: Computer Engineering and Artificial Intelligence and Data Engineering. Deadline: 1 February 2027 at 23:59 GMT; tentative results date 12 March 2027; €30 per application, up to two applications through applymscenglish.unipi.it. The call requires a three-year BSc/equivalent with computer hardware/software preparation, algorithms/programming, computer architecture, operating systems, networks and databases, strong mathematics and English B2; applicants needing a visa must provide an internationally recognised four-skill B2 certificate (a Medium of Instruction letter is insufficient). It lists required documents, selection steps, financial-aid schemes, and states 2027/28 tuition is expected around June 2027 while MAECI and Invest Your Talent scholarship calls are not yet announced.",
        "supports": ["program.availability_2027_2028", "program.application_windows", "program.application_fee_2027_2028", "program.application_route", "program.program_specific_requirements_2027_2028", "program.english_language_requirement_2027_2028", "program.application_documents", "program.selection_process", "program.tuition_2027_2028", "program.scholarships_2027_2028"],
    },
    {
        "id": "SRC-UNIPI-AIDE-COURSE-PROFILE",
        "university_id": "pisa",
        "title": "Artificial Intelligence and Data Engineering – current official MSc profile",
        "url": "https://computer.ing.unipi.it/en/masters-degree-in-artificial-intelligence-and-data-engineering/",
        "source_type": "Official Department degree programme profile",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The current Department profile identifies Artificial Intelligence and Data Engineering as an LM-32 Master's degree in Pisa. It describes delivery as English/Italian: compulsory activities are in English, and English-taught credits suffice to complete the degree without Italian; some remedial basic Computer Engineering courses are only in Italian. The profile supports current course identity and language scope; the separate named 2027/28 Department call is the evidence for new-entry availability and its foreign-degree route.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.degree_class", "program.course_structure"],
    },
    {
        "id": "SRC-UNIPI-COMPUTER-ENGINEERING-PROFILE",
        "university_id": "pisa",
        "title": "Computer Engineering – current official MSc profile",
        "url": "https://computer.ing.unipi.it/en/masters-degree-in-computer-engineering/",
        "source_type": "Official Department degree programme profile",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The official Department profile identifies Computer Engineering as an English-taught Master's degree in the LM-32 class, based in Pisa, with open access subject to skills assessment. It lists Cloud/Network Infrastructure and Services, Cyber-Physical Systems, and Cybersecurity study tracks. The linked 2027/28 foreign-qualification call separately establishes the current intake and applicant-category deadlines.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.degree_class", "program.tracks", "program.access"],
    },
    {
        "id": "SRC-BBS-DSBA-2027",
        "university_id": "bologna",
        "title": "Data Science and Business Analytics – 2027/28 BBS Professional Master",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/master-in-data-science-2/",
        "source_type": "Official Bologna Business School programme and admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The BBS programme page explicitly advertises 2027/28 applications opening soon, four selection rounds between March and September 2027, and an October 2027 start. It identifies the course as a one-year, full-time, English-language, 60-ECTS Professional Master delivered at the Bologna BBS campus in collaboration with the University of Bologna Department of Computer Science and Engineering (DISI). The detailed annual call is pending. The page currently displays a €14,800 tuition fee, partial awards of €4,000 and €6,000, B2 English, a first-cycle degree, tests and interview, and a €60 selection fee; these are not labelled as 2027/28 terms and are retained only as current displayed information pending the annual call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.credits", "program.program_type", "program.availability_2027_2028", "program.selection_period_2027_2028", "program.current_published_fees", "program.current_published_requirements"],
    },
    {
        "id": "SRC-BBS-AI-MANAGEMENT-2027",
        "university_id": "bologna",
        "title": "Artificial Intelligence for Management – 2027/28 BBS Professional Master",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/artificial-intelligence-2/",
        "source_type": "Official Bologna Business School programme and admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The BBS programme page explicitly advertises 2027/28 applications opening soon, four selection rounds between March and September 2027, and an October 2027 start. It identifies the course as a one-year, full-time, English-language Professional Master delivered in Bologna in collaboration with the University of Bologna Department of Computer Science and Engineering (DISI). The detailed annual call is pending. The page currently displays a €14,800 tuition fee, partial awards of €4,000 and €6,000, B2 English, a first-cycle degree, tests and interview, and a €60 selection fee; these are not labelled as 2027/28 terms and are retained only as current displayed information pending the annual call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.program_type", "program.availability_2027_2028", "program.selection_period_2027_2028", "program.current_published_fees", "program.current_published_requirements"],
    },
    {
        "id": "SRC-BBS-ENTREPRENEURIAL-FINANCE-2027",
        "university_id": "bologna",
        "title": "Finance – Entrepreneurial Finance – 2027/28 BBS Professional Master",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/entrepreneurial-finance/",
        "source_type": "Official Bologna Business School programme and admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The BBS programme page explicitly advertises 2027/28 applications opening soon, four selection rounds between March and September 2027, and an October 2027 start. It identifies the course as a one-year, full-time, English-language, 60-ECTS Professional Master delivered in Bologna in collaboration with the University of Bologna Department of Management (DISA). The detailed annual call is pending. The page currently displays a €14,800 tuition fee, partial awards of €4,000 and €6,000, B2 English, a first-cycle degree, tests and interview, and a €60 selection fee; these are not labelled as 2027/28 terms and are retained only as current displayed information pending the annual call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.credits", "program.program_type", "program.availability_2027_2028", "program.selection_period_2027_2028", "program.current_published_fees", "program.current_published_requirements"],
    },
    {
        "id": "SRC-BBS-FINANCE-AI-2027",
        "university_id": "bologna",
        "title": "Finance – Finance and Artificial Intelligence – 2027/28 BBS Professional Master",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/finance-and-ai-2/",
        "source_type": "Official Bologna Business School programme and admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The BBS page explicitly advertises 2027/28 applications opening soon, four selection rounds between March and September 2027, and an October 2027 start. It identifies Finance and Artificial Intelligence as a one-year, full-time, English-language, 60-ECTS Professional Master delivered in Bologna with the University of Bologna Department of Management (DISA). The annual call is pending. The page currently displays €14,800 tuition, €4,000 and €6,000 partial awards, B2 English, a Bachelor's degree, selection tests/interview and a €60 application fee; it does not label these as 2027/28 terms, so they remain current displayed information pending the annual call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.credits", "program.program_type", "program.availability_2027_2028", "program.selection_period_2027_2028", "program.current_published_fees", "program.current_published_requirements"],
    },
    {
        "id": "SRC-BBS-MARKETING-ANALYTICS-AI-2027",
        "university_id": "bologna",
        "title": "Marketing Management – Analytics and AI for Marketing – 2027/28 BBS track",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/analytics-and-ai-for-marketing/",
        "source_type": "Official Bologna Business School programme and admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2027-2028",
        "evidence": "The BBS page explicitly advertises 2027/28 applications opening soon, four selection rounds between March and September 2027, and an October 2027 start. It identifies Analytics and AI for Marketing as a track within the Marketing Management first-level Professional Master, not as a separate Laurea Magistrale or stand-alone degree. The track is full-time, English-language, 12 months and 60 ECTS at the BBS campus in Bologna, run with the University of Bologna Department of Management (DISA). The annual call is pending. The page currently displays €14,800 tuition, €4,000 and €6,000 partial awards, B2 English, a Bachelor's degree, selection tests/interview and a €60 application fee; these are not labelled as 2027/28 terms and remain current displayed information pending the annual call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.credits", "program.program_type", "program.availability_2027_2028", "program.selection_period_2027_2028", "program.current_published_fees", "program.current_published_requirements"],
    },
    {
        "id": "SRC-SAPIENZA-MEDICINE-VARIANTS-2026",
        "university_id": "sapienza",
        "title": "Medicine and Surgery course variants – AY 2026/27 catalogue",
        "url": "https://corsidilaurea.uniroma1.it/it/solr-offerta-formativa-t?search_api_views_fulltext=Medicina+e+chirurgia",
        "source_type": "Official Sapienza course catalogue search",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current official AY 2026/27 catalogue lists eight Italian-taught LM-41 single-cycle Medicine and Surgery variants: A (33452), B (33559), C (33560), D (33561), E/Polo Pontino (33453), HT (33562), Sant'Andrea (33567), and G/Rieti (32925). Each is marked Semestre filtro. It separately lists Medicine and Surgery F (33454), six-year single-cycle LM-41, English, Rome, with admission-test access. The legacy tracker row does not specify a campus/variant and remains an umbrella lead, not a one-to-one course match.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_admission_route"],
    },
    {
        "id": "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026",
        "university_id": "sapienza",
        "title": "Medicine and Surgery F – AY 2026/27 course profile",
        "url": "https://corsidilaurea.uniroma1.it/en/course/33454",
        "source_type": "Official Sapienza course profile",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "Course 33454 is a six-year single-cycle LM-41 degree in Rome, taught in English and marked as admission-test access. This identifies only the English F variant; it does not resolve which Sapienza Medicine course the generic legacy row intended.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_admission_route"],
    },
    {
        "id": "SRC-SAPIENZA-MEDICINE-F-CALL-2026",
        "university_id": "sapienza",
        "title": "Medicine and Surgery F – AY 2026/27 admission call",
        "url": "https://www.corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/33454_i.pdf",
        "source_type": "Official Sapienza admission call PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The 2026/27 Sapienza call for the English-language Medicine and Surgery F course states 52 places for Italian/EU/equivalent applicants and 13 for non-EU residents abroad. Universitaly registration ran 26 August–9 September 2026 at 15:00 Rome time; the in-person test was 29 September. It required a secondary-school diploma obtained or to be obtained in 2026, plus the separate visa-pre-enrolment route by 30 June for non-EU applicants resident abroad. The test comprised 60 questions in 100 minutes, scored +1.5 correct, −0.4 incorrect and 0 blank; the ranking threshold was at least 20 for Italian/EU/equivalent applicants and above zero for non-EU residents abroad. Listed language certificates are tie-break evidence, not a separately stated minimum entry requirement. The call requires a test contribution through Universitaly but does not state its amount. All of these are historical 2026/27 terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_available_places", "program.previous_cycle_admission_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_application_fee"],
    },
    {
        "id": "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026",
        "university_id": "sapienza",
        "title": "Medicine and Surgery – AY 2026/27 open-semester procedure",
        "url": "https://www.uniroma1.it/it/notizia/semestre-aperto-2026-2027-i-corsi-di-medicina-e-chirurgia-e-di-odontoiatria-e-protesi",
        "source_type": "Official Sapienza open-semester admissions guidance",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "Sapienza's 2026/27 open-semester guidance concerns its Italian-taught Medicine and Surgery routes: three 6-CFU foundation courses (Biology, Chemistry and Biochemical Preparations, Physics); Universitaly registration 13 July–3 August 2026 at 18:00, followed by Sapienza payment by 6 August; compulsory attendance; and national ranking after exam sessions on 10 December 2026 and 11 January 2027. The semester contribution is €250, reduced to €200 for qualifying ISEE between €22,000 and €30,000, with specified total exemptions including ISEE up to €22,000, disability/invalidity at least 66%, DiSCo eligibility/award and MAECI award. The page requires an upper-secondary diploma obtained or expected in 2026; non-EU applicants abroad needing a visa had to pre-enrol by 30 June 2026 and meet Italian B2. It names five Sapienza sites available for later course preferences (Policlinico, HT, Sant'Andrea, Polo Pontino and Rieti). These rules are prior-cycle only and do not establish 2027/28 intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_admission_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026",
        "university_id": "sapienza",
        "title": "Ingegneria Aerospaziale – AY 2026/27 TOLC-I admission call (Bando 14616)",
        "url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/14616_bando_ici.pdf",
        "source_type": "Official Sapienza admission call PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The 2026/27 call for course 33474 (test code 14616, L-9) sets 250 total places: 60 EU/equivalent in selection one; 110 plus unused seats from selection one in selection two; 72 plus unused seats from selection two for EU/equivalent in selection three; and 8 non-EU visa-applicant seats in selection three, one reserved for Marco Polo. It gives three TOLC-I selection windows, test format/scoring, cutoffs, qualification and language requirements, €10 per Sapienza selection, a separate €35 CISIA test fee, first-round €200 pre-enrolment contribution credited against tuition, and 2026/27 enrollment dates. All details are historical and do not establish the 2027/28 call.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_application_windows", "program.previous_cycle_available_places", "program.previous_cycle_admission_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_application_fee", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026",
        "university_id": "sapienza",
        "title": "Civil and Industrial Engineering – AY 2026/27 restricted-access call listing",
        "url": "https://ici.web.uniroma1.it/it/bandi-di-accesso-ai-corsi-di-studio-numero-programmato-aa-202627",
        "source_type": "Official Sapienza faculty admissions page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The Faculty of Civil and Industrial Engineering's 2026/27 call index links Bando 14616 for course 33474 Ingegneria Aerospaziale and identifies the L-9 call inventory. It is prior-cycle evidence only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route"],
    },
    {
        "id": "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026",
        "university_id": "sapienza",
        "title": "Engineering restricted-access admissions and 2026/27 selection results",
        "url": "https://www.uniroma1.it/it/pagina/corsi-ad-accesso-programmato-delle-facolta-di-ingegneria",
        "source_type": "Official Sapienza admissions and results page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current page lists the Sapienza engineering restricted-access procedures and results for AY 2026/27. For Aerospace Engineering 33474, it says that all places in the DR 688/2026 call were assigned after the second scrolling, so a third list would not be published. This is a closed prior-cycle result, not evidence about 2027/28 availability.",
        "supports": ["program.previous_cycle_admission_windows", "program.previous_cycle_available_places", "program.previous_cycle_outcome"],
    },
    {
        "id": "SRC-SAPIENZA-SCHOLARSHIPS-2026",
        "university_id": "sapienza",
        "title": "Sapienza scholarships and student benefits inventory",
        "url": "https://www.uniroma1.it/en/pagina/scholarships",
        "source_type": "Official university scholarship inventory",
        "accessed_at": "2026-11-11",
        "cycle": "general",
        "evidence": "The official scholarship inventory describes regional DiSCo Lazio benefits and other competitive or eligibility-limited schemes. The reviewed page did not publish a 2027/28 incoming-student scholarship call for this Bachelor's course; annual calls and individual eligibility must be checked when issued.",
        "supports": ["program.previous_cycle_scholarships", "program.scholarships_2027_2028"],
    },
    {
        "id": "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026",
        "university_id": "sapienza",
        "title": "Scienze politiche e relazioni internazionali – AY 2026/27 access call (Bando 14620)",
        "url": "https://corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/14620_i_0.pdf",
        "source_type": "Official Sapienza admission call PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The 2026/27 call (D.R. 1296/2026, published 23 June 2026) covers course 33618, L-36, under a knowledge-verification procedure and assigns test code 14620. It requires TOLC-SU or TOLC@CASA (valid from January 2025), with a limited exemption for applicants who took TOLC-SPS in 2025; no competitive seat ranking is specified. The call gives the original 29 October TOLC/access-contribution deadline and 5 November first-installment deadline; a later university notice extended deadlines for non-restricted courses. The TOLC-SU is 50 questions/100 minutes plus separate English, scored +1/−0.25/0; the call assigns an Italian OFA at scores <=18/50 and for TOLC-SPS <=12/40. It requires a 2026 secondary-school diploma (obtained or expected); applicants resident abroad who need a study visa also had to submit Universitaly pre-enrolment by 30 June 2026 and satisfy Italian B2. Sapienza's access contribution was €10 and CISIA's test fee €35. These facts are historical and do not establish 2027/28 entry terms.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_admission_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_application_fee", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026",
        "university_id": "sapienza",
        "title": "Sapienza AY 2026/27 admissions index – Political Science area",
        "url": "https://www.uniroma1.it/it/node/534988",
        "source_type": "Official Sapienza admissions index",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The official admissions index lists the Political Science-area 2026/27 knowledge-verification call, test code 14620, and course 33618 Scienze politiche e relazioni internazionali. It is prior-cycle listing evidence only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route", "program.previous_cycle_available_places"],
    },
    {
        "id": "SRC-SAPIENZA-POLITICAL-SCIENCE-APPLY-2026",
        "university_id": "sapienza",
        "title": "Scienze politiche e relazioni internazionali – application and OFA page",
        "url": "https://corsidilaurea.uniroma1.it/it/course/33618/apply",
        "source_type": "Official Sapienza course application page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current course page links the 2026/27 access call and displays an OFA news note that explicitly refers to the older D.R. 1696/2025 call, with no-OFA thresholds of >=18/50 for TOLC-SU and >=12/40 for TOLC-SPS. The current 2026/27 call is D.R. 1296/2026 and states OFA thresholds <=18/50 and <=12/40, respectively. The score-18 boundary is therefore recorded with the newer cycle-specific call and the stale older-cycle page note is flagged instead of silently merged.",
        "supports": ["program.previous_cycle_entrance_test", "program.previous_cycle_admission_requirements"],
    },
    {
        "id": "SRC-SAPIENZA-OPEN-ACCESS-DEADLINE-EXTENSION-2026",
        "university_id": "sapienza",
        "title": "Sapienza 2026/27 deadline extension for non-restricted degree programmes",
        "url": "https://www.uniroma1.it/en/pagina/tuition-fees-and-benefits",
        "source_type": "Official Sapienza enrollment and tuition guidance",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current Sapienza page says applicants to non-restricted degree programmes may sit the required TOLC and pay the €10 access contribution through 19 November 2026, and pay the first tuition instalment through 25 November 2026. It lists the second and third instalments as due 27 December 2026 and 25 March 2027. These university-wide extensions apply to the non-restricted 2026/27 route; they do not establish 2027/28 dates.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_tuition", "program.application_windows_2027_2028"],
    },
    {
        "id": "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026",
        "university_id": "sapienza",
        "title": "Psychology and Health – AY 2026/27 admission call (Bando 05429)",
        "url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/05429_i.pdf",
        "source_type": "Official Sapienza admission call PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The 2026/27 Bando 05429 (D.R. 1329/2026, issued 24 June 2026) is for four separate L-24 courses including Psicologia e Salute (33570), with test code 05429. It assigns Psychology and Health 275 Italian/EU/equivalent places and 10 places for non-EU applicants resident abroad who need a study visa. New entrants had to take CISIA TOLC-PSI or TOLC@CASA, score at least 23/50 for ranking, register a single course preference in Infostud from 2 July to 7 September 2026, and pay a non-refundable €10 Sapienza selection contribution plus the separate €35 CISIA TOLC fee. The call gives the ranking/scorrimento calendar through October and vacancy procedures through 11 November. The test has 50 scored questions in 100 minutes plus 30 English questions in 15 minutes; scoring is +1/−0.25/0, and the English section does not affect ranking. It required a secondary-school diploma obtained or expected in 2026; non-EU visa applicants abroad also needed Universitaly pre-enrolment by 30 June 2026 and Italian B2. These terms are historical and do not establish 2027/28 entry.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_available_places", "program.previous_cycle_admission_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_application_fee", "program.previous_cycle_tuition"],
    },
    {
        "id": "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026",
        "university_id": "sapienza",
        "title": "Sapienza AY 2026/27 admissions index – L-24 Psychology courses",
        "url": "https://www.uniroma1.it/it/node/534988",
        "source_type": "Official Sapienza admissions index",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The official admissions index lists the 2026/27 L-24 Psychology admission call with code 05429 and includes Psicologia e Salute, course 33570. The page is prior-cycle course and route evidence only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route", "program.application_windows_2027_2028"],
    },
    {
        "id": "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026",
        "university_id": "sapienza",
        "title": "Psicologia e Salute – current catalogue application and ranking page",
        "url": "https://corsidilaurea.uniroma1.it/it/course/33570/apply",
        "source_type": "Official Sapienza course application and ranking page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current course page links Bando 05429 and the initial EU ranking plus first, second and third EU scrolling lists. It says OFA must be resolved by the end of year one through support activities and a course recovery test or exam. The linked pages describe the 2026/27 procedure and do not confirm 2027/28 first-year entry.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_windows", "program.previous_cycle_outcome", "program.previous_cycle_entrance_test"],
    },
    {
        "id": "SRC-SAPIENZA-ENGCSAI-PROFILE-2026",
        "university_id": "sapienza",
        "title": "Engineering in Computer Science and Artificial Intelligence – 2026/27 course profile",
        "url": "https://corsidilaurea.uniroma1.it/en/course/33515/home",
        "source_type": "Official Sapienza course profile",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current 2026/27 course catalogue identifies code 33515 as a two-year, English-taught LM-32 Master's degree in Rome, taught in person, with curricular and personal-preparation assessment. The separate official 2024/25 archive identifies code 30430 under a different course title; no source reviewed states that one is the successor of the other.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_admission_route", "program.course_relationship_assessment"],
    },
    {
        "id": "SRC-SAPIENZA-ENGCSAI-CALL-2026",
        "university_id": "sapienza",
        "title": "Engineering in Computer Science and Artificial Intelligence – AY 2026/27 admission call",
        "url": "https://corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/33515_e_1.pdf",
        "source_type": "Official Sapienza admission call PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The 2026/27 call for course 33515 (LM-32, English-taught) requires a suitable three-year Bachelor's degree or equivalent and at least 60 recognized ECTS: at least 24 in basic sciences, including at least 9 in mathematics, and at least 36 in engineering/computing, including at least 18 in Computer Science or Information Processing Systems. English B2 is required. The committee assesses curricular and personal preparation and may interview applicants. Applicants pay €10 for the Infostud eligibility check; deadlines were 15 September 2026 for non-EU visa applicants, 15 October, 17 November and 17 December 2026, and 14 January 2027 for Sapienza graduates/about-to-graduate students. Visa applicants abroad also needed a 2026/27 pre-acceptance letter. All terms are prior-cycle evidence only.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_program_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_contacts"],
    },
    {
        "id": "SRC-SAPIENZA-ENGCSAI-APPLY-2026",
        "university_id": "sapienza",
        "title": "Engineering in Computer Science and Artificial Intelligence – application page",
        "url": "https://corsidilaurea.uniroma1.it/en/course/33515/apply",
        "source_type": "Official Sapienza course application page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current course application page links separate 2026/27 admission-call PDFs in English and Italian and directs applicants to the official call for deadlines and procedure. It confirms the active prior-cycle application page; it does not confirm a 2027/28 first-year call.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.application_windows_2027_2028"],
    },
    {
        "id": "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026",
        "university_id": "sapienza",
        "title": "English-program MoveIN academic and language requirements – June 2026 revision",
        "url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/academic_requirements_movein_2026-2027_web_20260608.pdf",
        "source_type": "Official Sapienza international pre-selection requirements PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The June 8, 2026 revision lists Engineering in Computer Science and Artificial Intelligence among the 2026/27 English-taught Master's programmes in MoveIN pre-selection. For this pre-selection it states a minimum GPA of 75/100, English B2 (with accepted evidence/exemptions), and individual academic review; the course call separately governs final Infostud eligibility and enrollment. Non-EU visa applicants' MoveIN deadline was 15 May 2026, and the document says Italian, EU and EU-equivalent students must not apply through MoveIN. It lists admissions@diag.uniroma1.it as the programme contact. Historical 2026/27 evidence only.",
        "supports": ["program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_program_requirements", "program.previous_cycle_contacts"],
    },
]

BATCH = {
    "id": "physics-of-data-2027-28-call-and-grenfin-joint-master",
    "status": "partial",
    "result": "Added Padua's named 2027/28 Physics of Data international intake and first-call deadline, its English-degree €60 non-refundable application fee and prior-cycle course requirements. Added three Padua English-taught Bachelor's proposals announced for 2027/28 and marked pending approval; recorded Arqus Physics for Technology only as a joint-programme development lead with cycle and language unresolved. The latest official English-degree catalogue also identifies two proposed English Master's candidates: Data Analytics and Decision Support and Statistical Science, each marked as awaiting approval; the Department page gives Statistical Science a projected September 2027 start and preliminary requirements, which remain unconfirmed against the central approval status and annual admissions call. Added Bologna's 2027/28 GrEnFIn Erasmus Mundus Joint Master with exact dates, 51-place maximum, B2/selection rules and up to 18 competitive scholarships. Added PoliTO Mathematical Engineering as a 2027/28 discovery supported by its admissions-linked scholarship call; separately recorded that the planned all-English track remains pending approval and that scholarship dates are not degree admission deadlines. Added Polimi's named 2027/28 28DIGITAL pathway for Computer Science and Engineering (T2A) and High Performance Computing Engineering, with the separate local application, applicant-category deadlines and fee. Linked individual official 2026/27 course profiles for 14 Bologna rows, 15 Padua rows and four Pisa rows that previously had no source IDs. Corrected the Bologna AI and Manufacturing lead to a 2027/28 Global MBA, identified Business Analytics as a curriculum, corrected BBS professional-master classifications, corrected Bologna's Forlì campus for Economia e commercio, corrected Medicine and Giurisprudenza to single-cycle degrees, recorded Padua's Medicine campus move to Venice, and corrected several Padua programme language/course-identity classifications. Added official programme and admission evidence for all 10 previously unlinked Federico II rows, all seven University of Florence rows, and Tor Vergata Computer Science. Corrected Florence Architecture and Urban Planning to curriculum-level records, set Urban Planning's campus to Prato, scoped the RISE English-only route as an optional pathway, corrected Tor Vergata Computer Science to Italian, and preserved 2026/27 admissions data as historical facts only. Rebuilt the 201-program dataset, 561-source inventory, report, Claude checklist and manifest; the data audit passed, all 12 static-site tests passed, the UI regression test passed after fixing proposed programme records leaking into the 'Not offered' filter, and desktop/mobile browser tests passed. No Vercel preview or production deployment was triggered while research remains partial.",
}

BATCH2 = {
    "id": "padua-2027-28-application-procedure-and-call-two-source-correction",
    "status": "partial",
    "result": "Rechecked Padua's current official application procedure in Italian. The Italian legal-language page confirms the 2027/28 open-place calls (15 Sep–15 Nov 2026; 1 Dec 2026–1 Mar 2027; 1 Apr–1 Jun 2027 for EU and non-EU residents in Italy), the separate limited-place rounds (7 Jan–7 Mar 2027 for non-EU abroad; 15 Mar–7 Apr 2027 for English programmes for EU/equated applicants), the apply.unipd.it route, €60 non-refundable fee and two-programme limit, with course-specific exceptions. Corrected the university-level source attribution to cite the Italian page; kept the English translation's erroneous Call Two start explicitly flagged. No generic application date was copied to an individual unconfirmed course or to the unapproved English Master's proposals. The official Italian URL returned HTTP 200; rebuilt the dataset with 201 programs and 562 sources; data integrity audit passed; all 12 static-site tests, the UI regression test and desktop/mobile browser tests passed. Production and preview remain untouched while the larger research audit is incomplete.",
}

BATCH3 = {
    "id": "padua-2027-28-excellence-scholarship-and-tuition-publication-status",
    "status": "partial",
    "result": "The University's Board of Administration approved €1,432,200 for the 2027/28 Padua International Excellence Scholarship edition, up to 76 awards for the top candidate per English-taught degree/curriculum (including newly activated programmes), at €8,000 gross/year plus university-fee exemption. General scheme details include max two years for Master's and three for Bachelor's/single-cycle degrees, with only regional tax and stamp duty remaining; the 2027/28 annual call, detailed selection/retention criteria and final programme allocations are still pending publication in November. Recorded the scheme as applicable to the three confirmed Padua English-taught 2027/28 candidates, and conditionally relevant to English-taught candidates whose course intake or proposal approval is pending. The latest official general tuition notice remains 2026/27; its amounts are preserved as historical only, with 2027/28 tuition still unconfirmed. All three new source URLs returned HTTP 200; rebuilt the 201-program, 565-source dataset, audit and site; data integrity passed, all 12 static tests passed, UI regression passed, and desktop/mobile browser tests passed. Production and preview remain untouched while the comprehensive research audit is incomplete.",
}

BATCH4 = {
    "id": "padua-astrophysics-cosmology-2027-28-intake-discovery",
    "status": "partial",
    "result": "Discovered and source-linked Padua's English-taught Astrophysics and Cosmology MSc, which was absent from the tracker. The current official degree profile confirms its name, LM-17 R/LM-58 R classes, two-year duration and Padua location. The Department's official page names an open first international call for AY 2027/28 (October 2027 entry), with a 15 November 2026 deadline; the deadline and route were added with an explicit scope limited to applicants with an international Bachelor's degree. Its 24-ECTS Physics and 24-ECTS Mathematics criteria are recorded as not cycle-labelled, so the 2027/28 course-specific requirements and English certificate threshold remain unconfirmed. The current Padua scholarship scheme is associated with the course but is not presented as a guaranteed award; 2027/28 tuition remains unannounced. The central degree profile returned HTTP 200. Direct HTTP and content retrieval for the Department call page were inconclusive, but official indexed results exposed its stated 2027/28 call; it remains inconclusive, not broken. The rebuilt dataset contains 202 program records and 567 sources; data audit passed, all 12 static-site tests passed, UI regression passed, and desktop/mobile browser tests passed after updating the browser test to navigate through paginated results. Production and preview remain untouched while the full research refresh continues.",
}

BATCH5 = {
    "id": "padua-course-award-cohort-scope-review",
    "status": "partial",
    "result": "Checked Padua's current official student-awards page. It lists two €11,280 Cybersecurity awards for high-achieving students in the final two years, paid in 2026/27 and 2027/28, with an 18 March 2027 deadline. Recorded this as current-student funding and explicitly excluded it from the 2027/28 incoming-cohort scholarship offer. The same page's Computer Engineering awards target students entering in 2025/26 and were not carried into the new-intake funding fields. Padua's separate University-wide International Excellence scheme remains the applicable 2027/28 headline scheme for confirmed English-taught intakes; detailed eligibility and the annual call are still pending. The official student-awards page returned HTTP 200. Rebuilt and audited the 202-program, 568-source dataset; all 12 static tests, the UI regression test and desktop/mobile browser tests passed. Production and preview remain untouched while the full research refresh continues.",
}

BATCH6 = {
    "id": "unito-economic-analysis-and-policy-epog-2027-29-intake-discovery",
    "status": "partial",
    "result": "Added UniTo's English-taught Economic Analysis and Policy LM-56 R MSc as newly discovered candidate discovered-038. The University course profile confirms its two-year degree identity and Turin location; the EPOG consortium's live 2027–2029 call and application platform confirm an active 2027/28-entry route, with applications closing 27 January 2027 at 13:00 Europe/Paris. The course is a multi-partner Erasmus Mundus joint master, and the degree-policy matrix confirms a University of Turin award only for Major A and Minor C2 pathway combinations. Recorded the 180-ECTS prior-degree threshold, 24 ECTS economics plus 6 ECTS statistics/econometrics, English C1/equivalent, statement, two references and application route. Preserved the conflict that UniTo's central course profile says 18 CFU economics + 6 statistics, while its EAP checklist and EPOG call say 24 ECTS + 6. Published EPOG scholarship terms (€1,400/month for both years and tuition/insurance coverage) and the general fee policy (€1,000/year under the stated personal-income threshold; potentially €9,600/year above it) are recorded with cycle-specific award count and 2027/28 tuition confirmation still pending. No application fee is stated in the official pages reviewed; the amount remains unverified and no standard UniTo fee was copied to the consortium route. Production and preview remain untouched while the full research audit continues.",
}

BATCH7 = {
    "id": "pisa-information-engineering-2027-28-intake-and-degree-discovery",
    "status": "partial",
    "result": "Rechecked the University of Pisa Department of Information Engineering's live foreign-qualification call. The 2027/28 call names two English-taught MScs—Computer Engineering and Artificial Intelligence and Data Engineering—so added Computer Engineering as discovered-039 and promoted the existing Artificial Intelligence and Data Engineering row from pending to confirmed for applicants with foreign degrees. Both have a 1 February 2027, 23:59 GMT deadline, tentative 12 March results, €30/application (up to two) and the applymscenglish.unipi.it route. Recorded the common three-year degree, subject preparation, mathematics, B2 English, required documents and competitive review process, with visa-specific English-certificate conditions. The current Computer Engineering and AIDE profiles preserve their separate language and track details. The call says the 2027/28 tuition schedule is expected around June 2027; MAECI and Invest Your Talent calls for 2027/28 are not yet announced, and scholarship eligibility/award terms still need verification. The older tracker Computer Science row is separate and remains correctly named: Pisa's CS Department call explicitly names that degree independently. Production and preview remain untouched while the full research audit continues.",
}

BATCH8 = {
    "id": "source-audit-alternate-http-recheck-trieste-and-naples",
    "status": "partial",
    "result": "Used an independent Windows PowerShell HTTP client with GET and Cache-Control: no-cache on sources that the Python verifier had left inconclusive. The historical Trieste 2022 DSSC call PDF returned an explicit HTTP 404 Not Found (text/html, 196 bytes); this individual URL is now marked broken, while the other historical programme and discontinuation evidence remains linked. A University of Naples Federico II Department of Economics and Statistics page returned HTTP 200 (47,855 bytes, title 'About us | Department of Economics and Statistics'), so its direct reachability is confirmed despite the local Python TLS-chain failure. The Camerino fee portal still failed TLS validation and remains inconclusive; Padua Psychology's course-list page returned HTTP 500 and remains inconclusive, not broken. The alternate client does not resolve remaining TLS, timeout or server-error cases. The review manifest now prioritizes explicit direct HTTP outcomes over an unsuccessful content-reader attempt when assigning each source's refresh_status. No cache purges, site changes, previews or deployments were made.",
}

BATCH9 = {
    "id": "bbs-professional-masters-2027-28-announcements",
    "status": "partial",
    "result": "Reviewed Bologna Business School's official English full-time catalogue and individual programme pages. Added discovered-040 Data Science and Business Analytics, discovered-041 Artificial Intelligence for Management, and discovered-042 Finance – Entrepreneurial Finance because each programme page explicitly advertises AY 2027/28 entry, four selection rounds from March through September 2027, and an October 2027 start. Recorded each as a Professional Master (First Level), not a Laurea Magistrale; the pages identify English, full-time, 12-month delivery, and collaboration with the University of Bologna. Exact application dates and the annual call are not yet published. The displayed €14,800 tuition, €60 selection fee, B2/degree/test requirements and partial scholarship schemes are recorded only as currently published, non-cycle-labelled information; 2027/28 fee, selection terms, detailed entry requirements and scholarship terms remain pending confirmation. Fresh direct PowerShell GET requests with Cache-Control: no-cache returned HTTP 200 for all three programme pages (189,124, 183,598 and 171,618 response bytes respectively).",
}

BATCH10 = {
    "id": "source-audit-alternate-http-recheck-padua-and-naples",
    "status": "partial",
    "result": "Retried nine official URLs that remained inconclusive after the independent content-reader review using Windows PowerShell Invoke-WebRequest GET with Cache-Control: no-cache. Four sources returned direct HTTP 200: the Padua School of Science How to Apply page (35,355 bytes), Molecular Biology Bachelor's admission page (54,743 bytes), English-language Master's catalogue for AY 2026/27 (66,513 bytes), and Federico II Architecture and Heritage 2024/25 regulations PDF (300,389 bytes, application/pdf). These are historical/general cycle sources and remain labelled as such; their direct reachability does not make their facts current for 2027/28. Five sources remain inconclusive: Camerino foreign-fee portal and Padua Astrophysics admissions page failed TLS validation; the Padua Psychology course index returned HTTP 500 Service unavailable; Federico II Quantum Science timed out/failed TLS; Federico II Civil and Environmental Engineering admissions failed TLS validation. None of these five is classified broken. No programme or infrastructure changes were made.",
}

BATCH11 = {
    "id": "source-audit-alt-client-camerino-and-trieste",
    "status": "partial",
    "result": "Rechecked the 11 official sources whose content had been retrieved by the Codex web reader but whose Python direct-HTTP checks remained inconclusive. Windows PowerShell Invoke-WebRequest GET with Cache-Control: no-cache returned HTTP 200 for all 10 Camerino pages/PDFs (FAQ, Master's catalogue, Computer Science, two Chemistry profiles, Mathematics and Applications, Physics, 2026/27 pre-admission page and guide, and lump-sum payment page) and Trieste's 2022 manifesto PDF. The two PDFs returned application/pdf and their first five bytes were %PDF-. Each source record now distinguishes its direct HTTP 200 result from the earlier browser-reader retrieval. These older-cycle/general pages retain their original cycle labels and are not promoted to 2027/28 evidence. The five remaining direct-HTTP-inconclusive official URLs are still not classified as broken: Camerino foreign-student fees, Padua Astrophysics admissions (TLS), Padua Psychology course index (HTTP 500), Federico II Quantum Science (TLS/timeout), and Federico II Civil and Environmental Engineering admission (TLS).",
}

BATCH12 = {
    "id": "source-audit-curl-retry-five-remaining-inconclusives",
    "status": "partial",
    "result": "Retried the five still-unresolved official URLs using curl.exe with redirect following and Cache-Control: no-cache. Padua Psychology again returned HTTP 500 (text/html; 6,306 response bytes), confirming a reproducible server-side service error rather than a broken/not-found URL. The other four requests did not reach an HTTP response: Camerino's fee portal failed certificate hostname verification (SEC_E_WRONG_PRINCIPAL), Padua Astrophysics admissions reset the connection, Federico II Quantum Science's certificate was reported revoked (CRYPT_E_REVOKED), and Federico II Civil and Environmental Engineering's certificate was expired (SEC_E_CERT_EXPIRED). All five remain inconclusive; none is marked broken. Source records preserve the latest client/method and response detail. No site, DNS, cache or deployment changes were made.",
}

BATCH13 = {
    "id": "bbs-finance-ai-and-marketing-analytics-2027-28",
    "status": "partial",
    "result": "Continued the BBS professional-master catalogue review and added discovered-043 Finance – Finance and Artificial Intelligence and discovered-044 Marketing Management – Analytics and AI for Marketing. Both official pages explicitly advertise the 2027/28 intake, four selection rounds between March and September 2027, and an October 2027 start. Finance and Artificial Intelligence is a first-level Professional Master; Analytics and AI for Marketing is a track within the Marketing Management first-level Professional Master, not a separate Laurea Magistrale. Both pages identify English-language, full-time, 12-month, 60-ECTS delivery in Bologna with the University of Bologna Department of Management (DISA). Exact dates and the annual call remain pending. The current displayed €14,800 fee, €60 application fee, B2/degree/test requirements and partial scholarship terms are explicitly kept separate from 2027/28 confirmed fields. Fresh PowerShell GET requests with Cache-Control: no-cache returned HTTP 200 for both pages (179,806 and 177,732 response bytes).",
}

BATCH14 = {
    "id": "bbs-green-management-track-2027-28-cycle-and-current-details-review",
    "status": "partial",
    "result": "Individually rechecked the existing Bologna BBS Green Management and Sustainable Businesses tracker record. Corrected its level to a first-level Professional Master track and confirmed its English delivery, 12-month/60-ECTS format and DISA collaboration. The official page currently displays an application deadline of 16 November 2026, written test on 18 November, interview on 19 November, enrollment by 1 December and January 2027 class start; it does not state the academic-year label and contains no 2027/28 text or call. Preserved those currently displayed dates, €13,800 tuition, €60 selection fee, €3,000/€5,000 partial awards, and Bachelor's/B2/test/interview requirements as current non-cycle-labelled information. Kept 2027/28 availability, exact application dates, fees, admissions requirements and scholarships pending; no current amount or deadline was carried forward. A fresh PowerShell GET with Cache-Control: no-cache returned HTTP 200 (177,197 bytes); the HTML did not contain a 2027/28 marker.",
}

BATCH15 = {
    "id": "unibo-business-analytics-curriculum-live-profile-recheck",
    "status": "partial",
    "result": "Reopened the University of Bologna's official Statistics, Economics and Business parent-degree page and its Business Analytics curriculum profile. Confirmed the current LM-82 parent degree is in Bologna, open access, with Italian/English delivery; Business Analytics is a two-year English curriculum and not a separate degree, with all curriculum courses taught in English. Fresh PowerShell GET requests with Cache-Control: no-cache returned HTTP 200 for both pages (285,258 and 298,449 bytes). Neither page contains 2027/28 admissions information, so the exact 2027/28 intake, application dates, fees and requirements remain pending. Updated the existing record with current course identity while keeping its 2027/28 availability unconfirmed and preserving the separate BBS Professional Master classification.",
}

BATCH16 = {
    "id": "unibo-artificial-intelligence-profile-and-admissions-recheck",
    "status": "partial",
    "result": "Rechecked the University of Bologna Artificial Intelligence degree profile and programme-enrolment page. The profile identifies an English-taught two-year MSc in Bologna, classes LM-18/LM-32, open access with a skills assessment, and DISI as the department. The enrolment page still links only the 2026/27 call and labels its admission requirements as a summary of that cycle; it contains no 2027/28 call or named 2027/28 intake. Current course identity is retained as 2026/27 evidence, while 2027/28 availability, dates, requirements, application fees, tuition and scholarships remain unconfirmed. Independent fresh PowerShell GETs with Cache-Control and Pragma no-cache returned HTTP 200 (304,424 and 345,713 bytes); neither response contained a 2027/28 marker.",
}

BATCH17 = {
    "id": "unibo-dhdk-profile-2026-27-call-and-next-cycle-review",
    "status": "partial",
    "result": "Rechecked the University of Bologna Digital Humanities and Digital Knowledge profile, enrolment page and official 24-page 2026/27 admission notice. Confirmed the current profile as the English-taught LM-43 MSc in Bologna, open access with an assessment, under FICLIT. The currently linked 2026/27 notice has three expired application windows (11 March–2 April, 27 April–28 May, and 10 August–3 September 2026), online interviews, results from 15 April / 10 June / 11 September respectively, and matriculation by 19 November 2026. Its historical entry requirements include a qualifying degree, 24 relevant ECTS including at least 6 in Computer Science/Data Processing Systems, English B2, and an online interview; 2026/27 tuition is €157.04 fixed plus an ISEE-variable amount with a programme-dependent maximum. The live enrolment page links only that expired call; no 2027/28 intake, dates or terms are published. Those historical details are explicitly cycle-tagged and not carried forward. Fresh no-cache PowerShell/curl GETs returned HTTP 200 for all three sources (305,142; 343,603; and 554,964 bytes).",
}

BATCH18 = {
    "id": "unibo-mechanical-engineering-for-sustainability-2026-27-call-review",
    "status": "partial",
    "result": "Rechecked the University of Bologna Mechanical Engineering for Sustainability profile, admission page, 2026/27 call and current notice board. The profile confirms the English-taught LM-33 MSc in Forlì, open access with assessment. The 2026/27 call gives three applicant-group-specific rounds, including a non-EU-abroad intake (11 December 2025–27 January 2026), a second round (2 February–1 April 2026), and a third round (1 June–10 September 2026); the call is expired. It requires relevant degrees and credits (18 ECTS mathematics/computing, 12 physics, 18 mechanical engineering), English B2, and an online preparation interview, with an interview exemption for a specified Italian L-9 Mechanical Engineering degree. The generic enrolment page additionally says Italian B2 is required, while the named 2026/27 call lists English B2 only; this discrepancy is documented as unresolved. The current notice board's 2027/28 reference is an Overseas mobility call for existing students, not new-entry admissions. Fresh no-cache GETs returned HTTP 200 for profile, admissions, call PDF and notice board; the 2027/28 intake, dates, requirements and tuition remain unconfirmed.",
}

BATCH19 = {
    "id": "unibo-clabe-2026-27-sat-call-and-next-cycle-review",
    "status": "partial",
    "result": "Rechecked the CLaBE profile, course-code page, admission page, linked English 2026/27 call and notice board. Confirmed Business and Economics (CLaBE) is a three-year English-taught Bologna BSc, L-18, prospective-student code 6609. The linked 2026/27 call has two regular SAT-selection intakes and a possible third if places remain, 177 regular seats plus 13 special-programme seats, and a non-refundable €20 fee valid across that call's intakes. The current page links only that expired 2026/27 call. The notice board's 2027/28 reference is Overseas study mobility for current students, not first-year CLaBE admission; 2027/28 intake, dates, seats, SAT thresholds, fee, tuition and aid remain unconfirmed. The PDF is an adapted English translation and states that the Italian call prevails for legal interpretation. Fresh no-cache GETs returned HTTP 200 for all five reviewed pages (283,165; 288,734; 363,283; 601,090; and 296,126 bytes).",
}

BATCH20 = {
    "id": "unibo-clef-2026-27-sat-call-extra-selection-and-next-cycle-review",
    "status": "partial",
    "result": "Rechecked CLEF's official overview, current enrolment page, notice board, 2026/27 call and separate extra-selection notice. The overview confirms a three-year English-taught Bologna L-33 bachelor's degree with restricted access; the displayed 130-place count is not cycle-labelled. The 2026/27 official call identifies course code 6646 and 130 places, two SAT rounds, a possible extra round, Digital SAT, B2 English, secondary-school eligibility and a €20 non-refundable application fee. The separate 2 September 2026 notice confirms six residual CLEF places in the extra selection. The main call prints the extra-round opening date as `03/09/206`; this apparent typo is not silently corrected, so only its clear 11 September deadline, 24 September ranking and 24 September–1 October enrolment window are recorded. The current enrolment page links only expired 2026/27 calls. A 2027/28 Overseas notice on the current notice board is student mobility, not a new-entry call. Therefore 2027/28 availability, admissions windows, SAT terms, seats, application fee, tuition and scholarship awards remain pending. Fresh no-cache GETs returned HTTP 200 for all five reviewed sources (307,062; 364,528; 295,954; 747,442; and 348,225 bytes); only the notice board contains a literal 2027/28 marker, in the mobility item.",
}

BATCH21 = {
    "id": "unibo-medicine-english-2026-27-imat-and-tuition-review",
    "status": "partial",
    "result": "Rechecked Bologna's English-taught Medicine and Surgery degree through its 2026/27 profile/catalogue, live enrolment page, official Italian IMAT call, English call summary, certificate annex, MUR decree, open-semester guidance and tuition sources. The cycle-specific entry confirms course code 6264, six-year single-cycle LM-41, Bologna, English delivery and 160 places; the call divides those places into 140 for Italian/EU/equivalent applicants and 20 for non-EU applicants resident abroad. Registration ran 26 August–9 September 2026, the IMAT was on 29 September, and national rankings/enrolment began 26 October. The test had 60 questions in 100 minutes, +1.5/−0.4/0 scoring, a 20-point threshold for the national EU/equivalent quota, and a >0 threshold for the local abroad-resident quota. The call names a qualifying secondary-school credential, optional listed English certificates (B2-level examples; English-medium schooling for at least one year is accepted), and no separate GPA threshold. It requires a test-payment contribution but gives no amount in the reviewed call, so the prior-cycle amount is unavailable. The 2026/27 maximum course contribution is €3,315 plus the €157.04 fixed fee; regional tax, stamp duty and insurance are excluded from that maximum. The current page links only expired 2026/27 material. The open-semester route is scoped to Italian-taught Medicine, while this English degree's prior-cycle call uses IMAT. No 2027/28 English intake or admissions rules are published as of 11 November 2026; availability, test dates, capacity, application fee, tuition and scholarship terms remain pending. Fresh no-cache GETs returned HTTP 200 for all eleven official sources reviewed; all PDF signatures were valid.",
}

BATCH22 = {
    "id": "unibo-italian-medicine-2026-27-open-semester-review",
    "status": "partial",
    "result": "Updated the Italian-taught Bologna Medicine and Surgery record from the 2026/27 course catalogue, current course admissions page, University open-semester guidance, the newly published 2026/27 course-specific post-semester call and MUR policy page. Confirmed course code 6733, six-year LM-41 R, Bologna, Italian and 435 catalogue places; the current detailed call divides these into 425 Italian/EU/equivalent and 10 non-EU-resident-abroad seats. Historical 2026/27 entry used Universitaly by 3 August and Bologna Student Online by 6 August, a €250 open-semester contribution, three 6-ECTS foundation subjects, 51% attendance, exams on 10 December 2026 and 11 January 2027, and a national ranking published 22 January 2027. Recorded secondary-credential and English B2 conditions, with no separate GPA minimum stated in the reviewed call. The general 2026/27 tuition table provides a €2,244 standard single-cycle maximum-contribution reference; the call says the contribution is ISEE-progressive and offsets the open-semester payment except for the €157.04 first instalment, so no total cost was inferred. The detailed call is specifically a post-semester process for the 2026/27 cohort, not a new 2027/28 intake call. No 2027/28 course intake, deadlines, fee or scholarship terms are published in the sources reviewed. Fresh no-cache GETs returned HTTP 200 for six official pages/PDFs; the admission PDF signature was valid.",
}

BATCH23 = {
    "id": "unibo-giurisprudenza-2026-27-tolc-su-review",
    "status": "partial",
    "result": "Rechecked Bologna Giurisprudenza against its current degree profile, 2026/27 catalogue entry, admission page, official annual enrollment notice, course regulation, OFA guidance and University tuition references. Confirmed a five-year Italian single-cycle Bologna degree, course code 6827, class LMG/01 R, free access with required TOLC-SU knowledge verification. The 2026/27 notice sets enrollment from 22 July to 24 September without late fee, then late-fee periods through 19 November; TOLC-SU is accepted from 1 January 2025 and should be completed by 48 hours before enrollment. A score below 20/50 assigns an OFA but does not block enrollment; the 2026/27 rule requires the alignment course and final check by 31 March 2028. The test has 50 scored questions in three sections over 100 minutes plus an optional 30-question English self-assessment; TOLC fee is paid to CISIA but no amount is stated in the University notice. The 2026/27 tuition framework is ISEE-progressive with a €157.04 fixed component and the general €2,244 single-cycle maximum-contribution reference; code 6827 is not listed separately among higher-contribution exceptions, so the value is recorded as the standard-category reference only. No separate GPA threshold is stated. No 2027/28 admissions call or terms were found; new intake, dates, TOLC conditions, fee, tuition and aid remain pending. Fresh no-cache GETs returned HTTP 200 for six official pages/PDFs, and both PDF signatures were valid.",
}

BATCH24 = {
    "id": "unibo-scienze-comunicazione-2026-27-admissions-review",
    "status": "partial",
    "result": "Reviewed Bologna Scienze della comunicazione against the 2026/27 catalogue, current course profile and admissions page, the full 2026/27 selection call, the posted extraordinary-selection notice, and the University 2026/27 tuition schedule. Confirmed course 6620: three-year Italian L-20 R bachelor's degree in Bologna, locally capped at 600 places and admitted by TOLC-SU. The 2026/27 call provided first selection (applications 3 March–29 April 2026, 13:00; ranking 15 May; enrollment 15–22 May), second selection (30 April–13 July, 13:00; ranking 22 July; enrollment 22–28 July), and an extraordinary selection for remaining seats (applications 2–11 September, 13:00; ranking 24 September; enrollment 24–29 September). The extraordinary notice listed 156 remaining seats; this is a vacancy count, not added capacity. The first round required 26/50; later rounds had no minimum admission score, while admitted second/extra-round candidates below 26/50 received an OFA due by 31 March 2028. The TOLC-SU score weights the 30 reading/Italian, 10 prior-study knowledge, and 10 logical reasoning questions equally; the extra English section does not count. The University selection contribution was €20; TOLC payment was separate through CISIA and its price is not specified in the reviewed University notice. 2026/27 tuition was ISEE-progressive with a €157.04 fixed component and a €2,040 maximum comprehensive contribution for first-cycle courses, excluding regional tax, stamp duty, and insurance; code 6620 is not among separately listed higher-contribution programmes. No separate GPA requirement appears in the call. No 2027/28 course listing or admission call was found on the reviewed pages, so availability, dates, places, thresholds, application and tuition fees, requirements, and scholarships for that cycle remain pending. Fresh no-cache GETs returned HTTP 200 for all five official pages/PDFs; both PDF signatures were valid.",
}

BATCH25 = {
    "id": "unibo-ingegneria-informatica-2026-27-admissions-review",
    "status": "partial",
        "result": "Rechecked Bologna Ingegneria informatica against its current course profile, 2026/27 catalogue, four-intake annual admission call, current linked course-specific personal-preparation guide (the PDF is not cycle-labelled), and the separate Ubiquitous Systems and Networks double-degree notice. Confirmed course 6719: two-year LM-32 in Bologna, open access without a capped cohort, with the Italian/English curricula listed by the University. The 2026/27 base call opened four application intakes from 4 June through 28 October 2026, with outcomes through 9 November and enrollment deadlines through 19 November; all application windows are closed, and the call is not next-cycle evidence. Applicants needed a first-cycle three-year degree or recognized foreign equivalent, defined curricular credits (or specified degree classes), English B2, and a positive committee assessment of personal preparation. The course guide ties assessment to final degree marks and subject-credit totals: at least 107/110 satisfies the mark route; 92–106 requires at least 60 relevant CFU with subfield minima; below 92 requires at least 90 relevant CFU with higher subfield minima. Current undergraduates needed 165 CFU and a weighted-average equivalent assessed by those criteria. Applications were submitted through Studenti Online with the required course workbook; the call does not state an application-fee amount, so none is inferred. 2026/27 tuition was ISEE-progressive with a €157.04 fixed component and a €2,550 maximum comprehensive contribution for second-cycle courses, excluding regional tax, stamp duty and insurance; code 6719 is not separately listed as a higher-contribution course. A distinct 2026/27 supplementary double-degree call limited Ubiquitous Systems and Networks to five already-admitted students, with a second year at Université Côte d’Azur; it is not the main intake process. No 2027/28 catalogue or admissions call was present in the reviewed material; availability, deadlines, curricular and language rules, fees, tuition, scholarships, and double-degree terms remain pending for that cycle. Fresh no-cache GETs returned HTTP 200 for all six official pages/PDFs, and all three PDF signatures were valid.",
}

BATCH26 = {
    "id": "sapienza-medicine-2026-27-variant-and-admissions-route-review",
    "status": "partial",
    "result": "Rechecked Sapienza Medicine against its live 2026/27 catalogue, English course profile and full English-course admission call, plus the University open-semester guidance for Italian-taught Medicine. Resolved the generic legacy label as an umbrella record with no campus/track match: the catalogue lists eight Italian-taught LM-41 variants using the open-semester route and one separate English-taught six-year course F (33454) using the admission-test route. Recorded the Italian route's Universitaly and payment dates, three 6-CFU subjects, exam/ranking structure, €250 flat semester contribution and documented ISEE/disability/aid waivers. For English F, recorded 52 EU/equivalent and 13 non-EU-abroad places, 26 August–9 September 2026 registration, 29 September test, 60-question/100-minute format, scoring and citizenship-group thresholds. The English call requires a 2026 secondary diploma (or expected in 2026), and its Universitaly test-payment amount is not stated; no application charge is inferred. The 2026/27 ordinary second contribution group is €2,924 before individual ISEE/eligibility rules, while the open-semester payment is a separate first-stage amount; regional tax and stamp duty are additional. The existing 2026/27 scholarship records are historical and the Wanted the Best scheme is not assumed to cover this single-cycle course. No 2027/28 course listing, call, deadline, fee schedule or new-entrant scholarship call was published in the reviewed pages, so availability and terms remain not yet announced and the umbrella-to-course match remains unresolved. Fresh no-cache GETs returned HTTP 200 for five official catalogue, course, admissions and PDF endpoints; the call PDF had a valid %PDF signature. No site or deployment changes were made.",
}

BATCH27 = {
    "id": "sapienza-aerospace-engineering-2026-27-tolc-i-and-next-cycle-review",
    "status": "partial",
    "result": "Rechecked Sapienza Ingegneria Aerospaziale course 33474 against its current profile, the full 2026/27 Bando 14616 PDF, the Civil and Industrial Engineering call index, the current engineering admissions/results page, and tuition and scholarship sources. Confirmed a three-year Italian L-9 bachelor's degree in Rome with restricted access. The prior-cycle call offered 250 seats: 60 in selection one; 110 plus remaining seats in selection two; 72 plus remaining seats for EU/equivalent applicants and 8 non-EU visa seats in selection three (one reserved for Marco Polo). Applications used three rounds (1–27 April, 20 May–20 July, and 31 July–7 September 2026), with the TOLC-I valid from 1 January 2025 and score thresholds of at least 18/50 in rounds one/two and above zero in round three. The 50 scored items covered mathematics, science, logic and verbal comprehension over 110 minutes, plus an unscored 30-item English section; scoring was +1/−0.25/0, highest valid attempt counted, and a score below 18/50 could assign a Mathematics OFA. The call required an upper-secondary diploma obtained or expected in 2026; non-EU applicants resident abroad requiring a study visa could apply only in round three and also needed Universitaly pre-enrolment by 30 June 2026 and Italian B2. University selection payment was €10 per selection and non-refundable; CISIA TOLC registration was a separate €35. First-round winners paid a €200 pre-enrolment contribution, subject to ISEE reductions/exemptions and credited against tuition. The 2026/27 tuition page applies an ISEE-based contribution model and 30/35/35 installment schedule; its €2,924 contribution-group total applies to second-level and single-cycle Master's degrees, so it is not applied to this BSc. The course-specific 2026/27 tuition amount was not stated in the call or tuition pages reviewed. Regional tax and stamp duty are additional. DiSCo Lazio was the competitive regional aid route; Wanted the Best is scoped to Master's entrants and is not represented as an Aerospace BSc award. The live results page says all 2026/27 places were assigned after the second scrolling. No 2027/28 new-entry call, fee schedule or incoming scholarship call is published in the official materials reviewed as of 11 November 2026. The course profile's literal 2027/28 marker concerns laboratory assignments for students already in year three. Fresh no-cache GETs returned HTTP 200 for nine official profile, call, admissions, tuition and aid pages; the admission PDF signature was valid. No preview, production or Vercel changes were made.",
}

BATCH28 = {
    "id": "sapienza-political-science-2026-27-open-access-and-next-cycle-review",
    "status": "partial",
    "result": "Rechecked Sapienza Scienze politiche e relazioni internazionali (course 33618, L-36, Rome, Italian) against its live catalogue, application page, the 2026/27 Bando 14620, Sapienza's admissions index, the non-restricted-program deadline extension, tuition pages and current scholarship inventory. The prior-cycle route requires a knowledge-verification TOLC-SU/TOLC@CASA, with a limited exemption for candidates who took TOLC-SPS in 2025; this is an open access check, not a competitive seat ranking. Recorded the original test/payment cutoff of 29 October 2026 and the later extension to 19 November, plus the original 5 November first-payment deadline and its extension to 25 November. The €10 Sapienza access contribution and separate €35 CISIA TOLC fee are distinguished. The call requires a 2026 upper-secondary diploma; non-EU applicants resident abroad needing a visa also needed Universitaly pre-enrolment by 30 June and Italian B2. TOLC-SU is 50 scored questions in 100 minutes plus an unscored 30-question English section, with +1/−0.25/0 scoring and a once-per-month retake limit. The 2026/27 call sets OFA at <=18/50 (SU) or <=12/40 (SPS); the live course-page news note references the prior 2025 call and says >=18/50 / >=12/40 avoids OFA, so the score-18 boundary is flagged as a stale-page discrepancy. Tuition follows the ISEE-based framework and 30/35/35 installment structure; the €2,821 Art. 38 amount is restricted to second-level and single-cycle degrees and is not applied to this three-year BSc. DiSCo Lazio is competitive regional aid; Wanted the Best is a Master's entrant scheme, not a BSc award. No 2027/28 course entry call, application dates, fee, tuition schedule or incoming scholarship call was present in the reviewed official material as of 11 November 2026; the absence is not treated as discontinuation. Fresh no-cache GETs returned HTTP 200 for all seven reviewed profile, application, call, index, fee and scholarship endpoints, and the call PDF signature was valid. No deployment or Vercel changes were made.",
}

SOURCES.extend([
    {
        "id": "SRC-SAPIENZA-ECFIN-PROFILE-2026",
        "university_id": "sapienza",
        "title": "Economics and Finance course profile 2026/27",
        "url": "https://corsidilaurea.uniroma1.it/en/course/34177",
        "source_type": "Official course catalogue",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The current 2026/27 catalogue identifies Economics and Finance as programme code 34177, test code 14613, a three-year Bachelor's degree in class L-33 at Sapienza's Faculty of Economics, Department of Economics and Law, taught in person in Rome. The catalogue lists Italian and English; the official course regulation specifies three Italian curricula and one fully English curriculum. This does not establish a 2027/28 intake.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.official_course_url"],
    },
    {
        "id": "SRC-SAPIENZA-ECFIN-APPLY-2026",
        "university_id": "sapienza",
        "title": "Economics and Finance enrollment page 2026/27",
        "url": "https://corsidilaurea.uniroma1.it/en/course/34177/apply",
        "source_type": "Official course application page",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The official 2026/27 apply page links the Faculty of Economics' combined admission call for the Bachelor's programmes, including Economics and Finance. It says the call governs enrollment and confirms that test results below its thresholds lead to an OFA to be completed in the first year. No 2027/28 call is shown.",
        "supports": ["program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_entrance_test", "program.application_windows_2027_2028"],
    },
    {
        "id": "SRC-SAPIENZA-ECFIN-CALL-2026",
        "university_id": "sapienza",
        "title": "Economics and Finance 2026/27 admission call (English version)",
        "url": "https://corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/14613_e_0.pdf",
        "source_type": "Official admission call PDF",
        "accessed_at": "2026-11-11",
        "cycle": "2026-2027",
        "evidence": "The 22 June 2026 call (Rector's Decree 1285/2026) covers test code 14613 and the 2026/27 Economics and Finance L-33 Bachelor's degree. It makes access open and requires a non-selective knowledge test: TOLC-E or CEnT-S, with SAT also accepted for the English curriculum. Infostud registration and the €10 contribution ran 2 July–29 October 2026; the test had to be taken by 29 October and the first tuition installment was due 1 September–5 November. The call distinguishes Italian and English curricula, requires valid English B2 evidence for the English curriculum (with listed exemptions), and sets OFA thresholds below 9/36 TOLC-E, 8 in the selected CEnT-S sections, or 960/1600 SAT. Non-EU applicants resident abroad who need a study visa require the applicable pre-acceptance/pre-enrolment steps; Universitaly deadline was 30 June 2026. These terms are prior-cycle only.",
        "supports": ["program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_program_requirements", "program.previous_cycle_entrance_test", "program.previous_cycle_language"],
    },
    {
        "id": "SRC-SAPIENZA-ECFIN-ARCHIVE-2025",
        "university_id": "sapienza",
        "title": "Economics and Finance archived course profile 2025/26",
        "url": "https://www.corsidilaurea.uniroma1.it/en/corso/2025/33438/home",
        "source_type": "Official archived course catalogue",
        "accessed_at": "2026-11-11",
        "cycle": "2025-2026",
        "evidence": "Sapienza's official 2025/26 archive identifies the same-name Economics and Finance course, code 33438, as a three-year L-33 Bachelor's degree with Italian and English curricula. The following year's current catalogue uses code 34177 for the L-33 course. These official course records contradict the previous tracker MSc label; the old classification is retained only as provenance, not as the current degree identity.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_tracker_classification_review"],
    },
])

BATCH29 = {
    "id": "sapienza-psychology-and-health-2026-27-tolc-psi-and-next-cycle-review",
    "status": "partial",
    "result": "Rechecked Sapienza Psicologia e Salute (course 33570, L-24, Rome, Italian) against its live catalogue, current application/ranking page, Bando 05429, the University admissions index, tuition pages and scholarship inventory. The 2026/27 course is restricted access: 275 places for Italian/EU/equivalent applicants plus 10 for non-EU applicants resident abroad needing a visa. Applicants took TOLC-PSI/TOLC@CASA, needed at least 23/50 to be ranked, chose this or one of three other L-24 courses as their single Infostud preference, and used the best valid test score. Applications and test preference ran 2 July–7 September 2026; the call listed rankings and payment/scorrimento deadlines through October and a vacancy process through 11 November. Recorded the 2026 diploma requirement, non-EU Universitaly deadline of 30 June and Italian B2, and separate non-refundable €10 Sapienza selection and €35 CISIA TOLC fees. The test has 50 scored items in 100 minutes plus an unranked 30-question English section; scoring is +1/−0.25/0. OFA thresholds are section-specific for Italian, mathematics and English. Sapienza's general ISEE-based fee framework applies; the call adds regional tax and €16 stamp duty, with no course-specific annual total stated. DiSCo Lazio is competitive regional aid; Wanted the Best is for Master's entrants and is not an L-24 BSc entrant award. No 2027/28 course intake call, application dates, fee, requirements, tuition schedule or incoming scholarship call appeared in the reviewed official material as of 11 November 2026; absence of the new call is not treated as discontinuation. Fresh no-cache GETs returned HTTP 200 for all seven profile, application, call, index, fee and scholarship endpoints, and the call PDF signature was valid. No deployment or Vercel changes were made.",
}

BATCH30 = {
    "id": "sapienza-engineering-computer-science-ai-and-historical-course-relationship-review",
    "status": "partial",
    "result": "Resolved the Sapienza legacy-157 ambiguity without merging it into a similarly named course. The official archive lists the 2024/25 two-year, English-taught LM-32 Engineering in Computer Science - Ingegneria Informatica (course 30430). The 2026/27 catalogue separately lists Engineering in Computer Science and Artificial Intelligence (course 33515), also LM-32 and English-taught; no official source reviewed establishes a direct successor relationship, so both records remain distinct and the older candidate's active status stays unresolved. For discovered-026/course 33515, recorded the current 2026/27 profile, the admission call's 60-ECTS curricular thresholds (24 basic sciences including 9 mathematics; 36 engineering/computing including 18 Computer Science/Information Processing Systems), B2 English, committee assessment/interview route, €10 Infostud requirement-check contribution and five applicant-category deadlines. The June 2026 MoveIN document separately records a 75/100 pre-selection GPA floor, B2 evidence, the 15 May non-EU visa pre-selection deadline and programme contact; the €30 MoveIN application charge is kept distinct from the €10 course check. Sapienza's general ISEE-based tuition and competitive scholarship context is recorded as 2026/27 only. No 2027/28 course listing, call, fee, tuition schedule or incoming scholarship call was found in the reviewed pages; no 2026/27 term is carried into the new cycle. Fresh no-cache GETs returned HTTP 200 for the profile and application page and HTTP 206 with valid PDF signatures for the course call, MoveIN requirements and 2024 archive. No production, preview, domain, cache or Vercel changes were made.",
}

BATCH31 = {
    "id": "sapienza-economics-finance-degree-identity-and-2026-27-admissions-review",
    "status": "partial",
    "result": "Rechecked legacy-158 against Sapienza's current course catalogue, 2025/26 archived profile, 2026/27 official enrollment call, international MoveIN requirements, general fee pages and scholarship sources. Corrected the old tracker MSc label: the same-name official course was a three-year L-33 Bachelor's in the 2025/26 archive (code 33438) and is listed for 2026/27 as course 34177, test code 14613, in-person in Rome. Its four curricula comprise three in Italian and one fully in English. The 2026/27 course is open access with a mandatory non-selective knowledge-verification test: TOLC-E or CEnT-S, with SAT also accepted for the English curriculum; low scores trigger first-year OFAs rather than exclusion. Recorded the 2 July–29 October Infostud/test-fee window, the €10 university contribution, conditional €35 TOLC-E fee, 1 September–5 November first tuition installment window, English B2 requirement and exceptions. For non-EU applicants abroad needing a visa, the English route also involved MoveIN pre-selection, its 2026/27 GPA/test/language criteria and separate €30 per application charge, plus Universitaly by 30 June. Corrected the tuition record: the former €2,924 figure is a second-level Master's standard and does not apply to this Bachelor's course; the applicable 2026/27 tuition is income/residence dependent and the course call does not state one course-specific amount. DiSCo is competitive regional aid; Wanted the Best is restricted to Master's entrants. No 2027/28 course listing, call, dates, fees, tuition schedule or incoming scholarship call was found, so those remain not yet announced rather than discontinued. Fresh no-cache GETs returned HTTP 200 for the live profile, enrollment page, 2025/26 archive, English admissions and fee pages, and HTTP 206 with valid PDF signatures for the course call and MoveIN requirements. No deployment or Vercel changes were made.",
}

BATCH32 = {
    "id": "padova-clinical-psychology-identity-and-2026-27-admissions-review",
    "status": "partial",
    "result": "Reviewed legacy-159 (Psicologia clinica) against Padua's current official degree profile, the 2026/27 Italian Psychology Master's call, the separate call for non-EU applicants residing abroad, the School of Psychology admissions catalogue, the general 2026/27 fee page and the regional scholarship call. Confirmed the 2026/27 course as a two-year, Italian-taught, in-person restricted-access Laurea Magistrale in LM-51 R, based in Padua, with a qualification enabling professional psychologist practice in Italy. The EU/equivalent call lists 116 places for its applicant category and the separate non-EU-abroad call lists 9 places, of which 2 are reserved for Marco Polo. For the EU/equivalent route, recorded the 15 July–1 September pre-enrolment and curricular-review windows, €30 selection contribution, up to three ordered course preferences, degree-by-30-September rule, minimum 88 M-PSI CFU with sector minima, weighted average of at least 24/30 across the best 88 relevant CFU, English B2, and the ranking formula based on M-PSI grades weighted by CFU up to 110 CFU (30L counted as 33; ties to the younger candidate). For non-EU applicants abroad, separately recorded the 7 January–7 March application window, €60 non-refundable contribution, up to two course applications, nine course places including two Marco Polo, a three-year first-cycle degree, B2 Italian and English, and committee assessment of subject background with possible video interview. Added the current 2026/27 regional scholarship as competitive aid subject to economic and merit eligibility, without presenting it as guaranteed or course-specific; general tuition remains income/residence dependent and no 2027/28 amount is carried forward. The reviewed admission page and linked calls still concern 2026/27; no 2027/28 course intake, call, places, dates, application fee, requirements, tuition schedule or scholarship call was identified. Fresh no-cache GETs returned HTTP 200 for the admissions and regional-aid pages and HTTP 206 with valid PDF signatures for both annual calls. No deployment or Vercel changes were made.",
}

SOURCE_RECHECKS = {
    "SRC-UNIBO-AI-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/artificial-intelligence/",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "137",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Artificial intelligence - Laurea Magistrale - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 304424,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell)",
        },
    },
    "SRC-UNIBO-AI-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/artificial-intelligence/how-to-enrol",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "633",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Programme enrolment: requirements, deadlines and methods — Artificial intelligence - Laurea Magistrale - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 345713,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell)",
        },
    },
    "SRC-UNIBO-DHDK-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge/",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "21",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Digital Humanities and Digital Knowledge - Laurea Magistrale - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 305142,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-DHDK-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge/how-to-enrol",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "71",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Programme enrolment: requirements, deadlines and methods — Digital Humanities and Digital Knowledge - Laurea Magistrale - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 343603,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-DHDK-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/s/3391/p/en/digital-humanities-and-digital-knowledge-dhdk/call-dhdk-2026.pdf/@@download/file/Call%20DHDK%202026.pdf",
            "content_type": "application/pdf",
            "content_length_header": None,
            "etag": None,
            "last_modified": "Fri, 20 Feb 2026 10:54:26 GMT",
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "28",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": None,
            "pdf_signature": True,
            "has_2027_marker": False,
            "bytes_read": 554964,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-MES-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "35",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Mechanical Engineering for Sustainability - Laurea Magistrale - Forlì",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 305461,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-MES-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli/how-to-enrol",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "42",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Programme enrolment: requirements, deadlines and methods — Mechanical Engineering for Sustainability - Laurea Magistrale - Forlì",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 348728,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-MES-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/s/3427/p/en/programma-enrolment-new/bando-lm-aerospace_ita_2025-26-def-1.pdf/@@download/file/Bando%20LM%20MES%2026-27_ENG.pdf",
            "content_type": "application/pdf",
            "content_length_header": None,
            "etag": None,
            "last_modified": "Mon, 15 Dec 2025 11:58:26 GMT",
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "0",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": None,
            "pdf_signature": True,
            "has_2027_marker": False,
            "bytes_read": 582032,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-MES-NOTICE-BOARD-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli/notice-board",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "101",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Notice board — Mechanical Engineering for Sustainability - Laurea Magistrale - Forlì",
            "pdf_signature": None,
            "has_2027_marker": True,
            "bytes_read": 301355,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell)",
        },
    },
}

SOURCE_RECHECKS.update({
    "SRC-UNIBO-CLABE-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/CLaBE/Presentation",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "47",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Presentation — Business and Economics - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 283165,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-CLABE-PROGRAM-CODE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/CLaBE/prospects",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "47",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Prospects — Business and Economics - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 288734,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-CLABE-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/CLaBE/how-to-enrol",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "43",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Programme enrolment: requirements, deadlines and methods — Business and Economics - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 363283,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-CLABE-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clabe/clabe-clame-call-for-applications-2025_26-1.pdf/@@download/file/CLABE-CLAME%20Call%20for%20Applications%202025_26%20(1).pdf",
            "content_type": "application/pdf",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": None,
            "age": None,
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": None,
            "pdf_signature": True,
            "has_2027_marker": True,
            "bytes_read": 601090,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
    "SRC-UNIBO-CLABE-NOTICE-BOARD-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/CLaBE/notice-board",
            "content_type": "text/html;charset=utf-8",
            "content_length_header": None,
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "3143",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Notice board — Business and Economics - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": True,
            "bytes_read": 296126,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell/curl)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-SAPIENZA-AEROSPACE-BSC-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/course/33474",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794389844-1\"", "last_modified": "Wed, 11 Nov 2026 09:37:24 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Ingegneria Aerospaziale | Course catalogue", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 21810, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/14616_bando_ici.pdf",
            "content_type": "application/pdf", "content_length_header": "608590",
            "etag": "\"9494e-64e61bacdf9a7\"", "last_modified": "Wed, 01 Apr 2026 08:18:33 GMT",
            "cache_control": None, "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": False, "bytes_read": 608590, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://ici.web.uniroma1.it/it/bandi-di-accesso-ai-corsi-di-studio-numero-programmato-aa-202627",
            "content_type": "text/html; charset=UTF-8", "content_length_header": "78290",
            "etag": "\"1794388025\"", "last_modified": "Wed, 11 Nov 2026 09:07:05 GMT",
            "cache_control": "public, max-age=10800", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "BANDI DI ACCESSO AI CORSI DI STUDIO A NUMERO PROGRAMMATO A.A. 2026/27 | Facoltà Ingegneria Civile e Industriale - ICI", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 78290, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/it/pagina/corsi-ad-accesso-programmato-delle-facolta-di-ingegneria",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794393473-1\"", "last_modified": "Wed, 11 Nov 2026 10:37:53 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Corsi ad accesso programmato delle Facoltà di Ingegneria | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 100126, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-FEES-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/tuition-fees-and-benefits",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794393528-1\"", "last_modified": "Wed, 11 Nov 2026 10:38:48 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Tuition Fees and Benefits | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 49893, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-FEE-TABLE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/node/29732",
            "content_type": "text/html; charset=utf-8", "content_length_header": "47296",
            "etag": "\"1794393487-1\"", "last_modified": "Wed, 11 Nov 2026 10:38:07 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Standard registration fee amounts | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 47296, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-WANTED-BEST-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/scholarships-meritorious-students-italian-and-international-universities",
            "content_type": "text/html; charset=utf-8", "content_length_header": "40281",
            "etag": "\"1794393654-1\"", "last_modified": "Wed, 11 Nov 2026 10:40:54 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Scholarships for Meritorious Students from Italian and International Universities | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 40281, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-DISCO-LAZIO-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://laziodisco.it/on-line-il-bando-diritto-allo-studio-2026-2027/?lang=en",
            "content_type": "text/html; charset=UTF-8", "content_length_header": None,
            "etag": None, "last_modified": None, "cache_control": None, "age": None,
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "On line il Bando diritto allo studio 2026/2027 - Lazio DiSCo", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 119124, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-SCHOLARSHIPS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/scholarships",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794393528-1\"", "last_modified": "Wed, 11 Nov 2026 10:38:48 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Scholarships | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 50499, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/it/notizia/semestre-aperto-2026-2027-i-corsi-di-medicina-e-chirurgia-e-di-odontoiatria-e-protesi",
            "content_type": "text/html; charset=utf-8", "content_length_header": "70538",
            "etag": "\"1794392250-1\"", "last_modified": "11/11/2026 10:17:30 +00:00",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Semestre aperto 2026-2027 per i corsi di Medicina e Chirurgia e di Odontoiatria e protesi dentaria in Sapienza | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 70538, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-UNIBO-COMMUNICATION-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/laurea/ScienzeComunicazione",
            "content_type": "text/html; charset=utf-8", "content_length_header": 306020,
            "etag": None, "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "275",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Scienze della comunicazione - Laurea - Bologna", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 306020, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-COMM-CATALOGUE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/studiare/lauree-e-lauree-magistrali-a-ciclo-unico/corso/2026/6620",
            "content_type": "text/html; charset=utf-8", "content_length_header": 493837,
            "etag": None, "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "445",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Scienze della comunicazione — Università di Bologna", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 493837, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-COMM-ADMISSION-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/laurea/ScienzeComunicazione/iscriversi-al-corso",
            "content_type": "text/html; charset=utf-8", "content_length_header": 367778,
            "etag": None, "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "4926",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Iscriversi al Corso: requisiti, tempi e modalità — Scienze della comunicazione - Laurea - Bologna", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 367778, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-COMM-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3391/p/it/iscriversi-11/bando-scienze-della-comunicazione-a-a-2025-2026.pdf/@@download/file/BANDO%20SCIENZE%20DELLA%20COMUNICAZIONE%2026_27%20firmato.pdf",
            "content_type": "application/pdf", "content_length_header": 1062159,
            "etag": None, "last_modified": "02/17/2026 08:44:55 +00:00", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "1620",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 1062159, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-COMM-EXTRA-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3391/p/it/iscriversi-11/avviso-selezione-straordinaria-scienze-della-comunicazione-1.pdf/@@download/file/Avviso%20selezione%20straordinaria%20SCIENZE%20DELLA%20COMUNICAZIONE.pdf",
            "content_type": "application/pdf", "content_length_header": 352704,
            "etag": None, "last_modified": "08/28/2026 07:14:48 +00:00", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "49",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 352704, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-UNIBO-CLEF-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/EconomicsFinance/overview",
            "content_type": "text/html; charset=utf-8",
            "content_length_header": "307062",
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "178",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Overview — Economics and Finance - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 307062,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-CLEF-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clef/bando-clef-etac_a-a-2026-2027.pdf/@@download/file/Bando%20CLEF%20-ETAC_a.a.%202026-2027.pdf",
            "content_type": "application/pdf",
            "content_length_header": "747442",
            "etag": None,
            "last_modified": "Mon, 09 Feb 2026 10:12:35 GMT",
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "170",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": None,
            "pdf_signature": True,
            "has_2027_marker": None,
            "bytes_read": 747442,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-CLEF-ENROLMENT-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/EconomicsFinance/how-to-enrol",
            "content_type": "text/html; charset=utf-8",
            "content_length_header": "364528",
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "66",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Programme enrolment: requirements, deadlines and methods — Economics and Finance - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": False,
            "bytes_read": 364528,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-CLEF-NOTICE-BOARD-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/1cycle/EconomicsFinance/notice-board",
            "content_type": "text/html; charset=utf-8",
            "content_length_header": "295954",
            "etag": None,
            "last_modified": None,
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "176",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": "Notice board — Economics and Finance - Laurea - Bologna",
            "pdf_signature": None,
            "has_2027_marker": True,
            "bytes_read": 295954,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-CLEF-EXTRA-INTAKE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clef/notice-of-extra-selection-process_etac-clef-2026-2027.pdf/@@download/file/Notice%20of%20extra%20selection%20process_ETAC-CLEF%202026-2027.pdf",
            "content_type": "application/pdf",
            "content_length_header": "348225",
            "etag": None,
            "last_modified": "Thu, 03 Sep 2026 06:44:35 GMT",
            "cache_control": "must-revalidate, max-age=0, s-maxage=0",
            "age": "20",
            "x_vercel_cache": None,
            "x_vercel_id": None,
            "location": None,
            "observed_title": None,
            "pdf_signature": True,
            "has_2027_marker": None,
            "bytes_read": 348225,
            "outcome": "accessible",
            "error": None,
            "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-UNIBO-MED-EN-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery/overview",
            "content_type": "text/html; charset=utf-8", "content_length_header": "302897", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "219",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Overview — Medicine and Surgery - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 302897,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-EN-CATALOGUE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/en/study/first-and-single-cycle-degree/programme/2026/6264",
            "content_type": "text/html; charset=utf-8", "content_length_header": "481678", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "266",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Medicine and Surgery — University of Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 481678,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-EN-2026-CALL": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery",
            "content_type": "text/html; charset=utf-8", "content_length_header": "304922", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "812",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Medicine and Surgery - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 304922,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-EN-ENROLMENT-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery/how-to-enrol",
            "content_type": "text/html; charset=utf-8", "content_length_header": "347549", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "57",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Programme enrolment: requirements, deadlines and methods — Medicine and Surgery - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 347549,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-EN-IT-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3317/p/en/enrolling-1/bando-medicine-and-surgery-2024-2025-1.pdf/@@download/file/BANDO%20MEDICINE%20AND%20SURGERY%20%2B%20VETERINARY%20MEDICINE%202026-2027.pdf",
            "content_type": "application/pdf", "content_length_header": "838789", "etag": None,
            "last_modified": "Mon, 17 Aug 2026 13:59:05 GMT", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "718",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": None, "bytes_read": 838789,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-EN-CALL-SUMMARY-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3317/p/en/enrolling-1/abstract-2024-2025-3.pdf/@@download/file/ABSTRACT%202026-2027%20%283%29.pdf",
            "content_type": "application/pdf", "content_length_header": "1051614", "etag": None,
            "last_modified": "Thu, 15 Oct 2026 14:57:55 GMT", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "1145",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": None, "bytes_read": 1051614,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-EN-LANGUAGE-ANNEX-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3317/p/en/enrolling-1/allegato-2-certificazioni-linguistiche.pdf/@@download/file/Allegato%202%20-%20Certificazioni%20linguistiche.pdf",
            "content_type": "application/pdf", "content_length_header": "167141", "etag": None,
            "last_modified": "Mon, 17 Aug 2026 14:03:44 GMT", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "121",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": None, "bytes_read": 167141,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-MUR-IMAT-2026-DECREE": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.mur.gov.it/it/atti-e-normativa/decreto-ministeriale-n-1005-del-06-08-2026",
            "content_type": "text/html; charset=UTF-8", "content_length_header": "194773", "etag": None,
            "last_modified": "Tue, 10 Nov 2026 15:53:54 GMT", "cache_control": "public, max-age=14400", "age": None,
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Decreto Ministeriale n. 1005 del 06-08-2026 | Ministero dell'Università e della Ricerca",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 194773,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-OPEN-SEMESTER-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/en/study/enrolment-fees-and-other-procedures/enrolment-in-combined-bachelors-and-masters-degree-programmes-in-medicine-and-surgery-dentistry-and-orthodontics%2C-veterinary-medicine",
            "content_type": "text/html; charset=utf-8", "content_length_header": "507030", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "164",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Open semester: enrolment in the degree programmes in Medicine and Surgery, Dentistry and Orthodontics, Veterinary Medicine — University of Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 507030,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-TUITION-PAGE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/lauree-e-lauree-magistrali/tasse-e-contributi",
            "content_type": "text/html; charset=utf-8", "content_length_header": "558106", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "185",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Tasse ed esenzioni: importi e scadenze — Università di Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 558106,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-TUITION-TABLE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/allegati/Tabellaimportimassimi2627.pdf/@@download/file/Tabella%20importi%20massimi%202026-2027.pdf",
            "content_type": "application/pdf", "content_length_header": "314600", "etag": None,
            "last_modified": "Fri, 08 May 2026 12:14:12 GMT", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "355",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": None, "bytes_read": 314600,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-UNIBO-MED-IT-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistralecu/MedicinaChirurgia",
            "content_type": "text/html; charset=utf-8", "content_length_header": "303139", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "299",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Medicina e chirurgia - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 303139,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-IT-ENROL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistralecu/MedicinaChirurgia/iscriversi-al-corso",
            "content_type": "text/html; charset=utf-8", "content_length_header": "334074", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "457",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Iscriversi al Corso: requisiti, tempi e modalità — Medicina e chirurgia - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 334074,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-IT-CATALOGUE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/studiare/lauree-e-lauree-magistrali-a-ciclo-unico/corso/2026/6733",
            "content_type": "text/html; charset=utf-8", "content_length_header": "495695", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "606",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Medicina e chirurgia — Università di Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 495695,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-IT-OPEN-SEMESTER-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/studiare/iscrizioni-tasse-e-altre-procedure/iscrizioni-al-semestre-aperto",
            "content_type": "text/html; charset=utf-8", "content_length_header": "505143", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "37",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Semestre aperto: iscrizioni ai corsi di laurea magistrale a ciclo unico di Medicina e Chirurgia, Odontoiatria e Protesi Dentaria, Medicina Veterinaria — Università di Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 505143,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-MED-IT-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3317/p/it/iscriversi-al-corso-requisiti-tempi-e-modalita/bando-medicina-odontoiatria-veterinaria-2026-2027.pdf/@@download/file/Bando%20medicina%2C%20odontoiatria%2C%20veterinaria%202026-2027.pdf",
            "content_type": "application/pdf", "content_length_header": "711773", "etag": None,
            "last_modified": "Thu, 05 Nov 2026 14:52:29 GMT", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "76",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 711773,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-MUR-ITALIAN-MED-OPEN-SEMESTER": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.mur.gov.it/it/aree-tematiche/universita/lofferta-formativa-titoli-rilasciati/accesso-programmato-cose",
            "content_type": "text/html; charset=UTF-8", "content_length_header": "194553", "etag": None,
            "last_modified": "Tue, 10 Nov 2026 16:28:34 GMT", "cache_control": "public, max-age=14400", "age": None,
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Accesso programmato: cos'è | Ministero dell'Università e della Ricerca",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 194553,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-UNIBO-LAW-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/esplora-il-corso",
            "content_type": "text/html; charset=utf-8", "content_length_header": "307445", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "180",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Esplora il Corso — Giurisprudenza - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 307445,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-LAW-CATALOGUE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/studiare/lauree-e-lauree-magistrali-a-ciclo-unico/corso/2026/6827",
            "content_type": "text/html; charset=utf-8", "content_length_header": "498637", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "784",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Giurisprudenza — Università di Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 498637,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-LAW-ENROLMENT-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/iscriversi-al-corso",
            "content_type": "text/html; charset=utf-8", "content_length_header": "345178", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "223",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Iscriversi al Corso: requisiti, tempi e modalità — Giurisprudenza - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 345178,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-LAW-OFA-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/ofa",
            "content_type": "text/html; charset=utf-8", "content_length_header": "288687", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "4021",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Cosa sono e come assolvere gli OFA — Giurisprudenza - Laurea Magistrale CU - Bologna",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 288687,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-GIURISPRUDENZA-REG-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/il-corso/all-e-regolamento-parte-normativa-26-27.pdf",
            "content_type": "application/pdf", "content_length_header": "588497", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "5767",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 588497,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-LAW-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3394/p/it/iscriversi-nuova-4/avviso-tolc-25-26.pdf/@@download/file/AVVISO%20IMMA%2026_27.pdf",
            "content_type": "application/pdf", "content_length_header": "741801", "etag": None,
            "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "52",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 741801,
            "outcome": "accessible", "error": None, "checked_at": "2026-11-11",
            "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})


SOURCE_RECHECKS.update({
    "SRC-UNIBO-ING-INF-MSC-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistrale/ingegneriainformatica/index.html",
            "content_type": "text/html; charset=utf-8", "content_length_header": 303946,
            "etag": None, "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "40747",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Ingegneria informatica - Laurea Magistrale - Bologna", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 303946, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-ING-INF-CATALOGUE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unibo.it/it/studiare/lauree-magistrali/corso/2026/6719",
            "content_type": "text/html; charset=utf-8", "content_length_header": 493715,
            "etag": None, "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "1768",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Ingegneria informatica — Università di Bologna", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 493715, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-ING-INF-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/magistrale/ingegneriainformatica/iscriversi-al-corso",
            "content_type": "text/html; charset=utf-8", "content_length_header": 340639,
            "etag": None, "last_modified": None, "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "3339",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Iscriversi al Corso: requisiti, tempi e modalità — Ingegneria informatica - Laurea Magistrale - Bologna", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 340639, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-ING-INF-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3387/p/it/iscriversi-nuova-13/avviso-lm-a-libero-accesso-2025-26.pdf/@@download/file/Avviso%20ammissioni%202026-2027_nuovi%20intakes.pdf",
            "content_type": "application/pdf", "content_length_header": 616454,
            "etag": None, "last_modified": "06/04/2026 07:32:13 +00:00", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "120",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 616454, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-ING-INF-ACCESS-GUIDE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3387/p/it/iscriversi-nuova-13/informativa-sulle-modalita-di-accesso.pdf/@@download/file/INFORMATIVA%20SULLE%20MODALITA%20DI%20ACCESSO.pdf",
            "content_type": "application/pdf", "content_length_header": 471943,
            "etag": None, "last_modified": "02/26/2025 15:27:36 +00:00", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "121",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 471943, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-UNIBO-ING-INF-DOUBLE-DEGREE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsi.unibo.it/s/3387/p/it/iscriversi-nuova-13/call-for-admission-to-join-the-double-degree-program.pdf/@@download/file/CALL%20FOR%20ADMISSION%20TO%20JOIN%20THE%20DOUBLE%20DEGREE%20PROGRAM.pdf",
            "content_type": "application/pdf", "content_length_header": 238447,
            "etag": None, "last_modified": "06/09/2026 10:25:44 +00:00", "cache_control": "must-revalidate, max-age=0, s-maxage=0", "age": "120",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None, "observed_title": None,
            "pdf_signature": True, "has_2027_marker": False, "bytes_read": 238447, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-SAPIENZA-MEDICINE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/solr-offerta-formativa-t?search_api_views_fulltext=Medicina+e+chirurgia",
            "content_type": "text/html; charset=utf-8", "content_length_header": 656795,
            "etag": "W/\"1794392765-1\"", "last_modified": "11/11/2026 10:26:05 +00:00",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Catalogo dei corsi di studio | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 656795, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-MEDICINE-VARIANTS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/solr-offerta-formativa-t?search_api_views_fulltext=Medicina+e+chirurgia",
            "content_type": "text/html; charset=utf-8", "content_length_header": 656795,
            "etag": "W/\"1794392765-1\"", "last_modified": "11/11/2026 10:26:05 +00:00",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Catalogo dei corsi di studio | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 656795, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/en/course/33454",
            "content_type": "text/html; charset=utf-8", "content_length_header": 20508,
            "etag": "W/\"1794390244-1\"", "last_modified": "11/11/2026 09:44:04 +00:00",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Medicine and Surgery &quot;F&quot; | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 20508, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-MEDICINE-F-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/33454_i.pdf",
            "content_type": "application/pdf", "content_length_header": 774667,
            "etag": "\"bd20b-6587616b09e56\"", "last_modified": "08/07/2026 14:47:50 +00:00",
            "cache_control": None, "age": "95", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": False, "bytes_read": 774667, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/it/notizia/semestre-aperto-2026-2027-i-corsi-di-medicina-e-chirurgia-e-di-odontoiatria-e-protesi",
            "content_type": "text/html; charset=utf-8", "content_length_header": 70538,
            "etag": "\"1794392250-1\"", "last_modified": "11/11/2026 10:17:30 +00:00",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Semestre aperto 2026-2027 per i corsi di Medicina e Chirurgia e di Odontoiatria e protesi dentaria in Sapienza | Sapienza Università di Roma",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 70538, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-SAPIENZA-POLITICAL-SCIENCE-2026": {
        "accessed_at": "2026-11-11",
        "evidence": "The live 2026/27 catalogue identifies course 33618 Scienze politiche e relazioni internazionali as a three-year L-36 Laurea in Rome, taught in Italian, with an entrance test for knowledge verification. This is the prior-cycle identity and does not confirm 2027/28 first-year intake.",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/course/33618",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794388665-1\"", "last_modified": "Wed, 11 Nov 2026 09:17:45 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Scienze politiche e relazioni internazionali | Course catalogue", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 17172, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/14620_i_0.pdf",
            "content_type": "application/pdf", "content_length_header": "552688",
            "etag": "\"86ef0-65743e8e2e683\"", "last_modified": "Thu, 23 Jul 2026 09:30:41 GMT",
            "cache_control": None, "age": "180", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": True, "bytes_read": 552688, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/it/node/534988",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794394387-1\"", "last_modified": "Wed, 11 Nov 2026 10:53:07 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Corsi di studio: ammissioni 2026-2027 | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 73364, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-POLITICAL-SCIENCE-APPLY-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/course/33618/apply",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794391640-1\"", "last_modified": "Wed, 11 Nov 2026 10:07:20 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Scienze politiche e relazioni internazionali | Course catalogue", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 17138, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-OPEN-ACCESS-DEADLINE-EXTENSION-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/tuition-fees-and-benefits",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794394387-1\"", "last_modified": "Wed, 11 Nov 2026 10:53:07 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Tuition Fees and Benefits | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 49893, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-FEES-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/tuition-fees-and-benefits",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794394387-1\"", "last_modified": "Wed, 11 Nov 2026 10:53:07 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Tuition Fees and Benefits | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 49893, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-FEE-TABLE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/node/29732",
            "content_type": "text/html; charset=utf-8", "content_length_header": "47296",
            "etag": "\"1794394388-1\"", "last_modified": "Wed, 11 Nov 2026 10:53:08 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Standard registration fee amounts | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 47296, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-SCHOLARSHIPS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/scholarships",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794394388-1\"", "last_modified": "Wed, 11 Nov 2026 10:53:08 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Scholarships | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 50499, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-SAPIENZA-PSYCHOLOGY-2026": {
        "accessed_at": "2026-11-11",
        "evidence": "The live 2026/27 catalogue identifies Psicologia e Salute (course 33570, test code 05429) as a three-year L-24 Laurea in Rome, taught in Italian, with admission-test access. This is prior-cycle evidence and does not confirm a 2027/28 first-year intake.",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/course/33570",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794393877-1\"", "last_modified": "Wed, 11 Nov 2026 10:44:37 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Psicologia e Salute | Course catalogue", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 20380, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/05429_i.pdf",
            "content_type": "application/pdf", "content_length_header": "618408",
            "etag": "\"96fa8-654ff61a40960\"", "last_modified": "Wed, 24 Jun 2026 12:54:51 GMT",
            "cache_control": None, "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": True, "bytes_read": 618408, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/it/node/534988",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794395015-1\"", "last_modified": "Wed, 11 Nov 2026 11:03:35 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Corsi di studio: ammissioni 2026-2027 | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 73364, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
    "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/it/course/33570/apply",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794394912-1\"", "last_modified": "Wed, 11 Nov 2026 11:01:52 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Psicologia e Salute | Course catalogue", "pdf_signature": None,
            "has_2027_marker": True, "bytes_read": 20788, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache (PowerShell HttpClient)",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-SAPIENZA-INGINFO-ARCHIVE-2024": {
        "accessed_at": "2026-11-11",
        "evidence": "The official 2024 archive identifies course 30430 as Engineering in Computer Science - Ingegneria Informatica, a two-year LM-32 Master's degree taught in English. The 2026/27 catalogue separately identifies course 33515 as Engineering in Computer Science and Artificial Intelligence. The reviewed official material does not establish that 33515 is the formal successor of archived course 30430; do not merge their admissions facts.",
        "url_check": {
            "http_status": 206, "effective_url": "https://corsidilaurea.uniroma1.it/sites/default/files/archive/2024/30430.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"177f4-6353a985c3dd8\"", "last_modified": "Fri, 16 May 2025 06:07:20 GMT",
            "cache_control": None, "age": "29803", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": None, "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ENGCSAI-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/en/course/33515/home",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794395711-1\"", "last_modified": "Wed, 11 Nov 2026 11:15:11 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Engineering in Computer Science and Artificial Intelligence | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 21139, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ENGCSAI-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 206, "effective_url": "https://corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/33515_e_1.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"2bf8f-65743e2c490d0\"", "last_modified": "Thu, 23 Jul 2026 09:28:59 GMT",
            "cache_control": None, "age": "565", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": None, "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 206, "effective_url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/academic_requirements_movein_2026-2027_web_20260608.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"184921-653bcdb3da29d\"", "last_modified": "Mon, 08 Jun 2026 12:07:37 GMT",
            "cache_control": None, "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": None, "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ENGCSAI-APPLY-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/en/course/33515/apply",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794394232-1\"", "last_modified": "Wed, 11 Nov 2026 10:50:32 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Engineering in Computer Science and Artificial Intelligence | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 19895, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
})

SOURCE_RECHECKS.update({
    "SRC-SAPIENZA-ECONOMICS-FINANCE-2026": {
        "accessed_at": "2026-11-11",
        "evidence": "A fresh no-cache GET of the official 2026/27 archived organization view returned the Economics and Finance catalogue record. It confirms class L-33 and the three-year Bachelor's identity; the currently served full profile and admission call are separately linked as SRC-SAPIENZA-ECFIN-PROFILE-2026 and SRC-SAPIENZA-ECFIN-CALL-2026. This source does not support the previous tracker MSc classification or a 2027/28 offer.",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/en/timeview/2026/34177/organization",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": None, "last_modified": None, "cache_control": "no-cache, must-revalidate", "age": "0",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Economics and Finance | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 41760, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ECFIN-PROFILE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/en/course/34177",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794394088-1\"", "last_modified": "Wed, 11 Nov 2026 10:48:08 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Economics and Finance | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 19784, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ECFIN-APPLY-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://corsidilaurea.uniroma1.it/en/course/34177/apply",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794392788-1\"", "last_modified": "Wed, 11 Nov 2026 10:26:28 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Economics and Finance | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 19522, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ECFIN-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 206, "effective_url": "https://corsidilaurea.uniroma1.it/sites/default/files/offertaformativa/documenti_ufficiali/187/14613_e_0.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"aecce-65743e2bf83d7\"", "last_modified": "Thu, 23 Jul 2026 09:28:58 GMT",
            "cache_control": None, "age": "304", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": None, "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ECFIN-ARCHIVE-2025": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.corsidilaurea.uniroma1.it/en/corso/2025/33438/home",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "W/\"1794396573-1\"", "last_modified": "Wed, 11 Nov 2026 11:29:33 GMT",
            "cache_control": "public, max-age=0", "age": "0", "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Economics and Finance | Course catalogue", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 16333, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026": {
        "accessed_at": "2026-11-11",
        "evidence": "The June 8, 2026 revision includes both BSc Economics and Finance and MSc Engineering in Computer Science and Artificial Intelligence among the 2026/27 English-taught programmes in MoveIN pre-selection. For Economics and Finance, the document sets an 80/100 minimum GPA, requires a SAT score of at least 960 or a positive converted CEnT-S score, and specifies English B2 with listed evidence and exemptions. For Engineering in Computer Science and AI it separately states 75/100. These are programme-specific MoveIN pre-selection criteria, not general course-admission rules; course calls govern final eligibility and enrollment. The central admissions page gives the 2026/27 MoveIN deadlines by applicant group (15 May for non-EU visa applicants and 31 July for EU/equivalent applicants). Historical evidence only.",
        "url_check": {
            "http_status": 206, "effective_url": "https://www.uniroma1.it/sites/default/files/field_file_allegati/academic_requirements_movein_2026-2027_web_20260608.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"184921-653bcdb3da29d\"", "last_modified": "Mon, 08 Jun 2026 12:07:37 GMT",
            "cache_control": None, "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": None, "pdf_signature": True,
            "has_2027_marker": None, "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/en/admissions",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794396199-1\"", "last_modified": "Wed, 11 Nov 2026 11:23:19 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Programmes in English | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 49669, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-APPLICATION-FEE-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/it/pagina/international-admissions-2026-2027",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794396208-1\"", "last_modified": "Wed, 11 Nov 2026 11:23:28 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Programmes in English | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 51191, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-FEES-2026": {
        "accessed_at": "2026-11-11",
        "evidence": "The official 2026/27 fees page describes ISEE-based reductions, three installments of 30%, 35% and 35%, and country-group fixed contributions for students with foreign tax residence. Amounts depend on course and student circumstances; it does not supply a course-specific amount for this L-33 Bachelor's course.",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/pagina/tuition-fees-and-benefits",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": "\"1794396405-1\"", "last_modified": "Wed, 11 Nov 2026 11:26:45 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Tuition Fees and Benefits | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 49893, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
    "SRC-SAPIENZA-FEE-TABLE-2026": {
        "accessed_at": "2026-11-11",
        "evidence": "Article 38's €2,821 and €2,924 standard amounts are specifically for second-level two-year, single-cycle and unified Master's degrees, not this three-year L-33 Bachelor's course. It also lists foreign-income contribution bands of €300, €700 or €1,500 by country group. Check the course and the student's residence, income and exemptions before quoting an amount.",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.uniroma1.it/en/node/29732",
            "content_type": "text/html; charset=utf-8", "content_length_header": "47296",
            "etag": "\"1794396456-1\"", "last_modified": "Wed, 11 Nov 2026 11:27:36 GMT",
            "cache_control": "public, max-age=86400", "age": None, "x_vercel_cache": None, "x_vercel_id": None,
            "location": None, "observed_title": "Standard registration fee amounts | Sapienza Università di Roma", "pdf_signature": None,
            "has_2027_marker": False, "bytes_read": 47296, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control: no-cache",
        },
    },
})


SOURCE_RECHECKS.update({
    "SRC-PADOVA-PSYCHOLOGY-MSC-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200, "effective_url": "https://www.unipd.it/ammissioni-psi-magistrali-linguaitaliana",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": None, "last_modified": None,
            "cache_control": "private, no-cache, no-store, max-age=0, must-revalidate",
            "age": None, "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": "Corsi di laurea magistrale in lingua italiana della scuola di Psicologia | Universit� di Padova",
            "pdf_signature": None, "has_2027_marker": False, "bytes_read": 131072,
            "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache",
        },
    },
    "SRC-PADOVA-PSYCHOLOGY-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 206,
            "effective_url": "https://wwwassets.unipd.it/sites/default/files/2026-07/2026_Bando_LM_PsicologiaItaliano.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"157aec-657e3349a8330\"", "last_modified": "Fri, 31 Jul 2026 07:33:31 GMT",
            "cache_control": "max-age=31536000", "age": "174811",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": None, "pdf_signature": True, "has_2027_marker": None,
            "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 206,
            "effective_url": "https://wwwassets.unipd.it/sites/default/files/pdf_imported_files/nonUE_LM%20Psicologia_0.pdf",
            "content_type": "application/pdf", "content_length_header": "4096",
            "etag": "\"71961-64ce5c44559c8\"", "last_modified": "Fri, 13 Mar 2026 10:59:44 GMT",
            "cache_control": "max-age=31536000", "age": "4384",
            "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": None, "pdf_signature": True, "has_2027_marker": None,
            "bytes_read": 4096, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with byte range and Cache-Control: no-cache",
        },
    },
    "SRC-PADOVA-REGIONAL-SCHOLARSHIP-2026": {
        "accessed_at": "2026-11-11",
        "url_check": {
            "http_status": 200,
            "effective_url": "https://www.unipd.it/servizi/supporto-studio/borse-premi-studio/borse-studio-alloggi-sussidi-straordinari",
            "content_type": "text/html; charset=utf-8", "content_length_header": None,
            "etag": None, "last_modified": None,
            "cache_control": "private, no-cache, no-store, max-age=0, must-revalidate",
            "age": None, "x_vercel_cache": None, "x_vercel_id": None, "location": None,
            "observed_title": None, "pdf_signature": None, "has_2027_marker": False,
            "bytes_read": 131072, "outcome": "accessible", "error": None,
            "checked_at": "2026-11-11", "method": "GET with Cache-Control and Pragma no-cache",
        },
    },
})


def _fact(value: Any, status: str, source_ids: list[str], notes: str | None = None) -> dict[str, Any]:
    return {"value": value, "status": status, "source_ids": source_ids, "notes": notes}


def _apply_prior_cycle_review(
    program: dict[str, Any], *, official_name: str, level: str, language: str, field: str,
    source_ids: list[str], city: str | None = None, program_type: str | None = None,
    extra_facts: dict[str, dict[str, Any]] | None = None, cycle: str = "2026-2027",
    checked_at: str = "2026-11-10",
) -> None:
    """Attach current course identity while keeping next-cycle admissions unconfirmed."""
    academic_year = cycle.replace("-", "/")
    program["program"] = official_name
    if city:
        program["city"] = city
    program["level"] = _fact(
        level, "REQUIRES_VERIFICATION", source_ids,
        f"Official course identity is confirmed for the {academic_year} catalogue; this value is not promoted to 2027/28 without a named-cycle source.",
    )
    program["language"] = _fact(
        language, "REQUIRES_VERIFICATION", source_ids,
        f"Official delivery is confirmed for the {academic_year} catalogue only; verify the 2027/28 course record.",
    )
    program["field"] = _fact(field, "REQUIRES_VERIFICATION", source_ids,
                             "Course subject identity is based on current official profile/catalogue evidence; next-cycle catalogue not yet verified.")
    program["availability_2027_2028"] = _fact(
        None, "NOT_YET_PUBLISHED", source_ids,
        f"Not yet announced for 2027/28 in the official programme/admission pages reviewed as of {checked_at}. This does not mean discontinued.",
    )
    program["overall_status"] = "REQUIRES_VERIFICATION"
    program["source_ids"] = list(dict.fromkeys(source_ids))
    program["previous_cycle_tags"] = {
        "level": level, "language": language, "field": field,
        "cycle": cycle,
        "label": f"Official course identity checked for {academic_year}; 2027/28 first-year intake and terms remain unconfirmed",
    }
    program["facts"] = {
        "previous_cycle_course_listing": _fact(
            {"academic_year": academic_year, "official_name": official_name, "level": level, "language": language,
             **({"program_type": program_type} if program_type else {})},
            "CONFIRMED", source_ids,
            f"Official course profile/catalogue evidence is cycle-scoped to {academic_year} and does not establish 2027/28 first-year admission.",
        ),
        "application_windows": _fact(
            None, "NOT_YET_PUBLISHED", source_ids,
            f"Not yet announced for 2027/28 in the official programme page reviewed as of {checked_at}; do not reuse 2026/27 dates.",
        ),
        "application_fee_2027_2028": _fact(
            None, "NOT_YET_PUBLISHED", source_ids,
            f"Not yet announced for 2027/28 in the programme-specific material reviewed as of {checked_at}; check the annual call and application portal.",
        ),
        "program_specific_requirements_2027_2028": _fact(
            None, "NOT_YET_PUBLISHED", source_ids,
            f"Not yet announced for 2027/28 in the programme-specific material reviewed as of {checked_at}; any 2026/27 criteria are historical only.",
        ),
        "tuition_2027_2028": _fact(
            None, "NOT_YET_PUBLISHED", source_ids,
            f"Not yet announced for 2027/28 in the programme-specific material reviewed as of {checked_at}; do not carry forward prior-cycle amounts.",
        ),
        "scholarships_2027_2028": _fact(
            None, "NOT_YET_PUBLISHED", source_ids,
            f"Not yet announced for 2027/28 in the programme-specific material reviewed as of {checked_at}; annual university and regional calls still need checking.",
        ),
        "acceptance_rate": _fact(
            None, "UNAVAILABLE", source_ids,
            "The reviewed official course/admission sources do not provide both applicants and admitted students; no acceptance rate is inferred.",
        ),
    }
    if extra_facts:
        program["facts"].update(extra_facts)
    program["last_checked"] = checked_at


def apply_legacy_course_reviews(programs: list[dict[str, Any]], fact: Callable[..., dict[str, Any]]) -> None:
    """Record official course-identity reviews for legacy rows that lacked source links."""
    by_id = {program["id"]: program for program in programs}
    prior = _apply_prior_cycle_review

    bologna = [
        ("legacy-019", "Artificial intelligence", "MSc", "English", "Artificial Intelligence", ["SRC-UNIBO-AI-PROFILE-2026", "SRC-UNIBO-AI-ADMISSIONS-2026"]),
        ("legacy-021", "Digital Humanities and Digital Knowledge", "MSc", "English", "Digital Humanities", ["SRC-UNIBO-DHDK-PROFILE-2026", "SRC-UNIBO-DHDK-ADMISSIONS-2026", "SRC-UNIBO-DHDK-CALL-2026"]),
        ("legacy-022", "Statistics, Economics and Business — Business Analytics curriculum", "MSc", "English", "Statistics and Business Analytics", ["SRC-UNIBO-BA-CURRICULUM-2026", "SRC-UNIBO-BA-CURRICULUM-PARENT-2026", "SRC-UNIBO-BA-BBS-2026"], "Bologna", "Curriculum within the parent MSc; not a separate degree programme"),
        ("legacy-024", "Mechanical Engineering for Sustainability", "MSc", "English", "Mechanical Engineering and Sustainability", ["SRC-UNIBO-MES-PROFILE-2026", "SRC-UNIBO-MES-ADMISSIONS-2026", "SRC-UNIBO-MES-CALL-2026", "SRC-UNIBO-MES-NOTICE-BOARD-2026"], "Forlì"),
        ("legacy-025", "Business and Economics (CLaBE)", "BSc", "English", "Business and Economics", ["SRC-UNIBO-CLABE-PROFILE-2026", "SRC-UNIBO-CLABE-PROGRAM-CODE-2026", "SRC-UNIBO-CLABE-ADMISSIONS-2026", "SRC-UNIBO-CLABE-CALL-2026", "SRC-UNIBO-CLABE-NOTICE-BOARD-2026"]),
        ("legacy-026", "Economics and Finance (CLEF)", "BSc", "English", "Economics and Finance", ["SRC-UNIBO-CLEF-PROFILE-2026", "SRC-UNIBO-CLEF-ADMISSIONS-2026", "SRC-UNIBO-CLEF-ENROLMENT-2026", "SRC-UNIBO-CLEF-NOTICE-BOARD-2026", "SRC-UNIBO-CLEF-EXTRA-INTAKE-2026"]),
        ("legacy-027", "Medicine and Surgery", "Single-cycle Master's (LM-41)", "English", "Medicine and Surgery", ["SRC-UNIBO-MED-EN-PROFILE-2026", "SRC-UNIBO-MED-EN-CATALOGUE-2026", "SRC-UNIBO-MED-EN-2026-CALL", "SRC-UNIBO-MED-EN-ENROLMENT-2026", "SRC-UNIBO-MED-EN-IT-CALL-2026", "SRC-UNIBO-MED-EN-CALL-SUMMARY-2026", "SRC-UNIBO-MED-EN-LANGUAGE-ANNEX-2026", "SRC-MUR-IMAT-2026-DECREE", "SRC-UNIBO-MED-OPEN-SEMESTER-2026", "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026"]),
        ("legacy-028", "Business Management — Green Management and Sustainable Businesses (BBS professional-master track)", "Professional Master's track", "English", "Sustainable Business and Green Management", ["SRC-UNIBO-BBS-GREEN-MGMT-2026"], "Bologna", "Professional Master's concentration; not a separate MSc/Laurea Magistrale"),
        ("legacy-147", "Ingegneria gestionale", "BSc", "Italian", "Industrial and Management Engineering", ["SRC-UNIBO-GESTIONALE-BSC-2026"]),
        ("legacy-148", "Economia e commercio", "BSc", "Italian", "Economics and Commerce", ["SRC-UNIBO-ECON-COMMERCIO-2026", "SRC-UNIBO-ECONOMIA-COMMERCIO-LOCATION-2026"], "Forlì"),
        ("legacy-149", "Medicina e chirurgia", "Single-cycle Master's (LM-41)", "Italian", "Medicine and Surgery", ["SRC-UNIBO-MED-IT-PROFILE-2026", "SRC-UNIBO-MED-IT-ENROL-2026"]),
        ("legacy-150", "Giurisprudenza", "Single-cycle Master's (LMG/01)", "Italian", "Law", ["SRC-UNIBO-LAW-2026", "SRC-UNIBO-GIURISPRUDENZA-REG-2026"]),
        ("legacy-151", "Scienze della comunicazione", "BSc", "Italian", "Communication Sciences", ["SRC-UNIBO-COMMUNICATION-2026", "SRC-UNIBO-COMM-ADMISSION-2026", "SRC-UNIBO-COMM-CATALOGUE-2026", "SRC-UNIBO-COMM-CALL-2026", "SRC-UNIBO-COMM-EXTRA-2026", "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026"]),
        ("legacy-152", "Ingegneria informatica", "MSc", "Italian and English", "Computer Engineering", ["SRC-UNIBO-ING-INF-MSC-2026", "SRC-UNIBO-ING-INF-ADMISSIONS-2026", "SRC-UNIBO-ING-INF-CATALOGUE-2026", "SRC-UNIBO-ING-INF-CALL-2026", "SRC-UNIBO-ING-INF-ACCESS-GUIDE-2026", "SRC-UNIBO-ING-INF-DOUBLE-DEGREE-2026", "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026"]),
    ]
    for item in bologna:
        pid, name, level, language, field_name, sources, *optional = item
        city = optional[0] if optional and optional[0] in {"Bologna", "Forlì"} else None
        program_type = optional[1] if optional and optional[0] in {"Bologna", "Forlì"} and len(optional) > 1 else (optional[0] if optional and optional[0] not in {"Bologna", "Forlì"} else None)
        # The two BBS records are not standard Laurea degrees and need separate status handling below.
        if pid == "legacy-023":
            continue
        prior(by_id[pid], official_name=name, level=level, language=language, field=field_name,
              source_ids=sources, city=city, program_type=program_type)

    prior(by_id["legacy-019"], official_name="Artificial intelligence", level="MSc", language="English",
          field="Artificial Intelligence", source_ids=["SRC-UNIBO-AI-PROFILE-2026", "SRC-UNIBO-AI-ADMISSIONS-2026"],
          cycle="2026-2027", checked_at="2026-11-11")

    prior(by_id["legacy-021"], official_name="Digital Humanities and Digital Knowledge", level="MSc", language="English",
          field="Digital Humanities", source_ids=["SRC-UNIBO-DHDK-PROFILE-2026", "SRC-UNIBO-DHDK-ADMISSIONS-2026", "SRC-UNIBO-DHDK-CALL-2026"],
          cycle="2026-2027", checked_at="2026-11-11")
    dhdk = by_id["legacy-021"]
    dhdk_call = "SRC-UNIBO-DHDK-CALL-2026"
    dhdk["facts"]["previous_cycle_application_windows"] = _fact(
        [
            {"intake": 1, "opening": "2026-03-11", "deadline": "2026-04-02", "results_from": "2026-04-15", "interview_window": ["2026-04-20", "2026-05-08"]},
            {"intake": 2, "opening": "2026-04-27", "deadline": "2026-05-28", "results_from": "2026-06-10", "interview_window": ["2026-06-15", "2026-07-03"]},
            {"intake": 3, "opening": "2026-08-10", "deadline": "2026-09-03", "results_from": "2026-09-11", "interview_window": ["2026-09-17", "2026-09-25"]},
        ],
        "CONFIRMED", [dhdk_call],
        "These deadlines and interview windows are from the official 2026/27 notice and are expired. The notice sets matriculation by 19 November 2026 for all three intakes. They are not 2027/28 dates.",
    )
    dhdk["facts"]["previous_cycle_program_requirements"] = _fact(
        {"qualification":"First-cycle degree or suitable foreign equivalent", "italian_degree_classes":["L-1", "L-3", "L-5", "L-8", "L-10", "L-11", "L-12", "L-15", "L-19", "L-20", "L-31", "L-42", "L-43"], "curricular_credits":"At least 24 ECTS across the listed humanities, language, cultural-heritage and computing subject areas, including at least 6 ECTS in INF/01 or ING-INF/05 for Italian degrees", "english":"CEFR B2", "assessment":"Remote oral interview on prior digital-humanities experience and compulsory/suggested readings"},
        "CONFIRMED", [dhdk_call],
        "Historical 2026/27 entry rules. Foreign degrees are assessed as equivalent; this detail must be rechecked against the forthcoming 2027/28 notice.",
    )
    dhdk["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "fixed_fee_eur":157.04, "variable_fee":"ISEE-based; maximum varies by programme", "programme_maximum_published_in_notice":False},
        "CONFIRMED", [dhdk_call],
        "Historical 2026/27 tuition framework only. The notice directs students to the annual fee page and does not state the programme-specific maximum; do not present this as 2027/28 tuition.",
    )
    dhdk["facts"]["application_fee_2026_2027"] = _fact(
        None, "UNAVAILABLE", [dhdk_call],
        "The reviewed 2026/27 admission notice does not state a programme-specific application fee; no amount is inferred.",
    )
    dhdk["last_checked"] = "2026-11-11"

    prior(by_id["legacy-024"], official_name="Mechanical Engineering for Sustainability", level="MSc", language="English",
          field="Mechanical Engineering and Sustainability", source_ids=["SRC-UNIBO-MES-PROFILE-2026", "SRC-UNIBO-MES-ADMISSIONS-2026", "SRC-UNIBO-MES-CALL-2026", "SRC-UNIBO-MES-NOTICE-BOARD-2026"],
          city="Forlì", cycle="2026-2027", checked_at="2026-11-11")
    mes = by_id["legacy-024"]
    mes_call = "SRC-UNIBO-MES-CALL-2026"
    mes_notice = "SRC-UNIBO-MES-NOTICE-BOARD-2026"
    mes["facts"]["previous_cycle_application_windows"] = _fact(
        [
            {"intake": 1, "applicant_scope":"Non-EU citizens residing abroad", "opening":"2025-12-11", "deadline":"2026-01-27 13:00 CET", "preliminary_results":"2026-02-12", "interview_window":["2026-02-16", "2026-02-19"], "final_results":"2026-03-03", "enrolment_window":["2026-03-03", "2026-04-01"]},
            {"intake": 2, "applicant_scope":"EU citizens, equivalent non-EU citizens, and non-EU citizens residing abroad", "opening":"2026-02-02", "deadline":"2026-04-01 13:00 CEST", "preliminary_results":"2026-04-14", "interview_window":["2026-04-21", "2026-04-24"], "final_results":"2026-05-05", "enrolment_window":["2026-05-05", "2026-06-01"]},
            {"intake": 3, "applicant_scope":"EU citizens, equivalent non-EU citizens, and non-EU citizens residing abroad", "opening":"2026-06-01", "deadline":"2026-09-10 13:00 CEST", "preliminary_results":"2026-09-14", "interview_window":["2026-09-16", "2026-09-18"], "final_results":"2026-09-25", "enrolment_window":["2026-09-25", "2026-11-19"]},
        ],
        "CONFIRMED", [mes_call],
        "These three rounds are from the expired 2026/27 call. They are not application windows for 2027/28.",
    )
    mes["facts"]["previous_cycle_program_requirements"] = _fact(
        {"qualification":"Bachelor's degree or equivalent foreign qualification", "eligible_italian_degree_classes":["L-9 Industrial Engineering", "L-8 Information Engineering"], "curricular_credits":{"mathematics_and_computing_ects":18,"physical_sciences_ects":12,"mechanical_engineering_ects":18}, "english":"CEFR B2", "selection":"Curriculum assessment and remote interview; the call exempts holders of a specified Italian L-9 degree titled Mechanical Engineering"},
        "CONFIRMED", [mes_call],
        "Historical requirements from the AY 2026/27 call. The admissions page lists English B2 plus Italian B2, but the named-cycle call's language section specifies English B2 only; see the explicit conflict fact. Recheck all requirements against the 2027/28 call.",
    )
    mes["facts"]["previous_cycle_language_requirement_conflict"] = _fact(
        {"current_programme_page":"Italian B2 is also required; international students who lack it must include activities to attain the level", "2026_2027_call":"Section 4.3 specifies English B2; no Italian-language requirement was found in the call"},
        "CONFLICTING_SOURCES", ["SRC-UNIBO-MES-ADMISSIONS-2026", mes_call],
        "The two official sources differ in their language requirements. The programme page is not explicitly cycle-labelled, while the call is explicitly for 2026/27. Do not resolve this discrepancy by assumption or carry either version into 2027/28.",
    )
    mes["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "fixed_fee_eur":157.04, "variable_fee":"ISEE-based; maximum varies by programme", "programme_maximum_published_in_call":False},
        "CONFIRMED", [mes_call],
        "Historical 2026/27 tuition framework only. The call points to the annual fee page and does not state this programme's maximum contribution; do not present it as 2027/28 tuition.",
    )
    mes["facts"]["application_fee_2026_2027"] = _fact(
        None, "UNAVAILABLE", [mes_call],
        "The 2026/27 admission call does not state a programme-specific application fee; no amount is inferred.",
    )
    mes["facts"]["current_notice_board_2027_2028_mobility"] = _fact(
        {"notice":"Bando Overseas – study mobility AY 2027/28", "audience":"Current first- and second-year students and graduates", "incoming_first_year_admission":False},
        "CONFIRMED", [mes_notice],
        "This 2027/28 notice concerns outgoing study mobility, not admission to the MSc for a new 2027/28 cohort. The programme admission page still links only the 2026/27 call.",
    )
    mes["last_checked"] = "2026-11-11"

    clabe_sources = ["SRC-UNIBO-CLABE-PROFILE-2026", "SRC-UNIBO-CLABE-PROGRAM-CODE-2026", "SRC-UNIBO-CLABE-ADMISSIONS-2026", "SRC-UNIBO-CLABE-CALL-2026", "SRC-UNIBO-CLABE-NOTICE-BOARD-2026"]
    prior(by_id["legacy-025"], official_name="Business and Economics (CLaBE)", level="BSc", language="English",
          field="Business and Economics", source_ids=clabe_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    clabe = by_id["legacy-025"]
    clabe_call = "SRC-UNIBO-CLABE-CALL-2026"
    clabe_notice = "SRC-UNIBO-CLABE-NOTICE-BOARD-2026"
    clabe["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Business and Economics (CLaBE)", "course_code":"6609 for prospective students", "degree_class":"L-18", "level":"BSc", "duration_years":3, "language":"English", "campus":"Bologna", "access":"Limited enrolment through SAT selection"},
        "CONFIRMED", ["SRC-UNIBO-CLABE-PROFILE-2026", "SRC-UNIBO-CLABE-PROGRAM-CODE-2026", clabe_call],
        "Course identity and selection details are for 2026/27 only and do not establish a 2027/28 first-year cohort.",
    )
    clabe["facts"]["previous_cycle_application_windows"] = _fact(
        [
            {"intake":1, "opening":"2026-02-10", "deadline":"2026-05-04 13:00 local time", "sat_score_received_by":"2026-05-04", "ranking":"2026-05-26", "enrolment_window":["2026-05-29", "2026-06-05"], "scope":"Regular first intake"},
            {"intake":2, "opening":"2026-05-05", "deadline":"2026-07-03 13:00 local time", "sat_score_received_by":"2026-07-03", "ranking":"2026-07-21", "enrolment_window":["2026-07-24", "2026-07-31"], "scope":"Regular second intake"},
            {"intake":3, "opening":"2026-09-03", "deadline":"2026-09-11 13:00 local time", "sat_score_received_by":"2026-09-11", "ranking":"2026-09-25", "enrolment_window":["2026-09-29", "2026-10-06"], "scope":"Possible extraordinary intake only if places remain"},
        ],
        "CONFIRMED", [clabe_call],
        "These dates are from the expired 2026/27 call and are not 2027/28 application dates.",
    )
    clabe["facts"]["previous_cycle_admission_requirements"] = _fact(
        {"school_qualification":"Five-year upper-secondary diploma or suitable foreign qualification after at least 12 years of schooling", "entrance_test":"Digital SAT General Test; essay is not required", "english":"At least B2; the call treats taking the SAT in English as satisfying the language requirement", "diploma_deadline":"2026-12-31"},
        "CONFIRMED", [clabe_call],
        "Historical 2026/27 entry requirements only. The English call is an adapted translation; the Italian call prevails for legal interpretation. Verify the upcoming 2027/28 call.",
    )
    clabe["facts"]["previous_cycle_available_places"] = _fact(
        {"regular_places":177, "special_programme_places":13, "total_including_special_programmes":190, "regular_intake_1":{"eu_or_equivalent":85,"non_eu_abroad":32}, "regular_intake_2":{"eu_or_equivalent":60,"plus_residual_from_intake_1":True}, "possible_intake_3":"Residual places only"},
        "CONFIRMED", [clabe_call],
        "The 177 regular positions plus 13 special-programme positions are the AY 2026/27 allocation, not a 2027/28 seat count.",
    )
    clabe["facts"]["application_fee_2026_2027"] = _fact(
        {"amount_eur":20, "refundable":False, "valid_for":"All intakes within the same 2026/27 call"},
        "CONFIRMED", [clabe_call],
        "Historical 2026/27 application fee only; do not carry it forward to 2027/28.",
    )
    clabe["facts"]["current_notice_board_2027_2028_mobility"] = _fact(
        {"notice":"Bando Overseas – study mobility AY 2027/28", "audience":"Current first- and second-year students and graduates", "incoming_first_year_admission":False},
        "CONFIRMED", [clabe_notice],
        "The 2027/28 reference concerns outgoing study mobility, not admission of new students to CLaBE. The programme admission page still links the expired 2026/27 call.",
    )
    clabe["last_checked"] = "2026-11-11"

    clef_sources = ["SRC-UNIBO-CLEF-PROFILE-2026", "SRC-UNIBO-CLEF-ADMISSIONS-2026", "SRC-UNIBO-CLEF-ENROLMENT-2026", "SRC-UNIBO-CLEF-NOTICE-BOARD-2026", "SRC-UNIBO-CLEF-EXTRA-INTAKE-2026"]
    prior(by_id["legacy-026"], official_name="Economics and Finance (CLEF)", level="BSc", language="English",
          field="Economics and Finance", source_ids=clef_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    clef = by_id["legacy-026"]
    clef_call = "SRC-UNIBO-CLEF-ADMISSIONS-2026"
    clef_enrolment = "SRC-UNIBO-CLEF-ENROLMENT-2026"
    clef_notice = "SRC-UNIBO-CLEF-NOTICE-BOARD-2026"
    clef_extra = "SRC-UNIBO-CLEF-EXTRA-INTAKE-2026"
    clef["availability_2027_2028"] = _fact(
        None, "NOT_YET_PUBLISHED", clef_sources,
        "Not yet announced for 2027/28 on the official profile or enrolment page checked 11 November 2026: the page links only expired 2026/27 calls. The 130 places shown on the profile are not labelled for 2027/28, and the notice board's 2027/28 Overseas item is student mobility, not a new-entry call. This does not mean discontinued.",
    )
    clef["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Economics and Finance (CLEF)", "course_code":"6646", "degree_class":"L-33 R", "level":"BSc", "duration_years":3, "language":"English", "campus":"Bologna", "access":"Restricted access; SAT selection", "places_in_2026_2027_call":130},
        "CONFIRMED", ["SRC-UNIBO-CLEF-PROFILE-2026", clef_call],
        "Official degree profile and named 2026/27 call evidence only. The profile's currently displayed 130 places are not independently labelled for 2027/28.",
    )
    clef["facts"]["previous_cycle_application_windows"] = _fact(
        [
            {"intake":1, "opening":"2026-02-10", "deadline":"2026-05-04 13:00 local time", "ranking":"2026-05-26", "enrolment_window":["2026-05-26", "2026-06-05"], "scope":"Ordinary first selection; official call's applicant quotas apply"},
            {"intake":2, "opening":"2026-05-05", "deadline":"2026-07-03 13:00 local time", "ranking":"2026-07-23", "enrolment_window":["2026-07-23", "2026-07-30"], "scope":"Ordinary second selection"},
            {"intake":3, "opening":None, "opening_date_as_printed":"03/09/206 (apparent typo in official call)", "deadline":"2026-09-11 13:00 local time", "ranking":"2026-09-24", "enrolment_window":["2026-09-24", "2026-10-01"], "scope":"Extra selection if places remained; official extra-selection notice dated 2026-09-02 confirms six CLEF places but gives no application opening or closing date"},
        ],
        "CONFIRMED", [clef_call, clef_extra],
        "All dates above belong to the expired 2026/27 call, not 2027/28. The main call prints the extra-selection opening date as `03/09/206`; this apparent typo is preserved and not silently corrected. The separately linked extra-selection notice confirms the 2 September notice date and six places but gives no application window.",
    )
    clef["facts"]["previous_cycle_admission_requirements"] = _fact(
        {"school_qualification":"Five-year upper-secondary diploma or qualifying foreign credential after at least twelve years of schooling; specified four-year diplomas are also eligible", "entrance_test":"Digital SAT; essay section not required; SATs from 2024-02-01 accepted under the 2026/27 call", "english":"At least B2 CEFR; assessed with the SAT, which is taken in English", "diploma_deadline":"2026-12-31", "selection":"SAT score ranking", "applicant_groups":"The call defines applicant quotas by citizenship/residence; the first selection includes a separate non-EU-resident-abroad quota, while later selection rules are call-specific"},
        "CONFIRMED", [clef_call],
        "Historical 2026/27 criteria only. Do not apply these test, quota or diploma rules to 2027/28 without the new call.",
    )
    clef["facts"]["previous_cycle_gpa_requirement"] = _fact(
        "No separate GPA threshold stated in the 2026/27 call; candidates were ranked using their Digital SAT score.",
        "CONFIRMED", [clef_call],
        "This finding is limited to the reviewed 2026/27 call and does not establish the 2027/28 selection criteria.",
    )
    clef["facts"]["previous_cycle_application_route"] = _fact(
        {"portal":"Studenti Online", "portal_url":"https://studenti.unibo.it/sol/welcome.htm?siteLanguage=en", "payment":"PagoPA", "application_fee_eur":20},
        "CONFIRMED", [clef_enrolment, clef_call],
        "Historical 2026/27 application route. The page also directs non-EU applicants to Universitaly pre-enrolment after selection where applicable; the upcoming cycle's route must be rechecked.",
    )
    clef["facts"]["previous_cycle_available_places"] = _fact(
        {"total_in_2026_2027_call":130, "first_selection":{"eu_or_equivalent":50, "non_eu_resident_abroad":40}, "second_selection":{"eu_or_equivalent":40, "plus_residual_from_first_selection":True}, "extra_selection":"Only residual seats; a separate official notice dated 2026-09-02 lists 6 CLEF places"},
        "CONFIRMED", [clef_call, clef_extra],
        "These are the 2026/27 call allocation and 2026 extra-selection vacancy count only; not 2027/28 capacity.",
    )
    clef["facts"]["previous_cycle_additional_learning_requirement"] = _fact(
        {"condition":"SAT Mathematics score below 500/800", "deadline":"2028-03-31", "consequence":"Students who do not fulfil the OFA by the deadline must repeat the first year in the following academic year"},
        "CONFIRMED", [clef_call],
        "The deadline falls in 2027/28 but applies to students admitted under the 2026/27 call; it is not evidence of a new 2027/28 incoming CLEF cohort.",
    )
    clef["facts"]["application_fee_2026_2027"] = _fact(
        {"amount_eur":20, "refundable":False, "valid_for":"Subsequent selections under the same 2026/27 call"},
        "CONFIRMED", [clef_call, clef_enrolment],
        "Historical 2026/27 application fee only; do not carry it forward to 2027/28.",
    )
    clef["facts"]["current_tuition_reference_2026_2027"] = _fact(
        {"fee_basis":"2026 ISEE; first-year students with low ISEE may receive full exemption", "standard_isee_submission_deadline":"2026-10-30 18:00", "late_submission_deadline":"2026-11-16 18:00", "late_fee_eur":100},
        "CONFIRMED", [clef_enrolment],
        "Current fee instructions displayed on the official page when checked 11 November 2026. These are not a CLEF-specific 2027/28 tuition schedule; no 2027/28 amount is published here.",
    )
    clef["facts"]["current_notice_board_2027_2028_mobility"] = _fact(
        {"notice":"Bando Overseas – study mobility AY 2027/28", "incoming_first_year_admission":False},
        "CONFIRMED", [clef_notice],
        "The 2027/28 notice-board marker is a study-mobility call for enrolled students, not CLEF first-year admission. The current enrolment page still links only expired 2026/27 admissions material.",
    )
    clef["last_checked"] = "2026-11-11"

    med_en_sources = ["SRC-UNIBO-MED-EN-PROFILE-2026", "SRC-UNIBO-MED-EN-CATALOGUE-2026", "SRC-UNIBO-MED-EN-2026-CALL", "SRC-UNIBO-MED-EN-ENROLMENT-2026", "SRC-UNIBO-MED-EN-IT-CALL-2026", "SRC-UNIBO-MED-EN-CALL-SUMMARY-2026", "SRC-UNIBO-MED-EN-LANGUAGE-ANNEX-2026", "SRC-MUR-IMAT-2026-DECREE", "SRC-UNIBO-MED-OPEN-SEMESTER-2026", "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026"]
    prior(by_id["legacy-027"], official_name="Medicine and Surgery", level="Single-cycle Master's (LM-41)", language="English",
          field="Medicine and Surgery", source_ids=med_en_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    med_en = by_id["legacy-027"]
    med_en_call = "SRC-UNIBO-MED-EN-IT-CALL-2026"
    med_en_summary = "SRC-UNIBO-MED-EN-CALL-SUMMARY-2026"
    med_en_enrolment = "SRC-UNIBO-MED-EN-ENROLMENT-2026"
    med_en_catalogue = "SRC-UNIBO-MED-EN-CATALOGUE-2026"
    med_en_language = "SRC-UNIBO-MED-EN-LANGUAGE-ANNEX-2026"
    med_en_tuition_page = "SRC-UNIBO-TUITION-PAGE-2026"
    med_en_tuition_table = "SRC-UNIBO-TUITION-TABLE-2026"
    med_en["program"] = "Medicine and Surgery"
    med_en["availability_2027_2028"] = _fact(
        None, "NOT_YET_PUBLISHED", med_en_sources,
        "Not yet announced for 2027/28 on the English programme profile or enrolment page checked 11 November 2026: the current page links only the expired 2026/27 IMAT call. The named 2026/27 course catalogue and national test decree do not confirm a 2027/28 intake or seat count. This does not mean discontinued.",
    )
    med_en["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Medicine and Surgery", "course_code":"6264", "degree_class":"LM-41 R", "level":"Single-cycle Master's (LM-41)", "duration_years":6, "language":"English", "campus":"Bologna", "access":"National restricted access", "places":160},
        "CONFIRMED", ["SRC-UNIBO-MED-EN-PROFILE-2026", med_en_catalogue],
        "Cycle-specific course identity and seat count are for 2026/27 only; they do not establish 2027/28 availability or capacity.",
    )
    med_en["facts"]["previous_cycle_application_windows"] = _fact(
        [{"route":"IMAT admission selection", "registration_portal":"Universitaly", "registration_open":"2026-08-26", "registration_deadline":"2026-09-09 15:00 Italian time", "test_date":"2026-09-29", "anonymous_score":"2026-10-08", "answers_and_scores":"2026-10-19", "ranking_and_enrolment_start":"2026-10-26", "additional_non_eu_steps":{"open":"2026-09-10", "close":"2026-10-05 13:00 Italian time", "portal":"Studenti Online"}}],
        "CONFIRMED", [med_en_call, med_en_summary],
        "All dates are from the expired 2026/27 IMAT call and must not be reused as 2027/28 dates. Non-EU candidates have additional quota-document and university-portal steps; timing and ranking route depend on EU-equivalent status or residence abroad.",
    )
    med_en["facts"]["previous_cycle_admission_requirements"] = _fact(
        {"school_qualification":"Five-year upper-secondary diploma or suitable equivalent; foreign qualifications must meet Italian university-access rules, generally after at least twelve years of schooling", "entrance_test":"International Medical Admissions Test (IMAT), administered under the 2026/27 national procedure", "selection":"National ranking for Italian/EU/EU-equivalent candidates; local University of Bologna ranking for non-EU citizens residing abroad", "non_eu_equivalent_status":"Non-EU citizens meeting the official equivalence criteria compete in the EU-equivalent quota; non-EU citizens resident abroad compete in the reserved local quota", "program_language":"English"},
        "CONFIRMED", [med_en_call, med_en_summary],
        "Historical 2026/27 requirements only. The Italian call is the legally authoritative version; non-EU categories must be checked against the official eligibility rules and the 2027/28 call.",
    )
    med_en["facts"]["previous_cycle_english_requirement"] = _fact(
        {"certificate_required_for_all_test_applicants":False, "listed_certificate_level":"B2 or higher", "examples":{"IELTS":"5.5–6.5 at B2", "TOEFL":"87–109 at B2", "Cambridge":"First (FCE) at B2", "Trinity":"ISE II at B2"}, "schooling_alternative":"At least one academic year at a school whose instruction was in English is treated as certificate possession", "role":"Optional certificate declaration in 2026/27 test registration; certificate possession is a tie-break criterion"},
        "CONFIRMED", [med_en_call, med_en_language],
        "The 2026/27 call does not state that every applicant must submit a language certificate to sit IMAT; it records possession as optional and uses it for tie-breaking. Do not turn the examples into a 2027/28 requirement.",
    )
    med_en["facts"]["previous_cycle_test_scoring"] = _fact(
        {"test":"IMAT", "question_count":60, "duration_minutes":100, "maximum_score":90, "correct_answer_points":1.5, "incorrect_answer_points":-0.4, "omitted_answer_points":0, "minimum_score_eu_or_equivalent":20, "minimum_score_non_eu_resident_abroad":">0; a completely blank test is excluded"},
        "CONFIRMED", [med_en_call, med_en_summary, "SRC-MUR-IMAT-2026-DECREE"],
        "Scoring and thresholds belong to the 2026/27 admission call only; annual ministerial rules may change.",
    )
    med_en["facts"]["previous_cycle_gpa_requirement"] = _fact(
        "No separate GPA threshold is stated in the 2026/27 call; admission ranking is based on the IMAT score and the applicable quota.",
        "CONFIRMED", [med_en_call],
        "Historical 2026/27 call only; future cycle eligibility and ranking rules must be rechecked.",
    )
    med_en["facts"]["previous_cycle_available_places"] = _fact(
        {"total":160, "italian_eu_and_non_eu_equivalent_national_quota":140, "non_eu_resident_abroad_local_quota":20},
        "CONFIRMED", [med_en_catalogue, med_en_call, "SRC-MUR-IMAT-2026-DECREE"],
        "These are 2026/27 places for course code 6264; no 2027/28 seat count is published in the reviewed material.",
    )
    med_en["facts"]["previous_cycle_application_route"] = _fact(
        {"test_registration_portal":"https://www.universitaly.it/", "test_date_location":"29 September 2026; Bologna or an approved overseas test venue", "additional_non_eu_steps":"Studenti Online from 10 September to 5 October 2026; documents and quota status depend on applicant category", "visa_pre_enrolment":"Universitaly for non-EU applicants residing abroad where applicable"},
        "CONFIRMED", [med_en_call, med_en_summary, med_en_enrolment],
        "This is the 2026/27 application route. The exact 2027/28 route and portals must be verified from the next annual call.",
    )
    med_en["facts"]["application_fee_2026_2027"] = _fact(
        {"amount_eur":None, "test_payment_required":True, "amount_stated_in_call":False},
        "UNAVAILABLE", [med_en_call, med_en_summary],
        "The 2026/27 call requires payment of an admission-test contribution but does not state its amount in the reviewed official call documents. No fee is inferred from another year or from the portal payment flow.",
    )
    med_en["facts"]["previous_cycle_additional_learning_requirement"] = _fact(
        {"condition":"An admitted candidate with a 2026/27 IMAT score below 40 may receive an OFA", "deadline":"2027-03-31", "consequence":"Candidates who do not fulfil the OFA by the deadline are enrolled as repeat first-year students"},
        "CONFIRMED", [med_en_call],
        "This condition and deadline apply to the 2026/27 admitted cohort only, not to new 2027/28 entrants.",
    )
    med_en["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "fixed_fee_eur":157.04, "maximum_comprehensive_course_contribution_eur":3315, "maximum_before_other_charges_eur":3472.04, "additional_charges_excluded_from_3315":["Regional study tax", "Stamp duty", "Insurance"], "variable_component":"Depends on ISEE/family financial situation; exemptions and reductions may apply"},
        "CONFIRMED", [med_en_tuition_page, med_en_tuition_table],
        "Historical 2026/27 tuition only. The €3,315 programme maximum is code 6264 and excludes regional tax, stamp duty and insurance; do not treat this as 2027/28 tuition.",
    )
    med_en["facts"]["previous_cycle_admissions_route_scope"] = _fact(
        {"English_taught_course":"IMAT national admission test under the 2026/27 English-course call", "Italian_taught_medicine":"Separate open-semester procedure described by University of Bologna for Italian-language courses"},
        "CONFIRMED", [med_en_call, "SRC-MUR-IMAT-2026-DECREE", "SRC-UNIBO-MED-OPEN-SEMESTER-2026"],
        "The distinction prevents applying the 2026/27 Italian-language open-semester procedure to the English-taught course. It does not predict the 2027/28 rules.",
    )
    med_en["facts"]["last_cycle_scholarships"] = _fact(
        None, "UNAVAILABLE", [med_en_enrolment],
        "The reviewed programme-specific 2026/27 admissions page does not state a dedicated programme scholarship award or amount; general University and ER.GO aid is handled through separate annual calls.",
    )
    med_en["last_checked"] = "2026-11-11"

    med_it_sources = [
        "SRC-UNIBO-MED-IT-PROFILE-2026", "SRC-UNIBO-MED-IT-CATALOGUE-2026",
        "SRC-UNIBO-MED-IT-ENROL-2026", "SRC-UNIBO-MED-IT-OPEN-SEMESTER-2026",
        "SRC-UNIBO-MED-IT-CALL-2026", "SRC-MUR-ITALIAN-MED-OPEN-SEMESTER",
        "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026",
    ]
    prior(by_id["legacy-149"], official_name="Medicina e chirurgia", level="Single-cycle Master's (LM-41)", language="Italian",
          field="Medicine and Surgery", source_ids=med_it_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    med_it = by_id["legacy-149"]
    med_it_call = "SRC-UNIBO-MED-IT-CALL-2026"
    med_it_open = "SRC-UNIBO-MED-IT-OPEN-SEMESTER-2026"
    med_it_enrolment = "SRC-UNIBO-MED-IT-ENROL-2026"
    med_it_catalogue = "SRC-UNIBO-MED-IT-CATALOGUE-2026"
    med_it["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Medicina e chirurgia", "course_code":"6733", "degree_class":"LM-41 R", "level":"Single-cycle Master's (LM-41)", "duration_years":6, "language":"Italian", "campus":"Bologna", "access":"National restricted access after the open-semester and ranking procedure", "places":435},
        "CONFIRMED", ["SRC-UNIBO-MED-IT-PROFILE-2026", med_it_catalogue, med_it_call],
        "Course identity and available seats are from the 2026/27 cycle only; they do not establish a 2027/28 first-year intake or seat count.",
    )
    med_it["facts"]["previous_cycle_available_places"] = _fact(
        {"total":435, "italian_eu_and_non_eu_equivalent":425, "non_eu_resident_abroad":10},
        "CONFIRMED", [med_it_catalogue, med_it_call],
        "The 2026/27 catalogue reports 435 places; the later course-specific call provides the 425+10 quota breakdown. These counts are historical and must not be reused for 2027/28.",
    )
    med_it["facts"]["previous_cycle_application_windows"] = _fact(
        [{"academic_year":"2026/27", "route":"Open semester, followed by national ranking", "Universitaly_deadline":"2026-08-03 18:00 Italian time", "Bologna_Studenti_Online_deadline":"2026-08-06 23:59 Italian time", "lectures":"2026-09-01 to 2026-11-18", "exam_sessions":["2026-12-10 08:00", "2027-01-11 08:00"], "ranking_publication":"2027-01-22 16:00", "first_enrolment_or_credit-recovery_window":"2027-01-22 to 2027-01-28", "additional_assignment_for_unassigned_EU_equivalent":"2027-02-02 to 2027-02-05", "later_enrolment_window":"2027-02-08 to 2027-02-10"}],
        "CONFIRMED", [med_it_open, med_it_call],
        "Every date is explicitly for the 2026/27 open-semester cohort and must not be copied into 2027/28. Later reassignments and recovery steps depend on candidate category and exam results.",
    )
    med_it["facts"]["previous_cycle_admission_requirements"] = _fact(
        {"school_qualification":"Five-year upper-secondary diploma or recognized equivalent; qualifying four-year diplomas and foreign qualifications are governed by the call's specific rules", "foreign_qualification":"Foreign upper-secondary credential after at least twelve years of schooling and valid for access to Italian higher education", "initial_subject_knowledge":["Biology", "Chemistry", "Physics", "Mathematics"], "course_language":"Italian", "attendance_requirement_for_exams":"At least 51% of the open-semester learning activities in each course, unless attendance is validated", "open_semester_attempt_limit":3, "international_language_step":"Non-EU applicants residing abroad must satisfy the Italian-language requirement before the semester starts", "english_requirement_for_medicine":"B2 English evidence is required for admission to Medicine; the 2026/27 call allows an accepted certificate or a certified prior-course English exam, with an OFA if evidence is not uploaded by the deadline"},
        "CONFIRMED", [med_it_enrolment, med_it_call],
        "These are 2026/27 requirements and entry procedures. The Italian-language open semester must not be conflated with the English-taught Medicine and Surgery IMAT route.",
    )
    med_it["facts"]["previous_cycle_test_scoring"] = _fact(
        {"exam_subjects":["Biology", "Chemistry and Biochemistry Preparation", "Physics"], "credits_per_subject":6, "questions_per_subject":31, "question_types":{"multiple_choice":21, "completion":10}, "minutes_per_subject":50, "correct_points":1, "incorrect_points":-0.1, "omitted_points":0, "pass_threshold_each_exam":18, "minimum_for_national_ranking":"At least 18/30 in one subject; the ranking has sections for passing one, two or all three subjects", "maximum_ranking_points":93},
        "CONFIRMED", [med_it_call, "SRC-UNIBO-MED-IT-OPEN-SEMESTER-2026"],
        "Exam format and ranking-score rules apply to the 2026/27 national procedure only. Progression to the second semester also requires the necessary credits under the assigned ranking section and course-call deadlines.",
    )
    med_it["facts"]["previous_cycle_application_route"] = _fact(
        {"first_step":"Register on Universitaly and select the open-semester course path and preferred universities", "Bologna_step":"Complete Bologna registration on Studenti Online and pay through PagoPA", "second_semester":"National MUR/CINECA ranking assigns the university seat; complete Bologna matriculation or credit recovery through Studenti Online", "foreign_qualification_documents":"Studenti Online documents and Universitaly visa pre-enrolment when applicable"},
        "CONFIRMED", [med_it_open, med_it_enrolment, med_it_call],
        "This is the historical 2026/27 route; the new academic-year call may change portal steps and dates.",
    )
    med_it["facts"]["previous_cycle_open_semester_contribution"] = _fact(
        {"academic_year":"2026/27", "open_semester_flat_contribution_eur":250, "payment_platform":"PagoPA", "full_exemption":{"conditions":["ISEE 2026 at or below €22,000", "specified disability certification"], "refund_if_exempt":True}, "partial_isee_reductions":{"22000.01-24000":80, "24000.01-26000":50, "26000.01-28000":25, "28000.01-30000":10}},
        "CONFIRMED", [med_it_open],
        "This is the 2026/27 open-semester contribution, not a 2027/28 application fee or the full annual tuition amount. Eligible exemptions were refunded after payment under the published process.",
    )
    med_it["facts"]["previous_cycle_gpa_requirement"] = _fact(
        "No separate school GPA threshold is stated in the 2026/27 course call; selection for second-semester seats is based on the national ranking built from the open-semester examinations and applicable quota.",
        "CONFIRMED", [med_it_call],
        "Historical 2026/27 call only; later-year selection rules must be checked in the annual call.",
    )
    med_it["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "general_single_cycle_max_comprehensive_contribution_reference_eur":2244, "course_specific_maximum_separately_listed":False, "first_installment_eur":157.04, "isee_based_progressive_contribution":True, "open_semester_contribution_offset_against_annual_contribution":True, "first_installment_still_due":True, "separate_charges_in_first_installment":["Regional study tax", "Stamp duty", "Insurance"]},
        "CONFIRMED", [med_it_call, "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026"],
        "Historical fee framework only. The €2,244 table entry is the general single-cycle reference and course code 6733 is not separately named among the table's higher-contribution exceptions; the open-semester €250 payment is offset against annual contribution except that the €157.04 first instalment remains due. Do not calculate a net total or carry amounts into 2027/28.",
    )
    med_it["facts"]["previous_cycle_admissions_route_scope"] = _fact(
        {"italian_taught_medicine":"Open semester, standardized subject examinations and national ranking from AY 2025/26 under the Italian-language system", "english_taught_medicine":"Separate national IMAT procedure in the 2026/27 call"},
        "CONFIRMED", ["SRC-MUR-ITALIAN-MED-OPEN-SEMESTER", "SRC-UNIBO-MED-IT-CALL-2026", "SRC-UNIBO-MED-EN-IT-CALL-2026"],
        "This distinguishes two separate 2026/27 routes; it does not establish 2027/28 rules.",
    )
    med_it["facts"]["last_cycle_scholarships"] = _fact(
        {"course_specific_award":None, "general_support":"The programme page directs applicants to University of Bologna and ER.GO calls for need-based aid and fee benefits"},
        "UNAVAILABLE", [med_it_enrolment, med_it_open],
        "No dedicated Medicine-course scholarship award is stated in the reviewed course call; general University and ER.GO benefit calls are separate and must be checked for the relevant year.",
    )
    med_it["last_checked"] = "2026-11-11"

    law_sources = [
        "SRC-UNIBO-LAW-2026", "SRC-UNIBO-LAW-CATALOGUE-2026", "SRC-UNIBO-LAW-ENROLMENT-2026",
        "SRC-UNIBO-LAW-ADMISSIONS-2026", "SRC-UNIBO-LAW-OFA-2026", "SRC-UNIBO-GIURISPRUDENZA-REG-2026",
        "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026",
    ]
    prior(by_id["legacy-150"], official_name="Giurisprudenza", level="Single-cycle Master's (LMG/01)", language="Italian",
          field="Law", source_ids=law_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    law = by_id["legacy-150"]
    law_admissions = "SRC-UNIBO-LAW-ADMISSIONS-2026"
    law_enrolment = "SRC-UNIBO-LAW-ENROLMENT-2026"
    law_regulation = "SRC-UNIBO-GIURISPRUDENZA-REG-2026"
    law["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Giurisprudenza", "course_code":"6827", "degree_class":"LMG/01 R", "level":"Single-cycle Master's (LMG/01)", "duration_years":5, "language":"Italian", "campus":"Bologna", "access":"Free access with TOLC-SU knowledge verification"},
        "CONFIRMED", ["SRC-UNIBO-LAW-2026", "SRC-UNIBO-LAW-CATALOGUE-2026", law_regulation],
        "These course facts apply to the 2026/27 cycle and do not establish a 2027/28 incoming cohort.",
    )
    law["facts"]["previous_cycle_application_windows"] = _fact(
        [{"academic_year":"2026/27", "test":"TOLC-SU, valid from 2025-01-01 and taken no later than 48 hours before enrollment", "enrollment_without_late_fee":"2026-07-22 to 2026-09-24", "enrollment_with_30_eur_late_fee":"2026-09-25 to 2026-10-24", "enrollment_with_150_eur_late_fee":"2026-10-25 to 2026-11-19", "international_non_eu_residing_abroad":"Meet the Italian-language requirement and complete Universitaly visa pre-enrolment where applicable"}],
        "CONFIRMED", [law_admissions, law_enrolment],
        "Dates and procedures are from the 2026/27 call only. TOLC sittings follow CISIA's calendar; the University notice says to take the test within 48 hours before enrollment and does not set a single annual test date.",
    )
    law["facts"]["previous_cycle_admission_requirements"] = _fact(
        {"school_qualification":"Upper-secondary diploma or recognized foreign equivalent; foreign qualifications must satisfy Italian university-access rules, generally after at least twelve years of schooling", "entrance_test":"TOLC-SU is required to verify initial knowledge; access is not capped", "knowledge_areas":["Italian reading comprehension and language knowledge", "Knowledge and skills acquired in prior studies", "Logical reasoning"], "separate_gpa_requirement":False, "international_non_eu_residing_abroad":"Italian-language proficiency and Universitaly pre-enrolment/visa procedure where applicable"},
        "CONFIRMED", [law_admissions, law_enrolment, law_regulation],
        "Historical 2026/27 requirements. The test is a knowledge assessment for an open-access course; a low score assigns an OFA rather than ranking applicants for a limited number of seats.",
    )
    law["facts"]["previous_cycle_test_scoring"] = _fact(
        {"test":"TOLC-SU", "scored_questions":50, "duration_minutes":100, "sections":[{"name":"Reading comprehension and Italian-language knowledge", "questions":30, "minutes":60}, {"name":"Knowledge and skills acquired in studies", "questions":10, "minutes":20}, {"name":"Logical reasoning", "questions":10, "minutes":20}], "optional_english_self_assessment":{"questions":30, "minutes":15, "counts_toward_TOLC_score":False}, "OFA_threshold":"TOLC-SU score below 20/50", "low_score_blocks_enrollment":False},
        "CONFIRMED", [law_enrolment, law_admissions, "SRC-UNIBO-LAW-OFA-2026"],
        "Format and OFA threshold are for the 2026/27 admission notice only; the optional English section is a self-assessment and does not contribute to the TOLC-SU score.",
    )
    law["facts"]["previous_cycle_additional_learning_requirement"] = _fact(
        {"trigger":"TOLC-SU below 20/50", "deadline":"2028-03-31", "procedure":"From AY 2026/27, attend the Department of Legal Sciences alignment course and pass its final assessment", "consequence_if_unfulfilled":"Repeat enrollment in the first year; second-year exams remain blocked until OFA completion"},
        "CONFIRMED", ["SRC-UNIBO-LAW-OFA-2026", law_admissions, law_regulation],
        "This is the 2026/27 Bologna rule and applies to the relevant cohort; later cohorts require a new call/regulation check.",
    )
    law["facts"]["previous_cycle_application_route"] = _fact(
        {"test_registration":"CISIA TOLC-SU calendar and registration; TOLC contribution paid through CISIA", "university_enrollment":"Studenti Online at the University of Bologna and PagoPA payment of the first tuition installment", "international_route":"Universitaly pre-enrolment for non-EU students residing abroad; University document review and Italian-language requirement"},
        "CONFIRMED", [law_admissions, law_enrolment],
        "Historical 2026/27 procedure. The next-year route, dates and platforms must be rechecked.",
    )
    law["facts"]["previous_cycle_application_fee"] = _fact(
        {"university_application_fee_amount_eur":None, "tolc_contribution_paid_to":"CISIA", "tolc_contribution_amount_stated_in_university_notice":False},
        "UNAVAILABLE", [law_admissions],
        "The 2026/27 University notice says the TOLC contribution is paid to CISIA but does not state the amount; no fee is inferred from another year or the CISIA checkout.",
    )
    law["facts"]["previous_cycle_gpa_requirement"] = _fact(
        "No separate school GPA threshold is stated in the 2026/27 call; applicants meet the diploma and TOLC-SU requirements, and a TOLC score below 20/50 results in an OFA rather than rejection for limited seats.",
        "CONFIRMED", [law_admissions, law_regulation],
        "Historical 2026/27 admission notice only.",
    )
    law["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "fixed_component_eur":157.04, "isee_progressive_variable_component":True, "general_single_cycle_max_comprehensive_contribution_reference_eur":2244, "course_code_6827_separately_listed_as_higher_contribution":False},
        "CONFIRMED", [law_admissions, law_enrolment, "SRC-UNIBO-TUITION-PAGE-2026", "SRC-UNIBO-TUITION-TABLE-2026"],
        "The €2,244 amount is the 2026/27 general single-cycle maximum-contribution reference; course 6827 is not separately listed among higher-contribution exceptions. It excludes the separate regional tax, stamp duty and insurance shown in the fee schedule. No net total or 2027/28 tuition is inferred.",
    )
    law["facts"]["last_cycle_scholarships"] = _fact(
        {"course_specific_award":None, "general_support":"University of Bologna and ER.GO publish separate annual scholarships and need-based benefits"},
        "UNAVAILABLE", [law_admissions, law_enrolment],
        "No dedicated Giurisprudenza award is stated in the reviewed course admissions sources; general University and ER.GO aid is handled through separate annual calls.",
    )
    law["last_checked"] = "2026-11-11"

    communication = by_id["legacy-151"]
    comm_profile = "SRC-UNIBO-COMMUNICATION-2026"
    comm_admissions = "SRC-UNIBO-COMM-ADMISSION-2026"
    comm_catalogue = "SRC-UNIBO-COMM-CATALOGUE-2026"
    comm_call = "SRC-UNIBO-COMM-CALL-2026"
    comm_extra = "SRC-UNIBO-COMM-EXTRA-2026"
    comm_tuition_page = "SRC-UNIBO-TUITION-PAGE-2026"
    comm_tuition_table = "SRC-UNIBO-TUITION-TABLE-2026"
    comm_sources = [comm_profile, comm_admissions, comm_catalogue, comm_call, comm_extra, comm_tuition_page, comm_tuition_table]
    prior(communication, official_name="Scienze della comunicazione", level="BSc", language="Italian",
          field="Communication Sciences", source_ids=comm_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    communication["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Scienze della comunicazione", "course_code":"6620", "degree_class":"L-20 R", "level":"Bachelor's degree", "duration_years":3, "language":"Italian", "campus":"Bologna", "access":"Locally restricted admission by TOLC-SU", "places":600},
        "CONFIRMED", [comm_catalogue, comm_profile],
        "These are the 2026/27 catalogue facts only; they do not establish that a 2027/28 cohort will be offered.",
    )
    communication["facts"]["previous_cycle_places"] = _fact(
        {"academic_year":"2026/27", "total_places":600, "first_selection_places":350, "second_selection":{"italian_eu_and_equivalent_base_places":230, "non_eu_resident_abroad_places":20, "plus_unfilled_places_from_previous_selection":True}, "extraordinary_selection_remaining_places":156, "extraordinary_places_are_additional_to_the_600_total":False},
        "CONFIRMED", [comm_catalogue, comm_call, comm_extra],
        "The 156 seats are reported by the extraordinary notice as places still available after ordinary selections; they are not additional capacity. The call splits the initial 600-seat allocation across the first and second selections and contingents.",
    )
    communication["facts"]["previous_cycle_application_windows"] = _fact(
        [
            {"selection":"First ordinary", "tolc_su_valid_from":"2025-01-01", "tolc_su_deadline":"2026-04-28", "application_open":"2026-03-03", "application_deadline":"2026-04-29T13:00", "ranking":"2026-05-15", "enrollment_window":["2026-05-15","2026-05-22"], "first_recovery_interest_window":["2026-05-15","2026-05-22"], "subsequent_recovery_publications":["2026-05-26","2026-06-04"], "final_recovery_enrollment_deadline":"2026-06-10"},
            {"selection":"Second ordinary", "tolc_su_valid_from":"2025-01-01", "tolc_su_deadline":"2026-07-10", "application_open":"2026-04-30", "application_deadline":"2026-07-13T13:00", "ranking":"2026-07-22", "enrollment_window":["2026-07-22","2026-07-28"], "recovery_interest_window":["2026-07-22","2026-07-28"], "recovery_publication":"2026-07-31", "recovery_enrollment_window":["2026-07-31","2026-08-25"]},
            {"selection":"Extraordinary", "tolc_su_valid_from":"2025-01-01", "tolc_su_deadline":"2026-09-10", "application_open":"2026-09-02", "application_deadline":"2026-09-11T13:00", "ranking":"2026-09-24", "enrollment_window":["2026-09-24","2026-09-29"], "recovery_interest_window":["2026-09-24","2026-09-29"], "recovery_publication":"2026-10-01", "recovery_enrollment_window":["2026-10-01","2026-10-07"]},
        ],
        "CONFIRMED", [comm_call, comm_extra],
        "All windows are historical AY 2026/27 dates from the expired call and its extraordinary notice. The extraordinary selection was conditional on unfilled seats. Do not reuse these dates for 2027/28.",
    )
    communication["facts"]["previous_cycle_admission_requirements"] = _fact(
        {"school_qualification":"Upper-secondary diploma or recognized equivalent; the call also allowed candidates completing the diploma by 31 December 2026 to apply", "entrance_test":"TOLC-SU required", "first_selection_minimum_score":26, "first_selection_score_denominator":50, "later_selection_minimum_score":None, "later_selection_minimum_score_required":False, "separate_gpa_requirement":False, "below_26_after_admission_in_second_or_extra_selection":"OFA assigned", "international_non_eu_residing_abroad":"Foreign qualification eligibility, Italian-language requirement and Universitaly pre-enrolment apply as specified in the annual call"},
        "CONFIRMED", [comm_call, comm_admissions, comm_extra],
        "Historical 2026/27 call rules only. Selection rounds had different score thresholds; the first-round threshold must not be generalized to the other rounds or to 2027/28.",
    )
    communication["facts"]["previous_cycle_test_scoring"] = _fact(
        {"test":"TOLC-SU", "scored_questions":50, "duration_minutes":100, "sections":[{"name":"Reading comprehension and Italian-language knowledge","questions":30,"weight":1},{"name":"Knowledge and skills acquired in studies","questions":10,"weight":1},{"name":"Logical reasoning","questions":10,"weight":1}], "additional_english_section":{"questions":30,"minutes":15,"counts_toward_ranking":False}, "scoring":{"correct":1,"incorrect":-0.25,"unanswered":0}, "ranking_order":"Descending weighted TOLC-SU score", "tie_breakers":["Higher reading-comprehension/Italian score","Younger candidate"]},
        "CONFIRMED", [comm_admissions, comm_call],
        "Format and selection scoring describe the 2026/27 TOLC-SU admission process only.",
    )
    communication["facts"]["previous_cycle_additional_learning_requirement"] = _fact(
        {"trigger":"Admission in second or extraordinary selection with TOLC-SU below 26/50", "deadline":"2028-03-31", "consequence_if_unfulfilled":"Enrollment in the first year as a repeat student"},
        "CONFIRMED", [comm_call],
        "The first selection instead required 26/50 for eligibility and did not permit enrollment below that threshold. The OFA rule applies to admitted 2026/27 candidates in later selections.",
    )
    communication["facts"]["previous_cycle_application_route"] = _fact(
        {"test_registration":"Register for TOLC-SU through CISIA; TOLC result normally transmitted to the University", "university_selection_application":"Studenti Online; University selection contribution paid through PagoPA", "international_route":"Universitaly pre-enrolment and additional qualification/Italian-language steps where applicable"},
        "CONFIRMED", [comm_admissions, comm_call],
        "Historical 2026/27 procedure. Recheck platforms and steps against the 2027/28 call.",
    )
    communication["facts"]["previous_cycle_application_fee"] = _fact(
        {"university_selection_contribution_eur":20, "payment_method":"PagoPA", "non_refundable":True, "covers_next_ordinary_and_possible_extraordinary_selection":True, "separate_cisia_tolc_fee_amount_eur":None},
        "CONFIRMED", [comm_admissions, comm_call],
        "The €20 is the 2026/27 University selection contribution, not the CISIA TOLC registration fee. The call directs TOLC payment to CISIA but does not state its amount.",
    )
    communication["facts"]["previous_cycle_gpa_requirement"] = _fact(
        {"separate_school_gpa_threshold_stated":False}, "CONFIRMED", [comm_call],
        "No separate GPA cutoff appears in the 2026/27 call; access uses the specified TOLC-SU selection thresholds and ranking rules.",
    )
    communication["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "fixed_component_eur":157.04, "isee_progressive_variable_component":True, "maximum_comprehensive_contribution_first_cycle_eur":2040, "course_code_6620_separately_listed_as_higher_contribution":False, "maximum_excludes":["Regional study tax","Stamp duty","Insurance"]},
        "CONFIRMED", [comm_call, comm_tuition_page, comm_tuition_table],
        "The official 2026/27 schedule lists a €2,040 maximum comprehensive contribution for first-cycle courses and separately lists the higher-rate exceptions; course 6620 is not among them. This is a maximum contribution reference before the excluded charges, not a promised net tuition bill. No 2027/28 amount is inferred.",
    )
    communication["facts"]["last_cycle_scholarships"] = _fact(
        {"course_specific_award":None, "general_support":"University and ER.GO benefits are handled through separate annual calls"},
        "UNAVAILABLE", [comm_call],
        "The reviewed admission call refers to general benefits but establishes no course-specific scholarship terms; 2027/28 aid remains pending.",
    )
    communication["last_checked"] = "2026-11-11"

    computer_engineering = by_id["legacy-152"]
    enginf_profile = "SRC-UNIBO-ING-INF-MSC-2026"
    enginf_admissions = "SRC-UNIBO-ING-INF-ADMISSIONS-2026"
    enginf_catalogue = "SRC-UNIBO-ING-INF-CATALOGUE-2026"
    enginf_call = "SRC-UNIBO-ING-INF-CALL-2026"
    enginf_guide = "SRC-UNIBO-ING-INF-ACCESS-GUIDE-2026"
    enginf_double = "SRC-UNIBO-ING-INF-DOUBLE-DEGREE-2026"
    enginf_tuition_page = "SRC-UNIBO-TUITION-PAGE-2026"
    enginf_tuition_table = "SRC-UNIBO-TUITION-TABLE-2026"
    enginf_sources = [enginf_profile, enginf_admissions, enginf_catalogue, enginf_call, enginf_guide, enginf_double, enginf_tuition_page, enginf_tuition_table]
    prior(computer_engineering, official_name="Ingegneria informatica", level="MSc", language="Italian and English",
          field="Computer Engineering", source_ids=enginf_sources, city="Bologna",
          cycle="2026-2027", checked_at="2026-11-11")
    computer_engineering["facts"]["previous_cycle_course_listing"] = _fact(
        {"academic_year":"2026/27", "official_name":"Ingegneria informatica", "course_code":"6719", "degree_class":"LM-32 - Computer Engineering", "level":"Master's degree", "duration_years":2, "campus":"Bologna", "languages_listed_by_university":["Italian","English"], "curricula":["Ingegneria dei sistemi informatici","Ubiquitous Systems and Networks"], "access":"Open access subject to curricular, language and personal-preparation verification", "maximum_enrollment_cap":None},
        "CONFIRMED", [enginf_catalogue, enginf_profile, enginf_call],
        "The University lists Italian and English across the degree and identifies separate curricula with separate study plans. AY 2026/27 open access means no maximum cohort size; applicants still had to pass the published eligibility checks. These facts do not establish 2027/28 availability.",
    )
    computer_engineering["facts"]["previous_cycle_places"] = _fact(
        {"academic_year":"2026/27", "access_type":"Open access", "maximum_places":None, "selection_by_ranked_limited_seats":False},
        "CONFIRMED", [enginf_call, enginf_catalogue],
        "The notice expressly says this course has no maximum enrollment for 2026/27. Admission was conditional on meeting the curricular, language and personal-preparation checks.",
    )
    computer_engineering["facts"]["previous_cycle_admission"] = _fact(
        {"academic_year":"2026/27", "access":"Open access without an enrollment cap", "process":"Four application intakes followed by committee review of qualification, curricular credits, English-language evidence and personal preparation", "standardized_entry_test":None, "passing_review_required_before_enrollment":True},
        "CONFIRMED", [enginf_call, enginf_catalogue, enginf_guide],
        "Historical 2026/27 admission process. Open access did not waive the stated eligibility and academic-preparation checks.",
    )
    computer_engineering["facts"]["previous_cycle_application_windows"] = _fact(
        [
            {"intake":1,"application_open":"2026-06-04","application_deadline":"2026-07-02T13:00","outcome_by":"2026-07-21","enrollment_window":["2026-07-28","2026-11-19"],"late_fee_applies_from":"2026-10-30","not_admitted_candidates_may_reapply_in_later_intakes":False},
            {"intake":2,"application_open":"2026-07-03","application_deadline":"2026-09-02T13:00","outcome_by":"2026-09-24","enrollment_window":["2026-10-01","2026-11-19"],"late_fee_applies_from":"2026-10-30","not_admitted_candidates_may_reapply_in_later_intakes":False},
            {"intake":3,"application_open":"2026-09-03","application_deadline":"2026-09-30T13:00","outcome_by":"2026-10-15","enrollment_window":["2026-10-22","2026-11-19"],"late_fee_applies_from":"2026-10-30","not_admitted_candidates_may_reapply_in_later_intakes":False},
            {"intake":4,"application_open":"2026-10-01","application_deadline":"2026-10-28T13:00","outcome_by":"2026-11-09","enrollment_window":["2026-11-13","2026-11-19"],"late_fee_applies_from":"2026-10-30","not_admitted_candidates_may_reapply_in_later_intakes":False},
        ],
        "CONFIRMED", [enginf_call],
        "These are the 2026/27 dates in the expired four-intake call. Application deadlines have passed; the final enrollment date listed was 19 November 2026. Do not reuse them for 2027/28.",
    )
    computer_engineering["facts"]["previous_cycle_program_requirements"] = _fact(
        {"academic_qualification":"Three-year first-cycle degree or recognized foreign equivalent", "accepted_italian_degree_classes":{"DM_270_2004":["L-8","L-31"],"DM_509_1999":["L-9","L-26"]}, "alternative_degree_credit_requirements":[{"subject_areas":["ING-INF/05","INF/01"],"minimum_cfu":36},{"subject_areas":["ING-INF/01","ING-INF/02","ING-INF/03","ING-INF/04","ING-INF/07"],"minimum_cfu":18},{"subject_areas":["MAT/02","MAT/03","MAT/05","MAT/06","MAT/07","MAT/08","MAT/09","FIS/01","FIS/03"],"minimum_cfu":24}], "foreign_degree":"Committee assesses equivalence; application includes transcript and full syllabus of exams", "undergraduate_applicant_minimum_cfu":165, "english_requirement":"B2 CEFR", "assessment":"Committee verifies personal preparation against degree-grade and subject-credit criteria", "required_preassessment_workbook":"Course-specific AccessoLM.xlsx uploaded through Studenti Online"},
        "CONFIRMED", [enginf_admissions, enginf_call, enginf_guide],
        "Historical 2026/27 requirements only. Applicants without one of the listed Italian degree classes could qualify through the stated subject-credit minima; the committee assessment remains a separate condition.",
    )
    computer_engineering["facts"]["previous_cycle_english_requirement"] = _fact(
        {"minimum_level":"B2 CEFR", "accepted_evidence":["IELTS accepted scores listed by the course","TOEFL accepted scores listed by the course","Trinity ISE II","Cambridge First Certificate","TOEIC accepted section scores listed by the course","PTE Academic accepted scores listed by the course","Curricular B2 language eligibility from CLA at Bologna or another university"]},
        "CONFIRMED", [enginf_admissions, enginf_call, enginf_guide],
        "B2 is required in the 2026/27 course admission material, even though the University catalogue lists two curricula and two languages overall. Recheck the next-cycle rule and currently accepted certificate tables.",
    )
    computer_engineering["facts"]["previous_cycle_personal_preparation"] = _fact(
        {"assessment":"Document review by a course committee", "relevant_subjects":["INF/01","ING-INF/01","ING-INF/02","ING-INF/03","ING-INF/04","ING-INF/05","ING-INF/07","ING-IND/31","ING-IND/35"], "core_subjects":["INF/01","ING-INF/05"], "degree_mark_at_least_107_of_110":"Personal-preparation requirement satisfied", "degree_mark_92_to_106_of_110":{"minimum_relevant_cfu":60,"minimum_cfu_in_core_subjects":33,"minimum_cfu_in_other_listed_technical_subjects":12,"other_listed_technical_subjects":["ING-INF/01","ING-INF/02","ING-INF/03","ING-INF/04","ING-INF/07","ING-IND/31","ING-IND/35"]}, "degree_mark_below_92_of_110":{"minimum_relevant_cfu":90,"minimum_cfu_in_core_subjects":66,"minimum_cfu_in_other_listed_technical_subjects":18,"other_listed_technical_subjects":["ING-INF/01","ING-INF/02","ING-INF/03","ING-INF/04","ING-INF/07","ING-IND/31","ING-IND/35"]}, "candidate_without_degree":{"minimum_cfu":165,"grade_basis":"Weighted-average exam mark converted to a 110-point equivalent and assessed under the same criteria"}},
        "CONFIRMED", [enginf_guide, enginf_admissions],
        "These are the published 2026/27 personal-preparation thresholds. A degree mark is part of a conditional credit-and-preparation assessment, not a stand-alone general GPA cutoff.",
    )
    computer_engineering["facts"]["previous_cycle_application_route"] = _fact(
        {"application":"Submit a separate request through Studenti Online for the selected intake", "documents":"Identity document, qualification and exams/transcript, B2 proof, and the course workbook for preliminary checking; candidates with foreign degrees upload a full exam syllabus", "international_non_eu_residing_abroad":"Universitaly pre-enrolment and study visa steps apply", "committee_result":"Published to the applicant in Studenti Online"},
        "CONFIRMED", [enginf_admissions, enginf_call, enginf_guide],
        "Historical AY 2026/27 route; the admission notice says incomplete mandatory uploads can exclude an application. Recheck the next cycle's portal and document list.",
    )
    computer_engineering["facts"]["previous_cycle_application_fee"] = _fact(
        {"application_fee_amount_eur":None, "fee_amount_stated_in_reviewed_2026_27_call":False},
        "UNAVAILABLE", [enginf_call],
        "The multi-course 2026/27 notice reviewed describes submitting the application but does not state a selection-fee amount. No zero-fee assumption is made.",
    )
    computer_engineering["facts"]["previous_cycle_gpa_requirement"] = _fact(
        {"standalone_gpa_cutoff":False, "personal_preparation_uses_degree_mark_and_credit_thresholds":True, "degree_mark_bands":{"at_least_107_of_110":"Pass mark route", "92_to_106_of_110":"Pass only with at least 60 specified CFU and subfield minima", "below_92_of_110":"Pass only with at least 90 specified CFU and subfield minima"}},
        "CONFIRMED", [enginf_guide],
        "The course uses final-degree-mark bands combined with curricular credit totals to verify preparation; these are not an independent GPA ranking threshold.",
    )
    computer_engineering["facts"]["previous_cycle_tuition"] = _fact(
        {"academic_year":"2026/27", "fixed_component_eur":157.04, "isee_progressive_variable_component":True, "maximum_comprehensive_contribution_second_cycle_eur":2550, "course_code_6719_separately_listed_as_higher_contribution":False, "maximum_excludes":["Regional study tax","Stamp duty","Insurance"]},
        "CONFIRMED", [enginf_call, enginf_tuition_page, enginf_tuition_table],
        "The official 2026/27 schedule gives €2,550 as the ordinary maximum comprehensive contribution for second-cycle courses and separately lists higher-rate exceptions; code 6719 is not among them. This is a maximum before the excluded charges, not a guaranteed net fee. No 2027/28 amount is inferred.",
    )
    computer_engineering["facts"]["previous_cycle_double_degree"] = _fact(
        {"academic_year":"2026/27", "curriculum":"Ubiquitous Systems and Networks", "partner":"Université Côte d’Azur", "maximum_places":5, "eligible_applicants":"Students already admitted to course 6719 in intake 1 or 2", "application_window":["2026-07-23","2026-09-16T12:00"], "results_date":"2026-09-23", "selection_criteria":["Bachelor's (and Master's, if held) CGPA","ECTS count","Final degree mark","Length of previous career versus standard duration"], "mobility_requirement":"Spend second year in Nice; complete 60 ECTS of year-1 exams by the September 2026 exam session before departure"},
        "CONFIRMED", [enginf_double],
        "This was a separate 2026/27 selection after admission to the LM-32; it did not replace the general course admission procedure and does not establish next-cycle double-degree availability.",
    )
    computer_engineering["facts"]["last_cycle_scholarships"] = _fact(
        {"course_specific_award":None, "general_support":"University and ER.GO scholarships and benefits are handled through separate annual calls"},
        "UNAVAILABLE", [enginf_call],
        "The reviewed general admission notice points to separate ER.GO and University benefit procedures but does not establish a course-specific 2026/27 award amount.",
    )
    computer_engineering["last_checked"] = "2026-11-11"

    business_analytics = by_id["legacy-022"]
    business_analytics_sources = ["SRC-UNIBO-BA-CURRICULUM-2026", "SRC-UNIBO-BA-CURRICULUM-PARENT-2026", "SRC-UNIBO-BA-BBS-2026"]
    business_analytics["level"] = _fact("MSc", "CONFIRMED", business_analytics_sources, "Business Analytics is a curriculum within the LM-82 Statistics, Economics and Business MSc; it is not a separate degree programme.")
    business_analytics["language"] = _fact("English", "CONFIRMED", business_analytics_sources, "The current official curriculum profile says all courses in Business Analytics are taught in English.")
    business_analytics["field"] = _fact("Statistics and Business Analytics", "CONFIRMED", business_analytics_sources)
    business_analytics["availability_2027_2028"] = _fact(None, "NOT_YET_PUBLISHED", business_analytics_sources, "The current parent and curriculum profiles, checked 11 November 2026, contain no 2027/28 marker or course-specific admission call. This does not mean the curriculum is discontinued.")
    business_analytics["overall_status"] = "REQUIRES_VERIFICATION"
    business_analytics["source_ids"] = business_analytics_sources
    business_analytics["previous_cycle_tags"] = None
    business_analytics["facts"]["current_course_identity"] = _fact({"parent_degree":"Statistics, Economics and Business", "degree_class":"LM-82 - Statistics", "course_type":"Business Analytics curriculum; not a separate degree", "campus":"Bologna", "curriculum_language":"English", "parent_degree_languages":["Italian","English"], "curriculum_duration_years":2, "parent_access":"Open access"}, "CONFIRMED", ["SRC-UNIBO-BA-CURRICULUM-2026", "SRC-UNIBO-BA-CURRICULUM-PARENT-2026"], "The live course and curriculum pages confirm current identity and delivery but do not identify the 2027/28 admission cycle.")
    business_analytics["facts"]["application_windows"] = _fact(None, "NOT_YET_PUBLISHED", business_analytics_sources, "No course-specific 2027/28 admission dates are published on the current parent/curriculum pages; the 2026/27 call is not reused.")
    business_analytics["last_checked"] = "2026-11-11"

    green_management = by_id["legacy-028"]
    green_source = "SRC-UNIBO-BBS-GREEN-MGMT-2026"
    green_management["level"] = _fact("Professional Master's track (First Level)", "CONFIRMED", [green_source], "BBS identifies Green Management and Sustainable Businesses as a track within the first-level Professional Master in Business Management; it is not a Laurea Magistrale.")
    green_management["language"] = _fact("English", "CONFIRMED", [green_source])
    green_management["field"] = _fact("Green Management and Sustainable Businesses", "CONFIRMED", [green_source])
    green_management["availability_2027_2028"] = _fact(None, "NOT_YET_PUBLISHED", [green_source], "The official track page checked on 11 November 2026 shows a current schedule ending with a January 2027 start but contains no 2027/28 marker or new-cycle call. The intake remains unconfirmed, not discontinued.")
    green_management["overall_status"] = "REQUIRES_VERIFICATION"
    green_management["source_ids"] = [green_source]
    green_management["previous_cycle_tags"] = None
    green_management["facts"] = {
        "previous_cycle_course_listing": _fact({"academic_year":"Not stated on current BBS page", "official_name":"Business Management – Green Management and Sustainable Businesses", "programme_type":"Track within a first-level Professional Master", "duration_months":12, "credits_ects":60, "language":"English", "format":"Full-time, on campus", "learning_hours":1500, "learning_hours_breakdown":{"lectures":360,"independent_study":540,"internship":600}, "collaborating_department":"University of Bologna Department of Management (DISA)"}, "CONFIRMED", [green_source], "Current official course facts only; BBS does not label the programme page's calendar as 2027/28."),
        "current_published_calendar": _fact({"application_deadline":"2026-11-16", "selection":{"written_test":"2026-11-18","motivational_interview":"2026-11-19"}, "enrollment_deadline":"2026-12-01", "crash_courses_start":"2026-12-09", "classes_start":"2027-01-07", "academic_year_label":"Not stated on page"}, "CONFIRMED", [green_source], "These are the dates currently displayed on the BBS page. The page does not assign them to AY 2027/28; do not reuse them as next-cycle dates."),
        "application_windows": _fact(None, "NOT_YET_PUBLISHED", [green_source], "No 2027/28 application dates are published on the official programme page; its current displayed last round leads to January 2027 classes."),
        "application_fee_currently_displayed": _fact({"amount_eur":60,"cycle_label":"Not stated"}, "CONFIRMED", [green_source], "Current application-page amount only; 2027/28 fee unconfirmed."),
        "application_fee_2027_2028": _fact(None, "NOT_YET_PUBLISHED", [green_source], "No 2027/28 application fee is stated on the official track page."),
        "current_published_requirements": _fact({"qualifying_degree":"First-cycle Bachelor's degree by the selected-round enrollment deadline", "english":"Minimum B2", "selection":["Online aptitude test","English-language test","Motivational interview in English"], "cycle_label":"Not stated"}, "CONFIRMED", [green_source], "Current displayed requirements; confirm the annual 2027/28 call before relying on them."),
        "program_specific_requirements_2027_2028": _fact(None, "NOT_YET_PUBLISHED", [green_source], "No 2027/28 call or cycle-labelled detailed requirements are published on the page."),
        "tuition_currently_displayed": _fact({"amount_eur":13800,"vat_free":True,"installments_eur":[1850,7000,4950],"cycle_label":"Not stated"}, "CONFIRMED", [green_source], "The BBS page currently displays this tuition and installment schedule but does not label it for 2027/28."),
        "tuition_2027_2028": _fact(None, "NOT_YET_PUBLISHED", [green_source], "No 2027/28 fee amount is stated; do not carry forward the current €13,800 display."),
        "scholarships_currently_displayed": _fact({"partial_awards_per_round_eur":[3000,5000], "full_awards":"Not available per page", "university_dsu_ergo":"Not eligible per page", "cycle_label":"Not stated"}, "CONFIRMED", [green_source], "Current general BBS track information only; the page does not promise these awards for 2027/28."),
        "scholarships_2027_2028": _fact(None, "NOT_YET_PUBLISHED", [green_source], "No 2027/28 scholarship call or cycle-labelled award terms are published on the page."),
        "acceptance_rate": _fact(None, "UNAVAILABLE", [green_source], "BBS does not publish applicant and admission counts; no acceptance rate is inferred."),
    }
    green_management["last_checked"] = "2026-11-11"

    # AI and Manufacturing is a named 2027/28 Global MBA concentration, not an MSc.
    mba = by_id["legacy-023"]
    mba["program"] = "Global MBA in AI and Manufacturing (Bologna Business School)"
    mba["level"] = _fact("Professional Master's / MBA", "CONFIRMED", ["SRC-UNIBO-BBS-AI-MFG-2027", "SRC-UNIBO-AI-MFG-2026-27-MASTER"])
    mba["language"] = _fact("English", "CONFIRMED", ["SRC-UNIBO-BBS-AI-MFG-2027"])
    mba["field"] = _fact("Artificial Intelligence, Robotics and Manufacturing Management", "CONFIRMED", ["SRC-UNIBO-BBS-AI-MFG-2027", "SRC-UNIBO-AI-MFG-2026-27-MASTER"])
    mba["availability_2027_2028"] = _fact(True, "CONFIRMED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "BBS states applications open in December 2026 for the 2027/28 intake; selections begin February and the programme starts September 2027.")
    mba["overall_status"] = "REQUIRES_VERIFICATION"
    mba["source_ids"] = ["SRC-UNIBO-BBS-AI-MFG-2027", "SRC-UNIBO-AI-MFG-2026-27-MASTER"]
    mba["previous_cycle_tags"] = None
    mba["facts"] = {
        "official_course_listing_2027_2028": _fact({"official_name": "Global MBA in AI and Manufacturing", "programme_type": "12-month full-time English Global MBA / first-level professional master's", "provider": "Bologna Business School with University of Bologna", "application_opening": "December 2026", "selection_period": "from February 2027", "start": "September 2027"}, "CONFIRMED", ["SRC-UNIBO-BBS-AI-MFG-2027"]),
        "application_windows": _fact([{"opening": "December 2026", "selection_from": "February 2027", "programme_start": "September 2027"}], "CONFIRMED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "The BBS page does not give exact round-by-round deadlines; the detailed 2027/28 call is not yet published."),
        "application_deadline": _fact(None, "NOT_YET_PUBLISHED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "Not yet announced for 2027/28; the BBS page says detailed instructions will be published later."),
        "application_fee_2027_2028": _fact(None, "NOT_YET_PUBLISHED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "Not yet announced for 2027/28 in the official programme page reviewed."),
        "program_specific_requirements_2027_2028": _fact(None, "NOT_YET_PUBLISHED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "The page describes selection by academic profile, tests and interview, but the detailed 2027/28 notice has not yet been published."),
        "tuition_2027_2028": _fact(None, "NOT_YET_PUBLISHED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "Not yet announced for 2027/28 in the official programme page reviewed."),
        "scholarships_2027_2028": _fact(None, "NOT_YET_PUBLISHED", ["SRC-UNIBO-BBS-AI-MFG-2027"], "The programme page says high-ranking candidates may be eligible for a scholarship, but 2027/28 award amount and terms are not published."),
        "acceptance_rate": _fact(None, "UNAVAILABLE", ["SRC-UNIBO-BBS-AI-MFG-2027"], "The programme page does not publish the applicant denominator and admitted count; no acceptance rate is inferred."),
    }
    mba["last_checked"] = "2026-11-10"

    padua = [
        ("legacy-029", "Computer Engineering", "MSc", "English", "Computer Engineering", ["SRC-PADOVA-COMPUTER-ENGINEERING-2026", "SRC-PADOVA-ENG-MSC-ADMISSIONS-2026"]),
        ("legacy-030", "Computer Science", "MSc", "English", "Computer Science", ["SRC-PADOVA-COMPUTER-SCIENCE-2026", "SRC-PADOVA-SCIENCE-MSC-2026"]),
        ("legacy-031", "Cybersecurity", "MSc", "English", "Cybersecurity", ["SRC-PADOVA-CYBERSECURITY-2026"]),
        ("legacy-032", "Data Science", "MSc", "English", "Data Science", ["SRC-PADOVA-DATA-SCIENCE-2026"]),
        ("legacy-033", "Information Engineering", "BSc", "English", "Information Engineering", ["SRC-PADOVA-INFORMATION-ENGINEERING-BSC-2026"]),
        ("legacy-034", "Aerospace Engineering", "MSc", "English", "Aerospace Engineering", ["SRC-PADOVA-AEROSPACE-MSC-2026", "SRC-PADOVA-ENG-MSC-ADMISSIONS-2026"]),
        ("legacy-035", "Medicine and Surgery (single-cycle degree)", "Single-cycle Master's (LM-41)", "English", "Medicine and Surgery", ["SRC-PADOVA-MEDICINE-2026"], "Venice (University of Padua degree; cohorts from 2025/26)", "Course location changed for newer cohorts; 2027/28 programme call remains unverified"),
        ("legacy-036", "Psychological Science", "BSc", "English", "Psychology", ["SRC-PADOVA-PSYCHOLOGICAL-SCIENCE-BSC-2026"]),
        ("legacy-159", "Psicologia clinica", "MSc", "Italian", "Clinical Psychology", ["SRC-PADOVA-CLINICAL-PSYCHOLOGY-2026", "SRC-PADOVA-PSYCHOLOGY-MSC-2026"]),
        ("legacy-160", "Psicologia dello sviluppo e dell'educazione", "MSc", "Italian", "Developmental and Educational Psychology", ["SRC-PADOVA-DEVELOPMENTAL-PSYCHOLOGY-2026", "SRC-PADOVA-PSYCHOLOGY-MSC-2026"]),
        ("legacy-161", "Ingegneria gestionale — Management Engineering English-taught track", "MSc", "Italian and English (English-taught track)", "Management Engineering", ["SRC-PADOVA-MANAGEMENT-ENGINEERING-2026", "SRC-PADOVA-ENG-MSC-ADMISSIONS-2026"], "Vicenza", "The official course is based in Vicenza and offers an English-taught study track; the legacy record's Padua-only/English-only description is overbroad"),
        ("legacy-162", "Scienze e tecnologie agrarie", "MSc", "Italian", "Agricultural Sciences and Technologies", ["SRC-PADOVA-AGRICULTURAL-SCIENCES-2026"]),
        ("legacy-163", "Biologia Molecolare", "BSc", "Italian", "Molecular Biology", ["SRC-PADOVA-MOLECULAR-BIOLOGY-BSC-2026"]),
        ("legacy-164", "Ingegneria informatica", "BSc", "Italian", "Computer Engineering", ["SRC-PADOVA-COMPUTER-ENGINEERING-BSC-2026"]),
        ("legacy-165", "Scienze psicologiche cognitive e psicobiologiche", "BSc", "Italian", "Cognitive Psychology and Psychobiology", ["SRC-PADOVA-COGNITIVE-PSYCHOLOGY-BSC-2026"]),
    ]
    for item in padua:
        pid, name, level, language, field_name, sources, *optional = item
        city = optional[0] if optional and ("Padua" in optional[0] or "Vicenza" in optional[0] or "Venice" in optional[0]) else None
        note = optional[1] if optional and city else (optional[0] if optional else None)
        extra = {}
        if note:
            extra["course_identity_correction"] = _fact(note, "CONFIRMED", sources, "Correction applies to 2026/27 course identity and does not establish the 2027/28 intake.")
        prior(by_id[pid], official_name=name, level=level, language=language, field=field_name,
              source_ids=sources, city=city,
              program_type=("English-taught study track within the Italian/English Management Engineering degree" if pid == "legacy-161" else None),
              extra_facts=extra)

    pisa = [
        ("legacy-053", "Cybersecurity", "MSc", "English", "Cybersecurity", ["SRC-UNIPI-CYBERSECURITY-2026", "SRC-UNIPI-MSC-CATALOGUE-2026"]),
        ("legacy-054", "Artificial Intelligence and Data Engineering", "MSc", "English/Italian (required courses in English)", "Artificial Intelligence and Data Engineering", ["SRC-UNIPI-AIDE-2026"]),
        ("legacy-056", "Bionics Engineering", "MSc", "English", "Bionics Engineering", ["SRC-UNIPI-BIONICS-2026", "SRC-UNIPI-MSC-CATALOGUE-2026"]),
        ("legacy-057", "Nuclear Engineering", "MSc", "English", "Nuclear Engineering", ["SRC-UNIPI-NUCLEAR-2026", "SRC-UNIPI-MSC-CATALOGUE-2026"]),
    ]
    for pid, name, level, language, field_name, sources in pisa:
        prior(by_id[pid], official_name=name, level=level, language=language, field=field_name, source_ids=sources)

    naples = [
        ("legacy-085", "Computer Science", "MSc", "Mostly Italian", "Computer Science", ["SRC-UNINA-COMPUTER-SCIENCE-2025"], "2025-2026"),
        ("legacy-086", "Data Science", "MSc", "English", "Data Science", ["SRC-UNINA-DATA-SCIENCE-GUIDE-2026", "SRC-UNINA-DATA-SCIENCE-ADMISSIONS-2026"], "2026-2027"),
        ("legacy-117", "Autonomous Vehicle Engineering (MOVE)", "MSc", "English", "Autonomous Vehicle Engineering", ["SRC-UNINA-MOVE-2026", "SRC-UNINA-MOVE-PROFILE-2025"], "2026-2027"),
        ("legacy-118", "Industrial Bioengineering", "MSc", "English", "Industrial Bioengineering", ["SRC-UNINA-INDUSTRIAL-BIOENGINEERING-2026"], "2026-2027"),
        ("legacy-119", "Economics and Finance (LMEF)", "MSc", "English", "Economics and Finance", ["SRC-UNINA-ECONOMICS-FINANCE-2026", "SRC-UNINA-ECONOMICS-FINANCE-DEPT-2026"], "2026-2027"),
        ("legacy-120", "International Relations (English-taught MSc)", "MSc", "English", "International Relations", ["SRC-UNINA-INTERNATIONAL-RELATIONS-2026"], "2024-2025"),
        ("legacy-121", "Quantum Science and Engineering", "MSc", "English", "Quantum Science and Engineering", ["SRC-UNINA-QUANTUM-2025", "SRC-UNINA-QUANTUM-PROFILE-2025"], "2025-2026"),
        ("legacy-122", "Architecture and Heritage", "MSc", "English", "Architecture and Heritage", ["SRC-UNINA-ARCH-HERITAGE-2025", "SRC-UNINA-ARCH-HERITAGE-REG-2024"], "2024-2025"),
        ("legacy-123", "Medicine and Surgery in English (single-cycle degree)", "Single-cycle Master's (LM-41)", "English", "Medicine and Surgery", ["SRC-UNINA-MED-ENGLISH-2025", "SRC-UNINA-MED-ENGLISH-2026"], "2025-2026"),
        ("legacy-124", "Civil and Environmental Engineering", "BSc", "English", "Civil and Environmental Engineering", ["SRC-UNINA-CIVIL-ENV-BSC-2026"], "2026-2027"),
    ]
    for pid, name, level, language, field_name, sources, cycle in naples:
        extra: dict[str, dict[str, Any]] = {}
        if pid == "legacy-086":
            extra["previous_cycle_program_requirements"] = _fact(
                {"academic_background": "Scientific or economic bachelor's degree", "curricular_credits": "At least 30 CFU in mathematics, physics, statistics or related areas, including at least 6 CFU in computing/information technology", "english": "B2"},
                "CONFIRMED", ["SRC-UNINA-DATA-SCIENCE-ADMISSIONS-2026"], "Official course admission page criteria; recheck the annual 2027/28 notice.",
            )
        elif pid == "legacy-117":
            extra["previous_cycle_application_windows"] = _fact(
                [{"eligible_group": "International applicants", "deadline": "2026-06-15", "route": "Universitaly"}],
                "CONFIRMED", ["SRC-UNINA-MOVE-2026"], "Published for AY 2026/27 only; do not reuse as a 2027/28 deadline.",
            )
        elif pid == "legacy-118":
            extra["previous_cycle_program_requirements"] = _fact(
                {"qualifying_degrees": ["Information Engineering (L-8)", "Industrial Engineering (L-9)"], "grade_average": "Above 24/30", "english": "B2 CEFR"},
                "CONFIRMED", ["SRC-UNINA-INDUSTRIAL-BIOENGINEERING-2026"], "2026/27/current guide requirements only; the 2027/28 call may change them.",
            )
        elif pid == "legacy-119":
            extra["previous_cycle_course_listing"] = _fact(
                {"academic_year": "2026/27", "official_name": "Economics and Finance (LMEF)", "level": "MSc", "language": "English", "duration_years": 2, "degree_class": "LM-56"},
                "CONFIRMED", sources, "LMEF is the two-year degree course. Do not confuse it with the separate 9-month/one-year postgraduate MEF programme.",
            )
        elif pid == "legacy-123":
            extra["previous_cycle_course_listing"] = _fact(
                {"academic_year": "2025/26", "official_name": "Medicine and Surgery in English", "level": "Six-year single-cycle LM-41", "language": "English"},
                "CONFIRMED", sources, "The 2026/27 university notice confirms current programme activity; the cited course regulation is in force for 2025/26.",
            )
        elif pid == "legacy-124":
            extra["previous_cycle_english_requirement"] = _fact(
                {"minimum_level": "B2 CEFR", "tests": ["CEnT-S or SAT under the 2026/27 procedure"]},
                "CONFIRMED", ["SRC-UNINA-CIVIL-ENV-BSC-2026"], "Course admission page labels the CEnT-S/SAT route as current for 2026/27; the 2027/28 test rules are not established.",
            )
        prior(by_id[pid], official_name=name, level=level, language=language, field=field_name,
              source_ids=sources, extra_facts=extra, cycle=cycle)

    florence = [
        ("legacy-087", "Architecture — Architectural Design (iCAD) curriculum", "MSc", "English (iCAD curriculum within an Italian/English degree)", "Architecture and Architectural Design", ["SRC-UNIFI-ARCHITECTURE-MSC-2026", "SRC-UNIFI-ARCH-ICAD-2026"], "Florence", "Curriculum within the two-year MSc Architecture (LM-4-R); not a separate all-English degree"),
        ("legacy-126", "Finance and Risk Management", "MSc", "English", "Finance and Risk Management", ["SRC-UNIFI-FINANCE-RISK-MSC-2026", "SRC-UNIFI-FINANCE-RISK-ADMISSION-2026"], "Florence", None),
        ("legacy-127", "Economics and Development", "MSc", "English", "Economics and Development", ["SRC-UNIFI-ECON-DEV-MSC-2026"], "Florence", None),
        ("legacy-128", "Geoengineering", "MSc", "English", "Geoengineering and Environmental Engineering", ["SRC-UNIFI-GEOENGINEERING-MSC-2026", "SRC-UNIFI-GEOENGINEERING-ENROLMENT-2026"], "Florence", None),
        ("legacy-129", "Urban and Regional Planning and Design for Sustainability — English-taught curriculum", "MSc", "English (English-taught curriculum; parent degree is Italian/English)", "Urban and Regional Planning", ["SRC-UNIFI-URBAN-PLANNING-MSC-2026", "SRC-UNIFI-URBAN-PLANNING-ADMISSION-2025"], "Prato", "English curriculum within the two-year LM-48-R degree; course location is Prato, not Florence"),
        ("legacy-130", "International Relations and European Studies — English-only pathway", "MSc", "Italian and English (optional English-only study pathway)", "International Relations and European Studies", ["SRC-UNIFI-RISE-MSC-2026", "SRC-UNIFI-RISE-ENGLISH-PATHWAY-2026", "SRC-UNIFI-RISE-ADMISSION-2026"], "Florence", "Interclass degree LM-52-R/LM-90-R; students can choose Italian, English-only, or mixed-language coursework"),
        ("legacy-131", "Sustainable Business for Societal Challenges", "BSc", "English", "Sustainable Business and Societal Challenges", ["SRC-UNIFI-SUSBUS-BSC-2026", "SRC-UNIFI-SUSBUS-CALL-2026"], "Florence", None),
    ]
    for pid, name, level, language, field_name, sources, city, program_type in florence:
        extra: dict[str, dict[str, Any]] = {}
        if pid == "legacy-087":
            extra["previous_cycle_program_requirements"] = _fact(
                {"english": "Proficiency in English is required", "selection": "Comparative evaluation of prior academic record; exact requirements depend on current programme instructions."},
                "CONFIRMED", ["SRC-UNIFI-ARCH-ICAD-2026"], "Current official curriculum page; verify annually for 2027/28.",
            )
        elif pid == "legacy-126":
            extra["previous_cycle_program_requirements"] = _fact(
                {"academic_background": ["Management", "Economics", "Statistics", "Mathematics", "Computer Science", "Physics"], "minimum_grade_for_listed_Italian_degrees": ">99/110", "preparation": ["Mathematics", "Statistics", "Social sciences", "IT/data analysis"], "english": "B2"},
                "CONFIRMED", ["SRC-UNIFI-FINANCE-RISK-ADMISSION-2026"], "Requirements described on the official programme page; check current instructions for foreign-degree equivalents and annual changes.",
            )
            extra["previous_cycle_english_requirement"] = _fact({"minimum_level": "B2 CEFR"}, "CONFIRMED", ["SRC-UNIFI-FINANCE-RISK-ADMISSION-2026"], "Official programme guidance; verify any 2027/28 changes.")
        elif pid == "legacy-128":
            extra["previous_cycle_program_requirements"] = _fact(
                {"qualifying_degree": "First-cycle or single-cycle degree", "curricular_requirements": "Specified subject-credit requirements; Teaching Committee evaluates foreign qualifications or credit gaps", "personal_preparation": "At least 90/110 final grade, or at least 22/30 average for conditional enrollees", "english": "B2 CEFR"},
                "CONFIRMED", ["SRC-UNIFI-GEOENGINEERING-MSC-2026"], "Profile links 2026/27 study plan and states these programme rules; reconfirm in the 2027/28 call.",
            )
            extra["previous_cycle_english_requirement"] = _fact({"minimum_level": "B2 CEFR"}, "CONFIRMED", ["SRC-UNIFI-GEOENGINEERING-MSC-2026"], "Profile-linked 2026/27 requirements; annual call may change details.")
            extra["previous_cycle_application_windows"] = _fact(
                [{"start": "2026-07-01", "end": "2026-12-18", "description": "ordinary enrolment deadline for AY 2026/27", "late_enrolment": "allowed with €100 extra fee"}],
                "CONFIRMED", ["SRC-UNIFI-GEOENGINEERING-ENROLMENT-2026"], "Dates are explicitly for entry in 2026/27 only, not 2027/28.",
            )
        elif pid == "legacy-129":
            extra["previous_cycle_program_requirements"] = _fact(
                {"eligible_backgrounds": ["Planning", "Architecture", "equivalent three-year degree"], "other_degrees": "comparative evaluation; committee may request interview or curricular integration", "english": "B2 CEFR"},
                "CONFIRMED", ["SRC-UNIFI-URBAN-PLANNING-ADMISSION-2025"], "This source page was last updated in 2023; treat as historical guidance pending a newer 2027/28 admission page.",
            )
            extra["previous_cycle_english_requirement"] = _fact({"minimum_level": "B2 CEFR"}, "CONFIRMED", ["SRC-UNIFI-URBAN-PLANNING-ADMISSION-2025"], "Older programme-level page; verify current-year proof rules.")
        elif pid == "legacy-130":
            extra["previous_cycle_program_requirements"] = _fact(
                {"qualifying_degree": "Three-year university degree or equivalent", "minimum_gpa_for_foreign_degree_applicants": "80/100", "english_only_pathway": "Applicants completing the programme entirely in English are exempt from the University's Italian-language test"},
                "CONFIRMED", ["SRC-UNIFI-RISE-ADMISSION-2026", "SRC-UNIFI-RISE-ENGLISH-PATHWAY-2026"], "Non-Italian degree requirements are for AY 2026/27; do not infer future annual deadlines or unchanged requirements.",
            )
        elif pid == "legacy-131":
            extra["previous_cycle_application_windows"] = _fact(
                [
                    {"round": "First", "start": "2026-04-20", "end": "2026-05-11", "eligible_group": "EU and non-EU applicants", "test_date": "2026-05-26"},
                    {"round": "Second", "start": "2026-04-20", "end": "2026-08-24", "eligible_group": "EU and equivalent applicants only", "test_date": "2026-09-10"},
                    {"round": "Third", "start": "2026-04-20", "end": "2026-09-24", "eligible_group": "EU and equivalent applicants only", "test_date": "2026-10-06"},
                ], "CONFIRMED", ["SRC-UNIFI-SUSBUS-CALL-2026"], "Three historical 2026/27 application rounds; not 2027/28 deadlines.",
            )
            extra["previous_cycle_available_places"] = _fact({"total": 250, "academic_year": "2026/27"}, "CONFIRMED", ["SRC-UNIFI-SUSBUS-CALL-2026"], "Places are for the 2026/27 call only.")
            extra["previous_cycle_entrance_test"] = _fact(
                {"format": "online Mathematics and reasoning on texts/data test; no TOLC-E under revised 2026/27 procedure"},
                "CONFIRMED", ["SRC-UNIFI-SUSBUS-CALL-2026"], "Historical 2026/27 procedure only.",
            )
        prior(by_id[pid], official_name=name, level=level, language=language, field=field_name,
              source_ids=sources, city=city, program_type=program_type, extra_facts=extra,
              cycle="2026-2027", checked_at="2026-11-11")

    tor_vergata_sources = ["SRC-ROMA2-COMPUTER-SCIENCE-MSC-2026", "SRC-ROMA2-COMPUTER-SCIENCE-REGULATIONS-2026"]
    prior(
        by_id["legacy-095"], official_name="Computer Science", level="MSc", language="Italian",
        field="Computer Science", source_ids=tor_vergata_sources, city="Rome",
        program_type="Two-year LM-18 degree; catalogued as Italian-taught with curriculum evaluation for admission",
        extra_facts={
            "previous_cycle_program_requirements": _fact(
                {"qualifying_degree": "Three-year degree, university diploma or recognized foreign qualification", "admission": "No restricted number of places; individual curriculum evaluation; supplementary Computer Science courses may be recommended"},
                "CONFIRMED", ["SRC-ROMA2-COMPUTER-SCIENCE-REGULATIONS-2026"], "Official regulations describe academic entry criteria; annual application portal dates and 2027/28 intake still need checking.",
            ),
        }, cycle="2026-2027", checked_at="2026-11-11",
    )


def apply(
    programs: list[dict[str, Any]],
    fact: Callable[..., dict[str, Any]],
    make_program: Callable[..., dict[str, Any]],
) -> None:
    """Apply fully sourced cycle findings to the generated snapshot."""

    by_id = {program["id"]: program for program in programs}
    pod_id = "legacy-037"
    physics = by_id[pod_id]
    physics_sources = [
        "SRC-PADUA-PHYSICS-DATA-PROFILE",
        "SRC-PADUA-PHYSICS-DATA-REQUIREMENTS",
        "SRC-PADUA-PHYSICS-DATA-2027-CALL",
        "SRC-PADUA-SCIENCE-MSC-CATALOGUE-2026",
        "SRC-PADUA-STUDY-ENGLISH-APPLY-2027",
    ]
    physics["level"] = fact("MSc", "CONFIRMED", physics_sources)
    physics["language"] = fact("English", "CONFIRMED", physics_sources)
    physics["field"] = fact("Physics and Data Science", "CONFIRMED", physics_sources)
    physics["availability_2027_2028"] = fact(
        True, "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-PROFILE", "SRC-PADUA-PHYSICS-DATA-2027-CALL"],
        "The programme-specific official announcement invites international Bachelor's-degree applicants for AY 2027/28 entry.",
    )
    physics["overall_status"] = "CONFIRMED"
    physics["source_ids"] = physics_sources
    physics["previous_cycle_tags"] = None
    physics["facts"] = {
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Physics of Data", "degree": "Master's Degree", "degree_class": "LM-17 R", "duration_years": 2, "location": "Padua", "language": "English", "access": "Open admission with requirements"},
            "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-PROFILE", "SRC-PADUA-SCIENCE-MSC-CATALOGUE-2026"],
            "Prior-cycle catalogue/profile evidence; the separate 2027/28 announcement confirms new international intake.",
        ),
        "previous_cycle_program_requirements": fact(
            {"qualifying_degree": "Bachelor's degree or equivalent, minimum three-year undergraduate degree", "academic_background": "Demonstrated skills in Physics and Mathematics"},
            "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-REQUIREMENTS"],
            "Course-level requirements page is not expressly cycle-labelled; recheck the 2027/28 call for any changed criteria.",
        ),
        "previous_cycle_english_requirement": fact(
            {"minimum_level": "B2 CEFR or equivalent"}, "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-REQUIREMENTS"],
            "The current requirements page states B2; accepted certificates and any waivers must be checked in the relevant annual call.",
        ),
        "application_windows": fact(
            [{"round": "First call", "start": None, "end": "2026-11-15", "eligible_group": "Applicants with an international Bachelor's degree, including candidates graduating by July 2027", "application_route": "apply.unipd.it"}],
            "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-2027-CALL"],
            "The programme-specific announcement states that the first call is open and gives its deadline, but does not state the opening date or later rounds.",
        ),
        "application_deadline": fact(
            {"date": "2026-11-15", "round": "First call"}, "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-2027-CALL"],
            "International applicants to the named 2027/28 programme; this is not a final enrolment or visa deadline.",
        ),
        "application_fee_2027_2028": fact(
            {"amount_eur": 60, "refundable": False, "route": "apply.unipd.it", "program_limit": 2},
            "CONFIRMED", ["SRC-PADUA-PHYSICS-DATA-2027-CALL", "SRC-PADUA-STUDY-ENGLISH-APPLY-2027"],
            "The University-wide English-degree application procedure applies to the named English-taught MSc; confirm any exception shown in the live portal.",
        ),
        "tuition_2027_2028": fact(
            None, "REQUIRES_VERIFICATION", ["SRC-PADUA-INTL-2027"],
            "No 2027/28 tuition amount is stated in the programme-specific call notice.",
        ),
        "scholarships_2027_2028": fact(
            None, "REQUIRES_VERIFICATION", ["SRC-PADUA-PHYSICS-DATA-2027-CALL"],
            "No programme-specific 2027/28 scholarship terms were stated in the first-call notice reviewed.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "REQUIRES_VERIFICATION", ["SRC-PADUA-PHYSICS-DATA-2027-CALL", "SRC-PADUA-PHYSICS-DATA-REQUIREMENTS"],
            "The call confirms the named programme and international intake but refers applicants to the portal for the full requirements; the page's current B2 and subject-background details need confirmation in the 2027/28 application factsheet.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-PADUA-PHYSICS-DATA-2027-CALL"],
            "No applicant and admission counts are published in the first-call notice; no rate is inferred.",
        ),
    }
    physics["last_checked"] = "2026-11-10"

    grenfin_sources = ["SRC-UNIBO-GRENFIN-2027-PROFILE", "SRC-UNIBO-GRENFIN-2027-CALL"]
    grenfin = make_program(
        "discovered-029", "bologna", "Greening Energy Market and Finance (GrEnFIn Erasmus Mundus Joint Master)",
        "MSc", "English", "Finance and Sustainable Energy", "CONFIRMED", grenfin_sources,
        city="Bologna", discovery="newly_discovered",
    )
    grenfin["facts"] = {
        "official_course_listing_2027_2028": fact(
            {"academic_year": "2027/28", "official_name": "Greening Energy Market and Finance (GrEnFIn-EMJM)", "degree": "Second-cycle joint Master's degree", "degree_class_at_unibo": "LM-16 Finance", "duration_months": 24, "credits": 120, "teaching_language": "English", "tracks": ["Renewable Technologies", "Environmental Finance", "Climate & Business"], "mobility_partners": ["University of Bologna", "Ludwig-Maximilians-Universität München", "Université Paris Dauphine"]},
            "CONFIRMED", grenfin_sources,
        ),
        "application_windows": fact(
            [{"start": "2026-10-14", "end": "2027-01-07", "end_time": "11:00 CET", "eligible_group": "EU and non-EU applicants; one of three tracks"}],
            "CONFIRMED", ["SRC-UNIBO-GRENFIN-2027-CALL"],
        ),
        "application_deadline": fact(
            {"date": "2027-01-07", "time": "11:00 CET"}, "CONFIRMED", ["SRC-UNIBO-GRENFIN-2027-CALL"],
        ),
        "application_route": fact(
            "Studenti Online; select the Second Cycle Degree Programme and one of the three GrEnFIn tracks.",
            "CONFIRMED", ["SRC-UNIBO-GRENFIN-2027-CALL"],
        ),
        "available_places": fact(
            {"maximum": 51}, "CONFIRMED", ["SRC-UNIBO-GRENFIN-2027-CALL"],
            "Maximum places stated for AY 2027/28; no applicant count is published.",
        ),
        "program_specific_requirements_2027_2028": fact(
            {"qualifying_degree": "Three-year first-cycle degree or a foreign qualification recognized as suitable", "eligible_backgrounds": ["Mathematics", "Physics", "Economics", "Statistics", "Information Technology", "Engineering"], "english": "B2 CEFR", "selection": {"scoring_max": 100, "minimum_eligibility_score": 60, "interview_threshold": 80, "optional_evidence": ["GRE", "GMAT"]}},
            "CONFIRMED", ["SRC-UNIBO-GRENFIN-2027-CALL"],
        ),
        "application_fee_2027_2028": fact(
            None, "UNAVAILABLE", ["SRC-UNIBO-GRENFIN-2027-CALL"],
            "The 2027/28 official admission notice does not state an application fee.",
        ),
        "tuition_2027_2028": fact(
            {"self_funded_fee_structure": {"fixed_element_eur": 157.04, "variable_element": "Calculated by ISEE up to a programme-specific maximum", "programme_maximum_eur": None}},
            "REQUIRES_VERIFICATION", ["SRC-UNIBO-GRENFIN-2027-CALL"],
            "The admission notice gives the fixed-plus-variable structure but not the programme maximum; obtain the applicable 2027/28 amount from the annual tuition schedule. This does not apply to the Erasmus Mundus scholarship's covered costs.",
        ),
        "scholarships": fact(
            {"academic_year": "2027/28", "provider": "Erasmus Mundus Joint Master", "maximum_awards": 18, "gross_monthly_amount_eur": 1400, "coverage": ["Travel", "Visa", "Installation", "Subsistence"], "eligibility": "Full-time students worldwide meeting programme requirements; competitive ranking"},
            "CONFIRMED", ["SRC-UNIBO-GRENFIN-2027-CALL"],
            "Maximum award counts and rates; awards are competitive and not guaranteed.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-UNIBO-GRENFIN-2027-CALL"],
            "The notice gives a maximum of 51 places but no applicant denominator; no acceptance rate is inferred.",
        ),
    }
    grenfin["last_checked"] = "2026-11-10"
    programs.append(grenfin)

    mathematical_sources = [
        "SRC-POLITO-MATHEMATICAL-ENGINEERING-PROFILE-2026",
        "SRC-POLITO-MATHEMATICAL-ENGINEERING-ENGLISH-TRACK-2027",
        "SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027",
    ]
    mathematical = make_program(
        "discovered-030", "politecnico-torino", "Mathematical Engineering – planned English-taught track",
        "MSc", "English (planned; track approval pending)", "Mathematical Engineering",
        "REQUIRES_VERIFICATION", mathematical_sources, city="Turin", discovery="newly_discovered",
    )
    mathematical["level"] = fact("MSc", "CONFIRMED", mathematical_sources,
        "The 2027/28 scholarship call identifies admission to the LM-44 Master's programme; the detailed study track remains subject to approval.")
    mathematical["field"] = fact("Mathematical Engineering", "CONFIRMED", mathematical_sources)
    mathematical["language"] = fact("English (planned track; pending approval)", "REQUIRES_VERIFICATION",
        ["SRC-POLITO-MATHEMATICAL-ENGINEERING-PROFILE-2026", "SRC-POLITO-MATHEMATICAL-ENGINEERING-ENGLISH-TRACK-2027"],
        "The latest profile lists the existing programme as Italian-taught for 2026/27. The university describes an all-English 2027/28 track as planned but explicitly pending approval.")
    mathematical["availability_2027_2028"] = fact(True, "CONFIRMED",
        ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"],
        "The official 2027/28 scholarship call requires applicants to apply for admission and enroll in the Mathematical Engineering MSc in 2027/28. This confirms the degree intake, not approval of the proposed English track.")
    mathematical["source_ids"] = mathematical_sources
    mathematical["facts"] = {
        "previous_cycle_course_listing": fact({"academic_year":"2026/27", "degree":"Master's degree", "degree_class":"LM-44", "duration_years":2, "language":"Italian", "admission":"Uncapped, subject to evaluation of requirements", "campus":"Main Campus"}, "CONFIRMED", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-PROFILE-2026"], "This is the prior-cycle profile; do not apply its language or admission details to 2027/28 without the annual rules."),
        "official_course_listing_2027_2028": fact({"academic_year":"2027/28", "degree":"LM-44 Master's programme", "degree_intake":"Supported by programme-specific 2027/28 scholarship call", "planned_track":"English-taught; Scientific Computing & HPC and Cryptography & Cybersecurity", "track_approval":"Pending; university says the proposal may change"}, "CONFIRMED", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-ENGLISH-TRACK-2027", "SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "The degree intake is supported; the proposed track is not finally approved."),
        "scholarships_2027_2028": fact({"academic_year":"2027/28", "awards":3, "gross_amount_eur_each":16000, "eligible_group":"Applicants with suitable foreign first-cycle qualification", "conditions":["Submit a 2027/28 admission application", "Be assessed eligible for admission or admitted", "Enroll for the first time in the programme in 2027/28"]}, "CONFIRMED", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "Competitive scholarship call; eligibility and award are not guaranteed."),
        "scholarship_application_window_2027_2028": fact({"start":"2026-10-14", "end":"2027-01-29", "end_time":"23:55"}, "CONFIRMED", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "This is the scholarship application window, not the degree admission application window."),
        "application_windows": fact(None, "NOT_YET_PUBLISHED", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "No degree admission dates were found in the reviewed sources; the published dates above apply only to the scholarship call."),
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "The scholarship call references compliance with the programme's admission requirements but does not set out the detailed 2027/28 course-specific requirements."),
        "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "The reviewed 2027/28 sources do not state a degree application fee."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "No programme-specific 2027/28 tuition amount was found in the reviewed sources."),
        "acceptance_rate": fact(None, "UNAVAILABLE", ["SRC-POLITO-MATHEMATICAL-ENGINEERING-SCHOLARSHIP-2027"], "No applicant and admission counts were found; no acceptance rate is inferred from the three scholarships."),
    }
    mathematical["last_checked"] = "2026-11-11"
    programs.append(mathematical)

    polimi_28digital_source = "SRC-POLIMI-28DIGITAL-APPLICATIONS-2027"
    for pid, local_degree in [
        ("legacy-001", "Computer Science and Engineering (T2A)"),
        ("legacy-004", "High Performance Computing Engineering"),
    ]:
        program = by_id[pid]
        # Active-cycle evidence is specific to this route; keep prior-cycle facts,
        # but do not render the row as exclusively supported by the prior cycle.
        program["previous_cycle_tags"] = None
        program["availability_2027_2028"] = fact(
            True, "CONFIRMED", [polimi_28digital_source],
            "Confirmed only for the named 28DIGITAL 2027/28 entry pathway. The joint programme assigns Polimi as entry university based on preferences and selection, and requires a separate local application; general course-wide admission terms remain subject to the relevant Polimi call.",
        )
        program["source_ids"] = list(dict.fromkeys(program.get("source_ids", []) + [polimi_28digital_source]))
        program["facts"]["official_2027_2028_28digital_pathway"] = fact(
            {"academic_year":"2027/28", "entry_university":"Politecnico di Milano (conditional on assigned study offer)", "local_msc":local_degree, "separate_polimi_application_required":True, "first_28digital_period_deadline":"2027-01-31", "later_28digital_periods":"Further periods subject to availability; exact dates not given"},
            "CONFIRMED", [polimi_28digital_source],
            "This confirms the named joint-degree route, not a general promise of admission or a standalone 28DIGITAL degree at Polimi.",
        )
        program["facts"]["28digital_local_application_windows_non_italian_degree"] = fact(
            [{"start":"2026-10-01","end":"2026-12-01","eligible_group":"Applicants with a degree from outside Italy; all citizenship groups"}, {"start":"2027-01-12","end":"2027-02-25","eligible_group":"Applicants with a degree from outside Italy; all citizenship groups"}, {"start":"2027-03-01","end":"2027-03-18","eligible_group":"EEA citizens and non-EEA citizens resident in Italy only"}],
            "CONFIRMED", [polimi_28digital_source],
            "These are the local Polimi application windows for candidates seeking a Polimi entry in 28DIGITAL. Submit the separate 28DIGITAL application in parallel.",
        )
        program["facts"]["28digital_local_application_window_italian_degree"] = fact(
            None, "NOT_YET_PUBLISHED", [polimi_28digital_source],
            "For degrees obtained in Italy, the page says successful 28DIGITAL applicants assigned to Polimi will be invited to submit the local application in July–August 2027; exact dates are to be published in spring.",
        )
        program["facts"]["28digital_local_application_fee_2027_2028"] = fact(
            {"early_bird_eur":50,"early_bird_through":"2026-12-01","standard_eur":150,"standard_from":"2026-12-02","payment_effect":"Without the Polimi fee, the local application is evaluated only in connection with 28DIGITAL admission"},
            "CONFIRMED", [polimi_28digital_source],
        )
        program["facts"]["application_windows"] = fact(
            None, "CONFLICTING_SOURCES", ["SRC-POLIMI-DEADLINES-2027", polimi_28digital_source],
            "The general Polimi page still gives a general 2027/28 end date of 28 January and an Engineering subsection labelled 2026/27 with a 25 February end date for September 2027 intake. The 28DIGITAL-specific page confirms 25 February for this special pathway only; it does not resolve the course-wide Engineering deadline for non-28DIGITAL applicants.",
        )
        program["last_checked"] = "2026-11-11"

    padua_planned_source = "SRC-PADUA-ENGLISH-DEGREES-PROPOSED-2027"
    planned_padua = [
        ("discovered-031", "Management, Finance and Business Analytics (proposed 2027/28)", "Business Analytics", "Business / analytics"),
        ("discovered-032", "Food Safety for Global Health (proposed 2027/28)", "Food Science and Global Health", "Food safety / public health"),
        ("discovered-033", "Innovative Technologies in Agriculture (proposed 2027/28)", "Agricultural Technology", "Agricultural technology"),
    ]
    for pid, title, field_name, field_value in planned_padua:
        candidate = make_program(
            pid, "padova", title, "BSc (proposed)", "English (proposed)", field_value,
            "REQUIRES_VERIFICATION", [padua_planned_source], city="Padua", discovery="newly_discovered",
        )
        candidate["level"] = fact("BSc (proposed)", "CONFIRMED", [padua_planned_source],
            "The official catalogue places the item under Bachelor's Degree Programmes but explicitly marks it as a new programme awaiting approval.")
        candidate["language"] = fact("English (proposed)", "CONFIRMED", [padua_planned_source],
            "The official page is the English-taught programme catalogue; the individual proposal remains subject to approval.")
        candidate["field"] = fact(field_name, "REQUIRES_VERIFICATION", [padua_planned_source],
            "Field label is an editorial classification from the proposed programme title; no approved course specification is published.")
        candidate["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", [padua_planned_source],
            "The university lists the programme for 2027/28 but explicitly says it is still to be approved. No course-specific 2027/28 call was identified.")
        candidate["facts"] = {
            "official_planned_course_listing_2027_2028": fact({"academic_year":"2027/28", "proposed_name":title.split(" (proposed")[0], "proposed_level":"Bachelor's degree", "listed_in_english_degree_catalogue":True, "approval_status":"To be approved"}, "CONFIRMED", [padua_planned_source], "Confirms a published proposal only; it does not confirm accreditation, opening, or first-year admission."),
            "application_windows": fact(None, "NOT_YET_PUBLISHED", [padua_planned_source, "SRC-PADUA-INTL-2027"], "The University has general 2027/28 international calls for most courses, but the proposed degree itself is awaiting approval and no course-specific admission window or inclusion in those calls was identified."),
            "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source], "No approved course regulations or programme-specific entry requirements have been published in the reviewed source."),
            "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source], "No programme-specific application fee is confirmed for this unapproved proposal."),
            "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source], "No course-specific 2027/28 fee is confirmed for this unapproved proposal."),
            "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source], "No programme-specific 2027/28 scholarship call is confirmed."),
        }
        candidate["source_ids"] = [padua_planned_source, "SRC-PADUA-INTL-2027"]
        candidate["last_checked"] = "2026-11-11"
        programs.append(candidate)

    padua_master_candidates = [
        ("discovered-035", "Data Analytics and Decision Support (proposed 2027/28)", "Data Analytics and Decision Support", "Data analytics and decision support", "School of Science English Master's catalogue; explicitly marked as a new 2027/28 programme to be approved."),
        ("discovered-036", "Statistical Science (proposed 2027/28)", "Statistical Science", "Statistics and data science", "School of Science English Master's catalogue marks Statistical Sciences as to be approved; the Department profile describes an English Master's programme with a projected September 2027 start, which remains a plan pending central approval."),
    ]
    statistical_profile = "SRC-PADUA-STATISTICAL-SCIENCE-PROFILE-2027"
    statistical_requirements = "SRC-PADUA-STATISTICAL-SCIENCE-ENTRY-REQUIREMENTS"
    for pid, title, proposed_name, field_value, approval_note in padua_master_candidates:
        source_ids = [padua_planned_source]
        if pid == "discovered-036":
            source_ids.extend([statistical_profile, statistical_requirements])
        candidate = make_program(
            pid, "padova", title, "MSc (proposed)", "English (proposed)", field_value,
            "REQUIRES_VERIFICATION", source_ids, city="Padua", discovery="newly_discovered",
        )
        candidate["program"] = title
        candidate["level"] = fact("MSc (proposed)", "CONFIRMED", [padua_planned_source],
            "The official catalogue places this candidate under English-taught Master's programmes but explicitly marks it as awaiting approval; no approved course regulation is published.")
        candidate["language"] = fact("English (proposed)", "CONFIRMED", [padua_planned_source] + ([statistical_profile] if pid == "discovered-036" else []),
            "The official English-degree catalogue lists the proposal under Master's programmes taught in English; for Statistical Science the Department page independently describes English delivery. Approval and the final course offer remain pending.")
        candidate["field"] = fact(field_value, "REQUIRES_VERIFICATION", source_ids,
            "Editorial subject classification based on the proposed name; no approved course specification is available.")
        candidate["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", source_ids,
            "The University catalogue marks the proposed programme as awaiting approval. For Statistical Science, the Department's projected September 2027 start does not establish approval or a confirmed first-year intake.")
        candidate["facts"] = {
            "official_planned_course_listing_2027_2028": fact(
                {"academic_year":"2027/28", "proposed_name":proposed_name, "proposed_level":"Master's degree", "listed_in_english_degree_catalogue":True, "approval_status":"To be approved"},
                "CONFIRMED", [padua_planned_source], approval_note,
            ),
            "department_projected_profile": fact(
                {"academic_year":"2027/28 (projected)", "duration_years":2, "ects":120, "attendance":"Full-time, on campus", "language":"English", "expected_start":"2027-09-27"} if pid == "discovered-036" else None,
                "REQUIRES_VERIFICATION",
                [statistical_profile] if pid == "discovered-036" else [padua_planned_source],
                "The Department profile publishes a projected start and course details, but the central English Master's catalogue still labels the proposal as awaiting approval. Treat all profile details as provisional." if pid == "discovered-036" else "No department-level programme profile has been identified; verify whether a separate proposal specification is published.",
            ),
            "proposed_admission_requirements": fact(
                {"italian_degree_applicants":"Department page lists at least 35 ECTS in specified subject sectors, including 15 ECTS in MATH-03/A, a final mark of at least 85/110, a three-year degree and English B2; these criteria are not cycle-labelled.", "international_degree_applicants":"No complete course-specific requirement checklist is published in the reviewed page."} if pid == "discovered-036" else None,
                "REQUIRES_VERIFICATION",
                [statistical_requirements] if pid == "discovered-036" else [padua_planned_source],
                "Provisional, undated Department information only; do not present these thresholds as approved 2027/28 admission rules." if pid == "discovered-036" else "No approved course admission requirements have been identified; verify when the proposal is approved.",
            ),
            "application_windows": fact(None, "NOT_YET_PUBLISHED", [padua_planned_source, "SRC-PADUA-INTL-2027"] + ([statistical_profile] if pid == "discovered-036" else []),
                "The University-level 2027/28 application calls cover most courses but do not confirm that this unapproved proposal is included; no programme-specific call or deadline was found."),
            "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", source_ids,
                "No approved annual programme regulation or 2027/28 course-specific requirements are available."),
            "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source],
                "No programme-specific 2027/28 application fee is confirmed for this unapproved proposal."),
            "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source],
                "No programme-specific 2027/28 tuition amount is confirmed."),
            "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", [padua_planned_source],
                "No programme-specific 2027/28 scholarship call or eligibility is confirmed."),
            "acceptance_rate": fact(None, "UNAVAILABLE", [padua_planned_source],
                "No applicant and admitted-student totals are published; no acceptance rate is inferred."),
        }
        candidate["source_ids"] = list(dict.fromkeys(source_ids + ["SRC-PADUA-INTL-2027"]))
        candidate["last_checked"] = "2026-11-11"
        programs.append(candidate)

    arqus_source = "SRC-PADUA-ARQUS-PHYSICS-TECH-2026"
    arqus_physics = make_program(
        "discovered-034", "padova", "Physics for Technology (planned Arqus joint Bachelor's)",
        "BSc (joint programme in development)", "REQUIRES_VERIFICATION", "Physics and Technology",
        "REQUIRES_VERIFICATION", [arqus_source], city="Padua", discovery="newly_discovered",
    )
    arqus_physics["level"] = fact("BSc (joint programme in development)", "CONFIRMED", [arqus_source],
        "The official announcement calls this a joint Bachelor's programme under development; no academic-year launch is stated.")
    arqus_physics["language"] = fact(None, "REQUIRES_VERIFICATION", [arqus_source, padua_planned_source],
        "The 2027/28 English-language degree catalogue does not list Physics for Technology; the Arqus development announcement does not state teaching language.")
    arqus_physics["field"] = fact("Physics and Technology", "CONFIRMED", [arqus_source])
    arqus_physics["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", [arqus_source, padua_planned_source],
        "The source confirms a consortium development agreement only. It gives no launch cycle, admission call or approval/accreditation status.")
    arqus_physics["facts"] = {
        "official_programme_development": fact({"name":"Physics for Technology", "degree_type":"Joint Bachelor's programme", "partners":["University of Padua", "University of Granada", "Vilnius University", "University of Wroclaw"], "status":"Consortium development agreement signed; launch details not published"}, "CONFIRMED", [arqus_source]),
        "application_windows": fact(None, "NOT_YET_PUBLISHED", [arqus_source], "No application window or launch academic year is given in the programme-development announcement."),
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", [arqus_source], "No approved programme regulation or admission requirements have been published in the reviewed source."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", [arqus_source], "No applicable programme fee or tuition structure is published in the reviewed source."),
        "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", [arqus_source], "No programme-specific scholarship call is published in the reviewed source."),
    }
    arqus_physics["last_checked"] = "2026-11-11"
    programs.append(arqus_physics)

    astro_profile = "SRC-PADUA-ASTROPHYSICS-COURSE-PROFILE-2027"
    astro_call = "SRC-PADUA-ASTROPHYSICS-2027-CALL"
    astro = make_program(
        "discovered-037", "padova", "Astrophysics and Cosmology", "MSc", "English",
        "Astrophysics and Cosmology", "CONFIRMED", [astro_profile, astro_call],
        city="Padua", discovery="newly_discovered",
    )
    astro["level"] = fact("MSc", "CONFIRMED", [astro_profile])
    astro["language"] = fact("English", "CONFIRMED", [astro_profile])
    astro["field"] = fact("Astrophysics and Cosmology", "CONFIRMED", [astro_profile])
    astro["availability_2027_2028"] = fact(
        True, "CONFIRMED", [astro_call],
        "A named first call confirms 2027/28 entry for applicants with an international Bachelor's degree. This does not confirm the 2027/28 domestic-qualification call or make admission automatic.",
    )
    astro["facts"] = {
        "official_course_profile": fact(
            {"academic_year":"current official course profile", "degree_class":["LM-17 R - Physics", "LM-58 R - Sciences of the Universe"], "duration_years":2, "campus":"Padua", "language":"English", "access":"Open admission with requirements"},
            "CONFIRMED", [astro_profile],
        ),
        "application_windows": fact(
            [{"start":None, "end":"2026-11-15", "round":"First call", "eligible_group":"Applicants with an international Bachelor's degree seeking entry in AY 2027/28"}],
            "CONFIRMED", [astro_call],
            "The course-specific Department notice gives the first-call deadline but not the opening date. The open window is scoped to international degree holders; domestic-degree applicants follow a separate notice.",
        ),
        "application_route": fact("apply.unipd.it", "CONFIRMED", [astro_profile, astro_call], "The official profile links the University application portal; the Department call directs eligible international Bachelor's degree holders to apply there."),
        "application_fee_2027_2028": fact(
            {"amount_eur":60, "non_refundable":True, "maximum_programmes":2}, "CONFIRMED", ["SRC-PADUA-STUDY-ENGLISH-APPLY-ITALIAN-2027"],
            "University international application procedure; the course call confirms this programme's participation in the international application route.",
        ),
        "applicant_scope_2027_2028": fact(
            {"confirmed_group":"Applicants with an international Bachelor's degree, including those graduating by July 2027", "course_start":"October 2027", "domestic_degree_call":"Not verified"},
            "CONFIRMED", [astro_call],
        ),
        "published_course_requirements_not_cycle_labeled": fact(
            {"physics_credits_ects":24, "physics_sectors":"FIS/01-07", "mathematics_credits_ects":24, "mathematics_sectors":"MAT/01-09", "assessment":"Foreign qualifications assessed by an admission committee; a remote interview may be used"},
            "REQUIRES_VERIFICATION", [astro_call],
            "These criteria appear on the Department admissions page but are not explicitly tied to AY 2027/28. Do not present them as confirmed annual requirements until the relevant 2027/28 call or regulation confirms them.",
        ),
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", [astro_call], "The reviewed call page does not explicitly date the listed 24-ECTS subject thresholds to AY 2027/28; verify against the course's annual regulation."),
        "english_certificate_requirement_2027_2028": fact(None, "REQUIRES_VERIFICATION", [astro_profile, astro_call], "The course profile confirms English delivery, but the reviewed first-call page does not specify a 2027/28 English certificate threshold. No earlier-cycle B2 claim is carried forward."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-PADUA-TUITION-2026"], "The latest official Padua fee page reviewed links 2026/27 tariffs only; no 2027/28 programme fee is confirmed."),
        "acceptance_rate": fact(None, "UNAVAILABLE", [astro_call], "No comparable applicant and admitted-student totals are published in the reviewed sources; no acceptance rate is inferred."),
    }
    astro["source_ids"] = list(dict.fromkeys(astro["source_ids"] + ["SRC-PADUA-STUDY-ENGLISH-APPLY-ITALIAN-2027", "SRC-PADUA-TUITION-2026"]))
    astro["last_checked"] = "2026-11-11"
    astro["previous_cycle_tags"] = None
    programs.append(astro)

    eap_profile = "SRC-UNITO-EAP-PROFILE-2027"
    eap_apply = "SRC-UNITO-EAP-APPLICATION-2027"
    epog_admission = "SRC-EPOG-ADMISSION-2027"
    epog_platform = "SRC-EPOG-APPLICATION-PLATFORM-2027"
    epog_scholarship = "SRC-EPOG-SCHOLARSHIPS"
    epog_tuition = "SRC-EPOG-TUITION-FEES"
    epog_degree = "SRC-EPOG-DEGREE-POLICY"
    eap_sources = [eap_profile, eap_apply, epog_admission, epog_platform, epog_scholarship, epog_tuition, epog_degree]
    eap = make_program(
        "discovered-038", "torino", "Economic Analysis and Policy", "MSc", "English",
        "Economics", "CONFIRMED", eap_sources, city="Turin", discovery="newly_discovered",
    )
    eap["level"] = fact("MSc", "CONFIRMED", [eap_profile])
    eap["language"] = fact("English", "CONFIRMED", [eap_profile])
    eap["field"] = fact("Economics", "CONFIRMED", [eap_profile, epog_admission])
    eap["availability_2027_2028"] = fact(
        True, "CONFIRMED", [eap_apply, epog_admission, epog_platform],
        "The active EPOG-JM call confirms the 2027–2029 cohort, corresponding to 2027/28 first-year entry. This is a consortium route; the University of Turin joint award is available only for Major A and Minor C2 pathway combinations.",
    )
    eap["facts"] = {
        "official_course_profile": fact(
            {"degree_class":"LM-56 R - Economics", "duration_years":2, "language":"English", "access":"Free access with preliminary curricular evaluation and personal-preparation interview", "campus":"Turin; joint-programme teaching seats also include Johannesburg and Paris"},
            "CONFIRMED", [eap_profile, eap_apply],
        ),
        "joint_degree_pathways": fact(
            {"programme":"EPOG-JM Erasmus Mundus Joint Master", "total_ects":120, "degree_award":"Joint or multiple degree based on first- and second-year institutions", "University_of_Turin_pathways":["Major A", "Minor C2"], "mobility":"Depends on selected pathway; not every EPOG student receives a Turin degree"},
            "CONFIRMED", [epog_degree, epog_admission],
        ),
        "application_windows": fact(
            [{"start":"2026-10", "end":"2027-01-27T13:00:00+01:00", "round":"EPOG-JM two-year programme, 2027–2029 cohort", "eligible_group":"Applicants to the consortium cohort; University of Turin degree award is pathway-dependent"}],
            "CONFIRMED", [epog_admission, epog_platform],
            "The official call says the platform opened in October 2026 and closes at 13:00 Europe/Paris on 27 January 2027. Interviews are scheduled for March 2027, with selection results by the end of March.",
        ),
        "application_route": fact("https://application.epog.eu/", "CONFIRMED", [eap_apply, epog_admission, epog_platform], "Apply through the EPOG consortium portal, not the standard UniTo application route."),
        "program_specific_requirements_2027_2028": fact(
            {"consortium_call":{"prior_degree":"Bachelor's or equivalent, minimum 180 ECTS", "economics_ects":24, "statistics_or_econometrics_ects":6, "motivation":"Clear motivation for the programme"}, "unito_profile":{"economics_cfu":18, "statistics_cfu":6}, "eap_application_checklist":{"economics_ects":24, "statistics_or_econometrics_ects":6}, "documents":["CV", "diploma", "academic transcripts", "English proficiency evidence", "statement of purpose up to 500 words", "two recommendation letters", "passport"], "scholarship_applicants_additional_document":"Proof of place of residence issued within the previous 12 months, plus signed residence history declaration"},
            "REQUIRES_VERIFICATION", [eap_profile, eap_apply, epog_admission],
            "The actual EPOG 2027–2029 call and the EAP checklist require 24 ECTS in economics plus 6 ECTS in statistics/econometrics. UniTo's central course profile instead says 18 CFU economics plus 6 statistics. Keep both claims visible and obtain clarification before treating the local course-profile threshold as aligned with the consortium selection threshold.",
        ),
        "english_language_requirement_2027_2028": fact(
            {"minimum":"CEFR C1", "accepted_equivalents":{"TOEFL_iBT":95, "IELTS_Academic":7.0, "CAE":"Grade B", "CPE":"Grade C", "PTE_Academic":67}, "alternatives":"Native English speakers and applicants with a higher-education degree entirely taught in English may be exempt from an individual test", "evidence_deadline":"10 June (local exceptions may require end of April)"},
            "CONFIRMED", [epog_admission, eap_apply],
            "Current consortium 2027–2029 admission guidance; specific pathway/local-document checks may apply.",
        ),
        "selection_process_2027_2028": fact(
            {"consortium_interviews":"March 2027", "results":"End of March 2027", "local_course_check":"UniTo course profile describes a 15-minute Zoom TAPP interview after curricular evaluation"},
            "CONFIRMED", [epog_admission, eap_profile],
            "The EPOG interview window is stated for the 2027–2029 cohort. The separate local TAPP description is on the current course profile and is not itself labelled with an academic year.",
        ),
        "application_fee_2027_2028": fact(
            None, "REQUIRES_VERIFICATION", [epog_platform, eap_apply],
            "No application fee is stated on the reviewed consortium platform or programme checklist. Do not infer that the standard UniTo €60 foreign-qualification fee applies to the separate EPOG application.",
        ),
        "tuition_2027_2028": fact(
            {"published_general_policy_not_cycle_labelled":{"fee_below_personal_income_threshold_eur_per_year":1000, "personal_income_threshold_eur_per_year":26400, "includes":"Required health and accident insurance", "above_threshold_possible_fee_eur_per_year":9600, "erasmus_mundus_scholarship_holder":"Complete fee waiver", "non_scholarship_holder":"May request full or partial fee waiver"}},
            "REQUIRES_VERIFICATION", [epog_tuition, epog_scholarship],
            "These are the consortium's current published general two-year EPOG fee terms; the page does not explicitly label them for 2027–2029. Confirm the cohort-specific fee schedule before presenting them as a settled 2027/28 tuition amount.",
        ),
        "scholarships_2027_2028": fact(
            {"scheme":"Erasmus Mundus Joint Master scholarship", "published_general_terms":{"monthly_allowance_eur":1400, "duration":"Both academic years", "covers":["Tuition fees", "Required health and accident insurance"], "eligible_nationalities":"All, if academic conditions are met", "exclusions":["Previous EMJM scholarship holder", "Cannot combine with another EU-funded scholarship for the same course"]}, "2027_2029_award_count":None},
            "REQUIRES_VERIFICATION", [epog_scholarship, epog_admission],
            "The official scholarship page publishes the general EPOG EMJM award terms, but neither it nor the active call states the number of scholarships allocated to the 2027–2029 cohort. Treat award funding as competitive and cohort count/selection as unconfirmed.",
        ),
        "published_emjm_scholarship_terms": fact(
            {"monthly_allowance_eur":1400, "duration":"Both academic years", "tuition_and_insurance_covered":True, "eligibility":"Applicants of any nationality who meet academic requirements, except prior EMJM scholarship recipients", "eu_grant_combination":"No other EU-funded scholarship for the same course"},
            "CONFIRMED", [epog_scholarship],
            "General official scheme terms; 2027–2029 award count and cohort-specific allocation are not published on the reviewed page.",
        ),
        "application_documents_2027_2028": fact(
            ["Completed online EPOG application", "Full CV", "Degree certificate (at least 180 ECTS)", "Academic transcripts", "English proficiency evidence", "Statement of purpose (maximum 500 words)", "Two recommendation letters", "Passport", "Residence evidence and signed residence-history declaration for Erasmus Mundus scholarship applicants"],
            "CONFIRMED", [eap_apply, epog_admission],
        ),
        "acceptance_rate": fact(None, "UNAVAILABLE", [epog_admission], "No comparable applicant and admitted-student totals are published on the reviewed official call pages; no acceptance rate is inferred."),
    }
    eap["last_checked"] = "2026-11-11"
    eap["previous_cycle_tags"] = None
    programs.append(eap)

    apply_legacy_course_reviews(programs, fact)

    clinical_psych = by_id["legacy-159"]
    clinical_sources = [
        "SRC-PADOVA-CLINICAL-PSYCHOLOGY-2026",
        "SRC-PADOVA-PSYCHOLOGY-MSC-2026",
        "SRC-PADOVA-PSYCHOLOGY-CALL-2026",
        "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026",
        "SRC-PADUA-TUITION-2026",
        "SRC-PADOVA-REGIONAL-SCHOLARSHIP-2026",
    ]
    clinical_psych["program"] = "Psicologia clinica"
    clinical_psych["level"] = fact(
        "MSc", "REQUIRES_VERIFICATION", clinical_sources,
        "The two-year Laurea Magistrale (LM-51 R) is confirmed for 2026/27. The 2027/28 course listing has not yet been published.",
    )
    clinical_psych["language"] = fact(
        "Italian", "REQUIRES_VERIFICATION", clinical_sources,
        "The official profile and 2026/27 call identify Italian as the teaching language; no 2027/28 listing has been published.",
    )
    clinical_psych["field"] = fact("Clinical Psychology", "REQUIRES_VERIFICATION", clinical_sources)
    clinical_psych["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", ["SRC-PADOVA-PSYCHOLOGY-MSC-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
        "The official Psychology admissions catalogue and linked calls reviewed on 11 November 2026 are explicitly for 2026/27. No 2027/28 first-year listing or call was found; this is not evidence of discontinuation.",
    )
    clinical_psych["overall_status"] = "REQUIRES_VERIFICATION"
    clinical_psych["source_ids"] = clinical_sources
    clinical_psych["previous_cycle_tags"] = {
        "level": "MSc", "language": "Italian", "field": "Clinical Psychology",
        "cycle": "2026-2027",
        "label": "Official course and 2026/27 admission routes reviewed; 2027/28 intake and terms not yet published",
    }
    clinical_psych["facts"] = {
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Psicologia clinica", "degree": "Two-year Laurea Magistrale", "degree_class": "LM-51 R", "duration_years": 2, "location": "Padua", "study_mode": "In person", "teaching_language": "Italian", "admission": "Restricted access", "professional_qualification": "The degree is habilitating for psychologist practice in Italy, subject to required professional practical-evaluation training"},
            "CONFIRMED", ["SRC-PADOVA-CLINICAL-PSYCHOLOGY-2026", "SRC-PADOVA-PSYCHOLOGY-MSC-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
            "This confirms the prior cycle only; course accreditation and activation remain subject to the University's stated conditions.",
        ),
        "previous_cycle_available_places": fact(
            {"academic_year": "2026/27", "eu_or_equivalent_selection": 116, "non_eu_resident_abroad_selection": 9, "marco_polo_places_in_non_eu_quota": 2},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "The calls use separate applicant-category selections. The nine non-EU-abroad places include two Marco Polo places and must not be mistaken for additional seats in the EU/equivalent selection.",
        ),
        "previous_cycle_admission_requirements": fact(
            {"eu_or_equivalent": {"qualifying_degree": "First-cycle university qualification or recognized equivalent, earned by 30 September 2026", "minimum_psychology_credits": 88, "credit_sector_minima": {"M-PSI/01": 4, "M-PSI/02": 4, "M-PSI/03": 4, "M-PSI/04": 4, "M-PSI/05": 4, "at_least_one_of": {"M-PSI/06": 4, "M-PSI/07": 4, "M-PSI/08": 4}}, "weighted_average_minimum": "24/30 across the highest 88 CFU in M-PSI sectors", "english": "B2 CEFR"}, "non_eu_resident_abroad": {"qualifying_degree": "Foreign first-cycle university degree of at least three years, earned by 31 July 2026", "subject_background": ["General psychology", "Psychobiology", "Psychometrics", "Developmental and educational psychology", "Social psychology", "Work and organizational psychology", "Dynamic psychology", "Clinical psychology"], "italian": "B2 CEFR", "english": "B2 CEFR"}},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "The two categories have separate calls and different document/timing procedures; do not mix one category's deadlines or requirements with the other.",
        ),
        "previous_cycle_admission": fact(
            {"academic_year": "2026/27", "access": "Restricted / programmed access", "eu_or_equivalent_selection": "Ranked by M-PSI coursework score; no written entrance test is specified in the reviewed call", "international_non_eu_abroad_selection": "Committee assessment of curriculum and personal preparation; possible video interview", "tie_break": "Younger candidate has precedence"},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "These routes and selection methods are specific to the 2026/27 calls and do not establish 2027/28 procedures.",
        ),
        "previous_cycle_entrance_test": fact(
            {"academic_year": "2026/27", "eu_or_equivalent": "The call specifies a merit ranking from M-PSI grades and CFU, not a written entrance test", "ranking_formula": "Sum of each M-PSI examination grade multiplied by its CFU, up to 110 CFU; 30 e lode is counted as 33; when over 110 CFU, the higher-mark credits are used", "tie_break": "Younger candidate has precedence", "non_eu_resident_abroad": "Committee review may include a video interview"},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "This describes the 2026/27 selection only; the next-cycle selection format has not been published.",
        ),
        "previous_cycle_application_windows": fact(
            {"academic_year": "2026/27", "eu_or_equivalent": {"pre_enrolment_start": "2026-07-15 15:00", "pre_enrolment_deadline": "2026-09-01 12:00", "curricular_review_deadline": "2026-09-01 15:00", "maximum_ordered_preferences": 3, "first_ranking": "2026-09-14 15:00", "initial_enrolment": "2026-09-15 through 2026-09-17 15:00", "vacancy_round": "New pre-enrolment 2026-10-07 through 2026-10-09; subsequent reassignment/enrolment schedule through 2026-10-26"}, "non_eu_resident_abroad": {"application_start": "2026-01-07", "application_deadline": "2026-03-07 23:59 local time", "maximum_programme_applications": 2, "results_from": "2026-04-10", "degree_and_language_documents_deadline": "2026-07-31"}},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "All dates are historical 2026/27 deadlines, recorded to prevent accidental reuse for 2027/28.",
        ),
        "previous_cycle_application_fee": fact(
            {"academic_year": "2026/27", "eu_or_equivalent_selection_contribution_eur": 30, "non_eu_abroad_pre_enrolment_contribution_eur": 60, "non_eu_contribution_refundable": False},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "The €30 Uniweb selection contribution and €60 apply to different applicant routes; neither is the tuition charge. The non-EU call permits up to two course applications.",
        ),
        "previous_cycle_enrollment_contribution": fact(
            {"academic_year": "2026/27", "amount_eur": 205, "description": "Initial contribution quoted in the non-EU call, including regional right-to-study tax and stamp duty; amount may change annually"},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "This is the call's then-current initial enrollment contribution, separate from the €60 application charge and the annual tuition amount.",
        ),
        "previous_cycle_english_requirement": fact(
            {"academic_year": "2026/27", "eu_or_equivalent": "B2 CEFR", "non_eu_resident_abroad": "B2 CEFR"},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "The annual 2026/27 calls state B2; do not assume this certificate rule for 2027/28 until the new call is issued.",
        ),
        "previous_cycle_italian_requirement": fact(
            {"academic_year": "2026/27", "non_eu_resident_abroad": "B2 CEFR or equivalent"},
            "CONFIRMED", ["SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "The non-EU-abroad call explicitly requires Italian B2 for this Italian-taught degree; no separate Italian certificate threshold is stated in the EU/equivalent call.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "course_specific_amount": None, "general_degree_fee_guidance_eur_per_year": "€0 to approximately €3,000", "basis": "Varies by programme, income and residence category", "first_year_initial_installment_eur": 208},
            "CONFIRMED", ["SRC-PADUA-TUITION-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
            "General University tariff context, not a Clinical Psychology quote. The course call directs students to the annual fee schedule and Uniweb; first-installment components/amounts are subject to annual update.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "regional_right_to_study_scholarship": {"type": "Competitive; not guaranteed or course-specific", "eligible_degree_level": "Laurea Magistrale", "economic_and_merit_requirements": True, "published_isee_limit_eur": 26306.25, "published_ispe_limit_eur": 43125.94, "application_step_deadline": "2026-09-30"}},
            "CONFIRMED", ["SRC-PADOVA-REGIONAL-SCHOLARSHIP-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
            "Eligibility and award depend on the regional annual call, economic/merit requirements and applicant circumstances; no individual award is implied.",
        ),
        "application_windows": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-PADOVA-PSYCHOLOGY-MSC-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
            "The official admissions index and its linked call reviewed on 11 November 2026 remain for 2026/27. Do not reuse the prior-cycle dates.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "No 2027/28 selection contribution has been published; prior-cycle route-specific amounts are historical.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-PADOVA-PSYCHOLOGY-MSC-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
            "No 2027/28 call or updated curricular/language requirements were identified. The 2026/27 thresholds are preserved as historical facts only.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-PADUA-TUITION-2026", "SRC-PADOVA-PSYCHOLOGY-CALL-2026"],
            "The University fee page and call reviewed on 11 November 2026 provide 2026/27 information only; no 2027/28 annual schedule or course-specific amount was found.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-PADOVA-REGIONAL-SCHOLARSHIP-2026", "SRC-PADOVA-PSYCHOLOGY-MSC-2026"],
            "The regional aid page links the 2026/27 competition only. No 2027/28 regional, university or course-specific scholarship call was identified.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-PADOVA-PSYCHOLOGY-CALL-2026", "SRC-PADOVA-PSYCHOLOGY-NON-EU-CALL-2026"],
            "The calls list available places but do not provide comparable applicant and admitted counts; no acceptance rate is inferred.",
        ),
    }
    clinical_psych["last_checked"] = "2026-11-11"

    medicine = next(program for program in programs if program.get("id") == "legacy-153")
    medicine_sources = [
        "SRC-SAPIENZA-MEDICINE-2026",
        "SRC-SAPIENZA-MEDICINE-VARIANTS-2026",
        "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026",
        "SRC-SAPIENZA-MEDICINE-F-CALL-2026",
        "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026",
        "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026",
        "SRC-SAPIENZA-INTL-OFFICE-2026",
        "SRC-SAPIENZA-FEES-2026",
        "SRC-SAPIENZA-FEE-TABLE-2026",
        "SRC-SAPIENZA-WANTED-BEST-2026",
        "SRC-SAPIENZA-DISCO-LAZIO-2026",
    ]
    medicine["program"] = "Medicina e Chirurgia (campus/track unresolved)"
    medicine["level"] = fact(
        "Single-cycle Master's (LM-41)", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026"],
        "All reviewed 2026/27 variants are six-year LM-41 single-cycle Master's degrees; verify which variant, if any, is offered for first-year entry in 2027/28.",
    )
    medicine["language"] = fact(
        "Italian and English (distinct course variants)", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026"],
        "2026/27 catalogue has eight Italian variants and one distinct English variant; the legacy record does not identify one course and no 2027/28 course listing has been found.",
    )
    medicine["field"] = fact(
        "Medicine and Surgery", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026"],
        "Historical course identity only; the legacy row is an unresolved umbrella and 2027/28 offer remains unpublished.",
    )
    medicine["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026", "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026"],
        "Not yet announced for 2027/28 in the official Sapienza catalogue, course page and admissions material reviewed on 11 November 2026. The prior tracker did not identify a campus or track, so the nine 2026/27 variants remain an umbrella identity match; absence of a 2027/28 call is not treated as discontinuation.",
    )
    medicine["overall_status"] = "REQUIRES_VERIFICATION"
    medicine["source_ids"] = medicine_sources
    medicine["facts"] = {
        "previous_cycle_course_listing": fact(
            {
                "academic_year": "2026/27",
                "degree_class": "LM-41",
                "duration_years": 6,
                "degree_type": "Single-cycle Master's degree",
                "italian_taught_variants": [
                    {"name": "Medicina e chirurgia A", "course_code": "33452", "campus": "Policlinico Umberto I", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia B", "course_code": "33559", "campus": "Policlinico Umberto I", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia C", "course_code": "33560", "campus": "Policlinico Umberto I", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia D", "course_code": "33561", "campus": "Policlinico Umberto I", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia E", "course_code": "33453", "campus": "Polo Pontino", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia HT", "course_code": "33562", "campus": "Rome", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia", "course_code": "33567", "campus": "Sant'Andrea", "admission_route": "Semestre filtro"},
                    {"name": "Medicina e chirurgia G", "course_code": "32925", "campus": "Rieti", "admission_route": "Semestre filtro"},
                ],
                "english_taught_variant": {"name": "Medicine and Surgery F", "course_code": "33454", "campus": "Rome", "admission_route": "Admission test"},
                "legacy_match": "Unresolved umbrella entry; the previous tracker supplied no course code, campus or track, so no single variant is assigned.",
            },
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026"],
            "The catalogue confirms the cycle-specific course variants, class, duration, language and admission-route split for 2026/27 only. It does not establish that every variant will accept a new cohort in 2027/28.",
        ),
        "previous_cycle_admission_routes": fact(
            {
                "italian_taught_variants": {
                    "route": "National open semester (semestre aperto/semestre filtro)",
                    "universitaly_registration": {"start": "2026-07-13", "deadline": "2026-08-03 18:00 Europe/Rome"},
                    "sapienza_contribution_deadline": "2026-08-06",
                    "sapienza_campus_choices_for_later_study": ["Policlinico", "HT", "Sant'Andrea", "Polo Pontino", "Rieti"],
                    "registration_notes": "Candidates selected the Sapienza teaching location for the semester and listed course locations/preferences for the post-semester ranking; this is a prior-cycle process, not a 2027/28 timetable.",
                },
                "english_taught_F_variant": {
                    "route": "Separate national English-language admission test and ranking",
                    "universitaly_registration": {"start": "2026-08-26", "deadline": "2026-09-09 15:00 Europe/Rome"},
                    "infostud_registration_if_testing_at_sapienza": {"start": "2026-08-07", "deadline": "2026-09-09"},
                    "test_date": "2026-09-29",
                    "non_eu_abroad_visa_pre_enrolment_deadline": "2026-06-30",
                },
            },
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "These are distinct 2026/27 routes. The Italian open semester and the English F admission-test call must not be combined as if they applied to the same track.",
        ),
        "previous_cycle_application_windows": fact(
            {
                "italian_open_semester": {"universitaly_registration": ["2026-07-13", "2026-08-03 18:00 Europe/Rome"], "sapienza_payment_deadline": "2026-08-06", "exam_sessions": ["2026-12-10", "2027-01-11"]},
                "english_F": {"universitaly_registration": ["2026-08-26", "2026-09-09 15:00 Europe/Rome"], "test": "2026-09-29", "first_national_ranking": "2026-10-26", "first_later_scroll": "2026-11-03"},
            },
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "Expired dates for AY 2026/27 only. English F's non-EU applicants resident abroad also had to submit Universitaly visa pre-enrolment by 30 June 2026; the open-semester page states the same outer deadline for visa applicants.",
        ),
        "previous_cycle_available_places": fact(
            {"english_F_2026_27": {"italian_eu_and_equivalent": 52, "non_eu_resident_abroad": 13}, "italian_open_semester_variants": "Course-level 2026/27 seat totals are not stated in the reviewed Sapienza open-semester guidance."},
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-F-CALL-2026", "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026"],
            "The 65-seat split is for English course F only and is not a total for all Sapienza Medicine variants. No Italian-route capacity is inferred.",
        ),
        "previous_cycle_admission_requirements": fact(
            {
                "italian_taught_open_semester": {"secondary_credential": "Upper-secondary diploma obtained or expected in 2026", "non_eu_abroad_visa_applicants": {"universitaly_pre_enrolment_deadline": "2026-06-30", "italian_language": "B2 test or recognized certificate"}},
                "english_taught_F": {"secondary_credential": "Upper-secondary diploma obtained or expected in 2026", "non_eu_abroad_visa_applicants": {"universitaly_pre_enrolment_deadline": "2026-06-30"}, "english_certificates": "Recognized certificates (including listed B2 levels) are used as ranking tie-break evidence; the reviewed call does not state a separate minimum English certificate as an entry requirement.", "gpa": "No separate GPA threshold stated in the reviewed 2026/27 call."},
            },
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "These historical rules are route-specific. Foreign credentials require the University’s document and qualification review. Do not transfer them to 2027/28 without the new call.",
        ),
        "previous_cycle_entrance_test": fact(
            {
                "italian_taught_open_semester": {"subjects": [{"name": "Biology", "cfu": 6}, {"name": "Chemistry and Biochemical Preparations", "cfu": 6}, {"name": "Physics", "cfu": 6}], "attendance": "Compulsory, with exemptions described by the University", "exam_format_each": "31 completion items and 21 multiple-choice items; 50 minutes", "scoring_each": {"correct": 1, "incorrect": -0.1, "blank": 0}, "exam_dates": ["2026-12-10", "2027-01-11"], "ranking": "Three sections ordered by number of passed exams and score; best of two attempts is used and must exceed 18/30."},
                "english_taught_F": {"test_format": "60 multiple-choice questions", "duration_minutes": 100, "question_distribution": {"reading_and_study_knowledge": 4, "logic": 5, "biology": 23, "chemistry": 15, "physics_and_mathematics": 13}, "scoring": {"correct": 1.5, "incorrect": -0.4, "blank": 0}, "ranking_threshold": {"italian_eu_equivalent": "At least 20 points", "non_eu_resident_abroad": "Above 0 points"}, "ofa": "Biology and/or Chemistry OFA could be assigned under the call's subject-score thresholds."},
            },
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "Test and ranking rules vary by 2026/27 route. The 60-question test is the English F admission test, not the Italian open-semester exam.",
        ),
        "previous_cycle_route_contributions": fact(
            {
                "italian_open_semester_registration": {"standard_eur": 250, "isee_between_22000_and_30000_eur": 200, "full_exemption_including": ["ISEE up to €22,000 when available in Infostud by deadline", "certified disability/invalidity at least 66%", "DiSCo Lazio award or eligibility for 2026/27", "MAECI scholarship for 2026/27"], "deadline": "2026-08-06"},
                "english_F_test_payment": {"required": True, "amount": None, "payment_platform": "Universitaly", "amount_status": "Not stated in the Sapienza 2026/27 call"},
            },
            "CONFIRMED", ["SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "The €250/€200 amount is the Italian open-semester contribution, not a programme application fee or an annual tuition quote. The English test call requires a participation payment but publishes no amount.",
        ),
        "previous_cycle_application_fee": fact(
            None, "UNAVAILABLE", ["SRC-SAPIENZA-MEDICINE-F-CALL-2026", "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026"],
            "No separate course application-fee amount is published in the reviewed 2026/27 calls. The €250 open-semester contribution is recorded separately; the English test fee is paid through Universitaly but its amount is not given in Sapienza's call.",
        ),
        "application_windows_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026", "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026"],
            "Not yet announced for 2027/28 in the reviewed Sapienza catalogue and admissions pages as of 11 November 2026. Do not reuse the 2026/27 open-semester or English-test calendar.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026", "SRC-SAPIENZA-MEDICINE-OPEN-SEMESTER-2026"],
            "Not yet announced for 2027/28. Prior-cycle route contributions and the unspecified English test-payment amount are not carried forward.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-PROFILE-2026"],
            "Not yet announced for 2027/28 in the course catalogue or admissions material reviewed as of 11 November 2026.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "ordinary_second_contribution_group_total_eur": 2924, "scope": "Standard amount for courses in the Farmacia e Medicina, Medicina e Odontoiatria, Medicina e Psicologia and other listed faculty groups", "ordinary_installment_percentages": [30, 35, 35], "foreign_income_fixed_contribution_bands_eur": [300, 700, 1500], "amount_varies_by": ["ISEE and merit benefits", "course contribution group", "residence/income rules and exemptions"], "regional_tax_and_stamp_duty": "Additional where due (2026/27 call cites €140 regional tax plus €16 stamp duty for the English route)"},
            "CONFIRMED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "This is the official ordinary 2026/27 fee-table reference, not an individual bill or a 2027/28 amount. The €250 Italian open-semester contribution is recorded separately; the final contribution is subject to Sapienza rules and the student's case.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "Not yet announced for 2027/28 in the official fee pages reviewed as of 11 November 2026.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "Wanted_the_Best": {"awards": 85, "gross_eur_per_year": 3000, "duration_years": 2, "deadline": "2026-10-30", "scope": "Competitive award for eligible entrants with a first degree from another Italian university who enrol in a Sapienza Master's degree; applicability to this unresolved single-cycle Medicine umbrella is not confirmed"}, "DiSCo_Lazio": {"application_deadline_after_extension": "2026-07-23 20:00", "corrections_deadline": "2026-08-11 12:00", "scope": "Competitive regional right-to-study benefits; subject to annual economic and merit conditions"}},
            "CONFIRMED", ["SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "Historical 2026/27 schemes only. Wanted the Best is not represented as eligible for the LM-41 single-cycle degree without a course-specific statement; DiSCo is a separate competitive regional scheme.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "Not yet announced for 2027/28 in the new-entrant calls reviewed as of 11 November 2026.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-SAPIENZA-MEDICINE-VARIANTS-2026", "SRC-SAPIENZA-MEDICINE-F-CALL-2026"],
            "No comparable applicant and admitted-student denominator is supplied for this unmatched umbrella record; no acceptance rate is inferred.",
        ),
    }
    medicine["previous_cycle_tags"] = {
        "level": "Single-cycle Master's (LM-41)",
        "language": "Italian and English (distinct course variants)",
        "field": "Medicine and Surgery",
        "cycle": "2026-2027",
        "label": "Official 2026/27 evidence; generic legacy row does not identify one of the nine course variants; 2027/28 intake remains unannounced",
    }
    medicine["last_checked"] = "2026-11-11"

    aerospace = next(program for program in programs if program.get("id") == "legacy-154")
    aerospace_sources = [
        "SRC-SAPIENZA-AEROSPACE-BSC-2026",
        "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026",
        "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026",
        "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026",
        "SRC-SAPIENZA-FEES-2026",
        "SRC-SAPIENZA-FEE-TABLE-2026",
        "SRC-SAPIENZA-WANTED-BEST-2026",
        "SRC-SAPIENZA-DISCO-LAZIO-2026",
        "SRC-SAPIENZA-SCHOLARSHIPS-2026",
    ]
    aerospace["program"] = "Ingegneria Aerospaziale"
    aerospace["city"] = "Rome"
    aerospace["level"] = fact(
        "Bachelor's degree (Laurea, class L-9)", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-AEROSPACE-BSC-2026", "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
        "The 2026/27 profile and admission call agree on course 33474, class L-9 and a three-year Laurea. 2027/28 catalogue identity remains to be checked.",
    )
    aerospace["language"] = fact(
        "Italian", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-AEROSPACE-BSC-2026"],
        "Official delivery is Italian for 2026/27; verify the 2027/28 course profile.",
    )
    aerospace["field"] = fact(
        "Aerospace Engineering", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-AEROSPACE-BSC-2026"],
        "Official course identity is confirmed for 2026/27 only; the 2027/28 catalogue has not yet confirmed this new-entry row.",
    )
    aerospace["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-AEROSPACE-BSC-2026", "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026", "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026"],
        "No 2027/28 first-year Aerospace Engineering intake or admission call appears in the official course profile, Faculty call index or current engineering admissions page reviewed on 11 November 2026. The profile's 2027/28 laboratory assignment notice is for students already in year three and is not new-entry evidence; absence of a new call is not treated as discontinuation.",
    )
    aerospace["overall_status"] = "REQUIRES_VERIFICATION"
    aerospace["source_ids"] = aerospace_sources
    aerospace["facts"] = {
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Ingegneria Aerospaziale", "course_code": "33474", "selection_code": "14616", "degree_class": "L-9", "duration_years": 3, "degree_type": "Bachelor's degree (Laurea)", "campus": "Rome", "language": "Italian", "access": "Restricted access by TOLC-I selection", "department": "Mechanical and Aerospace Engineering"},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-BSC-2026", "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
            "This is the official AY 2026/27 course identity; it does not by itself establish a 2027/28 intake.",
        ),
        "previous_cycle_admission_routes": fact(
            {"academic_year": "2026/27", "route": "Three Sapienza selections using CISIA TOLC-I or TOLC@CASA, Infostud registration and a course preference", "selections": ["First selection", "Second selection", "Third selection"], "first_and_second_selection_scrolling": False, "third_selection_scrolling": True, "valid_test_period_start": "2025-01-01", "best_valid_test_score_used": True},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026"],
            "Selection structure is specific to the 2026/27 call; the next annual call may differ.",
        ),
        "previous_cycle_application_windows": fact(
            {"academic_year": "2026/27", "selection_1": {"application_and_test_deadline": "2026-04-27", "window_start": "2026-04-01", "score_list": "2026-04-30", "ranking": "2026-05-11", "pre_enrolment_payment": ["2026-05-11", "2026-05-20"], "final_enrolment_payment": ["2026-09-01", "2026-09-07"]}, "selection_2": {"window": ["2026-05-20", "2026-07-20"], "test_deadline": "2026-07-20", "effective_places_published": "2026-05-25", "score_list": "2026-07-23", "ranking": "2026-07-31", "enrolment_payment": ["2026-09-01", "2026-09-07"]}, "selection_3": {"window": ["2026-07-31", "2026-09-07"], "test_deadline": "2026-09-07", "effective_places_published": "2026-09-08", "score_list": "2026-09-10", "ranking": "2026-09-17", "enrolment_payment_deadline": "2026-09-22", "first_scroll_payment_deadline": "2026-09-29", "second_scroll_payment_deadline": "2026-10-05", "third_scroll_payment_deadline": "2026-10-12", "vacant_place_notice_deadline": "2026-10-22"}},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026"],
            "Expired AY 2026/27 dates only. The live results page states all course places were assigned after the second scrolling, so the call's planned third Aerospace scrolling was not published.",
        ),
        "previous_cycle_available_places": fact(
            {"academic_year": "2026/27", "total": 250, "first_selection_eu_and_equivalent": 60, "second_selection_eu_and_equivalent": "110 plus any places left unfilled in selection one", "third_selection_eu_and_equivalent": "72 plus any places left unfilled in selection two", "third_selection_non_eu_resident_abroad_with_visa": 8, "marco_polo_reserved_within_non_eu_quota": 1},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
            "The round figures are the call's initial distribution. Unfilled places flow to later rounds and must not be added a second time to the stated 250 total.",
        ),
        "previous_cycle_admission_requirements": fact(
            {"academic_year": "2026/27", "italian_eu_and_equivalent": {"secondary_credential": "Upper-secondary school diploma obtained or expected in 2026", "test": "TOLC-I or TOLC@CASA at Sapienza or another CISIA university; valid from 1 January 2025 through the selected round deadline"}, "non_eu_resident_abroad_requiring_study_visa": {"eligible_selection": "Third selection only", "secondary_credential": "Upper-secondary school diploma obtained or expected in 2026", "universitaly_pre_enrolment_deadline": "2026-06-30", "italian_language": "B2 test or recognized certificate"}, "foreign_secondary_qualification": "Sapienza qualification and document checks apply", "separate_gpa_threshold": "Not stated in the reviewed call"},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
            "The non-EU visa route is limited to applicants resident abroad who require a study visa; it is distinct from the EU/equivalent quota.",
        ),
        "previous_cycle_entrance_test": fact(
            {"test": "CISIA TOLC-I / TOLC@CASA", "scored_questions": 50, "sections": [{"name": "Mathematics", "questions": 20, "minutes": 50}, {"name": "Science", "questions": 10, "minutes": 20}, {"name": "Logic", "questions": 10, "minutes": 20}, {"name": "Verbal comprehension", "questions": 10, "minutes": 20}], "scored_duration_minutes": 110, "additional_english_section": {"questions": 30, "minutes": 15, "included_in_admission_score": False}, "scoring": {"correct": 1, "incorrect": -0.25, "blank": 0}, "retake_rule": "At most once in each calendar month; best valid test score is considered", "minimum_score": {"selection_1": "At least 18/50", "selection_2": "At least 18/50", "selection_3": "Above 0/50"}, "mathematics_ofa": "Applicants who matriculate with less than 18/50 receive a Mathematics OFA under the call conditions"},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
            "The extra English section does not contribute to the score used for selection. These are prior-cycle exam details only.",
        ),
        "previous_cycle_application_fee": fact(
            {"academic_year": "2026/27", "sapienza_selection_contribution_eur": 10, "sapienza_contribution_scope": "Per selection; non-refundable", "cisia_tolc_registration_fee_eur": 35, "cisia_fee_scope": "Separate payment to CISIA to take TOLC-I", "first_selection_pre_enrolment_contribution_eur": 200, "pre_enrolment_contribution_scope": "Only for eligible first-selection candidates; ISEE reductions or exemptions may apply; credited toward course tuition; not an application fee"},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
            "The €10 Sapienza charge is required for each selection and the €35 CISIA test charge is a separate payment. The €200 pre-enrolment amount is a later tuition advance, not an application fee.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "bachelor_course_specific_annual_total_eur": None, "amount_status": "No Aerospace BSc total is stated in the reviewed admission call or official tuition pages", "payment_installments_percent": [30, 35, 35], "calculation": "ISEE-based contribution rules and any applicable benefits/exemptions; the first-round €200 pre-enrolment payment is credited toward tuition", "additional_amounts": ["Regional tax, where due", "€16 stamp duty"], "foreign_income_fixed_contribution_bands_eur": [300, 700, 1500], "not_applied_reference": "The €2,924 Art. 38 contribution-group amount is scoped to second-level two-year, single-cycle and unified Master's programmes, not this three-year BSc"},
            "CONFIRMED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "2026/27 payment structure and ISEE treatment are confirmed, but a course-specific annual tuition total is not. The €2,924 Master's-group reference is deliberately excluded from this BSc record; no individual bill or total cost is inferred.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "DiSCo_Lazio": {"type": "Competitive regional right-to-study grant and related benefits", "application_deadline_after_extension": "2026-07-23 20:00", "corrections_deadline": "2026-08-11 12:00", "eligibility": "Subject to the annual economic, merit and other call requirements"}, "not_course_awards": {"Wanted_the_Best": "The 2026/27 award was limited to graduates of other Italian universities enrolling in a Sapienza Master's degree; it is not an Aerospace BSc entrant award"}},
            "CONFIRMED", ["SRC-SAPIENZA-DISCO-LAZIO-2026", "SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-SCHOLARSHIPS-2026"],
            "DiSCo Lazio is competitive regional aid, not a guaranteed course award. Wanted the Best is documented as an excluded Master's-only scheme. Other general benefits depend on personal eligibility and separate calls.",
        ),
        "application_windows_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-AEROSPACE-BSC-2026", "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026", "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026"],
            "No first-year 2027/28 selection dates were published on the reviewed course, faculty or engineering admissions pages as of 11 November 2026. The 2026/27 dates are not carried forward.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-AEROSPACE-ICI-CALLS-2026"],
            "No course-specific application or TOLC fee for the 2027/28 selection was announced in the reviewed official material.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-AEROSPACE-BSC-2026", "SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026"],
            "No 2027/28 call or named new-entry requirement was published on the reviewed course and admissions pages as of 11 November 2026.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "No 2027/28 tuition regulation or Aerospace BSc amount was published in the reviewed official pages as of 11 November 2026.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-SCHOLARSHIPS-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "No 2027/28 incoming-student scholarship call was present in the reviewed university and DiSCo material; do not assume 2026/27 competitions recur.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-SAPIENZA-AEROSPACE-ADMISSION-CALL-2026", "SRC-SAPIENZA-ENGINEERING-ADMISSIONS-2026"],
            "The official call gives capacity and later seat-fill status, but the reviewed evidence does not provide comparable total applicant and admitted-student counts for an acceptance-rate calculation.",
        ),
    }
    aerospace["previous_cycle_tags"] = {
        "level": "Bachelor's degree (Laurea, class L-9)",
        "language": "Italian",
        "field": "Aerospace Engineering",
        "cycle": "2026-2027",
        "label": "Official 2026/27 identity and admission call; 2027/28 first-year intake remains unannounced",
    }
    aerospace["last_checked"] = "2026-11-11"

    political_science = next(program for program in programs if program.get("id") == "legacy-155")
    political_science_sources = [
        "SRC-SAPIENZA-POLITICAL-SCIENCE-2026",
        "SRC-SAPIENZA-POLITICAL-SCIENCE-APPLY-2026",
        "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026",
        "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026",
        "SRC-SAPIENZA-OPEN-ACCESS-DEADLINE-EXTENSION-2026",
        "SRC-SAPIENZA-FEES-2026",
        "SRC-SAPIENZA-FEE-TABLE-2026",
        "SRC-SAPIENZA-DISCO-LAZIO-2026",
        "SRC-SAPIENZA-WANTED-BEST-2026",
        "SRC-SAPIENZA-SCHOLARSHIPS-2026",
    ]
    political_science["program"] = "Scienze politiche e relazioni internazionali"
    political_science["city"] = "Rome"
    political_science["level"] = fact(
        "Bachelor's degree (Laurea, class L-36)", "REQUIRES_VERIFICATION",
        ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026"],
        "The 2026/27 catalogue and call agree on course 33618, class L-36 and a three-year Laurea. 2027/28 catalogue identity remains to be checked.",
    )
    political_science["language"] = fact(
        "Italian", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026"],
        "Official delivery is Italian for 2026/27; verify the 2027/28 course profile.",
    )
    political_science["field"] = fact(
        "Political Science and International Relations", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026"],
        "Official course identity is confirmed for 2026/27 only; the 2027/28 catalogue has not yet confirmed this new-entry row.",
    )
    political_science["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", [
            "SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-APPLY-2026",
            "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026",
        ],
        "No 2027/28 course listing or first-year call appears in the official course profile, application page or central admissions index reviewed on 11 November 2026. The 2026/27 course is confirmed; absence of the new-cycle call is not treated as discontinuation.",
    )
    political_science["overall_status"] = "REQUIRES_VERIFICATION"
    political_science["source_ids"] = political_science_sources
    political_science["facts"] = {
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Scienze politiche e relazioni internazionali", "course_code": "33618", "test_code": "14620", "degree_class": "L-36", "duration_years": 3, "degree_type": "Bachelor's degree (Laurea)", "campus": "Rome", "language": "Italian", "access": "Open access with an entrance test for knowledge verification", "faculty": "Scienze Politiche, Sociologia, Comunicazione", "department": "Scienze Politiche"},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026"],
            "This is the official AY 2026/27 course identity; it does not by itself establish a 2027/28 intake.",
        ),
        "previous_cycle_admission_routes": fact(
            {"academic_year": "2026/27", "route": "Open access knowledge-verification test, not a competitive seat ranking", "standard_test": "CISIA TOLC-SU / TOLC@CASA", "test_code": "14620", "limited_exemption": "Applicants who took TOLC-SPS during 2025 were exempt from taking TOLC-SU under the call", "Infostud_registration": "Required", "competitive_selection": False},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026"],
            "The profile categorizes this as a test to verify knowledge and the University lists it among non-restricted courses. The result can assign OFA; the sources do not describe a ranking or fixed seat quota.",
        ),
        "previous_cycle_application_windows": fact(
            {"academic_year": "2026/27", "tolc_su": {"valid_from": "2025-01-01", "original_deadline": "2026-10-29", "later_extended_deadline": "2026-11-19"}, "sapienza_access_contribution": {"payment_open": "2026-07-02", "original_deadline": "2026-10-29", "later_extended_deadline": "2026-11-19"}, "first_tuition_installment": {"start": "2026-09-01", "original_deadline": "2026-11-05", "later_extended_deadline": "2026-11-25"}, "second_tuition_installment_deadline": "2026-12-27", "third_tuition_installment_deadline": "2027-03-25", "non_eu_abroad_visa_pre_enrolment_deadline": "2026-06-30"},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-OPEN-ACCESS-DEADLINE-EXTENSION-2026", "SRC-SAPIENZA-FEES-2026"],
            "These are historical 2026/27 dates. The University later extended the TOLC and €10 payment deadline to 19 November and the first tuition instalment to 25 November for non-restricted courses; do not copy them to 2027/28.",
        ),
        "previous_cycle_available_places": fact(
            None, "UNAVAILABLE", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026"],
            "The reviewed 2026/27 knowledge-verification call and admissions index do not state a fixed number of places or a competitive ranking; this is not a seat-count estimate.",
        ),
        "previous_cycle_admission_requirements": fact(
            {"academic_year": "2026/27", "italian_eu_and_equivalent": {"secondary_credential": "Upper-secondary school diploma obtained or expected in 2026", "test": "TOLC-SU or TOLC@CASA at Sapienza or another CISIA university, taken from January 2025 by the extended 19 November 2026 deadline", "test_exemption": "Call exempts applicants who took TOLC-SPS during 2025"}, "non_eu_resident_abroad_requiring_study_visa": {"secondary_credential": "Upper-secondary school diploma obtained or expected in 2026", "test": "TOLC-SU/TOLC@CASA under the call, subject to its stated exemption", "universitaly_pre_enrolment_deadline": "2026-06-30", "italian_language": "B2 test or recognized certificate"}, "foreign_secondary_qualification": "Sapienza qualification and document checks apply", "separate_gpa_threshold": "Not stated in the reviewed call"},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026"],
            "The non-EU visa route applies to applicants resident abroad who need a study visa and is separate from the EU/equivalent route. All criteria are prior-cycle only.",
        ),
        "previous_cycle_entrance_test": fact(
            {"test": "CISIA TOLC-SU / TOLC@CASA", "scored_questions": 50, "sections": [{"name": "Text comprehension and Italian language", "questions": 30, "minutes": 60}, {"name": "Knowledge and skills acquired in prior studies", "questions": 10, "minutes": 20}, {"name": "Logical reasoning", "questions": 10, "minutes": 20}], "scored_duration_minutes": 100, "additional_english_section": {"questions": 30, "minutes": 15, "included_in_knowledge_verification_score": False}, "scoring": {"correct": 1, "incorrect": -0.25, "blank": 0}, "retake_rule": "At most once per calendar month; the best total result is considered", "ofa_thresholds_in_2026_27_call": {"TOLC_SU": "OFA at <=18/50, excluding English", "TOLC_SPS": "OFA at <=12/40, excluding English"}, "ofa_resolution": "Recovery activities plus a course recovery test/interview or one of six listed first-year L-36 exams; OFA due by end of year one", "threshold_note": "The course application page carries a notice explicitly referring to the older 2025 D.R. 1696/2025 call and says scores >=18/50 (SU) or >=12/40 (SPS) avoid OFA. For the 2026/27 cycle, the specific D.R. 1296/2026 call sets OFA at <=18/50 and <=12/40; the score-18 boundary is flagged as a stale-page discrepancy."},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-APPLY-2026"],
            "The English section is separately scored and does not affect knowledge-verification or OFA thresholds. Because the course page's notice references a prior call, the 2026/27 admission call is the cycle-specific authority; verify an exact score of 18 with the course office if it affects enrollment.",
        ),
        "previous_cycle_application_fee": fact(
            {"academic_year": "2026/27", "sapienza_access_contribution_eur": 10, "sapienza_contribution_scope": "Required non-refundable Infostud access contribution for test-result acquisition; original due 29 October, extended to 19 November 2026", "cisia_tolc_su_registration_fee_eur": 35, "cisia_fee_scope": "Separate CISIA registration payment to sit TOLC-SU", "course_application_fee_label": "The call does not describe the Sapienza access contribution as a separate competitive application fee"},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-OPEN-ACCESS-DEADLINE-EXTENSION-2026"],
            "The €10 Infostud contribution and €35 CISIA TOLC charge are distinct and both were required under the 2026/27 procedure; these are not 2027/28 prices.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "bachelor_course_specific_annual_total_eur": None, "amount_status": "No Political Science L-36 annual total is stated in the reviewed call and tuition pages", "calculation": "ISEE-based Sapienza contribution rules and applicable benefits/exemptions", "payment_installments_percent": [30, 35, 35], "first_installment_extended_deadline": "2026-11-25", "additional_amounts": ["Regional tax, where due", "€16 stamp duty"], "not_applied_reference": "The €2,821 Art. 38 first-bracket total is scoped to second-level two-year, single-cycle and unified Master's degrees, not this three-year BSc"},
            "CONFIRMED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-OPEN-ACCESS-DEADLINE-EXTENSION-2026", "SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "The official pages confirm the ISEE-based framework and 30/35/35 payment structure, but not a course-specific BSc total. The €2,821 Art. 38 reference is expressly limited to second-level and single-cycle programmes; no individual bill is inferred.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "DiSCo_Lazio": {"type": "Competitive regional right-to-study grant and related benefits", "application_deadline_after_extension": "2026-07-23 20:00", "corrections_deadline": "2026-08-11 12:00", "eligibility": "Subject to annual economic, merit and other call requirements"}, "not_course_awards": {"Wanted_the_Best": "The 2026/27 award targets students entering Sapienza Master's degrees after graduating from another Italian university; it is not an incoming L-36 BSc award"}},
            "CONFIRMED", ["SRC-SAPIENZA-DISCO-LAZIO-2026", "SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-SCHOLARSHIPS-2026"],
            "DiSCo Lazio is competitive regional aid, not a guaranteed course award. The University's general inventory describes other limited eligibility schemes, but Wanted the Best is Master's-only and not a BSc entrant scholarship.",
        ),
        "application_windows_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-APPLY-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026"],
            "No first-year 2027/28 dates or new-cycle call appeared on the official course profile/application page or central admissions index reviewed on 11 November 2026. The amended 2026/27 dates are not carried forward.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026"],
            "No 2027/28 course access contribution or TOLC fee was announced in the reviewed official course and admissions material.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026"],
            "No 2027/28 first-year call or course-specific entry requirements were published in the reviewed catalogue and admissions pages as of 11 November 2026.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "The reviewed tuition pages display the 2026/27 framework; no 2027/28 tuition regulation or course-level annual amount was published as of 11 November 2026.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-SCHOLARSHIPS-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "No 2027/28 DiSCo annual call or incoming L-36 scholarship call was present in the reviewed official university and regional aid pages as of 11 November 2026. This does not mean students are ineligible for general aid once annual calls open.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-SAPIENZA-POLITICAL-SCIENCE-CALL-2026", "SRC-SAPIENZA-POLITICAL-SCIENCE-INDEX-2026"],
            "No competitive ranking, fixed place count, or comparable applicant/admitted denominator is supplied for this knowledge-verification route; no acceptance rate is inferred.",
        ),
    }
    political_science["previous_cycle_tags"] = {
        "level": "Bachelor's degree (Laurea, class L-36)",
        "language": "Italian",
        "field": "Political Science and International Relations",
        "cycle": "2026-2027",
        "label": "Official 2026/27 identity and open-access knowledge-verification call; 2027/28 first-year intake remains unannounced",
    }
    political_science["last_checked"] = "2026-11-11"

    psychology = next(program for program in programs if program.get("id") == "legacy-156")
    psychology_sources = [
        "SRC-SAPIENZA-PSYCHOLOGY-2026",
        "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026",
        "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026",
        "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026",
        "SRC-SAPIENZA-FEES-2026",
        "SRC-SAPIENZA-FEE-TABLE-2026",
        "SRC-SAPIENZA-DISCO-LAZIO-2026",
        "SRC-SAPIENZA-WANTED-BEST-2026",
        "SRC-SAPIENZA-SCHOLARSHIPS-2026",
    ]
    psychology["program"] = "Psicologia e Salute"
    psychology["city"] = "Rome"
    psychology["level"] = fact(
        "Bachelor's degree (Laurea, class L-24)", "REQUIRES_VERIFICATION",
        ["SRC-SAPIENZA-PSYCHOLOGY-2026", "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026"],
        "The 2026/27 catalogue and admission call agree on course 33570, class L-24 and a three-year Laurea. 2027/28 catalogue identity remains to be checked.",
    )
    psychology["language"] = fact(
        "Italian", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-PSYCHOLOGY-2026"],
        "Official delivery is Italian for 2026/27; verify the 2027/28 course profile.",
    )
    psychology["field"] = fact(
        "Psychology", "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-PSYCHOLOGY-2026"],
        "Official course identity is confirmed for 2026/27 only; the 2027/28 catalogue has not yet confirmed this new-entry row.",
    )
    psychology["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", [
            "SRC-SAPIENZA-PSYCHOLOGY-2026", "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026",
            "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026",
        ],
        "No 2027/28 course listing or first-year call appears in the official course profile, application/ranking page or central admissions index reviewed on 11 November 2026. The 2026/27 course is confirmed; absence of the new-cycle call is not treated as discontinuation.",
    )
    psychology["overall_status"] = "REQUIRES_VERIFICATION"
    psychology["source_ids"] = psychology_sources
    psychology["facts"] = {
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Psicologia e Salute", "course_code": "33570", "test_code": "05429", "degree_class": "L-24", "duration_years": 3, "degree_type": "Bachelor's degree (Laurea)", "campus": "Rome", "language": "Italian", "access": "Restricted access by ranked TOLC-PSI selection", "faculty": "Medicina e Psicologia", "department": "Psicologia Dinamica, Clinica e Salute"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-2026", "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026"],
            "This is the official AY 2026/27 course identity; it does not by itself establish a 2027/28 intake.",
        ),
        "previous_cycle_admission_routes": fact(
            {"academic_year": "2026/27", "route": "Competitive limited-access selection using TOLC-PSI/TOLC@CASA and merit ranking", "test_code": "05429", "ranking_minimum": "At least 23/50 in the five ranked TOLC-PSI sections", "test_score_rule": "Best valid TOLC-PSI score is used", "course_preference": "Choose one of four separate L-24 course rankings through Infostud; only the last valid preference is used"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026"],
            "The call treats the four L-24 programmes as separate rankings and permits a single course preference; the quota and score threshold recorded here are specifically for Psicologia e Salute.",
        ),
        "previous_cycle_application_windows": fact(
            {"academic_year": "2026/27", "selection_and_course_preference_window": ["2026-07-02", "2026-09-07"], "tolc_psi_deadline": "2026-09-07", "valid_test_period_start": "2025-01-01", "participant_score_list": "2026-09-09", "score_discrepancy_deadline": "2026-09-11", "initial_ranking_and_enrolment_start": "2026-09-17", "initial_winner_payment_deadline": "2026-09-22", "first_scrolling": {"published": "2026-09-24", "payment_deadline": "2026-09-28"}, "second_scrolling": {"published": "2026-10-01", "payment_deadline": "2026-10-06"}, "third_scrolling": {"published": "2026-10-08", "payment_deadline": "2026-10-13"}, "vacant_seat_notice": "2026-10-20", "vacancy_intention_deadline": "2026-10-27", "vacancy_list_and_payment_period": ["2026-11-05", "2026-11-11"], "non_eu_abroad_visa_pre_enrolment_deadline": "2026-06-30"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026"],
            "These are the prior-cycle competitive-selection and scrolling dates. The non-restricted-course November extension does not apply to this restricted-access selection.",
        ),
        "previous_cycle_available_places": fact(
            {"academic_year": "2026/27", "total": 285, "italian_eu_and_equivalent": 275, "non_eu_resident_abroad_requiring_study_visa": 10, "quota_reallocation": "Unused non-EU visa places may be made available to Italian/EU/equivalent applicants"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026"],
            "These are the initial places in the 2026/27 call. The 10-place quota is for non-EU applicants resident abroad who need a study visa; do not add the four course quotas together as a Psicologia e Salute count.",
        ),
        "previous_cycle_admission_requirements": fact(
            {"academic_year": "2026/27", "italian_eu_and_equivalent": {"secondary_credential": "Upper-secondary school diploma obtained or expected in 2026", "test": "TOLC-PSI or TOLC@CASA at Sapienza or another CISIA university, taken from January 2025 through 7 September 2026"}, "non_eu_resident_abroad_requiring_study_visa": {"secondary_credential": "Upper-secondary school diploma obtained or expected in 2026", "test": "TOLC-PSI or TOLC@CASA by 7 September 2026", "universitaly_pre_enrolment_deadline": "2026-06-30", "italian_language": "B2 test or recognized certificate"}, "foreign_secondary_qualification": "Sapienza qualification and document checks apply", "separate_gpa_threshold": "Not stated in the reviewed call"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026"],
            "The non-EU visa route is limited to applicants resident abroad who need a study visa; it is separate from the Italian/EU/equivalent quota. All criteria are prior-cycle only.",
        ),
        "previous_cycle_entrance_test": fact(
            {"test": "CISIA TOLC-PSI / TOLC@CASA", "scored_questions": 50, "sections": [{"name": "Text comprehension", "questions": 10, "minutes": 20}, {"name": "Basic mathematics", "questions": 10, "minutes": 20}, {"name": "Verbal reasoning", "questions": 10, "minutes": 25}, {"name": "Numerical reasoning", "questions": 10, "minutes": 20}, {"name": "Biology", "questions": 10, "minutes": 15}], "scored_duration_minutes": 100, "additional_english_section": {"questions": 30, "minutes": 15, "included_in_ranking": False, "used_for_english_ofa": True}, "scoring": {"correct": 1, "incorrect": -0.25, "blank": 0}, "ranking_minimum_score": "At least 23/50; English is excluded", "tie_break_order": ["Text comprehension", "Basic mathematics", "Verbal reasoning", "Numerical reasoning", "Biology", "Younger candidate"], "retake_rule": "At most once per calendar month; best valid result is used", "ofa_thresholds": {"Italian": "Score <=5 from combined text comprehension and verbal reasoning", "Mathematics": "Score <=5 from combined numerical reasoning and basic mathematics", "English": "Score <=5 in English section"}, "ofa_deadline": "By the end of first year; support course followed by recovery test or eligible first-year exam"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026"],
            "The 30-question English section is required but excluded from the ranking; it is used to assign English OFA. These are prior-cycle test and OFA rules only.",
        ),
        "previous_cycle_application_fee": fact(
            {"academic_year": "2026/27", "sapienza_selection_contribution_eur": 10, "sapienza_contribution_scope": "One non-refundable contribution for participation in the 05429 selection", "cisia_tolc_psi_registration_fee_eur": 35, "cisia_fee_scope": "Separate payment to CISIA to take TOLC-PSI"},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026"],
            "The €10 Infostud selection contribution and €35 CISIA test fee are separate; neither is a 2027/28 price.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "bachelor_course_specific_annual_total_eur": None, "amount_status": "No Psicologia e Salute L-24 total is stated in the reviewed admission call and tuition pages", "calculation": "ISEE-based Sapienza contribution rules and applicable benefits/exemptions", "payment_installments_percent": [30, 35, 35], "first_installment_due_by_rank": {"initial_winners": "2026-09-22", "first_scrolling": "2026-09-28", "second_scrolling": "2026-10-06", "third_scrolling": "2026-10-13"}, "additional_amounts": ["Regional tax, where due", "€16 stamp duty"]},
            "CONFIRMED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "The official pages confirm the ISEE-based framework, 30/35/35 structure and additional regional tax/stamp duty, but no course-specific annual L-24 total. No individual tuition amount is inferred.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "DiSCo_Lazio": {"type": "Competitive regional right-to-study grant and related benefits", "application_deadline_after_extension": "2026-07-23 20:00", "corrections_deadline": "2026-08-11 12:00", "eligibility": "Subject to annual economic, merit and other call requirements"}, "not_course_awards": {"Wanted_the_Best": "The 2026/27 award targets students entering Sapienza Master's degrees after graduating from another Italian university; it is not an incoming L-24 BSc award"}},
            "CONFIRMED", ["SRC-SAPIENZA-DISCO-LAZIO-2026", "SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-SCHOLARSHIPS-2026"],
            "DiSCo Lazio is competitive regional aid, not a guaranteed course award. The University's general inventory describes other limited-eligibility schemes, but Wanted the Best is Master's-only and not an L-24 BSc entrant scholarship.",
        ),
        "application_windows_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-PSYCHOLOGY-2026", "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026", "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026"],
            "No 2027/28 first-year dates or new-cycle call appeared on the official course profile/application page or central admissions index reviewed on 11 November 2026. Do not carry forward the 2026/27 restricted-selection calendar.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-INDEX-2026"],
            "No 2027/28 Sapienza selection contribution or TOLC-PSI fee was announced in the reviewed official course and admissions material.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-PSYCHOLOGY-2026", "SRC-SAPIENZA-PSYCHOLOGY-CALL-2026"],
            "No 2027/28 first-year call or course-specific entry requirements were published in the reviewed catalogue and admissions pages as of 11 November 2026.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "The reviewed tuition pages display the 2026/27 framework; no 2027/28 tuition regulation or course-level annual amount was published as of 11 November 2026.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-SCHOLARSHIPS-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "No 2027/28 DiSCo annual call or incoming L-24 scholarship call was present in the reviewed official university and regional aid pages as of 11 November 2026. This does not mean students are ineligible for general aid once annual calls open.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", ["SRC-SAPIENZA-PSYCHOLOGY-CALL-2026", "SRC-SAPIENZA-PSYCHOLOGY-APPLY-2026"],
            "The call provides quotas and rankings, but the reviewed sources do not provide a complete comparable applicant denominator and final admitted total across the selection and vacancy process; no acceptance rate is inferred.",
        ),
    }
    psychology["previous_cycle_tags"] = {
        "level": "Bachelor's degree (Laurea, class L-24)",
        "language": "Italian",
        "field": "Psychology",
        "cycle": "2026-2027",
        "label": "Official 2026/27 identity and restricted-access TOLC-PSI call; 2027/28 first-year intake remains unannounced",
    }
    psychology["last_checked"] = "2026-11-11"

    # Keep the archived 2024 programme lead separate from the current 2026/27
    # programme: official sources do not establish a direct successor link.
    inginfo_legacy = next(program for program in programs if program.get("id") == "legacy-157")
    inginfo_archive_source = "SRC-SAPIENZA-INGINFO-ARCHIVE-2024"
    engcsai_profile_source = "SRC-SAPIENZA-ENGCSAI-PROFILE-2026"
    engcsai_call_source = "SRC-SAPIENZA-ENGCSAI-CALL-2026"
    engcsai_course_sources = [
        "SRC-SAPIENZA-ENGCSAI-COURSE-2026",
        engcsai_profile_source,
        "SRC-SAPIENZA-ENGCSAI-APPLY-2026",
        engcsai_call_source,
        "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026",
        "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026",
        "SRC-SAPIENZA-INTL-OFFICE-2026",
        "SRC-SAPIENZA-APPLICATION-FEE-2026",
        "SRC-SAPIENZA-FEES-2026",
        "SRC-SAPIENZA-FEE-TABLE-2026",
        "SRC-SAPIENZA-DISCO-LAZIO-2026",
        "SRC-SAPIENZA-WANTED-BEST-2026",
        "SRC-SAPIENZA-SCHOLARSHIPS-2026",
    ]
    inginfo_legacy["program"] = "Ingegneria Informatica"
    inginfo_legacy["city"] = "Rome"
    inginfo_legacy["level"] = fact(
        "MSc (historical official course 30430)", "REQUIRES_VERIFICATION", [inginfo_archive_source],
        "The official archive establishes a 2024/25 two-year LM-32 Master's degree. It does not establish a current or 2027/28 first-year offer.",
    )
    inginfo_legacy["language"] = fact(
        "English (historical course 30430)", "REQUIRES_VERIFICATION", [inginfo_archive_source],
        "English delivery is confirmed in the official 2024 archive only; the legacy candidate's 2027/28 identity remains unresolved.",
    )
    inginfo_legacy["field"] = fact(
        "Computer Engineering", "REQUIRES_VERIFICATION", [inginfo_archive_source],
        "The 2024/25 official archived course title and description concern Engineering in Computer Science; no next-cycle course identity is confirmed.",
    )
    inginfo_legacy["availability_2027_2028"] = fact(
        None, "REQUIRES_VERIFICATION", [inginfo_archive_source, engcsai_profile_source, engcsai_call_source],
        "No 2027/28 first-year listing for archived course 30430 was found. The separate 2026/27 course 33515 is named Engineering in Computer Science and Artificial Intelligence; no official successor or discontinuation statement was identified, so the older lead remains unresolved.",
    )
    inginfo_legacy["overall_status"] = "REQUIRES_VERIFICATION"
    inginfo_legacy["source_ids"] = [inginfo_archive_source, engcsai_profile_source, engcsai_call_source]
    inginfo_legacy["facts"] = {
        "historical_course_reference": fact(
            {"academic_year": "2024/25", "official_name": "Engineering in Computer Science - Ingegneria Informatica", "course_code": "30430", "degree_class": "LM-32", "degree_type": "Two-year Laurea Magistrale / MSc", "language": "English", "campus": "Rome"},
            "CONFIRMED", [inginfo_archive_source],
            "This is a historic archive entry, not evidence of a 2026/27 or 2027/28 first-year intake.",
        ),
        "previous_cycle_course_listing": fact(
            None, "REQUIRES_VERIFICATION", [inginfo_archive_source, engcsai_profile_source],
            "No 2026/27 catalogue entry with the archived course 30430 title/code was identified. The current 2026/27 course 33515 has a different title/code and is tracked separately.",
        ),
        "course_relationship_assessment": fact(
            {"archived_course": {"academic_year": "2024/25", "course_code": "30430", "official_name": "Engineering in Computer Science - Ingegneria Informatica"}, "current_comparison_course": {"academic_year": "2026/27", "course_code": "33515", "official_name": "Engineering in Computer Science and Artificial Intelligence"}, "successor_relationship": "Not established by reviewed official sources"},
            "REQUIRES_VERIFICATION", [inginfo_archive_source, engcsai_profile_source, engcsai_call_source],
            "Both are LM-32 English-taught Master's degrees in Rome, but the course codes and titles differ. Similar subject matter is not proof of formal succession.",
        ),
        "previous_cycle_application_windows": fact(
            None, "UNAVAILABLE", [inginfo_archive_source, engcsai_call_source],
            "No 2026/27 admission call or application schedule for archived code 30430 was identified. Do not copy course 33515's current-cycle dates into this historical lead.",
        ),
        "previous_cycle_application_fee": fact(
            None, "UNAVAILABLE", [inginfo_archive_source, engcsai_call_source],
            "No 2026/27 application fee for the exact archived course 30430 was identified; course 33515's €10 requirement-check fee belongs to a separately named course.",
        ),
        "application_windows_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", [inginfo_archive_source, engcsai_profile_source, engcsai_call_source],
            "No 2027/28 first-year course listing or admission call for the exact archived course was found as of 11 November 2026. Its relationship to course 33515 remains unresolved.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", [engcsai_profile_source, engcsai_call_source],
            "No 2027/28 application fee is published for the exact historical course lead.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", [inginfo_archive_source, engcsai_profile_source],
            "No 2027/28 requirements for the exact archived code 30430 were published in the reviewed sources.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "No 2027/28 tuition regulation was found; the older programme's active 2027/28 status is also unresolved.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-SCHOLARSHIPS-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "No incoming 2027/28 call was published in the reviewed Sapienza or DiSCo pages; do not infer that general regional aid will be unavailable once its annual call opens.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", [inginfo_archive_source, engcsai_profile_source],
            "No comparable applicant and admitted-student denominator is available for the legacy course lead.",
        ),
    }
    inginfo_legacy["last_checked"] = "2026-11-11"

    engcsai = next(program for program in programs if program.get("id") == "discovered-026")
    engcsai["program"] = "Engineering in Computer Science and Artificial Intelligence"
    engcsai["city"] = "Rome"
    engcsai["level"] = fact(
        "Master's degree (Laurea Magistrale, class LM-32)", "REQUIRES_VERIFICATION", [engcsai_profile_source, engcsai_call_source],
        "Confirmed for 2026/27 only; verify the 2027/28 course catalogue before treating the label as current for next-cycle applicants.",
    )
    engcsai["language"] = fact(
        "English", "REQUIRES_VERIFICATION", [engcsai_profile_source, engcsai_call_source, "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026"],
        "All teaching is listed as English for 2026/27. This does not confirm a 2027/28 offer.",
    )
    engcsai["field"] = fact(
        "Computer Engineering and Artificial Intelligence", "REQUIRES_VERIFICATION", [engcsai_profile_source, engcsai_call_source],
        "Official 2026/27 programme title and regulations; confirm the next-cycle catalogue when published.",
    )
    engcsai["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", [engcsai_profile_source, "SRC-SAPIENZA-ENGCSAI-APPLY-2026", "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
        "The reviewed course profile and application page are for 2026/27 and the English admissions page still lists 2026/27 pre-selection only. No 2027/28 first-year call was identified as of 11 November 2026; this does not indicate discontinuation.",
    )
    engcsai["overall_status"] = "REQUIRES_VERIFICATION"
    engcsai["source_ids"] = list(dict.fromkeys(engcsai_course_sources))
    engcsai["facts"] = {
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Engineering in Computer Science and Artificial Intelligence", "italian_name": "Ingegneria Informatica e Intelligenza Artificiale", "course_code": "33515", "test_code": "33515", "degree_class": "LM-32", "degree_type": "Two-year Master's degree (Laurea Magistrale)", "campus": "Rome", "language": "English", "delivery": "In person", "department": "Ingegneria Informatica, Automatica e Gestionale Antonio Ruberti", "access": "Curricular requirements and personal preparation assessment"},
            "CONFIRMED", [engcsai_profile_source, "SRC-SAPIENZA-ENGCSAI-COURSE-2026", engcsai_call_source],
            "These are official prior-cycle identity facts for course 33515; they do not establish 2027/28 intake.",
        ),
        "previous_cycle_admission_route": fact(
            {"academic_year": "2026/27", "main_route": "Infostud application for curricular eligibility, followed by assessment of personal preparation by the degree committee", "assessment": ["Bachelor degree and recognized prior credits", "Academic record and relevance of previous curriculum", "Extracurricular activities and training", "Interview if required"], "non_eu_abroad_visa_route": "Mandatory MoveIN pre-selection/pre-acceptance followed by course application and Universitaly visa pre-enrolment", "standardized_test": "No standardized entrance test is listed in the course call"},
            "CONFIRMED", [engcsai_call_source, "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026", "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
            "MoveIN is the separate international pre-selection route for the applicant group specified by Sapienza; a pre-acceptance does not replace the course call or final enrolment.",
        ),
        "previous_cycle_application_windows": fact(
            {"academic_year": "2026/27", "infostud_requirement_check_opens": "2026-07-02", "course_call_deadlines": [{"applicant_group": "Non-EU applicants resident abroad requiring a study visa", "deadline": "2026-09-15"}, {"applicant_group": "General course applicants", "deadline": "2026-10-15"}, {"applicant_group": "General course applicants", "deadline": "2026-11-17"}, {"applicant_group": "General course applicants", "deadline": "2026-12-17"}, {"applicant_group": "Sapienza graduates or applicants about to graduate from Sapienza", "deadline": "2027-01-14"}], "movein_preselection_for_non_eu_visa_applicants": {"opens": "2025-12-22", "deadline": "2026-05-15"}, "universitaly_pre_enrolment_deadline": "2026-06-30"},
            "CONFIRMED", [engcsai_call_source, "SRC-SAPIENZA-ENGCSAI-APPLY-2026", "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
            "These are the 2026/27 deadlines. The January 2027 date is reserved for the specified Sapienza graduates; the non-EU visa MoveIN and Universitaly dates are separate steps.",
        ),
        "previous_cycle_application_fee": fact(
            {"academic_year": "2026/27", "infostud_curricular_eligibility_check_eur": 10, "movein_preselection_application_fee_eur": 30, "movein_fee_scope": "Per pre-selection application, maximum two programme applications per student per academic year"},
            "CONFIRMED", [engcsai_call_source, "SRC-SAPIENZA-APPLICATION-FEE-2026"],
            "The €10 course eligibility-check contribution and €30 MoveIN pre-selection charge are separate fees for different steps and applicant groups.",
        ),
        "previous_cycle_program_requirements": fact(
            {"academic_year": "2026/27", "degree": "Three-year Bachelor's degree or recognized equivalent", "curricular_credits": {"total_minimum_ects": 60, "basic_sciences_minimum_ects": 24, "mathematics_within_basic_sciences_minimum_ects": 9, "engineering_and_computing_minimum_ects": 36, "computer_science_or_information_processing_systems_within_engineering_computing_minimum_ects": 18}, "english": "B2 CEFR or higher", "personal_preparation": "Committee reviews degree grade, curricular relevance and additional training/experience; interview may be requested", "movein_preselection_only": {"minimum_gpa_100_scale": 75, "accepted_english_evidence": ["IELTS Academic 5.5", "TOEFL iBT 80", "Cambridge B2 First", "Trinity ISE II", "other certificates listed in the MoveIN document"], "english_evidence_exemptions": ["Native English speakers", "English-taught qualification from specified countries", "International Baccalaureate, GCSE or comparable credential"]}},
            "CONFIRMED", [engcsai_call_source, "SRC-SAPIENZA-ENGCSAI-COURSE-2026", "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026"],
            "The 75/100 GPA floor is a published MoveIN pre-selection criterion; the course's Infostud call separately defines curricular and personal-preparation assessment. All details are prior-cycle only.",
        ),
        "previous_cycle_entrance_test": fact(
            {"academic_year": "2026/27", "standardized_entrance_test": None, "assessment": "Document review, curricular eligibility and committee assessment of personal preparation; interview may be required"},
            "CONFIRMED", [engcsai_call_source, "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026"],
            "The reviewed course call does not specify a standardized admission test; it does specify an academic and personal-preparation assessment.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "faculty_group": "Second contribution bracket", "standard_total_eur": 2924, "foreign_income_fixed_contribution_bands_eur": [300, 700, 1500], "payment_installments_percent": [30, 35, 35], "calculation": "ISEE, country band, eligibility and exemptions affect the amount"},
            "CONFIRMED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "University-wide 2026/27 fee framework for second-level programmes in the Information Engineering, Computer Science and Statistics faculty group; this is not a personalized quote or a 2027/28 price.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "Wanted_the_Best": {"awards": 85, "gross_eur_per_year": 3000, "duration_years": 2, "eligibility": "Eligible Master's entrants graduating from another Italian university with 105/110 to 110/110 cum laude", "deadline": "2026-10-30"}, "DiSCo_Lazio": {"type": "Competitive regional right-to-study benefits", "application_deadline_after_extension": "2026-07-23 20:00", "corrections_deadline": "2026-08-11 12:00"}},
            "CONFIRMED", ["SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026", "SRC-SAPIENZA-SCHOLARSHIPS-2026"],
            "These are general competitive schemes, not guaranteed course awards; Wanted the Best's eligibility is limited to the call's specified Master's entrants.",
        ),
        "previous_cycle_contacts": fact(
            {"international_preselection": "admissions@diag.uniroma1.it", "course_student_affairs": "segreteriadidattica@diag.uniroma1.it"},
            "CONFIRMED", ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026", engcsai_call_source],
            "The admissions address appears in the official MoveIN requirements document; the course call names the Student Affairs contact for applicants from other Italian universities.",
        ),
        "application_windows_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", [engcsai_profile_source, "SRC-SAPIENZA-ENGCSAI-APPLY-2026", "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"],
            "No 2027/28 course call or English-program pre-selection schedule was identified on the official pages reviewed as of 11 November 2026.",
        ),
        "application_fee_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", [engcsai_call_source, "SRC-SAPIENZA-APPLICATION-FEE-2026"],
            "The €10 course-check and €30 MoveIN fees are 2026/27 terms only; no 2027/28 application charges were published.",
        ),
        "program_specific_requirements_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", [engcsai_profile_source, engcsai_call_source, "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026"],
            "No 2027/28 course call or updated MoveIN requirements document was identified as of 11 November 2026.",
        ),
        "tuition_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "The reviewed official tuition pages display the 2026/27 framework only; no 2027/28 fee regulation or course-level total was published.",
        ),
        "scholarships_2027_2028": fact(
            None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-SCHOLARSHIPS-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
            "No 2027/28 DiSCo annual call or incoming-student scholarship call was present in the reviewed official pages as of 11 November 2026. This does not imply that students will be ineligible for general aid once annual calls open.",
        ),
        "acceptance_rate": fact(
            None, "UNAVAILABLE", [engcsai_call_source, engcsai_profile_source],
            "The reviewed course call does not publish a comparable applicant and admitted-student denominator; no acceptance rate is inferred.",
        ),
    }
    engcsai["previous_cycle_tags"] = {
        "level": "Master's degree (Laurea Magistrale, class LM-32)",
        "language": "English",
        "field": "Computer Engineering and Artificial Intelligence",
        "cycle": "2026-2027",
        "label": "Official course 33515 profile and admission call; 2027/28 first-year intake remains unannounced",
    }
    engcsai["last_checked"] = "2026-11-11"

    econf = next(program for program in programs if program.get("id") == "legacy-158")
    econf_profile = "SRC-SAPIENZA-ECFIN-PROFILE-2026"
    econf_apply = "SRC-SAPIENZA-ECFIN-APPLY-2026"
    econf_call = "SRC-SAPIENZA-ECFIN-CALL-2026"
    econf_archive = "SRC-SAPIENZA-ECFIN-ARCHIVE-2025"
    econf_movein = "SRC-SAPIENZA-MOVEIN-REQUIREMENTS-JUN2026"
    econf_core_sources = [
        "SRC-SAPIENZA-ECONOMICS-FINANCE-2026",
        econf_profile,
        econf_apply,
        econf_call,
        econf_archive,
        econf_movein,
        "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026",
        "SRC-SAPIENZA-INTL-OFFICE-2026",
        "SRC-SAPIENZA-APPLICATION-FEE-2026",
        "SRC-SAPIENZA-FEES-2026",
        "SRC-SAPIENZA-FEE-TABLE-2026",
        "SRC-SAPIENZA-DISCO-LAZIO-2026",
        "SRC-SAPIENZA-WANTED-BEST-2026",
        "SRC-SAPIENZA-SCHOLARSHIPS-2026",
    ]
    econf["program"] = "Economics and Finance"
    econf["city"] = "Rome"
    econf["level"] = fact(
        "Bachelor's degree (Laurea, class L-33)", "REQUIRES_VERIFICATION",
        [econf_profile, econf_archive],
        "Sapienza's 2025/26 archived and 2026/27 current course records identify this as a three-year L-33 Bachelor's degree. The previous tracker MSc label is retained in previous_tracker_tags only; confirm the 2027/28 catalogue when published.",
    )
    econf["language"] = fact(
        "Italian and English (three Italian curricula; one fully English curriculum)", "REQUIRES_VERIFICATION",
        [econf_profile, econf_archive, econf_call, econf_movein],
        "Official 2026/27 evidence: the course lists Italian and English curricula, with the Economics and Finance path delivered fully in English. This does not establish the 2027/28 offer.",
    )
    econf["field"] = fact(
        "Economics and Finance", "REQUIRES_VERIFICATION", [econf_profile, econf_archive],
        "Official course identity is confirmed for the 2025/26 archive and 2026/27 catalogue only.",
    )
    econf["availability_2027_2028"] = fact(
        None, "NOT_YET_PUBLISHED", [econf_profile, econf_apply, econf_call, "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"],
        "Not yet announced for 2027/28 in the Sapienza catalogue and admission pages reviewed as of 11 November 2026. This does not mean discontinued.",
    )
    econf["overall_status"] = "REQUIRES_VERIFICATION"
    econf["source_ids"] = econf_core_sources
    econf["facts"] = {
        "previous_tracker_classification_review": fact(
            {"previous_tracker_tags": {"level": "MSc", "language": "Italian", "field": "Economics"}, "official_2025_2026_record": {"course_code": "33438", "degree_class": "L-33", "degree_type": "Three-year Bachelor's degree", "catalogue_languages": ["Italian", "English"]}, "official_2026_2027_record": {"course_code": "34177", "test_code": "14613", "degree_class": "L-33", "degree_type": "Three-year Bachelor's degree", "catalogue_languages": ["Italian", "English"]}, "finding": "The previous MSc classification is contradicted by both official course records; no master's facts are attached to this course."},
            "CONFIRMED", [econf_archive, econf_profile],
            "The prior tracker tags remain unchanged as provenance. Official records for two consecutive cycles identify the same-name course as a Bachelor's degree; the current listing is course 34177.",
        ),
        "previous_cycle_course_listing": fact(
            {"academic_year": "2026/27", "official_name": "Economics and Finance (Economia e finanza)", "course_code": "34177", "test_code": "14613", "degree_class": "L-33", "degree_type": "Three-year Bachelor's degree (Laurea)", "campus": "Rome", "faculty": "Economics", "department": "Economics and Law", "delivery": "In person", "access": "Open access; mandatory non-selective knowledge-verification test", "curricula": [{"name": "Economics and Finance", "language": "English", "delivery": "Fully taught in English"}, {"name": "Economia e integrazione internazionale", "language": "Italian"}, {"name": "Economia e ambiente", "language": "Italian"}, {"name": "Economia e mercati finanziari", "language": "Italian"}]},
            "CONFIRMED", [econf_profile, econf_call, "SRC-SAPIENZA-ECONOMICS-FINANCE-2026"],
            "These are prior-cycle course identity facts, not a confirmation of the 2027/28 first-year intake.",
        ),
        "official_course_url": fact("https://corsidilaurea.uniroma1.it/en/course/34177", "CONFIRMED", [econf_profile]),
        "official_application_url": fact("https://corsidilaurea.uniroma1.it/en/course/34177/apply", "CONFIRMED", [econf_apply]),
        "previous_cycle_admission_route": fact(
            {"academic_year": "2026/27", "general_route": "Infostud registration, €10 course access contribution, and a mandatory but non-selective initial-knowledge test", "qualification": "Secondary school diploma obtained or to be obtained in 2026", "Italian_curriculum_test": "TOLC-E or CEnT-S", "English_curriculum_test": "CEnT-S or SAT General Test", "english_curriculum_language_requirement": "Valid English B2 certificate, with official exemptions", "english_curriculum_preselection": "MoveIN pre-selection was listed as mandatory for the English programmes in the central admissions instructions; deadline depended on applicant group", "non_eu_abroad_visa_route": "Non-EU applicants residing abroad and requiring a study visa needed successful MoveIN pre-selection/pre-acceptance and Universitaly pre-enrolment by 30 June 2026; final enrollment still followed the course call"},
            "CONFIRMED", [econf_call, econf_movein, "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
            "The knowledge test is not a competitive ranking for places. MoveIN is a separate pre-selection step for its eligible English-program applicant group and does not itself complete course admission or enrollment.",
        ),
        "previous_cycle_application_windows": fact(
            {"academic_year": "2026/27", "infostud_registration_and_10_eur_payment": {"opens": "2026-07-02", "deadline": "2026-10-29"}, "test_deadline": "2026-10-29", "first_university_tuition_installment": {"opens": "2026-09-01", "deadline": "2026-11-05"}, "movein_preselection_for_non_eu_visa_applicants": {"opens": "2025-12-22", "deadline": "2026-05-15"}, "movein_preselection_for_eu_and_equivalent_applicants": {"deadline": "2026-07-31"}, "universitaly_pre_enrolment_for_visa_applicants": "2026-06-30"},
            "CONFIRMED", [econf_call, "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
            "These windows belong to 2026/27. MoveIN and Universitaly are international pre-selection/visa steps, distinct from the course's Infostud test-and-fee deadline.",
        ),
        "previous_cycle_application_fee": fact(
            {"academic_year": "2026/27", "infostud_course_contribution_eur": 10, "movein_preselection_eur_per_application": 30, "movein_maximum_applications": 2, "conditional_cisia_tolc_e_test_fee_eur": 35},
            "CONFIRMED", [econf_call, "SRC-SAPIENZA-APPLICATION-FEE-2026"],
            "The €10 course contribution and MoveIN's €30 per application are different charges. The €35 CISIA fee is specifically for applicants choosing TOLC-E; this amount is not asserted for CEnT-S or SAT.",
        ),
        "previous_cycle_program_requirements": fact(
            {"academic_year": "2026/27", "school_qualification": "Secondary school leaving diploma obtained or to be obtained in 2026; foreign qualifications must meet Sapienza recognition rules", "italian_curriculum": "No English-language certificate is required by this course call for the Italian curriculum", "english_curriculum": {"minimum_english": "CEFR B2", "official_exemptions": ["Native English speakers", "English-taught secondary diploma or university degree from an accredited institution in EU/EEA/Schengen, Australia, Canada, New Zealand, United Kingdom or United States", "International Baccalaureate, GCSE or equivalent" ]}, "movein_preselection_criteria": {"minimum_schooling": "12 years, or 11 years plus a Foundation Year or one year of higher education", "minimum_gpa_100_scale": 80, "minimum_test": {"SAT": "960/1600 or higher", "CEnT-S": "overall converted score higher than zero"}, "english": "B2; accepted evidence includes IELTS 5.5, TOEFL iBT 80, Cambridge B2 First, or Trinity ISE II, with listed exemptions"}},
            "CONFIRMED", [econf_call, econf_movein],
            "The 80/100 GPA and the listed test thresholds belong to the 2026/27 MoveIN pre-selection route, not a general course-admission GPA rule. The central admissions page gives different pre-selection deadlines for non-EU visa applicants and EU/equivalent applicants.",
        ),
        "previous_cycle_entrance_test": fact(
            {"academic_year": "2026/27", "nature": "Mandatory, non-selective initial-knowledge assessment", "test_routes": {"Italian_curriculum": "TOLC-E or CEnT-S", "English_curriculum": "CEnT-S or SAT"}, "OFA_if_below": {"TOLC-E": "9/36", "selected_CEnT-S_sections": 8, "SAT_for_English_curriculum": "960/1600"}, "OFA_completion_deadline": "Within the first year", "TOLC_E_structure": "36 scored questions in Logic, Verbal Comprehension and Mathematics, plus a separate 30-question English section that does not affect the result"},
            "CONFIRMED", [econf_call, econf_profile],
            "The test verifies initial knowledge and does not select among a fixed number of seats. Scores below the call's threshold assign OFA rather than denying access.",
        ),
        "previous_cycle_tuition": fact(
            {"academic_year": "2026/27", "course_specific_total_published": False, "calculation": "General Sapienza tuition depends on ISEE, eligibility and exemptions; foreign tax residents use the published country-group fixed-contribution schedule", "foreign_income_fixed_contribution_bands_eur": [300, 700, 1500], "payment_installments_percent": [30, 35, 35]},
            "CONFIRMED", [econf_call, "SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"],
            "The course call does not quote a course-specific total. The €2,924 figure previously attached to this record is the standard second-level Master's rate and must not be applied to this L-33 Bachelor's programme.",
        ),
        "previous_cycle_scholarships": fact(
            {"academic_year": "2026/27", "DiSCo_Lazio": {"type": "Competitive regional right-to-study benefits", "application_deadline_after_extension": "2026-07-23 20:00", "corrections_deadline": "2026-08-11 12:00"}, "Wanted_the_Best": {"eligible_for_this_Bachelors": False, "scope": "Competitive award for eligible Master's entrants only"}, "course_specific_university_award": "None identified in the reviewed official sources"},
            "CONFIRMED", ["SRC-SAPIENZA-DISCO-LAZIO-2026", "SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-SCHOLARSHIPS-2026"],
            "DiSCo is general competitive regional aid, not a guaranteed course award. The cited Wanted the Best scholarship targets Master's entrants and is not for new L-33 Bachelor's entrants.",
        ),
        "application_windows_2027_2028": fact(None, "NOT_YET_PUBLISHED", [econf_profile, econf_apply, econf_call, "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"], "No 2027/28 course listing or admission calendar was published on the official pages reviewed as of 11 November 2026."),
        "application_fee_2027_2028": fact(None, "NOT_YET_PUBLISHED", [econf_call, "SRC-SAPIENZA-APPLICATION-FEE-2026"], "The €10 course contribution and €30 MoveIN charge are 2026/27 terms only; no 2027/28 amounts were published."),
        "program_specific_requirements_2027_2028": fact(None, "NOT_YET_PUBLISHED", [econf_profile, econf_call, econf_movein], "No 2027/28 course call or updated MoveIN requirements were identified; 2026/27 qualifications, test routes and thresholds are not carried forward."),
        "english_language_requirement_2027_2028": fact(None, "NOT_YET_PUBLISHED", [econf_profile, econf_call, econf_movein], "No 2027/28 curriculum or English-certificate rule has been published in the reviewed pages."),
        "tuition_2027_2028": fact(None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"], "No 2027/28 tuition regulation or course-level total was available; the 2026/27 income/residence-dependent framework is historical only."),
        "scholarships_2027_2028": fact(None, "NOT_YET_PUBLISHED", ["SRC-SAPIENZA-DISCO-LAZIO-2026", "SRC-SAPIENZA-SCHOLARSHIPS-2026"], "No 2027/28 DiSCo call or incoming-student scholarship call was published in the reviewed official pages. This does not imply that general aid will be unavailable once annual calls open."),
        "acceptance_rate": fact(None, "UNAVAILABLE", [econf_call, econf_profile], "The programme is open access with a non-selective knowledge-verification test; no comparable applicant/admitted denominator is published, so no acceptance rate is inferred."),
    }
    econf["previous_cycle_tags"] = {
        "level": "Bachelor's degree (Laurea, class L-33)",
        "language": "Italian and English (three Italian curricula; one fully English curriculum)",
        "field": "Economics and Finance",
        "cycle": "2026-2027",
        "label": "Official course 34177 and 2026/27 call; 2027/28 entry remains unannounced",
    }
    econf["last_checked"] = "2026-11-11"

    cybersecurity = next(program for program in programs if program.get("id") == "legacy-031")
    cybersecurity_award_source = "SRC-PADUA-STUDENT-AWARDS-CYBERSECURITY-2026"
    cybersecurity.setdefault("facts", {})["current_student_award_2026_2028"] = fact(
        {"name":"Awards in memory of Engineer Giuseppe Mariani, Fourth Edition 2026", "academic_years":["2026/27", "2027/28"], "number_of_awards":2, "gross_eur_per_award":11280, "application_deadline":"2027-03-18", "eligible_population":"High-achieving students in the final two years of the Cybersecurity Master's degree"},
        "CONFIRMED", [cybersecurity_award_source],
        "This award is for students in the existing cohort during 2026/27 and 2027/28, not a scholarship for students newly entering in 2027/28. Keep it separate from the incoming-student scholarship offer.",
    )
    cybersecurity["source_ids"] = list(dict.fromkeys(cybersecurity.get("source_ids", []) + [cybersecurity_award_source]))

    padua_scholarship_sources = [
        "SRC-PADUA-INTL-EXCELLENCE-2027-BOARD",
        "SRC-PADUA-INTL-EXCELLENCE-PROGRAMME",
    ]
    padua_scholarship_terms = {
        "name": "Padua International Excellence Scholarship",
        "academic_year": "2027/28",
        "university_allocation_eur": 1432200,
        "maximum_awards": 76,
        "target": "Highest-ranked candidate per English-taught degree/curriculum, including newly activated programmes",
        "gross_eur_per_year": 8000,
        "university_tuition_fee_exemption": True,
        "remaining_fees": ["Regional fee", "Revenue stamp"],
        "maximum_duration_years": {"MSc": 2, "BSc": 3, "single_cycle": 3},
        "award_conditions": "Competitive; selection and renewal subject to the forthcoming 2027/28 annual call",
    }
    padua_tuition_source = "SRC-PADUA-TUITION-2026"
    for program in programs:
        if program.get("university_id") != "padova":
            continue
        facts = program.setdefault("facts", {})
        tuition = facts.get("tuition_2027_2028")
        if tuition is None:
            facts["tuition_2027_2028"] = fact(
                None, "REQUIRES_VERIFICATION", [padua_tuition_source],
                "The University fee page reviewed on 11 November 2026 still links the 2026/27 annual fee notice; no 2027/28 programme-specific amount is confirmed.",
            )
        else:
            tuition["source_ids"] = list(dict.fromkeys(tuition.get("source_ids", []) + [padua_tuition_source]))
            old_note = tuition.get("notes") or ""
            addition = "The University fee page reviewed on 11 November 2026 still links the 2026/27 annual fee notice; no 2027/28 programme-specific amount is confirmed."
            if addition not in old_note:
                tuition["notes"] = (old_note + " " + addition).strip()
        program["source_ids"] = list(dict.fromkeys(program.get("source_ids", []) + [padua_tuition_source]))

        language = (program.get("language") or {}).get("value") or ""
        if "English" not in language:
            continue
        active_and_confirmed = (
            program.get("overall_status") == "CONFIRMED"
            and (program.get("availability_2027_2028") or {}).get("status") == "CONFIRMED"
            and (program.get("availability_2027_2028") or {}).get("value") is True
            and (program.get("language") or {}).get("status") == "CONFIRMED"
        )
        facts["scholarships_2027_2028"] = fact(
            padua_scholarship_terms,
            "CONFIRMED" if active_and_confirmed else "REQUIRES_VERIFICATION",
            padua_scholarship_sources,
            "For this record, an active 2027/28 English-taught intake is confirmed; the University has approved the headline scholarship scheme. Awards are competitive and not guaranteed; annual call eligibility and course-level allocation remain to be checked."
            if active_and_confirmed else
            "The University approved the scheme for English-taught degree programmes, including new programmes, but this record's 2027/28 intake, final language/approval or course-level inclusion is still pending. Do not show it as a confirmed course award.",
        )
        facts["scholarship_call_details_2027_2028"] = fact(
            None, "NOT_YET_PUBLISHED", ["SRC-PADUA-INTL-EXCELLENCE-PROGRAMME"],
            "The official programme page says the 2027/28 annual call will be published in November 2026; as checked on 11 November the page still links the 2026/27 call. Confirm final eligibility, application/selection process and renewal criteria when the new notice appears.",
        )
        program["source_ids"] = list(dict.fromkeys(program["source_ids"] + padua_scholarship_sources))

    pisa_call = "SRC-UNIPI-INFO-ENG-2027-CALL"
    aide_profile = "SRC-UNIPI-AIDE-COURSE-PROFILE"
    computer_engineering_profile = "SRC-UNIPI-COMPUTER-ENGINEERING-PROFILE"
    pisa_requirement_value = {
        "prior_degree": "BSc or equivalent first-cycle degree after at least three years of study",
        "required_subjects": ["Algorithms and programming", "Computer architecture", "Operating systems", "Computer networks", "Database systems"],
        "mathematics": "Strong background required",
        "related_engineering": "Electronics, telecommunications, automation and management engineering are favorably considered",
        "professional_qualifications": "Purely technical/professional qualifications are not accepted",
        "english": "CEFR B2",
        "selection": "Committee assesses academic performance, subject alignment and CV; online tests or interviews may be used, followed by a final online interview for shortlisted applicants",
    }
    pisa_documents = [
        "B2 English certificate from an internationally recognised institution",
        "Degree certificate if graduated and academic transcripts in English/Italian or translated into one of those languages, showing at least three years of study",
        "Valid passport copy",
        "Complete CV including education and relevant experience",
    ]
    pisa_applicant_group = "Applicants with a foreign qualification (Bachelor's degree obtained from a non-Italian institution); this call does not establish the separate Italian-qualification application process."
    pisa_application_windows = [{
        "start": None,
        "end": "2027-02-01",
        "deadline_time": "23:59 GMT (strict)",
        "round": "2027/28 Department of Information Engineering international MSc call",
        "eligible_group": pisa_applicant_group,
    }]
    pisa_application_deadline = {
        "end": "2027-02-01",
        "time": "23:59 GMT (strict)",
        "applies_to": pisa_applicant_group,
        "selection_results": "12 March 2027 (tentative)",
    }
    pisa_fee = {"amount_eur": 30, "per": "application", "maximum_applications": 2}
    pisa_current_support = {
        "DSU_Tuscany": "Regional right-to-study support; consult the separate annual DSU call",
        "MAECI": "The 2027/28 call is not yet announced",
        "Invest_Your_Talent_in_Italy": "For selected countries; the 2027/28 call is not yet announced",
        "UniPi_merit_award": "Potential second-year award for the student with the best first-year academic performance; at least 45 CFU by 30 September 2028",
        "selection_guarantee": "Admission does not guarantee any scholarship",
    }

    aide = next(program for program in programs if program.get("id") == "legacy-054")
    aide["level"] = fact("MSc", "CONFIRMED", [aide_profile, pisa_call])
    aide["language"] = fact("English/Italian (required courses in English; Italian not required to complete the degree)", "CONFIRMED", [aide_profile, pisa_call])
    aide["field"] = fact("Artificial Intelligence and Data Engineering", "CONFIRMED", [aide_profile, pisa_call])
    aide["availability_2027_2028"] = fact(
        True, "CONFIRMED", [pisa_call],
        "The named 2027/28 Department call confirms an intake for applicants with foreign qualifications. It does not confirm the separate admission procedure for Italian qualifications.",
    )
    aide["overall_status"] = "CONFIRMED"
    aide["facts"].update({
        "official_course_profile_2027_2028": fact({"degree_class":"LM-32 - Computer systems engineering", "campus":"Pisa", "language":"English/Italian", "required_courses_language":"English", "italian_required":"No"}, "CONFIRMED", [aide_profile, pisa_call]),
        "applicant_scope_2027_2028": fact({"confirmed_group":"Applicants with a foreign qualification (Bachelor's obtained from a non-Italian institution)", "domestic_degree_route":"Not verified in this refresh"}, "CONFIRMED", [pisa_call]),
        "application_windows": fact(pisa_application_windows, "CONFIRMED", [pisa_call], "The Department has not published an opening date on the call page. Deadline is strictly 1 February 2027 at 23:59 GMT; the portal lists 12 March 2027 as a tentative results date."),
        "application_deadline": fact(pisa_application_deadline, "CONFIRMED", [pisa_call]),
        "application_fee": fact(pisa_fee, "CONFIRMED", [pisa_call]),
        "application_fee_2027_2028": fact(pisa_fee, "CONFIRMED", [pisa_call]),
        "application_route": fact("https://applymscenglish.unipi.it/", "CONFIRMED", [pisa_call]),
        "program_specific_requirements_2027_2028": fact(pisa_requirement_value, "CONFIRMED", [pisa_call]),
        "english_language_requirement_2027_2028": fact({"minimum":"CEFR B2", "visa_applicants":"Submit a certificate from an internationally recognised institution covering listening, reading, speaking and writing", "medium_of_instruction_letter_sufficient":False}, "CONFIRMED", [pisa_call]),
        "application_documents_2027_2028": fact(pisa_documents, "CONFIRMED", [pisa_call]),
        "selection_process_2027_2028": fact({"committee_assessment":["Undergraduate academic performance in country context", "Match between prior coursework and the programs", "CV and relevant experience"], "possible_steps":["Online test or interview", "Final online interview for successful applicants"], "results_date":"12 March 2027 (tentative)"}, "CONFIRMED", [pisa_call]),
        "tuition_2027_2028": fact(None, "NOT_YET_PUBLISHED", [pisa_call], "The official call says 2027/28 fees are set annually and usually announced in June for the following academic year; 2026/27 amounts are historical only."),
        "scholarships_2027_2028": fact(pisa_current_support, "REQUIRES_VERIFICATION", [pisa_call], "The call identifies these support routes but gives no confirmed course-specific 2027/28 award, amount or eligibility. It explicitly says the MAECI and Invest Your Talent in Italy 2027/28 calls have not been announced; DSU uses a separate annual call and the UniPi merit award is a later second-year competition."),
        "acceptance_rate": fact(None, "UNAVAILABLE", [pisa_call], "No applicant denominator or admitted-student count is published; no acceptance rate is inferred."),
    })
    aide["source_ids"] = list(dict.fromkeys(aide.get("source_ids", []) + [aide_profile, pisa_call]))
    aide["last_checked"] = "2026-11-11"
    aide["previous_cycle_tags"] = None

    computer_engineering = make_program(
        "discovered-039", "pisa", "Computer Engineering", "MSc", "English",
        "Computer Engineering", "CONFIRMED", [computer_engineering_profile, pisa_call],
        city="Pisa", discovery="newly_discovered",
    )
    computer_engineering["level"] = fact("MSc", "CONFIRMED", [computer_engineering_profile, pisa_call])
    computer_engineering["language"] = fact("English", "CONFIRMED", [computer_engineering_profile, pisa_call])
    computer_engineering["field"] = fact("Computer Engineering", "CONFIRMED", [computer_engineering_profile, pisa_call])
    computer_engineering["availability_2027_2028"] = fact(
        True, "CONFIRMED", [pisa_call],
        "The named 2027/28 Department call confirms an intake for applicants with foreign qualifications. It does not confirm the separate admission procedure for Italian qualifications.",
    )
    computer_engineering["facts"] = {
        "official_course_profile_2027_2028": fact({"degree_class":"LM-32 - Computer Engineering", "duration_years":2, "campus":"Pisa", "language":"English", "access":"Open access with skills assessment", "tracks":["Cloud and Network Infrastructures and Services", "Cyber-Physical Systems", "Cybersecurity"]}, "CONFIRMED", [computer_engineering_profile, pisa_call]),
        "applicant_scope_2027_2028": fact({"confirmed_group":"Applicants with a foreign qualification (Bachelor's obtained from a non-Italian institution)", "domestic_degree_route":"Not verified in this refresh"}, "CONFIRMED", [pisa_call]),
        "application_windows": fact(pisa_application_windows, "CONFIRMED", [pisa_call], "The Department has not published an opening date on the call page. Deadline is strictly 1 February 2027 at 23:59 GMT; the portal lists 12 March 2027 as a tentative results date."),
        "application_deadline": fact(pisa_application_deadline, "CONFIRMED", [pisa_call]),
        "application_fee": fact(pisa_fee, "CONFIRMED", [pisa_call]),
        "application_fee_2027_2028": fact(pisa_fee, "CONFIRMED", [pisa_call]),
        "application_route": fact("https://applymscenglish.unipi.it/", "CONFIRMED", [pisa_call]),
        "program_specific_requirements_2027_2028": fact(pisa_requirement_value, "CONFIRMED", [pisa_call]),
        "english_language_requirement_2027_2028": fact({"minimum":"CEFR B2", "visa_applicants":"Submit a certificate from an internationally recognised institution covering listening, reading, speaking and writing", "medium_of_instruction_letter_sufficient":False}, "CONFIRMED", [pisa_call]),
        "application_documents_2027_2028": fact(pisa_documents, "CONFIRMED", [pisa_call]),
        "selection_process_2027_2028": fact({"committee_assessment":["Undergraduate academic performance in country context", "Match between prior coursework and the programs", "CV and relevant experience"], "possible_steps":["Online test or interview", "Final online interview for successful applicants"], "results_date":"12 March 2027 (tentative)"}, "CONFIRMED", [pisa_call]),
        "tuition_2027_2028": fact(None, "NOT_YET_PUBLISHED", [pisa_call], "The official call says 2027/28 fees are set annually and usually announced in June for the following academic year; 2026/27 amounts are historical only."),
        "scholarships_2027_2028": fact(pisa_current_support, "REQUIRES_VERIFICATION", [pisa_call], "The call identifies these support routes but gives no confirmed course-specific 2027/28 award, amount or eligibility. It explicitly says the MAECI and Invest Your Talent in Italy 2027/28 calls have not been announced; DSU uses a separate annual call and the UniPi merit award is a later second-year competition."),
        "acceptance_rate": fact(None, "UNAVAILABLE", [pisa_call], "No applicant denominator or admitted-student count is published; no acceptance rate is inferred."),
    }
    computer_engineering["last_checked"] = "2026-11-11"
    computer_engineering["previous_cycle_tags"] = None
    programs.append(computer_engineering)

    bbs_programs = [
        ("discovered-040", "Data Science and Business Analytics", "Data Science and Business Analytics", "SRC-BBS-DSBA-2027", "Department of Computer Science and Engineering (DISI)", 1500, "First-level Professional Master", "Professional Master's (First Level)"),
        ("discovered-041", "Artificial Intelligence for Management", "Artificial Intelligence for Business Management", "SRC-BBS-AI-MANAGEMENT-2027", "Department of Computer Science and Engineering (DISI)", None, "First-level Professional Master", "Professional Master's (First Level)"),
        ("discovered-042", "Finance – Entrepreneurial Finance", "Entrepreneurial Finance and FinTech", "SRC-BBS-ENTREPRENEURIAL-FINANCE-2027", "Department of Management (DISA)", 1500, "First-level Professional Master", "Professional Master's (First Level)"),
        ("discovered-043", "Finance – Finance and Artificial Intelligence", "Finance, Artificial Intelligence and FinTech", "SRC-BBS-FINANCE-AI-2027", "Department of Management (DISA)", 1500, "First-level Professional Master", "Professional Master's (First Level)"),
        ("discovered-044", "Marketing Management – Analytics and AI for Marketing", "Marketing analytics and artificial intelligence", "SRC-BBS-MARKETING-ANALYTICS-AI-2027", "Department of Management (DISA)", 1500, "Track within the first-level Professional Master in Marketing Management", "Professional Master's track (First Level)"),
    ]
    for pid, title, field_name, source_id, department, learning_hours, programme_type, level_label in bbs_programs:
        sources = [source_id]
        program = make_program(
            pid, "bologna", title, level_label, "English", field_name,
            "CONFIRMED", sources, city="Bologna", discovery="newly_discovered",
        )
        program["availability_2027_2028"] = fact(
            True, "CONFIRMED", sources,
            "BBS explicitly advertises this programme for 2027/28 with an October 2027 start. This confirms the named intake, not the detailed annual admission call or its eventual terms.",
        )
        program["facts"] = {
            "official_course_listing_2027_2028": fact(
                {"academic_year":"2027/28", "official_name":title, "programme_type":programme_type, "duration_months":12, "credits_ects":60, "language":"English", "format":"Full-time", "campus":"Bologna Business School, Bologna", "collaborating_department":department, **({"learning_hours":learning_hours} if learning_hours else {})},
                "CONFIRMED", sources,
                "The official BBS page states the course type, duration, English language, full-time format, and 2027/28 start. The marketing option is a track within the parent Marketing Management Professional Master, not a separate Laurea Magistrale.",
            ),
            "program_type": fact(programme_type + "; offered by Bologna Business School in collaboration with the University of Bologna", "CONFIRMED", sources),
            "selection_period_2027_2028": fact(
                {"applications":"Opening soon", "selection_rounds":4, "period_start":"2027-03", "period_end":"2027-09", "start_date":"2027-10", "detailed_call":"Not yet published"},
                "CONFIRMED", sources,
                "BBS publishes the month range and number of selection rounds for 2027/28, but has not yet published the specific application opening dates, round deadlines, or annual call.",
            ),
            "application_windows": fact(None, "NOT_YET_PUBLISHED", sources, "The 2027/28 selection is announced for four rounds between March and September 2027, but exact application opening dates and deadlines are not yet published."),
            "application_deadline": fact(None, "NOT_YET_PUBLISHED", sources, "Exact 2027/28 round deadlines will be published in the forthcoming BBS Call for Applications."),
            "current_published_application_terms": fact(
                {"application_route":"University of Bologna Studenti Online; First Level Master", "selection_fee_eur":60, "current_page_status":"Displayed on the programme page but not labelled for AY 2027/28"},
                "CONFIRMED", sources,
                "Current displayed application instructions and fee may be replaced by the forthcoming 2027/28 call; do not treat the €60 amount or these instructions as confirmed cycle terms.",
            ),
            "application_fee_2027_2028": fact(None, "NOT_YET_PUBLISHED", sources, "The programme page displays a €60 selection fee but does not identify it as the 2027/28 fee. Confirm the amount in the annual call."),
            "current_published_requirements": fact(
                {"qualifying_degree":"First-cycle Bachelor's degree by the enrollment deadline of the selected round", "english":"Minimum B2", "selection":["Online aptitude test", "English-language test", "Motivational interview in English"], "cycle_label":"Not stated; current displayed requirements"},
                "CONFIRMED", sources,
                "These are the requirements currently shown on the BBS page; the page says the 2027/28 call and application instructions are forthcoming, so the new-cycle terms require confirmation.",
            ),
            "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", sources, "The annual call is pending. The current page shows a bachelor's degree, B2 English and selection tests/interview but does not label these detailed rules for 2027/28."),
            "tuition_currently_displayed": fact(
                {"amount_eur":14800, "vat_free":True, "cycle_label":"Not stated; current displayed tuition"},
                "CONFIRMED", sources,
                "The programme page displays €14,800 but does not state that this is the 2027/28 tuition. Check the annual call before presenting it as the new-cycle amount.",
            ),
            "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", sources, "The current programme page displays €14,800 without a 2027/28 cycle label; the annual call and applicable fee remain pending."),
            "scholarships_currently_displayed": fact(
                {"partial_awards_per_round_eur":[4000,6000], "full_scholarships":"Not available per current page", "university_dsu_ergo":"Not eligible per current page", "inps":"Separate call publication date not yet set", "cycle_label":"Not stated for 2027/28"},
                "CONFIRMED", sources,
                "These are currently displayed general BBS Professional Master funding terms; 2027/28 eligibility, amounts, availability and deadlines require confirmation in the annual call.",
            ),
            "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", sources, "The page displays current general partial-award schemes but does not confirm 2027/28 scholarship amounts or terms."),
            "acceptance_rate": fact(None, "UNAVAILABLE", sources, "No applicant and admission counts are published; no acceptance rate is inferred."),
        }
        program["source_ids"] = sources
        program["last_checked"] = "2026-11-11"
        program["previous_cycle_tags"] = None
        programs.append(program)
