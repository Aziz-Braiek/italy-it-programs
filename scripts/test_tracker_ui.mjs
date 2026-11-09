import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";

const html = await readFile(new URL("../index.html", import.meta.url), "utf8");
const script = html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert.ok(script, "tracker inline script exists");

const dataFiles = {
  "/research/programs-2027-2028.json": "../research/programs-2027-2028.json",
  "/research/universities-2027-2028.json": "../research/universities-2027-2028.json",
  "/research/sources.json": "../research/sources.json",
};

class Element {
  constructor(id = "") {
    this.id = id;
    this.value = id === "search" ? "" : id === "sort-filter" ? "status" : "all";
    this.checked = false;
    this.innerHTML = "";
    this._textContent = "";
    this.placeholder = "";
    this.options = Array.from({ length: id === "status-filter" ? 7 : 3 }, () => ({ text: "" }));
    this.listeners = {};
  }
  get textContent() { return this._textContent; }
  set textContent(value) { this._textContent = String(value); }
  addEventListener(type, listener) { this.listeners[type] = listener; }
  dispatch(type) { this.listeners[type]?.({ target: this }); }
}

const elements = new Map();
const getElementById = (id) => {
  if (!elements.has(id)) elements.set(id, new Element(id));
  return elements.get(id);
};
const dataText = [...html.matchAll(/<[^>]*data-en="([^"]*)"[^>]*data-it="([^"]*)"[^>]*>/g)].map((m) => ({
  innerHTML: "",
  attrs: { "data-en": m[1], "data-it": m[2] },
  getAttribute(name) { return this.attrs[name] ?? null; },
}));
const document = {
  documentElement: { lang: "en" },
  getElementById,
  querySelectorAll: () => dataText,
};
const fetch = async (url) => {
  const path = dataFiles[url];
  if (!path) return { ok: false, json: async () => null };
  return { ok: true, json: async () => JSON.parse(await readFile(new URL(path, import.meta.url), "utf8")) };
};

vm.runInNewContext(script, { document, fetch, console, Date, Promise });
await new Promise((resolve) => setTimeout(resolve, 50));

assert.equal(getElementById("stat-universities").textContent, "34", getElementById("program-grid").innerHTML);
assert.equal(getElementById("stat-programs").textContent, "189");
assert.equal(getElementById("stat-confirmed").textContent, "23");
assert.equal(getElementById("stat-deadlines").textContent, "9");
assert.match(getElementById("notice-count").textContent, /^164 /);
assert.match(getElementById("program-count").textContent, /^23 \/ 189 /);
assert.doesNotMatch(getElementById("program-grid").innerHTML, /legacy-001/);
const universityHtml = getElementById("university-grid").innerHTML;
assert.match(universityHtml, /Engineering application windows/);
assert.match(universityHtml, /Official sources conflict/);
assert.match(universityHtml, /International merit scholarships/);
assert.match(universityHtml, /2027\/28 tuition/);
assert.match(universityHtml, /Admissions contact/);
assert.match(universityHtml, /Merit Based Call for Applications/);
assert.match(universityHtml, /The official catalogue shows Data Science MSc coursework taught in 2027\/28 for the 2026\/27 cohort/);
assert.match(universityHtml, /Course Catalogue – Data Science, Big Data \(ICT curriculum\), 2027\/28/);
assert.match(universityHtml, /calendar says dates and deadlines have not yet been finalized/);

