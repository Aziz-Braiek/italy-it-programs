"""UniTrento legacy program review, checked 10 November 2026."""

CHECKED = "2026-11-10"
ENGLISH_ADMISSIONS = "https://www.unitn.it/en/admission-courses-taught-english"
GENERAL_ADMISSIONS = "https://www.unitn.it/en/international/coming-unitrento/admission-how-it-works"


def source(sid, title, url, cycle, evidence, supports, kind="Official course or admissions source"):
    return {"id": sid, "university_id": "trento", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


PROGRAMS = {
    "legacy-045": {
        "name": "Computer Science", "profile": "SRC-UNITN-CS-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/computer-science-master", "level": "MSc", "language": "English",
        "field": "Computer Science", "class": "LM-18", "duration": 2, "ects": 120,
        "campus": "Trento", "access": "Free access for European/equivalent applicants subject to requirements; non-EU applicants abroad use a limited-place annual call",
        "requirements": "For 2026/27, L-8 or L-31 graduates met the curricular requirements. Other candidates needed at least 30 CFU in mathematics, physics or statistics and at least 45 CFU in computer science or information technology engineering sectors, plus English B2 and suitable preparation.",
        "call_sources": ["SRC-UNITN-DISI-CALL-2026"],
        "selection": {"nonEU_abroad_positions": 60, "eit_reserved_within_positions": 20,
                      "selection": "Assessment of curricular requirements, academic preparation and ranking; interview possible"},
        "windows": {"nonEU_abroad_deadline": "2026-03-04 12:00 CET",
                    "European_equivalent_request": {"opening": "2026-05-18", "closing": "2026-11-12"}},
        "fee_eur": 30, "fee_scope": "2026/27 non-EU abroad call per application",
        "finance": "disi",
    },
    "legacy-046": {
        "name": "Artificial Intelligence Systems", "profile": "SRC-UNITN-AIS-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/artificial-intelligence-systems", "level": "MSc", "language": "English",
        "field": "Artificial Intelligence and Computer Systems", "class": "LM-32", "duration": 2, "ects": 120,
        "campus": "Trento", "access": "Free access for European/equivalent applicants subject to requirements; non-EU applicants abroad use a limited-place annual call",
        "requirements": "For 2026/27, L-8, L-9 or L-31 graduates met curricular requirements. Other candidates needed at least 36 CFU across listed chemistry, physics, mathematics and statistics sectors and at least 12 CFU in INF/01 or ING-INF/05, plus English B2 and suitable preparation.",
        "call_sources": ["SRC-UNITN-DISI-CALL-2026"],
        "selection": {"nonEU_abroad_positions": 60, "eit_reserved_within_positions": 20,
                      "selection": "Assessment of curricular requirements, academic preparation and ranking; interview possible"},
        "windows": {"nonEU_abroad_deadline": "2026-03-04 12:00 CET",
                    "European_equivalent_request": {"opening": "2026-05-18", "closing": "2026-11-12"}},
        "fee_eur": 30, "fee_scope": "2026/27 non-EU abroad call per application",
        "finance": "disi",
    },
    "legacy-047": {
        "name": "Data Science", "profile": "SRC-UNITN-DS-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/data-science", "level": "MSc", "language": "English",
        "field": "Data Science and Statistics", "class": "LM-DATA", "duration": 2, "ects": 120,
        "campus": "Sociology Building, Trento", "access": "Programmed access",
        "requirements": "For 2026/27, applicants needed a suitable first-cycle degree and curricular preparation across computer science/information engineering, social sciences/economics/psychology/law, mathematics/statistics and related sectors. The call specified minimum credits in each listed group and assessment of fundamental computer science, probability and statistics; an interview could be required. English was required for the programme.",
        "call_sources": ["SRC-UNITN-DS-CALL-2026"],
        "selection": {"total_positions": 56, "nonEU_abroad_positions": 8,
                      "first_call_places": {"European_and_equivalent": 20, "nonEU_abroad": 8},
                      "second_call_places": {"European_and_equivalent": 28},
                      "selection": "Curricular and academic evaluation with ranking; interview may be requested"},
        "windows": {"first_call": {"opening": "2025-12-17", "closing": "2026-03-04 12:00 CET"},
                    "second_call": {"opening": "2026-04-01", "closing": "2026-05-29 12:00 CET"}},
        "fee_eur": 30, "fee_scope": "2026/27 application; each submitted application",
        "finance": "data_science",
    },
    "legacy-048": {
        "name": "Human-Computer Interaction", "profile": "SRC-UNITN-HCI-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/human-computer-interaction", "level": "MSc", "language": "English",
        "field": "Human-Computer Interaction and Cognitive Science", "class": "LM-55 R", "duration": 2, "ects": 120,
        "campus": "Rovereto", "access": "Programmed access",
        "requirements": "The 2026/27 call required a suitable first-cycle qualification, at least 50 CFU in the listed humanistic, linguistic, psychological, computing, engineering, education, history, law, economics, social, biological, physical or mathematical areas, and English-language evidence. Selection was based on qualifications and could include an interview.",
        "call_sources": ["SRC-UNITN-HCI-CALL-2026"],
        "selection": {"total_positions": 35, "nonEU_abroad_positions": 20, "European_and_equivalent_positions": 15,
                      "selection": "Two selections based on qualifications and, if required, interview"},
        "windows": {"European_equivalent_call": {"opening": "2026-02-09", "closing": "2026-05-29 12:00 CET"},
                    "nonEU_abroad_call": "Annual call; 2026/27 call linked from the official profile"},
        "fee_eur": 30, "fee_scope": "2026/27 application fee shown for the Master's selection",
        "finance": "hci",
    },
    "legacy-049": {
        "name": "Cognitive Science", "profile": "SRC-UNITN-COGSCI-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/cognitive-science", "level": "MSc", "language": "English",
        "field": "Cognitive Science, Neuroscience and Computational Linguistics", "class": "LM-55", "duration": 2, "ects": 120,
        "campus": "Rovereto", "access": "Programmed access",
        "requirements": "For 2026/27, the call required an eligible first-cycle qualification, a relevant academic background spanning cognitive-science disciplines and English proficiency. Selection scored academic background, relevance of prior study and experience, and the statement of purpose; an interview could be requested.",
        "call_sources": ["SRC-UNITN-COGSCI-CALL-2026"],
        "selection": {"total_positions": 80, "nonEU_abroad_positions": 35,
                      "priority_reserve": "Six places per each of three curricula for non-EU abroad applicants and six per curriculum for European/equivalent applicants",
                      "selection": "Qualifications-based ranking; interview if the committee needs additional information"},
        "windows": {"nonEU_abroad_call": {"opening": "2025-12-17", "closing": "2026-03-04 12:00 CET"},
                    "European_equivalent_call": {"opening": "2026-02-09", "closing": "2026-05-29 12:00 CET"}},
        "fee_eur": 30, "fee_scope": "2026/27 application fee",
        "finance": "cognitive_science",
    },
    "legacy-050": {
        "name": "International Security Studies", "profile": "SRC-UNITN-ISS-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/international-security-studies", "level": "MSc", "language": "English",
        "field": "International Relations and Security Studies", "class": "LM-52 R", "duration": 2, "ects": 120,
        "campus": "Trento (first year) and Pisa at Scuola Superiore Sant’Anna (second year)",
        "access": "Joint degree with programmed selection",
        "requirements": "For 2026/27 non-EU applicants abroad, the call required at least 60 equivalent credits across at least two of history/philosophy, economics, law, political science, sociology or foreign languages; relevant academic/vocational background; minimum 24/30 or equivalent 75%; English B2; and basic knowledge of a second listed language.",
        "call_sources": ["SRC-UNITN-ISS-CALL-2026"],
        "selection": {"nonEU_abroad_positions": 5, "selection": "Committee evaluation and ranking based on requirements and call criteria"},
        "windows": {"nonEU_abroad_deadline": "2026-03-04 12:00 CET", "results_by": "2026-04-30"},
        "fee_eur": 30, "fee_scope": "2026/27 non-EU abroad application fee",
        "finance": "iss",
        "identity_note": "This row matches the joint International Security Studies (MISS) course with Scuola Superiore Sant’Anna. Security, Intelligence and Strategic Studies (IMSISS) is a separate Erasmus Mundus programme and is not substituted for this row.",
    },
    "legacy-051": {
        "name": "Comparative, European and International Legal Studies",
        "profile": "SRC-UNITN-CEILS-PROFILE-2026",
        "url": "https://corsi.unitn.it/en/comparative-european-and-international-legal-studies", "level": "BSc", "language": "English",
        "field": "Comparative, European and International Law", "class": "L-14 R", "duration": 3, "ects": 180,
        "campus": "Faculty of Law, Trento", "access": "Programmed access by admission test and ranking",
        "requirements": "For 2026/27, candidates needed an eligible secondary-school diploma, English B2 and a passing result in the University of Trento admission test. International applicants had a dedicated non-EU session and qualification-document verification.",
        "call_sources": ["SRC-UNITN-CEILS-CALL-2026"],
        "selection": {"first_session_places": {"European_and_equivalent": 50, "nonEU": 10, "total": 60},
                      "second_session_places": {"European_and_equivalent": 25, "nonEU": 0, "total": 25},
                      "selection": "Admission test and ranking; non-EU applicants could use only the first session"},
        "windows": {"first_session_application_deadline": "2026-03-06", "second_session_EU_only": {"opening": "2026-04-09", "closing": "2026-05-04"},
                    "admission_test_dates": ["2026-03-23 (online)", "2026-05-14 (in person)"],
                    "scope_note": "All dates and places are the 2026/27 call only."},
        "fee_eur": 35, "fee_scope": "2026/27 application/test registration fee",
        "finance": "bachelor",
    },
}


SOURCES = [
    source("SRC-UNITN-CS-PROFILE-2026", "Computer Science Master's degree", PROGRAMS["legacy-045"]["url"], "2026-2027",
           "Identifies a two-year/120-ECTS English MSc in class LM-18, based in Trento; European/equivalent applicants had a 2026/27 admission request through 12 November 2026. The 2027/28 new-first-year offer is not established by this profile.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-AIS-PROFILE-2026", "Artificial Intelligence Systems Master's degree", PROGRAMS["legacy-046"]["url"], "2026-2027",
           "Identifies an English-taught two-year/120-ECTS MSc in class LM-32 in Trento, with free access for European/equivalent applicants subject to requirements; its published European request window is for 2026/27.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-DS-PROFILE-2026", "Data Science Master's degree", PROGRAMS["legacy-047"]["url"], "2026-2027",
           "Identifies the English-taught two-year/120-ECTS programmed MSc in class LM-DATA, located at the Sociology Building in Trento. The official course call for 2026/27 sets 56 places, including eight for non-EU applicants abroad.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-HCI-PROFILE-2026", "Human-Computer Interaction Master's degree", PROGRAMS["legacy-048"]["url"], "2026-2027",
           "Identifies the English-taught two-year/120-ECTS programmed Master's in Rovereto; the official 2026/27 call identifies class LM-55 R, 35 total places and 20 places reserved for non-EU applicants abroad.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-COGSCI-PROFILE-2026", "Cognitive Science Master's degree", PROGRAMS["legacy-049"]["url"], "2026-2027",
           "Identifies the English-taught two-year/120-ECTS programmed Master's in class LM-55 at Palazzo Fedrigotti in Rovereto, with three study tracks; the annual call is for 2026/27.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-ISS-PROFILE-2026", "International Security Studies Master's degree", PROGRAMS["legacy-050"]["url"], "2026-2027",
           "Identifies the English-taught two-year/120-ECTS programmed joint LM-52 R Master's awarded by UniTrento and Scuola Superiore Sant’Anna; first year in Trento and second year in Pisa. A distinct Erasmus Mundus programme, Security, Intelligence and Strategic Studies, is not the same course.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-CEILS-PROFILE-2026", "Comparative, European and International Legal Studies Bachelor's degree", PROGRAMS["legacy-051"]["url"], "2026-2027",
           "Identifies the entirely English-taught three-year/180-ECTS Bachelor's in class L-14 R at the Faculty of Law in Trento; 2026/27 access is programmed and requires an admission test.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_course_identity"], "Official degree profile"),
    source("SRC-UNITN-DISI-CALL-2026", "DISI Master's admission call for non-European citizens abroad, AY 2026–2027", "https://corsi.unitn.it/sites/cds/files/2025-12/admission-call-master-disi-26-27.pdf", "2026-2027",
           "The 2026/27 call covers English-taught DISI Master's degrees and sets the non-EU abroad deadline at 4 March 2026, 12:00 CET, €30 per application, academic evaluation and ranking, possible interview, Universitaly pre-enrolment, and course-specific seat/credit rules. It lists 60 call positions each for Computer Science and Artificial Intelligence Systems, with 20 EIT-selected places within each. Tuition for non-EU students is score-based up to €10,000 per year; first-year bands are waiver at 90+, €1,000 at 70–89.99, €3,000 at 60–69.99 and €6,500 at 50–59.99. Top candidates scoring at least 70 may receive competitive tuition-exempting scholarships; counts are announced with rankings. These terms are historical only.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_tuition", "program.previous_cycle_scholarships"], "Official Rector's admission call PDF"),
    source("SRC-UNITN-DS-CALL-2026", "Data Science Master's admission call AY 2026–2027", "https://corsi.unitn.it/sites/cds/files/2025-12/bando-ammissione-lm-data-science-26-27.pdf", "2026-2027",
           "The call sets 56 seats total including eight reserved to non-EU applicants abroad; first-call allocation was 20 European/equivalent and eight non-EU, followed by 28 European/equivalent places. Applications ran 17 December 2025–4 March 2026 and 1 April–29 May 2026, with €30 fee. Non-EU tuition capped at €6,000/year, reduced by admission score; top non-EU candidates scoring at least 90 may receive a competitive scholarship. Curricular prerequisites, committee evaluation and optional interview are specified. Historical only.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_places", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_tuition", "program.previous_cycle_scholarships"], "Official Rector's admission call PDF"),
    source("SRC-UNITN-HCI-CALL-2026", "Human-Computer Interaction Master's admission call AY 2026–2027", "https://corsi.unitn.it/sites/cds/files/2025-12/bando-ammissione-lm-human-computer-interaction-non-eu-26-27.pdf", "2026-2027",
           "The 2026/27 call identifies class LM-55, 35 places including 20 reserved for non-EU candidates abroad, 50 relevant CFU, English instruction and selection based on qualifications with a possible interview. Non-EU tuition is capped at €10,000/year and reduced by score; top candidates scoring at least 90 may receive a competitive tuition-exempting award. The European/equivalent application page showed 9 February–29 May 2026 and €30 fee. Prior-cycle only.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_places", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_tuition", "program.previous_cycle_scholarships"], "Official Rector's admission call PDF"),
    source("SRC-UNITN-COGSCI-CALL-2026", "Cognitive Science Master's admission call AY 2026–2027", "https://corsi.unitn.it/sites/cds/files/2025-12/admission-call-master-cognitive-science-26-27.pdf", "2026-2027",
           "The call limits 2026/27 entry to 80 places, including 35 reserved to non-EU applicants abroad; priority reserves are six places per each of three tracks for each applicant category. The non-EU application period ran 17 December 2025–4 March 2026; the European/equivalent period ran 9 February–29 May 2026; fee €30. Selection evaluates academic background, relevance and statement of purpose, with interview possible. Non-EU fee cap €6,000/year, score-based reductions and competitive scholarships for top applicants scoring at least 70. Prior-cycle only.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_places", "program.previous_cycle_selection", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_tuition", "program.previous_cycle_scholarships"], "Official Rector's admission call PDF"),
    source("SRC-UNITN-ISS-CALL-2026", "International Security Studies non-European admission call AY 2026–2027", "https://corsi.unitn.it/sites/cds/files/2025-12/bando-ammissione-lm-miss-non-eu-26-27.pdf", "2026-2027",
           "The 2026/27 non-EU abroad call reserves five places; application deadline 4 March 2026, fee €30, results by 30 April and confirmation fee €100. It requires 60 equivalent credits across at least two listed subject areas, relevant background, minimum GPA 24/30 or 75%, English B2 and a second language. Non-EU tuition capped at €10,000/year and score-based; top candidates scoring at least 90 may receive a competitive tuition-exempting scholarship. Prior-cycle only.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_places", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_tuition", "program.previous_cycle_scholarships"], "Official Rector's admission call PDF"),
    source("SRC-UNITN-CEILS-CALL-2026", "Comparative, European and International Legal Studies admission information AY 2026–2027", "https://corsi.unitn.it/en/comparative-european-and-international-legal-studies/enrollment/admission-and-enrollment", "2026-2027",
           "The 2026/27 page publishes two tests (23 March online and 14 May in person), a €35 application fee, and links the annual call and rankings. The linked call sets 60 seats in session one (50 European/equivalent, 10 non-EU) and 25 in session two for European/equivalent candidates only; selection requires an eligible diploma, English B2 and passing the University test. Dates and places are prior-cycle only.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_places", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee"], "Official Bachelor's admission page and call"),
    source("SRC-UNITN-EN-ADMISSIONS", "Admission to courses taught in English", ENGLISH_ADMISSIONS, "general",
           "Official guidance says non-EU candidates abroad must follow the annual call for the selected course, submit online, upload required documents and complete Universitaly pre-enrolment after admission. Calls are program-specific; the page does not give named 2027/28 first-year calls for the reviewed legacy courses.",
           ["university.international_admissions", "university.non_eu_process", "program.application_route"], "Official international admissions guidance"),
    source("SRC-UNITN-GENERAL-ADMISSIONS", "Admission: how it works", GENERAL_ADMISSIONS, "general",
           "General guidance describes program-specific non-EU selection calls, ranked allocation of reserved places, score-based tuition brackets for English Master's programs and competitive score-based scholarship/accommodation processes. It does not confirm 2027/28 course calls for the seven reviewed legacy rows.",
           ["university.non_eu_process", "university.fees_general", "university.scholarships_general"], "Official international admissions guidance"),
    source("SRC-UNITN-FEES-NEU-2026", "Tuition fees for non-EU citizens", "https://www.unitn.it/en/study/fees-scholarships-accommodation/tuition-fees/non-eu-citizens", "2026-2027",
           "UniTrento explains that fees for non-EU citizens residing outside Italy are based on admission merit and the score obtained in the admission test; programme-specific annual regulations define the brackets and awards. This is general context, not one fixed 2027/28 amount.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition"], "Official tuition guidance"),
]


def fact(value, status, sources=(), note=None):
    return {"value": value, "status": status, "source_ids": list(sources), "notes": note}


def _finance(record):
    if record["finance"] == "disi":
        return ({"academic_year": "2026/27", "nonEU_abroad_max_per_year_eur": 10000,
                 "first_year_score_bands": [{"score": "90–100", "fee_eur": 0}, {"score": "70–89.99", "fee_eur": 1000},
                                            {"score": "60–69.99", "fee_eur": 3000}, {"score": "50–59.99", "fee_eur": 6500}],
                 "second_year_merit_reduction": "Full waiver at 42+ CFU by 10 August; lower credit bands have partial reductions and under 6 CFU costs the €10,000 maximum"},
                {"academic_year": "2026/27", "nonEU_abroad": "Top-ranked candidates scoring at least 70/100 may receive a competitive award; numbers are announced with rankings, award provides tuition exemption and partial mobility-expense support"})
    if record["finance"] == "data_science":
        return ({"academic_year": "2026/27", "nonEU_abroad_max_per_year_eur": 6000,
                 "first_year_score_bands": [{"score": "90–100", "fee_eur": 0}, {"score": "70–89.9", "fee_eur": 1000},
                                            {"score": "60–69.9", "fee_eur": 2000}, {"score": "50–59.9", "fee_eur": 4500}],
                 "second_year": "Fee reduction depends on credits achieved; 42 or more CFU by 10 August gives full exemption"},
                {"academic_year": "2026/27", "nonEU_abroad": "Top-ranked candidates scoring at least 90/100 may receive a competitive scholarship; number announced with rankings; mobility-expense contribution, paid after arrival"})
    if record["finance"] == "hci":
        return ({"academic_year": "2026/27", "nonEU_abroad_max_per_year_eur": 10000,
                 "first_year_score_bands": [{"score": "90–100", "fee_eur": 0}, {"score": "70–89.9", "fee_eur": 1000},
                                            {"score": "60–69.9", "fee_eur": 3000}, {"score": "50–59.9", "fee_eur": 6500}],
                 "second_year": "Full exemption at 42 or more CFU by 10 August; fee otherwise depends on credits"},
                {"academic_year": "2026/27", "nonEU_abroad": "Top-ranked candidates scoring at least 90/100 may receive a competitive tuition-exempting scholarship; award count announced with ranking"})
    if record["finance"] == "cognitive_science":
        return ({"academic_year": "2026/27", "nonEU_abroad_max_per_year_eur": 6000,
                 "first_year_score_bands": [{"score": "90–100", "fee_eur": 0}, {"score": "70–89.9", "fee_eur": 1000},
                                            {"score": "60–69.9", "fee_eur": 2000}, {"score": "50–59.9", "fee_eur": 4500}],
                 "second_year": "Full exemption at 42 or more CFU by 10 August; fee otherwise depends on credits"},
                {"academic_year": "2026/27", "nonEU_abroad": "Top-ranked candidates scoring at least 70/100 may receive a competitive tuition-exempting scholarship; award count announced with ranking"})
    if record["finance"] == "iss":
        return ({"academic_year": "2026/27", "nonEU_abroad_max_per_year_eur": 10000,
                 "first_year_score_bands": [{"score": "90–100", "fee_eur": 0}, {"score": "70–89.9", "fee_eur": 1000},
                                            {"score": "60–69.9", "fee_eur": 3000}, {"score": "50–59.9", "fee_eur": 6500}],
                 "second_year": "Full exemption at 42 or more CFU by 10 August; fee otherwise depends on credits"},
                {"academic_year": "2026/27", "nonEU_abroad": "Top-ranked candidates scoring at least 90/100 may receive a competitive tuition-exempting scholarship; award count announced with ranking"})
    return ({"academic_year": "2026/27", "European_equivalent": "Tuition is based on ISEE; Opera Universitaria publishes regional aid and housing calls.",
             "nonEU_abroad": "Admission-test score sets the tuition bracket under the annual non-EU regulation; exact course-year terms must be checked in that call."},
            {"academic_year": "2026/27", "regional_aid": "Opera Universitaria publishes annual scholarship and discounted-housing calls; eligibility and award amounts are competitive and call-specific."})


def apply(universities, programs, fact_builder):
    uni = next(u for u in universities if u["id"] == "trento")
    uni.update(
        research_stage="PARTIALLY_RESEARCHED",
        research_summary=REPORT,
        last_checked=CHECKED,
        contact_email="internationaladmissions@unitn.it",
        contact_url=GENERAL_ADMISSIONS,
    )
    uni["coverage"].update({
        "bachelors_admissions_examined": "partial",
        "masters_admissions_examined": "partial",
        "english_programs_examined": "partial",
        "fees_examined": "partial",
        "scholarships_examined": "partial",
        "non_eu_requirements_examined": "partial",
        "application_deadlines_examined": "partial",
        "program_level_review": "partial",
    })
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])
    if "SRC-UNITN-INTL" not in uni["source_ids"]:
        uni["source_ids"].append("SRC-UNITN-INTL")

    rows = {p["id"]: p for p in programs if p["university_id"] == "trento"}
    for pid, record in PROGRAMS.items():
        p = rows[pid]
        p["program"] = record["name"]
        p["last_checked"] = CHECKED
        p["overall_status"] = "REQUIRES_VERIFICATION"
        p["discovery_source"] = "previous_tracker"
        profile = record["profile"]
        source_ids = [profile, "SRC-UNITN-EN-ADMISSIONS", "SRC-UNITN-GENERAL-ADMISSIONS", "SRC-UNITN-FEES-NEU-2026"] + record["call_sources"]
        p["source_ids"] = list(dict.fromkeys(source_ids))
        p["level"] = fact_builder(record["level"], "REQUIRES_VERIFICATION", [profile],
            "Official course level shown in the 2026/27 profile; a 2027/28 new-first-year offer remains unconfirmed.")
        p["language"] = fact_builder(record["language"], "REQUIRES_VERIFICATION", [profile],
            "Official course language shown in the latest profile/call reviewed; verify the 2027/28 first-year offer.")
        p["field"] = fact_builder(record["field"], "REQUIRES_VERIFICATION", [profile],
            "Subject classification follows the official profile and 2026/27 call; it is not a 2027/28 offer confirmation.")
        p["availability_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            [profile] + record["call_sources"] + ["SRC-UNITN-EN-ADMISSIONS"],
            "The official course profiles and named admission calls reviewed are for 2026/27. No 2027/28 first-year call for this legacy programme was confirmed. No discontinuation is inferred.")
        p["previous_cycle_tags"] = {"level": record["level"], "language": record["language"],
            "field": record["field"], "cycle": "2026-2027",
            "label": "Official 2026/27 course profile and admissions call only; new 2027/28 first-year availability remains unverified"}
        p["facts"]["previous_cycle_course_identity"] = fact_builder(record["name"], "CONFIRMED", [profile],
            record.get("identity_note") or "Matches the official UniTrento programme title in the latest reviewed profile.")
        p["facts"]["previous_cycle_course_listing"] = fact_builder({
            "academic_year": "2026/27", "official_name": record["name"], "level": record["level"],
            "language": record["language"], "degree_class": record["class"], "duration_years": record["duration"],
            "ects": record["ects"], "campus": record["campus"], "access": record["access"]},
            "CONFIRMED", [profile] + record["call_sources"],
            "Official 2026/27 profile and call data only; listed duration, language and access terms are not rolled forward.")
        p["facts"]["previous_cycle_program_requirements"] = fact_builder(record["requirements"], "CONFIRMED",
            record["call_sources"], "Prior-cycle programme-specific entry requirements only; consult the new annual call before applying.")
        p["facts"]["program_specific_requirements_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            record["call_sources"] + ["SRC-UNITN-EN-ADMISSIONS"],
            "No 2027/28 course-specific admission call or requirements were confirmed in the reviewed official sources.")
        p["facts"]["previous_cycle_selection"] = fact_builder(record["selection"], "CONFIRMED",
            record["call_sources"], "Seat counts, applicant categories and selection rules are from 2026/27 only and may change.")
        p["facts"]["previous_cycle_application_windows"] = fact_builder({"academic_year": "2026/27", **record["windows"]},
            "CONFIRMED", record["call_sources"] + [profile], "These are 2026/27 dates only and must not be rolled forward.")
        p["facts"]["previous_cycle_application_fee"] = fact_builder({"academic_year": "2026/27", "fee_eur": record["fee_eur"],
            "scope": record["fee_scope"]}, "CONFIRMED", record["call_sources"],
            "Historical application fee only; later calls can change the amount or scope.")
        p["facts"]["application_fee_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            record["call_sources"], "The latest published application fee located is for 2026/27; no 2027/28 amount was confirmed.")
        p["facts"]["application_windows"] = fact_builder(None, "REQUIRES_VERIFICATION",
            record["call_sources"] + ["SRC-UNITN-EN-ADMISSIONS"],
            "No named 2027/28 first-year admission window was confirmed for this course. The University describes annual, programme-specific calls.")
        tuition, scholarship = _finance(record)
        p["facts"]["previous_cycle_tuition"] = fact_builder(tuition, "CONFIRMED",
            record["call_sources"] + (["SRC-UNITN-FEES-NEU-2026"] if record["finance"] == "bachelor" else []),
            "2026/27 framework only. International and domestic fee routes differ, and annual calls set the applicable amount and conditions.")
        p["facts"]["tuition_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            record["call_sources"] + ["SRC-UNITN-FEES-NEU-2026"],
            "The reviewed fee brackets are from 2026/27 or general guidance; no 2027/28 course call or schedule was confirmed.")
        p["facts"]["previous_cycle_scholarships"] = fact_builder(scholarship, "CONFIRMED",
            record["call_sources"] + (["SRC-UNITN-GENERAL-ADMISSIONS"] if record["finance"] == "bachelor" else []),
            "Competitive prior-cycle awards; the number is call-specific and not guaranteed. Domestic/regional support uses a separate annual Opera Universitaria call.")
        p["facts"]["scholarships_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            record["call_sources"] + ["SRC-UNITN-GENERAL-ADMISSIONS"],
            "No 2027/28 incoming-student award call or amount was confirmed for this course.")
        p["facts"]["acceptance_rate"] = fact_builder(None, "UNAVAILABLE", record["call_sources"],
            "Official places and ranking procedures exist for 2026/27, but no complete applicant denominator and admitted count was found; no acceptance rate is inferred.")
        if record.get("identity_note"):
            p["facts"]["course_identity_note"] = fact_builder(record["identity_note"], "CONFIRMED", [profile],
                "The distinction is recorded so the prior tracker row is not conflated with a separate UniTrento programme.")

    uni["cycle_facts"].update({
        "legacy_english_program_inventory_2026_2027": fact_builder({
            "reviewed_legacy_candidates": len(PROGRAMS),
            "bachelors": [PROGRAMS["legacy-051"]["name"]],
            "masters": [PROGRAMS[x]["name"] for x in ("legacy-045", "legacy-046", "legacy-047", "legacy-048", "legacy-049", "legacy-050")],
            "note": "These seven prior-tracker programmes are distinct from the seven separately tracked 28DIGITAL master tracks."},
            "CONFIRMED", [p["profile"] for p in PROGRAMS.values()] + ["SRC-UNITN-DISI-CALL-2026", "SRC-UNITN-DS-CALL-2026", "SRC-UNITN-HCI-CALL-2026", "SRC-UNITN-COGSCI-CALL-2026", "SRC-UNITN-ISS-CALL-2026", "SRC-UNITN-CEILS-CALL-2026"],
            "Official course profiles and 2026/27 calls matched against all seven legacy rows; this is not confirmation of a 2027/28 intake."),
        "nonEU_english_admissions_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITN-EN-ADMISSIONS", "SRC-UNITN-GENERAL-ADMISSIONS"],
            "UniTrento says non-EU English-program admissions are course-specific and handled through annual calls; no 2027/28 calls for these seven legacy rows were confirmed."),
        "bachelor_admissions_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITN-CEILS-CALL-2026"], "CEILS's latest located call and places are for 2026/27; no 2027/28 call was confirmed."),
        "master_admissions_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITN-EN-ADMISSIONS", "SRC-UNITN-DISI-CALL-2026", "SRC-UNITN-DS-CALL-2026", "SRC-UNITN-HCI-CALL-2026", "SRC-UNITN-COGSCI-CALL-2026", "SRC-UNITN-ISS-CALL-2026"],
            "The named course calls reviewed are for 2026/27. General guidance says calls are published annually by programme; no 2027/28 call for these candidates was confirmed."),
        "tuition_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITN-FEES-NEU-2026"], "Course-specific non-EU fee brackets located are for 2026/27; no 2027/28 fee regulation or new call was confirmed."),
        "scholarships_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITN-GENERAL-ADMISSIONS", "SRC-UNITN-FEES-NEU-2026"], "No new-entry 2027/28 course scholarship call or amount was confirmed; 28DIGITAL funding remains separately tracked."),
        "university_wide_acceptance_rate": fact_builder(None, "UNAVAILABLE", ["SRC-UNITN-GENERAL-ADMISSIONS"],
            "No official university-wide applicant denominator and admitted count was found; programme quotas are not acceptance rates."),
    })


