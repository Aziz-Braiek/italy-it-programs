# Applicant decision layer — evidence and gaps

Research snapshot: 13 November 2026 (Europe/Rome).

Program availability, original record review dates and application-deadline facts are unchanged: 47 confirmed / 159 awaiting / 3 not offered; 209 programs and 34 universities.

The 47 confirmed programs and their 11 host universities received the priority source review. Eight awaiting Polito records received older-cycle requirements; another 44 awaiting profiles received directly checked older-cycle duration/credit facts. The remaining awaiting-record research is incomplete; no blanket factual-completeness claim is made.

Known values are manually approved in verified-facts.json, with official URLs, academic cycle, field verification date and captured-source hashes. Unknowns say Not confirmed. Passing software checks and a successful HTTP fetch are not factual verification.

Current-cycle evidence totals include partly confirmed fields. The UI labels these Partly confirmed and names the missing components; they must not be read as fully resolved eligibility. Degree structure is displayed separately from intake confirmation. The priority-scope refinement report linked from the homepage separates before/after and full/partial counts.

## Field counts across the full tracker

Program-field rows each total 209; university-field rows each total 34. Scholarship offers are counted individually, including one explicit unknown placeholder for universities without an approved scheme.

| Field | 2027/28 confirmed | Previous cycle only | Not confirmed |
|---|---:|---:|---:|
| program.duration | 29 | 44 | 136 |
| program.ects | 26 | 16 | 167 |
| program.prerequisites | 37 | 10 | 162 |
| program.english_requirement | 34 | 9 | 166 |
| program.admission_test | 10 | 3 | 196 |
| program.selection_method | 17 | 0 | 192 |
| program.minimum_grade | 21 | 0 | 188 |
| program.non_eu_seats | 1 | 0 | 208 |
| program.tuition | 10 | 11 | 188 |
| university.universitaly | 1 | 0 | 33 |
| university.documents | 9 | 0 | 25 |
| university.regional_dsu | 2 | 8 | 24 |
| university.visa_permit | 7 | 0 | 27 |
| university.scholarship_offers | 5 | 7 | 25 |

## Source coverage and limits

Freshly captured official URLs: 517; HTTP 200 responses: 505. Captures include university sites/application portals, official joint-program admissions and regional right-to-study bodies. A transport result alone does not approve a field.

Responses not established as readable by the capture client: 12. Some sources initially failed through resets, TLS errors or timeouts; the EAP application page was subsequently recovered. Other old/broken, access-limited or unreadable sources remain explicit. HTTP 200 can also contain a soft error and does not establish readable admissions content. Successful alternatives were used only where applicable; TLS verification was not disabled. Each latest URL/outcome remains in source-checks.json.

## Normalisation and UI

University logistics, scholarship offers and shared fee/English policies live on university records. Program-specific values and policy references live on program records. Program cards resolve those references; they do not store copies of university logistics. Joint-program and applicant scopes are preserved. The older research observations remain frozen for audit transparency; public eligibility/cost sections use the new canonical decision fields.

Cards show known tuition, English, test and funding facts with cycle/date/source labels; unknown fields collapse into one line. Detail pages retain every field and explicit source conflicts without JavaScript. Yes/no filters accept only the exact current, sourced binary state; conditional rules remain not confirmed for an unspecified applicant. Tuition/funding filters use only current, supported facts. A test's absence is not a no-test exemption. Degree structure never establishes intake or cost/test/funding rules.

CSV adds value, cycle, official URL and verification date columns per decision field. Earlier-cycle values are replaced by Not confirmed while retaining their cycle label; historical amounts and requirements are not exported as actionable data. Existing deadline calculation and calendar logic are unchanged.

## Conflicts and missing records

See source-conflicts.json for exact competing claims, URLs and handling. The complete field-ledger.json includes every field outcome; unverified-fields.json lists each gap and pages checked. record-outcomes.json and the table below cover every program and university explicitly.

## Record outcomes

