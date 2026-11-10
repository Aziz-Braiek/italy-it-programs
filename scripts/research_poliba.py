"""Politecnico di Bari Computer Engineering review, checked 10 November 2026."""

CHECKED = "2026-11-10"
PROFILE = "https://www.poliba.it/laurea-magistrale-ingegneria-informatica"
REGULATION = "https://www.poliba.it/sites/default/files/regolamenti/regolamentodidattico/LM/Reg.LM32.ComputerScienceEng.A.Y.2026-27.pdf"
ADMISSIONS = "https://www.poliba.it/en/ammissioni-corsi-di-laurea-di-2deg-livello"
INTL = "https://www.poliba.it/en/general-overview"
FEES = "https://poliba.it/en/didattica/tasse"
FEE_REG = "https://poliba.it/sites/default/files/Tasse/Regolamento_contribuzione_studentesca_Politecnico_di_Bari_26_27_.pdf"
LANGUAGE = "https://www.poliba.it/en/inglese-b2-lauree-magistrali"
ADISU = "https://adisupuglia.it/pagina106703_borse-di-studio.html/"
SCHOLARSHIPS = "https://www.poliba.it/en/borse-di-studio"
GAZA_CALL = "https://www.poliba.it/sites/default/files/Borse%20di%20studio/D.R.%20Bando%20borsa%20di%20studio%20Palestina_signed_signed-signed.pdf"


