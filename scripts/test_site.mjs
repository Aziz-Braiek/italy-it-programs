import assert from "node:assert/strict";
import { createServer } from "node:http";
import { existsSync, readFileSync, statSync } from "node:fs";
import { join, extname, resolve, sep } from "node:path";
import { pathToFileURL } from "node:url";

const root = resolve(new URL("../dist/", import.meta.url).pathname.replace(/^\/(?:([A-Za-z]:))/, "$1"));
const playwrightPath = new URL("../work/qa/playwright-tools/node_modules/playwright-core/index.mjs", import.meta.url);
const { chromium } = await import(pathToFileURL(playwrightPath.pathname.replace(/^\/(?:([A-Za-z]:))/, "$1")).href);
const researchPrograms = JSON.parse(readFileSync(new URL("../research/programs-2027-2028.json", import.meta.url), "utf8"));
const researchUniversities = JSON.parse(readFileSync(new URL("../research/universities-2027-2028.json", import.meta.url), "utf8"));
const totalPrograms = researchPrograms.length;
const confirmedPrograms = researchPrograms.filter((program) => program.overall_status === "CONFIRMED").length;
const totalUniversities = researchUniversities.length;
const mimeTypes = { ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8", ".png": "image/png", ".xml": "application/xml; charset=utf-8", ".txt": "text/plain; charset=utf-8" };

const server = createServer((request, response) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(request.url, "http://localhost").pathname); }
  catch { response.writeHead(400).end("Bad request"); return; }
  if (pathname.endsWith("/")) pathname += "index.html";
  const file = resolve(root, `.${pathname}`);
  if (!file.startsWith(root + sep) && file !== join(root, "index.html")) { response.writeHead(403).end("Forbidden"); return; }
  if (!existsSync(file) || !statSync(file).isFile()) { response.writeHead(404).end("Not found"); return; }
  response.writeHead(200, { "content-type": mimeTypes[extname(file).toLowerCase()] || "application/octet-stream", "cache-control": "no-store" });
  response.end(readFileSync(file));
});

await new Promise((resolveListen, reject) => {
  server.once("error", reject);
  server.listen(0, "127.0.0.1", resolveListen);
});
const { port } = server.address();
const baseUrl = `http://127.0.0.1:${port}`;
const edge = process.env.EDGE_PATH || "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";
const browser = await chromium.launch({ headless: true, executablePath: edge });
const consoleErrors = [];
const pageErrors = [];

