import assert from "node:assert/strict";
import { mkdirSync, readFileSync } from "node:fs";
import { resolve, join } from "node:path";
import { pathToFileURL } from "node:url";

const baseUrl = (process.env.SITE_URL || "https://italy-it-programs-git-upgrade-809c06-azizbraaiek-7011s-projects.vercel.app/").replace(/\/$/, "");
const screenshotDir = resolve(process.env.SCREENSHOT_DIR || "work/qa/v2-release-preview");
mkdirSync(screenshotDir, { recursive: true });
const moduleUrl = new URL("../work/qa/playwright-tools/node_modules/playwright-core/index.mjs", import.meta.url);
const { chromium } = await import(pathToFileURL(moduleUrl.pathname.replace(/^\/(?:([A-Za-z]:))/, "$1")).href);
const researchPrograms = JSON.parse(readFileSync(new URL("../research/programs-2027-2028.json", import.meta.url), "utf8"));
const researchUniversities = JSON.parse(readFileSync(new URL("../research/universities-2027-2028.json", import.meta.url), "utf8"));
const totalPrograms = researchPrograms.length;
const confirmedPrograms = researchPrograms.filter((program) => program.overall_status === "CONFIRMED").length;
const totalUniversities = researchUniversities.length;
const browser = await chromium.launch({ headless: true, executablePath: process.env.EDGE_PATH || "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" });
const consoleErrors = [];
const pageErrors = [];
const failedSameOriginRequests = [];
const badSameOriginResponses = [];
const origin = new URL(baseUrl).origin;

