"""University of Turin course and admissions research, checked 10 November 2026."""

CHECKED = "2026-11-10"
CATALOGUE = "https://en.unito.it/studying-unito/programs/degree-programs/degree-programs-english"
INTERNATIONAL = "https://www.en.unito.it/studying-unito/international-degree-seeking-students/application-international-students"


def source(sid, title, url, cycle, evidence, supports, kind="Official course or admissions source"):
    return {"id": sid, "university_id": "torino", "title": title, "url": url,
            "source_type": kind, "accessed_at": CHECKED, "cycle": cycle,
            "evidence": evidence, "supports": supports}


PROGRAMS = {
    "legacy-108": {
        "name": "Artificial Intelligence and High Performance Computing Technologies",
        "profile": "SRC-UNITO-AIHPC-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/artificial-intelligence-and-high-performance-computing",
        "level": "MSc", "language": "English", "field": "Artificial Intelligence and High Performance Computing",
        "campus": "Turin", "class": "LM-18", "duration": 2, "ects": 120,
        "access": "Free access, subject to curricular requirements and personal-preparation assessment",
        "requirements": "The 2026/27 profile requires an L-31 or equivalent first-cycle degree, curricular adequacy of at least 48 CFU in INFO-01/A and/or IINF-05/A and at least 18 CFU in mathematics, followed by assessment of personal preparation.",
        "talents": True,
    },
    "legacy-109": {
        "name": "Stochastics and Data Science",
        "profile": "SRC-UNITO-STOCH-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/stochastics-and-data-science",
        "level": "MSc", "language": "English", "field": "Statistics, Mathematics and Data Science",
        "campus": "Turin", "class": "LM-40 R", "duration": 2, "ects": 120,
        "access": "Free access with curricular and personal-preparation assessment",
        "requirements": "The 2026/27 profile describes a first-cycle qualification, personal-preparation assessment and at least 36 CFU across listed mathematics, statistics, economics, computer science and physics areas. Exact criteria are annual and must be rechecked.",
        "talents": True,
    },
    "legacy-110": {
        "name": "Economics",
        "profile": "SRC-UNITO-ECON-MSC-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/economics-0",
        "level": "MSc", "language": "English", "field": "Economics",
        "campus": "Turin", "class": "LM-56 R", "duration": 2, "ects": 120,
        "access": "Free access with curricular and personal-preparation assessment",
        "requirements": "The 2026/27 profile describes an eligible first-cycle qualification and committee assessment of curricular requirements and personal preparation; an English interview may be requested. The course-specific annual notice controls.",
        "talents": True,
    },
    "legacy-111": {
        "name": "Business Administration",
        "profile": "SRC-UNITO-BUSADMIN-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/business-administration-3",
        "level": "MSc", "language": "English", "field": "Business Administration and Management",
        "campus": "Turin", "class": "LM-77 R", "duration": 2, "ects": 120,
        "access": "Locally programmed access with an admission test",
        "requirements": "The 2026/27 profile classifies this as restricted-access and requires a selection test. The course is excluded from the unrestricted-program Talents4UniTO call reviewed for 2026/27.",
        "talents": False, "additional_fee": True,
    },
    "legacy-112": {
        "name": "Language Technologies and Digital Humanities",
        "profile": "SRC-UNITO-LTDH-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/language-technologies-and-digital-humanities",
        "level": "MSc", "language": "English", "field": "Language Technologies and Digital Humanities",
        "campus": "Turin", "class": "LM-43 R", "duration": 2, "ects": 120,
        "access": "Free access subject to curricular and personal-preparation assessment",
        "requirements": "The 2026/27 profile requires a suitable first-cycle qualification, curricular credits and adequate preparation, including 18 CFU across specified information-technology and humanities subject groups. The annual call controls.",
        "talents": True,
    },
    "legacy-113": {
        "name": "Business and Management",
        "profile": "SRC-UNITO-BM-BSC-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/business-management",
        "level": "BSc", "language": "English", "field": "Business and Management",
        "campus": "Turin", "class": "L-18 R", "duration": 3, "ects": 180,
        "access": "Restricted selection using SAT and a ranking under the 2026/27 call",
        "requirements": "For 2026/27, candidates preregistered and were ranked using SAT results under the annual selection call; places were quota-limited. The 2027/28 rules are not inferred from this prior cycle.",
        "talents": False, "bachelor_call": True,
    },
    "legacy-114": {
        "name": "Economics and Finance with Data Science",
        "profile": "SRC-UNITO-EFDS-BSC-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/economics-and-finance-data-science",
        "level": "BSc", "language": "English", "field": "Economics, Finance and Data Science",
        "campus": "Turin", "class": "L-33 R", "duration": 3, "ects": 180,
        "access": "Official sources conflict in the 2026/27 profile; the specific 2026/27 SAT call confirms quota-limited ranking",
        "requirements": "The course profile contains conflicting access labels: its summary says locally programmed, while its requirements text says non-programmed/open access. The 2026/27 Rector's SAT call sets finite quotas and a ranking, so the conflict is retained rather than silently resolved.",
        "talents": False, "bachelor_call": True, "access_conflict": True,
    },
    "legacy-115": {
        "name": "Global Law and Transnational Legal Studies",
        "profile": "SRC-UNITO-GLTLS-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/global-law-and-transnational-legal-studies",
        "level": "BSc", "language": "English", "field": "Law and Transnational Legal Studies",
        "campus": "Turin", "class": "L-14 R", "duration": 3, "ects": 180,
        "access": "Free access with TOLC-SU/TARM and English B2 for 2026/27",
        "requirements": "The 2026/27 profile states free access subject to the listed TOLC-SU/TARM assessment and English B2. Annual rules and international qualification checks must be rechecked.",
        "talents": False,
    },
    "legacy-116": {
        "name": "Molecular Biotechnology",
        "profile": "SRC-UNITO-MOLBIOTECH-2026",
        "url": "https://en.unito.it/studying-unito/programs/degree-programs/molecular-biotechnology",
        "level": "MSc", "language": "English", "field": "Molecular Biotechnology",
        "campus": "Turin", "class": "LM-9 R", "duration": 2, "ects": 120,
        "access": "Free access after curricular and academic-preparation assessment",
        "requirements": "The 2026/27 course information requires a suitable first-cycle degree, at least 50 CFU across listed biology and chemistry sectors, at least 10 CFU in physics, mathematics, statistics or informatics, and English B2; personal preparation is assessed.",
        "talents": True,
    },
}