try {
  const noJsContext = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 1365, height: 900 } });
  const noJs = await noJsContext.newPage();
  await noJs.goto(baseUrl, { waitUntil: "networkidle" });
  assert.equal(await noJs.locator("[data-program-card]").count(), totalPrograms, "all program entries are in the initial HTML with JavaScript disabled");
  assert.equal(await noJs.locator("[data-university-card]").count(), totalUniversities, "all universities are in the initial HTML with JavaScript disabled");
  assert.equal(await noJs.locator(".program-card:not([hidden])").count(), totalPrograms, "static fallback exposes every entry");
  assert.equal(await noJs.locator("[data-program-card][data-status='CONFIRMED']").count(), confirmedPrograms);
  await noJs.close();
  await noJsContext.close();

  const context = await browser.newContext({ viewport: { width: 1365, height: 900 }, acceptDownloads: true });
  const page = await context.newPage();
  page.on("console", (message) => { if (message.type() === "error") consoleErrors.push(message.text()); });
  page.on("pageerror", (error) => pageErrors.push(error.message));
  await page.goto(baseUrl, { waitUntil: "networkidle" });
  await page.waitForFunction((count) => document.querySelector("#result-count")?.textContent.includes(`${count} programs`), confirmedPrograms);
  assert.equal(await page.locator(".program-card:not([hidden])").count(), 18, "enhanced results are paginated");
  assert.equal(await page.locator(".program-card:not([hidden])[data-status='CONFIRMED']").count(), 18, "pending candidates are not initially mixed into confirmed offers");
  assert.equal(await page.locator("#pagination").isVisible(), true);

  await page.locator("#search").fill("Data Science");
  await page.waitForTimeout(100);
  assert.match(page.url(), /[?&]q=Data\+Science/);
  assert.ok(await page.locator(".program-card:not([hidden])").count() > 0, "program search returns real records");
  const confirmedSearchCount = Number((await page.locator("#result-count").textContent()).match(/\d+/)?.[0]);
  await page.locator("#include-pending").check();
  await page.waitForTimeout(100);
  assert.ok(Number((await page.locator("#result-count").textContent()).match(/\d+/)?.[0]) > confirmedSearchCount, "pending records are separately included when requested");
  assert.match(page.url(), /pending=1/);
  await page.locator("#filter-city").fill("Venice");
  await page.waitForTimeout(100);
  assert.ok(Number((await page.locator("#result-count").textContent()).match(/\d+/)?.[0]) >= 0, "city and region filter runs");
  await page.locator("#clear-filters").click();

  const firstCard = page.locator(".program-card:not([hidden])").first();
  const firstProgramName = await firstCard.locator("h3").textContent();
  await firstCard.locator(".favorite-button").click();
  assert.equal(await firstCard.locator(".favorite-button").getAttribute("aria-pressed"), "true");
  await page.locator("#show-favorites").click();
  assert.equal(await page.locator(".program-card:not([hidden])").count(), 1, "favorites filter shows the saved program");
  assert.equal((await page.locator(".program-card:not([hidden]) h3").textContent())?.trim(), firstProgramName.trim());
  await page.locator("#show-favorites").click();

  const compareButtons = page.locator(".program-card:not([hidden]) .compare-button");
  await compareButtons.nth(0).click();
  await compareButtons.nth(1).click();
  assert.equal(await page.locator("#compare-tray").isVisible(), true, "comparison tray appears for selected records");
  await page.locator("#open-compare").click();
  assert.equal(await page.locator("#compare-dialog").evaluate((dialog) => dialog.open), true);
  assert.equal(await page.locator(".compare-table thead th").count(), 3, "comparison presents two programs side by side");
  await page.keyboard.press("Escape");
  assert.equal(await page.locator("#compare-dialog").evaluate((dialog) => dialog.open), false, "dialog closes by keyboard");

  const csvPromise = page.waitForEvent("download");
  await page.locator("#export-csv").click();
  const csv = await csvPromise;
  const csvText = readFileSync(await csv.path(), "utf8");
  assert.match(csvText, /Program,|"Program"/);
  assert.ok(csvText.includes(firstProgramName.trim()), "CSV contains the saved record");

  await page.locator("#clear-compare").click();
  await page.locator("#filter-deadline").selectOption("known");
  const knownDeadline = page.locator(".program-card:not([hidden])[data-status='CONFIRMED'][data-deadline]").first();
  assert.ok(await knownDeadline.count(), "at least one confirmed future deadline is available for export");
  const deadlineName = await knownDeadline.locator("h3").textContent();
  if (await knownDeadline.locator(".favorite-button").getAttribute("aria-pressed") !== "true") {
    await knownDeadline.locator(".favorite-button").click();
  }
  const icsPromise = page.waitForEvent("download");
  await page.locator("#export-ics").click();
  const ics = await icsPromise;
  const icsText = readFileSync(await ics.path(), "utf8");
  assert.match(icsText, /BEGIN:VCALENDAR/);
  assert.match(icsText, /DTSTART;VALUE=DATE:\d{8}/);
  assert.ok(icsText.includes(deadlineName.trim()), "calendar file contains a program with a confirmed future date");

  if (await firstCard.locator(".favorite-button").getAttribute("aria-pressed") === "true") {
    await firstCard.locator(".favorite-button").click();
  }
  const multiWindowCard = page.locator('.program-card[data-program-id="legacy-020"]');
  while (!(await multiWindowCard.isVisible())) {
    const nextPage = page.locator("#page-next");
    assert.equal(await nextPage.isDisabled(), false, "the multi-window program remains within the filtered result pages");
    await nextPage.click();
  }
  if (await multiWindowCard.locator(".favorite-button").getAttribute("aria-pressed") !== "true") {
    await multiWindowCard.locator(".favorite-button").click();
  }
  const multiWindowDownload = page.waitForEvent("download");
  await page.locator("#export-ics").click();
  const multiWindowIcs = await multiWindowDownload;
  const multiWindowText = readFileSync(await multiWindowIcs.path(), "utf8");
  assert.equal((multiWindowText.match(/BEGIN:VEVENT/g) || []).length, 3, "calendar exports each distinct confirmed future application window");
  assert.match(multiWindowText, /first session/i, "calendar descriptions retain the source applicant-group/session notes");

  await page.locator("#language-toggle").click();
  assert.equal(await page.locator("html").getAttribute("lang"), "it");
  assert.equal(await page.locator("nav a").first().textContent(), "Corsi");
  await page.locator("#language-toggle").click();
  assert.equal(await page.locator("html").getAttribute("lang"), "en");

  await page.locator("#theme-toggle").click();
  assert.equal(await page.locator("html").getAttribute("data-theme"), "dark");
  assert.equal(await page.locator("#theme-toggle").getAttribute("aria-pressed"), "true");
  assert.equal(await page.locator("body").evaluate((body) => getComputedStyle(body).backgroundColor), "rgb(17, 26, 38)");
  assert.equal(await page.locator(".hero .button-primary").evaluate((button) => getComputedStyle(button).color), "rgb(16, 35, 63)", "primary button text keeps dark-on-light contrast in dark theme");
  await page.reload({ waitUntil: "networkidle" });
  assert.equal(await page.locator("html").getAttribute("data-theme"), "dark", "dark theme preference persists across reloads");
  await page.locator("#theme-toggle").click();
  assert.equal(await page.locator("html").getAttribute("data-theme"), "light");

  await page.locator("#university-search").fill("Rome");
  const universityCount = await page.locator("#university-count").textContent();
  assert.match(universityCount || "", /universit/i);
  assert.ok((await page.locator("[data-university-card]:not([hidden])").count()) > 0);

  const pendingProgram = researchPrograms.find((program) => program.overall_status === "REQUIRES_VERIFICATION");
  assert.ok(pendingProgram, "dataset includes a pending program for detail-page coverage");
  const pendingProgramPath = `/programs/${pendingProgram.id}/`;
  await page.goto(baseUrl + pendingProgramPath, { waitUntil: "networkidle" });
  assert.ok((await page.locator("h1").textContent() || "").includes(pendingProgram.program), "pending program title renders");
  assert.equal(await page.locator(".status-pending").first().isVisible(), true, "pending detail page remains readable with JavaScript enabled");
  assert.ok(await page.locator(".detail-sources a").count() > 0, "individual program page links to evidence");

  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(baseUrl, { waitUntil: "networkidle" });
  const dimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, body: document.body.scrollWidth, document: document.documentElement.scrollWidth }));
  assert.equal(dimensions.body, dimensions.viewport, "mobile body has no horizontal overflow");
  assert.equal(dimensions.document, dimensions.viewport, "mobile document has no horizontal overflow");
  assert.equal(await page.locator("#filter-panel").evaluate((details) => details.open), false, "mobile filters begin collapsed");
  await page.locator("#filter-panel > summary").focus();
  await page.keyboard.press("Enter");
  assert.equal(await page.locator("#filter-panel").evaluate((details) => details.open), true, "mobile filters are keyboard-operable");
  const accessibleControls = await page.locator("input, select, button").evaluateAll((elements) => elements.every((element) => {
    if (element.type === "hidden") return true;
    const name = element.getAttribute("aria-label") || element.getAttribute("title") || element.closest("label")?.innerText?.trim() || element.innerText?.trim();
    return Boolean(name);
  }));
  assert.equal(accessibleControls, true, "interactive controls have an accessible name");
  await page.locator("#theme-toggle").click();
  assert.equal(await page.locator("html").getAttribute("data-theme"), "dark");
  const darkDimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, body: document.body.scrollWidth, document: document.documentElement.scrollWidth }));
  assert.equal(darkDimensions.body, darkDimensions.viewport, "dark mobile body has no horizontal overflow");
  assert.equal(darkDimensions.document, darkDimensions.viewport, "dark mobile document has no horizontal overflow");

  assert.deepEqual(consoleErrors, [], "browser console has no errors");
  assert.deepEqual(pageErrors, [], "browser reports no uncaught exceptions");
  const htmlSize = statSync(join(root, "index.html")).size;
  const cssSize = statSync(join(root, "assets", "site.css")).size;
  const jsSize = statSync(join(root, "assets", "site.js")).size;
  console.log(`BROWSER TESTS PASSED — static fallback: ${totalPrograms} programs, ${totalUniversities} universities; JS: ${confirmedPrograms} confirmed initially; desktop and 390px mobile checked; home HTML ${htmlSize} bytes, CSS ${cssSize} bytes, JS ${jsSize} bytes.`);
  await context.close();
} finally {
  await browser.close();
  await new Promise((resolveClose, rejectClose) => server.close((error) => error ? rejectClose(error) : resolveClose()));
}