def source(sid, title, url, cycle, evidence, supports, kind="Official university page"):
    return {"id": sid, "university_id": "politecnico-bari", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


SOURCES = [
    source("SRC-POLIBA-CENG-PROFILE-2026", "Computer Engineering MSc profile", PROFILE, "2026-2027",
           "The official profile lists the two-year English-taught Computer Engineering Master's at Bari. Current curricula are Artificial Intelligence and Data Science, Cybersecurity and Cloud, and Cyberphysical Systems. This is prior-cycle profile evidence only.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"]),
    source("SRC-POLIBA-CENG-REG-2026", "Computer Engineering teaching regulations 2026/27", REGULATION, "2026-2027",
           "Regulation identifies Class LM-32, 120 ECTS, two-year standard duration, English instruction, and three curricula. Admission requires a suitable bachelor's degree, at least 48 ECTS in listed engineering, computing, mathematics, physics and related areas, adequate preparation and English B2. Admission may require curricular integrations completed before entry; no educational debt is permitted.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_language_requirements"], "Official course regulation PDF"),
    source("SRC-POLIBA-MSC-ADMISSIONS-2026", "Admission to two-year Master's degrees 2026/27", ADMISSIONS, "2026-2027",
           "The mandatory prior-to-enrolment Esse3 process accepted one MSc preference per candidate after the bachelor's degree. 2026/27 application windows ran 28 July–15 September, then monthly windows through 10 May 2027. Eligibility checks covered the degree, curricular CFU, individual preparation and required English level. Eligible applicants enrolled 22 September 2026–20 May 2027; admission and enrollment are separate stages.",
           ["program.previous_cycle_application_windows", "program.previous_cycle_international_admission", "program.previous_cycle_application_fee", "program.previous_cycle_program_requirements"]),
    source("SRC-POLIBA-INTL-QUALIFICATIONS-2026", "General overview for international candidates 2026/27", INTL, "2026-2027",
           "Foreign-qualification evaluation requires academic records and proof of qualification authenticity. Visa applicants also submit Universitaly pre-enrolment; the 2026/27 page states a national visa-application outer date of 30 November 2026. Computer Engineering is an English-taught MSc, so foreign candidates use the Master's Esse3 assessment route and English evidence; Italian B2 applies to programmes taught in Italian. These are 2026/27 procedures only.",
           ["university.previous_cycle_non_eu_process", "program.previous_cycle_international_admission", "program.previous_cycle_application_windows", "program.previous_cycle_language_requirements" ]),
    source("SRC-POLIBA-B2-2026", "English B2 assessment for Master's degrees 2026/27", LANGUAGE, "2026-2027",
           "Computer Engineering is included in the 2026/27 Master's language-assessment list. The online English test has 30 questions, lasts 15 minutes and requires at least 21/30; applicants may register up to three working days before published test sessions. This calendar is prior-cycle only.",
           ["program.previous_cycle_language_requirements", "program.previous_cycle_application_windows"]),
    source("SRC-POLIBA-FEES-2026", "Tuition and fee information 2026/27", FEES, "2026-2027",
           "The 2026/27 calculator is ISEE-based and does not include merit reductions, exemptions or penalties. The initial enrollment installment is €136 (€120 regional tax plus €16 stamp duty); the regional contribution is adjusted at T2 according to the eligible ISEE. The annual all-inclusive contribution depends on the fee regulation and student circumstances.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition", "university.fee_conditions"]),
    source("SRC-POLIBA-FEE-REG-2026", "Student fees and contributions regulations 2026/27", FEE_REG, "2026-2027",
           "The annual all-inclusive contribution is income- and eligibility-dependent; it is zero in the no-tax area at ISEE ≤€26,000 when applicable criteria are satisfied and is capped at €2,257.60 for ISEE ≥€90,000 or absent eligible ISEE, before any late-payment or study-progress penalties. ADISU regional tax and €16 stamp duty are separate; normal contributions are divided across four payments. Merit and aid exemptions have additional conditions.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition", "university.fee_conditions"], "Official tuition regulation PDF"),
    source("SRC-ADISU-PUGLIA-2026", "ADISU Puglia benefits and scholarship call 2026/27", ADISU, "2026-2027",
           "The regional annual benefits call covered eligible students at the Polytechnic University of Bari. Degree-course applications ran 14 July–13 August 2026, noon, online. Awards and services are competitive and subject to the call's economic, merit, enrollment and documentation criteria; no Computer Engineering award is guaranteed.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarships", "university.regional_aid"], "Official regional scholarship call"),
    source("SRC-POLIBA-SCHOLARSHIPS-2026", "PoliBa scholarships and international-student support", SCHOLARSHIPS, "2026-2027",
           "The official index lists 2026/27 merit, international-student and other calls. Merit lists shown are for enrolled students and the previous cycle; do not treat them as first-year guarantees. It also records a 2026/27 one-scholarship call for Palestinian students resident in Gaza, restricted to candidates already admitted to an MSc and not compatible with ADISU aid.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarships"]),
    source("SRC-POLIBA-PALESTINE-SCHOLARSHIP-2026", "Targeted scholarship for Palestinian students from Gaza 2026/27", GAZA_CALL, "2026-2027",
           "The call offered one €22,000 gross award across two years to a Palestinian student resident in Gaza already admitted to a 2026/27 Poliba MSc. It includes €11,000 gross per year, full fee exemption and arrival/psychological support. Deadline was 23 October 2026. Second-year payment requires at least 12 CFU by 31 July 2027 and enrollment in 2027/28; the scholarship is incompatible with ADISU aid and is not a general 2027/28 new-entry award.",
           ["university.previous_cycle_targeted_scholarships", "university.previous_cohort_2027_2028_continuation", "program.previous_cycle_scholarships"], "Official targeted international scholarship call PDF"),
]

BATCH = {
    "id": "poliba-computer-engineering-course-and-admissions-review",
    "status": "partial",
    "result": "Matched the legacy Computer Engineering lead to Poliba's 2026/27 LM-32 English-taught two-year, 120-ECTS MSc. The course regulation requires a suitable bachelor's degree, at least 48 relevant ECTS, individual-preparation assessment and English B2; no educational debt is allowed. The mandatory 2026/27 Esse3 admission rounds precede enrollment; foreign-degree candidates also follow document/authenticity review and Universitaly if visa-requiring. Recorded conditional tuition, ADISU regional aid and narrowly targeted Poliba scholarship calls. The 2027/28 MSc first-year offer, course admission windows, requirements, fee schedule and new scholarship calls remain unconfirmed; the existing 2027/28 publication notice applies to first-level degrees only.",
}

