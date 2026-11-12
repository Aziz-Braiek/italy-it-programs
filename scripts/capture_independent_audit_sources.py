"""Capture full official-source responses for a factual audit; reachability is not fact verification."""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, io, json, re, subprocess, time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "independent-audit-2026-11"
EVIDENCE = ROOT / "tmp" / "independent-audit-2026-11" / datetime.now(timezone.utc).strftime("capture-%Y%m%dT%H%M%SZ")
BASE = "c3af9dc"

class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.skip=0; self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag in ("script","style","noscript"): self.skip+=1
        elif tag in ("p","div","li","br","h1","h2","h3","tr","td","section"): self.parts.append("\n")
    def handle_endtag(self,tag):
        if tag in ("script","style","noscript") and self.skip: self.skip-=1
    def handle_data(self,data):
        if not self.skip: self.parts.append(data)
    def value(self):
        return "\n".join(s for line in "".join(self.parts).splitlines() if (s:=re.sub(r"\s+"," ",line).strip()))

def baseline(name):
    return json.loads(subprocess.check_output(["git","show",f"{BASE}:research/{name}"],cwd=ROOT))

def capture(item):
    EVIDENCE.mkdir(parents=True,exist_ok=True)
    url,ids=item; key=hashlib.sha256(url.encode()).hexdigest()[:20]
    result={"url":url,"source_ids":ids,"evidence_key":key,"checked_at_utc":datetime.now(timezone.utc).isoformat(),"method":"Fresh full GET; TLS verification enabled; no account cookies; no-cache headers","fact_verification":"NOT_ESTABLISHED_BY_FETCH"}
    try:
        started=time.monotonic()
        with requests.get(url,headers={"User-Agent":"ItalyTrackerIndependentAudit/1.0","Cache-Control":"no-cache","Pragma":"no-cache"},timeout=(10,24),stream=True) as response:
            body=bytearray()
            for chunk in response.iter_content(65536):
                body.extend(chunk)
                if len(body)>12*1024*1024: raise ValueError("Response exceeds 12 MiB; manual document review required")
            body=bytes(body)
            result.update(http_status=response.status_code,effective_url=response.url,redirects=[{"status":r.status_code,"url":r.url,"location":r.headers.get("location")} for r in response.history],headers={k.lower():v for k,v in response.headers.items() if k.lower() in {"content-type","content-length","etag","last-modified","cache-control","age","date"}},bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),elapsed_seconds=round(time.monotonic()-started,3))
            is_pdf=body.startswith(b"%PDF")
            path=EVIDENCE/(key+(".pdf" if is_pdf else ".html"))
            path.write_bytes(body)
            result["local_raw_path"]=path.relative_to(ROOT).as_posix()
            if is_pdf:
                reader=PdfReader(io.BytesIO(body)); text="\n\n".join(f"[PDF PAGE {i+1}]\n"+(page.extract_text() or "") for i,page in enumerate(reader.pages)); result["pdf_pages"]=len(reader.pages)
            else:
                response.encoding=response.encoding if "charset=" in response.headers.get("Content-Type","").lower() else "utf-8"
                parser=Text(); parser.feed(body.decode(response.encoding or "utf-8",errors="replace")); text=parser.value()
            txt=EVIDENCE/(key+".txt"); txt.write_text(text,encoding="utf-8")
            result["local_text_path"]=txt.relative_to(ROOT).as_posix(); result["text_characters"]=len(text)
            result["transport_outcome"]="accessible" if response.status_code==200 else "broken" if response.status_code in (404,410) else "access_limited" if response.status_code in (401,403,429) else "inconclusive"
    except Exception as error:
        result.update(transport_outcome="inconclusive",error=f"{type(error).__name__}: {error}")
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--workers",type=int,default=10); parser.add_argument("--retry-inconclusive",action="store_true"); args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True); EVIDENCE.mkdir(parents=True,exist_ok=True)
    groups={}
    for source in baseline("sources.json"): groups.setdefault(source["url"],[]).append(source["id"])
    previous=[]
    if args.retry_inconclusive and (OUT/"source-capture-index.json").exists():
        previous=json.loads((OUT/"source-capture-index.json").read_text(encoding="utf-8"))["responses"]
        done={r["url"] for r in previous if r.get("transport_outcome")=="accessible"}
        groups={url:ids for url,ids in groups.items() if url not in done}
    rows={r["url"]:r for r in previous}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures={pool.submit(capture,item):item[0] for item in groups.items()}
        for index,future in enumerate(concurrent.futures.as_completed(futures),1):
            r=future.result(); rows[r["url"]]=r
            payload={"baseline_commit":BASE,"capture_is_not_a_factual_audit":True,"responses":sorted(rows.values(),key=lambda r:r["url"])}
            temporary=OUT/"source-capture-index.tmp"
            temporary.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
            temporary.replace(OUT/"source-capture-index.json")
            if index%25==0 or index==len(futures): print(f"Captured {index}/{len(futures)} unique URLs",flush=True)
    print(json.dumps({"unique_urls":len(rows),"source_records":sum(len(r["source_ids"]) for r in rows.values()),"outcomes":{s:sum(r.get("transport_outcome")==s for r in rows.values()) for s in ("accessible","broken","access_limited","inconclusive")}},indent=2))

if __name__=="__main__": main()
