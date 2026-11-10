"""Roma Tre research checked 10 November 2026.

The generic Engineering lead has no unique official course match.  University
procedures and annual context are recorded without assigning a different degree.
"""

CHECKED = "2026-11-10"
PORTAL = "https://gomp.uniroma3.it/"
INTERNATIONAL = "https://www.uniroma3.it/int/education/international-students/"
CONTACT = "https://www.uniroma3.it/int/education/international-students/international-students-office/"


def source(sid, title, url, cycle, evidence, supports, pdf=False):
    return {"id": sid, "university_id": "roma-tre", "title": title, "url": url,
            "source_type": "Official PDF call or regulation" if pdf else "Official university page",
            "accessed_at": CHECKED, "cycle": cycle, "evidence": evidence, "supports": supports}


SOURCES = [
    source("SRC-ROMATRE-MSC-CATALOGUE-2026", "Corsi di laurea magistrale – A.A. 2026/2027",
           "https://www.uniroma3.it/didattica/lauree-ws-lm/", "2026-2027",
           "Annual inventory lists eleven distinct Engineering MSc degrees across two departments; no unique degree named only Engineering is identified. The list and linked admission calls concern 2026/27.",
           ["university.previous_cycle_master_inventory", "program.identity_review"]),
    source("SRC-ROMATRE-BSC-CATALOGUE-2026", "Corsi di laurea – A.A. 2026/2027",
           "https://www.uniroma3.it/didattica/lauree-ws-l/", "2026-2027",
           "Bachelor inventory and admission links explicitly cover 2026/27. Includes Computer and Artificial Intelligence Engineering L-8 with restricted local access; BSc procedures are separate from the generic MSc lead.",
           ["university.previous_cycle_bachelor_inventory", "university.previous_cycle_bachelor_admissions"]),
    source("SRC-ROMATRE-ENGLISH-INVENTORY", "Offerta formativa in lingua inglese e doppi titoli",
           "https://www.uniroma3.it/internazionale/studiare-a-roma-tre/corsi-in-inglese/", "general",
           "Undated central list includes Sustainable Coastal and Ocean Engineering and Biomedical Engineering as entire English degrees, and Applied Artificial Intelligence / Wireless Technologies as English curricula within Telecommunications Engineering. English-course evidence does not identify the generic legacy Engineering MSc.",
           ["university.general_english_offer", "program.identity_review"]),
    source("SRC-ROMATRE-SCOE-PROFILE-2026", "Sustainable Coastal and Ocean Engineering LM-23",
           "https://www.uniroma3.it/didattica/lauree-ws-lm/sustainable-coastal-and-ocean-engineering-lm-23/", "2026-2027",
           "Profile identifies a separate English-taught, two-year/120-CFU, open-access LM-23 degree at Ostia, with 16 November 2026 enrollment deadline. This is one possible Engineering degree, not an established match to legacy-096.",
           ["university.previous_cycle_english_course_examples", "program.identity_review"]),
    source("SRC-ROMATRE-BIOMED-PROFILE-2026", "Biomedical Engineering LM-21",
           "https://www.uniroma3.it/didattica/lauree-ws-lm/biomedical-engineering-lm-21/", "2026-2027",
           "Profile identifies a separate English-taught, two-year/120-CFU, open-access LM-21 degree in Rome. Annual dates are 15 September 2026 for assessment (supplementary 15 December), 16 November enrollment and 31 March 2027 conditional enrollment. No match to the generic legacy lead is established.",
           ["university.previous_cycle_english_course_examples", "program.identity_review"]),
    source("SRC-ROMATRE-AEROSPACE-PROFILE-2026", "Ingegneria Aerospaziale LM-20",
           "https://www.uniroma3.it/didattica/lauree-ws-l/ingegneria-aerospaziale-lm-20/", "2026-2027",
           "Central profile labels the two-year/120-CFU Aerospace MSc language Italian/English. This differs from the department's English-course list; exact English-only pathway needs verification and no generic lead is assigned to it.",
           ["university.previous_cycle_english_course_examples", "program.identity_review"]),
    source("SRC-ROMATRE-ENGINEERING-ENGLISH", "Corsi in lingua straniera – Engineering department",
           "https://ingegneriacivileinformaticatecnologieaeronautiche.uniroma3.it/en/didattica/corsi-in-lingua-straniera/", "general",
           "Department page dated 1 September 2026 describes Sustainable Coastal and Ocean Engineering and Aerospace Engineering MSc courses as offered in English; central Aerospace profile instead says Italian/English.",
           ["university.general_english_offer", "university.language_source_discrepancy"]),
    source("SRC-ROMATRE-INTERNATIONAL-CURRENT", "International Students – current central guidance",
           INTERNATIONAL, "mixed",
           "Current page links 2026/27 course calls and a national circular valid for 2026/27 and 2027/28. Its own Universitaly deadline is explicitly 15 September 2026; university pre-enrollment approval does not guarantee a consular visa.",
           ["university.general_admissions", "university.previous_cycle_international_deadline", "university.non_eu_process"]),
    source("SRC-ROMATRE-FOREIGN-GUIDE-2026", "How to apply – students with foreign qualifications 2026/27",
           "https://www.uniroma3.it/int/wp-content/uploads/file_locked/2026/06/GUIDE-HOW-TO-APPLY-ENG-2026-27.pdf", "2026-2027",
           "Prior-cycle guide requires at least 12 school years for bachelor entry and a relevant first-cycle degree for MSc entry. GOMP assessment uses degree/transcript and detailed syllabi, translation/authenticity evidence as applicable; visa applicants also use Universitaly, then original-document verification. The introduction retains an outdated 2025/26 national-reference line.",
           ["university.previous_cycle_foreign_qualification_route", "university.previous_cycle_bachelor_requirements", "university.previous_cycle_master_requirements"], True),
    source("SRC-ROMATRE-MSC-CALL-2026", "Bando Lauree Magistrali 2026/27 – Engineering sections",
           "https://www.uniroma3.it/wp-content/uploads/file_locked/2026/06/Bando_Lauree_magistrali_2026-27.pdf", "2026-2027",
           "Engineering sections require a suitable first-cycle/equivalent degree, course-regulation curricular requirements and prior-career assessment. B2 English is stated for Sustainable Coastal/Ocean, Aerospace and Biomedical. The annual call distinguishes a 70-euro Italian language test and a 60-euro supplementary assessment surcharge; neither establishes a generic 2027/28 application fee.",
           ["university.previous_cycle_master_admissions", "university.previous_cycle_language_requirements", "university.previous_cycle_test_and_late_fees"], True),
    source("SRC-ROMATRE-NATIONAL-CIRCULAR-2026-2028", "National international-student procedures 2026/27 and 2027/28",
           "https://universitaly-private.cineca.it/uploads/universitaly-pubblico/Circolare_2026-2027_studenti_internazionali.pdf", "2026-2027;2027-2028",
           "Circular has explicit biennial validity. For degree courses the 2027/28 national visa-application outer deadline is 31 October 2027; universities may set earlier dates. Visa pre-enrollment uses Universitaly. Non-Italian courses require certification of their teaching language rather than an Italian test; visa-stage non-native language evidence must cover four skills at least at B2. This does not confirm any Roma Tre course intake.",
           ["university.national_visa_framework_2027_2028", "university.national_language_framework_2027_2028"], True),
    source("SRC-ROMATRE-FEES-2026", "Tasse e contributi universitari",
           "https://portalestudente.uniroma3.it/tasse/tasse/", "2026-2027",
           "Page states 2026/27 regional tax of 140 euros plus 16-euro stamp duty, with a separate income/course-dependent annual university contribution. One to four installments depend on the fee band; first-year payment deadlines come from the admission call. The fixed 156 euros is not normal total tuition.",
           ["university.previous_cycle_tuition", "university.fee_conditions"]),
    source("SRC-ROMATRE-FEE-REGULATION-2026", "Regolamento Tasse – DR 70/2026",
           "https://portalestudente.uniroma3.it/wp-content/uploads/sites/2/file_locked/2026/01/Regolamento-tasse-DR-70_2026.pdf", "general",
           "Current regulation applies from 2025/26 and was updated in January 2026. Contribution and exemptions depend on ISEE, course and career conditions; the foreign-income route uses ISEE Parificato through the agreed CAF. Its general continuing rules are not a dedicated 2027/28 annual fee schedule.",
           ["university.general_fee_framework", "university.general_foreign_income_fees"], True),
    source("SRC-ROMATRE-ISEE-2026", "Presentazione ISEE",
           "https://portalestudente.uniroma3.it/tasse/presentazione-isee/", "2026-2027",
           "2026/27 first-year students have 60 days from enrollment to present ISEE. Missing ISEE normally means the highest contribution bracket. Eligible foreign-income/nonresident households use the Personal CAF/CAF CISL process; even DiSCo winners with foreign income must submit the required declaration.",
           ["university.previous_cycle_fee_reductions", "university.previous_cycle_foreign_income_fees"]),
    source("SRC-ROMATRE-DISCO-CALL-2026", "DiSCo – 2026/27 right-to-study competition announcement",
           "https://laziodisco.it/on-line-il-bando-diritto-allo-studio-2026-2027/", "2026-2027",
           "Regional provider's 10 June 2026 announcement covers students at Lazio institutions and scholarships, accommodation, meals and other benefits. Application first phase ran 10 June–22 July 2026 at noon; enrollment could be completed by 10 February 2027. This is the prior-cycle competition, not a 2027/28 award call.",
           ["university.previous_cycle_scholarships", "university.previous_cycle_scholarship_windows"]),
    source("SRC-ROMATRE-DISCO-ELIGIBILITY-2026", "DiSCo – Bando Diritto allo Studio 2026/27",
           "https://laziodisco.it/wp-content/uploads/2026/06/BANDO-DIRITTO-ALLO-STUDIO-26-27-1.pdf", "2026-2027",
           "Official indexed call extract states scholarship ISEE/ISEEUP ceiling 28,339.88 euros and ISPE/ISPEUP ceiling 61,608.48 euros; exceeding either excludes the applicant. Full PDF retrieval returned HTTP 403 in this review, so detailed awards and documentation were not exhaustively verified.",
           ["university.previous_cycle_scholarship_eligibility"], True),
    source("SRC-ROMATRE-CONTACT-CURRENT", "International Students Office – contact details",
           CONTACT, "general",
           "Current International Students Office supports foreign-qualification pre-enrollment, admission and enrollment. Relevant email is international.admissions@uniroma3.it; address Via Ostiense 133, Tower B, 00154 Rome. This supersedes the older orientation page's foreign-qualification email/address for current contact purposes.",
           ["university.contact"]),
    source("SRC-ROMATRE-UNICORE-2026-COHORT", "UNICORE 8.0 – two refugee scholarships for 2026/27 entrants",
           "https://apps.uniroma3.it/ateneo/memo/files/pub_allegato_27f76020-905f-42b6-9c25-f6cb5e3f49e3.pdf", "2026-2027",
           "Closed refugee-only call admitted two 2026/27 MSc entrants; support extends to 2027/28 subject to renewal. Applications ran 2 March–17 April 2026 noon UTC+2. Benefits include fee exemption, housing and meals. Renewal needs 25 CFU by 10 August 2027. This is not a new 2027/28 entrant competition.",
           ["university.previous_cycle_targeted_scholarships", "university.previous_cohort_2027_2028_continuation"], True),
]

