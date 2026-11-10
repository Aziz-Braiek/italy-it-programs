"""University of Palermo research reviewed 10 November 2026.

The latest new-entry course plan is 2026/27. Official 2027/28 teaching
assignments establish academic activity only; admission remains pending.
"""

CHECKED = "2026-11-10"
PORTAL = "https://immaweb.unipa.it/immareg/facelets/anag/ins_anag_generale.seam?partnerId=IMMAWEB"

SOURCES = [{'id': 'SRC-PALERMO-CATALOGUE-2026',
  'university_id': 'palermo',
  'title': 'Degree offer 2026/27',
  'url': 'https://www.unipa.it/Offerta-Formativa-2026-2027/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Lists Computer Science and Artificial Intelligence, LM-18, Palermo, open access. The university '
              'resolution sets a general non-EU-abroad capacity of 30 for conventional open-access courses; the '
              'course row does not give a separate quota. This is a 2026/27 offer.',
  'supports': ['program.name',
               'program.level',
               'program.location',
               'program.access_type',
               'university.prior_cycle_places']},
 {'id': 'SRC-PALERMO-CSAI-PLAN-2026',
  'university_id': 'palermo',
  'title': 'Computer Science and Artificial Intelligence – new-enrolment study plan',
  'url': 'https://www.unipa.it/dipartimenti/matematicaeinformatica/cds/computerscienceandartificialintelligence2323/?pagina=pianodistudi',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'The new-enrolment study plan is explicitly labelled 2026/2027, with 2025/2026 in the archive. It '
              'does not publish a 2027/28 first-year plan.',
  'supports': ['program.previous_cycle_listing', 'program.latest_course_cycle']},
 {'id': 'SRC-PALERMO-CSAI-PROFILE',
  'university_id': 'palermo',
  'title': 'Computer Science and Artificial Intelligence – course profile',
  'url': 'https://www.unipa.it/dipartimenti/matematicaeinformatica/cds/computerscienceandartificialintelligence2323/index.html',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'Names the LM-18 MSc in Palermo and course contact cicsi@unipa.it. Lists B2 English and entry via '
              'L-31, L-35, L-8, L-41 or L-30 degrees, another Italian degree with 6 ECTS Mathematics/Physics and '
              '12 ECTS Computing, or an equivalent foreign degree. The profile has no 2027/28 intake declaration.',
  'supports': ['program.name', 'program.level', 'program.requirements', 'program.contact']},
 {'id': 'SRC-PALERMO-CSAI-LANGUAGE',
  'university_id': 'palermo',
  'title': 'Computer Science and Artificial Intelligence – course presentation',
  'url': 'https://www.unipa.it/dipartimenti/matematicaeinformatica/cds/computerscienceandartificialintelligence2323/?pagina=presentazione',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'The course presentation explicitly identifies English as the official teaching language and English '
              'thesis writing. This is an undated programme description and cannot establish a new 2027/28 intake.',
  'supports': ['program.language']},
 {'id': 'SRC-PALERMO-CSAI-REG-2025',
  'university_id': 'palermo',
  'title': 'Computer Science and Artificial Intelligence – teaching regulation, 2025/26',
  'url': 'https://www.unipa.it/dipartimenti/matematicaeinformatica/cds/computerscienceandartificialintelligence2323/.content/documenti/Regolamenti/Computer_Science_and_Artificial_Intelligence_reg_did_cds_2025_2_SA_08.04.2025.pdf',
  'source_type': 'Official degree regulation PDF',
  'accessed_at': '2026-11-10',
  'cycle': '2025-2026',
  'evidence': 'Regulation covers the 2025/26 cohort: LM-18, English, conventional teaching in Palermo. It repeats '
              'the course-profile academic routes and B2 English; candidates without L-31 must undergo a '
              'Mathematics/Computing interview with the coordinator or teachers. This regulation is not a 2026/27 '
              'or 2027/28 call.',
  'supports': ['program.prior_cycle_requirements', 'program.language', 'program.location', 'program.selection']},
 {'id': 'SRC-PALERMO-CSAI-TEACHING-2027',
  'university_id': 'palermo',
  'title': 'Giovanni Pilato – official teaching assignments',
  'url': 'https://www.unipa.it/persone/docenti/p/giovanni.pilato/?pagina=insegnamenti',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2027-2028',
  'evidence': 'Lists Information Retrieval and Natural Language Processing, 6 ECTS, under Computer Science and '
              'Artificial Intelligence in AY 2027/28. It is a teaching assignment and contains no new-entry '
              'admission, first-year cohort or application call.',
  'supports': ['program.academic_year_course_offering']},
 {'id': 'SRC-PALERMO-MASTERS-2026',
  'university_id': 'palermo',
  'title': 'International Master degrees – 2026/27',
  'url': 'https://www.unipa.it/mobilita/en/new-students/masters-degrees/?PageSpeed=noscript',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'The international catalogue is labelled enrolling in AY 2026/27 and lists Computer Science and '
              'Artificial Intelligence. The page describes two-year second-cycle courses with 120 credits.',
  'supports': ['program.name', 'program.level', 'program.duration']},
 {'id': 'SRC-PALERMO-INTL-CONTACT',
  'university_id': 'palermo',
  'title': 'International Students Enrolment',
  'url': 'https://www.unipa.it/mobilita/en/new-students/new-students---enrolment/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'International qualification holders use the dedicated international admission routes. Credential '
              'Evaluation Office email is internationalstudents@unipa.it. Visa pre-enrolment does not guarantee a '
              'visa.',
  'supports': ['university.contact', 'university.international_process']},
 {'id': 'SRC-PALERMO-NON-EU-2026',
  'university_id': 'palermo',
  'title': 'Extra-EU international enrolment – 2026/27',
  'url': 'https://www.unipa.it/mobilita/en/new-students/new-students---enrolment/enrolment-procedures-for-extra-eu-foreign-students/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'For 2026/27 English MSc applications: first call 15 January–15 March; second 15 April–20 July 2026; '
              'Universitaly application by 23 August for candidates already applying in UniPa portal; '
              'personal-knowledge interviews through 30 November. Requires passport, photo, degree, transcript, '
              'language evidence and CV. English route uses UniPa portal assessment followed by Universitaly.',
  'supports': ['university.prior_cycle_deadlines',
               'program.prior_cycle_international_route',
               'program.prior_cycle_documents']},
 {'id': 'SRC-PALERMO-MSC-FIRST-CALL-2026',
  'university_id': 'palermo',
  'title': 'First international Master call, 2026/27',
  'url': 'https://www.unipa.it/UNIPA-MASTERS-DEGREE--ADMISSION-OPEN/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'University notice dated 15 January 2026 gives the first Master application call as 15 January–15 '
              'March 2026 and expressly says there is no application fee for that call.',
  'supports': ['university.prior_cycle_application_fee', 'university.prior_cycle_application_window']},
 {'id': 'SRC-PALERMO-EU-ROUTE',
  'university_id': 'palermo',
  'title': 'EU and equivalent foreign-degree enrolment',
  'url': 'https://www.unipa.it/mobilita/en/new-students/new-students---enrolment/enrolment-procedures-for-intra-eu-foreign-students/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'EU/equivalent applicants use the UniPa Student Portal. After the admission letter, the course '
              'coordinator conducts a personal-knowledge interview, including English assessment. Foreign '
              'qualifications require original legalised degree and DOV or accepted CIMEA/Diploma Supplement '
              'alternatives.',
  'supports': ['program.international_route', 'program.required_documents']},
 {'id': 'SRC-PALERMO-LANGUAGE',
  'university_id': 'palermo',
  'title': 'International language requirements',
  'url': 'https://www.unipa.it/mobilita/en/new-students/admission-requirements/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': 'general',
  'evidence': 'General guidance lists IELTS Academic 5.5, TOEFL iBT 72, PTE 46, Trinity ISE II–IV and recognised '
              'Cambridge/British Institutes qualifications. Its explicit English-certificate exemption is for '
              'programmes with a recognised English standardised admission test; it does not repeat the MOI '
              'alternative found on the 2026/27 Extra-EU page. No 2027/28 course-specific standard is established.',
  'supports': ['university.general_english_guidance', 'university.language_evidence_discrepancy']},
 {'id': 'SRC-PALERMO-FOREIGN-FEES-2026',
  'university_id': 'palermo',
  'title': 'International tuition fees – 2026/27 framework',
  'url': 'https://www.unipa.it/mobilita/en/new-students/tuition-fees/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Foreign-resident non-EU students may choose €211/€267/€378 flat charges by country grouping or '
              'income assessment through ISEE parificato. The income route has €156 fixed charges (€140 regional '
              'tax + €16 stamp) plus a variable contribution. The flat-charge text incorrectly calls all €156 '
              'regional tax; the separate contribution table confirms €140 + €16. Financial-document references '
              'are for 2024 income and 2026 household/property circumstances.',
  'supports': ['university.previous_cycle_tuition',
               'university.fee_conditions',
               'university.fee_wording_discrepancy']},
 {'id': 'SRC-PALERMO-FEE-TABLE-2026',
  'university_id': 'palermo',
  'title': 'Student contribution table, 2026/27',
  'url': 'https://www.unipa.it/servizi/segreterie/.content/documenti/regolamenti_calendari/2026/contrib-stu-2026_27.pdf',
  'source_type': 'Official university fee table PDF',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'The table expressly covers 2026/27 and shows €16 stamp + €140 regional tax. Scientific-area '
              'contribution is €370–€2,914 by ISEE before exemptions/reductions. It gives 40%/30%/30% instalments '
              'and second-instalment deadline 29 December 2026, whereas the university web fee guide says 31 '
              'December.',
  'supports': ['university.previous_cycle_tuition',
               'university.fee_payment_structure',
               'university.fee_date_discrepancy']},
 {'id': 'SRC-PALERMO-FEES-2026',
  'university_id': 'palermo',
  'title': 'Student fees and contributions',
  'url': 'https://www.unipa.it/target/futuristudenti/tasse-agevolazioni/tasse-contributi/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Fees comprise stamp, regional tax and income/course-dependent contribution. General schedule is 40% '
              'on enrolment, 30% by 31 December 2026 and 30% by 28 February 2027; open-access MSc pays its first '
              'instalment when enrolling. The second instalment date conflicts with the 29 December date in the '
              '2026/27 table.',
  'supports': ['university.previous_cycle_tuition',
               'university.fee_payment_structure',
               'university.fee_date_discrepancy']},
 {'id': 'SRC-PALERMO-FEE-REG-INDEX-2026',
  'university_id': 'palermo',
  'title': 'Student contribution regulation and archive',
  'url': 'https://www.unipa.it/target/studenti-iscritti/risorse/regolamento-contribuzione-studentesca/index.html',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'The latest table is labelled 2026/27. The linked regulation is labelled 2025/26 in force for '
              '2026/27, but its PDF title and text are 2024/25. This document-label discrepancy should be verified '
              'before treating its exemption rules as current. No 2027/28 table appears.',
  'supports': ['university.fee_publication_status', 'university.fee_regulation_discrepancy']},
 {'id': 'SRC-PALERMO-SCHOLARSHIPS-2026',
  'university_id': 'palermo',
  'title': 'Scholarships for International Students',
  'url': 'https://www.unipa.it/mobilita/en/new-students/scholarship-for-international-students/',
  'source_type': 'Official university page',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'The page lists ERSU and MAECI as 2026/27 schemes, targeted UNICORE 8.0 for refugee entrants '
              '2026/28, and other older or restricted awards. ERSU is income/merit based and may provide tuition '
              'relief, accommodation, meals and cash. No general 2027/28 scholarship call was found.',
  'supports': ['university.scholarship_publication_status', 'university.prior_cycle_scholarships']},
 {'id': 'SRC-ERSU-PALERMO-CALL-2026',
  'university_id': 'palermo',
  'title': 'ERSU Palermo scholarship and services call, 2026/27',
  'url': 'https://www.ersupalermo.it/wp-content/uploads/2026/06/Bando-di-Concorso-dellERSU-di-Palermo-a.a.-2026_2027.pdf',
  'source_type': 'Official regional scholarship call PDF',
  'accessed_at': '2026-11-10',
  'cycle': '2026-2027',
  'evidence': 'Annual 2026/27 benefit competition: applications 5 June–22 July 2026 at 14:00. Income limits ISEE '
              '€23,000 and ISPE €52,500. International applicants need equivalent ISEE and residence '
              'documentation, regularisable by 30 November 2026. Monetary amounts depend on ISEE and residence '
              'classification; meals/housing values are deducted when provided. For ISEE €11,500–€15,333.33, the '
              'off-site gross base is €7,171.11; with both services the cash portion is €4,271.11. Eligibility, '
              'merit and available funding apply.',
  'supports': ['university.prior_cycle_scholarships',
               'university.scholarship_conditions',
               'university.housing_benefits']}]

