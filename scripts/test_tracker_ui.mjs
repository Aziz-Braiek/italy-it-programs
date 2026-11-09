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
assert.equal(getElementById("stat-programs").textContent, "188");
assert.equal(getElementById("stat-confirmed").textContent, "23");
assert.equal(getElementById("stat-deadlines").textContent, "8");
assert.match(getElementById("notice-count").textContent, /^163 /);
assert.match(getElementById("program-count").textContent, /^23 \/ 188 /);
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
getElementById("search").value = "";
getElementById("search").dispatch("input");

status.value = "CONFLICTING_SOURCES";
status.dispatch("change");
const conflictHtml = getElementById("program-grid").innerHTML;
assert.match(conflictHtml, /Cyber Security \(CSES\)/);
assert.doesNotMatch(conflictHtml, /\[object Object\]/);
assert.match(conflictHtml, /31 Jan 2027/);
assert.equal((conflictHtml.match(/class="status conflicting"/g) ?? []).length, 7);

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