SOURCES = [
    source("SRC-UNITO-EN-PROGRAMS-2026", "Degree programs in English, academic year 2026–2027", CATALOGUE, "2026-2027",
           "The official English-program page labels its list as AY 2026–2027 and includes the reviewed English Bachelor's and Master's candidates. This prior-year list does not establish a 2027/28 first-year offer.",
           ["university.previous_cycle_english_program_inventory", "program.previous_cycle_course_listing"], "Official English-degree catalogue"),
    source("SRC-UNITO-AIHPC-2026", "Artificial Intelligence and High Performance Computing Technologies", PROGRAMS["legacy-108"]["url"], "2026-2027",
           "Identifies the English-taught LM-18 Master's, two years/120 ECTS, in Turin; the 2026/27 entry profile requires L-31 or equivalent, 48 relevant CFU in INFO-01/A and/or IINF-05/A, at least 18 mathematics CFU, and personal-preparation assessment. Any 2027/28 year-two coursework is for an earlier cohort, not proof of a new first-year intake.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-STOCH-2026", "Stochastics and Data Science", PROGRAMS["legacy-109"]["url"], "2026-2027",
           "Identifies an English-taught LM-40 R Master's, two years/120 ECTS, in Turin with free access and assessment; prior-cycle curricular rules specify at least 36 CFU across listed quantitative and related subject areas. The profile's 2027/28 course year concerns second-year study for the 2026/27 cohort.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-ECON-MSC-2026", "Economics Master's degree", PROGRAMS["legacy-110"]["url"], "2026-2027",
           "Identifies an English-taught LM-56 R Master's, two years/120 ECTS, in Turin with free access subject to curricular and personal-preparation review; the page describes application during the prior cycle only.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-BUSADMIN-2026", "Business Administration Master's degree", PROGRAMS["legacy-111"]["url"], "2026-2027",
           "Identifies an English-taught LM-77 R Master's, two years/120 ECTS, in Turin; access is locally programmed and includes a selection test. The restricted classification excludes the course from the 2026/27 unrestricted Talents4UniTO award call.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements", "program.previous_cycle_scholarship_eligibility"], "Official degree profile"),
    source("SRC-UNITO-LTDH-2026", "Language Technologies and Digital Humanities", PROGRAMS["legacy-112"]["url"], "2026-2027",
           "Identifies an English-taught LM-43 R Master's, two years/120 ECTS, in Turin with curricular and preparation assessment; the course lists 18 CFU across designated information-technology and humanities sectors. Its displayed 2027/28 year-two modules do not confirm new first-year entry.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-BM-BSC-2026", "Business and Management Bachelor's degree", PROGRAMS["legacy-113"]["url"], "2026-2027",
           "Identifies an English-taught L-18 R Bachelor's, three years/180 ECTS, in Turin; the 2026/27 route uses SAT selection and a ranking under the annual call.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-EFDS-BSC-2026", "Economics and Finance with Data Science Bachelor's degree", PROGRAMS["legacy-114"]["url"], "2026-2027",
           "Identifies an English-taught L-33 R Bachelor's, three years/180 ECTS, in Turin. The page's summary describes local programmed access while its requirements text describes open access; see the separate 2026/27 Rector's SAT call for the quota and ranking procedure.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_access_classification"], "Official degree profile"),
    source("SRC-UNITO-GLTLS-2026", "Global Law and Transnational Legal Studies", PROGRAMS["legacy-115"]["url"], "2026-2027",
           "Identifies an English-taught L-14 R Bachelor's, three years/180 ECTS, in Turin with free access under the prior-cycle profile; TOLC-SU/TARM and English B2 requirements are listed.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-MOLBIOTECH-2026", "Molecular Biotechnology", PROGRAMS["legacy-116"]["url"], "2026-2027",
           "Identifies an English-taught LM-9 R Master's, two years/120 ECTS, in Turin. Prior-cycle requirements include at least 50 CFU in listed biology/chemistry areas, 10 CFU in physics/mathematics/statistics/informatics, English B2 and preparation assessment. Displayed year-two 2027/28 activities belong to the prior cohort.",
           ["program.previous_cycle_course_listing", "program.previous_cycle_program_requirements"], "Official degree profile"),
    source("SRC-UNITO-MASTER-ADMISSIONS-2026", "International applications for degree-seeking students, AY 2026–2027", INTERNATIONAL, "2026-2027",
           "The official page explicitly labels the procedure AY 2026–2027. Foreign-qualification applicants used Apply@UniTo, could select up to two programs, and paid €60. It lists prior-cycle postgraduate and undergraduate application windows and distinguishes programs with their own procedures; no 2027/28 dates are provided here.",
           ["university.previous_cycle_international_admission", "university.previous_cycle_application_windows", "program.previous_cycle_application_fee"], "Official international admissions page"),
    source("SRC-UNITO-FEES-INTL-2026", "Tuition fees for international students", "https://www.en.unito.it/studying-unito/tuition-fees/tuition-fees-international-students", "2026-2027",
           "For 2026/27, foreign students residing abroad are charged under country GDP-PPP bands; the first instalment is €156 (€16 stamp duty plus €140 regional tax), with comprehensive contributions of €500, €600, €700, €800, €1,000 or €1,500 by band. Eligibility, ISEE pathways, country categories and possible extra course contributions affect the total; this is historical, not a 2027/28 schedule.",
           ["university.previous_cycle_tuition", "program.previous_cycle_tuition"], "Official international tuition page"),
    source("SRC-UNITO-FEES-ADD-2026", "Courses with additional contributions", "https://www.unito.it/didattica/tasse/corsi-con-contributi-aggiuntivi", "2026-2027",
           "The 2026/27 additional-contribution table lists Business and Management Bachelor's and Business Administration Master's with an extra contribution ranging from €400 to €5,100 by ISEE/GDP-PPP band. This is an additional contribution, not total tuition, and is not carried into 2027/28.",
           ["program.previous_cycle_additional_contribution"], "Official additional-contribution table"),
    source("SRC-UNITO-TALENTS-2026", "Talents4UniTO call for applications AY 2026–2027", "https://en.unito.it/sites/sten/files/documenti/2026-01/bando_talents4unito_2026_2027_en.pdf", "2026-2027",
           "The prior-cycle call offers 40 competitive two-year awards of €20,000 total (€10,000 each year) to eligible non-Italian citizens residing abroad with foreign qualifications entering the first year of eligible unrestricted English-taught Master's programs. It lists AI/HPC, Economics, Language Technologies and Digital Humanities, Molecular Biotechnology, and Stochastics and Data Science among eligible programs; Business Administration is excluded as restricted-access. Its AY 2027/28 clause covers renewal by existing 2026/27 awardees entering year two, not new first-year awards.",
           ["university.previous_cycle_scholarships", "program.previous_cycle_scholarship_eligibility"], "Official scholarship call PDF"),
    source("SRC-UNITO-SAT-BACHELOR-2026", "Admission call for selected Bachelor's degrees using SAT, AY 2026–2027", "https://en.unito.it/sites/sten/files/document/2026-04/bando_SME_triennali_SAT_2026_2027.pdf", "2026-2027",
           "The 2026/27 call confirms a SAT-based preregistration and ranking with finite quotas. Business and Management quotas are 200 domestic/EU/equivalent residents, 40 non-EU visa applicants and 10 Marco Polo places; Economics and Finance with Data Science quotas are 195, 50 and 5. Procedure 1 preregistration was 1–19 June 2026 with SAT valid by 6 June; procedure 2 was 1 July–14 September 2026 with SAT valid by 12 September. Economics and Finance with Data Science used a Math score threshold in the first procedure. Historical figures only.",
           ["program.previous_cycle_application_windows", "program.previous_cycle_places", "program.previous_cycle_selection"], "Official Rector's selection call PDF"),
]