BATCH = {
    "id": "unitrento-legacy-programme-and-admissions-review",
    "status": "partial",
    "result": "Reviewed all seven remaining UniTrento legacy programme rows against official course profiles and their 2026/27 admissions material. Confirmed prior-cycle identity, degree class, language, duration, study location, quotas where published, programme-specific entry criteria, application routes and fees. Corrected the CEILS row to the full official title and distinguished International Security Studies (MISS) from the separate Erasmus Mundus IMSISS course. Recorded 2026/27 non-EU fee brackets and competitive award rules without copying them into 2027/28. The seven 28DIGITAL tracks already confirmed in the dataset are preserved as distinct joint-master offers. No 2027/28 first-year intake, programme call, application fee, tuition schedule or new-entry scholarship was confirmed for these seven legacy rows; 2027/28 status remains pending.",
}

REPORT = "UniTrento's seven remaining legacy course rows now have official 2026/27 profile and call evidence: Computer Science (LM-18), Artificial Intelligence Systems (LM-32), Data Science (LM-DATA), Human-Computer Interaction (LM-55 R), Cognitive Science (LM-55), International Security Studies (LM-52 R joint with Sant’Anna), and the English-taught CEILS Bachelor's (L-14 R). The records include their prior-cycle durations, language, locations, entry requirements, reserved places, application routes and fees. The CEILS row now uses the complete official title; International Security Studies (MISS) remains separate from the Erasmus Mundus Security, Intelligence and Strategic Studies (IMSISS). 2026/27 non-EU fee and scholarship rules varied by programme and score, so they are stored only as historical. The previously confirmed seven 28DIGITAL tracks remain distinct and unchanged. No 2027/28 first-year offer or named admission call, fees, or new-entry awards were confirmed for these seven legacy programmes, and their active availability status remains pending. Official applicant totals were not published in the reviewed sources, so no course acceptance rate is inferred."