try {
  const noJsContext = await browser.newContext({ javaScriptEnabled: false, colorScheme: "light", viewport: { width: 1440, height: 1000 } });
  const noJs = await noJsContext.newPage();
  const noJsResponse = await noJs.goto(baseUrl, { waitUntil: "networkidle" });
  assert.equal(noJsResponse?.status(), 200, "preview homepage responds with HTTP 200 without JavaScript");
  assert.equal(new URL(noJs.url()).origin, origin, "preview does not redirect to a different origin or access gate");
  assert.equal(await noJs.locator("[data-program-card]").count(), totalPrograms, "no-JS HTML contains every program record");
  assert.equal(await noJs.locator("[data-university-card]").count(), totalUniversities, "no-JS HTML contains every university");
  assert.equal(await noJs.locator(".program-card:not([hidden])").count(), totalPrograms, "no-JS mode keeps every program visible");
  assert.ok((await noJs.locator("h1").textContent())?.includes("Italy"), "no-JS mode keeps the page heading");
  assert.equal(await noJs.locator("html").getAttribute("data-theme"), "dark");
  assert.equal(await noJs.locator("body").evaluate((body) => getComputedStyle(body).backgroundColor), "rgb(17, 26, 38)");
  assert.equal(await noJs.locator("#theme-toggle").count(), 0);
  await noJsContext.close();

  const context = await browser.newContext({ colorScheme: "light", viewport: { width: 1440, height: 1000 }, acceptDownloads: true });
  await context.addInitScript(() => { localStorage.setItem("itu-tracker-theme-v2", "light"); });
  const page = await context.newPage();
  page.on("console", (message) => { if (message.type() === "error") consoleErrors.push(message.text()); });
  page.on("pageerror", (error) => pageErrors.push(error.message));
  page.on("requestfailed", (request) => { if (new URL(request.url()).origin === origin) failedSameOriginRequests.push(`${request.method()} ${request.url()} ${request.failure()?.errorText || "failed"}`); });
  page.on("response", (response) => { if (new URL(response.url()).origin === origin && response.status() >= 400) badSameOriginResponses.push(`${response.status()} ${response.url()}`); });

  const homeResponse = await page.goto(baseUrl, { waitUntil: "networkidle" });
  assert.equal(homeResponse?.status(), 200);
  await page.waitForFunction((count) => document.querySelector("#result-count")?.textContent.includes(`${count} programs`), confirmedPrograms);
  assert.equal(await page.locator("[data-program-card]").count(), totalPrograms);
  assert.equal(await page.locator("[data-university-card]").count(), totalUniversities);
  assert.equal(await page.locator(".program-card:not([hidden])").count(), 18, "confirmed program list paginates at 18 cards");
  assert.equal(await page.locator(".program-card:not([hidden])[data-status='CONFIRMED']").count(), 18);
  assert.equal(await page.locator("#pagination").isVisible(), true);
  assert.equal(await page.locator("link[rel=canonical]").getAttribute("href"), "https://italy-it-programs.vercel.app/");
  assert.ok(await page.locator("meta[property='og:image']").getAttribute("content"));
  assert.equal(await page.locator("script[type='application/ld+json']").count(), 1);
  await page.screenshot({ path: join(screenshotDir, "home-desktop.png") });
  await page.evaluate(() => document.activeElement?.blur());
  await page.keyboard.press("Tab");
  assert.equal(await page.evaluate(() => document.activeElement?.textContent?.trim()), "Skip to content", "keyboard navigation reaches the skip link first");

  const sitemap = await page.request.get(`${origin}/sitemap.xml`);
  assert.equal(sitemap.status(), 200);
  const sitemapText = await sitemap.text();
  assert.equal((sitemapText.match(/<url>/g) || []).length, totalUniversities + confirmedPrograms + 5);
  assert.ok(sitemapText.includes("/universities/bologna/"));
  assert.ok(sitemapText.includes("/programs/legacy-020/"));
  const robots = await page.request.get(`${origin}/robots.txt`);
  assert.equal(robots.status(), 200);
  assert.ok((await robots.text()).includes("Sitemap: https://italy-it-programs.vercel.app/sitemap.xml"));

  await page.locator("#search").fill("Data Science");
  await page.waitForTimeout(120);
  assert.ok(new URL(page.url()).searchParams.get("q")?.includes("Data Science"));
  assert.ok(await page.locator(".program-card:not([hidden])").count() > 0, "program search returns results");
  const beforePending = Number((await page.locator("#result-count").textContent()).match(/\d+/)?.[0]);
  await page.locator("#include-pending").check();
  await page.waitForTimeout(120);
  assert.ok(Number((await page.locator("#result-count").textContent()).match(/\d+/)?.[0]) > beforePending);
  assert.equal(new URL(page.url()).searchParams.get("pending"), "1");
  await page.locator("#filter-city").fill("Trento");
  await page.waitForTimeout(120);
  assert.ok(Number((await page.locator("#result-count").textContent()).match(/\d+/)?.[0]) > 0, "city filter narrows results");
  await page.locator("#clear-filters").click();

  await page.locator("#sort-by").selectOption("program");
  const sortedNames = await page.locator(".program-card:not([hidden]) h3").allTextContents();
  assert.deepEqual(sortedNames, [...sortedNames].sort((a, b) => a.localeCompare(b)), "program-name sorting is alphabetic");
  await page.locator("#sort-by").selectOption("availability");

  const firstCard = page.locator(".program-card:not([hidden])").first();
  const firstProgramName = (await firstCard.locator("h3").textContent())?.trim() || "";
  await firstCard.locator(".favorite-button").click();
  assert.equal(await firstCard.locator(".favorite-button").getAttribute("aria-pressed"), "true");
  await page.locator("#show-favorites").click();
  assert.equal(await page.locator(".program-card:not([hidden])").count(), 1, "favorites filter shows the saved program");
  assert.equal((await page.locator(".program-card:not([hidden]) h3").textContent())?.trim(), firstProgramName);
  await page.locator("#show-favorites").click();

  const visibleCompareButtons = page.locator(".program-card:not([hidden]) .compare-button");
  await visibleCompareButtons.nth(0).click();
  await visibleCompareButtons.nth(1).click();
  await page.locator("#open-compare").click();
  assert.equal(await page.locator("#compare-dialog").evaluate((dialog) => dialog.open), true);
  assert.equal(await page.locator(".compare-table thead th").count(), 3);
  await page.keyboard.press("Escape");

  const csvPromise = page.waitForEvent("download");
  await page.locator("#export-csv").click();
  const csv = await csvPromise;
  assert.ok(readFileSync(await csv.path(), "utf8").includes(firstProgramName), "CSV export includes the saved program");

  await firstCard.locator(".favorite-button").click();
  await page.locator("#search").fill("Intelligent Embedded Systems");
  await page.waitForTimeout(120);
  const multiWindowCard = page.locator('.program-card[data-program-id="legacy-020"]');
  assert.equal(await multiWindowCard.isVisible(), true, "calendar test locates its target program even when pagination hides it by default");
  await multiWindowCard.locator(".favorite-button").click();
  const icsPromise = page.waitForEvent("download");
  await page.locator("#export-ics").click();
  const calendar = await icsPromise;
  const calendarText = readFileSync(await calendar.path(), "utf8");
  assert.equal((calendarText.match(/BEGIN:VEVENT/g) || []).length, 3, "all three currently confirmed distinct application windows are exported");
  assert.match(calendarText, /first session/i, "calendar event notes retain applicant-group context");

  const universityUrl = `${origin}/universities/bologna/`;
  const universityResponse = await page.goto(universityUrl, { waitUntil: "networkidle" });
  assert.equal(universityResponse?.status(), 200);
  assert.match((await page.locator("h1").textContent()) || "", /Bologna/i);
  assert.equal(await page.locator("a[href^='/programs/']").count() > 0, true, "university page links to individual program pages");
  assert.equal(await page.locator("link[rel=canonical]").getAttribute("href"), "https://italy-it-programs.vercel.app/universities/bologna/");
  await page.screenshot({ path: join(screenshotDir, "university-desktop.png") });

  const programUrl = `${origin}/programs/legacy-020/`;
  const programResponse = await page.goto(programUrl, { waitUntil: "networkidle" });
  assert.equal(programResponse?.status(), 200);
  assert.match((await page.locator("h1").textContent()) || "", /Intelligent Embedded Systems/);
  assert.ok(await page.locator(".detail-sources a").count() >= 2, "program detail lists its official evidence links");
  assert.equal(await page.locator("link[rel=canonical]").getAttribute("href"), "https://italy-it-programs.vercel.app/programs/legacy-020/");
  await page.screenshot({ path: join(screenshotDir, "program-desktop.png") });

  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(baseUrl, { waitUntil: "networkidle" });
  const mobileDimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, body: document.body.scrollWidth, document: document.documentElement.scrollWidth }));
  assert.deepEqual(mobileDimensions, { viewport: 390, body: 390, document: 390 }, "dark-only mobile layout has no horizontal overflow at 390px");
  assert.equal(await page.locator("#filter-panel").evaluate((details) => details.open), false, "mobile filters start collapsed");
  {
    assert.equal(await page.locator("#theme-toggle").count(), 0);
    assert.equal(await page.locator("html").getAttribute("data-theme"), "dark");
    const darkDimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, body: document.body.scrollWidth, document: document.documentElement.scrollWidth }));
    assert.deepEqual(darkDimensions, { viewport: 390, body: 390, document: 390 }, "mobile dark theme has no horizontal overflow at 390px");
    await page.screenshot({ path: join(screenshotDir, "home-mobile-dark.png") });
    await page.goto(universityUrl, { waitUntil: "networkidle" });
    const mobileUniversityDimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, body: document.body.scrollWidth, document: document.documentElement.scrollWidth }));
    assert.deepEqual(mobileUniversityDimensions, { viewport: 390, body: 390, document: 390 }, "university detail has no mobile overflow");
    await page.screenshot({ path: join(screenshotDir, "university-mobile-dark.png") });
    await page.goto(programUrl, { waitUntil: "networkidle" });
    const mobileProgramDimensions = await page.evaluate(() => ({ viewport: document.documentElement.clientWidth, body: document.body.scrollWidth, document: document.documentElement.scrollWidth }));
    assert.deepEqual(mobileProgramDimensions, { viewport: 390, body: 390, document: 390 }, "program detail has no mobile overflow");
    await page.screenshot({ path: join(screenshotDir, "program-mobile-dark.png") });
  }

  assert.deepEqual(consoleErrors, [], "browser console has no JavaScript errors");
  assert.deepEqual(pageErrors, [], "browser has no uncaught exceptions");
  assert.deepEqual(failedSameOriginRequests, [], "no same-origin network requests failed");
  assert.deepEqual(badSameOriginResponses, [], "no same-origin request returned an HTTP error");
  console.log(`LIVE PREVIEW PASSED ${baseUrl} — HTTP 200; ${totalUniversities} universities; ${totalPrograms} programs; ${confirmedPrograms} confirmed; no-JS fallback; search, filters, sorting, favorites, comparison, CSV, 3-event ICS; university/program pages; SEO; keyboard; 390px mobile. Screenshots: ${screenshotDir}`);
  await context.close();
} finally {
  await browser.close();
}
