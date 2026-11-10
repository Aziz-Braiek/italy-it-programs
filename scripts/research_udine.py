"""University of Udine Computer Science review, checked 10 November 2026."""

CHECKED = "2026-11-10"
PROFILE = "https://www.uniud.it/en/education/offer/courses/scientific-area/mathematics-computer-sciences-multimedia-physics/master-degree-courses-graduate-120-ects/computer-science/computer-science?set_language=en"
REQUIREMENTS = "https://www.uniud.it/it/didattica/corsi/area-scientifica/scienze-matematiche-informatiche-multimediali-fisiche/laurea-magistrale/informatica/iscrizione/conoscenze-requisiti-accesso/main?set_language=it"
MANIFESTO = "https://www.uniud.it/it/didattica/segreteria-studenti/manifesto-degli-studi/scienze-matematiche-informatiche-multimediali-fisiche"
INTL_NOTICE = "https://www.uniud.it/en/uniud-international/International_Students/ammissione-non-ue/prima-arrivo-ue/documentazione/manifesto-aggiuntivo-extra-ue_eng.pdf"
INTL_GUIDANCE = "https://www.uniud.it/en/uniud-international/International_Students/ammissione-non-ue/prima-arrivo-ue/iscrizioni-con-titolo-di-studio-estero"
FEES = "https://www.uniud.it/it/didattica/area-servizi-studenti/servizi-studenti/diritto-allo-studio/tasse_merito/tasse-riduzioni-esoneri/allegati/avviso_aggiuntivo_2026-27"
FEES_INTERNATIONAL = "https://www.uniud.it/en/uniud-international/International_Students/ammissione-non-ue/prima-arrivo-ue/informazioni-utili?set_language=en"
ARDIS = "https://ardis.fvg.it/contenuti.php?id=268&view=page"
ARDIS_NEWS = "https://www.ardis.fvg.it/contenuti.php?id=11366&tipo=archivio&view=news"


def source(sid, title, url, cycle, evidence, supports, kind="Official university page"):
    return {"id": sid, "university_id": "udine", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


SOURCES = [
    source("SRC-UDINE-CS-PROFILE-2026", "Computer Science MSc course profile", PROFILE, "2026-2027",
           "Official profile identifies Computer Science as an unrestricted-access, two-year 120-credit LM-18 Master's degree in Udine. The language of instruction is Italian. This is course identity and 2026/27 context, not confirmation of a 2027/28 first-year intake.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language"]),
    source("SRC-UDINE-CS-REQ-2026", "Computer Science course admission requirements", REQUIREMENTS, "2026-2027",
           "Applicants need a suitable three-year degree. Curricular eligibility is an L-31 or L-8 degree (or former classes 26 or 9), or at least 24 CFU in relevant computer-science and mathematics subjects. A committee checks preparation and English at approximately B2; an interview or test may be required, except the page exempts graduates with at least 90/110. Listed 2026 dates are 9 July–5 October, with a justified-motives extension to 30 April 2027.",
           ["program.previous_cycle_program_requirements", "program.previous_cycle_application_windows", "program.previous_cycle_language_requirements"]),
    source("SRC-UDINE-SCIENCE-MANIFESTO-2026", "Mathematics, Computer Science and Physics study prospectus 2026/27", MANIFESTO, "2026-2027",
           "The official faculty prospectus lists Informatica LM-18 among active Master's courses and explicitly says it is taught in Italian. It gives course-specific admission rules and dates; its 2027/28 offering is not established.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_language", "program.previous_cycle_application_windows"], "Official study prospectus PDF"),
    source("SRC-UDINE-FOREIGN-QUALIFICATIONS-2026", "Additional Notice for applicants with foreign qualifications 2026/27", INTL_NOTICE, "2026-2027",
           "For second-cycle courses taught in Italian or English, non-EU residents and/or holders of foreign qualifications used Elix-Forms pre-evaluation from 1 February to 31 May 2026, with a non-refundable €20 fee and academic review within 30 working days. Successful applicants then used Universitaly; the 2026/27 pre-enrolment deadline was 30 June 2026. Applicants to Italian-taught courses needed Italian B2. These are closed prior-cycle terms only.",
           ["program.previous_cycle_international_admission", "program.previous_cycle_application_windows", "program.previous_cycle_application_fee", "program.previous_cycle_language_requirements", "university.previous_cycle_non_eu_process"], "Official international admissions notice PDF"),
    source("SRC-UDINE-INTERNATIONAL-GUIDANCE", "Admission requirements for applicants with foreign qualifications", INTL_GUIDANCE, "general",
           "The University directs foreign-degree Master's applicants to the Additional Notice for the relevant academic year, its annual prospectus and the course's own requirements. The page specifies the Additional Notice available at review as 2026/27 and gives the Elix-Forms assessment dates for that cycle; it does not publish 2027/28 course deadlines.",
           ["university.general_admissions", "university.non_eu_process", "program.previous_cycle_international_admission"]),
    source("SRC-UDINE-FEES-2026", "Additional Notice on tuition, contributions and exemptions 2026/27", FEES, "2026-2027",
           "The 2026/27 notice sets the annual university contribution from €0 to €2,000, stamp duty €16 and regional tax €120–€160, subject to conditions and exemptions; payment is normally in three instalments. It is a prior-cycle framework, not a 2027/28 quote.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition", "university.fee_conditions"], "Official tuition regulation PDF"),
    source("SRC-UDINE-FEES-INTERNATIONAL-2026", "Useful information for international students: fees and benefits", FEES_INTERNATIONAL, "2026-2027",
           "The international-student page reports 2026/27 fees between €16 and €2,076 and three instalments. The University's separate tuition page reports €16–€2,026, and its 2026/27 Additional Notice gives conditional components rather than that same range. The published totals differ; retain the discrepancy and do not choose a single total.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition", "university.fee_conditions"]),
    source("SRC-UDINE-ARDIS-2026", "ARDiS Unified Call for regional student benefits 2026/27", ARDIS, "2026-2027",
           "The call covers eligible students at Udine and Trieste. It requires enrollment plus economic and merit eligibility; foreign households use ISEE parificato. The 2026/27 ISEE and ISPE ceilings were €28,339.88 and €61,608.48. Awards and housing are competitive annual benefits, not guaranteed course-specific grants.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarships", "university.regional_aid"], "Official regional scholarship call"),
    source("SRC-UDINE-ARDIS-DEADLINES-2026", "ARDiS 2026/27 application opening and deadlines", ARDIS_NEWS, "2026-2027",
           "Online regional-benefit applications opened 15 July 2026. The scholarship deadline was 17 September at 13:00; new-student housing applications closed 27 August at 13:00. These are closed prior-cycle dates only.",
           ["university.previous_cycle_scholarship_windows", "program.previous_cycle_scholarships"], "Official regional scholarship notice"),
]