| Type | Stable ID | Program / university | Current | Previous | Unknown | Review outcome |
|---|---|---|---:|---:|---:|---|
| program | legacy-001 | Computer Science and Engineering | 4 | 1 | 4 | reviewed_with_field_gaps |
| program | legacy-002 | Cyber Risk Strategy and Governance | 6 | 0 | 3 | reviewed_with_field_gaps |
| program | legacy-003 | Artificial Intelligence (study plan within Computer Science and Engineering) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-004 | High Performance Computing Engineering | 4 | 1 | 4 | reviewed_with_field_gaps |
| program | legacy-005 | Biomedical Engineering | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-006 | Mechanical Engineering | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-007 | Aerospace Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-008 | Design & Engineering | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-009 | Architecture | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-010 | Communication Design | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-011 | Computer Engineering | 0 | 3 | 6 | partial_previous_cycle_review |
| program | legacy-012 | Cybersecurity Engineering | 0 | 3 | 6 | partial_previous_cycle_review |
| program | legacy-013 | Data Science and Engineering | 0 | 3 | 6 | partial_previous_cycle_review |
| program | legacy-014 | Automotive Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-015 | Aerospace Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-016 | ICT Engineering for Smart Societies | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-017 | Quantum Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-018 | Architecture Construction City | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-019 | Artificial intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-020 | Computer Science and Engineering — Intelligent Embedded Systems (28Digital track) | 3 | 0 | 6 | reviewed_with_field_gaps |
| program | legacy-021 | Digital Humanities and Digital Knowledge | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-022 | Statistics, Economics and Business — Business Analytics curriculum | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-023 | Global MBA in AI and Manufacturing (Bologna Business School) | 2 | 3 | 4 | reviewed_with_field_gaps |
| program | legacy-024 | Mechanical Engineering for Sustainability | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-025 | Business and Economics (CLaBE) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-026 | Economics and Finance (CLEF) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-027 | Medicine and Surgery | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-028 | Business Management — Green Management and Sustainable Businesses (BBS professional-master track) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-029 | Computer Engineering | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | legacy-030 | Computer Science | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | legacy-031 | Cybersecurity | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | legacy-032 | Data Science | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | legacy-033 | Information Engineering | 7 | 0 | 2 | reviewed_with_field_gaps |
| program | legacy-034 | Aerospace Engineering | 6 | 0 | 3 | reviewed_with_field_gaps |
| program | legacy-035 | Medicine and Surgery (single-cycle degree) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-036 | Psychological Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-037 | Physics of Data | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | legacy-038 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-039 | Artificial Intelligence and Robotics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-040 | Cybersecurity | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-041 | Data Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-042 | Applied Computer Science and Artificial Intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-043 | Ingegneria aeronautica - Aeronautical engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-044 | Sustainable Building Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-045 | Computer Science | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-046 | Artificial Intelligence Systems | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-047 | Data Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-048 | Human-Computer Interaction | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-049 | Cognitive Science | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-050 | International Security Studies | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-051 | Comparative, European and International Legal Studies | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-052 | Computer Science | 2 | 2 | 5 | reviewed_with_field_gaps |
| program | legacy-053 | Cybersecurity | 5 | 1 | 3 | reviewed_with_field_gaps |
| program | legacy-054 | Artificial Intelligence and Data Engineering | 4 | 1 | 4 | reviewed_with_field_gaps |
| program | legacy-055 | Data Science and Business Informatics | 2 | 1 | 6 | reviewed_with_field_gaps |
| program | legacy-056 | Bionics Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-057 | Nuclear Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-058 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-059 | Artificial Intelligence for Science and Technology | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-060 | Data Science for Economics and Health | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-061 | Bioinformatics for Computational Genomics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-062 | Artificial Intelligence for Science and Technology | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-063 | Data Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-064 | Human-Centered Artificial Intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-065 | Artificial Intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-066 | Astrophysics and Space Physics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-067 | International Economics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-068 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-069 | Chemistry | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-070 | Mathematics and Applications | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-071 | Physics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-072 | Data Science and Scientific Computing | 0 | 0 | 9 | not_offered_no_admissions_research |
| program | legacy-073 | Physics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-074 | Computer Science | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-075 | Robotics Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-076 | Data Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-077 | Data Science for Management | 0 | 0 | 9 | not_offered_no_admissions_research |
| program | legacy-078 | Data Science for Finance and Economics (curriculum) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-079 | Data Science for Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-080 | Physics | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-081 | Applied Mathematics | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-082 | Digital Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-083 | Hospitality Innovation and e-Tourism | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-084 | Biology for Translational Research and Precision Medicine | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-085 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-086 | Data Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-087 | Architecture — Architectural Design (iCAD) curriculum | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-088 | Computer Engineering | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-089 | Engineering Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-090 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-091 | Computer Science and Artificial Intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-092 | Computer Science | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-093 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-094 | Computer Engineering | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-095 | Computer Science | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-096 | Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-097 | Computer Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-098 | Computer Science | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-099 | Computer Science and Information Technology | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-100 | Data Analytics for Business and Society | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-101 | Economics, Finance and Sustainability | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-102 | International Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-103 | Comparative International Relations | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-104 | Digital Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-105 | Economics and Business | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-106 | Computer Science – Data Science curriculum | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-107 | Philosophy, International and Economic Studies | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-108 | Artificial Intelligence and High Performance Computing Technologies | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-109 | Stochastics and Data Science | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-110 | Economics | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-111 | Business Administration | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-112 | Language Technologies and Digital Humanities | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-113 | Business and Management | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-114 | Economics and Finance with Data Science | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-115 | Global Law and Transnational Legal Studies | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-116 | Molecular Biotechnology | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-117 | Autonomous Vehicle Engineering (MOVE) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-118 | Industrial Bioengineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-119 | Economics and Finance (LMEF) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-120 | International Relations (English-taught MSc) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-121 | Quantum Science and Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-122 | Architecture and Heritage | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-123 | Medicine and Surgery in English (single-cycle degree) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-124 | Civil and Environmental Engineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-125 | Software: Science and Technology | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | legacy-126 | Finance and Risk Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-127 | Economics and Development | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-128 | Geoengineering | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-129 | Urban and Regional Planning and Design for Sustainability — English-taught curriculum | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-130 | International Relations and European Studies — English-only pathway | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-131 | Sustainable Business for Societal Challenges | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-132 | Computer Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-133 | Economics and Data Science | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-134 | Bioengineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-135 | Electronic Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-136 | Energy Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-137 | Computer Science | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-138 | Computer Engineering | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-139 | Business Administration | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-140 | Ingegneria Aerospaziale | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-141 | Ingegneria Biomedica | 0 | 2 | 7 | partial_previous_cycle_review |
| program | legacy-142 | Ingegneria Gestionale | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-143 | Ingegneria Informatica | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-144 | Design degli Interni | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-145 | Progettazione dell'Architettura | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-146 | Ingegneria Civile - Civil Engineering | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-147 | Ingegneria gestionale | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-148 | Economia e commercio | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-149 | Medicina e chirurgia | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-150 | Giurisprudenza | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-151 | Scienze della comunicazione | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-152 | Ingegneria informatica | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-153 | Medicina e Chirurgia (campus/track unresolved) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-154 | Ingegneria Aerospaziale | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-155 | Scienze politiche e relazioni internazionali | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-156 | Psicologia e Salute | 0 | 1 | 8 | partial_previous_cycle_review |
| program | legacy-157 | Ingegneria Informatica | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-158 | Economics and Finance | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-159 | Psicologia clinica | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-160 | Psicologia dello sviluppo e dell'educazione | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-161 | Ingegneria gestionale — Management Engineering English-taught track | 6 | 0 | 3 | reviewed_with_field_gaps |
| program | legacy-162 | Scienze e tecnologie agrarie | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-163 | Biologia Molecolare | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-164 | Ingegneria informatica | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | legacy-165 | Scienze psicologiche cognitive e psicobiologiche | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-001 | Informatics for Digital Health | 2 | 1 | 6 | reviewed_with_field_gaps |
| program | discovered-002 | History | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-003 | Classical Languages and Literatures and Ancient History | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-004 | Historical Sciences | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-005 | Landscape Studies | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-006 | Religious Studies | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-007 | Local Development | 3 | 0 | 6 | reviewed_with_field_gaps |
| program | discovered-008 | Mobility Studies | 3 | 0 | 6 | reviewed_with_field_gaps |
| program | discovered-009 | Chemical Engineering | 0 | 0 | 9 | reviewed_no_approved_values |
| program | discovered-010 | Mechatronics Engineering | 6 | 0 | 3 | reviewed_with_field_gaps |
| program | discovered-011 | Buddhism and Asian Religions | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-012 | Cultures Littéraires Européennes (CLE) Erasmus Mundus Joint Master's Degree | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-013 | Cyber Security (CSES) – 28DIGITAL Master’s track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-014 | Data Science (DSC) – 28DIGITAL Master’s track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-015 | Fintech (FT) – 28DIGITAL Master’s track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-016 | Human-Computer Interaction and Design with Extended Reality (HCID/XR) – 28DIGITAL track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-017 | Cloud and Networking Infrastructure and HPC (CNIHPC) – 28DIGITAL track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-018 | Intelligent Chips and Systems (ICS) – 28DIGITAL track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-019 | Artificial Intelligence with Affective Computing (AIAC) – 28DIGITAL track | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-020 | Hydrogen Systems and Enabling Technologies (HySET Erasmus Mundus Joint Master) | 7 | 0 | 2 | reviewed_with_field_gaps |
| program | discovered-021 | Maritime Science and Technology | 0 | 0 | 9 | not_offered_no_admissions_research |
| program | discovered-022 | Conservation and Restoration Sciences (CORES Joint Master) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-023 | Data Science | 0 | 1 | 8 | partial_previous_cycle_review |
| program | discovered-024 | Engineering Management | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-026 | Engineering in Computer Science and Artificial Intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-027 | Finance and Insurance | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-028 | Digital Skills for Sustainable Societal Transitions | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-025 | Data Science and Artificial Intelligence | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-029 | Greening Energy Market and Finance (GrEnFIn Erasmus Mundus Joint Master) | 7 | 0 | 2 | reviewed_with_field_gaps |
| program | discovered-030 | Mathematical Engineering – planned English-taught track | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-031 | Management, Finance and Business Analytics (proposed 2027/28) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-032 | Food Safety for Global Health (proposed 2027/28) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-033 | Innovative Technologies in Agriculture (proposed 2027/28) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-035 | Data Analytics and Decision Support (proposed 2027/28) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-036 | Statistical Science (proposed 2027/28) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-034 | Physics for Technology (planned Arqus joint Bachelor's) | 0 | 0 | 9 | awaiting_record_research_incomplete |
| program | discovered-037 | Astrophysics and Cosmology | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-038 | Economic Analysis and Policy | 5 | 0 | 4 | reviewed_with_field_gaps |
| program | discovered-039 | Computer Engineering | 4 | 1 | 4 | reviewed_with_field_gaps |
| program | discovered-040 | Data Science and Business Analytics | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-041 | Artificial Intelligence for Management | 2 | 0 | 7 | reviewed_with_field_gaps |
| program | discovered-042 | Finance – Entrepreneurial Finance | 2 | 1 | 6 | reviewed_with_field_gaps |
| program | discovered-043 | Finance – Finance and Artificial Intelligence | 2 | 1 | 6 | reviewed_with_field_gaps |
| program | discovered-044 | Marketing Management – Analytics and AI for Marketing | 2 | 0 | 7 | reviewed_with_field_gaps |
| university | napoli-federico-ii | Università degli Studi di Napoli Federico II | 1 | 0 | 4 | reviewed_with_field_gaps |
| university | politecnico-bari | Politecnico di Bari | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | politecnico-milano | Politecnico di Milano | 3 | 1 | 1 | reviewed_with_field_gaps |
| university | politecnico-torino | Politecnico di Torino | 1 | 2 | 3 | reviewed_with_field_gaps |
| university | roma-tre | Università degli Studi Roma Tre | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | sapienza | Sapienza Università di Roma | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | tor-vergata | Università degli Studi di Roma Tor Vergata | 3 | 2 | 0 | reviewed_with_field_gaps |
| university | ca-foscari | Università Ca' Foscari Venezia | 0 | 2 | 3 | reviewed_with_field_gaps |
| university | milano-bicocca | Università degli Studi di Milano-Bicocca | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | marche | Università Politecnica delle Marche | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | catania | Università degli Studi di Catania | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | milano-statale | Università degli Studi di Milano | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | laquila | Università degli Studi dell'Aquila | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | insubria | Università degli Studi dell’Insubria | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | bologna | Università di Bologna | 4 | 0 | 2 | reviewed_with_field_gaps |
| university | camerino | Università di Camerino | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | ferrara | Università degli Studi di Ferrara | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | firenze | Università degli Studi di Firenze | 2 | 2 | 1 | reviewed_with_field_gaps |
| university | genova | Università degli Studi di Genova | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | messina | Università degli Studi di Messina | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | modena-reggio | Università degli Studi di Modena e Reggio Emilia | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | padova | Università degli Studi di Padova | 1 | 2 | 2 | reviewed_with_field_gaps |
| university | palermo | Università degli Studi di Palermo | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | parma | Università degli Studi di Parma | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | pavia | Università degli Studi di Pavia | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | perugia | Università degli Studi di Perugia | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | pisa | Università di Pisa | 4 | 1 | 1 | reviewed_with_field_gaps |
| university | salerno | Università degli Studi di Salerno | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | siena | Università degli Studi di Siena | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | torino | Università degli Studi di Torino | 2 | 2 | 1 | reviewed_with_field_gaps |
| university | trento | Università degli Studi di Trento | 3 | 1 | 1 | reviewed_with_field_gaps |
| university | trieste | Università degli Studi di Trieste | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | udine | Università degli Studi di Udine | 0 | 0 | 5 | awaiting_record_research_incomplete |
| university | verona | Università degli Studi di Verona | 0 | 0 | 5 | awaiting_record_research_incomplete |

## Rebuild and validation

Run python scripts/build_research_data.py, python scripts/build_site.py, python scripts/audit_research_data.py, python -m unittest discover -s tests, node scripts/test_site.mjs, and node scripts/test_tracker_ui.mjs. Use scripts/test_live_site.mjs for a protected preview after opening its deployment-specific share link.

No new institutions, alerts or applicant-profile filtering were added. Production deployment is outside this release.