BATCH = {
    "id": "roma-tre-engineering-identity-and-admissions-review", "status": "partial",
    "result": "Reviewed the sole Roma Tre candidate legacy-096 without assigning its generic Engineering MSc label to a different degree. Recorded 2026/27 bachelor/master inventories, distinct English Engineering course examples and an Aerospace language discrepancy; GOMP/Universitaly and qualification routes, fees, DiSCo and current contacts. Confirmed the national circular's 2027/28 framework and 31 October 2027 outer visa deadline only. A closed UNICORE call supports the 2026/27 refugee cohort into 2027/28. No 2027/28 Roma Tre first-year degree-specific offer, admission window, annual tuition schedule or new-entrant scholarship call was identified."
}

REPORT = "Roma Tre's legacy Engineering MSc remains an unresolved course identity: the official 2026/27 catalogue lists multiple distinct Engineering degrees, including English Sustainable Coastal and Ocean Engineering and Biomedical Engineering. The generic candidate is preserved without a speculative match. GOMP handles university procedures and Universitaly handles visa pre-enrollment. The national circular covers 2027/28 and sets an outer visa-application deadline of 31 October 2027, subject to earlier university dates; Roma Tre's displayed 15 September 2026 deadline belongs to 2026/27. Tuition remains income/course-dependent, with prior-cycle fixed charges of 140 euros regional tax plus 16 euros stamp duty. DiSCo's reviewed competition is 2026/27; closed UNICORE awards support the 2026/27 refugee cohort through 2027/28 under renewal conditions. Current foreign-qualification contact is international.admissions@uniroma3.it. No 2027/28 first-year course-specific intake, annual tuition schedule or new-entrant scholarship call was identified."