BATCH = {
    "id": "udine-computer-science-identity-and-international-admissions-review",
    "status": "partial",
    "result": "Reviewed Udine's sole legacy lead against the official 2026/27 profile, faculty prospectus, course admission rules and international qualification notice. Corrected the course language from English to Italian. The official profile identifies an unrestricted-access, two-year, 120-credit LM-18 MSc in Udine; admission requires an eligible degree or 24 relevant CFU, committee assessment, and approximately B2 English. Foreign-degree applicants had a separate 2026/27 Elix-Forms process (€20; 1 February–31 May) and Universitaly route (30 June outer deadline). The latest available course and foreign-qualification notices reviewed are 2026/27; no 2027/28 first-year call or program terms were confirmed. Official tuition totals conflict across pages and remain unresolved. ARDiS 2026/27 aid is recorded as historical competitive regional support only.",
}

REPORT = "Udine's official 2026/27 Computer Science profile identifies an unrestricted-access two-year, 120-credit LM-18 MSc in Udine taught in Italian; the old English-language tracker label was incorrect. Applicants needed an L-31/L-8 (or former 26/9) degree or at least 24 relevant computing and mathematics credits. The course committee reviews preparation and English at approximately B2 and can require a test or interview; the course page exempts graduates with at least 90/110. Non-EU residents and/or foreign-degree holders followed the 2026/27 Elix-Forms assessment process (1 February–31 May, €20), then Universitaly, with 30 June 2026 as the prior-cycle visa pre-enrolment deadline. This differs from the course's separate 5 October 2026 enrolment deadline and justified-motives extension to 30 April 2027. The 2026/27 additional tuition notice lists contribution and fixed-charge components; the international student page reports a different total fee ceiling. The discrepancy is preserved. ARDiS scholarships and housing were competitive 2026/27 regional benefits. No 2027/28 Computer Science first-year offer, application call, fee schedule or scholarship call was identified."


