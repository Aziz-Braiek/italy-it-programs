"""Official Salerno research reviewed 10 November 2026.

The 2026/27 Computer Science degree has Italian and English curricula; the
Internet of Things curriculum is fully English. No 2027/28 first-year offer is
inferred from that listing or from a scholarship's second-year renewal clause.
"""

CHECKED = "2026-11-10"
PORTAL = "https://esse3web.unisa.it/"


def source(sid, title, url, evidence, supports, cycle="2026-2027", kind="Official university page"):
    return dict(id=sid, university_id="salerno", title=title, url=url,
                source_type=kind, accessed_at=CHECKED, cycle=cycle,
                evidence=evidence, supports=supports)


SOURCES = [
    source("SRC-SALERNO-CATALOGUE-2026", "Enrolment course inventory 2026/27",
           "https://web.unisa.it/didattica/immatricolazioni/scegli-uno-dei-nostri",
           "The page explicitly welcomes applicants to 2026/27. Computer Science/Informatica NF225 is an LM-18 Master's with Italian and English teaching; the L-31 Bachelor's is Italian. Course-specific enrolment links control requirements. This does not confirm a 2027/28 first-year offer.",
           ["university.previous_cycle_course_inventory", "university.previous_cycle_bachelor_inventory", "program.previous_cycle_course_listing", "program.language"]),
    source("SRC-SALERNO-ENGLISH-OFFER-2026", "International teaching: degrees in English 2026/27",
           "https://web.unisa.it/en/teaching/international-teaching/postgraduate-degrees",
           "The explicit 2026/27 inventory lists Computer Science NF225 as English/Italian, rather than identifying every curriculum as English. It lists other BSc, MSc, postgraduate master and PhD categories separately. No new 2027/28 course offer is established.",
           ["university.previous_cycle_english_programs", "program.previous_cycle_language"]),
    source("SRC-SALERNO-CS-REGULATION-2026", "Computer Science NF225 course regulation, cohort 2026/27",
           "https://corsi.unisa.it/uploads/rescue/__regolamenti-cds/2026/NF225.pdf",
           "The course's regulation index labels this PDF NF225 cohort 2026/27. It establishes LM-18, two years/120 CFU, five curricula, L-31/L-8 entry or at least 45 CFU in INFO-01/A and IINF-05/A for other classes, individual foreign-curriculum assessment, and readiness assessment. The L-31/L-8 test exemption requires at least 85/110. Its 2026/27 IoT curriculum table marks technical teaching Engl. The English-language examination's B2 learning target is not a universal B2 admission-certificate requirement.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_requirements", "program.previous_cycle_curricula", "program.previous_cycle_language"], kind="Official course regulation PDF"),
    source("SRC-SALERNO-CS-ENGLISH-TRACK", "Computer Science: English Internet of Things curriculum",
           "https://corsi.unisa.it/informatica-magistrale/en/home",
           "The course describes five specializations and explicitly says Internet of Things is fully English and lasts two years. This undated presentation is corroborated by the named 2026/27 regulation and is not evidence of a 2027/28 intake.",
           ["program.curriculum", "program.language", "program.duration"], cycle="general"),
    source("SRC-SALERNO-CS-ADMISSION-2026", "Computer Science enrolment: foreign applicants",
           "https://corsi.unisa.it/informatica-magistrale/en/enrollment",
           "Applications for 2026/27 are now closed. Relevant Bachelor's preparation and at least 45 computing ECTS are assessed individually. Non-EU applications start on Universitaly; emailed dossiers are not assessed. Positive documentary assessment leads to a compulsory remote C++/Java/database-query quiz and interview. Two interview no-shows cause rejection. Applicants without B2 Italian enter the English IoT curriculum. English evidence may be in CV/academic records; an officially English-taught previous degree avoids further certification under this guidance, while consulates may require a certificate. Contact: international_incoming@cs.unisa.it.",
           ["program.previous_cycle_international_admission", "program.previous_cycle_requirements", "program.previous_cycle_language", "program.contact"]),
    source("SRC-SALERNO-CS-ENROLMENT-2026", "Computer Science: enrolment and assessment timing",
           "https://corsi.unisa.it/informatica-magistrale/immatricolazioni",
           "The course page states Master's enrolment 15 July 2026–1 March 2027, ESSE3 registration, assessment in September/February and academic contact gvitiello@unisa.it. One curricular bullet incorrectly names the separate Cloud/Security degree; the NF225 regulation and English Computer Science admission page provide independent course-specific requirements. The general enrolment period is not the earlier non-EU Universitaly deadline.",
           ["program.previous_cycle_enrollment_dates", "program.previous_cycle_assessment_timing", "program.contact"]),
    source("SRC-SALERNO-CS-UNIVERSITALY-DEADLINE-2026", "Universitaly pre-enrolment deadline: 30 September 2026",
           "https://www.di.unisa.it/unisa-rescue-page/dettaglio/id/1401/module/475/row/30421/universitaly-pre-enrolment-application-deadline-september-30-2026",
           "The Computer Science department notice published 25 September 2026 states Universitaly pre-enrolment is accepted until 30 September 2026 and later applications will not be assessed. This deadline belongs to the closed 2026/27 intake.",
           ["program.previous_cycle_application_deadline"]),
    source("SRC-SALERNO-NON-EU-2026", "Non-EU citizens abroad: qualification and visa route",
           "https://web.unisa.it/en/teaching/enrollment/non-eu-citizens-abroad",
           "University guidance uses Universitaly for non-EU applicants abroad, university qualification evaluation and subsequent consular visa processing. It mentions November 2026 and also retains an older March 2025 opening reference, so it is not a 2027/28 schedule. Bachelor's qualifications normally follow 12 years of schooling. Italian-taught degree applicants require B2 Italian or the indicated test unless exempt. Recognition documentation may include ENIC-NARIC, an official foreign institution's evidence or a Declaration of Value.",
           ["university.non_eu_process", "university.previous_cycle_bachelor_requirements", "university.foreign_qualification_documents"]),
    source("SRC-SALERNO-FEES-2026", "Tuition and contributions 2026/27",
           "https://web.unisa.it/didattica/segreteria/tasse-e-contributi",
           "The fee page explicitly covers 2026/27 and links the annual fee regulation. The no-tax-area COA exemption has an ISEE ceiling of 30,000 euros and statutory progress/enrolment conditions; payment is through pagoPA in ESSE3. This is not a 2027/28 fee publication.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition"]),
    source("SRC-SALERNO-FEE-REGULATION-2026", "Student contribution regulation 2026/27",
           "https://web.unisa.it/uploads/rescue/251/791/regolamento-in-materia-di-contribuzione-studentesca-a.a.-2026-27.pdf",
           "The official PDF was fetched directly with HTTP 200 and parsed after the page's relative link resolved incorrectly in the web tool. Fees comprise income/progress-dependent COA, stamp and regional tax. Regional tax is 130/151/173 euros; foreign-resident households ordinarily use 151 euros. Non-EU non-residents normally use COA band III or band I for listed low-human-development countries, unless eligible ISEE or hardship rules apply. Stamp is 16 euros; foreign-qualification first-year third instalment, if due, is 53 euros. General access-test contribution is 15 euros subject to course exceptions, not a verified IoT prescreening fee. First-year open-access MSc enrolment is due 1 March 2027.",
           ["university.previous_cycle_tuition", "university.previous_cycle_fee_exemptions", "university.previous_cycle_test_contribution", "program.previous_cycle_tuition"], kind="Official tuition regulation PDF"),
    source("SRC-SALERNO-SCHOLARSHIP-NOTICE-2026", "UNISA Scholarship 2026/27: latest deadline and ranking notice",
           "https://web.unisa.it/international/bandi/mobilita-in-ingresso?anno=2026&bando=14294",
           "The university lists 48 scholarships for non-EU international Master's applicants for 2026/27. The latest extended Universitaly submission deadline is 30 June 2026 at 23:59, followed by July rankings. This extension supersedes the original May deadline in the call. The competition is closed.",
           ["university.previous_cycle_scholarships", "university.previous_cycle_scholarship_window"]),
    source("SRC-SALERNO-SCHOLARSHIP-CALL-2026", "UNISA Scholarship call 2026/27",
           "https://web.unisa.it/uploads/rescue/167/14294/call-for-applications-unisa-scholarship-2026-2027.pdf",
           "The call is for 48 non-EU students resident abroad with suitable foreign degrees. Annual value is 8,000 euros: 1,800 cash after enrolment/payment plus room/board valued at 6,200 for 12 months from 1 October 2026. Required dossier includes CV, B2 language evidence, degree/transcripts, syllabi, two references and the incompatibility declaration. Renewal requires 27 credits by 15 September 2027; its 2027/28 reference is the second year of the 2026/27 intake. It is incompatible with MAECI and duplicate room/board benefits; ADISURC cash-only benefits may be sought under the rules. Tuition and regional payment obligations remain.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarships"], kind="Official scholarship call PDF"),
    source("SRC-SALERNO-ADISURC-NOTICE-2026", "ADISURC scholarship and accommodation competition 2026/27",
           "https://adisurcampania.it/notizie/approvazione-bando-di-concorso-20262027",
           "Published 24 July 2026: the regional competition closed 10 September 2026 at 12:00. Apply through the ADISURC student reserved area; foreign applicants can obtain registration credentials. The notice links the call and CAF/ISEE-equivalent documentation. The competition is not a 2027/28 award.",
           ["university.previous_cycle_regional_scholarship_window"], kind="Official regional scholarship notice"),
    source("SRC-SALERNO-ADISURC-CALL-2026", "ADISURC regional scholarship call 2026/27, English PDF",
           "https://adisurcampania.it/sites/default/files/2026-07/Bando%20di%20Concorso%20a.a.%202026.27_ENG.pdf",
           "University of Salerno students are eligible subject to enrolment, merit and financial requirements. ISEE ceiling is 25,500 euros and numeric ISPE ceiling 54,000 euros. Foreign-household ISEEUP must reach ADISURC by 31 March 2027. Base awards at ISEE up to 17,000 euros are 7,171.11 off-site, 4,190.71 commuter and 2,890.16 on-site; service deductions, higher-income reductions and eligible uplifts apply. First years normally need 20 credits by 10 August 2027 for full preservation, or by 30 November for half. Benefits are conditional and do not establish 2027/28 awards.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarships"], kind="Official regional scholarship call PDF"),
    source("SRC-SALERNO-CONTACT", "Internationalisation office contacts",
           "https://web.unisa.it/international/contatti",
           "General international enquiries: erasmus@unisa.it. UNISA Scholarship: unisascholarship@unisa.it. The page also lists distinct Erasmus incoming/outgoing contacts and a helpdesk for enrolled students; these are separate from the Computer Science assessment committee's address.",
           ["university.contact"], cycle="general"),
    source("SRC-SALERNO-CS-CONTACT", "Computer Science student and teaching offices",
           "https://corsi.unisa.it/informatica-magistrale/contatti",
           "Computer Science career administration: carrierestudenti.di@unisa.it. Teaching office: didattica.di@unisa.it. Both link the student Help Desk.",
           ["program.contact"], cycle="general"),
    source("SRC-SALERNO-CS-CAMPUS", "Computer Science teaching facilities",
           "https://corsi.unisa.it/informatica-magistrale/strutture-didattiche",
           "The course facilities page locates main classrooms and laboratories in F2/F3/F4 on the Fisciano campus; the shared inventory also includes Avellino facilities. It does not establish a 2027/28 campus change or promise remote attendance.",
           ["program.location"], cycle="general"),
    source("SRC-SALERNO-NATIONAL-VISA-2027", "Universitaly national international-student procedures 2026/27 and 2027/28",
           "https://www.universitaly.it/it/studenti-stranieri",
           "The national page expressly covers 2026/27 and 2027/28. The 2027/28 outer deadline for degree-study visa applications is 31 October 2027, with institutions allowed to set earlier course deadlines. Universitaly is the official free visa-pre-enrolment portal; admission/validation does not guarantee a visa. This does not publish a Salerno course application window or a new first-year offer.",
           ["university.national_visa_deadline_2027_2028", "university.non_eu_process"], cycle="2027-2028", kind="Official ministry / Universitaly guidance"),
]

