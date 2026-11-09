#!/usr/bin/env python3
"""Build the public 2027–28 dataset from the archived tracker and reviewed sources.

The legacy values are intentionally not copied into active records. They remain in
research/archive/legacy-programs.json as historical input and in Git history.
"""
from __future__ import annotations

import json
import re
import shutil
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
AS_OF = "2026-11-09"
CYCLE = "2027-2028"


UNIVERSITIES = [
    # id, canonical name, city, region, homepage, admissions page, admission status, note
    ("napoli-federico-ii", "Università degli Studi di Napoli Federico II", "Naples", "Campania", "https://www.unina.it/", "https://www.international.unina.it/education/admission-regulation/", "REQUIRES_VERIFICATION", "A program-specific 2027/28 notice was found for Chemical Engineering; remaining historical program rows need individual checks."),
    ("politecnico-bari", "Politecnico di Bari", "Bari", "Apulia", "https://www.poliba.it/", "https://www.poliba.it/en/ammissioni-corsi-di-laurea-di-1deg-livello", "REQUIRES_VERIFICATION", "The official admissions page says 2027/28 first-cycle call instructions are expected in February 2027; program inventory is pending."),
    ("politecnico-milano", "Politecnico di Milano", "Milan", "Lombardy", "https://www.polimi.it/", "https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-magistrale/foreign-qualification/deadlines", "CONFIRMED", "2027/28 MSc application windows, merit scholarships, English requirements and Engineering BSc test/enrolment details are recorded. The official page has an Engineering deadline discrepancy, the current fee schedule is 2026/27, and all 17 historic program rows still need individual cycle checks."),
    ("politecnico-torino", "Politecnico di Torino", "Turin", "Piedmont", "https://www.polito.it/", "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/bachelor-s-degree-programmes/calls-for-application-regulations-and-ranking-lists", "REQUIRES_VERIFICATION", "The 2027/29 HySET joint master intake and November deadline are confirmed; Polito’s broader 2027/28 degree catalogue and its other program records still need review. For bachelor’s access, Polito confirms in-person TOLC@UNI or CEnT@UNI tests; the detailed call is pending."),
    ("roma-tre", "Università degli Studi Roma Tre", "Rome", "Lazio", "https://www.uniroma3.it/", "https://orientamento.uniroma3.it/en/about-roma-tre/international-students-admissions/", "REQUIRES_VERIFICATION", "The official material reviewed covers international admission steps and a 2026/27 guide; 2027/28 degree-level calls remain outstanding."),
    ("sapienza", "Sapienza Università di Roma", "Rome", "Lazio", "https://www.uniroma1.it/", "https://www.uniroma1.it/en/pagina/international-admissions", "REQUIRES_VERIFICATION", "The international admissions material reviewed is still for 2026/27; 2027/28 program-level checks remain outstanding."),
    ("tor-vergata", "Università degli Studi di Roma Tor Vergata", "Rome", "Lazio", "https://web.uniroma2.it/", "https://mechatronics.uniroma2.it/how-to-apply-for-mechatronics/admission-a-y-2027-28/", "CONFIRMED", "The Mechatronics Engineering MSc has a detailed official 2027/28 call; the historic Computer Science row remains unverified."),
    ("ca-foscari", "Università Ca' Foscari Venezia", "Venice", "Veneto", "https://www.unive.it/", "https://www.unive.it/web/en/21001/admission-and-enrolment-with-an-international-qualification", "CONFIRMED", "Official international qualification page states that 2027/28 applications open in December 2026; exact windows and program calls are pending."),
    ("milano-bicocca", "Università degli Studi di Milano-Bicocca", "Milan", "Lombardy", "https://www.unimib.it/", "https://en.unimib.it/study/information-international-students/access-students-international-qualification", "REQUIRES_VERIFICATION", "The international qualifications page describes changes from 2027/28; program calls and dates need review."),
    ("marche", "Università Politecnica delle Marche", "Ancona", "Marche", "https://www.univpm.it/", "https://www.international.univpm.it/become-a-student/enrolment/non-eu-students-applying-for-a-visa/", "REQUIRES_VERIFICATION", "The official international site currently centers on 2026/27 admissions; program-level 2027/28 availability and calls remain outstanding."),
    ("catania", "Università degli Studi di Catania", "Catania", "Sicily", "https://www.unict.it/", "https://www.unict.it/en/node/5251", "REQUIRES_VERIFICATION", "Official sources show Data Science for Management was replaced by the Data Science MSc from 2022/23. Current course, English-program and admission evidence is for 2026/27; no 2027/28 program call, dates, tuition or scholarship call was identified, so the successor intake remains unverified."),
    ("milano-statale", "Università degli Studi di Milano", "Milan", "Lombardy", "https://www.unimi.it/", "https://www.unimi.it/en/study/enrolment", "REQUIRES_VERIFICATION", "The official enrolment page reviewed describes 2026/27 procedures; 2027/28 program calls need review."),
    ("laquila", "Università degli Studi dell'Aquila", "L'Aquila", "Abruzzo", "https://www.univaq.it/", "https://www.univaq.it/en/section.php?id=2065&lang_s=en", "REQUIRES_VERIFICATION", "International admissions page identified; cycle-specific program-level calls remain outstanding."),
    ("insubria", "Università degli Studi dell'Insubria", "Varese", "Lombardy", "https://www.uninsubria.it/", "https://www.uninsubria.it/servizi/vivere-insubria/immatricolarsi-e-iscriversi/immatricolazioni/studenti-non-ue-residenti", "REQUIRES_VERIFICATION", "The non-EU page reviewed describes the prior cycle; 2027/28 offer and program requirements remain outstanding."),
    ("bologna", "Università di Bologna", "Bologna", "Emilia-Romagna", "https://www.unibo.it/", "https://www.unibo.it/en/study/how-to-apply", "REQUIRES_VERIFICATION", "A 2027/28 call is confirmed for the Erasmus Mundus CLE and the English Intelligent Embedded Systems 28DIGITAL track; the rest of the degree inventory remains under review."),
    ("camerino", "Università di Camerino", "Camerino", "Marche", "https://www.unicam.it/", "https://international.unicam.it/admissions/faq", "REQUIRES_VERIFICATION", "The official admissions material reviewed is for 2026/27 or general guidance; 2027/28 program-level checks remain outstanding."),
    ("ferrara", "Università degli Studi di Ferrara", "Ferrara", "Emilia-Romagna", "https://www.unife.it/", "https://www.unife.it/en/come-to-study/enroll/how-to-enroll/arrival-enrolment/enrol-in-a-post-graduate-course", "REQUIRES_VERIFICATION", "Official international postgraduate enrollment guidance was identified, but 2027/28 calls and current program availability remain outstanding."),
    ("firenze", "Università degli Studi di Firenze", "Florence", "Tuscany", "https://www.unifi.it/", "https://www.sst.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=168", "CONFIRMED", "The Software: Science and Technology MSc page gives specific 2027/28 admission requirements; the other historical programs still need verification."),
    ("genova", "Università degli Studi di Genova", "Genoa", "Liguria", "https://unige.it/en", "https://unige.it/en/international-enrolment", "REQUIRES_VERIFICATION", "An official notice says the BSc Maritime Science and Technology will not run in 2027/28. UniGe also announced the planned 2027/28 start of CORES, a new joint MSc whose proposal remains under evaluation; admissions details are pending. Visa preselection dates and fees are also tracked at university level."),
    ("messina", "Università degli Studi di Messina", "Messina", "Sicily", "https://international.unime.it/", "https://international.unime.it/study-us/application-and-admission", "CONFIRMED", "Official 2027/28 international calls publish multiple application windows and a €40 fee for up to two applications. The official catalogue shows Data Science MSc coursework taught in 2027/28 for the 2026/27 cohort; a new 2027/28 first-year intake and its program-specific conditions still need confirmation."),
    ("modena-reggio", "Università degli Studi di Modena e Reggio Emilia", "Modena", "Emilia-Romagna", "https://www.unimore.it/", "https://www.unimore.it/en/internationalisation/foreign-qualification", "REQUIRES_VERIFICATION", "Official international-qualification guidance explains the degree-specific call process; individual 2027/28 calls require further review."),
    ("padova", "Università degli Studi di Padova", "Padua", "Veneto", "https://www.unipd.it/en/", "https://www.unipd.it/en/ammissione-studenti-internazionali", "CONFIRMED", "The 2027/28 international application calls are published; seven program listings on the source page have been verified, while the historic entries remain under review."),
    ("palermo", "Università degli Studi di Palermo", "Palermo", "Sicily", "https://www.unipa.it/", "https://www.unipa.it/mobilita/en/useful-information/faq-international-students/faq-international-students-p2/before-applying/index.html", "NOT_YET_PUBLISHED", "Official FAQ explicitly says exact 2027/28 application dates have not yet been published."),
    ("parma", "Università degli Studi di Parma", "Parma", "Emilia-Romagna", "https://www.unipr.it/en", "https://www.unipr.it/en/node/106538", "NOT_YET_PUBLISHED", "Official 2027/28 page asks international students to register interest and says admissions procedures will be communicated when available."),
    ("pavia", "Università degli Studi di Pavia", "Pavia", "Lombardy", "https://www.unipv.eu/", "https://webing.unipv.eu/home/international/international-applications/", "REQUIRES_VERIFICATION", "Official engineering-faculty international application guidance was examined; the full 2027/28 catalog and calls need review."),
    ("perugia", "Università degli Studi di Perugia", "Perugia", "Umbria", "https://www.unipg.it/", "https://www.unipg.it/en/international-students/becoming-a-unipg-student", "REQUIRES_VERIFICATION", "The official page reviewed still contains 2026 visa procedures; 2027/28 program-level requirements and deadlines remain outstanding."),
    ("pisa", "Università di Pisa", "Pisa", "Tuscany", "https://www.unipi.it/", "https://didattica.di.unipi.it/en/internazionale/degrees-offered-in-english/", "CONFIRMED", "A department call for three English-taught MSc programs publishes 2027/28 eligibility, dates and a €30 application fee; this does not verify all University of Pisa programs."),
    ("salerno", "Università degli Studi di Salerno", "Fisciano", "Campania", "https://www.unisa.it/", "https://web.unisa.it/en/teaching/enrollment/non-eu-citizens-abroad", "REQUIRES_VERIFICATION", "The official non-EU guidance reviewed is not a cycle-specific 2027/28 call; program checks remain outstanding."),
    ("siena", "Università degli Studi di Siena", "Siena", "Tuscany", "https://www.unisi.it/", "https://admission.unisi.it/", "NOT_YET_PUBLISHED", "The official portal says 2027/28 intake opens in November 2026; exact application deadlines and course-specific calls are not published yet."),
    ("torino", "Università degli Studi di Torino", "Turin", "Piedmont", "https://www.unito.it/", "https://www.en.unito.it/studying-unito/international-degree-seeking-students/application-international-students", "REQUIRES_VERIFICATION", "The international application page reviewed is for 2026/27; 2027/28 course inventory, fees and deadlines need review."),
    ("trento", "Università degli Studi di Trento", "Trento", "Trentino-Alto Adige", "https://www.unitn.it/en", "https://www.unitn.it/en/international/coming-unitrento/admission-how-it-works", "REQUIRES_VERIFICATION", "Seven 28DIGITAL master's tracks have 2027/28 evidence; the department and central consortium pages disagree on application-round boundaries. Other listed degrees remain under review."),
    ("trieste", "Università degli Studi di Trieste", "Trieste", "Friuli-Venezia Giulia", "https://portale.units.it/en", "https://portale.units.it/en/study/application", "REQUIRES_VERIFICATION", "The application page is general; 2027/28 program calls, fees and dates remain outstanding."),
    ("udine", "Università degli Studi di Udine", "Udine", "Friuli-Venezia Giulia", "https://www.uniud.it/en", "https://www.uniud.it/en/education/info-for/how-to-apply/how-to-apply?set_language=en", "REQUIRES_VERIFICATION", "The official page says detailed yearly rules are published in the June Prospectus; 2027/28 program availability and calls remain outstanding."),
    ("verona", "Università degli Studi di Verona", "Verona", "Veneto", "https://www.univr.it/en/", "https://www.univr.it/en/our-services/international-degree-seeking-students", "REQUIRES_VERIFICATION", "The reviewed official page gives 2026/27 international MSc application information; 2027/28 programs and calls remain outstanding."),
]

ALIASES = {
    "Federico II Napoli": "napoli-federico-ii",
    "Politecnico di Bari": "politecnico-bari",
    "Politecnico di Milano": "politecnico-milano",
    "Politecnico di Torino": "politecnico-torino",
    "Roma Tre": "roma-tre",
    "Sapienza Università di Roma": "sapienza",
    "Tor Vergata Roma": "tor-vergata",
    "Università Ca' Foscari Venezia": "ca-foscari",
    "Università Milano-Bicocca": "milano-bicocca",
    "Università Politecnica delle Marche": "marche",
    "Università degli Studi di Catania": "catania",
    "Università degli Studi di Milano": "milano-statale",
    "Università dell'Aquila": "laquila",
    "Università dell'Insubria": "insubria",
    "Università di Bologna": "bologna",
    "Università di Camerino": "camerino",
    "Università di Ferrara": "ferrara",
    "Università di Firenze": "firenze",
    "Università di Genova": "genova",
    "Università di Messina": "messina",
    "Università di Modena e Reggio Emilia": "modena-reggio",
    "Università di Padova": "padova",
    "Università di Palermo": "palermo",
    "Università di Parma": "parma",
    "Università di Pavia": "pavia",
    "Università di Perugia": "perugia",
    "Università di Pisa": "pisa",
    "Università di Salerno": "salerno",
    "Università di Siena": "siena",
    "Università di Torino": "torino",
    "Università di Trento": "trento",
    "Università di Trieste": "trieste",
    "Università di Udine": "udine",
    "Università di Verona": "verona",
}