def apply(universities, programs, fact):
    uni = next(u for u in universities if u["id"] == "udine")
    uni.update(application_portal_url="https://uniud.esse3.cineca.it/",
               international_admissions_url=INTL_GUIDANCE,
               contact_email="studenti@uniud.it",
               contact_url=INTL_GUIDANCE,
               cycle_status="REQUIRES_VERIFICATION", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    if "University of Udine" not in uni["aliases"]:
        uni["aliases"].append("University of Udine")
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    fee_sources = ["SRC-UDINE-FEES-2026", "SRC-UDINE-FEES-INTERNATIONAL-2026"]
    aid_sources = ["SRC-UDINE-ARDIS-2026", "SRC-UDINE-ARDIS-DEADLINES-2026"]
    prior_fees = fact({"academic_year": "2026/27", "additional_notice_components": {
                           "annual_university_contribution_eur": {"minimum": 0, "maximum": 2000},
                           "regional_tax_eur": {"minimum": 120, "maximum": 160}, "stamp_duty_eur": 16,
                           "installments": 3},
                       "published_total_ranges": [
                           {"source": "international-student guidance", "minimum_eur": 16, "maximum_eur": 2076},
                           {"source": "general tuition page", "minimum_eur": 16, "maximum_eur": 2026}],
                       "resolution": "Official totals differ; do not treat either as a verified individual amount."},
                      "CONFLICTING_SOURCES", fee_sources,
                      "Prior-cycle 2026/27 information only. The published total ceilings differ and depend on conditions; confirm the current schedule with the University.")
    aid = fact({"academic_year": "2026/27", "agency": "ARDiS FVG", "scholarship_window": {"start": "2026-07-15", "deadline": "2026-09-17 13:00"},
                "first_year_housing_deadline": "2026-08-27 13:00", "ISEE_ceiling_eur": 28339.88,
                "ISPE_ceiling_eur": 61608.48,
                "standard_gross_awards_eur": {"off_site": 7171.11, "commuter": 4190.71, "on_site": 2890.16},
                "conditions": "Competitive; income, merit, enrollment and housing rules apply; foreign household ISEE parificato required where applicable."},
               "CONFIRMED", aid_sources,
               "Closed 2026/27 regional competition only. Gross amounts and housing depend on ranking and individual eligibility; no 2027/28 aid is inferred.")
    uni["cycle_facts"] = {
        "application_windows": fact(None, "REQUIRES_VERIFICATION", ["SRC-UDINE-APPLY", "SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "No Computer Science-specific 2027/28 application dates were identified; 2026/27 foreign-degree dates are historical only."),
        "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "The €20 Elix-Forms fee belongs to the 2026/27 foreign-degree pre-evaluation process; no 2027/28 fee is confirmed."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", fee_sources, "No 2027/28 tuition schedule or individual amount was identified."),
        "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", aid_sources, "The reviewed regional competition is 2026/27; no 2027/28 call or award is confirmed."),
        "previous_cycle_tuition": prior_fees,
        "previous_cycle_scholarships": aid,
        "general_foreign_qualification_route": fact({"academic_year": "2026/27", "master_pre_evaluation": "Elix-Forms; course academic committee review", "next_step": "Universitaly pre-enrolment for visa applicants, followed by university assessment and enrolment", "prospective_international_contact": "studenti@uniud.it", "tuition_contact": "dirittoallostudio@uniud.it"}, "CONFIRMED", ["SRC-UDINE-FOREIGN-QUALIFICATIONS-2026", "SRC-UDINE-INTERNATIONAL-GUIDANCE"], "General 2026/27 foreign-qualification process only; follow the next annual notice for current dates and documents."),
    }

    p = next(p for p in programs if p["id"] == "legacy-093")
    p.update(program="Computer Science", city="Udine", overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
    sources = ["SRC-UDINE-CS-PROFILE-2026", "SRC-UDINE-CS-REQ-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026",
               "SRC-UDINE-FOREIGN-QUALIFICATIONS-2026", "SRC-UDINE-INTERNATIONAL-GUIDANCE",
               "SRC-UDINE-APPLY", "SRC-UDINE-FEES-2026", "SRC-UDINE-FEES-INTERNATIONAL-2026",
               "SRC-UDINE-ARDIS-2026", "SRC-UDINE-ARDIS-DEADLINES-2026"]
    p["source_ids"] = sources
    for key, value in (("level", "MSc"), ("language", "Italian"), ("field", "Computer Science")):
        p[key] = fact(value, "REQUIRES_VERIFICATION", ["SRC-UDINE-CS-PROFILE-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026"], "Verified for the 2026/27 course only; confirm the 2027/28 listing and delivery language.")
    p["previous_cycle_tags"] = {"level": "MSc", "language": "Italian", "field": "Computer Science", "cycle": "2026-2027", "label": "Official 2026/27 profile; new 2027/28 intake remains unverified"}
    p["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-UDINE-APPLY", "SRC-UDINE-CS-PROFILE-2026", "SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "The reviewed official course and foreign-degree notices cover 2026/27. No 2027/28 first-year offer was located; no discontinuation is inferred.")
    p["facts"] = {
        "previous_cycle_course_listing": fact({"academic_year": "2026/27", "official_name": "Informatica / Computer Science", "degree_class": "LM-18", "level": "MSc", "duration_years": 2, "ects": 120, "campus": "Udine", "language": "Italian", "access": "Unrestricted; curricular and preparation checks apply"}, "CONFIRMED", ["SRC-UDINE-CS-PROFILE-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026"], "Official 2026/27 listing only; not a 2027/28 new-entry confirmation."),
        "previous_cycle_program_requirements": fact({"academic_year": "2026/27", "qualification": "Suitable three-year degree or equivalent foreign qualification", "curricular_routes": ["L-31 or L-8 degree; former classes 26 or 9", "At least 24 CFU in relevant computer-science and mathematics subjects"], "personal_preparation": "Committee reviews academic background; may require a test or interview", "exemption": "Course page exempts graduates with final mark at least 90/110", "foreign_degree_assessment": "Individual academic committee review"}, "CONFIRMED", ["SRC-UDINE-CS-REQ-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026"], "Prior-cycle course criteria; new annual regulations control 2027/28."),
        "previous_cycle_language_requirements": fact({"academic_year": "2026/27", "instruction_language": "Italian", "course_admission_assessment": "English ability equivalent to B2 assessed by the course committee", "non_EU_foreign_degree_visa_applicants": "B2 Italian certification for Italian-taught degree, subject to listed exemptions"}, "CONFIRMED", ["SRC-UDINE-CS-REQ-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026", "SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "Keep the course's academic English assessment distinct from the Italian-language certification required for relevant foreign visa applicants; all terms are 2026/27 evidence."),
        "previous_cycle_application_windows": fact({"academic_year": "2026/27", "course_enrollment_start": "2026-07-09", "course_enrollment_deadline": "2026-10-05 12:00", "justified_extension_deadline": "2027-04-30 12:00", "foreign_degree_pre_evaluation": {"platform": "Elix-Forms", "start": "2026-02-01", "deadline": "2026-05-31"}, "visa_pre_enrollment_deadline": "2026-06-30"}, "CONFIRMED", ["SRC-UDINE-CS-REQ-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026", "SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "All dates belong to 2026/27. The foreign-degree pre-evaluation, Universitaly visa step and later course enrollment are separate stages."),
        "previous_cycle_application_fee": fact({"academic_year": "2026/27", "amount_eur": 20, "platform": "Elix-Forms", "scope": "Non-refundable foreign-degree pre-evaluation fee"}, "CONFIRMED", ["SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "Prior-cycle foreign-degree assessment fee only; no 2027/28 application fee is confirmed."),
        "previous_cycle_international_admission": fact({"academic_year": "2026/27", "steps": ["Elix-Forms foreign qualification pre-evaluation with degree, transcript, syllabi, passport, CV and language evidence", "Academic committee review; outcome within 30 working days", "Universitaly pre-enrolment and visa procedure for applicants requiring a study visa", "Course admission requirements and student enrollment"], "foreign_qualification_recognition": "CIMEA statements or Declaration of Value as required by the annual notice"}, "CONFIRMED", ["SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "University-wide 2026/27 procedure; the relevant annual notice governs current details and the consulate decides visa issuance."),
        "application_windows": fact(None, "REQUIRES_VERIFICATION", ["SRC-UDINE-APPLY", "SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "No 2027/28 Computer Science course call or dates were identified; the prospectus and international procedure are annual."),
        "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-UDINE-FOREIGN-QUALIFICATIONS-2026"], "The historical €20 foreign-degree fee is not carried forward."),
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-UDINE-CS-REQ-2026", "SRC-UDINE-SCIENCE-MANIFESTO-2026"], "Current course rules reviewed are for 2026/27; 2027/28 requirements remain unverified."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", fee_sources, "No 2027/28 tuition schedule or candidate-specific total was identified."),
        "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", aid_sources, "The reviewed ARDiS call covers 2026/27 only; no 2027/28 scholarship call was confirmed."),
        "previous_cycle_tuition": prior_fees,
        "previous_cycle_scholarships": aid,
        "acceptance_rate": fact(None, "UNAVAILABLE", ["SRC-UDINE-CS-PROFILE-2026", "SRC-UDINE-CS-REQ-2026"], "Official profile and admission guidance do not publish a comparable applicant denominator and admitted count; no acceptance rate is inferred from unrestricted access."),
    }
