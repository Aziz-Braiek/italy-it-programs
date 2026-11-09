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
    ("politecnico-milano", "Politecnico di Milano", "Milan", "Lombardy", "https://www.polimi.it/", "https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-magistrale/foreign-qualification/deadlines", "CONFIRMED", "Official 2027/28 MSc application windows are published; program-by-program availability and requirements remain to be checked."),
    ("politecnico-torino", "Politecnico di Torino", "Turin", "Piedmont", "https://www.polito.it/", "https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/bachelor-s-degree-programmes/calls-for-application-regulations-and-ranking-lists", "REQUIRES_VERIFICATION", "Official bachelor-call page says 2027/28 calls are being finalized; one special joint master call is not representative of the degree catalogue."),
    ("roma-tre", "Università degli Studi Roma Tre", "Rome", "Lazio", "https://www.uniroma3.it/", "https://orientamento.uniroma3.it/en/about-roma-tre/international-students-admissions/", "REQUIRES_VERIFICATION", "The official material reviewed covers international admission steps and a 2026/27 guide; 2027/28 degree-level calls remain outstanding."),
    ("sapienza", "Sapienza Università di Roma", "Rome", "Lazio", "https://www.uniroma1.it/", "https://www.uniroma1.it/en/pagina/international-admissions", "REQUIRES_VERIFICATION", "The international admissions material reviewed is still for 2026/27; 2027/28 program-level checks remain outstanding."),
    ("tor-vergata", "Università degli Studi di Roma Tor Vergata", "Rome", "Lazio", "https://web.uniroma2.it/", "https://mechatronics.uniroma2.it/how-to-apply-for-mechatronics/admission-a-y-2027-28/", "CONFIRMED", "The Mechatronics Engineering MSc has a detailed official 2027/28 call; the historic Computer Science row remains unverified."),
    ("ca-foscari", "Università Ca' Foscari Venezia", "Venice", "Veneto", "https://www.unive.it/", "https://www.unive.it/web/en/21001/admission-and-enrolment-with-an-international-qualification", "CONFIRMED", "Official international qualification page states that 2027/28 applications open in December 2026; exact windows and program calls are pending."),
    ("milano-bicocca", "Università degli Studi di Milano-Bicocca", "Milan", "Lombardy", "https://www.unimib.it/", "https://en.unimib.it/study/information-international-students/access-students-international-qualification", "REQUIRES_VERIFICATION", "The international qualifications page describes changes from 2027/28; program calls and dates need review."),
    ("marche", "Università Politecnica delle Marche", "Ancona", "Marche", "https://www.univpm.it/", "https://www.international.univpm.it/become-a-student/enrolment/non-eu-students-applying-for-a-visa/", "REQUIRES_VERIFICATION", "The official international site currently centers on 2026/27 admissions; program-level 2027/28 availability and calls remain outstanding."),
    ("catania", "Università degli Studi di Catania", "Catania", "Sicily", "https://www.unict.it/", "https://www.unict.it/en/node/5251", "REQUIRES_VERIFICATION", "Official international admissions information is general or for earlier cycles; historical programs require cycle-specific verification."),
    ("milano-statale", "Università degli Studi di Milano", "Milan", "Lombardy", "https://www.unimi.it/", "https://www.unimi.it/en/study/enrolment", "REQUIRES_VERIFICATION", "The official enrolment page reviewed describes 2026/27 procedures; 2027/28 program calls need review."),
    ("laquila", "Università degli Studi dell'Aquila", "L'Aquila", "Abruzzo", "https://www.univaq.it/", "https://www.univaq.it/en/section.php?id=2065&lang_s=en", "REQUIRES_VERIFICATION", "International admissions page identified; cycle-specific program-level calls remain outstanding."),
    ("insubria", "Università degli Studi dell'Insubria", "Varese", "Lombardy", "https://www.uninsubria.it/", "https://www.uninsubria.it/servizi/vivere-insubria/immatricolarsi-e-iscriversi/immatricolazioni/studenti-non-ue-residenti", "REQUIRES_VERIFICATION", "The non-EU page reviewed describes the prior cycle; 2027/28 offer and program requirements remain outstanding."),
    ("bologna", "Università di Bologna", "Bologna", "Emilia-Romagna", "https://www.unibo.it/", "https://www.unibo.it/en/study/how-to-apply", "REQUIRES_VERIFICATION", "A 2027/28 call is confirmed for the Erasmus Mundus CLE joint master's degree; broader degree-program calls remain outstanding."),
    ("camerino", "Università di Camerino", "Camerino", "Marche", "https://www.unicam.it/", "https://international.unicam.it/admissions/faq", "REQUIRES_VERIFICATION", "The official admissions material reviewed is for 2026/27 or general guidance; 2027/28 program-level checks remain outstanding."),
    ("ferrara", "Università degli Studi di Ferrara", "Ferrara", "Emilia-Romagna", "https://www.unife.it/", "https://www.unife.it/en/come-to-study/enroll/how-to-enroll/arrival-enrolment/enrol-in-a-post-graduate-course", "REQUIRES_VERIFICATION", "Official international postgraduate enrollment guidance was identified, but 2027/28 calls and current program availability remain outstanding."),
    ("firenze", "Università degli Studi di Firenze", "Florence", "Tuscany", "https://www.unifi.it/", "https://www.sst.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=168", "CONFIRMED", "The Software: Science and Technology MSc page gives specific 2027/28 admission requirements; the other historical programs still need verification."),
    ("genova", "Università degli Studi di Genova", "Genoa", "Liguria", "https://unige.it/en", "https://unige.it/en/international-enrolment", "REQUIRES_VERIFICATION", "2027/28 visa preselection is expected mid-December 2026 to end-March 2027, but exact dates are pending; €30 fee covers up to two assessments."),
    ("messina", "Università degli Studi di Messina", "Messina", "Sicily", "https://international.unime.it/", "https://international.unime.it/study-us/application-and-admission", "CONFIRMED", "Official 2027/28 international calls publish multiple application windows and a €40 fee for up to two applications; program-specific eligibility remains to be checked."),
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
    ("trento", "Università degli Studi di Trento", "Trento", "Trentino-Alto Adige", "https://www.unitn.it/en", "https://www.unitn.it/en/international/coming-unitrento/admission-how-it-works", "REQUIRES_VERIFICATION", "The general page describes typical December-to-March rounds; specific 2027/28 calls need individual review. A special RIT first-cycle opportunity is cycle-specific."),
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
    {"id":"SRC-POLIMI-DEADLINES-2027","university_id":"politecnico-milano","title":"Deadlines – Admission to Laurea Magistrale with foreign qualification","url":"https://www.polimi.it/en/prospective-students/how-to-apply/admission-to-laurea-magistrale/foreign-qualification/deadlines","source_type":"Official admissions deadlines page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"For MSc September 2027 intake, general application periods include 1 Oct–1 Dec 2026 early-bird and 12–28 Jan 2027; an additional 1–18 Mar 2027 call is restricted to EEA applicants and eligible non-EEA residents in Italy. Fees are €50 early-bird or €150 standard, for up to two programs. Architecture/Design has a separate cycle section.","supports":["university.application_window","university.application_fee","university.non_eu_process"]},
    {"id":"SRC-PISA-CALL-2027","university_id":"pisa","title":"International admissions call 2027/28 – English MSc programs","url":"https://didattica.di.unipi.it/wp-content/uploads/sites/2/2026/11/Bando2026_corsi_internazionali.pdf","source_type":"Official PDF admission call","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Department call lists MSc Computer Science, Data Science and Business Informatics, and Informatics for Digital Health. For non-EU applicants residing abroad it gives an application deadline of 1 February 2027 (Anywhere on Earth), notification on 1 March 2027, and a €30 fee per application (up to two). Tuition for 2027/28 is not specified; the call says annual fees are usually announced in June. No seats or acceptance rates are published in this call.","supports":["program.availability","program.deadline","program.application_fee","program.competitiveness","university.tuition"]},
    {"id":"SRC-PISA-CS","university_id":"pisa","title":"Master programme in Computer Science","url":"https://didattica.di.unipi.it/en/master-programme-in-computer-science/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official page describes the English-taught MSc Computer Science and links to international admissions. Cycle availability is confirmed separately by the 2027/28 department call.","supports":["program.name","program.level","program.language"]},
    {"id":"SRC-PISA-DSBI","university_id":"pisa","title":"Master programme in Data Science and Business Informatics","url":"https://didattica.di.unipi.it/en/master-programme-in-data-science-and-business-informatics/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official page describes the English-taught MSc. Cycle availability is confirmed separately by the 2027/28 department call.","supports":["program.name","program.level","program.language"]},
    {"id":"SRC-PISA-DH","university_id":"pisa","title":"Master programme in Informatics for Digital Health","url":"https://didattica.di.unipi.it/en/master-programme-in-informatics-for-digital-health/","source_type":"Official program page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Describes an English-taught open-admission MSc and links to foreign-student enrollment for AY 2027/28. The department call confirms cycle availability.","supports":["program.name","program.level","program.language","program.access_type"]},
    {"id":"SRC-UNIME-2027","university_id":"messina","title":"Application and Admission – 2027/28","url":"https://international.unime.it/study-us/application-and-admission","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Publishes 2027/28 application rounds for international candidates and a €40 fee for up to two program applications; English certificates are generally B2 unless exempt; program details and eligibility must be checked individually.","supports":["university.application_window","university.application_fee","university.english_requirement","university.non_eu_process"]},
    {"id":"SRC-UNIGE-2027","university_id":"genova","title":"UniGeApply International Admissions","url":"https://unige.it/en/international-enrolment","source_type":"Official international admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"2027/28 non-EU visa preselection is expected mid-December 2026 through end-March 2027; exact dates await publication. €30 fee covers up to two assessment applications. English-taught programs do not require Italian.","supports":["university.application_window_expected","university.application_fee","university.english_requirement"]},
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
    {"id":"SRC-POLITO-2027","university_id":"politecnico-torino","title":"Calls for application, regulations and ranking lists – Bachelor's","url":"https://www.polito.it/en/education/applying-studying-graduating/admissions-and-enrolment/bachelor-s-degree-programmes/calls-for-application-regulations-and-ranking-lists","source_type":"Official admissions page","accessed_at":AS_OF,"cycle":CYCLE,"evidence":"Official page says 2027/28 bachelor calls are being finalized and will be published soon; it also notes that CISIA tests will be used from 2027/28.","supports":["university.bachelor_deadline_status","university.admission_test"]},
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
        "availability_2027_2028": fact(status == "CONFIRMED", status, evidence_sources,
                                       None if status == "CONFIRMED" else "This program appears in the prior tracker or a discovery source, but its full 2027/28 offer has not been confirmed."),
        "overall_status": status,
        "discovery_source": discovery,
        "facts": facts or {},
        "source_ids": list(evidence_sources),
        "previous_tracker_tags": None,
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
            "bachelors_admissions_examined": "partial" if uid in {"padova", "politecnico-bari", "politecnico-torino", "firenze", "tor-vergata"} else "not_started",
            "masters_admissions_examined": "partial" if uid in {"padova", "politecnico-milano", "pisa", "firenze", "napoli-federico-ii", "tor-vergata", "messina", "genova"} else "not_started",
            "english_programs_examined": "partial" if uid in {"padova", "pisa", "firenze", "tor-vergata", "bologna", "genova"} else "not_started",
            "fees_examined": "partial" if uid in {"politecnico-milano", "pisa", "tor-vergata", "messina", "genova", "trento"} else "not_started",
            "scholarships_examined": "partial" if uid in {"pisa", "messina", "trento", "bologna"} else "not_started",
            "non_eu_requirements_examined": "partial" if src else "not_started",
            "application_deadlines_examined": "partial" if cycle_status in {"CONFIRMED", "NOT_YET_PUBLISHED"} or uid in {"genova", "politecnico-torino", "politecnico-bari"} else "not_started",
            "program_level_review": "partial" if uid in {"padova", "pisa", "firenze", "napoli-federico-ii", "tor-vergata", "bologna"} else "not_started",
        }
        relevant_sources = [s["id"] for s in SOURCES if s.get("university_id") == uid]
        if not relevant_sources:
            relevant_sources = []
        uni_rows.append({
            "id": uid, "name": name, "aliases": [alias for alias, alias_uid in ALIASES.items() if alias_uid == uid],
            "city": city, "region": region, "country": "Italy", "official_website": homepage,
            "international_admissions_url": admissions, "application_portal_url": None,
            "contact_email": None, "contact_url": admissions,
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
            {"label":"Early bird","start":"2026-10-01","end":"2026-12-01","eligible_group":"Most September 2027 MSc applicants; see study-area rules"},
            {"label":"Regular","start":"2027-01-12","end":"2027-01-28","eligible_group":"Most September 2027 MSc applicants; see study-area rules"},
            {"label":"Additional","start":"2027-03-01","end":"2027-03-18","eligible_group":"EEA and eligible non-EEA residents in Italy only"}], "CONFIRMED", ["SRC-POLIMI-DEADLINES-2027"], "Study-area exceptions apply; Architecture/Design has its own section."), "application_fee":fact({"early_bird_eur":50,"standard_eur":150,"program_limit":2},"CONFIRMED",["SRC-POLIMI-DEADLINES-2027"])},
        "pisa": {"application_windows": fact([{"label":"Non-EU abroad department call","start":None,"end":"2027-02-01","eligible_group":"Non-EU applicants residing abroad to the three named English MSc programs","timezone":"Anywhere on Earth"}], "CONFIRMED", ["SRC-PISA-CALL-2027"], "Call result date is 2027-03-01. This is a department call, not the entire university offer."), "application_fee":fact({"amount_eur":30,"per":"application","maximum_applications":2},"CONFIRMED",["SRC-PISA-CALL-2027"]), "tuition_2027_2028":fact(None,"NOT_YET_PUBLISHED",["SRC-PISA-CALL-2027"],"The call says annual fees are usually published in June; the listed 2026/27 range is not carried forward.")},
        "messina": {"application_windows": fact([
            {"label":"Early Bird visa applicants","start":"2026-12-01","end":"2026-12-20","eligible_group":"Non-EU study-visa applicants with final documents"},
            {"label":"Second call","start":"2027-02-02","end":"2027-03-19","eligible_group":"Visa applicants"},
            {"label":"Third call","start":"2027-04-08","end":"2027-05-08","eligible_group":"Visa applicants"},
            {"label":"Semestre Aperto","start":"2027-05-18","end":"2027-06-15","eligible_group":"Selected single-cycle degree programs"},
            {"label":"Medicine and Surgery (IMAT)","start":"2027-07-01","end":"2027-07-22","eligible_group":"English Medicine applicants"},
            {"label":"Non-visa applicants","start":"2027-07-06","end":"2027-11-13","eligible_group":"Applicants who do not need a study visa"}], "CONFIRMED", ["SRC-UNIME-2027"], "Program and applicant-category rules differ; use the live official call before applying."), "application_fee":fact({"amount_eur":40,"maximum_applications":2,"refundable":False},"CONFIRMED",["SRC-UNIME-2027"])},
        "genova": {"application_windows":fact([{"label":"Visa preselection (expected)","start":"2026-12-15","end":"2027-03-31","eligible_group":"Non-EU visa applicants","exact_dates":False}],"REQUIRES_VERIFICATION",["SRC-UNIGE-2027"],"The page labels these dates expected; exact opening and closing dates were not yet published."),"application_fee":fact({"amount_eur":30,"maximum_assessment_applications":2},"CONFIRMED",["SRC-UNIGE-2027"])},
        "ca-foscari": {"application_opening":fact("2026-12","CONFIRMED",["SRC-CA-FOSCARI-2027"],"Exact 2027/28 application periods were not yet listed."),"application_deadlines":fact(None,"NOT_YET_PUBLISHED",["SRC-CA-FOSCARI-2027"]),"honours_scholarships":fact({"bachelor_awards":8,"bachelor_eur_per_year":10000,"bachelor_years":3,"master_awards":20,"master_eur_per_year":10000,"master_years":2,"minimum_cgpa_percent":85,"ranking_factors":["CGPA","motivational video","reference letter(s)","language certification"]},"CONFIRMED",["SRC-CA-FOSCARI-SCHOLARSHIPS-2027"],"The complete 2027/28 call, including deadlines and detailed conditions, was expected in late fall 2026.")},
        "siena": {"application_opening":fact("2026-11","CONFIRMED",["SRC-SIENA-2027"],"The portal announces a November 2026 opening; precise dates are not yet listed."),"application_deadlines":fact(None,"NOT_YET_PUBLISHED",["SRC-SIENA-2027"])},
        "parma": {"application_procedure":fact(None,"NOT_YET_PUBLISHED",["SRC-PARMA-2027"],"The official page says application procedures will be communicated when available.")},
        "palermo": {"application_deadlines":fact(None,"NOT_YET_PUBLISHED",["SRC-PALERMO-2027"],"The official FAQ explicitly says exact 2027/28 dates have not yet been published.")},
        "politecnico-bari": {"bachelor_call":fact(None,"NOT_YET_PUBLISHED",["SRC-POLIBA-2027"],"Official page says instructions for 2027/28 first-level calls will be published in February 2027.")},
        "politecnico-torino": {"bachelor_call":fact(None,"NOT_YET_PUBLISHED",["SRC-POLITO-2027"],"Official page says 2027/28 calls are being finalized and will be published soon.")},
    }
    for u in uni_rows:
        u["cycle_facts"] = uni_facts.get(u["id"], {})

    programs = []
    for index, row in enumerate(old, 1):
        uid = ALIASES.get(row["university"])
        if not uid:
            raise ValueError(f"No university mapping for {row['university']!r}")
        pid = f"legacy-{index:03d}"
        programs.append(make_program(pid, uid, row["program"], row["level"], row["language"], row["field"], "REQUIRES_VERIFICATION", [], city=row.get("city"), discovery="previous_tracker"))
        programs[-1]["previous_tracker_tags"] = {"level":row["level"],"language":row["language"],"field":row["field"],"label":"Previous tracker classification — not reverified for 2027/28"}

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
    cle = make_program("discovered-011","bologna","Cultures Littéraires Européennes (CLE) Erasmus Mundus Joint Master","MSc","REQUIRES_VERIFICATION","Humanities","REQUIRES_VERIFICATION",["SRC-BOLOGNA-CLE-2027"],facts={
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

    verified = [p for p in programs if p["overall_status"] == "CONFIRMED"]
    level_counts = Counter(p["level"]["value"] for p in verified)
    fully_verified_count = len(verified)
    cycle_availability_count = sum(p["availability_2027_2028"]["status"] == "CONFIRMED" and p["availability_2027_2028"]["value"] is True for p in programs)
    deadlines = {u["id"] for u in uni_rows if u["cycle_facts"].get("application_windows", {}).get("status") == "CONFIRMED" and any(w.get("end") for w in u["cycle_facts"]["application_windows"]["value"])}
    # Include exact program-specific calls; do not count expected or month-only rounds.
    deadlines.update({"pisa", "tor-vergata"})
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
        "programs_requiring_verification": len(programs)-fully_verified_count,
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
        "universities_with_conflicting_sources": 0,
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
            {"id":"official-2027-28-initial-batch","status":"partial","result":"Recorded 34 university research outcomes, source-linked 13 program offers, and explicitly marked outstanding program rows."},
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
        f"- Universities with at least one confirmed date-specific 2027/28 application window in reviewed material: **{coverage['universities_with_confirmed_deadline_windows']}**",
        f"- Universities with admissions deadlines or calls explicitly marked not yet published: **{coverage['universities_with_deadlines_or_calls_explicitly_not_yet_published']}**",
        f"- Universities with at least one cycle field not yet published (including non-deadline fields): **{coverage['universities_with_explicit_not_yet_published_fields']}**",
        f"- Universities with an unavailable or conflicting researched program/university field: **{coverage['universities_with_unavailable_or_conflicting_information']}**; conflicting official sources: **{coverage['universities_with_conflicting_sources']}**",
        f"- Official source records: **{coverage['source_records']}**; source-backed confirmed fields: **{coverage['official_source_supported_fields']}**",
        "",
        "Program counts distinguish an availability confirmation from a fully verified program record. CLE at Bologna has a 2027/28 call page but its instruction language is still unverified, so it is included among the former and excluded from the latter.",
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
    lines += [
        "",
        "## Confirmed date windows and official publication status",
        "",
        "- **Padua:** first international call for most programs 15 September–15 November 2026; second 1 December 2026–1 March 2027; third 1 April–1 June 2027 for EU and non-EU applicants residing in Italy. Course calls may differ.",
        "- **Politecnico di Milano:** general MSc September 2027 early-bird window 1 October–1 December 2026, regular 12–28 January 2027; additional 1–18 March window only for EEA and eligible non-EEA residents in Italy. Study-area exceptions apply.",
        "- **Pisa Computer Science department:** non-EU applicants residing abroad to the three named English MSc programs: deadline 1 February 2027 (Anywhere on Earth); €30 per application, up to two. 2027/28 tuition is not published in the reviewed call; it says annual rates are usually announced in June.",
        "- **Messina:** official 2027/28 calls include multiple international windows, including early-bird visa applications 1–20 December 2026, further visa calls in February–May 2027, selected single-cycle rounds, English Medicine/IMAT, and a non-visa window 6 July–13 November 2027. €40 covers up to two applications. Program-specific conditions apply.",
        "- **Tor Vergata Mechatronics Engineering:** visa-applicant rounds 9–27 November 2026, 11–25 January 2027 and 8–22 February 2027; €30 application fee and 60 places for non-EU applicants abroad plus 4 Marco Polo places.",
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