SOURCES = [
    {"id":"SRC-PADUA-INTL-2027","university_id":"padova","title":"Admission of international students – How to apply","url":"https://www.unipd.it/en/ammissione-studenti-internazionali","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"First application call for most programs opens 15 September 2026 and closes 15 November 2026; bachelor's entry normally requires 12 years of schooling; master's applicants need a relevant bachelor’s degree and program-specific requirements; English-taught degrees use apply.unipd.it.","supports":["university.application_window","university.non_eu_process","university.bachelor_entry","university.master_entry"]},
    {"id":"SRC-PADUA-PROGRAMS-2027","university_id":"padova","title":"International students – 2027/28 applications (DiSSGeA)","url":"https://www.dissgea.unipd.it/en/en/international-students-202728-applications","source_type":"Official department admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Lists History (Bachelor’s), Classical Languages and Literatures and Ancient History, Historical Sciences, Landscape Studies, Religious Studies, Local Development and Mobility Studies, and gives calls 15 Sep–15 Nov 2026, 1 Dec 2026–1 Mar 2027, and 1 Apr–1 Jun 2027 for EU and non-EU residents in Italy only.","supports":["program.availability","program.name","program.level","program.language","program.deadlines"]},
    {"id":"SRC-POLIMI-DEADLINES-2027","university_id":"politecnico-milano","title":"Deadlines – Admission to Laurea Magistrale with foreign qualification","url":"https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-magistrale/foreign-qualification/deadlines","source_type":"Official admissions deadlines page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For September 2027 MSc entry, the page gives general 2027/28 windows of 1 Oct–1 Dec 2026 (early bird), 12–28 Jan 2027 and 1–18 Mar 2027 for EEA and certain non-EEA residents in Italy. Architecture/Design has its own table with a 1 Oct 2026–28 Jan 2027 general call and the same additional March call. A separate Engineering subsection labelled 2026/27 nevertheless describes the September 2027 intake and gives 12 Jan–25 Feb 2027, creating a cycle/date discrepancy that must be resolved by study area. Fees are €50 early bird or €150 standard, and candidates may apply to at most two programmes.","supports":["university.application_window","university.application_fee","university.non_eu_process"]},
    {"id":"SRC-POLIMI-BSC-2027","university_id":"politecnico-milano","title":"Engineering BSc enrolment – 2027/28","url":"https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-programmes/engineering/enrolment","source_type":"Official admissions and enrolment page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Publishes the 2027/28 Engineering BSc enrolment calendar: first phase 3 May–10 June 2027 (restricted eligibility and excludes English-taught programmes); preference deadlines for later phases are 17 June, 22 July and 26 August 2027, followed by rankings and enrolment deadlines. The page covers enrolment timing, not the pending cycle-specific Engineering call or total tuition amount. Dates are CEST.","supports":["university.bachelor_application_windows"]},
    {"id":"SRC-POLIMI-ENGLISH-2027","university_id":"politecnico-milano","title":"Documents required by the Admissions Office – English certification","url":"https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-magistrale/foreign-qualification/application/list-of-documents-required-by-the-admissions-office","source_type":"Official international admissions requirements page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Gives 2027/28 English certificate scores for MSc applicants: TOEFL iBT at least 78 for tests through 20 Jan 2026 and at least 4.5 from 21 Jan 2026; TOEIC at least 785 Listening/Reading and 310 Speaking/Writing; IELTS at least 6; specified Cambridge, Trinity, Pearson and LanguageCert scores. Applicants whose bachelor’s was taught in English for at least three years may be exempt if their university certifies at least 75% of courses were in English.","supports":["university.english_certificates","university.masters_entry"]},
    {"id":"SRC-POLIMI-SCHOLARSHIPS-2027","university_id":"politecnico-milano","title":"Merit Based Call for Applications – A.Y. 2027–2028","url":"https://www.polimi.it/fileadmin/user_upload/futuri_studenti/borse-di-studio/Merit_Based_Call_For_Applications_a.y._2027-2028.pdf","source_type":"Official 2027/28 scholarship call PDF","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Offers 10 Platinum (€10,000 gross), 18 Gold (€8,000 gross), 16 Piacenza Gold (€5,000 gross), 10 Piacenza Bronze (€2,500 gross), and 10 Silver awards (tuition waiver at Cremona, Lecco, Mantova and Piacenza); all include a tuition waiver for the award year. Eligible applicants must be international first-year MSc applicants to English-taught programs for 2027/28 and must have paid the admission application fee during 1 Oct–1 Dec 2026. Scholarship forms are accepted 1 Oct–15 Dec 2026 at noon Italian time. Awards are competitive and subject to admission and acceptance conditions.","supports":["university.scholarships","university.scholarship_deadline","university.scholarship_eligibility"]},
    {"id":"SRC-POLIMI-ENGINEERING-CALL-2027","university_id":"politecnico-milano","title":"Engineering BSc admissions – 2027/28 call publication status","url":"https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-programmes/engineering","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For first-year Engineering BSc programs in 2027/28, the page says the admission call will be published shortly. It describes the required admission test and non-Italian qualification documentation but does not yet provide the complete 2027/28 call rules, full seat inventory, or all deadlines.","supports":["university.bachelor_call_status","university.bachelor_entry"]},
    {"id":"SRC-POLIMI-CENTS-2027","university_id":"politecnico-milano","title":"CEnT-S – admission to Engineering BSc 2027/28","url":"https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-programmes/engineering/cent-s","source_type":"Official test requirements and deadlines page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For Engineering BSc entry in 2027/28, the page describes the English-language CEnT-S test (55 questions/110 minutes overall; Polimi uses Mathematics, reasoning on texts/data and Physics, 35 questions/70 minutes) and score-recording deadlines. For final-year or already graduated applicants taking a test from 1 Sep 2026 through 3 Jun 2027, the recording deadline is 3 Jun 2027 at 11:59 a.m. A separate 3 Jun deadline applies to the specified 2025/26 penultimate-year cohort that missed the prior recording deadline.","supports":["university.bachelor_admission_test","university.bachelor_test_deadline"]},
    {"id":"SRC-POLIMI-TUITION-2027","university_id":"politecnico-milano","title":"Tuition fees – current published fee schedule","url":"https://www.polimi.it/en/students/tuition-fees-scholarships-and-financial-aid/tuition-fees","source_type":"Official tuition and financial aid page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"The fee page currently labels its detailed fee structure as Academic Year 2026/2027, including regional tax brackets and an annual contribution range. It does not establish the 2027/28 tuition amount; 2026/27 amounts are not carried forward as current-cycle fees.","supports":["university.tuition_publication_status","university.fee_conditions"]},
    {"id":"SRC-POLIMI-CONTACTS","university_id":"politecnico-milano","title":"Contacts for international prospective students","url":"https://www.polimi.it/en/prospective-students/contacts/contacts-for-international-prospective-students","source_type":"Official international contacts page","accessed_at":AS_OF,"cycle":"general","evidence":"Routes international prospective students to the official enquiry form/Online Services rather than publishing a general admissions email. It distinguishes undergraduate applicants from postgraduate applicants and provides the relevant contact pathways.","supports":["university.admissions_contact","university.application_support"]},
    {"id":"SRC-POLITO-HYSET-2027","university_id":"politecnico-torino","title":"HySET applications open for the 2027–2029 edition","url":"https://hysetmaster.polito.it/news/join-hyset-applications-open-for-2027-29","source_type":"Official joint-master admissions announcement","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official announcement says the fifth HySET edition covers academic years 2027–2029 and opened 1 October 2026; the application deadline is 15 November 2026. HySET is jointly coordinated by Politecnico di Torino and Politecnico di Milano with international consortium partners.","supports":["program.availability","program.name","program.application_window"]},
    {"id":"SRC-POLITO-HYSET-REQ-2027","university_id":"politecnico-torino","title":"HySET admission requirements","url":"https://hysetmaster.polito.it/admission-requirements","source_type":"Official joint-master admission requirements","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Requires a relevant bachelor’s degree of at least 180 ECTS in listed engineering/science fields; minimum English evidence is TOEFL iBT 90 with at least 21 in each section, IELTS 6.5 overall with at least 6.0 each section, or Cambridge 160 (higher threshold for a TU/e destination). Selection is scored on academic achievements, background relevance, references/video, and experience. The current page states a 2027–29 call is open.","supports":["program.requirements","program.english_requirement","program.selection_criteria"]},
    {"id":"SRC-POLITO-HYSET-CURRICULUM","university_id":"politecnico-torino","title":"HySET programme structure and awarded degrees","url":"https://hysetmaster.polito.it/hyset-in-a-nutshell","source_type":"Official joint-master programme page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes a 120-ECTS four-semester master’s, with first-year entry allocated between Politecnico di Torino and Politecnico di Milano and second-year mobility to a consortium partner. Depending on the partner route, students earn two master’s degrees; the programme focuses on the hydrogen value chain.","supports":["program.level","program.duration","program.campus","program.degree_awards"]},
    {"id":"SRC-POLITO-HYSET-ENGLISH","university_id":"politecnico-torino","title":"HySET frequently asked questions – language of instruction","url":"https://hysetmaster.polito.it/faq","source_type":"Official joint-master FAQ","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States that the entire HySET programme is taught in English.","supports":["program.language"]},
    {"id":"SRC-POLITO-HYSET-FEES-2027","university_id":"politecnico-torino","title":"HySET continuation beyond 2026 – funding and admissions","url":"https://hysetmaster.polito.it/news/programme-continuation-beyond-2026-funding-and-admissions","source_type":"Official joint-master funding update","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States that funding for the 2027 cohort had not yet been secured and future scholarships depend on a successful external funding award; scholarship availability is not guaranteed. The separate self-funded page states annual fees of €4,500 for European students and €9,000 for non-European students.","supports":["program.scholarships","program.tuition"]},
    {"id":"SRC-POLITO-HYSET-SELF-FUNDED","university_id":"politecnico-torino","title":"HySET self-funded students – tuition fees","url":"https://hysetmaster.polito.it/self-funded-students","source_type":"Official joint-master tuition page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Lists self-funded tuition as €4,500 per year (€9,000 total) for European students and €9,000 per year (€18,000 total) for non-European students; living costs and travel between partner universities are excluded. Payment details/deadlines are to be provided later.","supports":["program.tuition","program.payment_structure"]},
    {"id":"SRC-PISA-CALL-2027","university_id":"pisa","title":"International admissions call 2027/28 – English MSc programs","url":"https://didattica.di.unipi.it/wp-content/uploads/sites/2/2026/11/Bando2026_corsi_internazionali.pdf","source_type":"Official PDF admission call","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Department call lists MSc Computer Science, Data Science and Business Informatics, and Informatics for Digital Health. For non-EU applicants residing abroad it gives an application deadline of 1 February 2027 (Anywhere on Earth), notification on 1 March 2027, and a €30 fee per application (up to two). Tuition for 2027/28 is not specified; the call says annual fees are usually announced in June. No seats or acceptance rates are published in this call.","supports":["program.availability","program.deadline","program.application_fee","program.competitiveness","university.tuition"]},
    {"id":"SRC-PISA-CS","university_id":"pisa","title":"Master programme in Computer Science","url":"https://didattica.di.unipi.it/en/master-programme-in-computer-science/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official page describes the English-taught MSc Computer Science and links to international admissions. Cycle availability is confirmed separately by the 2027/28 department call.","supports":["program.name","program.level","program.language"]},
    {"id":"SRC-PISA-DSBI","university_id":"pisa","title":"Master programme in Data Science and Business Informatics","url":"https://didattica.di.unipi.it/en/master-programme-in-data-science-and-business-informatics/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official page describes the English-taught MSc. Cycle availability is confirmed separately by the 2027/28 department call.","supports":["program.name","program.level","program.language"]},
    {"id":"SRC-PISA-DH","university_id":"pisa","title":"Master programme in Informatics for Digital Health","url":"https://didattica.di.unipi.it/en/master-programme-in-informatics-for-digital-health/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes an English-taught open-admission MSc and links to foreign-student enrollment for AY 2027/28. The department call confirms cycle availability.","supports":["program.name","program.level","program.language","program.access_type"]},
    {"id":"SRC-UNIME-2027","university_id":"messina","title":"Application and Admission – 2027/28","url":"https://international.unime.it/study-us/application-and-admission","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Publishes 2027/28 application rounds for international candidates and a €40 fee for up to two program applications; English certificates are generally B2 unless exempt; program details and eligibility must be checked individually.","supports":["university.application_window","university.application_fee","university.english_requirement","university.non_eu_process"]},
    {"id":"SRC-UNIME-DS-COURSE-ICT-2027","university_id":"messina","title":"Course Catalogue – Data Science, Big Data (ICT curriculum), 2027/28","url":"https://unime.coursecatalogue.cineca.it/af/2027?ad=A001855&annoOrdinamento=2026&coorte=2026&corso=9237R&linguaCC=EN&pds=110","source_type":"Official online course catalogue","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Names DATA SCIENCE as a Master or equivalent second-cycle course, taught in English in Messina. The page is for Year 2, enrollment cohort 2026/27, and lists Big Data for academic year 2027/28; it confirms ongoing second-year teaching, not a new first-year intake for 2027/28.","supports":["program.name","program.level","program.language","program.academic_year_course_offering"]},
    {"id":"SRC-UNIME-DS-COURSE-ECONOMY-2027","university_id":"messina","title":"Course Catalogue – Data Science, Big Data and Artificial Intelligence (Economy curriculum), 2027/28","url":"https://unime.coursecatalogue.cineca.it/af/2027?ad=A001898&annoOrdinamento=2026&coorte=2026&corso=9237R&linguaCC=EN&pds=120","source_type":"Official online course catalogue","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Names DATA SCIENCE as a Master or equivalent second-cycle course, taught in English in Messina. The page is for Year 2, enrollment cohort 2026/27, and lists Big Data and Artificial Intelligence for academic year 2027/28; it confirms ongoing second-year teaching, not a new first-year intake for 2027/28.","supports":["program.name","program.level","program.language","program.academic_year_course_offering"]},
    {"id":"SRC-UNIME-ENGLISH-PROGRAMS","university_id":"messina","title":"English-taught Programmes","url":"https://international.unime.it/study-us/english-taught-programmes","source_type":"Official English-taught degree inventory","accessed_at":AS_OF,"cycle":"general","evidence":"Current official English-programme inventory includes the Master's Degree in Data Science and describes its ICT, economics and forensics options. The page does not specify a 2027/28 admission intake.","supports":["university.english_program_inventory","program.name","program.language"]},
    {"id":"SRC-UNIME-MASTERS-PROGRAMS","university_id":"messina","title":"Master's Degree Programmes","url":"https://international.unime.it/study-us/masters-degrees","source_type":"Official degree inventory","accessed_at":AS_OF,"cycle":"general","evidence":"Current official master's inventory lists Data Science as an English-taught degree in Messina. The page explains that enrolment requires curricular-requirement and personal-preparation review, including an admission letter after international pre-evaluation; it does not specify the 2027/28 intake.","supports":["university.masters_program_inventory","program.name","program.language","program.admissions_route"]},
    {"id":"SRC-UNIME-DS-PAGE","university_id":"messina","title":"Data Science – Official degree page","url":"https://international.unime.it/didattica/corsi-di-laurea-magistrale/data-science","source_type":"Official degree page","accessed_at":AS_OF,"cycle":"general","evidence":"Current official degree page describes the Data Science master's course and study plan, with access requirements presented on the page. It is not dated for the 2027/28 first-year intake and cannot alone confirm 2027/28 admission requirements or availability.","supports":["program.name","program.study_plan","program.requirements"]},
    {"id":"SRC-UNICT-DSM-LEGACY","university_id":"catania","title":"Data Science for Management – course page and replacement notice","url":"https://www.dei.unict.it/corsi/lm-91","source_type":"Official historical degree page","accessed_at":AS_OF,"cycle":"2022-2023","evidence":"The official course page states that starting October 2022 (AY 2022/23), Data Science for Management would be replaced by the new Data Science course and enrollment for 2022/23 would be possible only in the new course.","supports":["program.historical_course_status","program.replacement"]},
    {"id":"SRC-UNICT-DS-PROGRAM-2026","university_id":"catania","title":"Data Science – 2026/27 degree page","url":"https://www.unict.it/en/node/32509","source_type":"Official degree page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"Lists Data Science for Academic Year 2026/27 as a two-year Master's Degree, class LM/DATA, taught in English, at Catania. This is prior-cycle evidence only and does not confirm the 2027/28 intake.","supports":["program.name","program.level","program.duration","program.language","program.location"]},
    {"id":"SRC-UNICT-ENGLISH-MASTERS-2026","university_id":"catania","title":"Master's Degree programmes taught in English","url":"https://www.unict.it/en/node/25736","source_type":"Official English-taught degree inventory and admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"Lists ten English-taught Master's Degree courses including Data Science (LM-DATA), and states that the non-EU abroad call for the 2026/27 academic year is published. This page does not publish a 2027/28 call.","supports":["university.english_program_inventory","program.name","program.language","university.latest_published_call_cycle"]},
    {"id":"SRC-UNICT-MASTER-CALLS-INDEX","university_id":"catania","title":"Master's admissions call archive","url":"https://www.unict.it/ammissioni-ai-corsi-di-laurea-magistrale/numero-programmato","source_type":"Official admissions call archive","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The archive page displays 2026/27 as its latest listed academic year (including the non-EU English-taught Master's call) and older calls; no 2027/28 Master's call is listed on the page checked on 9 November 2026. The page does not explicitly state that a 2027/28 call will not be published.","supports":["university.application_call_archive","university.latest_published_call_cycle"]},
    {"id":"SRC-UNICT-MASTER-ADMISSION-2026","university_id":"catania","title":"First-year admission procedure for non-programmed two-year Master's courses, 2026/27","url":"https://www.unict.it/it/corsi-numero-non-programmato/2026-2027/procedura-di-ammissione-al-1%C2%B0-anno-corsi-di-laurea-magistrale","source_type":"Official Master's admissions procedure","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The 2026/27 procedure lists Data Science (LM-DATA) among the two-year Master's courses. It is a prior-cycle admissions source and cannot establish a 2027/28 intake or deadline.","supports":["program.name","program.level","program.admissions_route"]},
    {"id":"SRC-UNICT-DS-CALL-2026","university_id":"catania","title":"Public selection for admission of non-EU students abroad to English-taught Master's degrees, 2026/27","url":"https://www.unict.it/it/corsi-numero-programmato/2026-2027/public-selection-admission-non-eu-students-living-abroad-english","source_type":"Official non-EU admissions call","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The 2026/27 selection lists Data Science (LM-DATA), for non-EU students living abroad applying to the first year of ten English-taught Master's degrees. It gives an application period of 10 February–17 March 2026, a €10 fee per course, and selection based on qualifications and, where applicable, an interview or test. These conditions apply to the prior cycle only; the table does not publish places for Data Science.","supports":["program.prior_cycle_admission","program.application_window","program.application_fee","program.selection_criteria","program.available_places"]},
    {"id":"SRC-UNICT-BACHELORS-INTERNATIONAL-2026","university_id":"catania","title":"Bachelor's Degrees – international qualification requirements","url":"https://www.unict.it/it/node/1304","source_type":"Official Bachelor's admissions guidance","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"Guidance reviewed for 2026/27 states general first-cycle entry requires a foreign secondary qualification after at least 12 years of schooling, suitable comparable-country access and any required country entrance exam; it describes B2 Italian or an accepted test for non-EU students and a 31 July 2026 Universitaly pre-enrolment deadline. These prior-cycle procedures are not carried forward to 2027/28.","supports":["university.bachelor_entry","university.non_eu_process","university.bachelor_application_deadline"]},
    {"id":"SRC-UNICT-FEES-2026","university_id":"catania","title":"Manifesto degli studi and student contribution rules, 2026/27","url":"https://www.unict.it/en/node/32717","source_type":"Official fee and student-regulations publication notice","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The latest fee-regulation notice located is for 2026/27. It reports contributions up to €2,150 for regular students meeting credit conditions and €2,350 for irregular students, with 2026/27 installment dates; none of these amounts or dates is treated as a 2027/28 fee schedule.","supports":["university.prior_cycle_tuition","university.tuition_publication_status","university.fee_conditions"]},
    {"id":"SRC-UNICT-SCHOLARSHIPS-2026","university_id":"catania","title":"University of Catania Scholarships 2026/27","url":"https://www.unict.it/it/node/31838","source_type":"Official international scholarship call notice","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The 2026/27 call offered five two-year scholarships of €2,000 per year for each of ten English-taught Master's degrees, including Data Science, with a 17 March 2026 deadline for non-EU applicants living abroad. This is prior-cycle information and no recurring 2027/28 award is inferred.","supports":["university.prior_cycle_scholarships","university.scholarship_publication_status"]},
    {"id":"SRC-UNIGE-2027","university_id":"genova","title":"UniGeApply International Admissions","url":"https://unige.it/en/international-enrolment","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"2027/28 non-EU visa preselection is expected mid-December 2026 through end-March 2027; exact dates await publication. €30 fee covers up to two assessment applications. English-taught programs do not require Italian.","supports":["university.application_window_expected","university.application_fee","university.english_requirement"]},
    {"id":"SRC-UNIGE-MST-2027","university_id":"genova","title":"Maritime Science and Technology – degree programme not offered in 2027/28","url":"https://corsi.unige.it/en/corsi/11929/news/attivazione-MST-2027-28","source_type":"Official program-cycle notice","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"UniGe notice dated 18 September 2026 explicitly says the BSc Maritime Science and Technology will not be offered for 2027/28 and first-year enrollment will not be possible in that academic year.","supports":["program.availability","program.not_offered"]},
    {"id":"SRC-UNIGE-CORES-2027","university_id":"genova","title":"CORES Joint Master Degree – planned 2027/28 start","url":"https://life.unige.it/index.php/presentazione-cores-mag2026","source_type":"Official university programme announcement","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"UniGe announced the joint Master’s degree Conservation and Restoration Sciences (CORES), coordinated by UniGe with four European partner universities, with admissions planned to open in early 2027 and a planned start in academic year 2027/28. The Erasmus Mundus Joint Master proposal was still under evaluation, so formal approval, call terms and exact dates were not yet confirmed.","supports":["program.planned_availability","program.application_opening_expected"]},
    {"id":"SRC-UNITRENTO-28DIGITAL-2027","university_id":"trento","title":"28DIGITAL Master School at UniTrento – technical majors and 2027/28 intake","url":"https://www.disi.unitn.it/eit-digital","source_type":"Official department and program admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the UniTrento 28DIGITAL offer as two-year, 120-ECTS double-degree master’s study with technical majors in Information Engineering (Cloud and Network Infrastructures and HPC; Intelligent Chips and Systems), Computer Science (Cyber Security, Data Science, Fintech, Human-Computer Interaction & Design with extended reality), and Artificial Intelligence Systems (Artificial Intelligence with Affective Computing). For the 2027/28 intake it lists three application periods: 31 Oct–11 Feb open to EU/EEA/CH and non-EU applicants; 11 Feb–15 Apr open to EU/EEA/CH and non-EU Italian residents, with visa timing limitations; and 15 Apr–1 Jun open to EU/EEA/CH and non-EU Italian residents. The page says not all trajectories may be available in period two, central selection is handled by 28DIGITAL, and consortium scholarships are first-come-first-served. UniTrento's additional double-degree scholarships are for second-year entrants who receive no other 28DIGITAL grant; their call is indicatively published in August.","supports":["program.duration","program.technical_major","program.application_windows","program.admissions_route","program.scholarships"]},
    {"id":"SRC-28DIGITAL-ADMISSIONS-2027","university_id":"trento","title":"28DIGITAL Master School – 2027 admission dates and criteria","url":"https://masterschool.28digital.eu/admissions","source_type":"Official joint-master admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Lists 2027 application periods as 30 Oct 2026–31 Jan 2027, 1 Feb–18 Apr 2027 and 19 Apr–31 May 2027, with applicant-category/visa restrictions by round. States all 28DIGITAL programmes are taught in English; applicants need a relevant bachelor’s degree of at least 180 ECTS and English proficiency, generally IELTS 6.5 with section minimums or TOEFL iBT scores depending on test scale/date. The University of Trento department’s 2027/28 intake page publishes different round boundaries; treat the university-level date comparison as conflicting and use each programme’s central portal before applying.","supports":["program.availability","program.language","program.requirements","program.application_windows","program.admissions_route"]},
    {"id":"SRC-28DIGITAL-FEES-2027","university_id":"trento","title":"28DIGITAL Master School – tuition fees and scholarships","url":"https://masterschool.28digital.eu/admissions/fees","source_type":"Official joint-master fees and funding page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Lists €75 non-refundable application fee per application, €250 non-refundable registration deposit credited to first-semester tuition, and tuition of €6,000 per academic year for EU/EEA citizens or €18,000 for non-EU/EEA citizens. General merit-based awards include full or half tuition waivers; additional excellence scholarships with living allowance are restricted to EU/EEA and associated-country citizens in selected programs. Period 1, 2 and 3 tuition-payment expected deadlines are 31 May, 30 June and 19 July 2027, respectively.","supports":["program.application_fee","program.registration_fee","program.tuition","program.scholarships","program.tuition_payment_deadline"]},
    {"id":"SRC-28DIGITAL-CYBER-2027","university_id":"trento","title":"Cyber Security (CSES) – 28DIGITAL Master School","url":"https://masterschool.28digital.eu/cyber-security","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the two-year Cyber Security master’s track, names the University of Trento as a partner, gives relevant bachelor fields and states the 2027 first-period deadline is 31 January. The programme page says central 28DIGITAL selection applies.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-28DIGITAL-DSC-2027","university_id":"trento","title":"Data Science (DSC) – 28DIGITAL Master School","url":"https://masterschool.28digital.eu/data-science","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the Data Science master’s, two-year entry/exit double-degree structure, relevant bachelor fields, at least 60 ECTS in computer science/computer architecture and 30 ECTS in mathematics, and the 2027 first-period deadline of 31 January. UniTrento lists itself as an exit point for this track.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-28DIGITAL-FINTECH-2027","university_id":"trento","title":"Fintech (FT) – 28DIGITAL Master School","url":"https://masterschool.28digital.eu/fintech","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the Fintech master’s, relevant bachelor fields, two-year mobility structure and 2027 first-period deadline of 31 January. UniTrento lists itself as an entry and exit point for this track.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-28DIGITAL-HCIDXR-2027","university_id":"trento","title":"Human-Computer Interaction and Design with Extended Reality (HCID/XR)","url":"https://masterschool.28digital.eu/human-computer-interaction-and-design-with-extended-reality","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the double-degree master’s, relevant bachelor fields and experience, and the 2027 first-period deadline of 31 January. UniTrento lists itself as an exit point for this track.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-28DIGITAL-CLOUD-2027","university_id":"trento","title":"Cloud and Networking Infrastructure and HPC (CNIHPC)","url":"https://masterschool.28digital.eu/cloud-and-networking-infrastructure-and-hpc","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the two-year double-degree master’s, relevant bachelor preparation and the 2027 first-period deadline of 31 January. UniTrento lists itself as an entry and exit point for this track.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-28DIGITAL-ICS-2027","university_id":"trento","title":"Intelligent Chips and Systems (ICS) – 28DIGITAL Master School","url":"https://masterschool.28digital.eu/intelligent-chips-and-systems","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the two-year master's, relevant bachelor fields, minimum 40 ECTS in ICT and 20 ECTS in mathematics, and the 2027 first-period deadline of 31 January. UniTrento lists itself as an exit point for this track.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-28DIGITAL-AIAC-2027","university_id":"trento","title":"Artificial Intelligence with Affective Computing (AIAC)","url":"https://masterschool.28digital.eu/artificial-intelligence-with-affective-computing","source_type":"Official joint-master program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes the two-year double-degree master's, relevant bachelor fields and expected background in programming, algorithms, mathematics and statistics, and the 2027 first-period deadline of 31 January. UniTrento lists itself as an entry and exit point for this track.","supports":["program.name","program.level","program.availability","program.requirements","program.application_deadline","program.duration"]},
    {"id":"SRC-CA-FOSCARI-2027","university_id":"ca-foscari","title":"Preliminary evaluation of international qualifications","url":"https://www.unive.it/pag/12520","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States that applications for international qualifications seeking 2027/28 bachelor’s or master’s admission start in December 2026; exact calls and dates are to be published later.","supports":["university.application_opening","university.non_eu_process"]},
    {"id":"SRC-CA-FOSCARI-BUDDHISM-2027","university_id":"ca-foscari","title":"Buddhism and Asian Religions – programme and 2027/28 admission","url":"https://www.unive.it/web/en/21007/home","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States that the MSc activates in 2027/28; level MSc, LM-64, Venice, English, two years/120 credits and open admission. The admission page says detailed 2027/28 procedures and deadlines will be updated in March 2027; the enrolment page requires B2 English and adequate preparation.","supports":["program.availability","program.name","program.level","program.language","program.duration","program.access_type","program.requirements","program.deadline_status"]},
    {"id":"SRC-CA-FOSCARI-SCHOLARSHIPS-2027","university_id":"ca-foscari","title":"Financial aid for high-achieving international students","url":"https://www.unive.it/pag/19545","source_type":"Official scholarship page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For 2027/28 lists 8 bachelor scholarships of €10,000/year for three years and 20 master’s scholarships of €10,000/year for two years. Ranking factors include CGPA at least 85%, motivational video, reference letters and language evidence; the complete call with exact deadlines is expected in late fall.","supports":["university.scholarships","university.scholarship_eligibility","university.scholarship_deadline_status"]},
    {"id":"SRC-TORVERGATA-MECH-2027","university_id":"tor-vergata","title":"Admission A.Y. 2027-28 – Mechatronics Engineering","url":"https://mechatronics.uniroma2.it/how-to-apply-for-mechatronics/admission-a-y-2027-28/","source_type":"Official program admission page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"MSc Mechatronics Engineering, two years/120 credits, taught in English; lists non-EU visa applicant windows 9–27 Nov 2026, 11–25 Jan 2027, 8–22 Feb 2027 and resident window 5 Jul–6 Sep 2027; €30 application fee, 60 non-EU-abroad seats plus 4 Marco Polo places, B2 English, curricular requirements and document list.","supports":["program.availability","program.name","program.level","program.language","program.duration","program.deadlines","program.application_fee","program.seats","program.requirements"]},
    {"id":"SRC-TORVERGATA-MECH-LANGUAGE","university_id":"tor-vergata","title":"Aims and scopes – Mechatronics Engineering","url":"https://mechatronics.uniroma2.it/about-us/aims-and-scopes/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States the program is taught entirely in English; the current cycle-specific admission page separately confirms 2027/28 availability.","supports":["program.language"]},
    {"id":"SRC-UNIFI-SST-2027","university_id":"firenze","title":"Enrollment (a.y. 2027/28) – Software: Science and Technology","url":"https://www.sst.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=168","source_type":"Official program admission page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Program page specifies open admission for the 2027/28 MSc, bachelor’s qualification, country-specific grade threshold, 24 ECTS in CS/Computer Engineering and 24 ECTS in Mathematics/Physics/Statistics, B2 English evidence and possible interview.","supports":["program.availability","program.name","program.level","program.access_type","program.requirements","program.english_requirement"]},
    {"id":"SRC-UNIFI-SST-LANGUAGE","university_id":"firenze","title":"Course presentation – Software: Science and Technology","url":"https://www.sst.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=167","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States the MSc is entirely delivered in English and has two-year duration/120 CFU.","supports":["program.language","program.duration"]},
    {"id":"SRC-UNINA-CHE-2027","university_id":"napoli-federico-ii","title":"Notice for International Students – AY 2027/2028, MSc Chemical Engineering","url":"https://www.dicmapi.unina.it/ingegneria-chimica/notice-for-international-students-academic-year-2027-2028-msc-chemical-engineering/","source_type":"Official program admission notice","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States international pre-evaluation opens 10 January 2027; Universitaly opens from February/March 2027; exact dates and deadlines to follow.","supports":["program.availability","program.deadline","program.application_opening"]},
    {"id":"SRC-UNINA-CHE-PROGRAM","university_id":"napoli-federico-ii","title":"Master’s Degree in Chemical Engineering","url":"https://www.dicmapi.unina.it/mag_ingchim/masters-degree-in-chemical-engineering/?lang=en","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Identifies the MSc in Chemical Engineering (LM-22), Napoli campus, and Italian/English language; English curricula include Product Engineering and Sustainable Engineering.","supports":["program.name","program.level","program.language","program.location"]},
    {"id":"SRC-BOLOGNA-CLE-2027","university_id":"bologna","title":"Application – Erasmus Mundus CLE","url":"https://cle.unibo.it/pages/23/presentazione-della-domanda/lang/en","source_type":"Official joint-master program admission page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Publishes AY 2027/28 application intakes from November 2026 to February 2027 and March to April 2027, with results in March and May. Exact day-level deadlines are not supplied on the reviewed page.","supports":["program.availability","program.application_windows"]},
    {"id":"SRC-UNIBO-CSE-2027","university_id":"bologna","title":"Computer Science and Engineering – admissions and requirements","url":"https://corsi.unibo.it/2cycle/ComputerScienceEngineering/how-to-enrol","source_type":"Official degree-program admission page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Identifies the MSc and its Intelligent Embedded Systems curriculum as English-taught, with a Bologna-managed local track (15 places) and a 28Digital track (10 places) managed by 28Digital. The shared curricular entry requirements include a relevant first-cycle degree or specified 42 ECTS including at least 18 ECTS in computer science/engineering; B2 English is required for Intelligent Embedded Systems. The 28Digital track is open for 2027/28.","supports":["program.name","program.level","program.language","program.requirements","program.seats","program.availability"]},
    {"id":"SRC-UNIBO-28DIGITAL-2027","university_id":"bologna","title":"Intelligent Embedded Systems – 28Digital track","url":"https://corsi.unibo.it/magistrale/IngegneriaScienzeInformatiche/curriculum-intelligent-embedded-systems-28digital-track","source_type":"Official degree-program admission page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For a.y. 2027/28, the English Intelligent Embedded Systems 28Digital track has three application sessions: 30 Oct 2026–31 Jan 2027 for EU/EEA/CH and non-EU applicants; 1 Feb–18 Apr 2027 primarily for EU/EEA/CH and applicants not requiring a residence permit; and 19 Apr–31 May 2027 only for EU/EEA/CH and non-EU applicants not requiring a study visa. Admissions are managed directly by 28Digital. The 28Digital track combines a first-year entry university and a different-country second-year exit university, and grants a double degree plus a 28Digital certificate.","supports":["program.availability","program.language","program.application_windows","program.admissions_route","program.degree_structure"]},
    {"id":"SRC-SIENA-2027","university_id":"siena","title":"International Students Admissions – Information Portal","url":"https://admission.unisi.it/","source_type":"Official admissions portal","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"States the next 2027/28 international admissions intake opens in November 2026; detailed deadlines are not yet published on the reviewed page.","supports":["university.application_opening","university.deadline_status"]},
    {"id":"SRC-PARMA-2027","university_id":"parma","title":"Admissions for a.y. 2027-2028 – Let’s keep in touch!","url":"https://www.unipr.it/en/node/106538","source_type":"Official international admissions update","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Asks international applicants interested in AY 2027/28 to register interest and states that admissions procedures will be communicated once available.","supports":["university.deadline_status","university.admissions_status"]},
    {"id":"SRC-PALERMO-2027","university_id":"palermo","title":"Before Applying – FAQ International Students","url":"https://www.unipa.it/mobilita/en/useful-information/faq-international-students/faq-international-students-p2/before-applying/index.html","source_type":"Official international admissions FAQ","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Explicitly says exact 2027/28 admission dates have not yet been published; explains that requirements and selection procedures vary by program.","supports":["university.deadline_status","university.program_requirements"]},
    {"id":"SRC-POLIBA-2027","university_id":"politecnico-bari","title":"Admissions to first-level degree courses","url":"https://www.poliba.it/en/ammissioni-corsi-di-laurea-di-1deg-livello","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"The official page says 2027/28 admission call instructions for first-level degrees will be published in February 2027.","supports":["university.bachelor_deadline_status"]},
    {"id":"SRC-POLITO-2027","university_id":"politecnico-torino","title":"Calls for application, regulations and ranking lists – Bachelor's","url":"https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/bachelor-s-degree-programmes/calls-for-application-regulations-and-ranking-lists","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official page says 2027/28 bachelor calls are being finalized and will be published soon; the call page says Polito joins CISIA for 2027/28.","supports":["university.bachelor_deadline_status","university.admission_test"]},
    {"id":"SRC-POLITO-BSC-TEST-2027","university_id":"politecnico-torino","title":"Admission test – Bachelor's programmes, 2027/28","url":"https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/bachelor-s-degree-programmes/admission-test","source_type":"Official admissions test page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For 2027/28, confirms Polito will use CISIA-administered tests and accept only in-person TOLC@UNI and CEnT@UNI tests at Polito or another participating university; remote TOLC@CASA and CEnT@CASA tests are not accepted. The official selection call is still forthcoming.","supports":["university.admission_test","university.bachelor_call"]},
    {"id":"SRC-BICOCCA-2027","university_id":"milano-bicocca","title":"Access for students with an international qualification","url":"https://en.unimib.it/study/information-international-students/access-students-international-qualification","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Notes 2027/28-specific country-dependent entry requirements; program calls and dates require individual review.","supports":["university.international_qualification"]},
    {"id":"SRC-UNIPG-INTL","university_id":"perugia","title":"Becoming a UniPG student","url":"https://www.unipg.it/en/international-students/becoming-a-unipg-student","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The reviewed page still describes 2026 visa-applicant pre-evaluation windows; it does not establish 2027/28 deadlines.","supports":["university.previous_cycle_process"]},
    {"id":"SRC-CAMERINO-FAQ","university_id":"camerino","title":"Admissions FAQ","url":"https://international.unicam.it/admissions/faq","source_type":"Official international admissions FAQ","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"General FAQ and prior-cycle information were available; a 2027/28 program-level call was not confirmed in the material reviewed.","supports":["university.general_admissions"]},
    {"id":"SRC-TRIESTE-APPLY","university_id":"trieste","title":"Application","url":"https://portale.units.it/en/study/application","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"General international application instructions; no program-specific 2027/28 deadline was confirmed in the material reviewed.","supports":["university.general_admissions"]},
    {"id":"SRC-LAQUILA-INTL","university_id":"laquila","title":"International students","url":"https://www.univaq.it/en/section.php?id=2065&lang_s=en","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"Official general international admissions guidance; detailed 2027/28 program-specific calls remain to be reviewed.","supports":["university.general_admissions"]},
    {"id":"SRC-SALERNO-INTL","university_id":"salerno","title":"Enrolment – Non-EU citizens abroad","url":"https://web.unisa.it/en/teaching/enrollment/non-eu-citizens-abroad","source_type":"Official non-EU admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"Official non-EU application guidance; the page reviewed does not establish a complete 2027/28 degree-program schedule.","supports":["university.non_eu_process"]},
    {"id":"SRC-SAPIENZA-INTL","university_id":"sapienza","title":"International Students Office","url":"https://www.uniroma1.it/it/pagina/segreteria-studenti-internazionali","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The cycle-specific information reviewed is for 2026/27; the 2027/28 program calls remain outstanding.","supports":["university.previous_cycle_process"]},
    {"id":"SRC-CATANIA-INTL","university_id":"catania","title":"International Students","url":"https://www.unict.it/en/node/5251","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"University page directs international students to degree-specific procedures and notes that rules and deadlines vary by program; no 2027/28 program facts are confirmed here.","supports":["university.general_admissions"]},
    {"id":"SRC-MILANO-ENROL","university_id":"milano-statale","title":"Enrolment","url":"https://www.unimi.it/en/study/enrolment","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The reviewed page describes 2026/27 admissions and explains that annual calls set requirements, tests, places, rankings and enrollment procedures.","supports":["university.previous_cycle_process","university.admission_structure"]},
    {"id":"SRC-UNITO-INTL","university_id":"torino","title":"Application for international students","url":"https://www.en.unito.it/studying-unito/international-degree-seeking-students/application-international-students","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"The reviewed page lists 2026/27 application rounds and a €60 fee; values are retained only as prior-cycle context and are not copied into the active dataset.","supports":["university.previous_cycle_process"]},
    {"id":"SRC-UNITN-INTL","university_id":"trento","title":"Admission: how it works","url":"https://www.unitn.it/en/international/coming-unitrento/admission-how-it-works","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"General guidance says visa-applicant calls are program-specific and typically run December–March; it describes ranked selection, merit-based fee brackets and scholarship/accommodation procedures, but does not confirm individual 2027/28 programs.","supports":["university.non_eu_process","university.scholarships_general","university.fees_general"]},
    {"id":"SRC-UNIFI-INTL","university_id":"firenze","title":"Pre-enrolment and study-visa application","url":"https://www.unifi.it/en/study-us/your-learning-path/start-your-enrolment/international-students/pre-enrolment-and-study","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"Explains visa applicants’ general procedure; not a full 2027/28 program deadline source.","supports":["university.non_eu_process"]},
    {"id":"SRC-UNIPI-ENGLISH","university_id":"pisa","title":"Degrees offered in English","url":"https://didattica.di.unipi.it/en/internazionale/degrees-offered-in-english/","source_type":"Official program catalogue page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Department’s English-program directory; the 2027/28 call is the source of cycle-specific availability and dates.","supports":["university.english_programs"]},
    {"id":"SRC-ROMATRE-INTL","university_id":"roma-tre","title":"International Students Admission","url":"https://orientamento.uniroma3.it/en/about-roma-tre/international-students-admissions/","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"Describes international admission steps for first- and second-cycle courses; a reviewed guide is for 2026/27, so no 2027/28 dates are inferred.","supports":["university.general_admissions","university.non_eu_process"]},
    {"id":"SRC-UNIVPM-INTL","university_id":"marche","title":"Non-EU students applying for a visa","url":"https://www.international.univpm.it/become-a-student/enrolment/non-eu-students-applying-for-a-visa/","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"Official international site describes visa-applicant steps and refers to program-specific procedures; reviewed pages focus on 2026/27.","supports":["university.general_admissions","university.non_eu_process"]},
    {"id":"SRC-INSUBRIA-INTL","university_id":"insubria","title":"Enrolment of non-EU students residing abroad","url":"https://www.uninsubria.it/servizi/vivere-insubria/immatricolarsi-e-iscriversi/immatricolazioni/studenti-non-ue-residenti","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"Page gives 2026/27 application and document deadlines and does not establish 2027/28 program-level dates.","supports":["university.previous_cycle_process","university.non_eu_process"]},
    {"id":"SRC-FERRARA-INTL","university_id":"ferrara","title":"Enrol in a post-graduate course","url":"https://www.unife.it/en/come-to-study/enroll/how-to-enroll/arrival-enrolment/enrol-in-a-post-graduate-course","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"General guidance for international applicants to postgraduate courses; no 2027/28 catalog or cycle-specific deadline is stated on this page.","supports":["university.general_admissions","university.non_eu_process"]},
    {"id":"SRC-UNIMORE-INTL","university_id":"modena-reggio","title":"Foreign study qualification","url":"https://www.unimore.it/en/internationalisation/foreign-qualification","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"Explains foreign-qualification procedures and directs candidates to degree-specific calls; no 2027/28 catalog or deadline is established here.","supports":["university.general_admissions","university.non_eu_process"]},
    {"id":"SRC-PAVIA-ENG-INTL","university_id":"pavia","title":"International Applications – Faculty of Engineering","url":"https://webing.unipv.eu/home/international/international-applications/","source_type":"Official faculty admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"Describes evaluation of foreign applications to English-taught engineering master's programs; faculty-specific, not the full 2027/28 university catalog.","supports":["university.general_admissions","university.master_entry"]},
    {"id":"SRC-UDINE-APPLY","university_id":"udine","title":"How to apply","url":"https://www.uniud.it/en/education/info-for/how-to-apply/how-to-apply?set_language=en","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":"general","evidence":"States that annual rules, deadlines and tests are listed in the prospectus published each June; non-EU applicants follow pre-enrolment and course-level reserved-place procedures.","supports":["university.admission_structure","university.non_eu_process"]},
    {"id":"SRC-VERONA-INTL","university_id":"verona","title":"International degree-seeking students","url":"https://www.univr.it/en/our-services/international-degree-seeking-students","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":"2026-2027","evidence":"Reviewed page states 2026/27 international master's call status; it does not confirm 2027/28 program availability or deadlines.","supports":["university.previous_cycle_process","university.non_eu_process"]},
]

SOURCE_BY_ID = {s["id"]: s for s in SOURCES}
UNI_BY_ID = {u[0]: u for u in UNIVERSITIES}


def fact(value, status, sources=(), note=None):
    return {"value": value, "status": status, "source_ids": list(sources), "notes": note}


def make_program(pid, uid, name, level, language, field, status, evidence_sources, *, city=None, facts=None, discovery="previous_tracker"):
    row = UNI_BY_ID[uid]
    return {
        "id": pid,
        "university_id": uid,
        "university": row[1],
        "city": city or row[2],
        "program": name,
        "level": fact(level, "CONFIRMED" if status == "CONFIRMED" else "REQUIRES_VERIFICATION", evidence_sources),
        "language": fact(language, "CONFIRMED" if status == "CONFIRMED" else "REQUIRES_VERIFICATION", evidence_sources),
        "field": fact(field, "CONFIRMED" if status == "CONFIRMED" else "REQUIRES_VERIFICATION", evidence_sources),
        "availability_2027_2028": fact(True if status == "CONFIRMED" else None, status, evidence_sources,
                                       None if status == "CONFIRMED" else "This program appears in the prior tracker or a discovery source, but its full 2027/28 offer has not been confirmed."),
        "overall_status": status,
        "discovery_source": discovery,
        "facts": facts or {},
        "source_ids": list(evidence_sources),
        "previous_tracker_tags": None,
        "previous_cycle_tags": None,
        "last_checked": AS_OF,
    }


def build():
    RESEARCH.mkdir(exist_ok=True)
    (RESEARCH / "archive").mkdir(exist_ok=True)
    old = json.loads((RESEARCH / "archive" / "legacy-programs.json").read_text(encoding="utf-8-sig"))
    uni_rows = []
    for uid, name, city, region, homepage, admissions, cycle_status, note in UNIVERSITIES:
        src = next((s for s in SOURCES if s.get("university_id") == uid), None)
        coverage = {
            "official_website_visited": "complete",
            "international_admissions_page_examined": "partial" if src else "not_started",
            "bachelors_admissions_examined": "partial" if uid in {"padova", "politecnico-milano", "politecnico-bari", "politecnico-torino", "firenze", "tor-vergata", "messina", "catania"} else "not_started",
            "masters_admissions_examined": "partial" if uid in {"padova", "politecnico-milano", "pisa", "firenze", "napoli-federico-ii", "tor-vergata", "messina", "genova", "catania"} else "not_started",
            "english_programs_examined": "partial" if uid in {"padova", "politecnico-milano", "pisa", "firenze", "tor-vergata", "bologna", "genova", "trento", "messina", "catania"} else "not_started",
            "fees_examined": "partial" if uid in {"politecnico-milano", "pisa", "tor-vergata", "messina", "genova", "trento", "catania"} else "not_started",
            "scholarships_examined": "partial" if uid in {"pisa", "messina", "trento", "bologna", "politecnico-milano", "catania"} else "not_started",
            "non_eu_requirements_examined": "partial" if src else "not_started",
            "application_deadlines_examined": "partial" if cycle_status in {"CONFIRMED", "NOT_YET_PUBLISHED"} or uid in {"genova", "politecnico-torino", "politecnico-bari", "catania"} else "not_started",
            "program_level_review": "partial" if uid in {"padova", "pisa", "firenze", "napoli-federico-ii", "tor-vergata", "bologna", "messina", "catania"} else "not_started",
        }
        relevant_sources = [s["id"] for s in SOURCES if s.get("university_id") == uid]
        if not relevant_sources:
            relevant_sources = []
        uni_rows.append({
            "id": uid, "name": name, "aliases": [alias for alias, alias_uid in ALIASES.items() if alias_uid == uid],
            "city": city, "region": region, "country": "Italy", "official_website": homepage,
            "international_admissions_url": admissions, "application_portal_url": None,
            "contact_email": None, "contact_url": "https://www.polimi.it/en/prospective-students/contacts/contacts-for-international-prospective-students" if uid == "politecnico-milano" else admissions,
            "cycle_status": cycle_status, "research_stage": "PARTIALLY_RESEARCHED",
            "research_summary": note, "coverage": coverage, "source_ids": relevant_sources,
            "last_checked": AS_OF,
        })

    # Source-linked, cycle-specific university facts, kept separate from program facts.
    uni_facts = {
        "padova": {"application_windows": fact([
            {"label":"Call 1","start":"2026-09-15","end":"2026-11-15","eligible_group":"Most degree programs; check individual course call"},
            {"label":"Call 2","start":"2026-12-01","end":"2027-03-01","eligible_group":"Most degree programs; check individual course call"},
            {"label":"Call 3","start":"2027-04-01","end":"2027-06-01","eligible_group":"EU and non-EU applicants residing in Italy only"}], "CONFIRMED", ["SRC-PADUA-INTL-2027"], "The general page says the first call applies to most degree programs; individual programs may differ.")},
        "politecnico-milano": {"application_windows": fact([
            {"label":"Early bird","start":"2026-10-01","end":"2026-12-01","eligible_group":"September 2027 MSc applicants; study-area rules apply"},
            {"label":"General period 2","start":"2027-01-12","end":"2027-01-28","eligible_group":"General cross-area schedule; verify the chosen study area's call"},
            {"label":"Additional","start":"2027-03-01","end":"2027-03-18","eligible_group":"EEA and non-EEA residents in Italy with one of the listed permit types"}], "CONFIRMED", ["SRC-POLIMI-DEADLINES-2027"], "The official page also has separate Architecture/Design and Engineering tables; the Engineering subsection is labelled 2026/27 while describing the September 2027 intake and gives a different second-call end date. See engineering_application_windows below."), "application_fee":fact({"early_bird_eur":50,"standard_eur":150,"maximum_programmes":2},"CONFIRMED",["SRC-POLIMI-DEADLINES-2027"],"The standard fee applies from 2 December; eligibility and study-area windows vary."),
            "architecture_design_application_windows":fact([
                {"label":"General call","start":"2026-10-01","end":"2027-01-28","eligible_group":"September 2027 Architecture and Design MSc applicants"},
                {"label":"Additional call","start":"2027-03-01","end":"2027-03-18","eligible_group":"EEA and non-EEA residents in Italy with a listed permit type"}],"CONFIRMED",["SRC-POLIMI-DEADLINES-2027"],"Early-bird fee deadline is 1 December 2026."),
            "engineering_application_windows":fact({
                "general_2027_2028_section":[
                    {"label":"Early bird","start":"2026-10-01","end":"2026-12-01"},
                    {"label":"Period 2","start":"2027-01-12","end":"2027-01-28"}],
                "engineering_subsection_labeled_2026_2027_for_september_2027_intake":[
                    {"label":"Call 1","start":"2026-10-01","end":"2026-12-01"},
                    {"label":"Call 2","start":"2027-01-12","end":"2027-02-25"}],
                "additional_call":[{"start":"2027-03-01","end":"2027-03-18","eligible_group":"EEA and non-EEA residents in Italy with a listed permit type"}]},"CONFLICTING_SOURCES",["SRC-POLIMI-DEADLINES-2027"],"A single official page has a 2027/28 general table ending 28 January, and an Engineering subsection labelled 2026/27 that nonetheless describes the September 2027 intake and ends the Engineering second call on 25 February. The applicable Engineering deadline needs confirmation from the program-specific call or admissions portal."),
            "bachelor_call":fact(None,"NOT_YET_PUBLISHED",["SRC-POLIMI-ENGINEERING-CALL-2027"],"The official Engineering admissions page says the 2027/28 call will be published shortly; the full call and places were not yet available on the reviewed page."),
            "bachelor_enrolment_schedule":fact([
                {"label":"Phase 1 (restricted eligibility; excludes English-taught programmes)","start":"2027-05-03","end":"2027-06-10"},
                {"label":"Phase 2 preference deadline","end":"2027-06-17"},
                {"label":"Phase 3 preference deadline","end":"2027-07-22"},
                {"label":"Phase 4 preference deadline","end":"2027-08-26"}],"CONFIRMED",["SRC-POLIMI-BSC-2027"],"The page also lists ranking and enrolment deadlines after each preference phase; this is not a single university-wide BSc application deadline."),
            "engineering_bachelor_tests":fact({"tests":["TOL","TOLC-I","CEnT-S","SAT"],"CEnT-S":{"language":"English","questions_total":55,"minutes_total":110,"questions_used_by_Polimi":35,"minutes_used_by_Polimi":70,"sections_used":["Mathematics","Reasoning on texts and data","Physics"]},"CEnT-S_score_record_deadline":"2027-06-03 11:59 a.m. for final-year 2026/27 or already-graduated test-takers taking a test from 2026-09-01 through 2027-06-03"},"CONFIRMED",["SRC-POLIMI-ENGINEERING-CALL-2027","SRC-POLIMI-CENTS-2027"],"CEnT-S recording deadlines differ by cohort; check the source for the separate prior-year penultimate-student rule."),
            "tuition_2027_2028":fact(None,"UNAVAILABLE",["SRC-POLIMI-TUITION-2027"],"The reviewed official fee page displays the 2026/27 schedule only. Do not carry those amounts forward as 2027/28 tuition."),
            "international_merit_scholarships":fact({"platinum":{"awards":10,"gross_eur":10000,"campus":"Milan"},"gold":{"awards":18,"gross_eur":8000,"campus":"Milan"},"gold_piacenza":{"awards":16,"gross_eur":5000,"campus":"Piacenza","eligible_programs":["Sustainable Architecture and Landscape Design","Landscape Architecture – Land Landscape Heritage","Energy Engineering – Renewables and Environmental Sustainability"]},"bronze_piacenza":{"awards":10,"gross_eur":2500,"campus":"Piacenza","eligible_program":"Mechanical Engineering – Mechatronics for Manufacturing"},"silver":{"awards":10,"campuses":["Cremona","Lecco","Mantova","Piacenza"],"benefit":"full tuition waiver"},"tuition_waiver":"All awards include a tuition waiver for the 2027/28 award year","eligible_group":"International applicants to first-year MSc programs taught in English; scholarship tier has campus/program restrictions","admission_application_fee_paid_between":["2026-10-01","2026-12-01"],"scholarship_application_period":{"start":"2026-10-01","end":"2026-12-15","deadline_time":"12:00 Italian time"},"award_conditions":"Competitive; applicants must be admitted and accept the admission outcome; award rules and renewal conditions apply"},"CONFIRMED",["SRC-POLIMI-SCHOLARSHIPS-2027"],"Gross award amounts are not net payments; campus, program, admission and renewal conditions apply."),
            "masters_english_certificates":fact({"TOEFL_iBT":"at least 78 for tests taken through 2026-01-20; at least 4.5 from 2026-01-21","TOEIC":"at least 785 Listening/Reading and 310 Speaking/Writing","IELTS":"at least 6","Cambridge":"First grade B; Advanced or Proficiency grade C","Trinity":"at least ISE II","Pearson_PTE":"at least 59","Pearson_PEIC":"at least 59","LanguageCert":"at least B2 Communicator (4 skills)","English_medium_exemption":"Bachelor's taught in English for at least 3 years with university certification that at least 75% of courses were in English"},"CONFIRMED",["SRC-POLIMI-ENGLISH-2027"])},
        "pisa": {"application_windows": fact([{"label":"Non-EU abroad department call","start":None,"end":"2027-02-01","eligible_group":"Non-EU applicants residing abroad to the three named English MSc programs","timezone":"Anywhere on Earth"}], "CONFIRMED", ["SRC-PISA-CALL-2027"], "Call result date is 2027-03-01. This is a department call, not the entire university offer."), "application_fee":fact({"amount_eur":30,"per":"application","maximum_applications":2},"CONFIRMED",["SRC-PISA-CALL-2027"]), "tuition_2027_2028":fact(None,"NOT_YET_PUBLISHED",["SRC-PISA-CALL-2027"],"The call says annual fees are usually published in June; the listed 2026/27 range is not carried forward.")},
        "catania": {
            "application_windows": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-MASTER-CALLS-INDEX", "SRC-UNICT-DS-CALL-2026"], "The latest official Master's call located is for 2026/27, whose non-EU English-MSc window was 10 February–17 March 2026 with a €10 fee per course. No 2027/28 call or dates were listed in the official archive checked on 9 November 2026; the archive does not explicitly say a new call will not be published, so the 2027/28 status remains unverified."),
            "tuition_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-FEES-2026"], "The latest fee rules located are for 2026/27 (up to €2,150 for regular students meeting credit conditions and €2,350 for irregular students). No 2027/28 fee schedule was identified, and prior-year amounts are not carried forward."),
            "international_scholarships_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-SCHOLARSHIPS-2026"], "The official 2026/27 call offered five two-year €2,000-per-year awards for each of ten English-taught Master's degrees, including Data Science, for non-EU applicants abroad. No 2027/28 call was identified; recurrence is not assumed."),
            "non_eu_requirements_2027_2028": fact(None, "REQUIRES_VERIFICATION", ["SRC-CATANIA-INTL", "SRC-UNICT-BACHELORS-INTERNATIONAL-2026", "SRC-UNICT-DS-CALL-2026"], "Official guidance routes international students to degree-specific procedures. The reviewed Bachelor's and English-MSc requirements are for 2026/27 and do not establish 2027/28 rules."),
        },
        "messina": {"application_windows": fact([
            {"label":"Early Bird visa applicants","start":"2026-12-01","end":"2026-12-20","eligible_group":"Non-EU study-visa applicants with final documents"},
            {"label":"Second call","start":"2027-02-02","end":"2027-03-19","eligible_group":"Visa applicants"},
            {"label":"Third call","start":"2027-04-08","end":"2027-05-08","eligible_group":"Visa applicants"},
            {"label":"Semestre Aperto","start":"2027-05-18","end":"2027-06-15","eligible_group":"Selected single-cycle degree programs"},
            {"label":"Medicine and Surgery (IMAT)","start":"2027-07-01","end":"2027-07-22","eligible_group":"English Medicine applicants"},
            {"label":"Non-visa applicants","start":"2027-07-06","end":"2027-11-13","eligible_group":"Applicants who do not need a study visa"}], "CONFIRMED", ["SRC-UNIME-2027"], "Program and applicant-category rules differ; use the live official call before applying."), "application_fee":fact({"amount_eur":40,"maximum_applications":2,"refundable":False},"CONFIRMED",["SRC-UNIME-2027"])},
        "genova": {"application_windows":fact([{"label":"Visa preselection (expected)","start":"2026-12-15","end":"2027-03-31","eligible_group":"Non-EU visa applicants","exact_dates":False}],"REQUIRES_VERIFICATION",["SRC-UNIGE-2027"],"The page labels these dates expected; exact opening and closing dates were not yet published."),"application_fee":fact({"amount_eur":30,"maximum_assessment_applications":2},"CONFIRMED",["SRC-UNIGE-2027"])},
        "trento": {"28digital_application_windows":fact({
            "unitrento_department_page":[
                {"label":"Period 1","start":"2026-10-31","end":"2027-02-11","eligible_group":"EU/EEA/CH and non-EU citizens"},
                {"label":"Period 2","start":"2027-02-11","end":"2027-04-15","eligible_group":"EU/EEA/CH and non-EU applicants residing in Italy; not recommended for study-visa applicants; some trajectories may be unavailable"},
                {"label":"Period 3","start":"2027-04-15","end":"2027-06-01","eligible_group":"EU/EEA/CH and non-EU applicants residing in Italy"}],
            "central_28digital_admissions_page":[
                {"label":"Period 1","start":"2026-10-30","end":"2027-01-31","eligible_group":"EU/EEA/CH and non-EU applicants; primarily aimed at study-visa applicants"},
                {"label":"Period 2","start":"2027-02-01","end":"2027-04-18","eligible_group":"Primarily EU and applicants who do not need a study permit; non-EU applicants may face visa timing constraints"},
                {"label":"Period 3","start":"2027-04-19","end":"2027-05-31","eligible_group":"EU and applicants who do not need a study permit"}]},"CONFLICTING_SOURCES",["SRC-UNITRENTO-28DIGITAL-2027","SRC-28DIGITAL-ADMISSIONS-2027"],"The University's department page and central 28DIGITAL admissions page publish different round boundaries for the same 2027/28 intake. Individual 28DIGITAL track pages confirm the period-one deadline of 31 January 2027. Check the central application portal for the specific track and entry/exit university before applying."),
            "28digital_scholarships":fact({"consortium_awards":"full or half tuition waivers; some selected programmes offer full waiver plus living allowance for eligible EU/EEA/associated-country citizens","unitrento_mobility_scholarships_eur_range":[2500,4500],"unitrento_awards":"for UniTrento entry students in the second year abroad; eligibility and combination rules apply","next_call":"eligible applicants contacted around August"},"CONFIRMED",["SRC-28DIGITAL-FEES-2027"],"Awards are conditional and not guaranteed; check the specific partner, programme and call conditions."),
            "28digital_admissions_contact":fact("eitmaster@unitn.it","CONFIRMED",["SRC-UNITRENTO-28DIGITAL-2027"],"This is the 28DIGITAL program contact, not the university-wide admissions office.")},
        "ca-foscari": {"application_opening":fact("2026-12","CONFIRMED",["SRC-CA-FOSCARI-2027"],"Exact 2027/28 application periods were not yet listed."),"application_deadlines":fact(None,"NOT_YET_PUBLISHED",["SRC-CA-FOSCARI-2027"]),"honours_scholarships":fact({"bachelor_awards":8,"bachelor_eur_per_year":10000,"bachelor_years":3,"master_awards":20,"master_eur_per_year":10000,"master_years":2,"minimum_cgpa_percent":85,"ranking_factors":["CGPA","motivational video","reference letter(s)","language certification"]},"CONFIRMED",["SRC-CA-FOSCARI-SCHOLARSHIPS-2027"],"The complete 2027/28 call, including deadlines and detailed conditions, was expected in late fall 2026.")},
        "siena": {"application_opening":fact("2026-11","CONFIRMED",["SRC-SIENA-2027"],"The portal announces a November 2026 opening; precise dates are not yet listed."),"application_deadlines":fact(None,"NOT_YET_PUBLISHED",["SRC-SIENA-2027"])},
        "parma": {"application_procedure":fact(None,"NOT_YET_PUBLISHED",["SRC-PARMA-2027"],"The official page says application procedures will be communicated when available.")},
        "palermo": {"application_deadlines":fact(None,"NOT_YET_PUBLISHED",["SRC-PALERMO-2027"],"The official FAQ explicitly says exact 2027/28 dates have not yet been published.")},
        "politecnico-bari": {"bachelor_call":fact(None,"NOT_YET_PUBLISHED",["SRC-POLIBA-2027"],"Official page says instructions for 2027/28 first-level calls will be published in February 2027.")},
        "politecnico-torino": {"bachelor_call":fact(None,"NOT_YET_PUBLISHED",["SRC-POLITO-2027","SRC-POLITO-BSC-TEST-2027"],"Official page says 2027/28 calls are being finalized and will be published soon; detailed dates and selection rules are not yet published."),"bachelor_admission_test":fact({"accepted_tests":["TOLC@UNI","CEnT@UNI"],"delivery":"in person only","not_accepted":["TOLC@CASA","CEnT@CASA"]},"CONFIRMED",["SRC-POLITO-BSC-TEST-2027"],"Applies to Bachelor's admission from 2027/28. The detailed call remains pending.")},
    }
    for u in uni_rows:
        u["cycle_facts"] = uni_facts.get(u["id"], {})
        if u["id"] == "politecnico-milano":
            u["source_ids"] = [s["id"] for s in SOURCES if s.get("university_id") == u["id"]]

    programs = []
    for index, row in enumerate(old, 1):
        uid = ALIASES.get(row["university"])
        if not uid:
            raise ValueError(f"No university mapping for {row['university']!r}")
        pid = f"legacy-{index:03d}"
        programs.append(make_program(pid, uid, row["program"], row["level"], row["language"], row["field"], "REQUIRES_VERIFICATION", [], city=row.get("city"), discovery="previous_tracker"))
        programs[-1]["previous_tracker_tags"] = {"level":row["level"],"language":row["language"],"field":row["field"],"label":"Previous tracker classification — not reverified for 2027/28"}

    # The historical Catania programme was explicitly replaced by Data Science
    # from AY 2022/23. Keep the archived candidate visible as discontinued and
    # create a separate successor record based on 2026/27 evidence only.
    catania_legacy = next(p for p in programs if p["id"] == "legacy-077")
    catania_legacy["availability_2027_2028"] = fact(False, "CONFIRMED", ["SRC-UNICT-DSM-LEGACY", "SRC-UNICT-DS-PROGRAM-2026"], "The official course page says Data Science for Management was replaced by the new Data Science course starting in AY 2022/23, with new enrollment only in the replacement course. It is therefore not an active 2027/28 intake; the successor is tracked separately.")
    catania_legacy["overall_status"] = "NOT_APPLICABLE"
    catania_legacy["source_ids"] = ["SRC-UNICT-DSM-LEGACY", "SRC-UNICT-DS-PROGRAM-2026"]
    catania_legacy["facts"] = {"course_replacement": fact("Replaced by Data Science from AY 2022/23", "CONFIRMED", ["SRC-UNICT-DSM-LEGACY"], "The current official Data Science listing is tracked in a separate candidate record; its 2027/28 intake is not yet verified.")}

    def promote(uid, name, level, language, field, srcs, facts=None, *, discovery="previous_tracker", city=None):
        norm = lambda x: re.sub(r"[^a-z0-9]+", "", x.lower())
        found = next((p for p in programs if p["university_id"] == uid and norm(p["program"]) == norm(name)), None)
        if found:
            found.update(make_program(found["id"], uid, name, level, language, field, "CONFIRMED", srcs, facts=facts, discovery=discovery, city=city))
            return found
        p = make_program(f"discovered-{len([x for x in programs if x['discovery_source'] != 'previous_tracker'])+1:03d}", uid, name, level, language, field, "CONFIRMED", srcs, facts=facts, discovery=discovery, city=city)
        programs.append(p)
        return p

    # Program-level 2027/28 confirmation; fields shown here have official evidence.
    pisa_deadline = fact({"end":"2027-02-01","applies_to":"non-EU applicants residing abroad"},"CONFIRMED",["SRC-PISA-CALL-2027"])
    pisa_fee = fact({"amount_eur":30,"per":"application","maximum_applications":2},"CONFIRMED",["SRC-PISA-CALL-2027"])
    for name, field, source in [
        ("Computer Science","Computer Science","SRC-PISA-CS"),
        ("Data Science and Business Informatics","Data Science","SRC-PISA-DSBI"),
    ]:
        promote("pisa",name,"MSc","English",field,["SRC-PISA-CALL-2027",source],{
            "application_deadline":pisa_deadline,"application_fee":pisa_fee,
            "tuition":fact(None,"NOT_YET_PUBLISHED",["SRC-PISA-CALL-2027"],"2027/28 tuition was not published in the call."),
            "available_places":fact(None,"UNAVAILABLE",["SRC-PISA-CALL-2027"],"No seat count is stated in the reviewed call."),
            "acceptance_rate":fact(None,"UNAVAILABLE",["SRC-PISA-CALL-2027"],"No acceptance rate is stated in the reviewed call.")})
    promote("pisa","Informatics for Digital Health","MSc","English","Computer Science",["SRC-PISA-CALL-2027","SRC-PISA-DH"],{
        "application_deadline":pisa_deadline,"application_fee":pisa_fee,
        "tuition":fact(None,"NOT_YET_PUBLISHED",["SRC-PISA-CALL-2027"],"2027/28 tuition was not published in the call."),
        "available_places":fact(None,"UNAVAILABLE",["SRC-PISA-CALL-2027"],"No seat count is stated in the reviewed call."),
        "acceptance_rate":fact(None,"UNAVAILABLE",["SRC-PISA-CALL-2027"],"No acceptance rate is stated in the reviewed call.")},discovery="newly_discovered")

    padua_programs = [
        ("History","BSc","Italian","Humanities"),
        ("Classical Languages and Literatures and Ancient History","MSc","Italian","Humanities"),
        ("Historical Sciences","MSc","Italian","Humanities"),
        ("Landscape Studies","MSc","Italian","Environmental Studies"),
        ("Religious Studies","MSc","Italian","Humanities"),
        ("Local Development","MSc","English","Social Sciences"),
        ("Mobility Studies","MSc","English","Social Sciences"),
    ]
    pdu_windows = fact([
        {"start":"2026-09-15","end":"2026-11-15","eligible_group":"All listed programs; first call"},
        {"start":"2026-12-01","end":"2027-03-01","eligible_group":"All listed programs; second call"},
        {"start":"2027-04-01","end":"2027-06-01","eligible_group":"EU and non-EU residents in Italy only; third call"}],"CONFIRMED",["SRC-PADUA-PROGRAMS-2027"])
    for name, level, language, field in padua_programs:
        promote("padova",name,level,language,field,["SRC-PADUA-PROGRAMS-2027"],{
            "application_windows":pdu_windows,
            "program_specific_requirements":fact(None,"REQUIRES_VERIFICATION",["SRC-PADUA-PROGRAMS-2027"],"Course-specific requirements were not included in the reviewed call summary."),
            "tuition":fact(None,"REQUIRES_VERIFICATION",["SRC-PADUA-INTL-2027"],"Program-specific 2027/28 tuition and individual eligibility need review."),
            "acceptance_rate":fact(None,"UNAVAILABLE",["SRC-PADUA-PROGRAMS-2027"],"No acceptance rate is stated in this call listing.")},discovery="newly_discovered")

    promote("firenze","Software: Science and Technology","MSc","English","Computer Science",["SRC-UNIFI-SST-2027","SRC-UNIFI-SST-LANGUAGE"],{
        "application_deadline":fact(None,"REQUIRES_VERIFICATION",["SRC-UNIFI-SST-2027"],"The program page confirms 2027/28 admission requirements but does not give an application date."),
        "requirements":fact({"bachelor_grade":"country-specific threshold","credits":{"computer_science_or_computer_engineering":24,"mathematics_physics_or_statistics":24},"english":"B2","interview":"may be requested"},"CONFIRMED",["SRC-UNIFI-SST-2027"]),
        "duration":fact("2 years / 120 CFU","CONFIRMED",["SRC-UNIFI-SST-LANGUAGE"]),
        "tuition":fact(None,"REQUIRES_VERIFICATION",["SRC-UNIFI-SST-2027"],"No 2027/28 fee is stated on this program admission page.")})

    promote("napoli-federico-ii","Chemical Engineering","MSc","Italian/English","Engineering",["SRC-UNINA-CHE-2027","SRC-UNINA-CHE-PROGRAM"],{
        "application_opening":fact("2027-01-10","CONFIRMED",["SRC-UNINA-CHE-2027"]),
        "universitaly_opening":fact("February or March 2027","CONFIRMED",["SRC-UNINA-CHE-2027"],"The source gives a month range, not an exact day."),
        "application_deadline":fact(None,"NOT_YET_PUBLISHED",["SRC-UNINA-CHE-2027"],"The official notice says precise dates and deadlines will be published later."),
        "english_tracks":fact(["Product Engineering","Sustainable Engineering"],"CONFIRMED",["SRC-UNINA-CHE-PROGRAM"]),
        "application_fee":fact(None,"REQUIRES_VERIFICATION",["SRC-UNINA-CHE-2027"],"The reviewed notice does not state a fee.")},discovery="newly_discovered")

    promote("tor-vergata","Mechatronics Engineering","MSc","English","Engineering",["SRC-TORVERGATA-MECH-2027","SRC-TORVERGATA-MECH-LANGUAGE"],{
        "duration":fact("2 years / 120 credits","CONFIRMED",["SRC-TORVERGATA-MECH-2027"]),
        "application_windows":fact([
            {"start":"2026-11-09","end":"2026-11-27","eligible_group":"Non-EU visa applicants"},
            {"start":"2027-01-11","end":"2027-01-25","eligible_group":"Non-EU visa applicants"},
            {"start":"2027-02-08","end":"2027-02-22","eligible_group":"Non-EU visa applicants"},
            {"start":"2027-07-05","end":"2027-09-06","eligible_group":"EU or non-EU residents in Italy with Italian bachelor’s"}],"CONFIRMED",["SRC-TORVERGATA-MECH-2027"]),
        "application_fee":fact({"amount_eur":30,"per":"application"},"CONFIRMED",["SRC-TORVERGATA-MECH-2027"]),
        "available_places":fact({"non_eu_abroad":60,"china_marco_polo":4},"CONFIRMED",["SRC-TORVERGATA-MECH-2027"]),
        "requirements":fact({"english":"B2","bachelor":"engineering or related field; curricular credits required"},"CONFIRMED",["SRC-TORVERGATA-MECH-2027"]),
        "acceptance_rate":fact(None,"UNAVAILABLE",["SRC-TORVERGATA-MECH-2027"],"Call publishes places but no applicant or admitted-student totals, so no rate is calculated.")},discovery="newly_discovered")

    promote("ca-foscari","Buddhism and Asian Religions","MSc","English","Religion",["SRC-CA-FOSCARI-BUDDHISM-2027"],{
        "duration":fact("2 years / 120 credits","CONFIRMED",["SRC-CA-FOSCARI-BUDDHISM-2027"]),
        "access_type":fact("Open admission with preparation and program requirements","CONFIRMED",["SRC-CA-FOSCARI-BUDDHISM-2027"]),
        "english_requirement":fact("B2","CONFIRMED",["SRC-CA-FOSCARI-BUDDHISM-2027"]),
        "application_deadline":fact(None,"NOT_YET_PUBLISHED",["SRC-CA-FOSCARI-BUDDHISM-2027"],"Program page says detailed 2027/28 procedures and deadlines will be updated in March 2027."),
        "tuition":fact(None,"REQUIRES_VERIFICATION",["SRC-CA-FOSCARI-BUDDHISM-2027"],"Program-specific 2027/28 tuition is not stated on the reviewed admission page.")},discovery="newly_discovered")

    # CLE is cycle-confirmed, but instruction language was not verified in the reviewed source.
    cle = make_program("discovered-012","bologna","Cultures Littéraires Européennes (CLE) Erasmus Mundus Joint Master","MSc","REQUIRES_VERIFICATION","Humanities","REQUIRES_VERIFICATION",["SRC-BOLOGNA-CLE-2027"],facts={
        "application_windows":fact([{"start":"2026-11","end":"2027-02","label":"Intake 1"},{"start":"2027-03","end":"2027-04","label":"Intake 2"}],"CONFIRMED",["SRC-BOLOGNA-CLE-2027"],"Month-level windows only; exact days are not listed."),
        "language":fact(None,"REQUIRES_VERIFICATION",["SRC-BOLOGNA-CLE-2027"],"The reviewed call does not state the language of instruction."),
        "application_fee":fact(None,"REQUIRES_VERIFICATION",["SRC-BOLOGNA-CLE-2027"],"The reviewed 2027/28 page does not establish an application fee.")},discovery="newly_discovered")
    cle["availability_2027_2028"] = fact(True,"CONFIRMED",["SRC-BOLOGNA-CLE-2027"])
    cle["source_ids"] = ["SRC-BOLOGNA-CLE-2027"]
    programs.append(cle)

    cse = promote("bologna","Computer Science and Engineering","MSc","English","Computer Science",["SRC-UNIBO-CSE-2027","SRC-UNIBO-28DIGITAL-2027"],{
        "curriculum":fact("Intelligent Embedded Systems – 28Digital track","CONFIRMED",["SRC-UNIBO-CSE-2027","SRC-UNIBO-28DIGITAL-2027"]),
        "application_windows":fact([
            {"start":"2026-10-30","end":"2027-01-31","eligible_group":"EU/EEA/CH and non-EU applicants; non-EU applicants are encouraged to apply in this first session"},
            {"start":"2027-02-01","end":"2027-04-18","eligible_group":"EU/EEA/CH and non-EU applicants; second session primarily reserved for EU/EEA/CH and applicants not requiring a residence permit"},
            {"start":"2027-04-19","end":"2027-05-31","eligible_group":"EU/EEA/CH and non-EU applicants not requiring a study visa"}],"CONFIRMED",["SRC-UNIBO-28DIGITAL-2027"],"Times are CET/CEST as shown on the official program page; admissions are managed by 28Digital."),
        "application_route":fact("Selection managed directly by 28Digital Master School","CONFIRMED",["SRC-UNIBO-CSE-2027","SRC-UNIBO-28DIGITAL-2027"]),
        "available_places":fact(10,"CONFIRMED",["SRC-UNIBO-CSE-2027"],"Published limit for the 28Digital track."),
        "requirements":fact({"bachelor":"Relevant first-cycle degree, or other degree meeting subject-credit requirements","minimum_subject_credits":42,"minimum_computer_science_or_engineering_credits":18,"english":"B2"},"CONFIRMED",["SRC-UNIBO-CSE-2027"]),
        "application_fee":fact(None,"REQUIRES_VERIFICATION",["SRC-UNIBO-CSE-2027","SRC-UNIBO-28DIGITAL-2027"],"The reviewed 2027/28 28Digital track pages do not establish its application fee."),
        "tuition":fact(None,"REQUIRES_VERIFICATION",["SRC-UNIBO-28DIGITAL-2027"],"The reviewed track page does not state the applicable 2027/28 tuition."),
        "acceptance_rate":fact(None,"UNAVAILABLE",["SRC-UNIBO-CSE-2027"],"The reviewed official pages give a 10-place limit but no applicant/admission counts from which to calculate a rate.")})
    cse["program"] = "Computer Science and Engineering — Intelligent Embedded Systems (28Digital track)"

    # The UniTrento 28DIGITAL technical majors are individually listed for the 2027/28 intake.
    # Central and department pages disagree on round boundaries, so preserve that field-level conflict.
    digital_tracks = [
        ("discovered-013","Cyber Security (CSES) – 28DIGITAL Master’s track","Computer Science","Computer Science","Entry and exit", "SRC-28DIGITAL-CYBER-2027", {"eligible_bachelor_fields":["Computer Science","Information Systems","Mathematics","Electrical Engineering"],"relevant_experience":"may be considered"}),
        ("discovered-014","Data Science (DSC) – 28DIGITAL Master’s track","Computer Science","Data Science","Exit", "SRC-28DIGITAL-DSC-2027", {"eligible_bachelor_fields":["Computer Science","Information Systems","Mathematics","Statistics","Electrical Engineering/Electronics"],"minimum_computer_science_ects":60,"minimum_mathematics_ects":30}),
        ("discovered-015","Fintech (FT) – 28DIGITAL Master’s track","Computer Science","Finance and Technology","Entry and exit", "SRC-28DIGITAL-FINTECH-2027", {"eligible_bachelor_fields":["Computer Science","Telecommunication Engineering","Information Systems","Mathematics","Statistics","Electrical Engineering/Electronics","Information Technology","Software Engineering","Business Informatics","Business Administration and Finance with strong computer science component"],"relevant_experience":"may be considered"}),
        ("discovered-016","Human-Computer Interaction and Design with Extended Reality (HCID/XR) – 28DIGITAL track","Computer Science","Human-Computer Interaction","Exit", "SRC-28DIGITAL-HCIDXR-2027", {"eligible_bachelor_fields":["Computer Science","Information Systems","Interaction Design","Cognitive Science","Engineering"],"relevant_experience":"HCI, UX or XR experience may be considered"}),
        ("discovered-017","Cloud and Networking Infrastructure and HPC (CNIHPC) – 28DIGITAL track","Engineering","Computer Engineering","Entry and exit", "SRC-28DIGITAL-CLOUD-2027", {"eligible_bachelor_fields":["Computer Science","Computer Engineering","Electrical/Electronic Engineering","Information Systems","related fields"],"expected_background":["mathematics","computer science foundations","computer architecture"]}),
        ("discovered-018","Intelligent Chips and Systems (ICS) – 28DIGITAL track","Engineering","Electrical and Computer Engineering","Exit", "SRC-28DIGITAL-ICS-2027", {"eligible_bachelor_fields":["Computer Science","Electrical Engineering","Computer Engineering","Software Engineering","Mechatronics","Mathematics","related fields"],"minimum_ict_ects":40,"minimum_mathematics_ects":20}),
        ("discovered-019","Artificial Intelligence with Affective Computing (AIAC) – 28DIGITAL track","Artificial Intelligence","Artificial Intelligence","Entry and exit", "SRC-28DIGITAL-AIAC-2027", {"eligible_bachelor_fields":["Computer Science","Data Science","Electrical Engineering","Information Technology","Cognitive Science","related fields"],"expected_background":["programming","algorithms","mathematics","statistics"]}),
    ]
    shared_conflicting_windows = fact({
        "unitrento_department_page":[
            {"label":"Period 1","start":"2026-10-31","end":"2027-02-11","eligible_group":"EU/EEA/CH and non-EU applicants"},
            {"label":"Period 2","start":"2027-02-11","end":"2027-04-15","eligible_group":"EU/EEA/CH and non-EU applicants residing in Italy; visa timing limits apply"},
            {"label":"Period 3","start":"2027-04-15","end":"2027-06-01","eligible_group":"EU/EEA/CH and non-EU applicants residing in Italy"}],
        "central_28digital_admissions_page":[
            {"label":"Period 1","start":"2026-10-30","end":"2027-01-31","eligible_group":"EU/EEA/CH and non-EU applicants; primarily aimed at applicants needing a study residence permit"},
            {"label":"Period 2","start":"2027-02-01","end":"2027-04-18","eligible_group":"Primarily EU and applicants not requiring a study permit"},
            {"label":"Period 3","start":"2027-04-19","end":"2027-05-31","eligible_group":"EU and applicants not requiring a study permit"}]},
        "CONFLICTING_SOURCES",["SRC-UNITRENTO-28DIGITAL-2027","SRC-28DIGITAL-ADMISSIONS-2027"],"The official UniTrento department page gives different round boundaries from the central 28DIGITAL admissions page. Each individual track page confirms the first-period deadline of 31 January 2027; verify the specific chosen pathway in the central application portal.")
    shared_digital_fees = fact({"application_fee_eur":75,"application_fee_refundable":False,"registration_deposit_eur":250,"registration_deposit_refundable":False,"registration_deposit_credited_to":"first semester tuition","annual_tuition_eur":{"EU_EEA":6000,"non_EU_EEA":18000}},"CONFIRMED",["SRC-28DIGITAL-FEES-2027"],"Tuition is stated per academic year. British citizens applying from 1 January 2021 onward are charged the non-EU rate.")
    shared_digital_scholarships = fact({"merit_awards":["full tuition waiver","half tuition waiver"],"excellence_awards":{"tuition":"full tuition waiver","living_allowance":"based on average living costs in study country","eligibility":"EU/EEA and associated-country citizens in selected programs"},"application":"apply through the 28DIGITAL portal with the program application","unitrento_mobility_award_eur_range":[2500,4500],"unitrento_mobility_award_eligibility":"UniTrento entry students during second year abroad"},"CONFIRMED",["SRC-28DIGITAL-FEES-2027"],"Scholarships are competitive and eligibility/combination rules vary by award and partner university; amounts are not guaranteed to every admitted student.")
    for pid, name, field, subject, unitn_role, track_source, track_requirements in digital_tracks:
        p = make_program(pid,"trento",name,"MSc","English",field,"CONFIRMED",["SRC-UNITRENTO-28DIGITAL-2027","SRC-28DIGITAL-ADMISSIONS-2027","SRC-28DIGITAL-FEES-2027",track_source],facts={
            "curriculum":fact(subject,"CONFIRMED",["SRC-UNITRENTO-28DIGITAL-2027",track_source]),
            "duration":fact("2 years / 120 ECTS; double degree with mandatory mobility between entry and exit universities","CONFIRMED",["SRC-UNITRENTO-28DIGITAL-2027",track_source]),
            "unitrento_role":fact(unitn_role,"CONFIRMED",["SRC-UNITRENTO-28DIGITAL-2027"]),
            "application_route":fact("Central 28DIGITAL Master School application portal","CONFIRMED",["SRC-UNITRENTO-28DIGITAL-2027","SRC-28DIGITAL-ADMISSIONS-2027"]),
            "application_windows":shared_conflicting_windows,
            "application_deadline":fact({"end":"2027-01-31","time":"23:59 CET","period":"1"},"CONFIRMED",[track_source],"The individual track page confirms period 1; the UniTrento department page gives a conflicting period-1 end date."),
            "application_fee":fact({"amount_eur":75,"per":"submitted application","refundable":False},"CONFIRMED",["SRC-28DIGITAL-FEES-2027"]),
            "registration_fee":fact({"amount_eur":250,"per":"accepted offer","refundable":False,"credited_to":"first-semester tuition"},"CONFIRMED",["SRC-28DIGITAL-FEES-2027"]),
            "tuition":shared_digital_fees,
            "english_requirement":fact({"IELTS_Academic":"overall 6.5; no section below 6.0; speaking and writing at least 6.5","TOEFL_iBT_after_2026_01_21":"at least 4.5 total and each section; writing at least 5.0","TOEFL_iBT_before_2026_01_21":"at least 92 total; 21 each section; speaking at least 23; writing at least 24","waiver":"degree taught in English at a university in USA, Canada, UK, Ireland, Australia or New Zealand"},"CONFIRMED",["SRC-28DIGITAL-ADMISSIONS-2027"]),
            "requirements":fact({"minimum_bachelor_ects":180,**track_requirements},"CONFIRMED",["SRC-28DIGITAL-ADMISSIONS-2027",track_source]),
            "scholarships":shared_digital_scholarships,
            "available_places":fact(None,"UNAVAILABLE",[track_source],"No seat count is published on the reviewed track page."),
            "acceptance_rate":fact(None,"UNAVAILABLE",[track_source],"No applicant or admission totals are published from which to calculate a rate.")},discovery="newly_discovered",city="Trento")
        programs.append(p)

    # HySET's fifth edition starts in 2027 and is jointly coordinated by Polito and Polimi.
    # The 2027 cohort's Erasmus Mundus funding is not secured, so scholarship availability stays pending.
    hyset = make_program("discovered-020","politecnico-torino","Hydrogen Systems and Enabling Technologies (HySET Erasmus Mundus Joint Master)","MSc","English","Energy Engineering","CONFIRMED",[
        "SRC-POLITO-HYSET-2027","SRC-POLITO-HYSET-REQ-2027","SRC-POLITO-HYSET-CURRICULUM","SRC-POLITO-HYSET-ENGLISH","SRC-POLITO-HYSET-FEES-2027","SRC-POLITO-HYSET-SELF-FUNDED"],facts={
        "duration":fact("2 years / 120 ECTS","CONFIRMED",["SRC-POLITO-HYSET-CURRICULUM"]),
        "curriculum":fact("Hydrogen value chain; consortium mobility across Politecnico di Torino, Politecnico di Milano and partner universities","CONFIRMED",["SRC-POLITO-HYSET-CURRICULUM"]),
        "application_route":fact("Apply@PoliTO portal; Politecnico di Torino coordinates document review","CONFIRMED",["SRC-POLITO-HYSET-2027","SRC-POLITO-HYSET-REQ-2027"]),
        "application_windows":fact([{"start":"2026-10-01","end":"2026-11-15","end_time":"23:59 CET","eligible_group":"Applicants worldwide"}],"CONFIRMED",["SRC-POLITO-HYSET-2027"],"The current 2027–29 intake notice gives the exact close time."),
        "application_deadline":fact({"date":"2026-11-15","time":"23:59 CET"},"CONFIRMED",["SRC-POLITO-HYSET-2027"]),
        "requirements":fact({"minimum_bachelor_ects":180,"eligible_fields":["Mechanical Engineering","Energy Engineering","Chemical Engineering or Chemistry","Electrical Engineering","Aeronautical Engineering","Physics","Industrial Engineering"],"additional_background":"Applicants in Physics, Chemistry, Aeronautical Engineering or Electrical Engineering must show thermodynamics, heat transfer and fluid mechanics; a stronger chemistry background is required for the TU/e destination."},"CONFIRMED",["SRC-POLITO-HYSET-REQ-2027"]),
        "english_requirement":fact({"TOEFL_iBT":"90 total, minimum 21 each section","IELTS":"6.5 overall, minimum 6.0 each section","Cambridge_CAE":"160; 180 with minimum 169 each section for TU/e destination","waiver":"Only for qualifying nationals of English-speaking countries taught and evaluated in English"},"CONFIRMED",["SRC-POLITO-HYSET-REQ-2027"]),
        "selection_criteria":fact({"scoring":"100 points maximum","academic_achievements":"up to 30 points; page references GPA at least 3.0/4.0 in the scoring description","previous_study_relevance":"up to 30 points","recommendations_and_video":"up to 15 points","experience_and_awards":"up to 25 points","interview":"may be requested"},"CONFIRMED",["SRC-POLITO-HYSET-REQ-2027"],"The GPA reference appears within the scored academic-achievements criterion; the source does not present it as a separate universal minimum eligibility rule."),
        "application_fee":fact(None,"UNAVAILABLE",["SRC-POLITO-HYSET-2027"],"No application fee is stated in the reviewed 2027–29 call pages."),
        "tuition":fact({"self_funded_eur_per_year":{"European":4500,"non_European":9000},"total_for_two_years_eur":{"European":9000,"non_European":18000},"living_and_travel":"excluded"},"CONFIRMED",["SRC-POLITO-HYSET-SELF-FUNDED"]),
        "payment_structure":fact("May be paid in full or in instalments; payment method and deadlines will be provided later.","CONFIRMED",["SRC-POLITO-HYSET-SELF-FUNDED"]),
        "scholarships":fact(None,"NOT_YET_PUBLISHED",["SRC-POLITO-HYSET-FEES-2027"],"External funding for the 2027 cohort had not been secured as of the official funding update; Erasmus Mundus scholarships are not guaranteed. The self-funded route remains available."),
        "available_places":fact(None,"UNAVAILABLE",["SRC-POLITO-HYSET-REQ-2027"],"The programme says places are limited but the reviewed official pages do not give a seat count."),
        "acceptance_rate":fact(None,"UNAVAILABLE",["SRC-POLITO-HYSET-REQ-2027"],"The reviewed official pages do not publish applicant and admission totals.")},discovery="newly_discovered",city="Turin")
    programs.append(hyset)

    # UniGe has a published non-offer notice and a separate planned joint degree whose formal status is pending.
    maritime = make_program("discovered-021","genova","Maritime Science and Technology","BSc","English","Maritime Science","REQUIRES_VERIFICATION",[],facts={},discovery="newly_discovered")
    maritime["overall_status"] = "NOT_APPLICABLE"
    maritime["availability_2027_2028"] = fact(False,"CONFIRMED",["SRC-UNIGE-MST-2027"],"Official notice says first-year enrollment will not be possible for 2027/28.")
    maritime["source_ids"] = ["SRC-UNIGE-MST-2027"]
    programs.append(maritime)

    cores = make_program("discovered-022","genova","Conservation and Restoration Sciences (CORES Joint Master)","MSc","REQUIRES_VERIFICATION","Conservation and Restoration Sciences","REQUIRES_VERIFICATION",[],facts={},discovery="newly_discovered")
    cores["level"] = fact("MSc","CONFIRMED",["SRC-UNIGE-CORES-2027"])
    cores["field"] = fact("Conservation and Restoration Sciences","CONFIRMED",["SRC-UNIGE-CORES-2027"])
    cores["availability_2027_2028"] = fact(None,"REQUIRES_VERIFICATION",["SRC-UNIGE-CORES-2027"],"UniGe announced a planned 2027/28 start, but its Erasmus Mundus Joint Master proposal was still under evaluation and formal call details were not published.")
    cores["facts"] = {
        "application_opening":fact("Planned for early 2027","CONFIRMED",["SRC-UNIGE-CORES-2027"],"This is a published plan, not an exact application date."),
        "application_deadline":fact(None,"NOT_YET_PUBLISHED",["SRC-UNIGE-CORES-2027"],"No exact deadline was included in the university announcement; formal call details remain pending."),
        "consortium":fact(["Università degli Studi di Genova","Universidad de Sevilla","Université Bordeaux-Montaigne","University of Montenegro","Universität Münster"],"CONFIRMED",["SRC-UNIGE-CORES-2027"],"The announcement names UniGe as coordinator and describes four partner universities.")}
    programs.append(cores)

    # The 2027/28 catalogue confirms second-year teaching for the 2026/27 cohort,
    # while the international calls describe windows by degree category rather
    # than naming Data Science. Keep the new-entry availability pending.
    data_science = next(p for p in programs if p["id"] == "legacy-076")
    ds_catalogue_sources = ["SRC-UNIME-DS-COURSE-ICT-2027", "SRC-UNIME-DS-COURSE-ECONOMY-2027"]
    data_science["level"] = fact("MSc", "CONFIRMED", ds_catalogue_sources)
    data_science["language"] = fact("English", "CONFIRMED", ds_catalogue_sources)
    data_science["field"] = fact("Data Science", "CONFIRMED", ds_catalogue_sources)
    data_science["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ds_catalogue_sources + ["SRC-UNIME-2027"], "The catalogue confirms second-year courses taught in 2027/28 for students enrolled in 2026/27. The 2027/28 calls do not name Data Science individually, so admission of a new first-year cohort and program-specific eligibility remain unconfirmed.")
    data_science["overall_status"] = "REQUIRES_VERIFICATION"
    data_science["source_ids"] = ds_catalogue_sources + ["SRC-UNIME-2027", "SRC-UNIME-ENGLISH-PROGRAMS", "SRC-UNIME-MASTERS-PROGRAMS", "SRC-UNIME-DS-PAGE"]
    uni_messina = next(u for u in uni_rows if u["id"] == "messina")
    windows = uni_messina["cycle_facts"]["application_windows"]
    fee = uni_messina["cycle_facts"]["application_fee"]
    data_science["facts"] = {
        "academic_year_course_offering": fact({"academic_year":"2027/28","course":"Big Data (ICT curriculum); Big Data and Artificial Intelligence (Economy curriculum)","year_of_course":2,"enrollment_cohort":"2026/27"}, "CONFIRMED", ds_catalogue_sources, "Confirms current second-year teaching only; it does not establish that first-year admission is open for 2027/28."),
        "application_windows": fact(windows["value"], "CONFIRMED", windows["source_ids"], "These are university-wide 2027/28 international application calls for degree categories. The call page does not name Data Science or establish its new-cohort intake."),
        "application_fee": fact(fee["value"], "CONFIRMED", fee["source_ids"], "University-wide pre-evaluation fee: €40 for up to two program applications; no separate Data Science fee is stated."),
        "program_specific_requirements": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNIME-2027"], "The 2027/28 call directs applicants to the chosen program's entry requirements. No Data Science-specific 2027/28 admission requirements or new-cohort call were identified."),
    }

    # Append this later-discovered Catania successor after the legacy ID-based
    # batch constructors so existing discovery IDs remain stable.
    catania_ds = make_program("discovered-023", "catania", "Data Science", "MSc", "English", "Data Science", "REQUIRES_VERIFICATION", [], facts={}, discovery="newly_discovered")
    catania_ds["level"] = fact("MSc", "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-PROGRAM-2026", "SRC-UNICT-MASTER-ADMISSION-2026"], "Confirmed in the official 2026/27 listing; not independently confirmed for 2027/28.")
    catania_ds["language"] = fact("English", "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-PROGRAM-2026", "SRC-UNICT-ENGLISH-MASTERS-2026"], "Confirmed in official 2026/27 pages; not independently confirmed for 2027/28.")
    catania_ds["field"] = fact("Data Science", "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-PROGRAM-2026"], "Official 2026/27 course name; the 2027/28 successor offer remains unverified.")
    catania_ds["availability_2027_2028"] = fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-PROGRAM-2026", "SRC-UNICT-ENGLISH-MASTERS-2026", "SRC-UNICT-MASTER-CALLS-INDEX"], "The latest official course and English-MSc call evidence located is for 2026/27. No 2027/28 first-year intake or program call was identified on the pages checked on 9 November 2026; absence from the reviewed pages is not treated as an explicit cancellation or publication statement.")
    catania_ds["previous_cycle_tags"] = {"level":"MSc", "language":"English", "field":"Data Science", "cycle":"2026-2027", "label":"Latest official 2026/27 listing"}
    catania_ds["source_ids"] = ["SRC-UNICT-DS-PROGRAM-2026", "SRC-UNICT-ENGLISH-MASTERS-2026", "SRC-UNICT-MASTER-ADMISSION-2026", "SRC-UNICT-DS-CALL-2026"]
    catania_ds["facts"] = {
        "previous_cycle_course_listing": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-PROGRAM-2026", "SRC-UNICT-ENGLISH-MASTERS-2026"], "Latest official listing reviewed is 2026/27: Data Science, two-year Master's Degree (LM/DATA), taught in English in Catania. These prior-cycle descriptors do not confirm the 2027/28 offer."),
        "previous_cycle_non_eu_admission": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-CALL-2026"], "The 2026/27 call included Data Science for non-EU applicants living abroad, with an application period of 10 February–17 March 2026 and a €10 fee per course. The call used title assessment and, where applicable, an interview or test. No 2027/28 rules or dates are confirmed by this prior-cycle source."),
        "program_specific_requirements": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-CALL-2026", "SRC-UNICT-MASTER-ADMISSION-2026"], "The reviewed course-level admission annexes and procedures are for 2026/27. 2027/28 curricular requirements, language evidence, selection details and applicant eligibility remain to be checked."),
        "application_fee": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-CALL-2026"], "The official prior-cycle non-EU call charged €10 per course application in 2026/27; this is not presented as the 2027/28 fee."),
        "available_places": fact(None, "REQUIRES_VERIFICATION", ["SRC-UNICT-DS-CALL-2026"], "The 2026/27 call table leaves the Data Science places field blank. No 2027/28 places have been identified."),
    }
    programs.append(catania_ds)

    verified = [p for p in programs if p["overall_status"] == "CONFIRMED"]
    level_counts = Counter(p["level"]["value"] for p in verified)
    fully_verified_count = len(verified)
    cycle_availability_count = sum(p["availability_2027_2028"]["status"] == "CONFIRMED" and p["availability_2027_2028"]["value"] is True for p in programs)
    programs_not_offered = sum(p["overall_status"] == "NOT_APPLICABLE" for p in programs)
    deadlines = {u["id"] for u in uni_rows if u["cycle_facts"].get("application_windows", {}).get("status") == "CONFIRMED" and any(w.get("end") for w in u["cycle_facts"]["application_windows"]["value"])}
    # Count exact program-specific application deadlines/windows, but exclude expected or conflicting schedules.
    for p in programs:
        if any(f.get("status") == "CONFIRMED" and f.get("value") for key, f in p.get("facts", {}).items() if key in {"application_deadline", "application_windows"}):
            deadlines.add(p["university_id"])
    not_published = {u["id"] for u in uni_rows if any(f.get("status") == "NOT_YET_PUBLISHED" for f in u["cycle_facts"].values())}
    deadline_related_fields = {"application_windows", "application_deadlines", "application_deadline", "bachelor_call", "application_procedure"}
    deadlines_not_published = {u["id"] for u in uni_rows if any(k in deadline_related_fields and f.get("status") == "NOT_YET_PUBLISHED" for k, f in u["cycle_facts"].items())}
    unavailable_or_conflicting = {
        p["university_id"] for p in programs
        if any(f.get("status") in {"UNAVAILABLE", "CONFLICTING_SOURCES"} for f in p.get("facts", {}).values())
    } | {
        u["id"] for u in uni_rows
        if any(f.get("status") in {"UNAVAILABLE", "CONFLICTING_SOURCES"} for f in u.get("cycle_facts", {}).values())
    }
    conflicting_source_universities = {
        p["university_id"] for p in programs
        if any(f.get("status") == "CONFLICTING_SOURCES" for f in p.get("facts", {}).values())
    } | {
        u["id"] for u in uni_rows
        if any(f.get("status") == "CONFLICTING_SOURCES" for f in u.get("cycle_facts", {}).values())
    }
    coverage = {
        "academic_year": CYCLE,
        "as_of": AS_OF,
        "original_universities": len({ALIASES[p["university"]] for p in old}),
        "universities_researched": len(uni_rows),
        "universities_fully_verified": 0,
        "universities_partially_researched": len(uni_rows),
        "program_records": len(programs),
        "prior_tracker_programs_archived": len(old),
        "newly_discovered_programs": len(programs)-len(old),
        "programs_cycle_availability_confirmed": cycle_availability_count,
        "programs_fully_verified": fully_verified_count,
        "programs_requiring_verification": sum(p["overall_status"] == "REQUIRES_VERIFICATION" for p in programs),
        "programs_not_offered_2027_2028": programs_not_offered,
        "bsc_programs_verified": level_counts.get("BSc",0),
        "msc_programs_verified": level_counts.get("MSc",0),
        "universities_with_confirmed_deadline_windows": len(deadlines),
        "university_ids_with_confirmed_deadline_windows": sorted(deadlines),
        "universities_with_explicit_not_yet_published_fields": len(not_published),
        "university_ids_with_explicit_not_yet_published_fields": sorted(not_published),
        "universities_with_deadlines_or_calls_explicitly_not_yet_published": len(deadlines_not_published),
        "university_ids_with_deadlines_or_calls_explicitly_not_yet_published": sorted(deadlines_not_published),
        "universities_with_unavailable_or_conflicting_information": len(unavailable_or_conflicting),
        "university_ids_with_unavailable_or_conflicting_information": sorted(unavailable_or_conflicting),
        "universities_with_conflicting_sources": len(conflicting_source_universities),
        "university_ids_with_conflicting_sources": sorted(conflicting_source_universities),
        "source_records": len(SOURCES),
        "official_source_supported_fields": sum(
            sum(1 for k in ("level", "language", "field", "availability_2027_2028") if p[k]["status"] == "CONFIRMED" and p[k]["source_ids"])
            + sum(1 for f in p["facts"].values() if f["status"] == "CONFIRMED" and f["source_ids"])
            for p in programs
        ) + sum(1 for u in uni_rows for f in u["cycle_facts"].values() if f["status"] == "CONFIRMED" and f["source_ids"]),
        "verification_statuses": ["CONFIRMED","NOT_YET_PUBLISHED","UNAVAILABLE","REQUIRES_VERIFICATION","CONFLICTING_SOURCES","NOT_APPLICABLE"],
        "limitations": [
            "A homepage or admissions overview does not count as complete program research.",
            "Program availability is counted as confirmed only when an official 2027/28 source names the degree and supports its level and language.",
            "The historic tracker contained estimates and prior-cycle fees, deadlines, GPA labels, tiers and acceptance claims; these remain only in the archive and are not active facts.",
            "No university is marked fully verified until its complete relevant BSc/MSc offer and the required fields have been checked program by program.",
        ],
    }

    (RESEARCH / "sources.json").write_text(json.dumps(SOURCES, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
    (RESEARCH / "universities-2027-2028.json").write_text(json.dumps(uni_rows, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
    (RESEARCH / "programs-2027-2028.json").write_text(json.dumps(programs, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
    (RESEARCH / "coverage-report.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
    progress = {
        "academic_year": CYCLE, "as_of": AS_OF, "branch": "upgrade/2027-2028-research",
        "phase": "research_and_data_model_in_progress", "next_actions": [
            "Review each of the 34 universities' complete official BSc and MSc offers.",
            "Verify every candidate program's 2027/28 availability, language and applicant eligibility.",
            "Collect fees, scholarships, application routes, contacts and field-specific requirements from official 2027/28 notices.",
            "Recheck sources that currently say information is not yet published.",
            "Run data and UI quality checks, deploy a preview, then repeat research/QA before any production deployment.",
        ],
        "completed_batches": [
            {"id":"baseline-and-archive","status":"complete","result":"Archived all 165 prior program rows and mapped the original 34 universities."},
            {"id":"official-2027-28-initial-batch","status":"partial","result":"Recorded 34 university research outcomes, source-linked 14 core program offers, and explicitly marked outstanding program rows."},
            {"id":"official-2027-28-program-batch-2","status":"partial","result":"Verified the Bologna Intelligent Embedded Systems 28Digital track and seven UniTrento 28DIGITAL tracks; recorded program costs, requirements and a documented conflict between official round calendars."},
            {"id":"polito-hyset-and-bachelor-tests","status":"partial","result":"Verified the HySET 2027–29 intake, November 15 deadline, eligibility, English tests, scoring and self-funded tuition; recorded that scholarship funding is not guaranteed. Confirmed Polito’s 2027/28 in-person CISIA test formats while the detailed bachelor call remains pending."},
            {"id":"unige-program-cycle-outcomes","status":"partial","result":"Recorded the official notice that Maritime Science and Technology will not be offered in 2027/28, and the planned CORES joint MSc with its proposal and intake details still pending."},
            {"id":"polimi-admissions-scholarships-and-fees","status":"partial","result":"Recorded the official 2027/28 MSc schedules and €50/€150 application fees, the deadline-page Engineering schedule discrepancy, 2027/28 international merit scholarships, English certificate requirements, CEnT-S timing and pending BSc call, current contact pathway, and the fact that the reviewed tuition page still covers 2026/27. The 17 historic program rows remain pending individual 2027/28 checks."},
            {"id":"unime-data-science-cycle-outcome","status":"partial","result":"Verified official Data Science MSc coursework in English during AY 2027/28 for the 2026/27 cohort and attached the university-wide international application windows and €40 fee with explicit scope notes. A new 2027/28 entrant call and course-specific requirements remain unconfirmed."},
            {"id":"catania-data-science-course-replacement-and-prior-cycle-review","status":"partial","result":"Confirmed that Data Science for Management was replaced by Data Science from 2022/23; recorded the successor MSc, English language, LM/DATA class and 2026/27 non-EU call evidence as prior-cycle only. Reviewed Bachelor's admissions, current fees and international scholarship pages; no 2027/28 call, deadlines, fees or scholarship award was identified, so the successor intake remains unverified."},
        ],
        "counts": coverage,
    }
    (RESEARCH / "research-progress.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
    source_map = {s["id"]: s for s in SOURCES}
    lines = [
        "# Italy University Tracker — 2027–2028 research report",
        "",
        f"**Interim snapshot, checked {AS_OF}. The research and website upgrade remain in progress.**",
        "",
        "This report is a saved research checkpoint, not a completion claim. All 34 original universities are retained. The active dataset separates official cycle evidence from previous tracker leads; the latter no longer carry old deadlines, fees, tuition, GPA labels, tiers or acceptance estimates.",
        "",
        "## Snapshot counts",
        "",
        f"- Universities in the original application: **{coverage['original_universities']}**",
        f"- Universities with an official-source outcome documented: **{coverage['universities_researched']}**",
        f"- Universities fully verified across the requested program and admissions fields: **{coverage['universities_fully_verified']}**",
        f"- Universities partially researched: **{coverage['universities_partially_researched']}**",
        f"- Program records: **{coverage['program_records']}** ({coverage['prior_tracker_programs_archived']} archived prior listings + {coverage['newly_discovered_programs']} discoveries)",
        f"- Program availabilities named in 2027/28 official sources: **{coverage['programs_cycle_availability_confirmed']}**",
        f"- Program offers with core name, level, language and cycle availability verified: **{coverage['programs_fully_verified']}** ({coverage['bsc_programs_verified']} BSc, {coverage['msc_programs_verified']} MSc)",
        f"- Program records still requiring verification: **{coverage['programs_requiring_verification']}**; programs explicitly confirmed not offered in 2027/28: **{coverage['programs_not_offered_2027_2028']}**",
        f"- Universities with at least one confirmed date-specific 2027/28 application window in reviewed material: **{coverage['universities_with_confirmed_deadline_windows']}**",
        f"- Universities with admissions deadlines or calls explicitly marked not yet published: **{coverage['universities_with_deadlines_or_calls_explicitly_not_yet_published']}**",
        f"- Universities with at least one cycle field not yet published (including non-deadline fields): **{coverage['universities_with_explicit_not_yet_published_fields']}**",
        f"- Universities with an unavailable or conflicting researched program/university field: **{coverage['universities_with_unavailable_or_conflicting_information']}**; conflicting official sources: **{coverage['universities_with_conflicting_sources']}**",
        f"- Official source records: **{coverage['source_records']}**; source-backed confirmed fields: **{coverage['official_source_supported_fields']}**",
        "",
        "Program counts distinguish an availability confirmation from a fully verified program record. CLE at Bologna has a 2027/28 call page but its instruction language is still unverified. The UniTrento 28DIGITAL tracks are core-verified from their individual 2027/28 pages, while a round-calendar conflict between the University department and central 28DIGITAL pages remains visible in the application data. CORES at UniGe is a planned 2027/28 joint master, but the university says its proposal remains under evaluation. Messina's Data Science catalogue confirms English-taught second-year coursework during 2027/28 for the 2026/27 cohort; the 2027/28 new-entry intake remains unverified. Catania's former Data Science for Management course is marked discontinued based on the university's 2022/23 replacement notice. The successor Data Science MSc is separately listed as an unverified 2027/28 candidate because the latest official course page and non-EU call reviewed are for 2026/27.",
        "",
        "## Programs with core 2027/28 details confirmed",
        "",
        "| University | Program | Level | Language | Verified facts | Official sources |",
        "|---|---|---:|---|---|---|",
    ]
    for p in verified:
        fact_names = [k.replace("_", " ") for k, v in p["facts"].items() if v["status"] == "CONFIRMED"]
        source_titles = [source_map[sid]["title"] for sid in p["source_ids"] if sid in source_map]
        source_links = "; ".join(f"[{title}]({source_map[sid]['url']})" for sid in p["source_ids"] if sid in source_map for title in [source_map[sid]["title"]])
        lines.append(f"| {p['university']} | {p['program']} | {p['level']['value']} | {p['language']['value']} | {', '.join(fact_names) or 'Cycle availability, name, level and language'} | {source_links} |")
    not_offered = [p for p in programs if p["overall_status"] == "NOT_APPLICABLE"]
    if not_offered:
        lines += ["", "## Programs confirmed not offered in 2027/28", ""]
        for p in not_offered:
            source_links = "; ".join(f"[{source_map[sid]['title']}]({source_map[sid]['url']})" for sid in p["source_ids"] if sid in source_map)
            lines.append(f"- **{p['university']} — {p['program']}:** {p['availability_2027_2028']['notes']} {source_links}")
    lines += [
        "",
        "## Confirmed date windows and official publication status",
        "",
        "- **Padua:** first international call for most programs 15 September–15 November 2026; second 1 December 2026–1 March 2027; third 1 April–1 June 2027 for EU and non-EU applicants residing in Italy. Course calls may differ.",
        "- **Politecnico di Milano:** the general MSc schedule shows 1 October–1 December 2026 early bird, 12–28 January 2027 and an additional 1–18 March call for EEA and certain non-EEA residents in Italy. Architecture/Design has a separate 1 October–28 January general call. The same official deadline page has an Engineering subsection labelled 2026/27 despite describing the September 2027 intake, and lists 12 January–25 February; this conflict is recorded pending a program-specific resolution.",
        "- **Politecnico di Milano scholarships:** the 2027/28 official merit call lists 10 Platinum awards (€10,000 gross), 18 Gold (€8,000), 16 Piacenza Gold (€5,000), 10 Piacenza Bronze (€2,500), and 10 Silver tuition waivers. Campus, English-taught first-year MSc, early-bird admission application, competitive selection, and acceptance conditions apply. The reviewed tuition fee page still publishes 2026/27 amounts only; no 2027/28 tuition values are copied forward.",
        "- **Politecnico di Milano BSc Engineering:** the official page says the 2027/28 full admissions call will be published shortly. Current guidance lists TOL, TOLC-I, CEnT-S and SAT; the CEnT-S 2027/28 score-recording deadline for final-year or already-graduated students taking a test from September 2026 through 3 June 2027 is 3 June 2027 at 11:59 a.m.",
        "- **Pisa Computer Science department:** non-EU applicants residing abroad to the three named English MSc programs: deadline 1 February 2027 (Anywhere on Earth); €30 per application, up to two. 2027/28 tuition is not published in the reviewed call; it says annual rates are usually announced in June.",
        "- **Messina:** official 2027/28 calls include multiple international windows, including early-bird visa applications 1–20 December 2026, further visa calls in February–May 2027, selected single-cycle rounds, English Medicine/IMAT, and a non-visa window 6 July–13 November 2027. €40 covers up to two applications. Program-specific conditions apply. The 2027/28 course catalogue lists Data Science MSc coursework in English for Year 2 students from the 2026/27 cohort; this does not confirm that new 2027/28 students can enter the course.",
        "- **Catania:** the former Data Science for Management MSc was replaced by Data Science from 2022/23, so the legacy entry is marked discontinued. Data Science appears as a two-year English MSc (LM/DATA) in 2026/27 sources. Its 2026/27 non-EU call ran 10 February–17 March 2026 and charged €10 per course application; the 2027/28 call, program availability, fee schedule and scholarship cycle remain unverified. The 2026/27 fee manifesto and scholarship notice are linked as historical evidence only.",
        "- **Tor Vergata Mechatronics Engineering:** visa-applicant rounds 9–27 November 2026, 11–25 January 2027 and 8–22 February 2027; €30 application fee and 60 places for non-EU applicants abroad plus 4 Marco Polo places.",
        "- **Bologna and UniTrento 28DIGITAL tracks:** individual 28DIGITAL pages confirm period-one deadlines through 31 January 2027. UniTrento's department page gives different round boundaries from 28DIGITAL's central admissions page; the conflict is recorded and later rounds should be checked in the central portal.",
        "- **Expected or upcoming, not confirmed deadlines:** Genoa labels its mid-December 2026 to end-March 2027 visa preselection dates as expected. Ca’ Foscari says 2027/28 applications open in December 2026 but exact windows are pending. Siena says the next intake opens in November 2026, without day-level dates yet.",
        "- **Explicitly not yet published in reviewed official pages:** Politecnico di Bari (first-cycle call instructions expected February 2027), Politecnico di Torino (bachelor calls being finalized), Parma (procedure to follow), Palermo (exact dates), Siena (exact deadlines), and Ca’ Foscari (exact windows).",
        "",
        "These date counts refer to at least one official program or applicant group at a university; they do not establish dates for every program listed at that institution.",
        "",
        "## University-by-university checklist",
        "",
        "Coverage codes: **P** = partial review recorded; **—** = not yet reviewed. The underlying JSON retains every checklist item separately, together with the official URL, source IDs and evidence notes. No university is fully verified in this snapshot.",
        "",
        "| University | Status | International page | BSc | MSc | English programs | Fees | Scholarships | Non-EU | Deadlines | Program review | Research outcome |",
        "|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|",
    ]
    checklist_keys = ["international_admissions_page_examined", "bachelors_admissions_examined", "masters_admissions_examined", "english_programs_examined", "fees_examined", "scholarships_examined", "non_eu_requirements_examined", "application_deadlines_examined", "program_level_review"]
    for u in uni_rows:
        vals = ["P" if u["coverage"][k] == "partial" else ("✓" if u["coverage"][k] == "complete" else "—") for k in checklist_keys]
        srcid = u["source_ids"][0] if u["source_ids"] else ""
        src = source_map.get(srcid, {})
        cite = f"[{src.get('title', 'official page')}]({src.get('url', u['international_admissions_url'])})" if src else f"[official page]({u['international_admissions_url']})"
        lines.append(f"| {u['name']} | {u['cycle_status']} | " + " | ".join(vals) + f" | {u['research_summary']} {cite} |")
    lines += [
        "",
        "## Data limits and next research batch",
        "",
        "- The 165 original rows remain candidates until each program's 2027/28 availability, teaching language, international eligibility and individual requirements are checked against official sources.",
        "- Program-level fees, scholarships, application contacts, accepted tests/certificates, required documents, EU vs non-EU rounds, places and selection statistics remain incomplete. No old-cycle value is carried into the active dataset.",
        "- No program-level acceptance rate was calculated. Where a reviewed call gives no rate or applicant counts, the record says so rather than inferring selectivity.",
        "- Continue university by university, inspect complete official BSc/MSc course catalogues, then refresh pages with pending call dates. Complete data, frontend, responsive, link and deployment audits before production release.",
        "",
        "## Repository data files",
        "",
        "- `universities-2027-2028.json` — source links, cycle facts and per-university coverage checklist.",
        "- `programs-2027-2028.json` — active program records, field statuses and source IDs.",
        "- `sources.json` — official source records and evidence notes.",
        "- `coverage-report.json` and `research-progress.json` — computed counts and work state.",
        "- `archive/legacy-programs.json` — preserved historic input; not used as current admissions data.",
    ]
    (RESEARCH / "2027-2028-final-report.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    if (ROOT / "build").is_dir():
        shutil.copyfile(ROOT / "index.html", ROOT / "build" / "index.html")
    print(json.dumps({"universities":len(uni_rows),"programs":len(programs),"confirmed_programs":len(verified),"confirmed_bsc":level_counts.get("BSc",0),"confirmed_msc":level_counts.get("MSc",0),"sources":len(SOURCES),"deadline_universities":len(deadlines)},indent=2))


if __name__ == "__main__":
    build()