BATCH = {
    "id": "salerno-computer-science-course-and-admissions-review", "status": "partial",
    "result": "Matched Salerno's sole legacy candidate to Computer Science NF225 LM-18 in the 2026/27 inventory and regulation. Corrected language scope: English/Italian degree with a fully English Internet of Things curriculum, at Fisciano, two years/120 CFU. Recorded curriculum/readiness checks, compulsory international quiz/interview, closed 30 September 2026 Universitaly deadline, separate 1 March 2027 enrolment deadline, conditional tuition and both UNISA/ADISURC benefits. No 2027/28 first-year course offer, university admissions schedule, application fee, tuition or scholarship call was identified. The national 31 October 2027 visa outer deadline and scholarship second-year renewal are separately scoped."
}
REPORT = "Salerno's Computer Science MSc (NF225, LM-18) is a two-year/120-CFU English/Italian degree in the official 2026/27 offer; its Internet of Things curriculum is fully English. International assessment uses Universitaly, document review, a remote programming/database quiz and interview. The 30 September 2026 pre-enrolment deadline is closed; the separate general MSc enrolment deadline is 1 March 2027 and belongs to 2026/27. Tuition depends on ISEE, residence/country and exemptions; a general €15 access-test contribution is not a verified international prescreening fee. The closed UNISA Scholarship 2026/27 offers €1,800 cash plus room/board valued at €6,200, subject to selection and renewal; its mention of 2027/28 is second-year renewal only. ADISURC requires economic, merit and enrolment eligibility. No new 2027/28 course, university application, tuition or scholarship call was identified. The national degree-visa outer application deadline is 31 October 2027, and Salerno may set earlier course deadlines."


