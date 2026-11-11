"""Politecnico di Torino course-catalogue review, checked 10 November 2026."""

CHECKED = "2026-11-10"
CATALOGUE = "https://www.polito.it/en/education/master-s-degree-programmes"
ADMISSIONS = "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/master-s-degree-programmes"
FOREIGN_ADMISSIONS = "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/master-s-degree-programmes/applicants-with-a-non-italian-qualification"
ENTRY_REQUIREMENTS = "https://www.polito.it/sites/default/files/2026-03/Annex%201_TABELLA%20REQUISITI%20LM%202627.pdf"
TUITION = "https://www.polito.it/en/education/services-and-life-at-politecnico/right-to-education-and-tuition-fees/tuition-fees"


def source(sid, title, url, cycle, evidence, supports, kind="Official admissions or course source"):
    return {"id": sid, "university_id": "politecnico-torino", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


PROGRAMS = {
    "legacy-011": {
        "name": "Computer Engineering", "profile": "SRC-POLITO-COMPUTER-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/computer-engineering",
        "language": "Italian and English", "field": "Computer Engineering and Computer Systems",
        "campus": "Main Campus", "class": "LM-32", "background": "Any field of Engineering; Computer Science",
        "english": "The programme profile lists Italian and English. The 2026/27 foreign-qualification annex lists this programme under its English route with IELTS 5.5; the general international page requires English B2, and Italian B2 for Italian-taught or mixed Italian/English programmes. Confirm the chosen track's applicable certificate rule.",
    },
    "legacy-012": {
        "name": "Cybersecurity Engineering", "profile": "SRC-POLITO-CYBER-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/cybersecurity-engineering",
        "language": "English", "field": "Cybersecurity and Information Security",
        "campus": "Main Campus", "class": "LM-32", "background": "Any field of Engineering; Computer Science",
        "english": "The 2026/27 foreign-qualification annex lists IELTS 5.5 for this English-taught programme; the general international page states English B2 or higher.",
    },
    "legacy-013": {
        "name": "Data Science and Engineering", "profile": "SRC-POLITO-DATA-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/data-science-and-engineering",
        "language": "English", "field": "Data Science and Computer Engineering",
        "campus": "Main Campus", "class": "LM-32", "background": "Any field of Engineering; Mathematics; Computer Science",
        "english": "The 2026/27 foreign-qualification annex lists IELTS 5.5 for this English-taught programme; the general international page states English B2 or higher.",
    },
    "legacy-014": {
        "name": "Automotive Engineering", "profile": "SRC-POLITO-AUTO-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/automotive-engineering",
        "language": "English", "field": "Automotive and Vehicle Engineering",
        "campus": "Mirafiori", "class": "LM-33", "background": "Automotive Engineering; Mechanical Engineering; Industrial Engineering; Electrical Engineering",
        "english": "The 2026/27 foreign-qualification annex lists IELTS 5.5 for this English-taught programme; the general international page states English B2 or higher.",
    },
    "legacy-015": {
        "name": "Aerospace Engineering", "profile": "SRC-POLITO-AERO-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/aerospace-engineering",
        "language": "Italian", "field": "Aerospace Engineering",
        "campus": "Main Campus", "class": "LM-20", "background": None,
        "english": "For the 2026/27 international admission cycle, Polito states B2 English and B2 Italian for Italian-taught programmes. The course-specific English-language requirements annex does not list this Italian-taught programme.",
    },
    "legacy-016": {
        "name": "ICT Engineering for Smart Societies", "profile": "SRC-POLITO-ICT-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/ict-engineering-for-smart-societies",
        "language": "English", "field": "Information and Communication Technologies",
        "campus": "Main Campus", "class": "LM-27", "background": "Any field of Engineering; Computer Science; Physics; Mathematics",
        "english": "The 2026/27 foreign-qualification annex lists IELTS 5.5 for this English-taught programme; the general international page states English B2 or higher.",
        "old_name": "ICT for Smart Societies",
        "identity_note": "The official course page says the Master's degree became ICT Engineering for Smart Societies starting in 2025/26. This is a title correction to the legacy tracker name.",
    },
    "legacy-017": {
        "name": "Quantum Engineering", "profile": "SRC-POLITO-QUANTUM-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/quantum-engineering",
        "language": "English", "field": "Quantum Engineering",
        "campus": "Main Campus", "class": "LM-29", "background": "Any field of Engineering; Physics; Mathematics",
        "english": "The 2026/27 foreign-qualification annex lists IELTS 5.5 for this English-taught programme; the general international page states English B2 or higher.",
    },
    "legacy-018": {
        "name": "Architecture Construction City", "profile": "SRC-POLITO-ARCHCC-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/architecture-construction-city",
        "language": "Italian and English", "field": "Architecture and Architectural Engineering",
        "campus": "Castello del Valentino", "class": "LM-4", "background": "Architecture (recommended)",
        "english": "The programme profile lists Italian and English. The 2026/27 foreign-qualification annex lists IELTS 5.5 for the English route; the general international page requires English B2 and Italian B2 for Italian-taught or mixed programmes. Confirm the chosen track's applicable certificate rule.",
    },
    "discovered-028": {
        "name": "Digital Skills for Sustainable Societal Transitions", "profile": "SRC-POLITO-DIGITAL-SKILLS-2026",
        "url": "https://www.polito.it/en/education/master-s-degree-programmes/digital-skills-for-sustainable-societal-transitions",
        "language": "English", "field": "Digital Skills and Societal Transitions (interdisciplinary)",
        "campus": "Castello del Valentino", "class": "LM-91", "background": "Information Technology and Computer Science; Architecture; Engineering; Geography; Economics; Public Policy and other listed fields",
        "english": "The 2026/27 foreign-qualification annex lists IELTS 5.5 for this English-taught programme; the general international page states English B2 or higher.",
        "discovered": True,
        "checked": "2026-11-11",
        "extra_sources": [
            "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026",
            "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-REQ-2026",
            "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-DEADLINES-2026",
        ],
        "identity_note": "Added as an interdisciplinary digital option: the 2026/27 course overview includes programming, database management and data elaboration, and the official entry annex lists Information Technology and Computer Sciences among recommended backgrounds. It is not a conventional Computer Science degree.",
    },
}


SOURCES = [
    source("SRC-POLITO-MSC-CATALOGUE-2026", "Master's degree programme catalogue", CATALOGUE, "2026-2027",
           "The official master's catalogue lists the reviewed degree pages as available programmes. The individual profiles identify academic year 2026/2027; this catalogue does not establish a first-year offer for 2027/28.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official programme catalogue"),
    source("SRC-POLITO-MSC-ADMISSIONS-2026", "Admissions and enrolment – Master's degree programmes", ADMISSIONS, "2026-2027",
           "Polito states that its master's programmes last two full-time academic years and total 120 ECTS. The listed special selection calls are for 2026/27; the reviewed page does not name the general 2027/28 candidate-course calls.",
           ["program.duration", "program.ects", "university.master_admissions_2027_2028"], "Official admissions page"),
    source("SRC-POLITO-MSC-FOREIGN-2026", "Applicants with a non-Italian qualification – Master's degree programmes", FOREIGN_ADMISSIONS, "2026-2027",
           "For the 2026/27 cycle, applicants need a foreign first-cycle degree giving access to second-cycle study, suitable academic performance, programme-specific curricular requirements and language evidence. English-taught programmes require English B2; Italian or mixed Italian/English programmes require English B2 and Italian B2. Applicants can select up to two programmes. The page gives 2026/27 calls (including a third call restricted to EU and non-EU residents in Italy) and a €50 application fee; these are historical and do not set 2027/28 dates or fees.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.application_windows", "program.application_fee_2027_2028"], "Official international admissions page"),
    source("SRC-POLITO-MSC-ENTRY-ANNEX-2026", "2026/27 entry requirements for Master's programmes", ENTRY_REQUIREMENTS, "2026-2027",
           "The official one-page annex gives course-specific language minima and recommended academic backgrounds. It lists IELTS 5.5 for the English routes of Automotive Engineering, Computer Engineering, Cybersecurity Engineering, Data Science and Engineering, ICT Engineering for Smart Societies, Quantum Engineering and Architecture Construction City. Recommended backgrounds vary by course; these are recommendations, not stated as automatic eligibility rules. Digital Skills lists Information Technology and Computer Sciences among its recommended backgrounds. The annex is not a 2027/28 requirements document.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement"], "Official PDF admission requirements"),
    source("SRC-POLITO-TUITION-2026", "Tuition fees and EDISU scholarships", TUITION, "2026-2027",
           "The official page links the 2026/27 tuition regulation applicable to master's students and identifies ISEE/ISEE Parificato procedures for reductions. It links EDISU Piemonte benefits for 2026/27. No 2027/28 fee regulation or course-specific scholarship amount is recorded by this source.",
           ["program.previous_cycle_tuition", "program.previous_cycle_scholarships", "program.tuition_2027_2028", "program.scholarships_2027_2028"], "Official tuition and aid page"),
]

