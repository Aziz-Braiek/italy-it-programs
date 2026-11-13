(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.ItalyProfileEngine = api;
})(globalThis, function () {
  "use strict";
  const CURRENT = "2027/28 confirmed";
  const unknown = (reason = "No confirmed value for this selected route; another route is never substituted.") => ({ value: "Not confirmed", cycle_status: "not confirmed", source_urls: [], verified_date: null, reason });
  const current = (fact) => fact?.cycle_status === CURRENT && ["2027/28", "2027-2028", "2027/2028", "2027–2029"].includes(fact.academic_cycle) && fact.value && fact.value !== "Not confirmed";
  function normalize(value = {}) {
    const result = {
      category: ["eu-eea-ch", "non-eu-abroad", "non-eu-in-italy", "italian-qualification"].includes(value.category) ? value.category : "",
      qualification: ["italy", "eu", "non-eu"].includes(value.qualification) ? value.qualification : "",
      degree: ["bsc", "msc", "single-cycle", "professional-master"].includes(value.degree) ? value.degree : ""
    };
    result.invalid = result.category === "italian-qualification" && result.qualification && result.qualification !== "italy";
    if (result.category === "italian-qualification" && !result.invalid) result.qualification = "italy";
    return result;
  }
  const active = (profile) => Boolean(profile.category || profile.qualification || profile.degree);
  const matches = (conditions = {}, value) => {
    const p = normalize(value);
    return !p.invalid && Object.entries(conditions).every(([key, allowed]) => p[key] && allowed.includes(p[key]));
  };
  function factFor(route, decisions, programId) {
    let fact = route.fact;
    if (!fact && route.fact_ref) {
      const [owner, id, key] = route.fact_ref.split(":");
      const p = decisions.programs?.[id];
      if (owner === "program") {
        fact = p?.facts?.[key];
        if (fact?.university_policy) fact = decisions.universities?.[p.university_id]?.policies?.[fact.university_policy];
      } else if (owner === "university") fact = decisions.universities?.[id]?.[key];
      else if (owner === "policy") fact = decisions.universities?.[id]?.policies?.[key];
      else if (owner === "scholarship") {
        const offers = (decisions.universities?.[p?.university_id]?.scholarships || []).filter((offer) => !offer.program_ids || offer.program_ids.includes(id));
        const supported = offers.filter(current);
        fact = supported.length ? { ...supported[0], value: supported.map((offer) => offer.value).join(" | "), source_urls: [...new Set(supported.flatMap((offer) => offer.source_urls || []))], missing_components: [...new Set(supported.flatMap((offer) => offer.missing_components || []))] } : unknown();
      }
    }
    if (fact?.program_ids && !fact.program_ids.includes(programId)) return unknown("The university guidance is scoped to another programme.");
    return { ...(fact || unknown()), ...(route.overrides || {}), covered_scope: route.scope };
  }
  function routesFor(data, id, field) {
    const p = data.programs?.[id] || {};
    const ids = p.routes?.[field] ?? data.universities?.[p.university_id]?.routes?.[field] ?? [];
    const pool = field === "tuition" ? data.tuition_rules : data.routes;
    return ids.map((rid) => pool?.[rid]).filter((route) => route && (!route.program_ids || route.program_ids.includes(id)));
  }
  function select(data, decisions, id, field, profile) {
    if (normalize(profile).invalid) return unknown("An Italian-qualification profile cannot also specify a qualification obtained outside Italy. Adjust either input.");
    const candidates = routesFor(data, id, field).map((route) => ({ route, fact: field === "tuition" ? route : factFor(route, decisions, id) }))
      .filter(({ route, fact }) => matches(route.conditions, profile) && current(fact));
    if (!candidates.length) return unknown();
    const specificity = Math.max(...candidates.map(({ route }) => Object.keys(route.conditions || {}).length));
    const selected = candidates.filter(({ route }) => Object.keys(route.conditions || {}).length === specificity);
    if (selected.length !== 1) return unknown("Multiple applicable official routes require clarification; no arbitrary route is selected.");
    const { route, fact } = selected[0];
    if (route.partial_profile_coverage) return { ...unknown(`The profile does not resolve all published conditions. ${route.coverage_reason || route.scope}`), checked_urls: fact.source_urls || [], checked_at: fact.verified_date };
    return { ...fact, covered_scope: route.scope, route_id: route.id };
  }
  function tuitionState(data, decisions, id, profile) {
    const facts = active(profile || {}) ? [select(data, decisions, id, "tuition", profile)] : routesFor(data, id, "tuition");
    const supported = facts.filter(current);
    if (supported.some((r) => ["fixed", "band"].includes(r.type) && !r.partial_profile_coverage)) return "documented";
    return supported.some((r) => r.type === "rule-only") ? "rule-only" : "pending";
  }
  const binaryState = (f) => current(f) && ["yes", "no"].includes(f.answer) ? f.answer : "not confirmed";
  function futureEvents(fact, today) {
    if (!current(fact)) return [];
    const seen = new Set();
    return (fact.events || []).filter((e) => /^\d{4}-\d{2}-\d{2}$/.test(e.date) && e.date >= today)
      .filter((e) => { const key = `${e.date}|${e.eligible || ""}`; if (seen.has(key)) return false; seen.add(key); return true; })
      .sort((a, b) => a.date.localeCompare(b.date));
  }
  function toParams(value) {
    const p = normalize(value);
    const params = new URLSearchParams();
    for (const [key, param] of [["category", "applicant"], ["qualification", "qualification"], ["degree", "degree-sought"]]) if (p[key]) params.set(param, p[key]);
    return params;
  }
  function fromParams(params) {
    return normalize({ category: params.get("applicant"), qualification: params.get("qualification"), degree: params.get("degree-sought") });
  }
  return { CURRENT, unknown, current, normalize, active, matches, factFor, routesFor, select, tuitionState, binaryState, futureEvents, toParams, fromParams };
});
