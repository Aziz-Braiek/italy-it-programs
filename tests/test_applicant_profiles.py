"""Source-route expectations and build guards; not a substitute for source review."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import applicant_profiles as A
import decision_support as D


class ApplicantProfilesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = A.compiled()

    def test_four_categories_on_seven_distinct_programs(self):
        # Expected dates are read from the named official routes, not the old
        # prose deadline labels. Resident permit ambiguity deliberately stays blank.
        expected = {
            'legacy-052': ['2027-08-31', '2027-02-01', None, None],
            'legacy-002': ['2027-01-26', '2027-01-26', '2027-01-26', '2027-05-25'],
            'legacy-029': ['2026-11-15', '2026-11-15', None, None],
            'legacy-020': ['2027-01-31', '2027-01-31', None, None],
            'discovered-013': ['2027-01-31']*4,
            'discovered-010': [None, '2026-11-27', None, None],
            'discovered-020': ['2026-11-15']*4,
        }
        for pid, dates in expected.items():
            for category, expected_date in zip(A.CATEGORIES, dates):
                p = {'category': category, 'qualification': 'italy' if category == 'italian-qualification' else 'non-eu'}
                fact = A.select(self.data, pid, 'deadline', p)
                future = sorted(e['date'] for e in fact.get('events', []) if e['date'] >= '2026-11-13')
                with self.subTest(program=pid, category=category):
                    self.assertEqual(future[0] if future else None, expected_date)

    def test_no_qualification_or_italian_category_deadline_fallback(self):
        for profile in [{'category': 'non-eu-abroad'}, {'category': 'italian-qualification'}]:
            f = A.select(self.data, 'legacy-054', 'deadline', profile)
            self.assertFalse(D.is_current(f))
            self.assertFalse(f.get('events'))
        self.assertFalse(D.is_current(A.select(self.data, 'legacy-002', 'deadline', {'category':'italian-qualification', 'qualification':'non-eu'})))

    def test_published_fee_types_and_historical_exclusion(self):
        self.assertEqual(A.tuition_state(self.data, 'legacy-020', {'category':'non-eu-abroad'}), 'documented')
        self.assertEqual(A.select(self.data, 'legacy-020', 'tuition', {'category':'non-eu-abroad'})['amount'], 18000)
        # EU/EEA is published, but CH equivalence is not; the coarse profile must not guess.
        self.assertEqual(A.tuition_state(self.data, 'legacy-020', {'category':'eu-eea-ch'}), 'pending')
        self.assertEqual(A.tuition_state(self.data, 'legacy-020', {'category':'italian-qualification'}), 'pending')
        self.assertEqual(A.tuition_state(self.data, 'discovered-029'), 'rule-only')
        self.assertEqual(A.tuition_state(self.data, 'legacy-002'), 'rule-only')
        for pid in ['legacy-001', 'legacy-052']:
            self.assertEqual(A.tuition_state(self.data, pid), 'pending')
            self.assertEqual(A.tuition_state(self.data, pid, {'category':'non-eu-abroad'}), 'pending')
        self.assertEqual(self.data['tuition_rules']['polimi-2026-income-band']['minimum'], 157.04)
        self.assertEqual(self.data['tuition_rules']['polimi-2026-income-band']['maximum'], 3943.04)
        self.assertEqual(self.data['tuition_rules']['grenfin-self-funded-rule']['amount'], 'Not confirmed')

    def test_route_value_without_source_and_rule_without_regulation_fail(self):
        bad = copy.deepcopy(self.data)
        route = next(r for r in bad['routes'].values() if D.is_current(r['fact']))
        route['fact']['source_urls'] = []
        with self.assertRaises(ValueError): A.validate(bad)
        bad = copy.deepcopy(self.data)
        del bad['tuition_rules']['grenfin-self-funded-rule']['regulation_url']
        with self.assertRaises(ValueError): A.validate(bad)

    def test_previous_cycle_label_and_current_filter_guard(self):
        bad = copy.deepcopy(self.data)
        del bad['tuition_rules']['polimi-2026-income-band']['cycle_status']
        with self.assertRaises(ValueError): A.validate(bad)
        with self.assertRaises(ValueError):
            D.validate_filter_flags({'id':'legacy-001'}, {}, 'documented', None)

    def test_national_rule_stored_once_and_uni_deadline_separate(self):
        self.assertEqual(set(self.data['national_rules']), {'universitaly_requirement'})
        ub = {u['id']:u for u in json.loads((ROOT/'research/universities-2027-2028.json').read_text(encoding='utf-8'))}
        hosts = self.data['research_limits']['host_universities']
        for uid in hosts:
            f = ub[uid]['decision_support']['universitaly']
            self.assertEqual(f.get('national_rule_ref'), 'universitaly_requirement')
            self.assertEqual(D.is_current(f), uid == 'tor-vergata')
        self.assertFalse(D.is_current(A.select(self.data, 'legacy-052','universitaly',{'category':'non-eu-abroad'})))
        self.assertTrue(D.is_current(A.select(self.data, 'discovered-010','universitaly',{'category':'non-eu-abroad'})))

    def test_original_partial_scope_audit_and_full_static_output(self):
        audit = json.loads((A.RESEARCH/'route-scope-audit.json').read_text(encoding='utf-8'))
        self.assertEqual(sum('/minimum_grade' in r['record'] for r in audit),18)
        self.assertEqual(sum('/prerequisites' in r['record'] for r in audit),21)
        for row in audit:
            self.assertTrue(row['covered_scope'])
            self.assertTrue(row['missing_components'])
            self.assertTrue(row['source_urls'])
        html = (ROOT/'dist/index.html').read_text(encoding='utf-8')
        self.assertEqual(html.count('data-program-card="" '),209)
        self.assertIn('id="applicant-profile-selector"',html)
        self.assertIn('rule-only',html)
        detail=(ROOT/'dist/programs/discovered-029/index.html').read_text(encoding='utf-8')
        self.assertIn('Rule only',detail)
        self.assertIn('Official fee regulation',detail)

    def test_historical_degree_cannot_enter_profile_degree_filter(self):
        self.assertEqual(A.degree_group({'level':{'value':'MSc','status':'PREVIOUS_CYCLE'}}),'')
        self.assertEqual(A.degree_group({'level':{'value':'MSc','status':'CONFIRMED'}}),'msc')


if __name__ == '__main__': unittest.main()
