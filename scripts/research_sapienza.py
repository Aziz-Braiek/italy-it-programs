"""Sapienza candidate program and admissions review, checked 10 November 2026."""

CHECKED = "2026-11-10"
ENGLISH_ADMISSIONS = "https://www.uniroma1.it/en/en/admissions"
MOVEIN_REQUIREMENTS = "https://www.uniroma1.it/sites/default/files/field_file_allegati/academic_requirements_movein_2026-2027_web.pdf"
INTERNATIONAL_OFFICE = "https://www.uniroma1.it/en/node/24774"
FEES = "https://www.uniroma1.it/en/pagina/tuition-fees-and-benefits"
FEE_TABLE = "https://www.uniroma1.it/en/node/29732"
WANTED_BEST = "https://www.uniroma1.it/en/pagina/scholarships-meritorious-students-italian-and-international-universities"
DISCO = "https://laziodisco.it/on-line-il-bando-diritto-allo-studio-2026-2027/?lang=en"


def source(sid, title, url, cycle, evidence, supports, kind="Official university page"):
    return {"id": sid, "university_id": "sapienza", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


SOURCES = [
    source("SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "Programmes in English and 2026/27 pre-selection", ENGLISH_ADMISSIONS, "2026-2027",
           "English-taught degree applicants used MoveIN pre-selection. The 2026/27 cycle opened 22 December 2025; the non-EU visa-applicant deadline was 15 May 2026, the EU/equivalent deadline was 31 July 2026, and Universitaly pre-enrolment was due 30 June 2026. A candidate could submit up to two applications. Pre-selection was only one step and did not guarantee final admission. No 2027/28 first-year schedule is stated on the reviewed page.",
           ["university.previous_cycle_admission_process", "university.previous_cycle_application_windows", "program.previous_cycle_application_windows"]),
    source("SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026", "English-program academic and language requirements 2026/27", MOVEIN_REQUIREMENTS, "2026-2027",
           "The official PDF lists 2026/27 English bachelor’s and master’s programs and gives program-specific prior-cycle entry requirements. It lists Computer Science, Artificial Intelligence and Robotics, Cybersecurity, Data Science, Applied Computer Science and Artificial Intelligence, and Sustainable Building Engineering among the tracker’s matches. Requirements and scores belong to 2026/27 only.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official admissions requirements PDF"),
    source("SRC-SAPIENZA-INTL-OFFICE-2026", "International Student Office admissions procedures 2026/27", INTERNATIONAL_OFFICE, "2026-2027",
           "The 2026/27 procedure distinguishes EU/equivalent candidates from non-EU applicants residing abroad. English-course applicants requiring a study visa needed the MoveIN pre-acceptance letter and Universitaly pre-enrolment by 30 June 2026; final admission still depended on the individual course call, qualification verification, visa, and completed enrollment. Foreign qualifications were reviewed for authenticity and comparability. Italian-taught programs required certified Italian B2 for non-EU applicants abroad who needed a visa.",
           ["university.previous_cycle_non_eu_process", "university.previous_cycle_foreign_qualification_review", "program.previous_cycle_international_admission"]),
    source("SRC-SAPIENZA-ENGCSAI-COURSE-2026", "Engineering in Computer Science and Artificial Intelligence course regulations 2026/27", "https://corsidilaurea.uniroma1.it/en/timeview/2026/33515/organization", "2026-2027",
           "The archived 2026/27 catalogue identifies the two-year, 120-ECTS LM-32 MSc, taught exclusively in English. Admission required a suitable bachelor’s degree, at least 60 recognized ECTS across defined scientific and engineering areas (including at least 24 basic-science and 36 engineering/computing credits, with specified sub-minima), and English B2; a committee assessed preparation and could interview applicants.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course regulations"),
    source("SRC-SAPIENZA-AERONAUTICAL-2026", "Aeronautical Engineering course profile 2026/27", "https://corsidilaurea.uniroma1.it/it/course/33483", "2026-2027",
           "The 2026/27 catalogue identifies Ingegneria aeronautica - Aeronautical engineering as a two-year LM-20 Master’s degree in Rome with Italian and English listed as languages of instruction. This bilingual course is not the separate Space and Astronautical Engineering program.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-MEDICINE-2026", "Medicine and Surgery course catalogue entries 2026/27", "https://corsidilaurea.uniroma1.it/it/solr-offerta-formativa-t?search_api_views_fulltext=Medicina+e+chirurgia", "2026-2027",
           "The 2026/27 catalogue lists several single-cycle LM-41 Medicine and Surgery courses at separate campuses. It lists one distinct English-taught course, Medicine and Surgery F, as a six-year program. The legacy candidate does not identify its campus or track, so the English and Italian variants are not merged.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-AEROSPACE-BSC-2026", "Ingegneria Aerospaziale course profile 2026/27", "https://corsidilaurea.uniroma1.it/it/course/33474", "2026-2027",
           "The current official profile identifies course 33474 / test code 14616 as a three-year L-9 Italian bachelor's degree in Rome with admission-test access. Its current-student notices include a 2027/28 laboratory-assignment notice for third-year students; that notice is not a 2027/28 first-year admission announcement.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-POLITICAL-SCIENCE-2026", "Political Science and International Relations bachelor’s profile 2026/27", "https://corsidilaurea.uniroma1.it/it/course/33618", "2026-2027",
           "The 2026/27 catalogue identifies Scienze politiche e relazioni internazionali as a three-year L-36 bachelor’s degree in Rome, taught in Italian. Its entry route is a test to verify knowledge.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-PSYCHOLOGY-2026", "Psychology and Health bachelor’s profile 2026/27", "https://corsidilaurea.uniroma1.it/it/course/33570", "2026-2027",
           "The 2026/27 catalogue identifies Psicologia e Salute as a three-year L-24 bachelor’s degree in Rome, taught in Italian and with an admission test.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-ECONOMICS-FINANCE-2026", "Economics and Finance bachelor’s listing 2026/27", "https://corsidilaurea.uniroma1.it/en/timeview/2026/34177/organization", "2026-2027",
           "The same-name 2026/27 course is Economia e finanza, an L-33 three-year bachelor’s program, not the MSc classification in the previous tracker. The catalogue lists Italian and English, but this does not establish that the entire course is English-taught. The match to the old MSc lead is unresolved.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-FINANCE-INSURANCE-2026", "Finance and Insurance Master’s profile 2026/27", "https://www.corsidilaurea.uniroma1.it/en/course/33439", "2026-2027",
           "The separate 2026/27 Finance and Insurance program is a two-year LM-16 Master’s degree in Rome. The catalogue lists Italian and English curricula/language, so it is not represented as entirely English-taught. It is tracked separately from the same-name Economia e finanza L-33 bachelor’s course.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"], "Official course catalogue"),
    source("SRC-SAPIENZA-INGINFO-ARCHIVE-2024", "Ingegneria Informatica historical course archive", "https://corsidilaurea.uniroma1.it/sites/default/files/archive/2024/30430.pdf", "2024-2025",
           "The archived official document identifies the earlier Ingegneria Informatica as an LM-32 two-year Master’s degree. This is older than the immediate prior cycle and does not establish a 2026/27 or 2027/28 offer. The 2026/27 English Engineering in Computer Science and Artificial Intelligence course is tracked separately pending proof of course succession.",
           ["program.historical_course_reference"], "Official archived course regulation PDF"),
    source("SRC-SAPIENZA-FEES-2026", "Tuition, payment and foreign-income guidance 2026/27", FEES, "2026-2027",
           "The 2026/27 tuition page describes ISEE-based reductions, three installments of 30%, 35% and 35%, the ordinary fee framework and foreign-income rules. These are annual rules and the amount depends on course area and individual circumstances.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition", "university.fee_conditions"]),
    source("SRC-SAPIENZA-FEE-TABLE-2026", "Standard registration-fee amounts for 2026/27", FEE_TABLE, "2026-2027",
           "Art. 38 lists a €2,924 second-contribution-bracket standard for second-level two-year, single-cycle and unified Master's degrees in named faculties, including Civil and Industrial Engineering; this is not a quoted fee for the three-year Aerospace BSc. The page also lists foreign-income contribution bands of €300, €700 or €1,500 by country group. Check the course, residence, income and exemptions before quoting a student's amount.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition", "university.fee_conditions"]),
    source("SRC-SAPIENZA-APPLICATION-FEE-2026", "MoveIN pre-selection application fee 2026/27", "https://www.uniroma1.it/it/pagina/international-admissions-2026-2027", "2026-2027",
           "The official admissions information states a €30 fee for each pre-selection application, up to two applications per candidate and intake, with no waiver. The general International Student Office separately describes a €10 course requirement-assessment payment for applicable Master’s routes; these are different processes.",
           ["university.previous_cycle_application_fee", "program.previous_cycle_application_fee"]),
    source("SRC-SAPIENZA-WANTED-BEST-2026", "Wanted the Best merit scholarship call 2026/27", WANTED_BEST, "2026-2027",
           "The 2026/27 call offered 85 two-year awards of €3,000 gross per year to students enrolling in a Sapienza Master’s after earning their first degree at another Italian university with a grade from 105/110 to 110/110 cum laude. Deadline: 30 October 2026. It is not a general award for applicants whose prior degree is from abroad.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarships"], "Official scholarship call"),
    source("SRC-SAPIENZA-DISCO-LAZIO-2026", "DiSCo Lazio Right to Education call 2026/27", DISCO, "2026-2027",
           "The regional competitive call covered students at Lazio universities, including Sapienza, and offered scholarships, housing, mobility grants and other benefits subject to the annual economic and merit rules. The application deadline was extended to 23 July 2026 at 20:00; corrections in the second phase closed 11 August. It is prior-cycle regional aid, not a guaranteed Sapienza or program award.",
           ["university.previous_cycle_regional_aid", "university.previous_cycle_scholarships", "program.previous_cycle_scholarships"], "Official regional scholarship call"),
]

