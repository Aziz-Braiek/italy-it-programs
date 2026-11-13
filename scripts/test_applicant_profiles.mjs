import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFileSync, existsSync, statSync, mkdirSync } from "node:fs";
import { resolve, extname, sep } from "node:path";
import { createRequire } from "node:module";
import { chromium } from "../work/qa/playwright-tools/node_modules/playwright-core/index.mjs";

const require = createRequire(import.meta.url);
const E = require("../site/applicant-profiles.js");
const root = resolve("dist");
const external = process.env.PROFILE_SITE_URL;
const server = external ? null : createServer((req, res) => {
  const path = new URL(req.url, "http://localhost").pathname;
  const file = resolve(root, `.${decodeURIComponent(path)}${path.endsWith("/") ? "index.html" : ""}`);
  if (!file.startsWith(root + sep) || !existsSync(file) || !statSync(file).isFile()) return res.writeHead(404).end();
  res.setHeader("Content-Type", ({".html":"text/html; charset=utf-8",".js":"text/javascript; charset=utf-8",".css":"text/css; charset=utf-8",".json":"application/json"})[extname(file)] || "application/octet-stream");
  res.end(readFileSync(file));
});
if (server) await new Promise(r => server.listen(0,"127.0.0.1",r));
const base = external || `http://127.0.0.1:${server.address().port}/`;
const pageUrl = (path="/", params={}) => { const u=new URL(base); u.pathname=path; for(const [k,v] of Object.entries(params))u.searchParams.set(k,v); return u.href; };
const browser = await chromium.launch({headless:true, executablePath:process.env.EDGE_PATH || "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"});
const errors=[];
function csvRows(text) {
  const rows=[]; let row=[],cell="",quoted=false;
  for(let i=0;i<text.replace(/^\uFEFF/,"").length;i++) {
    const c=text.replace(/^\uFEFF/,"")[i];
    if(c==='"') { if(quoted && text.replace(/^\uFEFF/,"")[i+1]==='"'){cell+='"';i++;} else quoted=!quoted; }
    else if(c===","&&!quoted){row.push(cell);cell="";}
    else if(c==='\n'&&!quoted){row.push(cell.replace(/\r$/,""));rows.push(row);row=[];cell="";}
    else cell+=c;
  }
  if(cell||row.length){row.push(cell.replace(/\r$/,""));rows.push(row);}
  return rows.slice(1).map(r=>Object.fromEntries(rows[0].map((h,i)=>[h,r[i]])));
}
async function download(page,button) {
  const pending=page.waitForEvent("download"); await page.locator(button).click();
  const d=await pending; return readFileSync(await d.path(),"utf8");
}
try {
  const context=await browser.newContext({acceptDownloads:true,viewport:{width:1365,height:900}});
  // The research snapshot is 13 Nov; freeze the browser's date for reproducibility.
  await context.addInitScript(() => {const RealDate=Date;window.Date=class extends RealDate {constructor(...args){super(...(args.length?args:["2026-11-13T12:00:00Z"]));}static now(){return new RealDate("2026-11-13T12:00:00Z").getTime();}};});
  const page=await context.newPage();page.on("pageerror",e=>errors.push(e.message));
  await page.goto(pageUrl(),{waitUntil:"networkidle"});
  const data=await page.evaluate(()=>ItalyProfileView.data), decisions=await page.evaluate(()=>ItalyProfileView.decisions);
  const expected={"legacy-052":["2027-08-31","2027-02-01",null,null],"legacy-002":["2027-01-26","2027-01-26","2027-01-26","2027-05-25"],"legacy-029":["2026-11-15","2026-11-15",null,null],"legacy-020":["2027-01-31","2027-01-31",null,null],"discovered-013":["2027-01-31","2027-01-31","2027-01-31","2027-01-31"],"discovered-010":[null,"2026-11-27",null,null],"discovered-020":["2026-11-15","2026-11-15","2026-11-15","2026-11-15"]};
  for(const [i,category] of Object.keys(data.categories).entries()) {
    const profile={category,qualification:category==="italian-qualification"?"italy":"non-eu",degree:""};
    const roundtrip=E.fromParams(E.toParams(profile));assert.equal(roundtrip.category,category);assert.equal(roundtrip.qualification,profile.qualification);
    await page.goto(pageUrl("/",Object.fromEntries(E.toParams(profile))),{waitUntil:"networkidle"});
    for(const [id,dates] of Object.entries(expected)) {
      const f=E.select(data,decisions,id,"deadline",profile);
      assert.equal(E.futureEvents(f,"2026-11-13")[0]?.date||null,dates[i],`${id} ${category}: source-route engine`);
      assert.equal(await page.locator(`[data-program-id="${id}"]`).getAttribute("data-deadline"),dates[i]||"",`${id} ${category}: browser rendering`);
      if(!dates[i])assert.match(await page.locator(`[data-program-id="${id}"] .profile-current`).textContent(),/Not confirmed/);
    }
  }
  assert.equal(E.current(E.select(data,decisions,"legacy-054","deadline",{category:"non-eu-abroad"})),false,"missing qualification never chooses foreign route");
  assert.equal(E.current(E.select(data,decisions,"legacy-020","tuition",{category:"eu-eea-ch"})),false,"no Swiss tariff inference");
  await page.locator("#clear-profile").click();
  const baseDeadlines=await page.locator('[data-program-id="legacy-052"]').getAttribute("data-deadlines");
  assert.match(await page.locator('#filter-admission-test option[value="no"]').textContent(),/\(1\)/);
  assert.match(await page.locator('#filter-english-certificate option[value="required"]').textContent(),/\(6\)/);
  for(const selector of ["#filter-admission-test","#filter-english-certificate"]){
    for(const value of ["yes","no","not confirmed"]){
      const option=selector.includes("english")&&value==="yes"?"required":value;
      await page.locator(selector).selectOption(option);
      const key=selector.includes("english")?"englishCertificate":"admissionTest";
      assert.ok((await page.locator('.program-card:not([hidden])').evaluateAll((cards,k)=>cards.map(c=>c.dataset[k]),key)).every(v=>v===value));
    }
    await page.locator("#clear-filters").click();
  }
  // Save four different programme routes, then exercise the actual download handlers.
  for(const id of ["legacy-052","legacy-002","legacy-020","discovered-029"])
    await page.locator(`[data-program-id="${id}"] [data-favorite]`).evaluate(e=>e.click());
  const originalCsv=csvRows(await download(page,"#export-csv"));
  assert.equal(originalCsv.length,4);assert.ok(originalCsv.every(r=>r["Applicant category"]===""));
  const pisa=originalCsv.find(r=>r["Program"].includes("Computer Science")&&!r["Program"].includes("Engineering"));
  assert.equal(pisa["Published annual amount"],"Not confirmed");
  assert.equal(pisa["Tuition and calculation"],"Not confirmed","historical fee is omitted");
  const originalIcs=await download(page,"#export-ics");assert.match(originalIcs,/BEGIN:VEVENT/);assert.ok(!originalIcs.includes("Profile:"));
  await page.locator("#profile-qualification").selectOption("non-eu");
  await page.locator("#profile-category").selectOption("non-eu-abroad");
  await page.locator("#sort-by").selectOption("deadline");
  const visibleDates=await page.locator('.program-card:not([hidden])').evaluateAll(cards=>cards.map(c=>c.dataset.deadline).filter(Boolean));
  assert.deepEqual(visibleDates,[...visibleDates].sort(),"sorting uses only selected-route deadlines");
  const foreignCsv=csvRows(await download(page,"#export-csv"));
  assert.ok(foreignCsv.every(r=>r["Applicant category"]==="non-eu-abroad"));
  const foreignPisa=foreignCsv.find(r=>r["Tracker page"].includes("legacy-052"));
  assert.equal(foreignPisa["Next confirmed date"],"2027-02-01");assert.match(foreignPisa["Profile deadline source URL"],/unipi/);
  const foreign28=foreignCsv.find(r=>r["Tracker page"].includes("legacy-020"));
  assert.equal(foreign28["Published annual amount"],"18000");assert.equal(foreign28["Tuition model type"],"fixed");
  const grenfin=foreignCsv.find(r=>r["Tracker page"].includes("discovered-029"));
  assert.equal(grenfin["Tuition model type"],"rule-only");assert.equal(grenfin["Published annual amount"],"Not confirmed");
  const foreignIcs=await download(page,"#export-ics");assert.match(foreignIcs,/DTSTART;VALUE=DATE:20270201/);assert.ok(!foreignIcs.includes("20270831"));assert.match(foreignIcs,/Profile: non-EU/);
  await page.locator("#profile-category").selectOption("eu-eea-ch");
  const euCsv=csvRows(await download(page,"#export-csv"));
  assert.equal(euCsv.find(r=>r["Tracker page"].includes("legacy-052"))["Next confirmed date"],"2027-08-31");
  assert.equal(euCsv.find(r=>r["Tracker page"].includes("legacy-020"))["Published annual amount"],"Not confirmed");
  await page.locator("#profile-qualification").selectOption("italy");
  await page.locator("#profile-category").selectOption("italian-qualification");
  const italianCsv=csvRows(await download(page,"#export-csv"));
  assert.equal(italianCsv.find(r=>r["Tracker page"].includes("legacy-052"))["Next confirmed date"],"");
  assert.equal(italianCsv.find(r=>r["Tracker page"].includes("legacy-002"))["Next confirmed date"],"2027-05-25");
  const italianIcs=await download(page,"#export-ics");assert.ok(!italianIcs.includes("20270201"));assert.match(italianIcs,/20270525/);
  await page.locator("#profile-degree").selectOption("bsc");
  assert.ok((await page.locator('.program-card:not([hidden])').evaluateAll(cards=>cards.map(c=>c.dataset.profileDegreeHidden))).every(v=>v==="false"));
  await page.locator("#clear-profile").click();
  assert.equal(await page.locator('[data-program-id="legacy-052"]').getAttribute("data-deadlines"),baseDeadlines,"clearing restores no-profile date logic exactly");
  assert.ok(!new URL(page.url()).searchParams.has("applicant"));
  // Detail page has an isolated compact dataset and must produce the same outcome.
  await page.goto(pageUrl("/programs/legacy-052/",{applicant:"non-eu-abroad",qualification:"non-eu"}),{waitUntil:"networkidle"});
  assert.match(await page.locator('.profile-current').innerText(),/2027-02-01/);
  assert.equal(await page.locator('.profile-base-content').isVisible(),false);
  await page.locator('.profile-other-routes > summary').click();assert.equal(await page.locator('.profile-base-content').isVisible(),true);
  assert.equal(await page.locator('.profile-current a[href*="unipi.it"]').evaluateAll(links=>links.every(a=>!new URL(a.href).searchParams.has("applicant"))),true,"profile is never appended to official sources");
  const homeLink=await page.locator('.brand').first().getAttribute('href');assert.match(homeLink,/applicant=non-eu-abroad/);
  await page.goto(pageUrl("/programs/legacy-052/",{applicant:"italian-qualification"}),{waitUntil:"networkidle"});
  assert.ok(!(await page.locator('.profile-current').innerText()).includes("2027-02-01"));
  // Mobile profile controls open and closed, including a long selected profile.
  mkdirSync("tmp/applicant-profile-qa",{recursive:true});
  for(const width of [320,390]) {
    await page.setViewportSize({width,height:844});
    await page.goto(pageUrl("/",{applicant:"non-eu-abroad",qualification:"non-eu", "degree-sought":"msc"}),{waitUntil:"networkidle"});
    for(const open of [false,true]) {
      await page.locator('#applicant-profile-selector').evaluate((el,state)=>el.open=state,open);
      assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth),width,`${width}px profile ${open?"open":"collapsed"}`);
      if(open) assert.ok((await page.locator('#applicant-profile-selector').boundingBox()).height<700,"mobile selector has no stretched status spacer");
      await page.locator('#applicant-profile-selector').scrollIntoViewIfNeeded();
      await page.screenshot({path:`tmp/applicant-profile-qa/profile-${width}-${open?"open":"collapsed"}.png`});
    }
  }
  const nojsContext=await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:844}});
  const nojs=await nojsContext.newPage();await nojs.goto(pageUrl("/",{applicant:"non-eu-abroad","degree-sought":"bsc"}),{waitUntil:"networkidle"});
  assert.equal(await nojs.locator('.program-card:not([hidden])').count(),209,"profile URL does not filter no-JS HTML");
  assert.equal(await nojs.evaluate(()=>document.documentElement.scrollWidth),320);
  await nojs.goto(pageUrl('/programs/discovered-029/'),{waitUntil:'networkidle'});
  assert.match(await nojs.locator('.profile-base-content').innerText(),/Rule only/);assert.match(await nojs.locator('.profile-base-content').innerText(),/Official fee regulation/);
  assert.deepEqual(errors,[]);
  console.log("Applicant profiles: 7 programmes × 4 categories; source-route expectations, no fallback, URL, three-state counts, selected-route sort/CSV/ICS, fee guards, details, no-JS and 320/390px layouts passed.");
} finally { await browser.close();if(server)await new Promise(r=>server.close(r)); }