def fact(value, status, sources=(), note=None):
    return {"value": value, "status": status, "source_ids": list(sources), "notes": note}


def apply(universities, programs, fact_builder):
    uni = next(u for u in universities if u["id"] == "torino")
    uni.update(
        research_stage="PARTIALLY_RESEARCHED",
        research_summary=REPORT,
        last_checked=CHECKED,
        application_portal_url="https://apply.unito.it/",
        contact_email="internationalstudents@unito.it",
        contact_url=INTERNATIONAL,
    )
    uni["coverage"].update({
        "international_admissions_page_examined": "partial",
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
    if "SRC-UNITO-INTL" not in uni["source_ids"]:
        uni["source_ids"].append("SRC-UNITO-INTL")

    rows = {p["id"]: p for p in programs if p["university_id"] == "torino"}
    for pid, record in PROGRAMS.items():
        p = rows[pid]
        p["program"] = record["name"]
        p["last_checked"] = CHECKED
        p["overall_status"] = "REQUIRES_VERIFICATION"
        p["discovery_source"] = "previous_tracker"
        profile = record["profile"]
        source_ids = [profile, "SRC-UNITO-EN-PROGRAMS-2026", "SRC-UNITO-MASTER-ADMISSIONS-2026",
                      "SRC-UNITO-FEES-INTL-2026", "SRC-UNITO-TALENTS-2026"]
        if record.get("bachelor_call"):
            source_ids.extend(["SRC-UNITO-SAT-BACHELOR-2026", "SRC-UNITO-INTL"])
        if record.get("additional_fee"):
            source_ids.append("SRC-UNITO-FEES-ADD-2026")
        p["source_ids"] = list(dict.fromkeys(source_ids))
        p["level"] = fact_builder(record["level"], "REQUIRES_VERIFICATION", [profile],
                                   "Official 2026/27 course level only; the 2027/28 first-year offer remains unverified.")
        p["language"] = fact_builder(record["language"], "REQUIRES_VERIFICATION", [profile],
                                      "Official 2026/27 course language only; verify against the 2027/28 first-year offer.")
        p["field"] = fact_builder(record["field"], "REQUIRES_VERIFICATION", [profile],
                                  "Subject classification follows the 2026/27 official course profile and has not been revalidated for 2027/28.")
        p["availability_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            [profile, "SRC-UNITO-EN-PROGRAMS-2026", "SRC-UNITO-MASTER-ADMISSIONS-2026"],
            "The latest named offer reviewed is for 2026/27. Any 2027/28 year-two coursework applies to the prior cohort and does not confirm a new first-year intake. No discontinuation is inferred.")
        p["previous_cycle_tags"] = {"level": record["level"], "language": record["language"],
            "field": record["field"], "cycle": "2026-2027",
            "label": "Official 2026/27 profile and admissions context only; 2027/28 first-year availability remains unverified"}
        p["facts"]["previous_cycle_course_identity"] = fact_builder(record["name"], "CONFIRMED", [profile],
            "Official 2026/27 course identity; this does not confirm 2027/28 new-entry availability.")
        p["facts"]["previous_cycle_course_listing"] = fact_builder({
            "academic_year": "2026/27", "official_name": record["name"], "level": record["level"],
            "language": record["language"], "campus": record["campus"], "degree_class": record["class"],
            "duration_years": record["duration"], "ects": record["ects"], "access": record["access"]},
            "CONFIRMED", [profile, "SRC-UNITO-EN-PROGRAMS-2026"],
            "Official 2026/27 profile/catalogue details only; no 2027/28 first-year offer is confirmed.")
        p["facts"]["previous_cycle_program_requirements"] = fact_builder(record["requirements"], "CONFIRMED",
            [profile] + (["SRC-UNITO-SAT-BACHELOR-2026"] if record.get("bachelor_call") else []),
            "Prior-cycle entry rules only. The annual 2027/28 call must be checked before applying.")
        p["facts"]["program_specific_requirements_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            [profile, "SRC-UNITO-MASTER-ADMISSIONS-2026"],
            "No 2027/28 course-specific admission call or requirements were confirmed in the reviewed official sources.")
        p["facts"]["previous_cycle_application_fee"] = fact_builder({"academic_year": "2026/27", "fee_eur": 60,
            "scope": "Foreign-qualification application; up to two programme choices"}, "CONFIRMED",
            ["SRC-UNITO-MASTER-ADMISSIONS-2026"], "This is the 2026/27 fee and must not be assumed for 2027/28.")
        p["facts"]["application_fee_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-MASTER-ADMISSIONS-2026"], "The official page reviewed states €60 for 2026/27 only; no 2027/28 fee was confirmed.")
        p["facts"]["previous_cycle_application_windows"] = fact_builder({
            "academic_year": "2026/27", "international_postgraduate_foreign_qualification": {"opening": "2025-11-25", "closing": "2026-01-29"},
            "international_undergraduate_foreign_qualification": {"opening": "2026-02-19", "closing": "2026-04-15"},
            "scope_note": "The international page lists general foreign-qualification windows; restricted programmes and separate course calls may follow different procedures."},
            "CONFIRMED", ["SRC-UNITO-MASTER-ADMISSIONS-2026"], "All dates are prior-cycle dates and are not rolled forward.")
        if record.get("bachelor_call"):
            p["facts"]["previous_cycle_selection"] = fact_builder({
                "academic_year": "2026/27", "test": "SAT", "procedure": "preregistration followed by a quota-based ranking",
                "quotas": ({"Italy_EU_and_nonEU_residents": 200, "nonEU_visa_applicants": 40, "Marco_Polo": 10}
                           if pid == "legacy-113" else
                           {"Italy_EU_and_nonEU_residents": 195, "nonEU_visa_applicants": 50, "Marco_Polo": 5})},
                "CONFIRMED", ["SRC-UNITO-SAT-BACHELOR-2026"], "2026/27 call only; places and selection may change by year.")
            p["facts"]["previous_cycle_application_windows"]["value"]["SAT_preregistration"] = [
                {"procedure": 1, "opening": "2026-06-01", "closing": "2026-06-19", "SAT_valid_by": "2026-06-06"},
                {"procedure": 2, "opening": "2026-07-01", "closing": "2026-09-14", "SAT_valid_by": "2026-09-12"}]
            if pid == "legacy-114":
                p["facts"]["previous_cycle_access_classification"] = fact_builder({
                    "profile_summary": "Locally programmed", "profile_requirements": "Non-programmed/open access",
                    "2026_2027_call": "SAT preregistration, finite places and ranked selection"}, "CONFLICTING_SOURCES",
                    ["SRC-UNITO-EFDS-BSC-2026", "SRC-UNITO-SAT-BACHELOR-2026"],
                    "The course profile conflicts internally on access. The specific Rector's call confirms quotas and ranking for 2026/27; retain the source conflict rather than treating the summary label as definitive.")
        p["facts"]["application_windows"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-MASTER-ADMISSIONS-2026"] + (["SRC-UNITO-SAT-BACHELOR-2026"] if record.get("bachelor_call") else []),
            "No 2027/28 course-specific opening or deadline was confirmed. 2026/27 dates remain historical only.")
        p["facts"]["previous_cycle_tuition"] = fact_builder({"academic_year": "2026/27",
            "international_fee_framework": "Country GDP-PPP contribution bands; the full contribution depends on the applicant's country and eligible documentation.",
            "first_instalment_eur": 156, "first_instalment_components_eur": {"stamp_duty": 16, "regional_tax": 140},
            "comprehensive_contribution_eur_by_band": [500, 600, 700, 800, 1000, 1500],
            "additional_course_contribution_may_apply": bool(record.get("additional_fee"))}, "CONFIRMED",
            ["SRC-UNITO-FEES-INTL-2026"] + (["SRC-UNITO-FEES-ADD-2026"] if record.get("additional_fee") else []),
            "Historical fee framework only; eligibility, country band, ISEE route and any course surcharge affect the total.")
        p["facts"]["tuition_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-FEES-INTL-2026"], "The latest fee framework reviewed is for 2026/27; no 2027/28 schedule was confirmed.")
        p["facts"]["previous_cycle_scholarships"] = fact_builder({
            "academic_year": "2026/27", "Talents4UniTO": {
                "eligible": bool(record.get("talents")), "scholarships_total": 40, "gross_total_eur": 20000,
                "gross_per_year_eur": 10000, "duration_years": 2,
                "scope": "Competitive award for eligible non-Italian citizens with foreign qualifications resident abroad, entering year one of eligible unrestricted English-taught Master's programmes",
                "listed_for_course": bool(record.get("talents")),
                "2027_2028_clause": "Renewal for existing 2026/27 awardees entering year two only; it is not a new-student 2027/28 call"}},
            "CONFIRMED", ["SRC-UNITO-TALENTS-2026"],
            "Award eligibility and amounts are from the prior-cycle call; competitive and not guaranteed. New 2027/28 incoming-student awards remain unconfirmed.")
        p["facts"]["scholarships_2027_2028"] = fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-TALENTS-2026"], "The 2026/27 call's 2027/28 provision covers renewal for continuing awardees; no new-entry 2027/28 scholarship call was confirmed.")
        if record.get("additional_fee"):
            p["facts"]["previous_cycle_additional_contribution"] = fact_builder({
                "academic_year": "2026/27", "additional_contribution_eur_range": [400, 5100],
                "determination": "ISEE/GDP-PPP band; separate from total tuition"}, "CONFIRMED",
                ["SRC-UNITO-FEES-ADD-2026"], "Historical additional contribution only; not a 2027/28 total-fee quote.")
        p["facts"]["acceptance_rate"] = fact_builder(None, "UNAVAILABLE",
            [profile] + (["SRC-UNITO-SAT-BACHELOR-2026"] if record.get("bachelor_call") else []),
            "No official applicant denominator and admitted-student count were found for a reliable course acceptance rate.")

    uni["cycle_facts"].update({
        "english_program_inventory_2026_2027": fact_builder({
            "catalogue_academic_year": "2026/27", "reviewed_candidates": len(PROGRAMS),
            "bachelors": [PROGRAMS[x]["name"] for x in ("legacy-113", "legacy-114", "legacy-115")],
            "masters": [PROGRAMS[x]["name"] for x in ("legacy-108", "legacy-109", "legacy-110", "legacy-111", "legacy-112", "legacy-116")]},
            "CONFIRMED", ["SRC-UNITO-EN-PROGRAMS-2026"] + [p["profile"] for p in PROGRAMS.values()],
            "The official English catalogue is explicitly 2026/27 and does not establish first-year entry in 2027/28."),
        "foreign_qualification_admissions_2026_2027": fact_builder({
            "portal": "Apply@UniTo", "application_fee_eur": 60, "programme_choices": 2,
            "postgraduate_window": {"opening": "2025-11-25", "closing": "2026-01-29"},
            "undergraduate_window": {"opening": "2026-02-19", "closing": "2026-04-15"},
            "academic_year": "2026/27"}, "CONFIRMED", ["SRC-UNITO-MASTER-ADMISSIONS-2026"],
            "Prior-cycle foreign-qualification workflow only; individual restricted programmes may use their own calls."),
        "bachelor_admissions_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-SAT-BACHELOR-2026"], "The reviewed BSc calls and SAT quotas are for 2026/27; no 2027/28 selection call was confirmed."),
        "master_admissions_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-MASTER-ADMISSIONS-2026"], "The official application page reviewed is labeled AY 2026/27; no 2027/28 MSc calls or dates were confirmed."),
        "application_fee_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-MASTER-ADMISSIONS-2026"], "The €60 amount applies to the 2026/27 foreign-qualification process only."),
        "tuition_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-FEES-INTL-2026", "SRC-UNITO-FEES-ADD-2026"], "Only 2026/27 fee schedules were reviewed; no 2027/28 tuition schedule was confirmed."),
        "scholarships_2027_2028": fact_builder(None, "REQUIRES_VERIFICATION",
            ["SRC-UNITO-TALENTS-2026"], "The reviewed call covers 2026/27 entrants and 2027/28 renewals for existing recipients, not new entrants."),
        "acceptance_rate": fact_builder(None, "UNAVAILABLE", ["SRC-UNITO-SAT-BACHELOR-2026"],
            "The reviewed call publishes quotas but no complete applicant denominator and admitted count; no acceptance rate is inferred."),
    })


