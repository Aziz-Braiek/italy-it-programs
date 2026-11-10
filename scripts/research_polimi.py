"""Politecnico di Milano candidate-programme review, checked 10 November 2026."""

CHECKED = "2026-11-10"
MSC_LIST = "https://www.polimi.it/en/education/laurea-magistrale-programmes"


def source(sid, title, url, cycle, evidence, supports, kind="Official programme catalogue"):
    return {"id": sid, "university_id": "politecnico-milano", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


SOURCES = [
    source("SRC-POLIMI-MSC-LIST-2026", "Master of Science programme catalogue", MSC_LIST, "2026-2027",
           "The official catalogue lists 45 Laurea Magistrale programmes, including Computer Science and Engineering, Cyber Risk Strategy and Governance, High Performance Computing Engineering, Biomedical Engineering, Mechanical Engineering, Aeronautical Engineering, Space Engineering, Design & Engineering, Architecture, Communication Design and Civil Engineering. It lists no standalone MSc named Artificial Intelligence or Aerospace Engineering. The list is current catalogue evidence, not a named 2027/28 first-year intake notice." ,
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"]),
    source("SRC-POLIMI-CSE-2026", "Computer Science and Engineering MSc profile", "https://www.polimi.it/en/education/laurea-programmes/programme-detail/computer-science-and-engineering", "2026-2027",
           "Identifies a two-year English-taught Master of Science at Milano Leonardo. The course is 120 ECTS and offers Computer Science and Engineering, Business and Innovation, and Artificial Intelligence study plans. Foreign-degree applicants need a comparable first-cycle qualification and their academic background is assessed against programme criteria; the profile is not a 2027/28 first-year offer.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official course profile"),
    source("SRC-POLIMI-CYBER-2025", "Cyber Risk Strategy and Governance MSc profile", "https://www.polimi.it/en/education/laurea-magistrale-programmes/programme-detail/cyber-risk-strategy-and-governance", "2025-2026",
           "The official page expressly says its information is for 2025/26 and may change in 2026/27. It identifies a two-year English MSc at the Milan partner-university campus, delivered with Bocconi. Foreign-degree applicants are evaluated competitively by a joint committee using transcript, curriculum and motivation letter; the page says there are no fixed admission criteria. This historical profile does not prove 2026/27 or 2027/28 intake.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official course profile"),
    source("SRC-POLIMI-HPC-2026", "High Performance Computing Engineering MSc profile", "https://www.polimi.it/en/education/laurea-programmes/programme-detail/high-performance-computing-engineering", "2026-2027",
           "Identifies a two-year English MSc at Milano Leonardo. Foreign applicants need an equivalent Bachelor’s degree in Computer Science/Engineering, Mathematical Engineering or a related field. The official profile specifies at least 20 ECTS in Computer Science/Computer Engineering, 20 ECTS in Mathematics/Statistics and 10 ECTS in Physics, with committee assessment and possible additional requirements.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-BIOMED-MSC-2026", "Biomedical Engineering MSc profile", "https://www.polimi.it/en/education/laurea-magistrale-programmes/programme-detail/biomedical-engineering-1", "2026-2027",
           "Identifies a two-year LM-21 Master of Science at Milano Leonardo taught in Italian or English. Foreign-degree applicants need an equivalent Bachelor’s qualification and relevant engineering preparation; eligibility is evaluated from the prior academic career under the programme rules. This corrects the previous tracker’s English-only label for the prior-cycle course.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-MECH-2025", "Mechanical Engineering MSc profile", "https://www.polimi.it/en/education/laurea-magistrale-programmes/programme-detail/mechanical-engineering-1", "2025-2026",
           "The official profile identifies a two-year English-taught MSc with campuses in Lecco, Piacenza and Milano Bovisa. The page states that its information refers to 2025/26 and may change in 2026/27; annual admission and course conditions must therefore be rechecked.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official course profile"),
    source("SRC-POLIMI-AERONAUTICAL-2026", "Aeronautical Engineering MSc profile", "https://www.polimi.it/en/education/laurea-programmes/programme-detail/aeronautical-engineering", "2026-2027",
           "Identifies a two-year English MSc at Milano Bovisa. Applicants with a foreign Bachelor’s qualification need comparable first-cycle study and adequate preparation in mathematics, physics and aerospace or mechanical engineering; a committee evaluates the academic curriculum and performance. This is a distinct named programme from the Italian Aerospace Engineering BSc and Space Engineering MSc.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-SPACE-2026", "Space Engineering MSc profile", "https://www.polimi.it/en/education/laurea-magistrale-programmes/programme-detail/space-engineering", "2026-2027",
           "Identifies a separate two-year English-taught Space Engineering MSc. Foreign applicants need a comparable first-level qualification and relevant mathematical, physical and aerospace/mechanical preparation. It is not the same name as the prior tracker’s generic Aerospace Engineering MSc lead.",
           ["program.previous_cycle_course_identity", "program.previous_cycle_course_listing"], "Official course profile"),
    source("SRC-POLIMI-DESIGNENG-2025", "Design & Engineering MSc profile", "https://www.polimi.it/en/education/laurea-programmes/programme-detail/design-engineering", "2025-2026",
           "Identifies a two-year English MSc at Milano Bovisa. The page expressly describes 2025/26 information and warns it may change in 2026/27. It gives foreign applicants’ degree-field and disciplinary-credit expectations and states admission is subject to individual-preparation assessment and a merit ranking; annual deadlines and rules still need checking.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-ARCH-MSC-2026", "Architecture MSc profile", "https://www.polimi.it/en/education/laurea-programmes/programme-detail/architecture", "2026-2027",
           "Identifies a two-year MSc at Milano Leonardo taught in Italian or English. Its admission profile requires a Bachelor’s degree in Architecture and a portfolio. Language and specialisation depend on the chosen study plan; the old English-only tag is too broad.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-COMM-DESIGN-2026", "Communication Design MSc profile", "https://www.polimi.it/en/education/laurea-magistrale-programmes/programme-detail/communication-design-1", "2026-2027",
           "Identifies a two-year MSc at Milano Bovisa taught in Italian or English. Foreign-degree candidates need a comparable first-cycle design or related qualification; programme-board review, individual preparation/ranking and at least B2 English are described on the course page. This corrects the previous tracker’s English-only label.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-AERO-BSC-2026", "Ingegneria Aerospaziale bachelor’s profile", "https://www.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/ingegneria-aerospaziale", "2026-2027",
           "Identifies Ingegneria Aerospaziale as a three-year Italian Laurea (BSc equivalent), L-9, at Milano Bovisa. First-year admission is through the annual engineering admission process; the profile does not publish the 2027/28 named offer or call.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-BIOMED-BSC-2026", "Ingegneria Biomedica bachelor’s profile", "https://www.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/ingegneria-biomedica", "2026-2027",
           "Identifies a three-year Italian Laurea, classes L-8/L-9, with the 2026/27 first year at Milano Bovisa and later years at Milano Leonardo. This is the BSc and must remain separate from the similarly named MSc. The 2027/28 first-year call is not established by this course profile.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-MGMT-BSC-2026", "Ingegneria Gestionale bachelor’s profile", "https://www.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/ingegneria-gestionale", "2026-2027",
           "Identifies a three-year Italian Laurea, classes L-8/L-9, at Cremona and Milano Bovisa. Programme access uses the Engineering admission process and annual call; current profile does not establish a 2027/28 programme-specific first-year offer.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-COMP-BSC-2026", "Ingegneria Informatica bachelor’s profile", "https://dynamicpoli.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/ingegneria-informatica", "2026-2027",
           "Identifies a three-year Italian Laurea, class L-8, at Milano Leonardo and Cremona. The course page describes the BSc-level computer-engineering degree, distinct from the Computer Science and Engineering MSc. Annual Engineering access tests and calls apply; this page is not a 2027/28 course offer.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-INTERIOR-BSC-2026", "Design degli Interni bachelor’s profile", "https://www.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/design-degli-interni", "2026-2027",
           "Identifies a three-year Italian Laurea, class L-4, at Milano Bovisa. It is a design BSc with its own admission route; the 2027/28 call, places and deadlines are not published in this profile.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-ARCH-BSC-2026", "Progettazione dell'Architettura bachelor’s profile", "https://www.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/progettazione-dellarchitettura", "2026-2027",
           "Identifies a three-year Laurea, class L-17, at Milano Leonardo, Piacenza and Mantova. The page lists Italian or English delivery, correcting the previous tracker’s Italian-only tag. This BSc is distinct from the two-year Architecture MSc.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language_requirements"], "Official course profile"),
    source("SRC-POLIMI-CIVIL-MSC-2026", "Ingegneria Civile – Civil Engineering MSc profile", "https://www.polimi.it/formazione/corsi-di-laurea/dettaglio-corso/ingegneria-civile-civil-engineering", "2026-2027",
           "Identifies a two-year LM-23 MSc at Milano Leonardo taught in Italian or English depending on the study plan: Geotechnics and Structures use English, while the other plans are mainly in Italian. Programme-specific admission is based on the previous academic curriculum and annual rules.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course profile"),
]


PROGRAMS = {
    "legacy-001": {"name": "Computer Science and Engineering", "profile": "SRC-POLIMI-CSE-2026", "level": "MSc", "language": "English", "field": "Computer Science and Engineering", "campus": "Milano Leonardo", "duration": 2, "ects": 120, "requirements": "Comparable first-cycle degree; academic preparation is assessed against the MSc's programme criteria.", "class": "LM-32"},
    "legacy-002": {"name": "Cyber Risk Strategy and Governance", "profile": "SRC-POLIMI-CYBER-2025", "level": "MSc", "language": "English", "field": "Cybersecurity and Governance", "campus": "Milano Leonardo partner campus; Bocconi University co-delivery", "duration": 2, "requirements": "No fixed criteria in the 2025/26 page; competitive joint-committee assessment of transcript, curriculum and motivation letter.", "uncertain_cycle": True},
    "legacy-003": {"name": "Artificial Intelligence (study plan within Computer Science and Engineering)", "profile": "SRC-POLIMI-CSE-2026", "level": "MSc candidate / study plan", "language": "English within Computer Science and Engineering", "field": "Artificial Intelligence", "campus": "Milano Leonardo", "duration": 2, "ects": 120, "requirements": "No separate degree admission identified; the official profile lists Artificial Intelligence as a study plan within Computer Science and Engineering.", "identity_note": "No standalone MSc named Artificial Intelligence appears in the reviewed official catalogue; the documented match is a study plan of the Computer Science and Engineering MSc."},
    "legacy-004": {"name": "High Performance Computing Engineering", "profile": "SRC-POLIMI-HPC-2026", "level": "MSc", "language": "English", "field": "Computer Science and Engineering", "campus": "Milano Leonardo", "duration": 2, "ects": 120, "requirements": "Relevant first-cycle degree; the profile specifies at least 20 ECTS in computing, 20 ECTS in mathematics/statistics and 10 ECTS in physics; committee may assign additional requirements."},
    "legacy-005": {"name": "Biomedical Engineering", "profile": "SRC-POLIMI-BIOMED-MSC-2026", "level": "MSc", "language": "Italian or English", "field": "Biomedical Engineering", "campus": "Milano Leonardo", "duration": 2, "ects": 120, "requirements": "Equivalent Bachelor’s qualification with relevant engineering preparation; eligibility is assessed under annual programme rules.", "class": "LM-21"},
    "legacy-006": {"name": "Mechanical Engineering", "profile": "SRC-POLIMI-MECH-2025", "level": "MSc", "language": "English", "field": "Mechanical Engineering", "campus": "Lecco, Piacenza and Milano Bovisa", "duration": 2, "ects": 120, "requirements": "Course profile is explicitly for 2025/26; recheck the applicable annual regulations for admissions requirements."},
    "legacy-007": {"name": "Aerospace Engineering", "profile": "SRC-POLIMI-AERONAUTICAL-2026", "level": "MSc lead unresolved", "language": "Unresolved", "field": "Aerospace Engineering", "campus": "Unresolved", "duration": None, "requirements": "No exact current MSc title was found. The official catalogue lists Aeronautical Engineering and Space Engineering as distinct English MSc degrees, and Aerospace Engineering as a separate Italian BSc.", "identity_note": "Do not map the generic tracker MSc name onto Aeronautical Engineering, Space Engineering or the separate Aerospace Engineering BSc without evidence."},
    "legacy-008": {"name": "Design & Engineering", "profile": "SRC-POLIMI-DESIGNENG-2025", "level": "MSc", "language": "English", "field": "Design Engineering", "campus": "Milano Bovisa", "duration": 2, "ects": 120, "requirements": "The prior-cycle page expects a suitable first-cycle degree in design, architecture or engineering; programme-board assessment and a merit ranking apply."},
    "legacy-009": {"name": "Architecture", "profile": "SRC-POLIMI-ARCH-MSC-2026", "level": "MSc", "language": "Italian or English", "field": "Architecture", "campus": "Milano Leonardo", "duration": 2, "ects": 120, "requirements": "Bachelor’s degree in Architecture and portfolio; language depends on selected study plan."},
    "legacy-010": {"name": "Communication Design", "profile": "SRC-POLIMI-COMM-DESIGN-2026", "level": "MSc", "language": "Italian or English", "field": "Communication Design", "campus": "Milano Bovisa", "duration": 2, "ects": 120, "requirements": "Comparable first-cycle design or related degree; programme-board evaluation, ranking and at least B2 English are described for the reviewed cycle."},
    "legacy-140": {"name": "Ingegneria Aerospaziale", "profile": "SRC-POLIMI-AERO-BSC-2026", "level": "BSc", "language": "Italian", "field": "Aerospace Engineering", "campus": "Milano Bovisa", "duration": 3, "ects": 180, "requirements": "Engineering BSc admission test and annual enrolment call; the 2027/28 test and course call were not yet complete in reviewed sources.", "class": "L-9"},
    "legacy-141": {"name": "Ingegneria Biomedica", "profile": "SRC-POLIMI-BIOMED-BSC-2026", "level": "BSc", "language": "Italian", "field": "Biomedical Engineering", "campus": "Milano Bovisa (first year in 2026/27); Milano Leonardo for later years", "duration": 3, "ects": 180, "requirements": "Engineering BSc admission process and annual call; course page lists 2026/27 campus sequencing.", "class": "L-8 / L-9"},
    "legacy-142": {"name": "Ingegneria Gestionale", "profile": "SRC-POLIMI-MGMT-BSC-2026", "level": "BSc", "language": "Italian", "field": "Management Engineering", "campus": "Cremona and Milano Bovisa", "duration": 3, "ects": 180, "requirements": "Engineering BSc admission test and annual call; campus-specific access and places are published in the relevant annual materials.", "class": "L-8 / L-9"},
    "legacy-143": {"name": "Ingegneria Informatica", "profile": "SRC-POLIMI-COMP-BSC-2026", "level": "BSc", "language": "Italian", "field": "Computer Engineering", "campus": "Milano Leonardo and Cremona", "duration": 3, "ects": 180, "requirements": "Engineering BSc admission test and annual call; distinct from the Computer Science and Engineering MSc.", "class": "L-8"},
    "legacy-144": {"name": "Design degli Interni", "profile": "SRC-POLIMI-INTERIOR-BSC-2026", "level": "BSc", "language": "Italian", "field": "Interior Design", "campus": "Milano Bovisa", "duration": 3, "ects": 180, "requirements": "Design BSc admission route; annual call and test rules must be rechecked for 2027/28.", "class": "L-4"},
    "legacy-145": {"name": "Progettazione dell'Architettura", "profile": "SRC-POLIMI-ARCH-BSC-2026", "level": "BSc", "language": "Italian or English", "field": "Architecture", "campus": "Milano Leonardo, Piacenza and Mantova", "duration": 3, "ects": 180, "requirements": "Annual architecture BSc admission call; course languages and available sections may vary by track/campus.", "class": "L-17"},
    "legacy-146": {"name": "Ingegneria Civile - Civil Engineering", "profile": "SRC-POLIMI-CIVIL-MSC-2026", "level": "MSc", "language": "Italian or English by study plan", "field": "Civil Engineering", "campus": "Milano Leonardo", "duration": 2, "ects": 120, "requirements": "Admission is assessed under the prior academic curriculum and annual rules; English is used in Geotechnics and Structures plans, while other plans are mainly Italian.", "class": "LM-23"},
}


BATCH = {
    "id": "polimi-program-catalogue-and-2027-28-intake-review",
    "status": "partial",
    "result": "Matched all 17 Politecnico di Milano legacy rows against its official 2026/27 course catalogue and individual programme profiles. Corrected Biomedical Engineering MSc, Architecture MSc, Communication Design MSc and Progettazione dell'Architettura BSc language scope; kept BSc and MSc Biomedical Engineering separate. The legacy Artificial Intelligence MSc is a study plan within Computer Science and Engineering, not a separate degree in the reviewed catalogue. The generic Aerospace Engineering MSc lead remains unresolved because Aeronautical Engineering, Space Engineering and the Aerospace Engineering BSc are separate official courses. Recorded prior-cycle course identity, duration, campus and available entry conditions. Existing 2027/28 university-level dates and scholarships do not prove the first-year availability of each named programme; all 17 individual 2027/28 intakes, fees and course-specific terms remain pending, and the Engineering deadline page's cycle/date discrepancy remains open.",
}

REPORT = "Politecnico di Milano's 2026/27 official catalogue lists the prior-cycle degree identities for the reviewed legacy candidates. Computer Science and Engineering is a two-year English MSc and its Artificial Intelligence option is a study plan, not a separate catalogue degree. High Performance Computing Engineering is a separate English MSc; its reviewed profile specifies 20 ECTS in computing, 20 in mathematics/statistics and 10 in physics. Biomedical Engineering is separately offered as a BSc in Italian and an MSc in Italian or English. Architecture and Communication Design MScs are listed in Italian or English, while the BSc Progettazione dell'Architettura is also listed in Italian or English. Mechanical Engineering and Design & Engineering profile pages explicitly refer to 2025/26 information and may change in later years. The generic Aerospace Engineering MSc lead was not matched to a standalone catalogue entry: official pages distinguish Aeronautical Engineering MSc, Space Engineering MSc and Aerospace Engineering BSc, so the record remains unresolved. All 17 candidate first-year offers are pending for 2027/28 because the published MSc calendar and scholarship call are university-level and do not name each programme intake; Engineering admissions pages state that the 2027/28 BSc call would follow, while the MSc Engineering deadlines contain a label/date inconsistency. The current tuition page still covers 2026/27; no 2027/28 tuition schedule or 2027/28 program-specific calls, places or admission criteria were confirmed in this batch."


def fact(value, status, sources=(), note=None):
    return {"value": value, "status": status, "source_ids": list(sources), "notes": note}


def apply(universities, programs, fact_builder):
    uni = next(u for u in universities if u["id"] == "politecnico-milano")
    uni.update(cycle_status="CONFIRMED", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    uni["coverage"]["program_level_review"] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    rows = {p["id"]: p for p in programs if p["university_id"] == "politecnico-milano"}
    for pid, record in PROGRAMS.items():
        p = rows[pid]
        profile = record["profile"]
        p["program"] = record["name"]
        p["last_checked"] = CHECKED
        source_ids = [profile, "SRC-POLIMI-MSC-LIST-2026"]
        if record["level"].startswith("BSc"):
            source_ids += ["SRC-POLIMI-ENGINEERING-CALL-2027", "SRC-POLIMI-BSC-2027"] if pid in {"legacy-140", "legacy-141", "legacy-142", "legacy-143"} else []
        else:
            source_ids += ["SRC-POLIMI-DEADLINES-2027", "SRC-POLIMI-ENGLISH-2027"]
        if pid in {"legacy-001", "legacy-002", "legacy-004", "legacy-005", "legacy-006", "legacy-007", "legacy-008", "legacy-009", "legacy-010"}:
            source_ids.append("SRC-POLIMI-SCHOLARSHIPS-2027")
        p["source_ids"] = list(dict.fromkeys(source_ids))
        for field, value in (("level", record["level"]), ("language", record["language"]), ("field", record["field"])):
            note = "This value describes the reviewed prior-cycle profile; the exact 2027/28 first-year programme listing and course terms remain unverified."
            if record.get("identity_note"):
                note = record["identity_note"] + " The programme identity and 2027/28 availability remain unresolved."
            p[field] = fact_builder(value, "REQUIRES_VERIFICATION", [profile], note)
        p["availability_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", [profile, "SRC-POLIMI-MSC-LIST-2026"],
             "The official course page/catalogue reviewed provides prior-cycle course identity, while the 2027/28 university-level call calendar does not name this programme's first-year offer. No discontinuation is confirmed." + (" " + record["identity_note"] if record.get("identity_note") else ""))
        p["previous_cycle_tags"] = {"level": record["level"], "language": record["language"], "field": record["field"],
             "cycle": "2026-2027" if profile != "SRC-POLIMI-CYBER-2025" and profile != "SRC-POLIMI-MECH-2025" and profile != "SRC-POLIMI-DESIGNENG-2025" else "2025-2026",
             "label": "Official prior-cycle profile/catalogue; not evidence of 2027/28 first-year availability"}
        if pid == "legacy-003":
            p["previous_tracker_tags"] = {"level": "MSc", "language": "English", "field": "Computer Science", "label": "Previous tracker described Artificial Intelligence as a separate MSc; official profile shows it as a Computer Science and Engineering study plan."}
        if pid == "legacy-007":
            p["previous_tracker_tags"] = {"level": "MSc", "language": "English", "field": "Engineering", "label": "Previous tracker generic Aerospace Engineering MSc name; exact official programme identity not established."}

        listing_status = "REQUIRES_VERIFICATION" if record.get("uncertain_cycle") or record.get("identity_note") else "CONFIRMED"
        p["facts"]["previous_cycle_course_listing"] = fact({
            "academic_year": "2025/26" if profile in {"SRC-POLIMI-CYBER-2025", "SRC-POLIMI-MECH-2025", "SRC-POLIMI-DESIGNENG-2025"} else "2026/27",
            "official_name": record["name"], "level": record["level"], "language": record["language"],
            "campus": record.get("campus"), "duration_years": record.get("duration"), "ects": record.get("ects"),
            "degree_class": record.get("class")}, listing_status, [profile, "SRC-POLIMI-MSC-LIST-2026"],
            record.get("identity_note") or "Prior-cycle course identity only; do not infer 2027/28 first-year availability.")
        p["facts"]["previous_cycle_course_identity"] = fact(record.get("identity_note", record["name"]),
            "REQUIRES_VERIFICATION" if record.get("identity_note") else "CONFIRMED", [profile, "SRC-POLIMI-MSC-LIST-2026"],
            record.get("identity_note") or "The official course identity matches this tracker candidate; this is prior-cycle evidence only.")
        p["facts"]["previous_cycle_program_requirements"] = fact(record["requirements"],
            "REQUIRES_VERIFICATION" if record.get("identity_note") or record.get("uncertain_cycle") else "CONFIRMED", [profile],
            "Prior-cycle admission context only; annual regulations, study-area route and applicant eligibility need review before treating as current." )
        p["facts"]["program_specific_requirements_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", [profile, "SRC-POLIMI-DEADLINES-2027"],
            "No 2027/28 programme-specific admission regulation or call for this candidate was identified in this batch.")
        if record["level"].startswith("MSc") or record["level"] == "MSc":
            if record.get("field") in {"Aerospace Engineering"} and record.get("identity_note"):
                p["facts"]["application_windows"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-DEADLINES-2027"], "The generic legacy programme identity has not been matched to a study area, so its 2027/28 MSc application window cannot be assigned.")
            elif record.get("field") == "Cybersecurity and Governance":
                p["facts"]["application_windows"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-DEADLINES-2027", profile], "This jointly delivered programme's applicable study area and 2027/28 call route were not established; do not assign the Engineering timetable based on its subject label alone.")
            elif record.get("field") in {"Architecture", "Communication Design", "Design Engineering"}:
                p["facts"]["application_windows"] = fact({"academic_year": "2027/28", "study_area": "Architecture and Design", "general_call": ["2026-10-01", "2027-01-28"], "additional_call": ["2027-03-01", "2027-03-18"], "additional_call_eligibility": "EEA and non-EEA residents in Italy holding one of the listed permits"}, "CONFIRMED", ["SRC-POLIMI-DEADLINES-2027"], "Shared study-area schedule; verify the chosen course and applicant eligibility in the official call.")
            else:
                p["facts"]["application_windows"] = fact(None, "CONFLICTING_SOURCES", ["SRC-POLIMI-DEADLINES-2027"], "The official 2027/28 general MSc schedule ends the second period on 28 January 2027, while the Engineering subsection is labelled 2026/27 but describes September 2027 intake and ends on 25 February. Await a course-level clarification.")
            p["facts"]["application_fee_2027_2028"] = fact({"early_bird_eur": 50, "standard_eur": 150, "maximum_programmes": 2}, "CONFIRMED", ["SRC-POLIMI-DEADLINES-2027"], "University MSc application fees; which deadline applies depends on study area and applicant group.")
        else:
            p["facts"]["application_windows"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-ENGINEERING-CALL-2027", "SRC-POLIMI-BSC-2027"], "The Engineering 2027/28 admission call was still marked as forthcoming; BSc program-specific admission windows and tests remain pending.")
            p["facts"]["application_fee_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-ENGINEERING-CALL-2027"], "The BSc Engineering admission call and program-specific fee were not published in the reviewed page.")
        p["facts"]["tuition_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-TUITION-2027"], "The reviewed fee page publishes 2026/27 amounts only; no 2027/28 course tuition is confirmed.")
        p["facts"]["scholarships_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-SCHOLARSHIPS-2027"],
            "A university-level merit scholarship call exists for first-year English-taught MSc applicants, but this candidate's 2027/28 intake and exact course/tier eligibility are not confirmed." if record["level"].startswith("MSc") or record["level"] == "MSc" else "The reviewed 2027/28 merit call is limited to specified English-taught programmes; this prior-cycle Italian-language BSc does not match that stated scope.")
        p["facts"]["acceptance_rate"] = fact(None, "UNAVAILABLE", [profile, "SRC-POLIMI-MSC-LIST-2026"], "No official comparable applicant and admitted-student totals were found for this candidate; no acceptance rate is inferred.")

    uni["cycle_facts"]["program_inventory_2026_2027"] = fact(
        {"legacy_program_rows_reviewed": len(PROGRAMS), "matches": 16, "identity_unresolved": ["legacy-007"],
         "catalogue_note": "Catalogue profile evidence is prior-cycle; it does not confirm individual 2027/28 first-year availability."},
        "CONFIRMED", ["SRC-POLIMI-MSC-LIST-2026"] + [v["profile"] for v in PROGRAMS.values()],
        "Candidate matching completed for all 17 original rows; one generic MSc identity remains unresolved.")
    uni["cycle_facts"]["tuition_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-POLIMI-TUITION-2027"],
        "The official tuition page currently displays academic year 2026/27; no 2027/28 amounts are copied forward.")