const status = getElementById("status-filter");
status.value = "REQUIRES_VERIFICATION";
status.dispatch("change");
getElementById("search").value = "Data Science";
getElementById("search").dispatch("input");
const messinaProgramHtml = getElementById("program-grid").innerHTML;
assert.match(messinaProgramHtml, /Università degli Studi di Messina/);
assert.match(messinaProgramHtml, /2027\/28 program availability/);
assert.match(messinaProgramHtml, /The catalogue confirms second-year courses taught in 2027\/28/);
assert.match(messinaProgramHtml, /Academic-year course offering/);
assert.match(messinaProgramHtml, /university-wide 2027\/28 international application calls/);
assert.match(messinaProgramHtml, /€40 for up to two program applications/);
assert.match(messinaProgramHtml, /English/);
assert.match(messinaProgramHtml, /Universit\u00e0 degli Studi di Catania/);
assert.match(messinaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(messinaProgramHtml, /The official course listing and admission evidence reviewed is from 2026\/27/);
assert.match(messinaProgramHtml, /10 February–17 March 2026 and a \u20ac10 fee per course/);
assert.match(messinaProgramHtml, /The latest official course and English-MSc call evidence located is for 2026\/27/);
assert.match(dataText.find((element) => element.attrs["data-en"]?.includes("Latest official listing"))?.attrs["data-en"] ?? "", /do not confirm 2027–28 availability/);
assert.match(dataText.find((element) => element.attrs["data-it"]?.includes("Ultima scheda ufficiale"))?.attrs["data-it"] ?? "", /non confermano la disponibilità per il 2027–28/);

getElementById("search").value = "Biology for Translational Research and Precision Medicine";
getElementById("search").dispatch("input");
const veronaProgramHtml = getElementById("program-grid").innerHTML;
assert.match(veronaProgramHtml, /Universit\u00e0 degli Studi di Verona/);
assert.match(veronaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(veronaProgramHtml, /Course admissions \(2026\/27\)/);
assert.match(veronaProgramHtml, /Course requirements \(2026\/27\)/);
assert.match(veronaProgramHtml, /Non-EU admission \u2013 prior cycle/);
assert.match(veronaProgramHtml, /Scholarships \(2026\/27\)/);
assert.match(veronaProgramHtml, /2 February\u201331 March 2026/);
assert.match(veronaProgramHtml, /The study plan says year two activates in 2027\/28 for students enrolled in 2026\/27/);
assert.match(veronaProgramHtml, /does not confirm a new 2027\/28 first-year intake/);
assert.match(veronaProgramHtml, /class=\"status pending\"/);
getElementById("search").value = "Applied Mathematics";
getElementById("search").dispatch("input");
const sienaProgramHtml = getElementById("program-grid").innerHTML;
assert.match(sienaProgramHtml, /Universit\u00e0 degli Studi di Siena/);
assert.match(sienaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(sienaProgramHtml, /LM-40/);
assert.match(sienaProgramHtml, /Scholarships \(2026\/27\)/);
assert.match(sienaProgramHtml, /Two different courses within Area D/);
assert.match(sienaProgramHtml, /does not confirm whether Applied Mathematics will admit a new first-year cohort/);
getElementById("search").value = "Università degli Studi di Parma";
getElementById("search").dispatch("input");
const parmaProgramHtml = getElementById("program-grid").innerHTML;
assert.match(parmaProgramHtml, /Università degli Studi di Parma/);
assert.match(parmaProgramHtml, /2027\/28 program availability/);
assert.match(parmaProgramHtml, /Requirements under the 2025 regulations/);
assert.doesNotMatch(parmaProgramHtml, /Course requirements \(2026\/27\)/);
assert.match(parmaProgramHtml, /These are from the 2025-version regulations only/);
assert.match(parmaProgramHtml, /first installment eur: 156/);
getElementById("search").value = "Università degli Studi di Pavia";
getElementById("search").dispatch("input");
const paviaProgramHtml = getElementById("program-grid").innerHTML;
assert.match(paviaProgramHtml, /Universit\u00e0 degli Studi di Pavia/);
assert.match(paviaProgramHtml, /class="status pending"/);
assert.match(paviaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(paviaProgramHtml, /2027\/28 program availability/);
assert.match(paviaProgramHtml, /Course requirements \(2026\/27\)/);
assert.match(paviaProgramHtml, /English requirement \(2026\/27\)/);
assert.match(paviaProgramHtml, /Tuition \(2026\/27\)/);
assert.match(paviaProgramHtml, /Tuition exemptions \(2026\/27\)/);
assert.match(paviaProgramHtml, /12 Nov 2026 – 18 Nov 2026/);
assert.match(paviaProgramHtml, /€35/);
assert.match(paviaProgramHtml, /2027\/28 windows for non-restricted Master’s programs/);
getElementById("search").value = "Università degli Studi di Perugia";
getElementById("search").dispatch("input");
const perugiaProgramHtml = getElementById("program-grid").innerHTML;
assert.match(perugiaProgramHtml, /Universit\u00e0 degli Studi di Perugia/);
assert.equal((perugiaProgramHtml.match(/class="card pending"/g) ?? []).length, 2);
assert.match(perugiaProgramHtml, /Engineering Management/);
assert.match(perugiaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(perugiaProgramHtml, /2027\/28 program availability/);
assert.match(perugiaProgramHtml, /Course requirements \(2026\/27\)/);
assert.match(perugiaProgramHtml, /English requirement \(2026\/27\)/);
assert.match(perugiaProgramHtml, /Admission tests \(2026\/27\)/);
assert.match(perugiaProgramHtml, /Program capacity \(2026\/27\)/);
assert.match(perugiaProgramHtml, /Enrollment timing \(prior guidance\)/);
assert.match(perugiaProgramHtml, /Non-EU admission – prior cycle/);
assert.match(perugiaProgramHtml, /Scholarships \(2026\/27\)/);
assert.match(perugiaProgramHtml, /ISEE max: 28339\.88/);
assert.match(perugiaProgramHtml, /class="status pending"/);
assert.match(getElementById("university-grid").innerHTML, /2027\/28 first-year call or procedure for Engineering Management/);
assert.match(getElementById("university-grid").innerHTML, /segr-studenti\.stranieri@unipg\.it/);
getElementById("search").value = "Università Ca' Foscari Venezia";
getElementById("search").dispatch("input");
const caFoscariProgramHtml = getElementById("program-grid").innerHTML;
assert.match(caFoscariProgramHtml, /Computer Science and Information Technology/);
assert.match(caFoscariProgramHtml, /Data Science curriculum/);
assert.match(caFoscariProgramHtml, /Hospitality Innovation and e-Tourism/);
assert.match(caFoscariProgramHtml, /No separate MSc/);
assert.match(caFoscariProgramHtml, /TOLC-E/);
assert.match(caFoscariProgramHtml, /minimum total cfu: 60/);
assert.equal((caFoscariProgramHtml.match(/class="card pending"/g) ?? []).length, 11);
assert.match(getElementById("university-grid").innerHTML, /applications open in December 2026/);
assert.match(getElementById("university-grid").innerHTML, /welcome@unive\.it/);
getElementById("search").value = "Università di Camerino";
getElementById("search").dispatch("input");
const camerinoProgramHtml = getElementById("program-grid").innerHTML;
assert.equal((camerinoProgramHtml.match(/class="card pending"/g) ?? []).length, 4);
assert.match(camerinoProgramHtml, /Universit\u00e0 di Camerino/);
assert.match(camerinoProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(camerinoProgramHtml, /Computer Science/);
assert.match(camerinoProgramHtml, /Chemistry and Advanced Chemical Methodologies/);
assert.match(camerinoProgramHtml, /Mathematics and Applications/);
assert.match(camerinoProgramHtml, /Physics/);
assert.match(camerinoProgramHtml, /named list contains four curricula, but its later prose says five/);
assert.match(camerinoProgramHtml, /curricula and the course profile lists three with different names/);
assert.match(camerinoProgramHtml, /Official University pages use both Chemistry and Chemistry and Advanced Chemical Methodologies/);
assert.match(camerinoProgramHtml, /physics minimum cfu: 70/);
assert.match(camerinoProgramHtml, /mathematics and informatics minimum cfu: 30/);
assert.match(camerinoProgramHtml, /at least 30 ECTS in Mathematics/);
assert.match(getElementById("university-grid").innerHTML, /welcome@unicam\.it/);
assert.match(getElementById("university-grid").innerHTML, /2026\/27 pre-admission/);
assert.match(getElementById("university-grid").innerHTML, /annual cost eur: 6876/);
assert.match(getElementById("university-grid").innerHTML, /ERDIS Marche/);
assert.match(getElementById("university-grid").innerHTML, /No 2027\/28 application window or deadline was identified/);
getElementById("search").value = "Università degli Studi di Ferrara";
getElementById("search").dispatch("input");
const ferraraProgramHtml = getElementById("program-grid").innerHTML;
assert.equal((ferraraProgramHtml.match(/class="card pending"/g) ?? []).length, 1);
assert.match(ferraraProgramHtml, /Physics/);
assert.match(ferraraProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(ferraraProgramHtml, /Course requirements \(2026\/27\)/);
assert.match(ferraraProgramHtml, /English requirement \(2026\/27\)/);
assert.match(ferraraProgramHtml, /12 January–30 April/);
assert.match(ferraraProgramHtml, /No 2027\/28 Physics application dates were identified/);
assert.match(ferraraProgramHtml, /amount eur: 20/);
assert.match(ferraraProgramHtml, /ER.GO Emilia-Romagna/);
assert.match(ferraraProgramHtml, /manager\.fisica@unife\.it/);
assert.match(getElementById("university-grid").innerHTML, /2026\/27 catalogue confirms the Physics MSc/);
assert.match(getElementById("university-grid").innerHTML, /apply\.unife\.it/);
assert.match(getElementById("university-grid").innerHTML, /No official 2027\/28 application calendar was identified/);
getElementById("search").value = "Insubria";
getElementById("search").dispatch("input");
const insubriaProgramHtml = getElementById("program-grid").innerHTML;
assert.equal((insubriaProgramHtml.match(/class="card pending"/g) ?? []).length, 1);
assert.match(insubriaProgramHtml, /Computer Science/);
assert.match(insubriaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(insubriaProgramHtml, /LM-18/);
assert.match(insubriaProgramHtml, /computer science: minimum credits: 60/);
assert.match(insubriaProgramHtml, /mathematics: minimum credits: 18/);
assert.match(insubriaProgramHtml, /B2 or equivalent/);
assert.match(insubriaProgramHtml, /1 Jul 2026/);
assert.match(insubriaProgramHtml, /30 Oct 2026/);
assert.match(insubriaProgramHtml, /area contribution max eur above 66000/);
assert.match(insubriaProgramHtml, /university merit awards for two year MSc/);
assert.match(insubriaProgramHtml, /Student Web Services \/ Esse3/);
assert.match(insubriaProgramHtml, /No 2027\/28 tuition or contribution rules were identified/);
assert.match(getElementById("university-grid").innerHTML, /2026\/27, including its English MSc profile/);
assert.match(getElementById("university-grid").innerHTML, /contact-center/);
getElementById("search").value = "L'Aquila";
getElementById("search").dispatch("input");
const laquilaProgramHtml = getElementById("program-grid").innerHTML;
assert.equal((laquilaProgramHtml.match(/class="card pending"/g) ?? []).length, 1);
assert.match(laquilaProgramHtml, /Computer Science/);
assert.match(laquilaProgramHtml, /Latest official listing \(2026\/27\)/);
assert.match(laquilaProgramHtml, /LM-18/);
assert.match(laquilaProgramHtml, /minimum credits: 48/);
assert.match(laquilaProgramHtml, /minimum credits: 12/);
assert.match(laquilaProgramHtml, /Written and oral English at B2/);
assert.match(laquilaProgramHtml, /25 Feb 2026/);
assert.match(laquilaProgramHtml, /13:00 Italy time/);
assert.match(laquilaProgramHtml, /fixed registration payment eur: 156/);
assert.match(laquilaProgramHtml, /No 2027\/28 Computer Science application window was found/);
assert.match(laquilaProgramHtml, /travel and installation/);
assert.match(laquilaProgramHtml, /eligible refugee student/i);
assert.match(getElementById("university-grid").innerHTML, /Official 2026\/27 Computer Science course, regulation and international selection sources/);
assert.match(getElementById("university-grid").innerHTML, /international\.students@univaq\.it/);
assert.match(getElementById("university-grid").innerHTML, /No 2027\/28 Computer Science call or application dates were identified/);
getElementById("search").value = "";
getElementById("search").dispatch("input");

status.value = "CONFLICTING_SOURCES";
status.dispatch("change");
const conflictHtml = getElementById("program-grid").innerHTML;
assert.match(conflictHtml, /Cyber Security \(CSES\)/);
assert.doesNotMatch(conflictHtml, /\[object Object\]/);
assert.match(conflictHtml, /31 Jan 2027/);
assert.equal((conflictHtml.match(/class="status conflicting"/g) ?? []).length, 10);

status.value = "NOT_YET_PUBLISHED";
status.dispatch("change");
assert.match(getElementById("program-grid").innerHTML, /Hydrogen Systems and Enabling Technologies/);
assert.doesNotMatch(getElementById("program-grid").innerHTML, /Cyber Security \(CSES\)/);

status.value = "NOT_APPLICABLE";
status.dispatch("change");
assert.match(getElementById("program-grid").innerHTML, /Maritime Science and Technology/);
assert.match(getElementById("program-grid").innerHTML, /will not be offered in 2027–28/);
assert.match(getElementById("program-grid").innerHTML, /Data Science for Management/);
assert.match(getElementById("program-grid").innerHTML, /Replaced by Data Science from AY 2022\/23/);
assert.equal((getElementById("program-grid").innerHTML.match(/<article class="card/g) ?? []).length, 2);

status.value = "all";
getElementById("search").value = "Hydrogen";
getElementById("search").dispatch("input");
assert.match(getElementById("program-grid").innerHTML, /Hydrogen Systems and Enabling Technologies/);
assert.equal((getElementById("program-grid").innerHTML.match(/<article class="card/g) ?? []).length, 1);

getElementById("search").value = "";
getElementById("language-toggle").dispatch("click");
assert.equal(document.documentElement.lang, "it");
assert.match(getElementById("status-chip").textContent, /campi supportati da fonti ufficiali/);
assert.match(getElementById("language-toggle").textContent, /EN/);
assert.ok(dataText.some((element) => element.innerHTML.includes("Le etichette ‘Tag del tracker precedente’")));

console.log("TRACKER UI TESTS PASSED");
