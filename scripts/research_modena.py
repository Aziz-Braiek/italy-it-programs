"""University of Modena and Reggio Emilia research reviewed 10 November 2026.

The named Computer Engineering MSc remains pending for 2027/28; reviewed course,
admission, tuition and benefit records concern the previous 2026/27 cycle.
"""

CHECKED = "2026-11-10"
PORTAL = "https://www.esse3.unimore.it/"

SOURCES = [{'id': 'SRC-UNIMORE-CATALOGUE-2026',
  'university_id': 'modena-reggio',
  'title': 'Degree Programmes – 2026/27',
  'url': 'https://www.unimore.it/en/education/degree-programmes?page=1',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Official inventory is explicitly AY 2026-2027; Computer Engineering LM-32 is an '
              'Italian-language open-access Master. No 2027/28 course offer is established.',
  'supports': ['university.previous_cycle_course_inventory',
               'program.name',
               'program.level',
               'program.language']},
 {'id': 'SRC-UNIMORE-CE-PROFILE-2026',
  'university_id': 'modena-reggio',
  'title': 'Computer Engineering MSc – course 20-362',
  'url': 'https://www.unimore.it/en/education/degree-programmes/computer-engineering-dm27004-1',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Course profile identifies a two-year, Italian-language, open-access LM-32 Master in Modena. '
              'President Francesco Guerra, francesco.guerra@unimore.it.',
  'supports': ['program.previous_cycle_course_listing',
               'program.duration',
               'program.location',
               'program.language',
               'program.contact']},
 {'id': 'SRC-UNIMORE-CE-CALL-2026',
  'university_id': 'modena-reggio',
  'title': 'Computer Engineering MSc admission call 2026/27',
  'url': 'https://www.unimore.it/sites/default/files/2026-05/BandoLMIngegneria%20Informatica%202026-2027%20def.pdf',
  'source_type': 'Official PDF call or regulation',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Assessment deadline 14 December 2026; enrollment 8 July–22 December 2026. Academic '
              'requirements, foreign-degree assessment, 10 reserved non-EU abroad places, Italian language '
              'and ESSE3/Universitaly steps are specified. The call provides no acceptance-rate denominator '
              'or specific application fee.',
  'supports': ['program.previous_cycle_requirements',
               'program.previous_cycle_application_windows',
               'program.previous_cycle_international_admission',
               'program.previous_cycle_available_places']},
 {'id': 'SRC-UNIMORE-CE-DEPARTMENT',
  'university_id': 'modena-reggio',
  'title': 'Computer Engineering – department information',
  'url': 'https://www.ingmo.unimore.it/en/education/corsi-di-laurea-magistrale-informazioni-generali/computer-engineering',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'Department describes Cloud and Cyber Security and Data Engineering and Analytics tracks since '
              '2023/24. General entry description mentions degree score at least 85/110 or foreign score '
              'above three quarters; the annual course call controls admission.',
  'supports': ['program.curricula', 'program.general_requirements']},
 {'id': 'SRC-UNIMORE-FOREIGN-QUALIFICATION',
  'university_id': 'modena-reggio',
  'title': 'Foreign study qualification',
  'url': 'https://www.unimore.it/en/internationalisation/foreign-qualification',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'Foreign qualification guidance directs open-access MSc applicants to ESSE3 academic '
              'assessment and the individual annual call; visa applicants also pre-enrol through '
              'Universitaly. Bachelor admission requires a recognized school qualification after at least 12 '
              'years. Translation/legalization and DOV/CIMEA documentation apply as required.',
  'supports': ['university.general_admissions',
               'university.non_eu_process',
               'university.bachelor_entry',
               'university.master_entry']},
 {'id': 'SRC-UNIMORE-FEES-2026',
  'university_id': 'modena-reggio',
  'title': 'Fees and benefits 2026/27',
  'url': 'https://www.unimore.it/en/services/fees-and-benefits',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'First-year initial fixed payment is €159.67, with any variable contribution charged later. '
              'Normal payments are up to four installments; first-year open-access MSc first and second '
              'installments are due 22 December 2026, then 1 March and 30 April 2027.',
  'supports': ['university.previous_cycle_tuition', 'university.previous_cycle_payment_dates']},
 {'id': 'SRC-UNIMORE-FEE-REGULATION-2026',
  'university_id': 'modena-reggio',
  'title': 'Student fee resolution – 14 May 2026',
  'url': 'https://www.unimore.it/sites/default/files/2026-06/ESTRATTO%20delibera%20tasse%202026%202027.pdf',
  'source_type': 'Official PDF call or regulation',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': '2026/27 fee resolution sets Computer Engineering MSc maximum annual fees including fixed '
              'items at €2,290 (€2,540 for the specified fuori-corso category). Fixed items total €159.67. '
              'ISEE/merit reductions and optional foreign-income country-ISEE flat tax are regulated '
              'separately.',
  'supports': ['university.previous_cycle_tuition',
               'program.previous_cycle_tuition',
               'university.fee_conditions']},
 {'id': 'SRC-UNIMORE-FLAT-TAX-2026',
  'university_id': 'modena-reggio',
  'title': 'Flat Tax Non-EU International Students',
  'url': 'https://www.unimore.it/en/services/fees-and-benefits/exemptions-and-reduction-tuition-fees/flat-tax-non-eu-international',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Optional country-based notional ISEE for non-EU students resident abroad with income and '
              'assets abroad. Applicants may instead submit translated/legalized financial documents. Links '
              'a 2026/27 country table and simulator; no 2027/28 rate is established.',
  'supports': ['university.previous_cycle_foreign_income_fees']},
 {'id': 'SRC-UNIMORE-ISEE-2026',
  'university_id': 'modena-reggio',
  'title': 'No Tax Area / ISEE reductions',
  'url': 'https://www.unimore.it/it/servizi/tasse-e-benefici/esoneri-e-riduzioni-tasse/esonero-e-riduzione-tasse-con-isee',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': '2026/27 No Tax Area and reduced contributions depend on ISEE and, after the first year, '
              'merit. First-year Master applicants apply via ER.GO by 22 December 2026 at 16:00. The fixed '
              '€159.67 remains payable for qualifying exemptions.',
  'supports': ['university.previous_cycle_fee_reductions']},
 {'id': 'SRC-UNIMORE-TOP-STUDENT-2026',
  'university_id': 'modena-reggio',
  'title': 'Top Student exemption 2026/27',
  'url': 'https://www.unimore.it/it/servizi/tasse-e-benefici/esoneri-e-riduzioni-tasse/esonero-top-student',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Conditional first-year fee exemption scheme requires top prior qualification marks; MSc '
              'applicants need 110/110. Outside Emilia-Romagna residents pay fixed €159.67 only; region '
              'residents pay €859.67 total. MSc application deadline 22 December 2026 at 16:00. '
              'Foreign-grade equivalence is not specified on this page.',
  'supports': ['university.previous_cycle_merit_benefits']},
 {'id': 'SRC-UNIMORE-ERGO-2026',
  'university_id': 'modena-reggio',
  'title': 'ER.GO 2026/27 study-benefit competition',
  'url': 'https://www.er-go.it/cosa-fare-per/bandi-di-concorso/leggi-il-bando/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf/%40%40display-file/file/bando-di-concorso-benefici-dsu-a-a-2026_2027.pdf',
  'source_type': 'Official PDF call or regulation',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Regional annual competition covers UNIMORE students. Scholarship application: 23 June–24 '
              'August 2026 16:00. Cash/services depend on income, merit and residence classification. '
              'Example lowest income band: off-site €7,171.11, commuting €4,190.71, on-site €2,890.16, '
              'including any meal-service conversion; higher ISEE reduces amounts. Foreign financial '
              'documentation is required.',
  'supports': ['university.previous_cycle_scholarships', 'university.previous_cycle_regional_aid']},
 {'id': 'SRC-UNIMORE-ERGO-THRESHOLDS-2026',
  'university_id': 'modena-reggio',
  'title': 'ER.GO economic thresholds 2026/27',
  'url': 'https://www.er-go.it/cosa-fare-per/bandi-di-concorso/soglie-economiche-per-laccesso',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Scholarship and housing economic thresholds: ISEE ≤€25,000 and ISPE ≤€50,000. Both indicators '
              'must qualify; other benefits have separate thresholds.',
  'supports': ['university.previous_cycle_scholarship_eligibility']},
 {'id': 'SRC-UNIMORE-CONTACT',
  'university_id': 'modena-reggio',
  'title': 'International Welcome Desk (Modena)',
  'url': 'https://www.unimore.it/en/services/registrar-and-student-offices/international-welcome-desk-modena-office',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'International Welcome Desk: internationalwelcomedesk@unimore.it, telephone 059 2058171, Via '
              'San Geminiano 3, Modena.',
  'supports': ['university.contact']},
 {'id': 'SRC-UNIMORE-BSC-CE-2026',
  'university_id': 'modena-reggio',
  'title': 'Computer Engineering BSc call 2026/27',
  'url': 'https://www.unimore.it/it/ateneo/bandi/bando-di-ammissione-al-corso-di-laurea-triennale-di-ingegneria-informatica-aa-20262027',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'BSc Computer Engineering has a separate 2026/27 call, published 11 March 2026. The catalogue '
              'classifies the Modena BSc as Italian and restricted access. This BSc is not the existing '
              'legacy MSc candidate.',
  'supports': ['university.previous_cycle_bachelor_admissions']}]

