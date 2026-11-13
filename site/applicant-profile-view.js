(function () {
  "use strict";
  const E = window.ItalyProfileEngine;
  const json = document.querySelector("#applicant-profile-data");
  if (!E || !json) return;
  const data = JSON.parse(json.textContent);
  const decisions = JSON.parse(document.querySelector("#decision-support-data")?.textContent || "{}");
  const controls = { category: document.querySelector("#profile-category"), degree: document.querySelector("#profile-degree"), qualification: document.querySelector("#profile-qualification") };
  const hosts = [...document.querySelectorAll("[data-profile-host]")];
  const originals = new Map(hosts.map((host) => [host, Object.fromEntries(["deadline", "deadlines", "tuition", "scholarship", "admissionTest", "englishCertificate"].map((key) => [key, host.dataset[key] || ""]))]));
  const hrefs = new WeakMap();
  const storageKey = "itu-tracker-applicant-profile-v1";
  const names = { deadline: "Deadline", tuition: "Tuition", english_requirement: "English requirement", documents: "Document path", prerequisites: "Prerequisites", minimum_grade: "Minimum grade", admission_test: "Admission test", selection_method: "Selection method", universitaly: "University Universitaly deadline", national_universitaly: "National visa pre-enrolment requirement" };
  const primary = ["deadline", "tuition", "english_requirement", "documents"];
  let profile;
  const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
  const today = () => new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Rome", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
  function readProfile(useStorage) {
    const params = new URLSearchParams(location.search);
    if (["applicant", "qualification", "degree-sought"].some((key) => params.has(key))) return E.fromParams(params);
    if (useStorage) { try { return E.normalize(JSON.parse(localStorage.getItem(storageKey) || "{}")); } catch { /* Storage is optional. */ } }
    return E.normalize({});
  }
  function save() { try { localStorage.setItem(storageKey, JSON.stringify(profile)); } catch { /* Private mode may disable storage. */ } }
  function label() {
    const parts = [data.categories[profile.category], data.qualifications[profile.qualification] ? `qualification: ${data.qualifications[profile.qualification]}` : "", data.degrees[profile.degree]].filter(Boolean);
    return parts.join(" · ") || "no applicant profile";
  }
  const selected = (id, field) => E.select(data, decisions, id, field, profile);
  const deadlines = (id) => E.futureEvents(selected(id, "deadline"), today());
  function paramsInto(params) {
    ["applicant", "qualification", "degree-sought"].forEach((key) => params.delete(key));
    E.toParams(profile).forEach((value, key) => params.set(key, value));
    return params;
  }
  function urlFor(href) {
    const url = new URL(href, location.origin);
    paramsInto(url.searchParams);
    return url.href;
  }
  function syncUrl() {
    const url = new URL(location.href);
    paramsInto(url.searchParams);
    history.replaceState(null, "", url.pathname + url.search + url.hash);
  }
  function money(value) { return `EUR ${Number(value).toLocaleString("en-GB", { maximumFractionDigits: 2 })}`; }
  function fieldHtml(field, fact, compact = false, historical = false) {
    const supported = E.current(fact);
    const partial = supported && fact.missing_components?.length;
    let text = fact.short_value || fact.value || "Not confirmed";
    if (supported && field === "deadline") {
      const events = E.futureEvents(fact, today());
      text = events.length ? `${events[0].date}${events[0].time && events[0].time !== "Not confirmed" ? ` · ${events[0].time}` : ""}` : "No confirmed future deadline for this route";
      if (!compact && events.length > 1) text += `; later rounds: ${events.slice(1).map((event) => event.date).join(", ")}`;
    } else if (supported && field === "tuition") {
      text = fact.type === "fixed" ? `${money(fact.amount)} / academic year` : fact.type === "band" ? `${money(fact.minimum)}–${money(fact.maximum)} / academic year` : "Rule only — full annual amount Not confirmed";
      if (!compact && fact.calculation_basis) text += `. ${fact.calculation_basis}`;
      if (!compact && fact.known_components?.length) text += ". Published components: " + fact.known_components.map((c) => `${c.name}: ${money(c.amount)}`).join("; ");
    } else if (compact && field === "documents" && supported) text = partial ? "Application path partly confirmed — see full path" : "Published application document path — see programme page";
    if (!supported && !historical) text = "Not confirmed";
    const cycle = !supported ? historical ? `${fact.cycle_status || "not confirmed"}${fact.academic_cycle ? ` · ${fact.academic_cycle}` : ""}` : "not confirmed" : partial ? "Partly confirmed · 2027/28" : "2027/28 confirmed";
    const sourceUrls = fact.source_urls || fact.checked_urls || [];
    const links = sourceUrls.slice(0, compact ? 1 : sourceUrls.length).map((url) => `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${supported || historical ? "Official source" : "Checked page"} ↗</a>`).join(" ");
    const missing = fact.missing_components?.length ? `<small class="decision-missing">Not confirmed: ${esc(fact.missing_components.join("; "))}</small>` : "";
    const scope = supported || historical ? `<small>Covered: ${esc(fact.covered_scope || "Only the route stated by this source")}</small>` : !compact && fact.reason ? `<small>${esc(fact.reason)}</small>` : "";
    return `<div class="decision-field ${partial ? "decision-partial" : supported ? "decision-current" : historical ? "decision-previous" : "decision-unknown"}"><dt>${esc(names[field])}${!supported && !historical ? ` for ${esc(label())}` : ""}</dt><dd><span class="decision-value">${esc(text)}</span><small class="decision-cycle">${esc(cycle)}</small>${scope}${missing}<small>${fact.verified_date ? `Verified: ${esc(fact.verified_date)}` : "Verified date: Not confirmed"} ${links}</small></dd></div>`;
  }
  function renderAlternatives(host, id) {
    const selectedIds = new Set(primary.map((field) => selected(id, field).route_id));
    let html = '<p>These alternatives and earlier observations are not used for your selected profile.</p><dl class="profile-fields">';
    for (const field of primary) {
      for (const route of E.routesFor(data, id, field)) {
        if (selectedIds.has(route.id)) continue;
        const f = field === "tuition" ? route : E.factFor(route, decisions, id);
        html += fieldHtml(field, { ...f, covered_scope: route.scope }, true, !E.current(f));
      }
    }
    host.querySelector(".profile-alternatives").innerHTML = html + '</dl><p>Full programme record and earlier evidence:</p>';
  }
  function apply() {
    Object.entries(controls).forEach(([key, element]) => { if (element) element.value = profile[key]; });
    const isActive = E.active(profile);
    const status = document.querySelector("#profile-status");
    if (status) status.textContent = profile.invalid ? "The category says Italian qualification, but the origin says outside Italy. Adjust either input; no route will be substituted." : isActive ? `Showing only verified information for: ${label()}. Unconfirmed combinations stay explicit.` : "Choose only what you know. No account; saved in this browser. The selected categories also appear in the shareable URL.";
    for (const host of hosts) {
      const id = host.dataset.profileHost;
      const detailed = host.dataset.profileDetailed === "true";
      const view = host.querySelector(".profile-current");
      const base = host.querySelector(".profile-base-content");
      const other = host.querySelector(".profile-other-routes");
      host.classList.toggle("has-profile", isActive);
      view.hidden = !isActive;
      other.hidden = !isActive;
      host.dataset.profileDegreeHidden = String(Boolean(profile.degree && data.programs[id]?.degree_group !== profile.degree));
      if (!isActive) {
        host.insertBefore(base, other);
        Object.assign(host.dataset, originals.get(host));
        continue;
      }
      other.appendChild(base);
      const events = deadlines(id);
      host.dataset.deadlines = JSON.stringify(events);
      host.dataset.deadline = events[0]?.date || "";
      host.dataset.tuition = E.tuitionState(data, decisions, id, profile);
      host.dataset.englishCertificate = E.binaryState(selected(id, "english_requirement"));
      host.dataset.admissionTest = E.binaryState(selected(id, "admission_test"));
      host.dataset.scholarship = E.current(selected(id, "scholarships")) ? "documented" : "pending";
      view.id = `profile-route-${id}`;
      const fields = detailed ? [...primary, "prerequisites", "minimum_grade", "admission_test", "selection_method", "universitaly"] : primary;
      const missing = [];
      let html = `<p class="profile-route-label">Your route: ${esc(label())}</p>`;
      if (detailed && host.dataset.profileDegreeHidden === "true") html += '<p>The programme’s recorded degree type does not match your requested degree level.</p>';
      html += `<dl class="${detailed ? "profile-fields" : "decision-summary"}">`;
      for (const field of fields) {
        const f = selected(id, field);
        if (!detailed && !E.current(f)) missing.push(names[field].toLowerCase());
        else html += fieldHtml(field, f, !detailed);
      }
      html += '</dl>';
      if (missing.length) html += `<p class="decision-unknown-summary">Not confirmed for ${esc(label())}: ${esc(missing.join(", "))}. <a href="${esc(urlFor(`/programs/${id}/#profile-route-${id}`))}">See programme page</a></p>`;
      if (detailed && profile.category === "non-eu-abroad") html += `<details class="national-rule"><summary>National visa pre-enrolment rule</summary><dl>${fieldHtml("national_universitaly", data.national_rules.universitaly_requirement)}</dl><p>This national requirement is separate from the university-specific deadline above and depends on whether the applicant requires a visa.</p></details>`;
      view.innerHTML = html;
      renderAlternatives(host, id);
    }
    document.querySelectorAll('a[href]').forEach((a) => {
      if (!hrefs.has(a)) hrefs.set(a, a.getAttribute("href"));
      const original = hrefs.get(a);
      const url = new URL(original, location.href);
      if (url.origin === location.origin && (url.pathname === "/" || url.pathname.startsWith("/programs/") || url.pathname.startsWith("/universities/"))) a.href = urlFor(original);
    });
    save();
  }
  function changed() { apply(); syncUrl(); window.dispatchEvent(new CustomEvent("itu-profile-change")); }
  profile = readProfile(true);
  Object.entries(controls).forEach(([, element]) => element?.addEventListener("change", () => { profile = E.normalize(Object.fromEntries(Object.entries(controls).map(([k, e]) => [k, e?.value || ""]))); changed(); }));
  document.querySelector("#clear-profile")?.addEventListener("click", () => { profile = E.normalize({}); changed(); });
  const selector = document.querySelector("#applicant-profile-selector");
  if (selector && matchMedia("(max-width: 680px)").matches) selector.open = false;
  window.addEventListener("popstate", () => { profile = readProfile(false); apply(); window.dispatchEvent(new CustomEvent("itu-profile-change")); });
  window.ItalyProfileView = { get profile() { return profile; }, get active() { return E.active(profile); }, label, selected, deadlines, paramsInto, urlFor, data, decisions };
  apply();
})();
