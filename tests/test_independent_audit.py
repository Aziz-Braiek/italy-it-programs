"""Regression checks for independently documented corrections, not factual proof."""
import json
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"research/independent-audit-2026-11"


def read(name):return json.loads((ROOT/"research"/name).read_text(encoding="utf-8"))


class IndependentAuditRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.programs={r["id"]:r for r in read("programs-2027-2028.json")}
        cls.sources={r["id"]:r for r in read("sources.json")}
        cls.ledger=json.loads((AUDIT/"review-ledger.json").read_text(encoding="utf-8"))

    def test_complete_review_scope_preserves_original_records(self):
        baseline=json.loads(subprocess.check_output(["git","show","c3af9dc:research/sources.json"],cwd=ROOT))
        self.assertEqual(len(self.programs),209)
        self.assertTrue({r["id"] for r in baseline}<=set(self.sources))
        self.assertEqual({r["program_id"] for r in self.ledger["program_reviews"]},set(self.programs))
        self.assertEqual(len(self.ledger["source_reviews"]),700)
        self.assertEqual(len(self.ledger["university_reviews"]),34)
        self.assertEqual(self.ledger["metadata"]["audit_state"],"REVIEWED_WITH_EXPLICIT_LIMITATIONS")
        self.assertFalse(self.ledger["validation"]["problems"])
        self.assertFalse(self.ledger["validation"]["baseline_mismatches"])
        self.assertFalse(self.ledger["validation"]["missing_field_reviews"])

    def test_pisa_programme_deadline_zones_remain_distinct(self):
        for rid in ["legacy-052","legacy-055","discovered-001"]:
            deadline=self.programs[rid]["facts"]["application_deadline"]["value"]
            self.assertEqual(deadline["timezone"],"Anywhere on Earth (AoE)")
            self.assertEqual(deadline["end"],"2027-02-01")
        cybersecurity=self.programs["legacy-053"]
        self.assertEqual(cybersecurity["overall_status"],"CONFIRMED")
        self.assertEqual(cybersecurity["facts"]["application_deadline"]["value"]["time"],"23:59 GMT")
        self.assertEqual(cybersecurity["facts"]["program_specific_requirements_2027_2028"]["value"]["minimum_cgpa_percent"],75)
        self.assertEqual(self.programs["legacy-057"]["facts"]["application_windows"]["status"],"CONFLICTING_SOURCES")

    def test_messina_draft_and_medical_routes_are_not_msc_admissions(self):
        program=self.programs["legacy-076"]
        self.assertIsNone(program["availability_2027_2028"]["value"])
        self.assertEqual(program["facts"]["academic_year_course_offering"]["status"],"REQUIRES_VERIFICATION")
        windows=program["facts"]["application_windows"]
        self.assertEqual(windows["status"],"REQUIRES_VERIFICATION")
        self.assertEqual(len(windows["value"]),4)
        self.assertFalse(any(w["label"] in {"Semestre Aperto","Medicine and Surgery (IMAT)"} for w in windows["value"]))

    def test_joint_bocconi_route_does_not_inherit_generic_polimi_fee(self):
        program=self.programs["legacy-002"]
        self.assertEqual(program["facts"]["application_fee_2027_2028"]["value"]["amount_eur"],100)
        windows=program["facts"]["application_windows"]["value"]
        self.assertEqual(len(windows["international_degree_rounds"]),4)
        self.assertEqual(len(windows["italian_degree_dedicated_joint_rounds"]),2)
        self.assertEqual(windows["international_round_closing_time"],"15:00 Italian time")

    def test_narrow_fee_and_applicant_scope_corrections_remain(self):
        for rid in ["legacy-058","legacy-059","legacy-060","legacy-061"]:
            self.assertEqual(self.programs[rid]["facts"]["previous_cycle_tuition"]["value"]["first_installment_eur"],146)
        self.assertEqual(self.programs["legacy-044"]["city"],"Rieti")
        self.assertEqual(self.programs["legacy-020"]["city"],"Cesena")
        self.assertEqual(self.programs["discovered-010"]["facts"]["application_windows"]["status"],"CONFLICTING_SOURCES")
        self.assertEqual(self.programs["legacy-033"]["facts"]["application_fee_2027_2028"]["value"]["CEnT_S_registration_fee_eur"],55)


if __name__=="__main__":unittest.main()