BATCH = {
    "id": "unito-program-catalogue-and-admissions-review",
    "status": "partial",
    "result": "Matched all nine University of Turin legacy candidates against its official 2026/27 English-degree catalogue and individual course profiles. Corrected the AI/HPC Master's title; recorded course class, language, duration, campus, historical requirements and access rules. The 2026/27 SAT call supplies finite quotas and dates for Business and Management and Economics and Finance with Data Science; the latter course profile also contains an internal open-versus-programmed access conflict, which is preserved. Recorded the previous-cycle Apply@UniTo route and €60 fee, GDP-PPP-based tuition and course surcharges, and the 2026/27 Talents4UniTO award scope, including that its 2027/28 clause is renewal only. No listed course's 2027/28 new-first-year offer, current admission window, fee schedule or new-entry scholarship call was confirmed. Year-two modules shown for 2027/28 belong to the 2026/27 cohort and were not treated as new intake evidence. No official acceptance-rate denominator was found.",
}

REPORT = "UniTo's official English-degree catalogue and individual profiles reviewed are for 2026/27. The nine legacy candidates now have current-cycle identities and historical course requirements: five Master's courses are eligible under the prior-cycle Talents4UniTO call, while restricted Business Administration is excluded. The profile for Economics and Finance with Data Science conflicts internally on whether access is locally programmed or open; the 2026/27 Rector's SAT call confirms a quota-based ranking, so the inconsistency remains explicit. The prior-cycle international process used Apply@UniTo, €60 for up to two choices and separate Bachelor's/Master's windows. International tuition used country GDP-PPP bands, with an initial €156 payment and comprehensive contributions from €500 to €1,500; Business and Management and Business Administration had additional €400–€5,100 charges by applicable band. The 2026/27 Talents4UniTO call offered competitive two-year awards of €20,000 total to eligible foreign-degree students in unrestricted English Master's courses; its 2027/28 provision concerns renewal of existing winners only. No 2027/28 first-year offer or current admissions, fees or incoming-student scholarship terms were confirmed for any of the nine candidates. Any 2027/28 year-two coursework displayed on prior-cycle profiles applies to students who entered in 2026/27. Acceptance rates were not officially published in the reviewed sources."