BATCH = {
    "id": "sapienza-program-catalogue-and-international-admissions-review",
    "status": "partial",
    "result": "Reviewed all 13 existing Sapienza candidate rows against official catalogue and admissions evidence, plus two newly identified adjacent Master's candidates. Six existing English-taught Computing/AI candidates are listed in the 2026/27 MoveIN requirements PDF; their historical entry criteria and B2 evidence are captured. Confirmed the separate 2026/27 bilingual Aeronautical Engineering LM-20, Italian Aerospace Engineering L-9, Political Science L-36, Psychology and Health L-24, and the single-cycle Medicine and Surgery variants. Corrected the same-name Economia e finanza lead from the prior tracker’s MSc label to the official 2026/27 L-33 bachelor’s listing while retaining uncertainty about whether it was the same lead. Added Engineering in Computer Science and Artificial Intelligence LM-32 and Finance and Insurance LM-16 as separate discoveries. The 2026/27 MoveIN and enrollment procedures, fees, foreign-qualification pathway and competitive regional/university aid are historical only. No 2027/28 new-entry call or terms have been confirmed.",
}

REPORT = "Sapienza's English admissions page and 2026/27 MoveIN requirements PDF list Computer Science, Artificial Intelligence and Robotics, Cybersecurity, Data Science, Applied Computer Science and Artificial Intelligence, and Sustainable Building Engineering among the program candidates. The PDF supplies historical course requirements and B2 English evidence; for example, Computer Science required a relevant bachelor’s degree and specified curricular credits, while Data Science used a preparation review, online test and committee interview. The 2026/27 MoveIN cycle required separate pre-selection, with 2026 deadlines, and visa applicants also had Universitaly and foreign-qualification checks. Other official 2026/27 catalogue matches include Aeronautical Engineering LM-20 (Italian/English), Aerospace Engineering L-9 (Italian), Political Science and International Relations L-36 (Italian), Psychology and Health L-24 (Italian), and multiple Medicine and Surgery LM-41 campus variants; the legacy Medicine lead does not identify a campus, so it remains ambiguous. The same-name Economia e finanza entry is an L-33 bachelor’s course in 2026/27, whereas Finance and Insurance is a distinct LM-16 Master’s; the latter is tracked separately. The English Engineering in Computer Science and Artificial Intelligence LM-32 course is also kept separate from the older archived Ingegneria Informatica lead. 2026/27 fee tables, Wanted the Best scholarship eligibility and DiSCo Lazio aid are stored as prior-cycle context. No reviewed official page confirms a 2027/28 first-year intake, deadlines, fees or awards for these candidates."


