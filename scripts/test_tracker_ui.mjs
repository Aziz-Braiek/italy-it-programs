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
assert.equal(getElementById("stat-programs").textContent, "187");
assert.equal(getElementById("stat-confirmed").textContent, "23");
assert.equal(getElementById("stat-deadlines").textContent, "8");
assert.match(getElementById("notice-count").textContent, /^163 /);
assert.match(getElementById("program-count").textContent, /^23 \/ 187 /);
assert.doesNotMatch(getElementById("program-grid").innerHTML, /legacy-001/);

const status = getElementById("status-filter");
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
assert.equal((getElementById("program-grid").innerHTML.match(/<article class="card/g) ?? []).length, 1);

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

console.log("TRACKER UI TESTS PASSED");