BATCH = {'id': 'modena-computer-engineering-course-and-admissions-review',
 'status': 'partial',
 'result': 'Matched the sole Modena-Reggio legacy candidate to the official 2026/27 Computer Engineering '
           'LM-32 MSc in Modena and corrected its language from English to Italian. Recorded prior-cycle '
           'curricular requirements, foreign-degree scoring, language rules, course assessment and '
           'enrollment dates, 10 reserved non-EU abroad places, ESSE3/Universitaly procedures, fee schedule '
           'and ER.GO/Top Student eligibility. No 2027/28 first-year offer, course call, fee schedule or '
           'scholarship call was identified; current intake and conditions remain pending.'}

REPORT = "Modena-Reggio's Computer Engineering MSc is a two-year Italian-taught LM-32 degree in Modena in the official 2026/27 catalogue. The prior-cycle call sets curriculum and readiness checks, a foreign qualification grade strictly above 75% of the maximum, an Italian test unless exempt, 10 non-EU abroad places, an ESSE3 assessment deadline of 14 December 2026 and enrollment by 22 December. The 2026/27 initial fixed payment is €159.67; the course's standard maximum annual total is €2,290 including those fixed items, with income, progress, exemption and eligible foreign-income rules. ER.GO's regional aid and the conditional Top Student fee exemption have separate eligibility and application terms. No 2027/28 first-year offer or new course, fee or scholarship call was identified, so the candidate remains pending."