SOURCES.extend([
    source("SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026", "Admission to Master's Degree Programmes – Architecture Area a.y. 2026/2027", "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/master-s-degree-programmes/applicants-with-an-italian-qualification/architecture-area-ay-20262027", "2026-2027",
           "For the 2026/27 Italian-qualification route, Digital Skills for Sustainable Societal Transitions is among the Master's programmes admitting in both semesters. Applicants use Apply@polito; the page says a fee is required for applicants from other Italian universities but does not state its amount. This is a prior-cycle route and does not establish a 2027/28 call.",
           ["program.previous_cycle_admission_route", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.availability_2027_2028"], "Official Italian-qualification admissions page"),
    source("SRC-POLITO-DIGITAL-SKILLS-ITALIAN-REQ-2026", "Requirements for applicants from other universities a.y. 2026/27 – Digital Skills", "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/master-s-degree-programmes/applicants-with-an-italian-qualification/architecture-area-ay-20262027/requisiti-per-studenti-provenienti-da-altri-atenei-aa-202627", "2026-2027",
           "The 2026/27 Italian-qualification rules list L-8, L-9, L-31 and L-35 degrees, or alternatively at least 25 CFU in the specified first subject group and 45 CFU in the second group, subject to committee review. They set academic-average thresholds by prior university, require English B2 (IELTS 5.5 equivalent, with listed exemptions), and describe handling of curricular gaps. These are historical criteria, not confirmed for 2027/28.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_english_requirement", "program.previous_cycle_admission_route", "program.program_specific_requirements_2027_2028"], "Official Italian-qualification requirements page"),
    source("SRC-POLITO-DIGITAL-SKILLS-ITALIAN-DEADLINES-2026", "Deadlines Architecture Area a.y. 2026/27 – Digital Skills", "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/master-s-degree-programmes/applicants-with-an-italian-qualification/scadenze-area-architettura-aa-202627", "2026-2027",
           "The 2026/27 deadline page gives separate first- and second-semester Apply@polito windows for Digital Skills, including application closing dates, scheduled admission tests, result dates and enrollment deadlines. Direct fresh GET returned HTTP 200; its dates are not 2027/28 dates.",
           ["program.previous_cycle_application_windows", "program.previous_cycle_entrance_test", "program.application_windows", "program.availability_2027_2028"], "Official Italian-qualification deadlines page"),
])

_profile_metadata = {
    "legacy-011": ("Computer Engineering MSc profile", "The profile identifies a 2026/27 Master's degree, Italian and English delivery, LM-32 and Main Campus.", "2026-2027"),
    "legacy-012": ("Cybersecurity Engineering MSc profile", "The profile identifies a 2026/27 English Master's degree, LM-32 and Main Campus.", "2026-2027"),
    "legacy-013": ("Data Science and Engineering MSc profile", "The profile identifies a 2026/27 English Master's degree, LM-32 and Main Campus.", "2026-2027"),
    "legacy-014": ("Automotive Engineering MSc profile", "The profile identifies a 2026/27 English Master's degree, LM-33 and the Mirafiori campus.", "2026-2027"),
    "legacy-015": ("Aerospace Engineering MSc profile", "The profile identifies a 2026/27 Italian Master's degree, LM-20 and Main Campus.", "2026-2027"),
    "legacy-016": ("ICT Engineering for Smart Societies MSc profile", "The profile identifies a 2026/27 English Master's degree, LM-27 and Main Campus. It says the title changed from ICT for Smart Societies starting in 2025/26.", "2026-2027"),
    "legacy-017": ("Quantum Engineering MSc profile", "The profile identifies a 2026/27 English Master's degree, LM-29 and Main Campus.", "2026-2027"),
    "legacy-018": ("Architecture Construction City MSc profile", "The profile identifies a 2026/27 Master's degree, Italian and English delivery, LM-4 and Castello del Valentino.", "2026-2027"),
    "discovered-028": ("Digital Skills for Sustainable Societal Transitions MSc profile", "The profile identifies a 2026/27 English Master's degree, LM-91 and Castello del Valentino. Its overview describes programming, database management, data elaboration, business management and sustainable-transition contexts.", "2026-2027"),
}
for pid, record in PROGRAMS.items():
    title, evidence, cycle = _profile_metadata[pid]
    SOURCES.append(source(record["profile"], title, record["url"], cycle, evidence,
                          ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity", "program.previous_cycle_program_requirements"],
                          "Official course profile"))


def fact(value, status, sources=(), note=None):
    return {"value": value, "status": status, "source_ids": list(sources), "notes": note}


def apply(universities, programs, fact_builder):
    uni = next(u for u in universities if u["id"] == "politecnico-torino")
    uni.update(research_stage="PARTIALLY_RESEARCHED", research_summary=REPORT, last_checked=CHECKED)
    uni["coverage"]["program_level_review"] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    rows = {p["id"]: p for p in programs if p["university_id"] == "politecnico-torino"}
    for pid, record in PROGRAMS.items():
        p = rows[pid]
        profile = record["profile"]
        extra_sources = record.get("extra_sources", [])
        src_ids = [profile, "SRC-POLITO-MSC-CATALOGUE-2026", "SRC-POLITO-MSC-ADMISSIONS-2026",
                   "SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-MSC-ENTRY-ANNEX-2026", "SRC-POLITO-TUITION-2026", *extra_sources]
        p["program"] = record["name"]
        p["last_checked"] = record.get("checked", CHECKED)
        p["overall_status"] = "REQUIRES_VERIFICATION"
        p["source_ids"] = src_ids
        if record.get("discovered"):
            p["discovery_source"] = "newly_discovered"
        note = "This field describes the official 2026/27 course profile only; the 2027/28 first-year offer and terms remain unverified."
        if record.get("identity_note"):
            note = record["identity_note"] + " The 2027/28 first-year offer remains unverified."
        for field, value in (("level", "MSc"), ("language", record["language"]), ("field", record["field"])):
            p[field] = fact_builder(value, "REQUIRES_VERIFICATION", [profile], note)
        p["availability_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            [profile, "SRC-POLITO-MSC-CATALOGUE-2026", "SRC-POLITO-MSC-ADMISSIONS-2026", *extra_sources],
            "The latest named course profile and catalogue reviewed are for 2026/27. No 2027/28 first-year offer for this course was confirmed; no discontinuation is inferred.")
        p["previous_cycle_tags"] = {"level": "MSc", "language": record["language"], "field": record["field"],
            "cycle": "2026-2027", "label": "Official 2026/27 profile and requirements only; 2027/28 first-year availability remains unverified"}
        if record.get("old_name"):
            p["previous_tracker_tags"] = {"level": "MSc", "language": "English", "field": "Engineering",
                "label": f"Legacy tracker title: {record['old_name']}; official course title changed starting in 2025/26."}
        elif pid == "legacy-011":
            p["previous_tracker_tags"] = {"level": "MSc", "language": "English", "field": "Computer Science",
                "label": "Legacy tracker described this as English-only; the 2026/27 official profile lists Italian and English."}
        elif pid == "legacy-015":
            p["previous_tracker_tags"] = {"level": "MSc", "language": "English", "field": "Engineering",
                "label": "Legacy tracker described this as English-only; the 2026/27 official profile lists Italian."}
        elif pid == "legacy-018":
            p["previous_tracker_tags"] = {"level": "MSc", "language": "English", "field": "Architecture",
                "label": "Legacy tracker described this as English-only; the 2026/27 official profile lists Italian and English."}
        p["facts"]["previous_cycle_course_listing"] = fact_builder({
            "academic_year": "2026/27", "official_name": record["name"], "level": "MSc",
            "language": record["language"], "campus": record["campus"], "duration_years": 2,
            "ects": 120, "degree_class": record["class"],
            "admissions": "Uncapped number of students; evaluation of admission requirements"},
            "CONFIRMED", [profile, "SRC-POLITO-MSC-ADMISSIONS-2026"],
            "Official 2026/27 profile details; the published admissions mode is not a 2027/28 guarantee.")
        p["facts"]["previous_cycle_course_identity"] = fact_builder(record["name"], "CONFIRMED",
            [profile, "SRC-POLITO-MSC-CATALOGUE-2026"], record.get("identity_note") or "Matches the official 2026/27 course title and level.")
        requirement_status = "CONFIRMED" if record.get("background") else "REQUIRES_VERIFICATION"
        requirement = ("For the 2026/27 foreign-qualification route, the official annex lists this recommended academic background: "
                       + record["background"] + ". The annex calls this recommended, not a binding minimum. The general route also requires a suitable foreign first-cycle qualification and Academic Committee review.") if record.get("background") else (
                       "The 2026/27 course profile says admission is by evaluation of admission requirements. The foreign-applicant route requires a suitable first-cycle degree, academic performance and curricular assessment, but the course-specific annex reviewed covers English programmes and does not list this Italian-taught course.")
        p["facts"]["previous_cycle_program_requirements"] = fact_builder(requirement, requirement_status,
            ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-MSC-ENTRY-ANNEX-2026", profile],
            "Previous-cycle admission context only; do not carry these criteria into the 2027/28 application without the new annual rules.")
        p["facts"]["previous_cycle_english_requirement"] = fact_builder(record["english"], "CONFIRMED",
            ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-MSC-ENTRY-ANNEX-2026", profile],
            "Language rules and IELTS minima are from 2026/27; accepted evidence and course-language pathways must be rechecked for 2027/28.")
        p["facts"]["program_specific_requirements_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-MSC-ENTRY-ANNEX-2026", *extra_sources],
            "No 2027/28 course-specific admission regulation or call was identified; the linked course criteria are for 2026/27.")
        p["facts"]["application_windows"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-MSC-ADMISSIONS-2026", *extra_sources],
            "The reviewed deadlines page contains 2026/27 calls only. No 2027/28 application window was confirmed for this candidate.")
        p["facts"]["application_fee_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-POLITO-MSC-FOREIGN-2026", *extra_sources], "The €50 fee shown on the foreign-applicant page is for 2026/27; no 2027/28 application fee was confirmed.")
        p["facts"]["previous_cycle_application_windows"] = fact_builder({
            "academic_year": "2026/27",
            "foreign_qualification_call_1": {"opening": "2025-12-19", "closing_extended": "2026-02-13 14:00 Europe/Rome", "results_extended": "2026-04-15"},
            "foreign_qualification_call_2": {"opening": "2026-03-18", "closing_extended": "2026-04-17 14:00 Europe/Rome", "technical_extension_to": "2026-04-20 14:00 Europe/Rome", "results_extended": "2026-06-22"},
            "third_call_if_engineering_area": {"opening": "2026-11-03", "closing": "2026-11-17 14:00 Europe/Rome", "results": "2027-01-29", "eligibility": "EU applicants and non-EU applicants residing in Italy"}},
            "CONFIRMED", ["SRC-POLITO-MSC-FOREIGN-2026"],
            "These are foreign-qualification dates for 2026/27 only; the third call is restricted by applicant residence and programme area. Architecture Construction City is not assigned the Engineering-area third call.")
        p["facts"]["previous_cycle_application_fee"] = fact_builder({"academic_year": "2026/27", "fee_eur": 50,
            "scope": "Non-Italian qualification application; payable online by Visa or Mastercard"}, "CONFIRMED",
            ["SRC-POLITO-MSC-FOREIGN-2026"], "Prior-cycle fee only; do not use as the 2027/28 fee.")
        if pid == "discovered-028":
            p["facts"]["previous_cycle_admission_route"] = fact_builder({
                "academic_year": "2026/27",
                "applicant_scope": "Applicants with an Italian qualification",
                "application_platform": "Apply@polito",
                "semester_options": ["first semester", "second semester"],
                "evaluation": "Curricular and academic-performance assessment under the Italian-qualification requirements; the course requirements are reviewed by the relevant committee.",
                "fee_note": "A fee is required for applicants from other Italian universities; the amount is not stated on the reviewed course-area page.",
            }, "CONFIRMED", ["SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026", "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-REQ-2026"],
                "This is the 2026/27 Italian-qualification route. Foreign-qualification applicants follow separate rules and the 2027/28 route is unverified.")
            p["facts"]["previous_cycle_program_requirements"] = fact_builder({
                "academic_year": "2026/27",
                "italian_qualification": {
                    "eligible_degree_classes": ["L-8", "L-9", "L-31", "L-35"],
                    "alternative_curricular_credits": {
                        "group_1_minimum_cfu": 25,
                        "group_1_ssd_codes_dm270_2004": ["MAT/03", "MAT/05", "MAT/07", "MAT/08", "MAT/09", "FIS/01", "ING-INF/05", "INF/01", "ING-IND/35", "IUS/10", "SECS-P/02", "SECS-P/07", "SECS-P/08", "SPS/04", "SPS/08", "SPS/10"],
                        "group_1_ssd_codes_dm1648_2023": ["MATH-02/B", "MATH-03/A", "MATH-04/A", "MATH-05/A", "MATH-06/A", "PHYS-01/A", "PHYS-03/A", "IINF-05/A", "INFO-01/A", "IEGE-01/A", "GIUR-06/A", "ECON-02/A", "ECON-06/A", "ECON-07/A", "GSPS-02/A", "GSPS-06/A", "GSPS-08/B"],
                        "group_2_minimum_cfu": 45,
                        "group_2_ssd_codes_dm270_2004": ["ICAR/06", "ICAR/08", "ICAR/12", "ICAR/14", "ICAR/18", "ICAR/20", "ICAR/21", "ICAR/22", "L-ART/06", "M-GGR/01", "M-GGR/02", "SPS/07", "SPS/09", "SECS-P/01", "SECS-P/06", "SECS-P/09", "SECS-P/10", "SECS-S/01", "SECS-S/03", "SECS-S/06", "ING-IND/10", "ING-IND/11", "ING-IND/16", "ING-IND/22", "M-PSI/01", "M-STO/04"],
                        "group_2_ssd_codes_dm1648_2023": ["CEAR-04/A", "CEAR-06/A", "CEAR-08/C", "CEAR-09/A", "CEAR-11/A", "CEAR-12/A", "CEAR-12/B", "CEAR-03/C", "PEMM-01/B", "GEOG-01/A", "GEOG-01/B", "GSPS-05/A", "GSPS-08/A", "ECON-01/A", "ECON-04/A", "ECON-09/A", "ECON-08/A", "STAT-01/A", "STAT-02/A", "STAT-04/A", "IIND-07/A", "IIND-07/B", "IIND-04/A", "IMAT-01/A", "PSIC-01/A", "HIST-03/A"],
                        "assessment": "A committee checks curricular requirements. Overlapping credits count first toward group 1, with residual credits toward group 2. The page allows up to 10 missing credits at Academic Advisor discretion; larger gaps are escalated to the Coordinator or Deputy Coordinator.",
                    },
                    "academic_performance": {
                        "other_universities_except_university_of_turin": "Weighted average at least 25/30, excluding the lowest 28 credits, without rounding.",
                        "university_of_turin": "No average threshold if time to degree is 4 years or less; at least 24/30 if over 4 and up to 5 years; at least 25/30 if over 5 years.",
                    },
                    "english": "B2 CEFR (IELTS 5.5 equivalence), with published exemptions.",
                },
                "foreign_qualification": "Separate 2026/27 route; course-specific foreign-entry annex lists recommended backgrounds, while the general foreign route requires an eligible first-cycle degree, academic performance, curricular assessment and English B2.",
            }, "CONFIRMED", ["SRC-POLITO-DIGITAL-SKILLS-ITALIAN-REQ-2026", "SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-MSC-ENTRY-ANNEX-2026"],
                "Previous-cycle rules only. Verify the annual call and applicant-specific route before relying on these criteria for 2027/28.")
            p["facts"]["application_fee_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
                ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026"],
                "The €50 fee shown on the foreign-applicant page is for 2026/27; the Italian-qualification route also requires a fee for applicants from other Italian universities, but its amount was not found. No 2027/28 application fee was confirmed.")
            p["facts"]["previous_cycle_english_requirement"] = fact_builder(
                "For the 2026/27 Italian-qualification route, English B2 CEFR is required; IELTS 5.5 is the stated equivalent and the official page lists exemptions. The separate 2026/27 foreign-qualification page also requires English B2 for English-taught programmes.",
                "CONFIRMED", ["SRC-POLITO-DIGITAL-SKILLS-ITALIAN-REQ-2026", "SRC-POLITO-MSC-FOREIGN-2026"],
                "Prior-cycle language evidence only; accepted certificates and exemptions must be checked in the 2027/28 rules.")
            p["facts"]["previous_cycle_application_windows"] = fact_builder({
                "academic_year": "2026/27",
                "foreign_qualification": {
                    "call_1": {"opening": "2025-12-19", "closing_extended": "2026-02-13 14:00 Europe/Rome", "results_extended": "2026-04-15"},
                    "call_2": {"opening": "2026-03-18", "closing_extended": "2026-04-17 14:00 Europe/Rome", "technical_extension_to": "2026-04-20 14:00 Europe/Rome", "results_extended": "2026-06-22"},
                    "third_call_if_engineering_area": {"opening": "2026-11-03", "closing": "2026-11-17 14:00 Europe/Rome", "results": "2027-01-29", "eligibility": "EU applicants and non-EU applicants residing in Italy"},
                },
                "italian_qualification": {
                    "semester_intakes": ["first semester", "second semester"],
                    "first_semester": {"applications_open": "2026-06-04", "application_deadline": "2026-08-27", "admission_test": "2026-09-08 14:00 Europe/Rome", "test_location": "Aula Astengo, Castello del Valentino", "results": "2026-09-10", "enrolment_deadline": "2026-11-02", "identity_verification_deadline_for_other_universities": "2026-12-03"},
                    "second_semester": {"applications_open": "2026-12-11", "application_deadline": "2027-01-18", "admission_test": "2027-01-27 14:00 Europe/Rome", "test_location": "Aula Astengo, Castello del Valentino", "results": "2027-01-29", "enrolment_deadline": "2027-02-22", "identity_verification_deadline_for_other_universities": "2027-04-08"},
                },
            }, "CONFIRMED", ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026", "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-DEADLINES-2026"],
                "Foreign-qualification and Italian-qualification timelines are separate 2026/27 routes. The scheduled course admission tests are not treated as proof of selectivity or as standardized tests. None of these dates carries over to 2027/28.")
            p["facts"]["previous_cycle_entrance_test"] = fact_builder({
                "academic_year": "2026/27",
                "italian_qualification_route": {
                    "first_semester": {"date_time": "2026-09-08 14:00 Europe/Rome", "location": "Aula Astengo, Castello del Valentino", "published_as": "Admission test"},
                    "second_semester": {"date_time": "2027-01-27 14:00 Europe/Rome", "location": "Aula Astengo, Castello del Valentino", "published_as": "Admission test"},
                },
                "foreign_qualification_route": "The reviewed foreign-qualification page describes academic and curricular review; no standardized test is listed there.",
            }, "CONFIRMED", ["SRC-POLITO-DIGITAL-SKILLS-ITALIAN-DEADLINES-2026", "SRC-POLITO-MSC-FOREIGN-2026"],
                "The Italian route schedule calls these admission tests but does not publish format, scores or selectivity on the deadline page; do not infer those details.")
            p["facts"]["previous_cycle_application_fee"] = fact_builder({
                "academic_year": "2026/27",
                "non_Italian_qualification": {"fee_eur": 50, "scope": "Apply@polito application for non-Italian qualifications; payable online by Visa or Mastercard"},
                "Italian_qualification": {"fee_eur": None, "scope": "The route page says applicants from other Italian universities must pay a fee; amount not stated in the reviewed course-area page."},
            }, "CONFIRMED", ["SRC-POLITO-MSC-FOREIGN-2026", "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026"],
                "The €50 charge applies to the foreign-qualification route. The domestic-route amount is unknown from reviewed sources; it is not assumed to be zero.")
            p["facts"]["available_places_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
                [profile, "SRC-POLITO-DIGITAL-SKILLS-ITALIAN-2026"],
                "The 2026/27 profile says the course had an uncapped number of students. No 2027/28 places or admission-capacity notice was identified, so the previous-cycle label does not establish next-cycle capacity.")
        p["facts"]["previous_cycle_international_admission"] = fact_builder({
            "academic_year": "2026/27", "portal": "Apply@PoliTO", "programme_choices": 2,
            "selection": "Administrative completeness check followed by Academic Committee review of academic performance and curricular background",
            "foreign_degree": "Bachelor's degree or equivalent qualification giving access to second-cycle study"}, "CONFIRMED",
            ["SRC-POLITO-MSC-FOREIGN-2026"], "Historical international-admission workflow; 2027/28 calls and applicant eligibility must be rechecked.")
        p["facts"]["previous_cycle_tuition"] = fact_builder({"academic_year": "2026/27",
            "regulation": "Polito tuition regulation applies to Master's students; reductions use ISEE/ISEE Parificato procedures; course pages do not state a fixed total."},
            "CONFIRMED", ["SRC-POLITO-TUITION-2026"], "No numeric programme-specific amount is inferred; this is prior-cycle university-wide fee guidance.")
        p["facts"]["tuition_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-TUITION-2026"],
            "The official tuition page reviewed links the 2026/27 regulation; no 2027/28 schedule or programme-specific amount was confirmed.")
        p["facts"]["previous_cycle_scholarships"] = fact_builder({"academic_year": "2026/27",
            "regional_aid": "EDISU Piemonte competitive scholarships and housing benefits are linked from Polito's tuition page; annual eligibility, amounts and application are determined by the regional call."},
            "CONFIRMED", ["SRC-POLITO-TUITION-2026"], "No course-specific 2026/27 award amount is claimed; the current-cycle page links the regional scheme only.")
        p["facts"]["scholarships_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-TUITION-2026"],
            "No 2027/28 course-specific scholarship or EDISU award was confirmed in the reviewed sources.")
        p["facts"]["acceptance_rate"] = fact_builder(None, "UNAVAILABLE", [profile, "SRC-POLITO-MSC-ENTRY-ANNEX-2026"],
            "No complete official applicant denominator and admitted-student count was found. The profile's uncapped-admission label is not an acceptance rate.")

    uni["cycle_facts"]["master_program_inventory_2026_2027"] = fact_builder({
        "legacy_program_rows_reviewed": 8, "identity_matches": 8,
        "title_corrections": {"legacy-016": "ICT for Smart Societies → ICT Engineering for Smart Societies"},
        "language_corrections": {"legacy-011": "Italian and English", "legacy-015": "Italian", "legacy-018": "Italian and English"},
        "additional_interdisciplinary_candidate": "discovered-028 Digital Skills for Sustainable Societal Transitions",
        "catalogue_scope": "Official 2026/27 profile evidence only; no per-course 2027/28 first-year availability confirmed."},
        "CONFIRMED", ["SRC-POLITO-MSC-CATALOGUE-2026"] + [record["profile"] for record in PROGRAMS.values()],
        "All eight legacy course leads have an official 2026/27 profile match; candidate offer availability for 2027/28 remains pending.")
    uni["cycle_facts"]["master_admissions_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
        ["SRC-POLITO-MSC-ADMISSIONS-2026", "SRC-POLITO-MSC-FOREIGN-2026"],
        "The reviewed general Master's and international-applicant pages publish 2026/27 calls and dates; no general 2027/28 MSc call or deadline schedule was found in this review.")
    uni["cycle_facts"]["master_tuition_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-TUITION-2026"],
        "The reviewed official fee page links the 2026/27 regulation; no 2027/28 regulation was confirmed.")
    uni["cycle_facts"]["master_scholarships_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-POLITO-TUITION-2026"],
        "The Polito page links EDISU's 2026/27 competition; no general 2027/28 award or course-specific call was confirmed in this review.")