def fact(value, status, sources=(), note=None):
    return {"value": value, "status": status, "source_ids": list(sources), "notes": note}


def apply(universities, programs, fact_builder):
    uni = next(u for u in universities if u["id"] == "sapienza")
    uni.update(application_portal_url="https://sapienza.gomovein.com/",
               international_admissions_url=INTERNATIONAL_OFFICE,
               contact_email="studentistranieri@uniroma1.it",
               contact_url=INTERNATIONAL_OFFICE,
               cycle_status="REQUIRES_VERIFICATION", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    if "Sapienza University of Rome" not in uni["aliases"]:
        uni["aliases"].append("Sapienza University of Rome")
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    windows = fact_builder({"academic_year": "2026/27", "movein_open": "2025-12-22", "non_eu_visa_deadline": "2026-05-15",
                            "eu_equivalent_deadline": "2026-07-31", "universitaly_outer_deadline": "2026-06-30",
                            "maximum_applications": 2, "scope": "General English-course pre-selection; individual course calls and final enrollment steps still applied"},
                           "CONFIRMED", ["SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
                           "Closed prior-cycle dates only; the 2027/28 English admissions schedule has not been verified.")
    fee = fact_builder({"academic_year": "2026/27", "MoveIN_preselection_eur_per_application": 30,
                        "MoveIN_maximum_applications": 2, "preselection_fee_waiver": False,
                        "separate_MSc_assessment_fee_eur_when_applicable": 10}, "CONFIRMED",
                       ["SRC-SAPIENZA-APPLICATION-FEE-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"],
                       "Historical fees for distinct steps; no 2027/28 application charge is confirmed.")
    tuition_sources = ["SRC-SAPIENZA-FEES-2026", "SRC-SAPIENZA-FEE-TABLE-2026"]
    tuition = fact_builder({"academic_year": "2026/27", "standard_second_faculty_group_total_eur": 2924,
                            "foreign_income_fixed_contribution_bands_eur": [300, 700, 1500],
                            "payment_installments_percent": [30, 35, 35],
                            "calculation": "ISEE and course/faculty group, foreign-income band, eligibility and exemptions affect the amount"},
                           "CONFIRMED", tuition_sources,
                           "Prior-cycle university fee framework only; the amounts are not a 2027/28 or individual quote.")
    scholarships = fact_builder({"academic_year": "2026/27",
                                 "Wanted_the_Best": {"awards": 85, "gross_eur_per_year": 3000, "duration_years": 2,
                                     "eligibility": "Master’s entrants graduating from another Italian university with 105/110 to 110/110 cum laude", "deadline": "2026-10-30"},
                                 "DiSCo_Lazio": {"application_deadline_after_extension": "2026-07-23 20:00", "second_phase_corrections_deadline": "2026-08-11 12:00", "scope": "Competitive regional scholarship, housing and other benefits"}},
                                "CONFIRMED", ["SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"],
                                "Annual 2026/27 competitions only. The university award is restricted and the regional award is competitive; neither is a guaranteed 2027/28 offer.")
    uni["cycle_facts"] = {
        "application_windows": fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"], "The page reviewed provides the 2026/27 calendar only; no 2027/28 first-year application schedule was found."),
        "application_fee_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-APPLICATION-FEE-2026"], "The €30 MoveIN and separate €10 assessment amounts are 2026/27 only; no 2027/28 fee is confirmed."),
        "tuition_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", tuition_sources, "No 2027/28 fee regulation or personal fee calculation was identified."),
        "scholarships_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"], "The reviewed calls are 2026/27; no 2027/28 call for incoming students was identified."),
        "previous_cycle_application_windows": windows,
        "previous_cycle_application_fee": fee,
        "previous_cycle_tuition": tuition,
        "previous_cycle_scholarships": scholarships,
        "previous_cycle_non_eu_process": fact_builder({"academic_year": "2026/27", "English_programs": "MoveIN pre-selection where listed, then course call and qualification assessment", "non_eu_visa_applicants": "Pre-acceptance letter followed by Universitaly pre-enrolment by 30 June 2026", "foreign_qualification_review": "Academic comparability, authenticity and required documentation assessed by Sapienza", "Italian_taught_programs": "Certified Italian B2 for non-EU applicants abroad who require a visa", "contact": "studentistranieri@uniroma1.it"},
                                                       "CONFIRMED", ["SRC-SAPIENZA-INTL-OFFICE-2026", "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"],
                                                       "General 2026/27 process only; final admission, visa and enrollment were separate decisions."),
    }

    profiles = {
        "legacy-038": {"name": "Computer Science", "level": "MSc", "language": "English", "field": "Computer Science", "sources": ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026"],
            "requirements": {"qualification": "Bachelor’s degree in Computer Science, Computer Science Engineering or equivalent", "curricular_credits": "At least 90 ECTS in listed scientific sectors; at least 72 in foundation/core areas", "preparation": "Computer science fundamentals; program-specific assessment", "minimum_gpa": "75/100"}, "english": "B2 CEFR; 2026/27 accepted IELTS 5.5, TOEFL iBT 80, Cambridge B2 First or Trinity ISE II; listed exemptions applied"},
        "legacy-039": {"name": "Artificial Intelligence and Robotics", "level": "MSc", "language": "English", "field": "Artificial Intelligence and Robotics", "sources": ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026"],
            "requirements": {"qualification": "Bachelor’s in Computer Engineering, Computer Science or another scientific discipline", "assessment": "Technical Skype interview for selected applicants", "minimum_gpa": "75/100"}, "english": "B2 CEFR; 2026/27 accepted IELTS 5.5 or TOEFL iBT 80 and listed equivalents/exemptions"},
        "legacy-040": {"name": "Cybersecurity", "level": "MSc", "language": "English", "field": "Cybersecurity", "sources": ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026"],
            "requirements": {"duration": "2 years / 120 ECTS", "qualification": "Bachelor’s in Computer Science, Computer Engineering, Mathematics, Physics, Statistics, Telecommunications or related field", "minimum_gpa": "75/100"}, "english": "B2 CEFR; 2026/27 accepted IELTS 5.5, TOEFL iBT 80, Cambridge B2 First or Trinity ISE II; listed exemptions applied"},
        "legacy-041": {"name": "Data Science", "level": "MSc", "language": "English", "field": "Data Science", "sources": ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026"],
            "requirements": {"qualification": "Three-year degree in computing, engineering, statistics, mathematics, physics, economics or related field", "assessment": "Career and degree relevance review, followed by online test and committee interview", "minimum_gpa": "80/100", "GRE": "Strongly recommended"}, "english": "B2 CEFR; 2026/27 accepted IELTS 5.5, TOEFL iBT 80, Cambridge B2 First or Trinity ISE II; listed exemptions applied"},
        "legacy-042": {"name": "Applied Computer Science and Artificial Intelligence", "level": "BSc", "language": "English", "field": "Computer Science and Artificial Intelligence", "sources": ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026"],
            "requirements": {"qualification": "Upper-secondary diploma after at least 12 years of schooling", "entry_tests": "For 2026/27, SAT or CISIA tests under candidate-specific thresholds; non-EU candidates required the SAT threshold", "minimum_gpa": "75/100"}, "english": "B2 CEFR; course-specific accepted 2026/27 evidence and exemptions in the annual PDF"},
        "legacy-043": {"name": "Ingegneria aeronautica - Aeronautical engineering", "level": "MSc", "language": "Italian and English", "field": "Aeronautical Engineering", "sources": ["SRC-SAPIENZA-AERONAUTICAL-2026"],
            "listing": {"degree_class": "LM-20", "duration_years": 2, "campus": "Rome", "catalogue_language": "Italian and English"}},
        "legacy-044": {"name": "Sustainable Building Engineering", "level": "BSc", "language": "English", "field": "Sustainable Building Engineering", "sources": ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026"],
            "requirements": {"qualification": "High-school diploma after 12 years, or 11 years plus at least one year of technical university enrollment", "entry_tests": "SAT or CEnT-S for 2026/27", "minimum_gpa": "80/100"}, "english": "B2 CEFR; 2026/27 accepted IELTS 5.5, TOEFL iBT 80, Cambridge B2 First or Trinity ISE II and listed exemptions"},
        "legacy-153": {"name": "Medicina e Chirurgia", "level": "MSc", "language": "Italian or English depending on campus/track", "field": "Medicine", "sources": ["SRC-SAPIENZA-MEDICINE-2026"],
            "listing": {"academic_year": "2026/27", "course_variants": "Multiple Italian-taught campus courses and a separate six-year English-taught Medicine and Surgery F course", "legacy_track_match": "Unresolved; the prior tracker did not identify a campus or curriculum"}},
        "legacy-154": {"name": "Ingegneria Aerospaziale", "level": "BSc", "language": "Italian", "field": "Aerospace Engineering", "sources": ["SRC-SAPIENZA-AEROSPACE-BSC-2026"],
            "listing": {"degree_class": "L-9", "duration_years": 3, "campus": "Rome", "admission": "Entry test"}},
        "legacy-155": {"name": "Scienze politiche e relazioni internazionali", "level": "BSc", "language": "Italian", "field": "Political Science and International Relations", "sources": ["SRC-SAPIENZA-POLITICAL-SCIENCE-2026"],
            "listing": {"degree_class": "L-36", "duration_years": 3, "campus": "Rome", "admission": "Knowledge-assessment entry test"}},
        "legacy-156": {"name": "Psicologia e Salute", "level": "BSc", "language": "Italian", "field": "Psychology", "sources": ["SRC-SAPIENZA-PSYCHOLOGY-2026"],
            "listing": {"degree_class": "L-24", "duration_years": 3, "campus": "Rome", "admission": "Admission test"}},
        "legacy-157": {"name": "Ingegneria Informatica", "level": "MSc", "language": "Italian (previous tracker label)", "field": "Computer Engineering", "sources": ["SRC-SAPIENZA-INGINFO-ARCHIVE-2024", "SRC-SAPIENZA-ENGCSAI-COURSE-2026"],
            "historical": {"academic_year": "2024/25", "degree_class": "LM-32", "duration_years": 2, "2026_27_exact_match": "Not established; the separate English Engineering in Computer Science and Artificial Intelligence record remains distinct"}},
        "legacy-158": {"name": "Economia e finanza", "level": "BSc", "language": "Italian and English listed", "field": "Economics and Finance", "sources": ["SRC-SAPIENZA-ECONOMICS-FINANCE-2026"],
            "listing": {"academic_year": "2026/27", "degree_class": "L-33", "duration_years": 3, "catalogue_languages": ["Italian", "English"], "legacy_conflict": "The previous tracker called this an MSc; the current same-name entry is a bachelor’s degree, so the intended match remains unresolved"}},
        "discovered-026": {"name": "Engineering in Computer Science and Artificial Intelligence", "level": "MSc", "language": "English", "field": "Computer Engineering and Artificial Intelligence", "sources": ["SRC-SAPIENZA-ENGCSAI-COURSE-2026"],
            "listing": {"degree_class": "LM-32", "duration_years": 2, "ects": 120, "campus": "Rome", "instruction": "English only"},
            "requirements": {"qualification": "Bachelor’s degree or recognized equivalent", "credits": "At least 60 ECTS: 24 basic-science and 36 engineering/computing, with specified sub-minima", "english": "B2", "assessment": "Committee review of academic preparation; interview may be used"}},
        "discovered-027": {"name": "Finance and Insurance", "level": "MSc", "language": "Italian and English curricula listed", "field": "Finance and Insurance", "sources": ["SRC-SAPIENZA-FINANCE-INSURANCE-2026"],
            "listing": {"degree_class": "LM-16", "duration_years": 2, "campus": "Rome", "catalogue_language": "Italian and English", "access": "Curricular requirements and personal-preparation assessment"}},
    }

    movein_programs = {"legacy-038", "legacy-039", "legacy-040", "legacy-041", "legacy-042", "legacy-044", "discovered-027"}
    for pid, profile in profiles.items():
        p = next(p for p in programs if p["id"] == pid)
        p.update(program=profile["name"], city="Rome", overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
        srcs = list(dict.fromkeys(profile["sources"] + ["SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026", "SRC-SAPIENZA-INTL-OFFICE-2026"]))
        p["source_ids"] = srcs
        note = "Official 2026/27 evidence only; it does not confirm a 2027/28 new-entry offer or current terms."
        for key, value in (("level", profile["level"]), ("language", profile["language"]), ("field", profile["field"])):
            p[key] = fact_builder(value, "REQUIRES_VERIFICATION", profile["sources"], note)
        p["availability_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION", srcs,
            "The reviewed university admissions and course materials concern 2026/27 or older. No 2027/28 first-year call was found, and absence from these pages is not treated as discontinuation.")
        p["previous_tracker_tags"] = p.get("previous_tracker_tags") or {"level": profile["level"], "language": profile["language"], "field": profile["field"], "label": "Earlier tracker lead; official 2026/27 comparison recorded separately"}
        if pid == "legacy-157":
            p["previous_cycle_tags"] = None
        else:
            p["previous_cycle_tags"] = {"level": profile["level"], "language": profile["language"], "field": profile["field"], "cycle": "2026-2027", "label": "Official 2026/27 evidence only; 2027/28 intake remains unverified"}
        facts = {
            "application_windows_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"], "The reviewed application schedule is for 2026/27 only."),
            "application_fee_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-APPLICATION-FEE-2026"], "No 2027/28 course application fee was identified."),
            "tuition_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", tuition_sources, "No 2027/28 tuition regulation or amount was identified."),
            "scholarships_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION", ["SRC-SAPIENZA-WANTED-BEST-2026", "SRC-SAPIENZA-DISCO-LAZIO-2026"], "No 2027/28 scholarship call for these new entrants was identified."),
            "previous_cycle_tuition": tuition,
            "previous_cycle_scholarships": scholarships,
            "acceptance_rate": fact_builder(None, "UNAVAILABLE", srcs, "The reviewed sources do not provide a comparable complete applicant and admitted-student denominator."),
        }
        if pid in movein_programs:
            facts["previous_cycle_application_windows"] = windows
            facts["previous_cycle_application_fee"] = fee
        else:
            facts["previous_cycle_application_windows"] = fact_builder(None, "REQUIRES_VERIFICATION", profile["sources"], "No course-specific 2026/27 application calendar was captured for this lead; the general MoveIN schedule applies only to the programs listed for pre-selection.")
            facts["previous_cycle_application_fee"] = fact_builder(None, "REQUIRES_VERIFICATION", profile["sources"], "No course-specific 2026/27 application charge was captured for this lead; the €30 MoveIN charge applies only to listed pre-selection applications.")
        if "listing" in profile:
            facts["previous_cycle_course_listing"] = fact_builder(profile["listing"], "CONFIRMED", profile["sources"], note)
        if "requirements" in profile:
            facts["previous_cycle_program_requirements"] = fact_builder(profile["requirements"], "CONFIRMED", profile["sources"], note)
        if "english" in profile:
            facts["previous_cycle_language_requirements"] = fact_builder(profile["english"], "CONFIRMED", profile["sources"], note)
        if "historical" in profile:
            facts["historical_course_reference"] = fact_builder(profile["historical"], "CONFIRMED", ["SRC-SAPIENZA-INGINFO-ARCHIVE-2024"], "This is 2024/25 archive evidence, not immediate prior-cycle or current offer confirmation.")
        p["facts"] = facts

    uni["cycle_facts"]["previous_cycle_course_admission_requirements"] = fact_builder({"academic_year": "2026/27", "english_programs": "Program-specific criteria published in the MoveIN academic-requirements PDF", "individual_calls": "Additional course catalogue calls may apply after pre-selection"}, "CONFIRMED", ["SRC-SAPIENZA-MOVEIN-REQUIREMENTS-2026", "SRC-SAPIENZA-ENGLISH-ADMISSIONS-2026"], "Historical course requirements only; use each new annual call for current criteria.")