def apply(universities, programs, fact):
    uni = next(u for u in universities if u["id"] == "roma-tre")
    uni.update(application_portal_url=PORTAL, international_admissions_url=INTERNATIONAL,
               contact_email="international.admissions@uniroma3.it", contact_url=CONTACT,
               cycle_status="REQUIRES_VERIFICATION", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    if "Roma Tre University" not in uni["aliases"]:
        uni["aliases"].append("Roma Tre University")
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    catalogue = "SRC-ROMATRE-MSC-CATALOGUE-2026"
    guide = "SRC-ROMATRE-FOREIGN-GUIDE-2026"
    call = "SRC-ROMATRE-MSC-CALL-2026"
    international = "SRC-ROMATRE-INTERNATIONAL-CURRENT"
    circular = "SRC-ROMATRE-NATIONAL-CIRCULAR-2026-2028"
    identity_sources = [catalogue, "SRC-ROMATRE-ENGLISH-INVENTORY", "SRC-ROMATRE-SCOE-PROFILE-2026",
                        "SRC-ROMATRE-BIOMED-PROFILE-2026"]
    fee_sources = ["SRC-ROMATRE-FEES-2026", "SRC-ROMATRE-FEE-REGULATION-2026", "SRC-ROMATRE-ISEE-2026"]
    aid_sources = ["SRC-ROMATRE-DISCO-CALL-2026", "SRC-ROMATRE-DISCO-ELIGIBILITY-2026"]
    identity = fact(None, "REQUIRES_VERIFICATION", identity_sources,
                    "The legacy label Engineering MSc is generic. Multiple official degrees fit that field and more than one is English taught; no unique course match or replacement is justified.")
    pending_windows = fact(None, "REQUIRES_VERIFICATION", [catalogue, international, call],
                           "No Roma Tre 2027/28 course application window identified. September/November/December 2026 and conditional March 2027 dates belong to 2026/27. The national visa outer deadline is a separate framework fact.")
    pending_fee = fact(None, "REQUIRES_VERIFICATION", [call],
                       "No 2027/28 application fee identified. The prior call's 70-euro Italian test and 60-euro late-assessment surcharge are conditional charges, not a generic application price.")
    pending_tuition = fact(None, "REQUIRES_VERIFICATION", fee_sources,
                           "No dedicated 2027/28 annual tuition schedule identified. The existing fee regulation supplies general context, and the specific course identity is unresolved.")
    pending_aid = fact(None, "REQUIRES_VERIFICATION", aid_sources + ["SRC-ROMATRE-UNICORE-2026-COHORT"],
                       "No scholarship call for new 2027/28 entrants identified. DiSCo is 2026/27; the closed UNICORE 8.0 call funds 2026/27 refugee entrants with conditional continuation into 2027/28.")
    prior_tuition = fact({"academic_year": "2026/27", "regional_tax_eur": 140,
                          "stamp_duty_eur": 16, "fixed_charges_total_eur": 156,
                          "university_contribution": "Additional amount depends on course, ISEE and career/exemption conditions",
                          "installments": "One to four depending on fee band; first-year deadlines follow the admission call",
                          "foreign_income": "ISEE Parificato via the agreed CAF route where applicable",
                          "first_year_ISEE_deadline": "60 days from enrollment under the 2026/27 page",
                          "missing_ISEE": "Normally highest contribution bracket"},
                         "CONFIRMED", fee_sources,
                         "Prior-cycle amounts and current general fee context only. The 156-euro fixed component is not total annual tuition; no course-specific maximum is assigned to the unidentified lead.")
    prior_aid = fact({"academic_year": "2026/27", "provider": "DiSCo Lazio",
                      "benefits": "Competitive scholarship, accommodation, meals and other annual benefits",
                      "application_start": "2026-06-10", "application_deadline": "2026-07-22 12:00 Italy time",
                      "enrollment_completion_deadline": "2027-02-10", "ISEE_or_ISEEUP_ceiling_eur": 28339.88,
                      "ISPE_or_ISPEUP_ceiling_eur": 61608.48,
                      "eligibility": "Income/assets, merit and other annual call conditions; both economic ceilings must be met",
                      "award_amount": "Not exhaustively verified in this review"},
                     "CONFIRMED", aid_sources,
                     "Closed prior-cycle first-phase application window only. Official indexed call extract supports thresholds; full PDF retrieval was denied (403), so detailed awards/documentation remain unverified.")
    national = fact({"valid_academic_years": ["2026/27", "2027/28"],
                     "visa_pre_enrollment_portal": "https://www.universitaly.it/",
                     "2027_2028_national_visa_application_outer_deadline": "2027-10-31",
                     "university_dates": "Universities may require earlier dates for individual courses",
                     "language": "Italian B2 assessment or exemption for Italian courses; other-language courses require suitable teaching-language certification, with visa-stage non-native evidence at least B2 in all four skills"},
                    "CONFIRMED", [circular],
                    "National framework is explicitly valid for 2027/28. This is not a Roma Tre admission deadline, course offer or visa guarantee; the circular permits later national updates.")
    unicore = fact({"entry_academic_year": "2026/27", "support_years": ["2026/27", "2027/28"],
                    "awards": 2, "eligible_group": "Recognized refugees resident in the thirteen countries listed in the call; valid relevant degree, academic and English requirements also apply",
                    "application_start": "2026-03-02", "application_deadline": "2026-04-17 12:00 UTC+2",
                    "benefits": "University fee exemption, regional-tax/stamp support, accommodation and meals; scholarship and other benefits under the call",
                    "2027_2028_continuation": "At least 25 CFU by 10 August 2027 and continued eligibility",
                    "contact_email": "unicore@uniroma3.it"},
                   "CONFIRMED", ["SRC-ROMATRE-UNICORE-2026-COHORT"],
                   "Closed targeted 2026-entry call. Its 2027/28 reference is second-year continuation, not a new 2027/28 first-year offer or scholarship application window.")
    prior_route = fact({"academic_year": "2026/27", "university_portal": PORTAL,
                        "bachelor_entry": "Eligible school qualification after at least 12 school years, with compensatory study evidence where applicable",
                        "master_entry": "Relevant first-cycle/equivalent degree; departmental prior-career assessment and course curricular requirements",
                        "documents": "Qualification, transcript and detailed syllabi; required translations and authenticity/recognition evidence (CIMEA, legalization/apostille or accepted DoV route as applicable)",
                        "visa_applicants": "Also pre-enroll on Universitaly; the same qualification documents are uploaded on both platforms",
                        "Universitaly_university_deadline": "2026-09-15",
                        "final_enrollment": "Departmental approval, university document checks and original-document verification",
                        "visa_decision": "Italian diplomatic-consular representation; university validation does not guarantee issuance"},
                       "CONFIRMED", [guide, call, international],
                       "University operational guidance reviewed is for 2026/27. Exact 2027/28 course admission requirements, dates and documentation remain pending; course-language and exemption rules must be checked against the applicable call and national circular.")
    examples = fact({"academic_year": "2026/27",
                     "separate_English_MSc_examples": [
                         {"name": "Sustainable Coastal and Ocean Engineering", "degree_class": "LM-23", "duration_years": 2, "credits": 120, "location": "Ostia, Rome"},
                         {"name": "Biomedical Engineering", "degree_class": "LM-21", "duration_years": 2, "credits": 120, "location": "Rome"}],
                     "Aerospace_language_discrepancy": "Central profile says Italian/English; departmental English-course list says English"},
                    "CONFIRMED", identity_sources + ["SRC-ROMATRE-AEROSPACE-PROFILE-2026", "SRC-ROMATRE-ENGINEERING-ENGLISH"],
                    "Discovery and identity-review context only. These are distinct degrees; none is assigned to the generic legacy-096 candidate and no 2027/28 intake is inferred.")
    uni["cycle_facts"] = {
        "application_windows": pending_windows, "application_fee_2027_2028": pending_fee,
        "tuition_2027_2028": pending_tuition, "scholarships_2027_2028": pending_aid,
        "national_visa_framework_2027_2028": national,
        "previous_cycle_foreign_qualification_route": prior_route,
        "previous_cycle_english_engineering_examples": examples,
        "general_aerospace_language_source_discrepancy": fact(
            {"central_course_profile": "Italian/English", "department_English_course_list": "English"},
            "CONFLICTING_SOURCES", ["SRC-ROMATRE-AEROSPACE-PROFILE-2026", "SRC-ROMATRE-ENGINEERING-ENGLISH"],
            "Different official language descriptions need course-office clarification before an English-only Aerospace route is assigned. Aerospace has not been matched to the generic Engineering candidate."),
        "previous_cycle_tuition": prior_tuition, "previous_cycle_scholarships": prior_aid,
        "previous_cycle_targeted_UNICORE_scholarships": unicore,
        "candidate_identity_match": identity,
        "previous_cycle_bachelor_inventory": fact({"academic_year": "2026/27", "review": "Bachelor catalogue and separate annual admission-call links examined",
                                                   "computing_example": "Computer and Artificial Intelligence Engineering L-8; restricted local access"},
                                                  "CONFIRMED", ["SRC-ROMATRE-BSC-CATALOGUE-2026"],
                                                  "Prior-cycle BSc inventory only; it is not the existing MSc candidate or a 2027/28 first-year offer.")
    }
    for p in (p for p in programs if p["university_id"] == "roma-tre"):
        p.update(overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
        for key in ("level", "language", "field"):
            p[key] = fact(p[key]["value"], "REQUIRES_VERIFICATION", identity_sources,
                          "Previous tracker classification retained as an unverified lead. The generic course label has no unique official match; this is not confirmation of a particular course, language or 2027/28 offer.")
        p["previous_cycle_tags"] = None
        p["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", identity_sources + [call],
                                            "No uniquely matched course or 2027/28 first-year offer identified. Existing official course evidence is 2026/27; no discontinuation is inferred.")
        p["source_ids"] = [s["id"] for s in SOURCES]
        p["facts"] = {
            "course_identity_match": identity,
            "previous_cycle_english_engineering_examples": examples,
            "previous_cycle_university_international_admission": prior_route,
            "national_visa_framework_2027_2028": national,
            "previous_cycle_university_tuition_context": prior_tuition,
            "previous_cycle_university_scholarships": prior_aid,
            "previous_cycle_targeted_UNICORE_scholarships": unicore,
            "application_windows": pending_windows, "application_fee_2027_2028": pending_fee,
            "tuition_2027_2028": pending_tuition, "scholarships_2027_2028": pending_aid,
            "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", identity_sources + [call],
                                                             "The generic candidate needs a unique official course match before course-specific curricular credits, selection rules, language thresholds or quotas can be assigned."),
            "acceptance_rate": fact(None, "UNAVAILABLE", [catalogue, call],
                                    "No uniquely matched course or complete comparable applicant/admitted totals identified. Open access is not an acceptance-rate statistic.")
        }
