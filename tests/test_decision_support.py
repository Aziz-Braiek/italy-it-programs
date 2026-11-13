"""Provenance and presentation guards; these tests do not prove admissions facts."""
import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import decision_support as D

SPEC = importlib.util.spec_from_file_location("decision_site", ROOT / "scripts/build_site.py")
B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(B)


class DecisionSupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.programs = {p["id"]: p for p in B.PROGRAMS}
        cls.universities = {u["id"]: u for u in B.UNIVERSITIES}

    def test_all_records_have_explicit_outcomes_and_provenance(self):
        D.validate(B.UNIVERSITIES, B.PROGRAMS)
        for p in B.PROGRAMS:
            self.assertEqual(set(p["decision_support"]), set(D.PROGRAM_FIELDS))
            for key in D.PROGRAM_FIELDS:
                fact = D.resolve(p, key, self.universities[p["university_id"]])
                self.assertIn(fact["cycle_status"], {D.CURRENT, D.PREVIOUS, D.UNKNOWN})
                self.assertIn("source_urls", fact)
                self.assertIn("verified_date", fact)
                if fact["cycle_status"] == D.UNKNOWN:
                    self.assertEqual(fact["value"], "Not confirmed")

    def test_values_without_source_or_verified_date_fail(self):
        p = self.programs["legacy-053"]
        original = D.resolve(p, "prerequisites", self.universities["pisa"])
        for key in ("source_urls", "verified_date"):
            bad = copy.deepcopy(original)
            bad[key] = [] if key == "source_urls" else None
            with self.assertRaises(ValueError, msg=key):
                D.validate_fact(bad, "fixture")

    def test_previous_cycle_without_label_fails(self):
        p = self.programs["legacy-052"]
        bad = copy.deepcopy(D.resolve(p, "tuition", self.universities["pisa"]))
        del bad["cycle_status"]
        with self.assertRaises(ValueError):
            D.validate_fact(bad, "fixture")

    def test_current_cost_or_scholarship_without_current_evidence_fails(self):
        facts = [D.resolve(self.programs["discovered-029"], "tuition", self.universities["bologna"]),
                 D.scholarship_summary(self.programs["legacy-001"], self.universities["politecnico-milano"])]
        for fact in facts:
            bad = copy.deepcopy(fact)
            del bad["current_cycle_evidence"]
            with self.assertRaises(ValueError):
                D.validate_fact(bad, "fixture")

    def test_rendered_confirmed_filter_flags_fail_for_historical_values(self):
        with self.assertRaises(ValueError):
            B.lint_visible_text('<article data-program-id="legacy-052" data-tuition="documented"></article>')
        with self.assertRaises(ValueError):
            B.lint_visible_text('<article data-program-id="discovered-011" data-scholarship="documented"></article>')

    def test_a_current_tag_cannot_substitute_for_captured_annual_evidence(self):
        fact = copy.deepcopy(D.resolve(self.programs["discovered-029"], "tuition", self.universities["bologna"]))
        old = next(row for row in D.read("source-checks.json")["responses"] if "DEC-POLITO-REQ-2026" in row["source_ids"])
        self.assertNotIn("2027/28", old["academic_cycles_detected"])
        fact.update(source_urls=[old["url"]], evidence_sha256={old["url"]: old["sha256"]},
                    current_cycle_evidence={"url": old["url"], "cycle_marker": "Claimed 2027/28"})
        with self.assertRaises(ValueError):
            D.validate_fact(fact, "false-current-tuition")

    def test_estimates_do_not_enter_confirmed_filters_or_csv_values(self):
        p = self.programs["legacy-052"]
        tuition = D.resolve(p, "tuition", self.universities["pisa"])
        self.assertEqual(D.filter_state(tuition), "pending")
        exported = D.export_fact(tuition)
        self.assertEqual(exported["value"], "Not confirmed")
        self.assertEqual(exported["cycle_status"], D.PREVIOUS)
        self.assertNotIn("2,900", json.dumps(exported))
        for pid in ("legacy-011", "legacy-012", "legacy-013"):
            attrs = B.program_data_attrs(self.programs[pid])
            self.assertIn('data-admission-test="not confirmed"', attrs)
        live = D.resolve(self.programs["discovered-029"], "admission_test", self.universities["bologna"])
        self.assertEqual(live["answer"], "no")
        self.assertTrue(D.is_current(live))

    def test_university_policies_are_inherited_and_scholarships_are_scoped(self):
        p = self.programs["legacy-029"]
        ref = p["decision_support"]["english_requirement"]
        self.assertEqual(set(ref), {"university_policy"})
        self.assertNotIn("scholarships", p["decision_support"])
        self.assertIs(D.resolve(p, "english_requirement", self.universities["padova"]), self.universities["padova"]["decision_support"]["policies"]["english_b2"])
        joint = D.scholarship_summary(self.programs["legacy-002"], self.universities["politecnico-milano"])
        self.assertFalse(D.is_current(joint), "Bocconi's route must not inherit Polimi's standard early-bird merit eligibility")
        hyset = D.scholarship_summary(self.programs["discovered-020"], self.universities["politecnico-torino"])
        self.assertEqual(hyset["value"], "Not confirmed", "uncertain 2027 funding is not an award")

    def test_no_js_html_contains_decision_fields_and_unknowns(self):
        home = (ROOT / "dist/index.html").read_text(encoding="utf-8")
        self.assertEqual(home.count('class="decision-summary"'), 209)
        self.assertIn("Scholarship available", home)
        self.assertIn("Verified date: Not confirmed", home)
        self.assertIn("previous cycle (estimate only)", home)
        detail = (ROOT / "dist/programs/legacy-053/index.html").read_text(encoding="utf-8")
        for label in [*D.PROGRAM_FIELDS.values(), *D.UNIVERSITY_FIELDS.values(), "Scholarships and fee waivers"]:
            self.assertIn(label, detail)
        self.assertIn("75%", detail)
        self.assertIn("2027/28 confirmed", detail)
        self.assertIn("Verified: 2026-11-13", detail)

    def test_phase_zero_wording_guards(self):
        for value in ("REQUIRES", "Earlier listing: Not confirmed", "Not confirmed / Not confirmed", "IT degrees"):
            with self.assertRaises(ValueError, msg=value):
                B.lint_visible_text(f"<p>{value}</p>")
        B.lint_visible_text("<p>This programme requires a B2 certificate.</p>")

    def test_original_statuses_review_dates_and_deadline_facts_are_unchanged(self):
        for filename, records in (("programs-2027-2028.json", B.PROGRAMS), ("universities-2027-2028.json", B.UNIVERSITIES)):
            original = json.loads(subprocess.check_output(["git", "show", f"778db56:research/{filename}"], cwd=ROOT))
            stripped = [{k: v for k, v in record.items() if k != "decision_support"} for record in records]
            self.assertEqual(stripped, original)


if __name__ == "__main__":
    unittest.main()