SOURCES.append({
    "id": "SRC-PALERMO-FEE-REG-2024", "university_id": "palermo",
    "title": "Student contribution regulation – linked PDF dated 2024/25",
    "url": "https://www.unipa.it/servizi/segreterie/.content/documenti/regolamenti_calendari/2024/5398717-Regolamento-per-la-contribuzione-studentesca-2024-2025.pdf",
    "source_type": "Official university fee regulation PDF", "accessed_at": CHECKED,
    "cycle": "2024-2025",
    "evidence": "The regulation's decree and text expressly state AY 2024/25. The current index labels this link as a 2025/26 regulation in force for 2026/27, creating a document-label mismatch. The PDF alone cannot confirm next-cycle exemptions.",
    "supports": ["university.fee_regulation_discrepancy"],
})

BATCH = {'id': 'palermo-computer-science-ai-program-and-international-admissions-review',
 'status': 'partial',
 'result': 'Reviewed the sole legacy MSc candidate individually. Official 2026/27 offer lists Computer Science and '
           'Artificial Intelligence (LM-18), with English delivery and historical requirements. Official 2027/28 '
           'subject assignments are evidence of teaching only; first-year intake is not confirmed. The '
           'international FAQ expressly says exact 2027/28 application dates are unpublished. Fee and scholarship '
           'material remains 2026/27; document and deadline discrepancies are recorded. Expanded the legacy '
           'abbreviated course name and recorded historical academic requirements, UniPa/Universitaly routes, '
           'flat-country or income-based tuition options and ERSU eligibility. Flagged the conflicting second '
           'instalment dates and the mislabelled fee-regulation link.'}