BATCH = {
    "id": "polito-program-catalogue-and-2027-28-intake-review",
    "status": "partial",
    "result": "Matched all eight legacy MSc leads against official 2026/27 course profiles and the course-specific entry annex. Corrected Computer Engineering and Architecture Construction City to Italian/English, Aerospace Engineering to Italian, and ICT for Smart Societies to the current title ICT Engineering for Smart Societies. Recorded course codes, campuses, two-year/120-ECTS duration, recommended backgrounds, English requirements, historical international application windows and €50 foreign-application fee. Added the interdisciplinary English MSc Digital Skills for Sustainable Societal Transitions because its official admission annex explicitly lists IT and Computer Science backgrounds. All nine Polito candidate programmes remain pending for 2027/28 first-year availability, requirements, dates, application fees, tuition and scholarships; the admission and fee sources reviewed are for 2026/27. Acceptance rates were not officially published in the reviewed sources.",
}

REPORT = "Politecnico di Torino's official 2026/27 Master's catalogue and course profiles were checked against all eight legacy candidates. Computer Engineering is Italian and English; Aerospace Engineering is Italian; Architecture Construction City is Italian and English; and the current title for the legacy ICT for Smart Societies row is ICT Engineering for Smart Societies (English). The other matched candidates are English-taught. Profiles identify a two-year, 120-ECTS MSc structure, course codes and campuses; the 2026/27 foreign-applicant annex supplies recommended backgrounds and IELTS 5.5 minima for the English routes. Those backgrounds are explicitly recommendations, not binding minimum entry conditions. The foreign-admissions page gives a first-cycle qualification, suitable academic performance, course-specific curricular review, and B2 language rules. Its 2026/27 dates and €50 application fee are retained as historical evidence only. The current fee page links 2026/27 tuition regulations and EDISU aid; no 2027/28 fee schedule or scholarship award was confirmed. An additional interdisciplinary English MSc, Digital Skills for Sustainable Societal Transitions, was identified because the official 2026/27 admissions annex lists Information Technology and Computer Sciences among its recommended backgrounds; it is not a conventional Computer Science degree. For this candidate, the 2026/27 Italian-qualification pages additionally confirm first- and second-semester entry routes, class and credit-group eligibility, academic thresholds, English B2 and scheduled admission-test dates; the amount of the domestic-route application fee was not found. The checked named course profiles are for 2026/27, so all nine course-level 2027/28 first-year offers and current admission, fee and scholarship terms remain unverified. No official acceptance-rate denominator and admitted count were found."