REPORT = "Politecnico di Bari's official 2026/27 Computer Engineering MSc is Class LM-32, two years/120 ECTS and taught in English, with curricula in AI and Data Science, Cybersecurity and Cloud, and Cyberphysical Systems. Applicants needed a suitable bachelor's degree, at least 48 ECTS across listed engineering, computer-science, mathematics and related areas, adequate individual preparation and English B2; any curricular integrations had to be completed before entry. The mandatory Esse3 application had multiple 2026/27 windows and had to precede the later enrollment period. Foreign qualifications required document and authenticity checks; applicants needing a visa also used Universitaly. The 2026/27 tuition contribution varied by ISEE and merit/study-progress eligibility: the fee regulation sets no-tax-area criteria and a €2,257.60 contribution cap for high or absent eligible ISEE, plus regional tax and stamp duty. ADISU Puglia aid was an annual competitive call, while the Poliba international award reviewed was restricted to one already-admitted Palestinian student resident in Gaza. No new 2027/28 Computer Engineering first-year call or terms were found; the published February 2027 notice concerns first-level courses only."


def apply(universities, programs, fact):
    uni = next(u for u in universities if u["id"] == "politecnico-bari")
    uni.update(application_portal_url="https://poliba.esse3.cineca.it/",
               international_admissions_url=INTL,
               contact_email="foreign-qualifications@poliba.it",
               contact_url=INTL,
               cycle_status="REQUIRES_VERIFICATION", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    for alias in ("Polytechnic University of Bari", "PoliBa"):
        if alias not in uni["aliases"]:
            uni["aliases"].append(alias)
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    fee_sources = ["SRC-POLIBA-FEES-2026", "SRC-POLIBA-FEE-REG-2026"]
    aid_sources = ["SRC-ADISU-PUGLIA-2026", "SRC-POLIBA-SCHOLARSHIPS-2026", "SRC-POLIBA-PALESTINE-SCHOLARSHIP-2026"]
    prior_fees = fact({"academic_year": "2026/27", "annual_contribution_eur": {"no_tax_area": 0, "upper_cap": 2257.60,
                           "upper_cap_conditions": "ISEE ≥€90,000 or eligible ISEE absent; late-payment and progress penalties may apply"},
                       "initial_installment_components_eur": {"regional_tax_initial": 120, "stamp_duty": 16, "initial_total": 136},
                       "regional_tax": "Adjusted by eligible ISEE at second installment", "payment_count": 4,
                       "no_tax_area_threshold_eur": 26000, "no_tax_area_conditions": "Subject to enrollment-duration and credit-progress criteria; first-year MSc uses economic criterion only"},
                      "CONFIRMED", fee_sources,
                      "Prior-cycle 2026/27 framework only. The all-inclusive contribution depends on ISEE and eligibility; the initial €136 is not the annual total.")
    aid = fact({"academic_year": "2026/27", "ADISU_Puglia": {"application_open": "2026-07-14 08:00", "application_deadline": "2026-08-13 12:00", "procedure": "Online; annual competitive scholarship/services call"},
                "PoliBa_targeted_Palestinian_award": {"awards": 1, "eligibility": "Palestinian students resident in Gaza already admitted to a Poliba Master's in 2026/27", "gross_total_eur": 22000, "gross_per_year_eur": 11000, "deadline": "2026-10-23 12:00", "second_year_conditions": "At least 12 CFU by 31 July 2027 and enrollment in 2027/28", "incompatible_with": "ADISU Puglia and listed international schemes"},
                "PoliBa_merit_schemes": "Annual competitive calls; reviewed calls concern enrolled students or earlier cycles, not a guaranteed first-year course award"},
               "CONFIRMED", aid_sources,
               "Historical 2026/27 funding context. ADISU is a separate competitive regional scheme; the €22,000 award is narrowly eligibility-restricted and second-year renewal is conditional.")
    cycle_facts = dict(uni.get("cycle_facts", {}))
    cycle_facts.update({
        "application_windows": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIBA-MSC-ADMISSIONS-2026"], "The available Master's rounds are for 2026/27; no 2027/28 Computer Engineering application calendar was identified."),
        "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIBA-MSC-ADMISSIONS-2026"], "The current admission page is for 2026/27 and does not establish a 2027/28 application fee."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", fee_sources, "No 2027/28 fee regulation or amount was identified."),
        "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", aid_sources, "The reviewed regional and university calls are scoped to 2026/27; no general 2027/28 award for new Computer Engineering entrants was identified."),
        "previous_cycle_tuition": prior_fees,
        "previous_cycle_scholarships": aid,
        "previous_cycle_non_eu_process": fact({"academic_year": "2026/27", "foreign_qualification_review": "Esse3 Master's admission assessment plus document/authenticity review", "visa_required": "Universitaly pre-enrolment in addition to university admission", "national_visa_application_outer_deadline": "2026-11-30", "international_contact": "foreign-qualifications@poliba.it"}, "CONFIRMED", ["SRC-POLIBA-INTL-QUALIFICATIONS-2026"], "Prior-cycle foreign-degree and national visa guidance only; visa issuance remains a consular decision."),
    })
    uni["cycle_facts"] = cycle_facts

    p = next(p for p in programs if p["id"] == "legacy-094")
    p.update(program="Computer Engineering", city="Bari", overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
    sources = ["SRC-POLIBA-CENG-PROFILE-2026", "SRC-POLIBA-CENG-REG-2026", "SRC-POLIBA-MSC-ADMISSIONS-2026",
               "SRC-POLIBA-INTL-QUALIFICATIONS-2026", "SRC-POLIBA-B2-2026", "SRC-POLIBA-FEES-2026",
               "SRC-POLIBA-FEE-REG-2026", "SRC-ADISU-PUGLIA-2026", "SRC-POLIBA-SCHOLARSHIPS-2026",
               "SRC-POLIBA-PALESTINE-SCHOLARSHIP-2026", "SRC-POLIBA-2027"]
    p["source_ids"] = sources
    for key, value in (("level", "MSc"), ("language", "English"), ("field", "Computer Engineering")):
        p[key] = fact(value, "REQUIRES_VERIFICATION", ["SRC-POLIBA-CENG-PROFILE-2026", "SRC-POLIBA-CENG-REG-2026"], "Official 2026/27 course identity only; the 2027/28 new-entry offer and current course terms are not confirmed.")
    p["previous_cycle_tags"] = {"level": "MSc", "language": "English", "field": "Computer Engineering", "cycle": "2026-2027", "label": "Official 2026/27 profile and regulation; new 2027/28 intake remains unverified"}
    p["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIBA-CENG-PROFILE-2026", "SRC-POLIBA-MSC-ADMISSIONS-2026"], "Reviewed official course and admission materials are for 2026/27. The 2027/28 publication notice found concerns first-level degrees; no MSc first-year intake or discontinuation is confirmed.")
    p["facts"] = {
        "previous_cycle_course_listing": fact({"academic_year": "2026/27", "official_name": "Computer Engineering", "degree_class": "LM-32", "level": "MSc", "duration_years": 2, "ects": 120, "campus": "Bari", "language": "English", "curricula": ["Artificial Intelligence and Data Science", "Cybersecurity and Cloud", "Cyberphysical Systems"]}, "CONFIRMED", ["SRC-POLIBA-CENG-PROFILE-2026", "SRC-POLIBA-CENG-REG-2026"], "Official 2026/27 course listing only; no new 2027/28 offer is inferred."),
        "previous_cycle_program_requirements": fact({"academic_year": "2026/27", "qualification": "Suitable bachelor's or equivalent degree from Italy or abroad", "curricular_requirements": "At least 48 ECTS in listed scientific disciplinary sectors across engineering, computer science, mathematics, physics and related areas", "integrations": "Any missing curricular credits must be completed before admission; no educational debt permitted", "preparation_assessment": "Bachelor final result normally used; coordinator may identify additional need", "application_limit": "One Master's preference per application; bachelor's degree must already be obtained"}, "CONFIRMED", ["SRC-POLIBA-CENG-REG-2026", "SRC-POLIBA-MSC-ADMISSIONS-2026"], "Prior-cycle course admission criteria; recheck the annual 2027/28 regulation."),
        "previous_cycle_language_requirements": fact({"academic_year": "2026/27", "instruction_language": "English", "requirement": "B2 or higher", "verification": "Recognized certificate or University Language Centre test; for Computer Engineering the English B2 test required at least 21/30 on a 30-question, 15-minute assessment"}, "CONFIRMED", ["SRC-POLIBA-CENG-REG-2026", "SRC-POLIBA-B2-2026", "SRC-POLIBA-MSC-ADMISSIONS-2026"], "Prior-cycle course language and language-test context only."),
        "previous_cycle_application_windows": fact({"academic_year": "2026/27", "admission_platform": "Esse3", "admission_windows": [["2026-07-28", "2026-09-15"], ["2026-10-01", "2026-10-15"], ["2026-11-01", "2026-11-15"], ["2026-12-01", "2026-12-15"], ["2027-01-05", "2027-01-20"], ["2027-02-01", "2027-02-15"], ["2027-03-01", "2027-03-15"], ["2027-04-01", "2027-04-15"], ["2027-05-02", "2027-05-10"]], "enrollment_window": ["2026-09-22", "2027-05-20"], "required_order": "Mandatory master's assessment before enrollment; candidates were admitted after review"}, "CONFIRMED", ["SRC-POLIBA-MSC-ADMISSIONS-2026"], "Closed prior-cycle schedule. Admission windows and later enrollment window are separate processes and are not 2027/28 dates."),
        "previous_cycle_application_fee": fact(None, "UNAVAILABLE", ["SRC-POLIBA-MSC-ADMISSIONS-2026"], "The reviewed 2026/27 Master's admission instructions do not state a course application charge; no zero-fee assumption is made."),
        "previous_cycle_international_admission": fact({"academic_year": "2026/27", "university_admission": "Esse3 master's assessment and qualification/document review", "visa_applicants": "Also submit Universitaly pre-enrolment", "foreign_document_authenticity": "CIMEA/ENIC-NARIC verification or legalisation/apostille, as applicable", "foreign_degree_documents": ["Degree certificate", "Transcript", "Translations to Italian or English"], "national_visa_application_outer_deadline": "2026-11-30"}, "CONFIRMED", ["SRC-POLIBA-MSC-ADMISSIONS-2026", "SRC-POLIBA-INTL-QUALIFICATIONS-2026"], "General 2026/27 route only. University academic admission and consular visa decisions are separate."),
        "application_windows": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIBA-MSC-ADMISSIONS-2026", "SRC-POLIBA-CENG-PROFILE-2026"], "No Computer Engineering 2027/28 Master's call or dates were identified."),
        "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIBA-MSC-ADMISSIONS-2026"], "No 2027/28 Master's application fee was published in the reviewed material."),
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-POLIBA-CENG-REG-2026", "SRC-POLIBA-MSC-ADMISSIONS-2026"], "Current course-specific regulation and admissions page are for 2026/27; new-cycle rules remain unverified."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", fee_sources, "No 2027/28 tuition regulation or course fee was identified."),
        "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", aid_sources, "The reviewed regional and targeted awards are 2026/27; no general award for 2027/28 new entrants was confirmed."),
        "previous_cycle_tuition": prior_fees,
        "previous_cycle_scholarships": aid,
        "acceptance_rate": fact(None, "UNAVAILABLE", ["SRC-POLIBA-MSC-ADMISSIONS-2026"], "The admission page describes eligibility outcomes but does not provide comparable total applicant and admitted counts; no acceptance rate is inferred."),
    }