REPORT = 'Reviewed the sole legacy MSc candidate individually. Official 2026/27 offer lists Computer Science and Artificial Intelligence (LM-18), with English delivery and historical requirements. Official 2027/28 subject assignments are evidence of teaching only; first-year intake is not confirmed. The international FAQ expressly says exact 2027/28 application dates are unpublished. Fee and scholarship material remains 2026/27; document and deadline discrepancies are recorded. The course regulation is explicitly for 2025/26, although the undated profile repeats its B2 English and curricular routes. Prior-cycle international MSc windows were 15 January–15 March and 15 April–20 July 2026; the first call was free. Foreign-resident non-EU tuition options in 2026/27 were country tariffs of €211/€267/€378 or an income-based route, with €156 fixed tax/stamp charges plus a variable contribution. ERSU benefits depend on income, merit, student classification and available funding. Official second-instalment dates conflict between 29 and 31 December 2026, and the fee-regulation index points to an older PDF than its label states.'

def apply(universities, programs, fact):
    uni = next(u for u in universities if u["id"] == "palermo")
    uni.update(application_portal_url=PORTAL, contact_email="internationalstudents@unipa.it",
               contact_url="https://www.unipa.it/mobilita/en/new-students/new-students---enrolment/",
               last_checked=CHECKED, research_summary=REPORT)
    uni["source_ids"] = list(dict.fromkeys(uni["source_ids"] + [s["id"] for s in SOURCES]))
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    uni["cycle_facts"] = {
        "application_deadlines": fact(None, "NOT_YET_PUBLISHED", ["SRC-PALERMO-2027"], "The official FAQ explicitly says exact 2027/28 dates have not yet been published. The 2026/27 calendar is retained as historical context only."),
        "application_fee_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-PALERMO-MSC-FIRST-CALL-2026"], "Only the first 2026/27 international MSc call was expressly free. No 2027/28 application fee was identified."),
        "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-PALERMO-FEE-TABLE-2026", "SRC-PALERMO-FEE-REG-INDEX-2026"], "The latest annual contribution table is 2026/27. No 2027/28 amount, exemption or payment calendar is confirmed."),
        "scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-PALERMO-SCHOLARSHIPS-2026", "SRC-ERSU-PALERMO-CALL-2026"], "The reviewed university list and ERSU call concern 2026/27 or older and targeted schemes. No 2027/28 call or recurring award is inferred."),
        "previous_cycle_application_windows": fact({"academic_year":"2026/27", "first_international_msc_call":{"start":"2026-01-15", "end":"2026-03-15", "fee_eur":0}, "second_international_msc_call":{"start":"2026-04-15", "end":"2026-07-20"}, "Universitaly_deadline":"2026-08-23", "Universitaly_scope":"Candidates already holding a started UniPa portal application", "personal_knowledge_interview_deadline":"2026-11-30"}, "CONFIRMED", ["SRC-PALERMO-NON-EU-2026", "SRC-PALERMO-MSC-FIRST-CALL-2026"], "These dates apply to the prior-cycle international non-EU abroad route. They are not 2027/28 application dates."),
        "previous_cycle_international_process": fact({"academic_year":"2026/27", "English_MSc_route":"UniPa Student Portal application, administrative and course-coordinator evaluation, then Universitaly pre-enrolment for study-visa applicants", "documents":["Passport", "Photo", "Bachelor's degree", "Transcript of Records", "English-language evidence", "CV"], "foreign_qualification":"Original legalised degree with DOV or accepted CIMEA/Diploma Supplement alternative, as required", "EU_or_equivalent_route":"UniPa portal, admission letter and personal-knowledge interview including English assessment"}, "CONFIRMED", ["SRC-PALERMO-NON-EU-2026", "SRC-PALERMO-EU-ROUTE"], "Prior-cycle international process plus undated EU guidance. The new annual procedure and course requirements must be checked."),
        "previous_cycle_tuition": fact({"academic_year":"2026/27", "non_eu_resident_abroad_country_tariff_eur":{"B2A":211,"B2B":267,"other":378}, "alternative":"ISEE parificato income-based contribution", "fixed_charges_eur":156, "fixed_charges_components":{"regional_tax_eur":140,"stamp_eur":16}, "scientific_area_gross_contribution_eur_range":[370,2914], "gross_table_conditions":"Before applicable exemptions and reductions; the contribution excludes fixed regional tax/stamp charges", "installment_percent":[40,30,30], "first_installment_for_open_MSc":"Upon enrolment", "third_installment_deadline":"2027-02-28"}, "CONFIRMED", ["SRC-PALERMO-FOREIGN-FEES-2026", "SRC-PALERMO-FEE-TABLE-2026", "SRC-PALERMO-FEES-2026"], "University-wide previous-cycle framework. Country tariffs apply to the specified foreign-resident non-EU category. €156 is the fixed component, not total income-based tuition. The English page mislabels this sum as regional tax in its flat-rate paragraph; the annual table gives €140 tax plus €16 stamp."),
        "previous_cycle_second_installment_deadline": fact({"academic_year":"2026/27", "annual_fee_table":"2026-12-29", "university_web_guide":"2026-12-31"}, "CONFLICTING_SOURCES", ["SRC-PALERMO-FEE-TABLE-2026", "SRC-PALERMO-FEES-2026"], "Two official sources publish different second-instalment dates. Confirm with the student fee office; neither date is a 2027/28 payment deadline."),
        "previous_cycle_fee_regulation_link": fact({"index_label":"2025/26 regulation in force for 2026/27", "linked_PDF_title_and_content":"2024/25"}, "CONFLICTING_SOURCES", ["SRC-PALERMO-FEE-REG-INDEX-2026", "SRC-PALERMO-FEE-REG-2024"], "The linked PDF is older than the index label. The current annual table supports the recorded amounts; the link does not independently verify 2026/27 exemption rules."),
        "previous_cycle_scholarships": fact({"academic_year":"2026/27", "regional_provider":"ERSU Palermo", "application_window":"5 June–22 July 2026, 14:00 Italy time", "ISEE_ceiling_eur":23000, "ISPE_ceiling_eur":52500, "conditions":"Enrollment, merit, economic eligibility, residence classification and available funding under the annual call", "benefits":"Monetary award, meals and possible housing; service values are deducted from the gross award", "example":{"ISEE_band_eur":"11,500–15,333.33", "off_site_gross_base_eur":7171.11, "cash_if_both_housing_and_meals_are_provided_eur":4271.11}, "foreign_income":"ISEE parificato and required identity/residence documentation; international regularisation deadline 30 November 2026"}, "CONFIRMED", ["SRC-ERSU-PALERMO-CALL-2026", "SRC-PALERMO-SCHOLARSHIPS-2026"], "Closed prior-cycle regional competition. Eligibility does not guarantee an award, and its amounts or thresholds are not projected into 2027/28."),
    }
    p = next(p for p in programs if p["id"] == "legacy-091")
    p.update(program="Computer Science and Artificial Intelligence", city="Palermo", overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
    for key, value in (("level", "MSc"), ("language", "English"), ("field", "Computer Science")):
        p[key] = fact(value, "REQUIRES_VERIFICATION", ["SRC-PALERMO-CATALOGUE-2026", "SRC-PALERMO-CSAI-LANGUAGE"], "Official prior-cycle course listing and undated description only; confirm the 2027/28 new-entry offer.")
    p["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-PALERMO-2027", "SRC-PALERMO-CSAI-PLAN-2026", "SRC-PALERMO-CSAI-TEACHING-2027"], "The newest first-year plan is 2026/27. A 2027/28 subject assignment confirms planned teaching activity, but contains no first-year cohort or admission offer. Exact 2027/28 application dates are expressly unpublished.")
    p["previous_cycle_tags"] = dict(level="MSc", language="English", field="Computer Science", cycle="2026-2027", label="Official 2026/27 course evidence only; 2027/28 first-year intake remains unverified")
    p["source_ids"] = ["SRC-PALERMO-2027"] + [s["id"] for s in SOURCES]
    p["facts"] = {
        "previous_cycle_course_listing": fact({"academic_year":"2026/27", "official_name":"Computer Science and Artificial Intelligence", "course_code":"2323", "level":"MSc", "language":"English", "degree_class":"LM-18", "duration_years":2, "ects":120, "campus":"Palermo", "access":"Open access subject to curricular and personal-preparation verification"}, "CONFIRMED", ["SRC-PALERMO-CATALOGUE-2026", "SRC-PALERMO-CSAI-PLAN-2026", "SRC-PALERMO-CSAI-LANGUAGE", "SRC-PALERMO-MASTERS-2026"], "Named previous-cycle offer and current undated course description only. The legacy abbreviated name has been expanded to the official title."),
        "previous_cycle_program_requirements": fact({"academic_year":"2025/26", "degree_routes":["L-31 Computing", "L-35 Mathematics", "L-8 Information Engineering", "L-41 Statistics", "L-30 Physics", "Other Italian Bachelor/Master with at least 6 ECTS Mathematics/Physics and 12 ECTS Computing", "Recognised equivalent foreign qualification"], "english":"B2 CEFR", "assessment":"For graduates outside L-31, basic Mathematics and Computing interview with the coordinator or teachers"}, "CONFIRMED", ["SRC-PALERMO-CSAI-REG-2025", "SRC-PALERMO-CSAI-PROFILE"], "The regulation explicitly covers the 2025/26 cohort. Its curricular routes and B2 threshold are repeated on the undated course profile; they have not been verified as 2027/28 criteria."),
        "academic_year_2027_2028_teaching": fact({"subject":"Information Retrieval and Natural Language Processing", "ects":6, "academic_year":"2027/28", "source_kind":"Official teacher assignment"}, "CONFIRMED", ["SRC-PALERMO-CSAI-TEACHING-2027"], "An individual subject's academic-year assignment does not identify the entrant cohort or establish a 2027/28 first-year intake."),
        "English_certificate_guidance": fact({"general_page":{"IELTS_Academic":5.5, "TOEFL_iBT":72, "PTE":46}, "certificate_alternative":"The 2026/27 Extra-EU page accepts MOI, while the general language page does not repeat that exemption"}, "REQUIRES_VERIFICATION", ["SRC-PALERMO-LANGUAGE", "SRC-PALERMO-NON-EU-2026"], "These sources do not establish course-specific 2027/28 accepted evidence. Confirm the annual call before relying on any certificate threshold or MOI waiver."),
        "previous_cycle_application_windows": uni["cycle_facts"]["previous_cycle_application_windows"],
        "previous_cycle_international_admission": uni["cycle_facts"]["previous_cycle_international_process"],
        "previous_cycle_tuition": uni["cycle_facts"]["previous_cycle_tuition"],
        "previous_cycle_scholarships": uni["cycle_facts"]["previous_cycle_scholarships"],
        "application_windows": fact(None, "NOT_YET_PUBLISHED", ["SRC-PALERMO-2027"], "Exact 2027/28 application dates have not been published. The prior-cycle windows must not be used for this intake."),
        "application_fee_2027_2028": uni["cycle_facts"]["application_fee_2027_2028"],
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-PALERMO-CSAI-REG-2025", "SRC-PALERMO-CSAI-PROFILE"], "No new 2027/28 course requirements or available places were identified."),
        "tuition_2027_2028": uni["cycle_facts"]["tuition_2027_2028"],
        "scholarships_2027_2028": uni["cycle_facts"]["scholarships_2027_2028"],
        "acceptance_rate": fact(None, "UNAVAILABLE", ["SRC-PALERMO-CSAI-PROFILE", "SRC-PALERMO-CATALOGUE-2026"], "No official comparable applicant and admitted totals were identified. Open access does not establish an acceptance percentage."),
        "course_contact": fact({"email":"cicsi@unipa.it", "office":"Department of Mathematics and Computer Science, Via Archirafi 34, Palermo"}, "CONFIRMED", ["SRC-PALERMO-CSAI-PROFILE"], "Current course-office contact; international credential questions go to internationalstudents@unipa.it."),
    }
