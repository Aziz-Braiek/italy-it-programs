import assert from "node:assert/strict";
import {createServer} from "node:http";
import {readFileSync,existsSync,statSync} from "node:fs";
import {resolve,extname,sep} from "node:path";
import {chromium} from "../work/qa/playwright-tools/node_modules/playwright-core/index.mjs";

const root=resolve('dist');const external=process.env.MONITOR_SITE_URL;
const server=external?null:createServer((req,res)=>{
  const path=new URL(req.url,'http://localhost').pathname;const file=resolve(root,'.'+path+(path.endsWith('/')?'index.html':''));
  if(!file.startsWith(root+sep)||!existsSync(file)||!statSync(file).isFile())return res.writeHead(404).end();
  res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.json':'application/json','.js':'text/javascript','.css':'text/css'})[extname(file)]||'application/octet-stream');res.end(readFileSync(file));
});
if(server)await new Promise(r=>server.listen(0,'127.0.0.1',r));
const base=external||`http://127.0.0.1:${server.address().port}/`;
const url=(path)=>{const u=new URL(base);u.pathname=path;return u.href;};
const browser=await chromium.launch({headless:true,executablePath:process.env.EDGE_PATH||'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
try{
  for(const javaScriptEnabled of [false,true]){
    const context=await browser.newContext({javaScriptEnabled,viewport:{width:390,height:844}});const page=await context.newPage();
    await page.goto(url('/programs/legacy-052/'),{waitUntil:'networkidle'});
    assert.match(await page.locator('.source-checks').innerText(),/Official pages last checked: 2026-11-13/);
    assert.match(await page.locator('.source-checks').innerText(),/Monitoring flags changes; nothing updates automatically/);
    const reviewed=await page.locator('p.last-checked:not(.source-checks)').allTextContents();assert.ok(reviewed.some(t=>t.startsWith('Last reviewed:')));
    for(const width of [320,390]){await page.setViewportSize({width,height:844});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth),width);}
    await page.goto(url('/universities/pisa/'),{waitUntil:'networkidle'});assert.equal(await page.locator('.source-checks').count(),1);
    await page.goto(url('/methodology/'),{waitUntil:'networkidle'});assert.match(await page.locator('main').innerText(),/Nothing updates automatically/);
    for(const path of ['/data/monitoring/queue.json','/research/monitoring/queue.json','/data/monitoring/queue.md','/data/monitoring/snapshots/test.txt.gz']){
      const response=await context.request.get(url(path));assert.equal(response.status(),404,`private path is not deployed: ${path}`);
    }
    const publicResponse=await context.request.get(url('/data/source-checks.json'));assert.equal(publicResponse.status(),200);
    const text=await publicResponse.text();for(const word of ['diff_excerpt','passages','initial_keyword_hits','sample_fingerprints'])assert.ok(!text.includes(word));
    await context.close();
  }
  console.log('SOURCE CHECKS PASSED: distinct check/review dates; no-JS; 320/390px; methodology; metadata-only public JSON; private paths return 404.');
}finally{await browser.close();if(server)await new Promise(r=>server.close(r));}
