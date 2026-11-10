(function () {
  "use strict";

  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const PAGE_SIZE = 18;
  const storageKeys = { favorites: "itu-tracker-favorites-v2", language: "itu-tracker-language-v2" };
  let pageNumber = 1;
  let compareIds = [];
  let favoriteIds = loadJson(storageKeys.favorites, []);
  let showFavorites = false;
  let language = loadJson(storageKeys.language, "en");

  const copy = {
    en: {
      navPrograms: "Programs", navUniversities: "Universities", navGuide: "Application guide", navAbout: "About",
      languageLabel: "Change language to Italian", sectionPrograms: "Programs", sectionUniversities: "Universities in this tracker",
      search: "Search", degree: "Degree level", university: "University", city: "City or region", language: "Teaching language",
      field: "Field of study", status: "Program status", dates: "Application dates", tuition: "Tuition information",
      scholarships: "Scholarship information", sort: "Sort by", pending: "Show programs awaiting confirmation",
      save: "Save program", saved: "Saved", compare: "Compare", available: "Available for 2027/28",
      waiting: "Awaiting 2027/28 confirmation", unavailable: "Not offered for 2027/28",
      latest: "Latest program review", notice: "Many 2027/28 calls are still being published",
      guide: "Application guide", footerExplore: "Explore", footerAbout: "About this site",
      csv: "Download shortlist CSV", ics: "Add confirmed deadlines to calendar", empty: "No programs match these filters.",
      prev: "Previous", next: "Next", include: "Show programs awaiting confirmation",
      confirmedStatus: "Available for 2027/28", pendingStatus: "Awaiting 2027/28 confirmation", unavailableStatus: "Not offered for 2027/28",
      universityConfirmed: "2027/28 information found", universityPending: "Some 2027/28 details not announced"
    },
    it: {
      navPrograms: "Corsi", navUniversities: "Università", navGuide: "Guida alle candidature", navAbout: "Informazioni",
      languageLabel: "Passa all’interfaccia in inglese", sectionPrograms: "Corsi", sectionUniversities: "Università nel tracker",
      search: "Cerca", degree: "Livello di laurea", university: "Università", city: "Città o regione", language: "Lingua di insegnamento",
      field: "Area di studio", status: "Stato del corso", dates: "Date di candidatura", tuition: "Informazioni sulle tasse",
      scholarships: "Informazioni sulle borse", sort: "Ordina per", pending: "Mostra i corsi in attesa di conferma",
      save: "Salva corso", saved: "Salvato", compare: "Confronta", available: "Disponibile per il 2027/28",
      waiting: "Conferma 2027/28 in attesa", unavailable: "Non offerto nel 2027/28",
      latest: "Ultimo controllo dei corsi", notice: "Molti bandi 2027/28 sono ancora in pubblicazione",
      guide: "Guida alle candidature", footerExplore: "Esplora", footerAbout: "Informazioni sul sito",
      csv: "Scarica la selezione CSV", ics: "Aggiungi le scadenze confermate al calendario", empty: "Nessun corso corrisponde ai filtri.",
      prev: "Precedente", next: "Successiva", include: "Mostra i corsi in attesa di conferma",
      confirmedStatus: "Disponibile per il 2027/28", pendingStatus: "Conferma 2027/28 in attesa", unavailableStatus: "Non offerto nel 2027/28",
      universityConfirmed: "Informazioni 2027/28 trovate", universityPending: "Alcuni dati 2027/28 non ancora pubblicati"
    }
  };

  function loadJson(key, fallback) {
    try {
      const parsed = JSON.parse(localStorage.getItem(key) || "null");
      return parsed == null ? fallback : parsed;
    } catch (_error) {
      return fallback;
    }
  }

  function saveJson(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (_error) { /* Private mode can disable storage. */ }
  }

  function announce(message) {
    const region = $("#site-announcer");
    if (region) region.textContent = message;
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[char]);
  }

  function applyLanguage() {
    const dictionary = copy[language] || copy.en;
    $$('[data-i18n]').forEach((element) => {
      const value = dictionary[element.dataset.i18n];
      if (value) element.textContent = value;
    });
    const filterLabels = { search: "search", "filter-level": "degree", "filter-university": "university", "filter-city": "city", "filter-language": "language", "filter-field": "field", "filter-status": "status", "filter-deadline": "dates", "filter-tuition": "tuition", "filter-scholarship": "scholarships", "sort-by": "sort" };
    Object.entries(filterLabels).forEach(([id, key]) => {
      const label = document.getElementById(id)?.closest("label");
      const span = label?.querySelector("span");
      if (span) span.textContent = dictionary[key];
    });
    const panelSummary = $("#filter-panel > summary");
    if (panelSummary) panelSummary.textContent = language === "it" ? "Filtra e ordina i corsi" : "Filter and sort programs";
    const programsHeading = $("#programs .section-heading h2");
    if (programsHeading) programsHeading.textContent = dictionary.sectionPrograms;
    const universitiesHeading = $("#universities .section-heading h2");
    if (universitiesHeading) universitiesHeading.textContent = dictionary.sectionUniversities;
    const noticeHeading = $("#notice-title");
    if (noticeHeading) noticeHeading.textContent = dictionary.notice;
    const pendingLabel = $("#include-pending")?.closest("label")?.querySelector("span");
    if (pendingLabel) pendingLabel.textContent = dictionary.pending;
    const exportCsvButton = $("#export-csv");
    if (exportCsvButton) exportCsvButton.textContent = dictionary.csv;
    const exportIcsButton = $("#export-ics");
    if (exportIcsButton) exportIcsButton.textContent = dictionary.ics;
    const previousPageButton = $("#page-previous");
    if (previousPageButton) previousPageButton.textContent = dictionary.prev;
    const nextPageButton = $("#page-next");
    if (nextPageButton) nextPageButton.textContent = dictionary.next;
    $$('[data-status-copy]').forEach((element) => {
      const key = ({ CONFIRMED: "confirmedStatus", REQUIRES_VERIFICATION: "pendingStatus", NOT_APPLICABLE: "unavailableStatus", NOT_YET_PUBLISHED: "universityPending", UNAVAILABLE: "unavailableStatus", CONFLICTING_SOURCES: "pendingStatus", UNIVERSITY_CONFIRMED: "universityConfirmed", UNIVERSITY_PENDING: "universityPending" })[element.dataset.statusCopy];
      if (key) element.textContent = dictionary[key];
    });
    const button = $("#language-toggle");
    if (button) {
      button.textContent = language === "en" ? "IT" : "EN";
      button.setAttribute("aria-label", dictionary.languageLabel);
      button.setAttribute("aria-pressed", String(language === "it"));
    }
    document.documentElement.lang = language;
    $$(".favorite-button").forEach(updateFavoriteButton);
    $$(".compare-button").forEach(updateCompareButton);
  }

  const languageToggle = $("#language-toggle");
  if (languageToggle) {
    languageToggle.addEventListener("click", () => {
      language = language === "en" ? "it" : "en";
      saveJson(storageKeys.language, language);
      applyLanguage();
      announce(language === "it" ? "Interfaccia in italiano. I nomi dei corsi e i testi delle fonti restano nella lingua originale." : "English interface. Program names and source text remain in their original language.");
    });
  }

  const cards = $$("[data-program-card]");
  const programById = new Map(cards.map((card) => [card.dataset.programId, card]));
  const filters = {
    query: $("#search"), level: $("#filter-level"), university: $("#filter-university"), city: $("#filter-city"),
    language: $("#filter-language"), field: $("#filter-field"), status: $("#filter-status"), deadline: $("#filter-deadline"),
    tuition: $("#filter-tuition"), scholarship: $("#filter-scholarship"), sort: $("#sort-by"), pending: $("#include-pending")
  };

  function readFiltersFromUrl() {
    if (!cards.length) return;
    const params = new URLSearchParams(location.search);
    const names = { q: "query", level: "level", university: "university", city: "city", language: "language", field: "field", status: "status", deadline: "deadline", tuition: "tuition", scholarship: "scholarship", sort: "sort" };
    Object.entries(names).forEach(([param, key]) => {
      const control = filters[key];
      const value = params.get(param);
      if (control && value && Array.from(control.options || []).some((option) => option.value.toLowerCase() === value.toLowerCase())) control.value = value;
      else if (control && value && control.tagName === "INPUT") control.value = value;
    });
    filters.pending.checked = params.get("pending") === "1";
    showFavorites = params.get("favorites") === "1";
    const favoritesButton = $("#show-favorites");
    if (favoritesButton) favoritesButton.setAttribute("aria-pressed", String(showFavorites));
  }

  function queryGroup(value) {
    const normalized = (value || "").trim().toLowerCase();
    if (!normalized) return "Unknown";
    const english = normalized.includes("english");
    const italian = normalized.includes("italian");
    if (english && italian) return "Mixed";
    if (english) return "English";
    if (italian) return "Italian";
    return "Unknown";
  }

  function matches(card) {
    const q = (filters.query?.value || "").trim().toLowerCase();
    const level = (filters.level?.value || "").toLowerCase();
    const university = filters.university?.value || "";
    const city = (filters.city?.value || "").toLowerCase();
    const lang = filters.language?.value || "";
    const field = (filters.field?.value || "").trim().toLowerCase();
    const status = filters.status?.value || "";
    const deadline = filters.deadline?.value || "";
    const tuition = filters.tuition?.value || "";
    const scholarship = filters.scholarship?.value || "";
    const pendingIncluded = filters.pending?.checked || showFavorites;
    const statusValue = card.dataset.status;
    const favorite = favoriteIds.includes(card.dataset.programId);
    if (!pendingIncluded && statusValue !== "CONFIRMED") return false;
    if (showFavorites && !favorite) return false;
    if (q && !card.dataset.search.includes(q)) return false;
      if (level && card.dataset.level.toLowerCase() !== level) return false;
    if (university && card.dataset.university !== university) return false;
    if (city && !`${card.dataset.city} ${card.dataset.region}`.toLowerCase().includes(city)) return false;
    if (lang && queryGroup(card.dataset.language) !== lang) return false;
    if (field && !card.dataset.field.toLowerCase().includes(field)) return false;
    if (status && statusValue !== status) return false;
    if (deadline === "known" && !card.dataset.deadline) return false;
    if (deadline === "pending" && card.dataset.deadline) return false;
    if (tuition && card.dataset.tuition !== tuition) return false;
    if (scholarship && card.dataset.scholarship !== scholarship) return false;
    return true;
  }

  function sortCards(result) {
    const sort = filters.sort?.value || "recommended";
    const getName = (card) => $("h3", card)?.textContent?.trim() || "";
    const getUniversity = (card) => card.querySelector(".card-title-row .eyebrow")?.textContent?.split("·")[0]?.trim() || "";
    result.sort((a, b) => {
      if (sort === "deadline") {
        const ad = a.dataset.deadline || "9999-12-31";
        const bd = b.dataset.deadline || "9999-12-31";
        return ad.localeCompare(bd) || getUniversity(a).localeCompare(getUniversity(b)) || getName(a).localeCompare(getName(b));
      }
      if (sort === "university") return getUniversity(a).localeCompare(getUniversity(b)) || getName(a).localeCompare(getName(b));
      if (sort === "program") return getName(a).localeCompare(getName(b));
      return (a.dataset.status === "CONFIRMED" ? 0 : 1) - (b.dataset.status === "CONFIRMED" ? 0 : 1) || getUniversity(a).localeCompare(getUniversity(b)) || getName(a).localeCompare(getName(b));
    });
    return result;
  }

  function updateUrl() {
    if (!cards.length) return;
    const params = new URLSearchParams();
    const controls = { q: filters.query, level: filters.level, university: filters.university, city: filters.city, language: filters.language, field: filters.field, status: filters.status, deadline: filters.deadline, tuition: filters.tuition, scholarship: filters.scholarship, sort: filters.sort };
    Object.entries(controls).forEach(([param, control]) => {
      if (control?.value) params.set(param, control.value);
    });
    if (filters.pending?.checked) params.set("pending", "1");
    if (showFavorites) params.set("favorites", "1");
    const query = params.toString();
    history.replaceState(null, "", location.pathname + (query ? `?${query}` : "") + location.hash);
  }

  function renderResults() {
    if (!cards.length) return;
    let result = sortCards(cards.filter(matches));
    const count = result.length;
    const pages = Math.max(1, Math.ceil(count / PAGE_SIZE));
    pageNumber = Math.min(Math.max(pageNumber, 1), pages);
    const start = (pageNumber - 1) * PAGE_SIZE;
    const visible = new Set(result.slice(start, start + PAGE_SIZE));
    const grid = $("#program-grid");
    if (grid) result.forEach((card) => grid.appendChild(card));
    cards.forEach((card) => { card.hidden = !visible.has(card); });
    const countElement = $("#result-count");
    if (countElement) {
      const pending = filters.pending.checked || showFavorites ? "including pending records" : "showing confirmed records only";
      countElement.textContent = `${count} ${count === 1 ? "program" : "programs"} match${count === 1 ? "es" : ""} · ${pending}.`;
    }
    const pageSummary = $("#page-summary");
    if (pageSummary) pageSummary.textContent = count ? `Page ${pageNumber} of ${pages}` : "No results";
    const previous = $("#page-previous");
    const next = $("#page-next");
    if (previous) previous.disabled = pageNumber <= 1;
    if (next) next.disabled = pageNumber >= pages;
    const pagination = $("#pagination");
    if (pagination) pagination.hidden = count <= PAGE_SIZE;
    updateUrl();
  }

  readFiltersFromUrl();
  const filterPanel = $("#filter-panel");
  if (filterPanel && window.matchMedia("(max-width: 680px)").matches) filterPanel.open = false;
  Object.values(filters).forEach((control) => {
    if (!control) return;
    control.addEventListener(control.type === "search" || control.type === "text" ? "input" : "change", () => {
      pageNumber = 1;
      renderResults();
    });
  });
  $("#clear-filters")?.addEventListener("click", () => {
    Object.values(filters).forEach((control) => { if (control) control.value = ""; });
    if (filters.pending) filters.pending.checked = false;
    showFavorites = false;
    $("#show-favorites")?.setAttribute("aria-pressed", "false");
    pageNumber = 1;
    renderResults();
    announce("Filters cleared.");
  });
  $("#show-favorites")?.addEventListener("click", (event) => {
    showFavorites = !showFavorites;
    event.currentTarget.setAttribute("aria-pressed", String(showFavorites));
    pageNumber = 1;
    renderResults();
    announce(showFavorites ? `${favoriteIds.length} saved programs shown.` : "Saved-program filter cleared.");
  });
  $("#page-previous")?.addEventListener("click", () => { pageNumber -= 1; renderResults(); $("#program-grid")?.scrollIntoView({ behavior: "smooth", block: "start" }); });
  $("#page-next")?.addEventListener("click", () => { pageNumber += 1; renderResults(); $("#program-grid")?.scrollIntoView({ behavior: "smooth", block: "start" }); });

  function updateFavoriteButton(button) {
    const id = button.dataset.favorite;
    const isSaved = favoriteIds.includes(id);
    const t = copy[language] || copy.en;
    button.textContent = isSaved ? t.saved : t.save;
    button.setAttribute("aria-pressed", String(isSaved));
  }

  function updateCompareButton(button) {
    const t = copy[language] || copy.en;
    const selected = compareIds.includes(button.dataset.compare);
    button.textContent = selected ? (language === "it" ? "Rimuovi" : "Remove") : t.compare;
    button.setAttribute("aria-pressed", String(selected));
  }

  function syncActionButtons() {
    $$(".favorite-button").forEach(updateFavoriteButton);
    $$(".compare-button").forEach(updateCompareButton);
  }

  document.addEventListener("click", (event) => {
    const favoriteButton = event.target.closest("[data-favorite]");
    if (favoriteButton) {
      const id = favoriteButton.dataset.favorite;
      favoriteIds = favoriteIds.includes(id) ? favoriteIds.filter((item) => item !== id) : [...favoriteIds, id];
      saveJson(storageKeys.favorites, favoriteIds);
      syncActionButtons();
      renderResults();
      announce(favoriteIds.includes(id) ? "Program saved on this device." : "Program removed from saved programs.");
      return;
    }
    const compareButton = event.target.closest("[data-compare]");
    if (compareButton) {
      const id = compareButton.dataset.compare;
      if (compareIds.includes(id)) compareIds = compareIds.filter((item) => item !== id);
      else if (compareIds.length < 3) compareIds.push(id);
      else { announce("Choose up to three programs to compare."); return; }
      updateCompareButton(compareButton);
      renderCompareTray();
    }
  });

  function renderCompareTray() {
    const tray = $("#compare-tray");
    if (!tray) return;
    tray.hidden = compareIds.length === 0;
    const label = $("#compare-tray-label");
    if (label) label.textContent = `${compareIds.length} program${compareIds.length === 1 ? "" : "s"} selected`;
    syncActionButtons();
    announce(compareIds.length ? `${compareIds.length} program${compareIds.length === 1 ? "" : "s"} selected for comparison.` : "Comparison cleared.");
  }

  function valueFor(card, selector) {
    return $(selector, card)?.textContent?.trim() || "Not confirmed";
  }

  function openComparison() {
    const dialog = $("#compare-dialog");
    const content = $("#compare-content");
    if (!dialog || !content) return;
    const selected = compareIds.map((id) => programById.get(id) || document.querySelector(`[data-program-id="${CSS.escape(id)}"]`)).filter(Boolean);
    const rows = [
      ["Program", (card) => valueFor(card, "h3")],
      ["University", (card) => card.querySelector(".card-title-row .eyebrow")?.textContent?.split("·")[0]?.trim() || "Not listed"],
      ["2027/28 status", (card) => valueFor(card, ".status")],
      ["Degree", (card) => card.dataset.level ? `${card.dataset.level}${card.dataset.levelCurrent === "true" ? " (verified for 2027/28)" : " (earlier listing)"}` : "Not confirmed"],
      ["Teaching language", (card) => card.dataset.language ? `${card.dataset.language}${card.dataset.languageCurrent === "true" ? " (verified for 2027/28)" : " (earlier listing)"}` : "Not confirmed"],
      ["Field", (card) => card.dataset.field ? `${card.dataset.field}${card.dataset.fieldCurrent === "true" ? " (verified for 2027/28)" : " (earlier listing)"}` : "Not confirmed"],
      ["Next confirmed application date", (card) => card.dataset.deadline || "No confirmed future date"],
      ["Tuition", (card) => card.dataset.tuition === "documented" ? "2027/28 information documented; check the source" : "No confirmed 2027/28 amount"],
      ["Scholarships", (card) => card.dataset.scholarship === "documented" ? "2027/28 information documented; check the source" : "No confirmed 2027/28 details"]
    ];
    const table = `<div class="table-scroll"><table class="compare-table"><thead><tr><th scope="col">Information</th>${selected.map((card) => `<th scope="col">${escapeHtml(valueFor(card, "h3"))}</th>`).join("")}</tr></thead><tbody>${rows.slice(1).map(([heading, getter]) => `<tr><th scope="row">${escapeHtml(heading)}</th>${selected.map((card) => `<td>${escapeHtml(getter(card))}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    content.innerHTML = table;
    if (typeof dialog.showModal === "function") dialog.showModal();
    else dialog.setAttribute("open", "");
  }

  $("#open-compare")?.addEventListener("click", openComparison);
  $("#close-compare")?.addEventListener("click", () => $("#compare-dialog")?.close());
  $("#clear-compare")?.addEventListener("click", () => { compareIds = []; renderCompareTray(); });

  function csvCell(value) {
    let text = String(value ?? "");
    if (/^[\s]*[=+@]/.test(text)) text = `'${text}`;
    return `"${text.replace(/"/g, '""')}"`;
  }

  function exportCsv() {
    const rows = favoriteIds.map((id) => programById.get(id)).filter(Boolean);
    if (!rows.length) { announce("Save one or more programs before exporting a shortlist."); return; }
    const headers = ["Program", "University", "City", "2027/28 status", "Degree value", "Degree verified for 2027/28", "Language value", "Language verified for 2027/28", "Next confirmed date", "Tuition information", "Scholarship information", "Tracker page"];
    const lines = [headers, ...rows.map((card) => [
      valueFor(card, "h3"), card.querySelector(".card-title-row .eyebrow")?.textContent?.split("·")[0]?.trim() || "",
      card.dataset.city, valueFor(card, ".status"), card.dataset.level, card.dataset.levelCurrent === "true" ? "Yes" : "No",
      card.dataset.language, card.dataset.languageCurrent === "true" ? "Yes" : "No", card.dataset.deadline,
      card.dataset.tuition === "documented" ? "2027/28 information documented" : "Not confirmed",
      card.dataset.scholarship === "documented" ? "2027/28 information documented" : "Not confirmed",
      new URL($('h3 a', card).getAttribute("href"), location.origin).href
    ])].map((row) => row.map(csvCell).join(",")).join("\r\n");
    downloadFile("italy-university-tracker-shortlist.csv", "text/csv;charset=utf-8", "\uFEFF" + lines);
    announce(`${rows.length} saved programs exported as CSV.`);
  }

  function exportIcs() {
    const now = new Date();
    const today = [now.getFullYear(), String(now.getMonth() + 1).padStart(2, "0"), String(now.getDate()).padStart(2, "0")].join("-");
    const rows = favoriteIds.map((id) => programById.get(id)).filter(Boolean);
    const escapeIcs = (value) => String(value).replace(/\\/g, "\\\\").replace(/;/g, "\\;").replace(/,/g, "\\,").replace(/\r?\n/g, "\\n");
    const stamp = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d{3}Z$/, "Z");
    const events = rows.flatMap((card) => {
      let deadlines = [];
      try { deadlines = JSON.parse(card.dataset.deadlines || "[]"); } catch { deadlines = []; }
      const future = deadlines.filter((event) => /^\d{4}-\d{2}-\d{2}$/.test(event.date) && event.date >= today);
      const title = valueFor(card, "h3");
      const university = card.querySelector(".card-title-row .eyebrow")?.textContent?.split("·")[0]?.trim() || "";
      const url = new URL($('h3 a', card).getAttribute("href"), location.origin).href;
      return future.map((event, index) => {
      const deadline = event.date.replace(/-/g, "");
      const nextDay = new Date(`${event.date}T00:00:00Z`);
      nextDay.setUTCDate(nextDay.getUTCDate() + 1);
      const endDate = nextDay.toISOString().slice(0, 10).replace(/-/g, "");
      const eventLabel = event.type === "window" ? "Application window closes" : "Application deadline";
      const eligibility = event.eligible ? ` This date is listed for: ${event.eligible}.` : " Confirm that this date applies to your applicant category.";
      return ["BEGIN:VEVENT", `UID:${card.dataset.programId}-${event.date}-${index}@italy-it-programs.vercel.app`, `DTSTAMP:${stamp}`, `DTSTART;VALUE=DATE:${deadline}`, `DTEND;VALUE=DATE:${endDate}`, `SUMMARY:${escapeIcs(`${eventLabel}: ${title}`)}`, `DESCRIPTION:${escapeIcs(`${university}.${eligibility} Confirm details on the official university source.`)}`, `URL:${url}`, "END:VEVENT"].join("\r\n");
      });
    });
    if (!events.length) { announce("No saved programs have a confirmed future application date to export."); return; }
    downloadFile("italy-university-tracker-deadlines.ics", "text/calendar;charset=utf-8", `BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//Italy University Tracker//2027-28//EN\r\nCALSCALE:GREGORIAN\r\n${events.join("\r\n")}\r\nEND:VCALENDAR\r\n`);
    announce(`${events.length} confirmed future application dates exported to the calendar file.`);
  }

  function downloadFile(filename, type, content) {
    const blob = new Blob([content], { type });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  }

  $("#export-csv")?.addEventListener("click", exportCsv);
  $("#export-ics")?.addEventListener("click", exportIcs);

  const universitySearch = $("#university-search");
  if (universitySearch) {
    const universityCards = $$("[data-university-card]");
    universitySearch.addEventListener("input", () => {
      const q = universitySearch.value.trim().toLowerCase();
      let count = 0;
      universityCards.forEach((card) => {
        const visible = !q || `${card.dataset.name} ${card.dataset.city} ${card.dataset.region}`.toLowerCase().includes(q);
        card.hidden = !visible;
        if (visible) count += 1;
      });
      const result = $("#university-count");
      if (result) result.textContent = `${count} ${count === 1 ? "university" : "universities"} match${count === 1 ? "es" : ""}.`;
      const empty = $("#university-empty");
      if (empty) empty.hidden = count > 0;
    });
  }

  syncActionButtons();
  renderCompareTray();
  applyLanguage();
  renderResults();
})();
