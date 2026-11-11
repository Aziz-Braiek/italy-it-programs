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
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the English-taught two-year MSc in Bologna, classes LM-18/LM-32 and open access with assessment; profile is current course evidence, not a 2027/28 intake call.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-AI-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Artificial Intelligence – 2026/27 admission requirements and call",
        "url": "https://corsi.unibo.it/2cycle/artificial-intelligence/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The page links the 2026/27 call and specifies degree-background, English B2 and personal-preparation assessment requirements. No 2027/28 call is linked on the reviewed page.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-DHDK-PROFILE-2026",
        "university_id": "bologna", "title": "Digital Humanities and Digital Knowledge – official degree profile",
        "url": "https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge/",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official Bologna profile for the English-taught second-cycle Digital Humanities and Digital Knowledge degree in Bologna.",
        "supports": ["program.name", "program.level", "program.language", "program.location"],
    },
    {
        "id": "SRC-UNIBO-DHDK-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Digital Humanities and Digital Knowledge – 2026/27 admission page",
        "url": "https://corsi.unibo.it/2cycle/DigitalHumanitiesKnowledge/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Links the expired 2026/27 admission call and describes qualification, interview and admission procedures. No 2027/28 call was linked on the reviewed page.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-BA-CURRICULUM-2026",
        "university_id": "bologna", "title": "Business Analytics – official curriculum profile",
        "url": "https://corsi.unibo.it/2cycle/BusinessAnalytics/overview",
        "source_type": "Official curriculum profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies Business Analytics as an English-language curriculum within the two-year MSc Statistics, Economics and Business (LM-82), taught in Bologna; it is not a separate degree programme.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.program_type"],
    },
    {
        "id": "SRC-UNIBO-BA-CURRICULUM-PARENT-2026",
        "university_id": "bologna", "title": "Statistics, Economics and Business – parent degree profile",
        "url": "https://corsi.unibo.it/2cycle/StatisticsEconomicsBusiness",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists Statistics, Economics and Business as the degree programme and Business Analytics among its curricula; the parent degree has Italian and English delivery and is based in Bologna.",
        "supports": ["program.parent_degree", "program.program_type", "program.language"],
    },
    {
        "id": "SRC-UNIBO-MES-PROFILE-2026",
        "university_id": "bologna", "title": "Mechanical Engineering for Sustainability – official degree profile",
        "url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the two-year English-taught MSc (LM-33) at Forlì, open access with assessment of personal competencies.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-MES-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Mechanical Engineering for Sustainability – 2026/27 admission page",
        "url": "https://corsi.unibo.it/2cycle/MechanicalEngineering-Forli/how-to-enrol",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Links the 2026/27 call and describes relevant degree and curricular-credit requirements. No 2027/28 call was linked on the reviewed page.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-CLABE-PROFILE-2026",
        "university_id": "bologna", "title": "Business and Economics (CLaBE) – official degree profile",
        "url": "https://corsi.unibo.it/1cycle/CLaBE/Presentation",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies CLaBE as a three-year first-cycle degree taught entirely in English and open to Italian and international students; its enrolment information identifies programme code 6609.",
        "supports": ["program.name", "program.level", "program.language", "program.location"],
    },
    {
        "id": "SRC-UNIBO-CLEF-PROFILE-2026",
        "university_id": "bologna", "title": "Economics and Finance (CLEF) – official degree profile",
        "url": "https://corsi.unibo.it/1cycle/EconomicsFinance/overview",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the three-year English-taught Bologna bachelor's degree in Economics and Finance (L-33); admission is limited-enrolment and selection criteria are announced annually.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.previous_cycle_access"],
    },
    {
        "id": "SRC-UNIBO-CLEF-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Economics and Finance – 2026/27 admission notice",
        "url": "https://corsi.unibo.it/s/3394/p/en/enrolling-clef/bando-clef-etac_a-a-2026-2027.pdf/@@download/file/Bando%20CLEF%20-ETAC_a.a.%202026-2027.pdf",
        "source_type": "Official programme admission notice", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Official 2026/27 selection notice names Economics and Finance (CLEF, Bologna), class L-33 R and annual selection process.",
        "supports": ["program.previous_cycle_application_windows", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIBO-MED-EN-PROFILE-2026",
        "university_id": "bologna", "title": "Medicine and Surgery – English-taught single-cycle course profile",
        "url": "https://corsi.unibo.it/singlecycle/MedicineAndSurgery/overview",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the Bologna English-taught six-year single-cycle degree (LM-41 R) with national restricted access; this is not a bachelor's-level-only degree.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration", "program.access"],
    },
    {
        "id": "SRC-UNIBO-MED-IT-PROFILE-2026",
        "university_id": "bologna", "title": "Medicina e chirurgia – Italian-taught single-cycle course profile",
        "url": "https://corsi.unibo.it/magistralecu/MedicinaChirurgia",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the Italian-language Bologna single-cycle degree in Medicine and Surgery, class LM-41 R, with nationally restricted admission.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
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
        "university_id": "bologna", "title": "Green Management and Sustainable Businesses – BBS professional master",
        "url": "https://www.bbs.unibo.it/en/master-fulltime/business-management-green-management-and-sustainable-businesses/",
        "source_type": "Official Bologna Business School programme page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies Green Management and Sustainable Businesses as a concentration in the one-year, 60-CFU professional Master in Business Management, with BBS course structure and not a standalone MSc/Laurea Magistrale. Current displayed application rounds are for the 2026/27 edition.",
        "supports": ["program.name", "program.level", "program.language", "program.program_type", "program.previous_cycle_application_windows"],
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
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Describes the Italian course's 2026/27 access via open semester and national ranking; this is cycle-specific and is not carried into 2027/28.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_route"],
    },
    {
        "id": "SRC-UNIBO-LAW-2026",
        "university_id": "bologna", "title": "Giurisprudenza – Bologna single-cycle degree profile and 2026/27 regulation",
        "url": "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/esplora-il-corso",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies Giurisprudenza as a five-year Italian-language single-cycle degree, class LMG/01, taught in Bologna; it is not a two-year MSc.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.duration"],
    },
    {
        "id": "SRC-UNIBO-COMMUNICATION-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – Bologna bachelor's profile",
        "url": "https://corsi.unibo.it/laurea/ScienzeComunicazione",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists an Italian-taught three-year Bologna bachelor's degree in Communication Sciences, class L-20 R, with restricted admission.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-MSC-2026",
        "university_id": "bologna", "title": "Ingegneria informatica – Bologna MSc profile and admission page",
        "url": "https://corsi.unibo.it/magistrale/ingegneriainformatica/index.html",
        "source_type": "Official degree programme profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Lists the two-year LM-32 Bologna MSc as taught in both Italian and English, with open access; the historic Italian-only label was inaccurate.",
        "supports": ["program.name", "program.level", "program.language", "program.location", "program.access"],
    },
    {
        "id": "SRC-UNIBO-ING-INF-ADMISSIONS-2026",
        "university_id": "bologna", "title": "Ingegneria informatica – 2026/27 admission requirements",
        "url": "https://corsi.unibo.it/magistrale/ingegneriainformatica/iscriversi-al-corso",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Provides 2026/27 curricular and English-language requirements and links the annual 2026/27 admission notice; no 2027/28 notice was linked on the reviewed page.",
        "supports": ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_application_route"],
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
        "source_type": "Official programme regulation PDF", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The regulation names the Bologna single-cycle degree in Giurisprudenza, class LMG/01 R, course code 6827, for students enrolling in AY 2026/27.",
        "supports": ["program.previous_cycle_course_listing"],
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
        "source_type": "Official degree programme and admission profile", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Identifies the English-taught Bologna single-cycle course and the annual national restricted-admission process. The course-specific admission test, places and dates are announced in annual calls; no 2027/28 call was reviewed here.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_route"],
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
        "source_type": "Official degree programme page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Names the active Business and Economics degree (CLaBE) and its current course codes; verifies identity without confirming the next academic year's admission call.",
        "supports": ["program.corrected_identity", "program.previous_cycle_course_listing"],
    },
    {
        "id": "SRC-UNIBO-DHDK-CALL-2026",
        "university_id": "bologna", "title": "Digital Humanities and Digital Knowledge – AY 2026/27 admission call",
        "url": "https://corsi.unibo.it/s/3391/p/en/digital-humanities-and-digital-knowledge-dhdk/call-dhdk-2026.pdf/@@download/file/Call%20DHDK%202026.pdf",
        "source_type": "Official programme admission notice PDF", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "Admission notice explicitly names the Second Cycle Degree Programme in Digital Humanities and Digital Knowledge for AY 2026/27; not evidence for 2027/28.",
        "supports": ["program.previous_cycle_course_listing", "program.previous_cycle_admission"],
    },
    {
        "id": "SRC-UNIBO-COMM-ADMISSION-2026",
        "university_id": "bologna", "title": "Scienze della comunicazione – 2026/27 admissions page",
        "url": "https://corsi.unibo.it/laurea/ScienzeComunicazione/iscriversi-al-corso",
        "source_type": "Official programme admission page", "accessed_at": "2026-11-10", "cycle": "2026-2027",
        "evidence": "The official page links an expired 2026/27 call and an additional selection notice, confirming the prior-cycle restricted-entry procedure only.",
        "supports": ["program.previous_cycle_admission", "program.previous_cycle_application_route"],
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
        ("legacy-024", "Mechanical Engineering for Sustainability", "MSc", "English", "Mechanical Engineering and Sustainability", ["SRC-UNIBO-MES-PROFILE-2026", "SRC-UNIBO-MES-ADMISSIONS-2026"], "Forlì"),
        ("legacy-025", "Business and Economics (CLaBE)", "BSc", "English", "Business and Economics", ["SRC-UNIBO-CLABE-PROFILE-2026", "SRC-UNIBO-CLABE-PROGRAM-CODE-2026"]),
        ("legacy-026", "Economics and Finance (CLEF)", "BSc", "English", "Economics and Finance", ["SRC-UNIBO-CLEF-PROFILE-2026", "SRC-UNIBO-CLEF-ADMISSIONS-2026"]),
        ("legacy-027", "Medicine and Surgery (English-taught single-cycle degree)", "Single-cycle Master's (LM-41)", "English", "Medicine and Surgery", ["SRC-UNIBO-MED-EN-PROFILE-2026", "SRC-UNIBO-MED-EN-2026-CALL"]),
        ("legacy-028", "Business Management — Green Management and Sustainable Businesses (BBS professional-master track)", "Professional Master's track", "English", "Sustainable Business and Green Management", ["SRC-UNIBO-BBS-GREEN-MGMT-2026"], "Bologna", "Professional Master's concentration; not a separate MSc/Laurea Magistrale"),
        ("legacy-147", "Ingegneria gestionale", "BSc", "Italian", "Industrial and Management Engineering", ["SRC-UNIBO-GESTIONALE-BSC-2026"]),
        ("legacy-148", "Economia e commercio", "BSc", "Italian", "Economics and Commerce", ["SRC-UNIBO-ECON-COMMERCIO-2026", "SRC-UNIBO-ECONOMIA-COMMERCIO-LOCATION-2026"], "Forlì"),
        ("legacy-149", "Medicina e chirurgia", "Single-cycle Master's (LM-41)", "Italian", "Medicine and Surgery", ["SRC-UNIBO-MED-IT-PROFILE-2026", "SRC-UNIBO-MED-IT-ENROL-2026"]),
        ("legacy-150", "Giurisprudenza", "Single-cycle Master's (LMG/01)", "Italian", "Law", ["SRC-UNIBO-LAW-2026", "SRC-UNIBO-GIURISPRUDENZA-REG-2026"]),
        ("legacy-151", "Scienze della comunicazione", "BSc", "Italian", "Communication Sciences", ["SRC-UNIBO-COMMUNICATION-2026", "SRC-UNIBO-COMM-ADMISSION-2026"]),
        ("legacy-152", "Ingegneria informatica", "MSc", "Italian and English", "Computer Engineering", ["SRC-UNIBO-ING-INF-MSC-2026", "SRC-UNIBO-ING-INF-ADMISSIONS-2026"]),
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

    apply_legacy_course_reviews(programs, fact)

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