def apply(universities, programs, fact):
    uni = next(u for u in universities if u["id"] == "modena-reggio")
    uni.update(application_portal_url=PORTAL,
               contact_email="internationalwelcomedesk@unimore.it",
               contact_url="https://www.unimore.it/en/services/registrar-and-student-offices/international-welcome-desk-modena-office",
               cycle_status="REQUIRES_VERIFICATION", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    for alias in ("University of Modena and Reggio Emilia", "UNIMORE"):
        if alias not in uni["aliases"]:
            uni["aliases"].append(alias)
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    for src in SOURCES:
        if src["id"] not in uni["source_ids"]:
            uni["source_ids"].append(src["id"])

    historical_tuition = fact({
        "academic_year": "2026/27",
        "first_installment_eur": 159.67,
        "fixed_components_eur": {"regional_tax": 140, "stamp_duty": 16,
                                 "accident_insurance": 1.90, "civil_liability_insurance": 1.77},
        "Computer_Engineering_MSc_maximum_annual_total_eur": 2290,
        "specified_fuori_corso_maximum_total_eur": 2540,
        "maximum_includes_fixed_components": True,
        "ordinary_installments": 4,
        "first_year_open_access_MSc_payment_dates": ["2026-12-22", "2026-12-22", "2027-03-01", "2027-04-30"],
        "reductions": "Income/ISEE, progress, exemptions and timely benefit application determine the actual contribution",
        "first_year_No_Tax_Area": "ISEE at most 30,000 euros under the regulation; first-year applicants have no merit condition",
        "income_based_reduction_ceiling_ISEE_eur": 60000,
        "foreign_income": "Eligible non-EU students with income/assets abroad may use country notional ISEE or submit complete translated/legalized financial documents",
        "first_year_MSc_fee_reduction_deadline": "2026-12-22 16:00 Italy time"
    }, "CONFIRMED", ["SRC-UNIMORE-FEES-2026", "SRC-UNIMORE-FEE-REGULATION-2026",
                     "SRC-UNIMORE-FLAT-TAX-2026", "SRC-UNIMORE-ISEE-2026"],
       "Prior-cycle framework only. The 159.67 euro first payment is not normal total annual tuition. Maximum amounts include the fixed charges; reductions and foreign-income schemes have eligibility conditions.")
    historical_scholarships = fact({
        "academic_year": "2026/27",
        "ERGO": {"provider": "ER.GO Emilia-Romagna", "application_start": "2026-06-23",
                 "application_deadline": "2026-08-24 16:00 Italy time",
                 "ISEE_ceiling_eur": 25000, "ISPE_ceiling_eur": 50000,
                 "eligibility": "Annual enrollment, economic and merit requirements; both financial indicators must qualify",
                 "benefits": "Competitive scholarship, meals and housing under the annual call",
                 "lowest_income_band_ISEE_ceiling_eur": 16666.67,
                 "example_awards_lowest_income_band_eur": {"off_site": 7171.11, "commuting": 4190.71, "on_site": 2890.16},
                 "amount_conditions": "Amounts include any meal-service conversion; higher ISEE bands have lower awards, and residence status requires the call's documentation",
                 "foreign_income": "Annual household income/assets documentation must be submitted under the call"},
        "Top_Student_fee_exemption": {"prior_degree_score_for_MSc": "110/110",
                                      "foreign_grade_equivalence": "Not specified on the reviewed page",
                                      "outside_Emilia_Romagna_resident_total_eur": 159.67,
                                      "Emilia_Romagna_resident_total_eur": 859.67,
                                      "MSc_application_deadline": "2026-12-22 16:00 Italy time",
                                      "income_requirement": "No ISEE condition; qualifying prior mark and other annual rules apply"}
    }, "CONFIRMED", ["SRC-UNIMORE-ERGO-2026", "SRC-UNIMORE-ERGO-THRESHOLDS-2026",
                     "SRC-UNIMORE-TOP-STUDENT-2026"],
       "Prior-cycle regional competition and conditional first-year fee exemptions only. Awards are subject to the annual rules; no 2027/28 award or foreign-grade conversion is inferred.")
    pending_window = fact(None, "REQUIRES_VERIFICATION", ["SRC-UNIMORE-CATALOGUE-2026", "SRC-UNIMORE-CE-CALL-2026"],
                          "No 2027/28 Computer Engineering course call or application window was identified. The 14 and 22 December 2026 deadlines belong to 2026/27.")
    pending_fee = fact(None, "REQUIRES_VERIFICATION", ["SRC-UNIMORE-CE-CALL-2026"],
                       "No 2027/28 application fee was identified. The reviewed 2026/27 course call does not state a specific assessment-application fee; no zero-fee assumption is made.")
    pending_tuition = fact(None, "REQUIRES_VERIFICATION", ["SRC-UNIMORE-FEES-2026", "SRC-UNIMORE-FEE-REGULATION-2026"],
                           "No 2027/28 tuition schedule was identified. All recorded amounts and payment dates apply to 2026/27.")
    pending_scholarships = fact(None, "REQUIRES_VERIFICATION", ["SRC-UNIMORE-ERGO-2026", "SRC-UNIMORE-TOP-STUDENT-2026"],
                                "No 2027/28 scholarship or fee-exemption call was identified. The reviewed ER.GO and Top Student schemes apply to 2026/27.")
    uni["cycle_facts"] = {
        "application_windows": pending_window,
        "application_fee_2027_2028": pending_fee,
        "tuition_2027_2028": pending_tuition,
        "scholarships_2027_2028": pending_scholarships,
        "previous_cycle_tuition": historical_tuition,
        "previous_cycle_scholarships": historical_scholarships,
        "general_foreign_qualification_route": fact({
            "open_access_MSc_assessment": "ESSE3; follow the degree's annual call",
            "visa_pre_enrolment": "Universitaly",
            "bachelor_qualification": "Recognized school qualification following at least 12 years of schooling",
            "qualification_documents": "Degree/school diploma and transcripts, translations/legalization and DOV/CIMEA or accepted recognition evidence as required"
        }, "CONFIRMED", ["SRC-UNIMORE-FOREIGN-QUALIFICATION"],
           "Undated university guidance only. It does not establish 2027/28 course intake, dates or current visa-document requirements.")
    }

    p = next(p for p in programs if p["id"] == "legacy-097")
    profile = "SRC-UNIMORE-CE-PROFILE-2026"
    call = "SRC-UNIMORE-CE-CALL-2026"
    p.update(program="Computer Engineering", city="Modena", overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
    for key, value in (("level", "MSc"), ("language", "Italian"), ("field", "Computer Engineering")):
        p[key] = fact(value, "REQUIRES_VERIFICATION", [profile],
                      "Official 2026/27 course identity only; confirm the 2027/28 offer and teaching language.")
    p["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-UNIMORE-CATALOGUE-2026", profile, call],
                                       "The current named catalogue listing and course call reviewed are for 2026/27. No 2027/28 first-year offer was identified; no discontinuation is inferred.")
    p["previous_cycle_tags"] = dict(level="MSc", language="Italian", field="Computer Engineering", cycle="2026-2027",
                                    label="Official 2026/27 course evidence only; 2027/28 first-year intake remains unverified")
    p["source_ids"] = [s["id"] for s in SOURCES if s["id"] != "SRC-UNIMORE-BSC-CE-2026"]
    p["facts"] = {
        "previous_cycle_course_listing": fact({"academic_year": "2026/27", "official_name": "Computer Engineering",
                                                "course_code": "20-362", "level": "MSc", "language": "Italian",
                                                "duration_years": 2, "degree_class": "LM-32", "campus": "Modena",
                                                "access": "Open access subject to curriculum and personal-preparation assessment"},
                                               "CONFIRMED", [profile, "SRC-UNIMORE-CATALOGUE-2026"],
                                               "The official Italian and English web profiles both classify teaching as Italian. This verifies the 2026/27 listing only."),
        "previous_cycle_program_requirements": fact({
            "academic_year": "2026/27", "degree": "Three-year degree or recognized equivalent",
            "Italian_qualification_curricular_credits": {"minimum_total_cfu": 90, "mathematics_physics_minimum_cfu": 30,
                                                          "computing_information_engineering_minimum_cfu": 57,
                                                          "of_which_computing_computer_engineering_minimum_cfu": 18,
                                                          "English_minimum_cfu": 3},
            "Italian_degree_readiness": "At least 85/110 satisfies the titles-based preparation check",
            "foreign_degree_score": "Final grade, or weighted mean if unavailable, strictly above three quarters of the scale maximum",
            "foreign_qualification_assessment": "Academic-record evaluation and possible interview",
            "Italian_language": "Test required unless exempt",
            "English": "Adequate to use technical texts and attend seminars; the call states no B2 admission-certificate threshold"
        }, "CONFIRMED", [call], "2026/27 call requirements only. Grade thresholds differ by qualification route; no GPA conversion or 2027/28 threshold is inferred."),
        "previous_cycle_curricula": fact(["Cloud and Cyber Security", "Data Engineering and Analytics"], "CONFIRMED",
                                          ["SRC-UNIMORE-CE-DEPARTMENT"], "The department describes these tracks from 2023/24; confirm the new offer's curricula."),
        "previous_cycle_application_windows": fact({"academic_year": "2026/27", "assessment_deadline": "2026-12-14",
                                                     "qualifying_degree_deadline": "2026-12-18",
                                                     "enrollment_start": "2026-07-08", "enrollment_deadline": "2026-12-22"},
                                                    "CONFIRMED", [call], "All dates belong to the 2026/27 procedure and must not be used as 2027/28 deadlines."),
        "previous_cycle_international_admission": fact({
            "academic_year": "2026/27", "assessment_portal": "ESSE3", "visa_pre_enrolment": "Universitaly",
            "documents": ["Qualification and transcript", "Detailed exam syllabi", "CV", "Optional motivation letter",
                          "Required language, recognition and identity documents at enrollment"],
            "course_admissions_email": "admissions-inginf@unimore.it",
            "course_registrar_email": "segrstud.ingegneria@unimore.it"
        }, "CONFIRMED", [call, "SRC-UNIMORE-FOREIGN-QUALIFICATION"],
           "Prior-cycle course process and general qualification guidance only; admission assessment does not replace Universitaly and visa processing."),
        "previous_cycle_available_places": fact({"academic_year": "2026/27", "non_EU_resident_abroad_reserved": 10},
                                                "CONFIRMED", [call], "Reserved prior-cycle quota only; no 2027/28 quota or acceptance rate is established."),
        "previous_cycle_application_fee": fact(None, "UNAVAILABLE", [call], "The reviewed 2026/27 MSc call states no specific application fee; no zero-fee assumption is made."),
        "previous_cycle_tuition": historical_tuition,
        "previous_cycle_scholarships": historical_scholarships,
        "application_windows": pending_window,
        "application_fee_2027_2028": pending_fee,
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", [call, "SRC-UNIMORE-CATALOGUE-2026"],
                                                        "No 2027/28 course call, selection requirements or places were identified."),
        "tuition_2027_2028": pending_tuition,
        "scholarships_2027_2028": pending_scholarships,
        "acceptance_rate": fact(None, "UNAVAILABLE", [profile, call],
                                "No complete comparable applicant and admitted totals were identified; no acceptance rate is calculated.")
    }