def apply(universities, programs, fact):
    uni = next(u for u in universities if u["id"] == "salerno")
    uni.update(application_portal_url=PORTAL, contact_email="erasmus@unisa.it",
               contact_url="https://web.unisa.it/international/contatti",
               cycle_status="REQUIRES_VERIFICATION", research_stage="PARTIALLY_RESEARCHED",
               research_summary=REPORT, last_checked=CHECKED)
    for alias in ("University of Salerno", "UNISA"):
        if alias not in uni["aliases"]:
            uni["aliases"].append(alias)
    for key in uni["coverage"]:
        if key != "official_website_visited":
            uni["coverage"][key] = "partial"
    for s in SOURCES:
        if s["id"] not in uni["source_ids"]:
            uni["source_ids"].append(s["id"])

    regulation = "SRC-SALERNO-CS-REGULATION-2026"
    admission = "SRC-SALERNO-CS-ADMISSION-2026"
    fee_reg = "SRC-SALERNO-FEE-REGULATION-2026"
    catalogue = "SRC-SALERNO-CATALOGUE-2026"
    pending_window = fact(None, "REQUIRES_VERIFICATION", [catalogue, admission],
                          "No 2027/28 Salerno application window was identified. The course's 2026/27 Universitaly applications are explicitly closed; its generic April-opening description is not an announced 2027 date.")
    pending_fee = fact(None, "REQUIRES_VERIFICATION", [admission, fee_reg],
                       "No 2027/28 application fee was identified. The prior-cycle €15 general access-test contribution is subject to course exceptions and does not prove the international assessment fee; Universitaly itself is free.")
    pending_tuition = fact(None, "REQUIRES_VERIFICATION", ["SRC-SALERNO-FEES-2026", fee_reg],
                           "Only the 2026/27 fee schedule was identified. Do not carry its brackets, exemptions or amounts into 2027/28.")
    pending_scholarship = fact(None, "REQUIRES_VERIFICATION", ["SRC-SALERNO-SCHOLARSHIP-NOTICE-2026", "SRC-SALERNO-SCHOLARSHIP-CALL-2026", "SRC-SALERNO-ADISURC-NOTICE-2026"],
                               "No 2027/28 first-year scholarship call was identified. The UNISA call's reference to 2027/28 concerns conditional renewal for the 2026/27 intake, not a new competition.")
    tuition = fact({
        "academic_year": "2026/27", "components": ["Income/progress-dependent COA contribution", "Stamp duty", "Regional tax"],
        "stamp_duty_eur": 16, "regional_tax_eur_brackets": [130, 151, 173],
        "foreign_resident_household_ordinary_regional_tax_eur": 151,
        "No_Tax_Area": {"ISEE_ceiling_eur": 30000, "scope": "COA exemption; regional tax and stamp remain", "first_year_merit": "No merit condition", "other_conditions": "University-enrolment duration and subsequent-year progress under the regulation"},
        "non_EU_non_resident_COA": {"ordinary_band": "III", "listed_low_human_development_countries_band": "I", "alternatives": "Eligible ISEE or documented hardship assessment"},
        "ordinary_full_time_table_totals_eur": {"band_I": 371, "band_III": 610, "without_ISEE": 1783},
        "table_total_scope": "These table totals include stamp but exclude regional tax and precede applicable exemptions/foreign-qualification third-instalment adjustment",
        "foreign_qualification_first_enrolment_third_instalment_if_due_eur": 53,
        "maximum_ordinary_full_time_instalments": 3,
        "first_year_open_access_MSc_enrolment_and_first_payment_deadline": "2027-03-01",
        "later_payments": "If enrolled after 2 November 2026, remaining instalments due 31 March 2027; otherwise ordinary second instalment 21 December 2026 and third 31 March 2027"
    }, "CONFIRMED", ["SRC-SALERNO-FEES-2026", fee_reg],
       "Prior-cycle 2026/27 framework only. Amounts are conditional, not a universal annual price; the no-tax-area exemption excludes stamp/regional tax, and foreign-qualification adjustments can alter the table total.")
    scholarship = fact({
        "academic_year": "2026/27",
        "UNISA": {"awards": 48, "eligible_group": "Non-EU students resident abroad with suitable foreign degrees", "latest_application_deadline": "2026-06-30 23:59", "portal": "Universitaly", "annual_total_value_eur": 8000, "cash_eur": 1800, "room_and_board_value_eur": 6200, "service_start": "2026-10-01", "service_months": 12, "renewal": "27 course credits by 15 September 2027 for the second year of the 2026/27 intake", "fees": "Cash disbursement follows enrolment and required fee/tax payments; this is not an automatic tuition waiver", "documents": ["CV", "B2 programme-language evidence", "Degree and transcript with translation", "Relevant syllabi", "Two references", "Incompatibility declaration"], "incompatibilities": "MAECI and duplicate room/board stipends; ADISURC cash-only aid may be sought under the calls"},
        "ADISURC": {"application_deadline": "2026-09-10 12:00", "ISEE_ceiling_eur": 25500, "ISPE_ceiling_eur": 54000, "base_awards_at_ISEE_up_to_17000_eur": {"off_site": 7171.11, "commuter": 4190.71, "on_site": 2890.16}, "amount_conditions": "Income/status-dependent, with service deductions and eligible uplifts; figures are not guaranteed cash payments", "first_year_progress": "Normally 20 credits by 10 August 2027 for full award; by 30 November 2027 for half", "foreign_household_ISEEUP_deadline": "2027-03-31", "eligibility": "Enrolment, economic, merit and annual documentation requirements"}
    }, "CONFIRMED", ["SRC-SALERNO-SCHOLARSHIP-NOTICE-2026", "SRC-SALERNO-SCHOLARSHIP-CALL-2026", "SRC-SALERNO-ADISURC-NOTICE-2026", "SRC-SALERNO-ADISURC-CALL-2026"],
       "Both competitions concern 2026/27 and are closed. UNISA's €8,000 includes services; 2027/28 is conditional second-year renewal only. ADISURC award values depend on income, status, services, merit and ranking. No 2027/28 award is inferred.")
    national_visa = fact({"academic_year": "2027/28", "outer_visa_application_deadline": "2027-10-31", "portal": "Universitaly", "portal_fee_eur": 0, "earlier_course_deadlines": "Institutions can require earlier visa applications according to course start dates", "visa_decision": "Consular authority; university acceptance/validation is not a visa guarantee"}, "CONFIRMED", ["SRC-SALERNO-NATIONAL-VISA-2027"],
                         "National degree-study visa rule only; this is not a Salerno course application, admission or enrolment deadline and does not establish a new first-year offer.")
    uni["cycle_facts"] = {
        "application_windows": pending_window, "application_fee_2027_2028": pending_fee,
        "tuition_2027_2028": pending_tuition, "scholarships_2027_2028": pending_scholarship,
        "national_visa_application_deadline_2027_2028": national_visa,
        "previous_cycle_tuition": tuition, "previous_cycle_scholarships": scholarship,
        "previous_cycle_general_access_test_contribution": fact({"academic_year": "2026/27", "amount_eur": 15, "exceptions": "Different course resolutions or restricted-admission calls may set another amount"}, "CONFIRMED", [fee_reg], "General previous-cycle test contribution only. Its applicability to the international IoT quiz/interview is not established; no course application fee or zero-fee assumption is made."),
        "general_foreign_qualification_route": fact({"non_EU_abroad": "Universitaly pre-enrolment, university academic evaluation, consular visa route, then university enrolment", "bachelor_schooling": "Normally at least 12 years; compensating university study may be required for shorter schooling", "Italian_taught_degrees": "B2 Italian or required test unless exempt", "qualification_documents": "Degree/school credentials, transcripts and recognition/translation documents as required"}, "CONFIRMED", ["SRC-SALERNO-NON-EU-2026"], "University guidance contains mixed historical dates and is used only for route/qualification context, not a 2027/28 admissions calendar.")
    }
    p = next(p for p in programs if p["id"] == "legacy-090")
    p.update(program="Computer Science", city="Fisciano", overall_status="REQUIRES_VERIFICATION", last_checked=CHECKED)
    for key, value in (("level", "MSc"), ("language", "Italian / English"), ("field", "Computer Science")):
        p[key] = fact(value, "REQUIRES_VERIFICATION", [catalogue, regulation],
                      "Official 2026/27 identity only. The degree is Italian/English; the Internet of Things curriculum is fully English. Confirm the 2027/28 offer and curriculum language.")
    p["previous_cycle_tags"] = dict(level="MSc", language="Italian / English", field="Computer Science", cycle="2026-2027", label="Official 2026/27 evidence only; English Internet of Things curriculum within an Italian/English degree; 2027/28 intake unverified")
    p["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", [catalogue, regulation, admission],
                                       "The named offer and regulation cover 2026/27; no 2027/28 first-year offer was identified. The scholarship's second-year renewal and the national visa rule do not verify this course intake; no discontinuation is inferred.")
    p["source_ids"] = [s["id"] for s in SOURCES]
    p["facts"] = {
        "previous_cycle_course_listing": fact({"academic_year": "2026/27", "official_name": "Informatica / Computer Science", "course_code": "NF225", "degree_class": "LM-18", "level": "MSc", "duration_years": 2, "ects": 120, "campus": "Fisciano", "language": "Italian / English", "fully_English_curriculum": "Internet of Things", "teaching_mode": "Conventional, with course-specific attendance arrangements"}, "CONFIRMED", [catalogue, regulation, "SRC-SALERNO-CS-ENGLISH-TRACK", "SRC-SALERNO-CS-CAMPUS"], "This verifies the named 2026/27 degree only. English applies to the IoT curriculum; it is not claimed for every curriculum. Shared facility inventories include Avellino, without establishing an IoT campus change."),
        "previous_cycle_curricula": fact(["Cloud Computing", "Data Science & Machine Learning", "Internet of Things", "Sicurezza Informatica", "Software Engineering & IT Management"], "CONFIRMED", [regulation], "Five curricula in the 2026/27 NF225 regulation only; do not convert individual tracks into additional degree records."),
        "previous_cycle_program_requirements": fact({"academic_year": "2026/27", "degree": "Bachelor's/three-year university diploma or suitable foreign degree", "Italian_classes": ["L-31", "L-8", "corresponding former classes 26/9"], "other_classes_minimum_computing_cfu": 45, "sectors": ["INFO-01/A", "IINF-05/A"], "foreign_degrees": "Individual curriculum coherence assessment", "curricular_gaps": "Must be completed before readiness assessment; enrolment with curricular debt is not allowed", "readiness": "Curriculum analysis and admission assessment", "Italian_L31_L8_test_exemption_minimum_mark": "85/110", "international_assessment": "Document assessment followed by compulsory remote quiz and interview; the Italian-degree exemption does not waive the stated international interview procedure"}, "CONFIRMED", [regulation, admission], "Course-specific 2026/27 regulation and international guidance only. The Italian enrolment page contains a copied reference to the separate Cloud/Security MSc; requirements here use the independent NF225 regulation and English Computer Science page."),
        "previous_cycle_language_requirements": fact({"academic_year": "2026/27", "IoT": "Fully English; English knowledge is mandatory and evidenced in CV/academic records", "previous_English_medium_degree": "No further certificate under course guidance", "Italian": "No Italian certificate for IoT; applicants lacking certified B2 Italian are assigned to IoT", "certificate_caution": "A consulate may require English certification; the course guidance states no universal IELTS/TOEFL minimum", "scholarship": "The separate UNISA Scholarship call requires B2 programme-language evidence", "in_degree_English_exam": "6 CFU with B2 learning target; this is not an across-the-board B2 admission-certificate threshold"}, "CONFIRMED", [admission, regulation, "SRC-SALERNO-SCHOLARSHIP-CALL-2026"], "Prior-cycle course language/assessment guidance only. Scholarship dossier requirements and consular evidence are separate from general academic admission; confirm all three for 2027/28."),
        "previous_cycle_application_windows": fact({"academic_year": "2026/27", "Universitaly_pre_enrolment_deadline": "2026-09-30", "status": "Closed", "general_MSc_enrolment_start": "2026-07-15", "general_MSc_enrolment_deadline": "2027-03-01", "ordinary_assessment_months": ["September", "February"]}, "CONFIRMED", ["SRC-SALERNO-CS-UNIVERSITALY-DEADLINE-2026", "SRC-SALERNO-CS-ENROLMENT-2026", admission], "2026/27 dates only. The March 2027 university enrolment deadline does not reopen the September 2026 international assessment route or establish a 2027/28 application window."),
        "previous_cycle_international_admission": fact({"academic_year": "2026/27", "assessment_portal": "Universitaly", "university_enrolment_portal": PORTAL, "academic_assessment": "Document review, compulsory remote C++/Java/database-query quiz, then interview", "quiz_required_for_interview": True, "two_interview_no_shows": "Rejection", "assessment_contact": "international_incoming@cs.unisa.it", "student_office": "carrierestudenti.di@unisa.it", "teaching_office": "didattica.di@unisa.it", "visa": "Consular application after university academic acceptance; permit application within eight days of arrival under the guidance"}, "CONFIRMED", [admission, "SRC-SALERNO-CS-CONTACT", "SRC-SALERNO-NON-EU-2026"], "Closed prior-cycle assessment process and general university route only. The next course-specific procedures, recognition documents and assessment dates must be verified."),
        "previous_cycle_application_fee": fact(None, "UNAVAILABLE", [admission, fee_reg], "No dedicated international Computer Science assessment fee was established. The 2026/27 regulation states a general €15 test contribution with course exceptions; it is not automatically assigned to this remote quiz/interview."),
        "previous_cycle_tuition": tuition, "previous_cycle_scholarships": scholarship,
        "application_windows": pending_window, "application_fee_2027_2028": pending_fee,
        "tuition_2027_2028": pending_tuition, "scholarships_2027_2028": pending_scholarship,
        "program_specific_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", [regulation, admission], "No course-specific 2027/28 call or requirements were identified; the available regulation is cohort 2026/27."),
        "national_visa_application_deadline_2027_2028": national_visa,
        "available_places": fact(None, "UNAVAILABLE", [catalogue, regulation, admission], "No course-specific 2027/28 intake quota was identified. The 48 UNISA scholarships are university-wide benefit awards, not Computer Science seats."),
        "acceptance_rate": fact(None, "UNAVAILABLE", [regulation, admission], "No complete comparable applicant/admitted totals were identified. Neither scholarship awards nor assessment requirements establish an acceptance rate.")
    }
