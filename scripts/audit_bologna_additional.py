"""Persist manual comparisons for the two additional Bologna BSc records."""
import copy,json
from build_independent_audit import OUT,baseline,lookup

DAY="2026-11-12"


def main():
    programs=baseline("programs-2027-2028.json")
    sources=baseline("sources.json")
    sm={s["id"]:s for s in sources}
    captures=json.loads((OUT/"bologna-additional-captures.json").read_text(encoding="utf-8"))
    cm={sid:r for r in captures for sid in r["source_ids"]}
    result={"metadata":{"baseline_commit":"c3af9dc","checked_at":DAY,"method":"Manually read fresh profiles, admissions summaries and relevant formal2026/27 call sections; inspected annual labels and degree-specific table rows. No2027/28 rules inferred from older calls."},"program_reviews":[],"university_reviews":[],"source_reviews":[],"confirmed_corrections":[],"additional_official_sources":[]}
    def comp(p,path,value,ids,summary,outcome="MATCH",year="2026/27"):
        return {"field_path":path,"existing_value":lookup(p,path)[1],"official_value":copy.deepcopy(value),"academic_year":year,"checked_at":DAY,"source_ids":ids,"source_urls":[sm[s]["url"] if s in sm else cm[s]["url"] for s in ids],"evidence_summary":summary,"outcome":outcome}
    def correction(p,path,after,ids,why):
        c=comp(p,path,after,ids,why,"CORRECTION_CONFIRMED")
        result["confirmed_corrections"].append({"record_type":"program","record_id":p["id"],"program_id":p["id"],**c,"replacement_value":copy.deepcopy(after),"reason":why})
        return c
    for p in programs:
        if p["id"] not in {"legacy-147","legacy-148"}:continue
        gestionale=p["id"]=="legacy-147"
        prefix="SRC-AUDIT-BOLOGNA-GESTIONALE" if gestionale else "SRC-AUDIT-BOLOGNA-ECONCOM"
        ids=p["source_ids"]+[prefix+"-REQUIREMENTS",prefix+"-CALL-2026"]
        comparisons=[]
        for key in ["program","university","city","level","language","field"]:
            old=p[key];value=old.get("value") if isinstance(old,dict) else old
            comparisons.append(comp(p,key,value,ids,"The official course profile and formal2026/27 call identify the named Bologna University BSc: "+("Italian, L-9, Bologna, locally restricted TOLC-I." if gestionale else "Italian, L-18, Forlì, locally restricted TOLC-E. This is not the Bologna CLaBE/CLEF English route.")+" No named2027/28 intake is established."))
        comparisons.append(comp(p,"availability_2027_2028",None,ids,"Current linked first-year formal call expressly says2026/27. The2027 news/Overseas links and ministerial-activation boilerplate do not establish a new first-year2027/28 intake.","PENDING_ANNOUNCEMENT","2027/28 not established"))
        for key,old in p["facts"].items():
            path="facts."+key
            if key=="previous_cycle_course_listing":
                after=copy.deepcopy(old);after["source_ids"]=ids
                after["notes"]="The linked formal2026/27 call independently corroborates the named course, level, language and campus. Profile news dates alone are not annual admissions evidence."
                comparisons.append(correction(p,path,after,ids,"Add the independently read annual-call provenance for the historical course listing, preserving its2026/27 scope."))
            elif key=="acceptance_rate":
                comparisons.append(comp(p,path,None,ids,"The call gives seat quotas and selection procedures, but the reviewed sources do not give a comparable total of applicants and admitted students. A quota is not an acceptance rate.","UNPUBLISHED_IN_REVIEWED_SOURCES"))
            else:
                explanation={"application_windows":"Only2026/27 annual-call rounds and extraordinary-selection notices were linked; they are not2027/28 dates.","application_fee_2027_2028":"The2026/27 call charges EUR20 once for its selections, separate from the displayed CISIA test fee; it publishes no2027/28 course application fee.","program_specific_requirements_2027_2028":"The older call requires a suitable secondary qualification and programme-specific Italian TOLC, with separate non-EU-abroad eligibility; no2027/28 test, score, quota or language procedure is established.","tuition_2027_2028":"The admissions page links2026 ISEE documentation and2026/27 tuition rules; no programme-specific2027/28 amount is established. Income, country and exemption rules prevent one universal price.","scholarships_2027_2028":"Displayed health/tutoring benefits concern2026/27 or existing students. The2027/28 Overseas mobility notice is not a new-entrant degree scholarship. No2027/28 entry-award amount or guaranteed eligibility is established."}[key]
                comparisons.append(comp(p,path,None,ids,explanation,"PENDING_ANNOUNCEMENT","2027/28 not established"))
        context={"academic_year":"2026/27","degree_class":"L-9" if gestionale else "L-18","secondary_qualification":"Eligible Italian upper-secondary qualification or suitable foreign qualification after at least12 years of schooling; formal recognition checks apply","admission_test":"TOLC-I" if gestionale else "Italian TOLC-E; English TOLC-E is not accepted for this Italian course","english_test_section":"Does not count toward ranking; not an English-taught programme","italian_language":"Non-EU-abroad applicants must satisfy the University Italian-language requirement or an applicable exemption","test_delivery_scope":"TOLC@UNI2025/2026; TOLC@CASA accepted only for the dedicated non-EU-abroad contingent","non_eu_abroad_round":"Second ordinary selection only, within its reserved quota","application_contribution_eur":20,"contribution_rule":"Paid once for this call; a new online application is needed for each selection, without paying the contribution again","published_total_seats":283 if gestionale else 330,"reserved_non_eu_abroad_seats":6 if gestionale else 20,"current_year_warning":"These are historical2026/27 rules, not a2027/28 offer"}
        historical={"value":context,"status":"CONFIRMED","source_ids":ids,"notes":"Independently checked formal2026/27 call Sections2–4 and course admissions page. No numerical school-GPA floor is stated in the inspected eligibility sections; ranking is based on the required TOLC and annual selection rules. Do not transfer the separate English Bologna degree routes or their SAT/CEnT-S rules to this programme."}
        comparisons.append(correction(p,"facts.previous_cycle_2026_2027_admission_context",historical,ids,"Add previously missing, independently verified historical applicant/test/fee/quota scope without promoting it to2027/28."))
        comparisons.append(correction(p,"source_ids",list(dict.fromkeys(ids)),ids,"Preserve original source IDs and add inspected programme-specific admissions/call evidence."))
        result["program_reviews"].append({"program_id":p["id"],"university_id":"bologna","university":p["university"],"program":p["program"],"checked_at":DAY,"overall_outcome":"CORRECTION_CONFIRMED","comparisons":comparisons})
    for sid,r in cm.items():
        is_baseline=sid in sm
        summary=""
        if sid=="SRC-UNIBO-GESTIONALE-BSC-2026":summary="Profile confirms Bologna, Italian, L-9 BSc, locally restricted TOLC-I. A2027/28 Overseas mobility link is not a new first-year offer; linked admissions call is2026/27."
        elif sid=="SRC-UNIBO-ECON-COMMERCIO-2026":summary="Profile confirms Italian L-18 BSc at Forlì, TOLC-E and the two administration/finance and economics/management curricula. This is distinct from the English CLaBE/CLEF courses. Linked first-year call is2026/27."
        elif sid=="SRC-UNIBO-ECONOMIA-COMMERCIO-LOCATION-2026":summary="Graduation-session page identifies the Forlì degree in its header but concerns final-degree ceremonies, not first-year admission rules or a new annual offer. Location matches; no admission inference is made."
        elif "-CALL-" in sid:summary="Formal annual PDF expressly says2026/27. Read cover, course/seat table, applicant categories, secondary qualification, TOLC delivery and selection-contribution sections. Non-EU-abroad applicants use the second ordinary selection. EUR20 is paid once, not once per round; new online applications remain necessary. No2027/28 rules are established."
        elif sid.endswith("-REQUIREMENTS"):summary="Read course-specific admission page: linked annual call2026/27, Italian TOLC-I or TOLC-E as appropriate, Italian-language requirement/exemptions for non-EU-abroad route, separate EUR20 selection and EUR35 test fees, annual quota and qualification checks. Dates/fees remain historical."
        else:summary="Admissions navigation page links programme-specific requirements, annual call, OFA and international/fee guidance. It is a navigation source, not an independent annual admission announcement."
        row={"source_id":sid,"url":r["url"],"content_reviewed":True,"content_review_outcome":"SUPPORTS_RECORDED_SCOPE","observed_cycle":"2026/27 call; general current profile/navigation" if not sid.endswith("LOCATION-2026") else "General graduation page; not annual admission evidence","checked_at":DAY,"evidence_summary":summary,"capture_sha256":r.get("sha256"),"capture_evidence_key":r.get("evidence_key"),"linked_program_ids":["legacy-147" if "GESTIONALE" in sid else "legacy-148"]}
        result["source_reviews"].append(row)
        if not is_baseline:
            result["additional_official_sources"].append({"id":sid,"university_id":"bologna","title":sid.replace("SRC-AUDIT-BOLOGNA-","").replace("-"," "),"url":r["url"],"source_type":"Official course admissions page or linked annual call","accessed_at":DAY,"cycle":"2026-2027","evidence":summary,"supports":["independent_audit.programme_comparison"],"url_check":{"http_status":r["http_status"],"effective_url":r["effective_url"],"content_type":r["headers"].get("content-type"),"bytes_read":r["bytes"],"outcome":r["transport_outcome"],"checked_at":DAY,"method":r["method"]}})
    (OUT/"batch-bologna-additional.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:len(v) for k,v in result.items() if isinstance(v,list)},indent=2))


if __name__=="__main__":main()
