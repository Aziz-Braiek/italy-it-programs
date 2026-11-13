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

    def test_binary_filters_have_only_three_states(self):
        for key in ('admission_test', 'english_requirement'):
            for program in B.PROGRAMS:
                fact = D.resolve(program, key, self.universities[program['university_id']])
                self.assertIn(D.binary_state(fact), {'yes', 'no', D.UNKNOWN})
                if not D.is_current(fact) or fact.get('answer') not in {'yes', 'no'}:
                    self.assertEqual(D.binary_state(fact), D.UNKNOWN)
        unknown = D.unknown()
        unknown['answer'] = 'no'
        self.assertEqual(D.binary_state(unknown), D.UNKNOWN)
        current = copy.deepcopy(D.resolve(self.programs['discovered-029'], 'admission_test', self.universities['bologna']))
        for answer in ('yes', 'no', 'conditional', 'not confirmed'):
            current['answer'] = answer
            self.assertEqual(D.binary_state(current), answer if answer in {'yes', 'no'} else D.UNKNOWN)

    def test_rendered_yes_no_flags_require_matching_current_evidence(self):
        for attr in ('admission-test', 'english-certificate'):
            with self.assertRaises(ValueError):
                B.lint_visible_text(f'<article data-program-id="legacy-011" data-{attr}="no"></article>')

    def test_partial_fields_have_distinct_badge_and_named_gaps(self):
        fact = copy.deepcopy(D.resolve(self.programs['legacy-029'], 'prerequisites', self.universities['padova']))
        self.assertTrue(fact['missing_components'])
        html = B.decision_field('Prerequisites', fact)
        self.assertIn('Partly confirmed', html)
        self.assertIn('decision-missing', html)
        self.assertNotIn('class="decision-cycle">2027/28 confirmed', html)
        del fact['missing_components']
        with self.assertRaises(ValueError):
            D.validate_fact(fact, 'unlabelled partial')

    def test_unknown_card_fields_are_collapsed_but_detail_is_explicit(self):
        p = self.programs['discovered-009']
        summary = B.decision_summary(p)
        self.assertIn('4 details not confirmed', summary)
        self.assertNotIn('decision-value', summary)
        details = B.decision_details(p)
        first_section = details.split('</section>', 1)[0]
        self.assertEqual(first_section.count('class="decision-field decision-unknown"'), 9)
        self.assertIn('Not confirmed', details)

    def test_degree_structure_has_source_and_is_separate_from_intake(self):
        p = self.programs['legacy-005']
        fact = D.resolve(p, 'duration', self.universities[p['university_id']])
        self.assertEqual(fact['evidence_scope'], 'degree_structure')
        html = B.decision_field('Duration', fact)
        self.assertIn('Degree structure', html)
        self.assertNotIn('previous cycle (estimate only)', html)
        self.assertNotEqual(D.filter_state(fact), 'documented')
        self.assertEqual(D.export_fact(fact)['value'], 'Not confirmed')
        bad = copy.deepcopy(fact)
        del bad['structure_evidence']
        with self.assertRaises(ValueError):
            D.validate_fact(bad, 'no course evidence')

    def test_every_conflict_is_visible_with_sources_and_conservative_handling(self):
        for conflict in D.read('source-conflicts.json'):
            for pid in conflict['record_ids']:
                html = B.decision_details(self.programs[pid])
                self.assertIn('id="source-conflicts"', html, conflict['id'])
                self.assertIn(B.esc(conflict['handling']), html, conflict['id'])
                for claim in conflict['claims']:
                    self.assertIn(B.esc(claim['source_url']), html, conflict['id'])

    def test_padua_fee_conflict_never_enters_tuition_filter(self):
        self.assertIn('data-tuition="pending"', B.program_data_attrs(self.programs['legacy-029']))
        self.assertIn('Padua fee amounts differ', B.decision_summary(self.programs['legacy-029']))

    def test_hyset_unsecured_funding_is_never_funded(self):
        p = self.programs['discovered-020']
        self.assertFalse(D.is_current(D.scholarship_summary(p, self.universities[p['university_id']])))
        self.assertIn('funding is unsecured', B.decision_summary(p))
        self.assertIn('data-scholarship="pending"', B.program_data_attrs(p))

    def test_pisa_historical_fee_bases_are_not_merged_or_exported(self):
        p = self.programs['legacy-052']
        self.assertIn('fee examples use different bases', B.decision_summary(p))
        self.assertEqual(D.export_fact(D.resolve(p, 'tuition', self.universities['pisa']))['value'], 'Not confirmed')

    def test_28digital_calendar_and_document_conflicts_remain_explicit(self):
        html = B.decision_details(self.programs['discovered-013'])
        self.assertIn('calendars differ', html)
        self.assertIn('mix 2026 and 2027', html)

    def test_florence_overlapping_cambridge_bands_are_not_cleanly_confirmed(self):
        p = self.programs['legacy-125']
        fact = D.resolve(p, 'english_requirement', self.universities['firenze'])
        self.assertTrue(fact['missing_components'])
        self.assertIn('Partly confirmed', B.decision_field('English', fact))
        self.assertIn('Cambridge score bands overlap', B.decision_summary(p))

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
        self.assertTrue("details not confirmed" in home, "homepage collapses unknown fields into one line")
        self.assertIn("previous cycle (estimate only)", home)
        detail = (ROOT / "dist/programs/legacy-053/index.html").read_text(encoding="utf-8")
        self.assertTrue("Verified date: Not confirmed" in detail, "detail page retains explicit unknown provenance")
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
