"""Explicit, source-backed applicant routes. No text-label route inference."""
import copy
import json
import re
from functools import lru_cache
from datetime import date
from pathlib import Path
import decision_support as D

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research/applicant-profiles-2026-11'
CATEGORIES = {'eu-eea-ch': 'EU/EEA/CH', 'non-eu-abroad': 'non-EU residing abroad', 'non-eu-in-italy': 'non-EU already in Italy', 'italian-qualification': 'Italian-qualification holder'}
ORIGINS = {'italy': 'Italy', 'eu': 'EU outside Italy', 'non-eu': 'non-EU'}
LEVELS = {'bsc': 'BSc', 'msc': 'MSc', 'single-cycle': 'single-cycle', 'professional-master': 'professional master'}
FIELDS = ('deadline', 'tuition', 'english_requirement', 'documents', 'prerequisites', 'minimum_grade', 'admission_test', 'selection_method', 'universitaly', 'scholarships')


def read():
    return json.loads((RESEARCH/'verified-routes.json').read_text(encoding='utf-8'))


@lru_cache(maxsize=1)
def _compiled(version):
    return json.loads((RESEARCH/'compiled-routes.json').read_text(encoding='utf-8'))


def compiled():
    path = RESEARCH/'compiled-routes.json'
    return _compiled(path.stat().st_mtime_ns)


def normalise(profile):
    result = {key: profile.get(key, '') for key in ('category', 'qualification', 'degree')}
    for key, allowed in [('category', CATEGORIES), ('qualification', ORIGINS), ('degree', LEVELS)]:
        if result[key] not in allowed:
            result[key] = ''
    result['invalid'] = result['category'] == 'italian-qualification' and result['qualification'] not in ('', 'italy')
    if result['category'] == 'italian-qualification' and not result['invalid']:
        result['qualification'] = 'italy'
    return result


def matches(conditions, profile):
    p = normalise(profile)
    return not p['invalid'] and all(p.get(key) and p[key] in allowed for key, allowed in conditions.items())


def resolve_ref(ref, universities, programs):
    owner, rid, key = ref.split(':', 2)
    ub = {u['id']: u for u in universities}
    pb = {p['id']: p for p in programs}
    if owner == 'program':
        return D.resolve(pb[rid], key, ub[pb[rid]['university_id']])
    if owner == 'university':
        return ub[rid]['decision_support'][key]
    if owner == 'policy':
        return ub[rid]['decision_support']['policies'][key]
    if owner == 'scholarship':
        return D.scholarship_summary(pb[rid], ub[pb[rid]['university_id']])
    raise ValueError(f'Unknown route fact reference: {ref}')


def compile_data(universities, programs):
    approved = read()
    result = copy.deepcopy(approved)
    result['national_rules'] = json.loads((RESEARCH/'national-rules.json').read_text(encoding='utf-8'))
    result.update(categories=CATEGORIES, qualifications=ORIGINS, degrees=LEVELS, fields=list(FIELDS))
    for route in result['routes'].values():
        if route.get('fact_ref'):
            route['fact'] = copy.deepcopy(resolve_ref(route['fact_ref'], universities, programs))
        route['fact'].update(copy.deepcopy(route.get('overrides', {})))
        route['fact']['covered_scope'] = route['scope']
    for rule in result['tuition_rules'].values():
        if rule.get('provenance_ref'):
            fact = resolve_ref(rule['provenance_ref'], universities, programs)
            for key in ('cycle_status', 'academic_cycle', 'source_urls', 'verified_date', 'current_cycle_evidence', 'evidence_sha256', 'evidence_source_ids'):
                rule[key] = copy.deepcopy(fact.get(key))
    ub = {u['id']: u for u in universities}
    for p in programs:
        result['programs'].setdefault(p['id'], {'university_id': p['university_id'], 'routes': {}})
        result['programs'][p['id']]['degree_group'] = degree_group(p)
    for u in universities:
        result['universities'].setdefault(u['id'], {'routes': {}})
    validate(result)
    return result


def degree_group(program):
    # A historical degree label cannot satisfy a confirmed profile filter.
    if program.get('level', {}).get('status') != 'CONFIRMED':
        return ''
    value = str(program.get('level', {}).get('value') or '').lower()
    if 'professional' in value or 'mba' in value:
        return 'professional-master'
    if 'single' in value:
        return 'single-cycle'
    return {'bsc': 'bsc', 'msc': 'msc'}.get(value, '')


def apply(universities, programs):
    if not (RESEARCH/'verified-routes.json').exists():
        return
    data = compile_data(universities, programs)
    for u in universities:
        u['applicant_routes'] = copy.deepcopy(data['universities'][u['id']]['routes'])
        u['decision_support']['tuition_rule_ids'] = [rid for rid, r in data['tuition_rules'].items() if r.get('university_id') == u['id'] or u['id'] in r.get('university_ids', [])]
    for p in programs:
        p['applicant_routes'] = copy.deepcopy(data['programs'][p['id']]['routes'])
    (RESEARCH/'compiled-routes.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def validate(data):
    def conditions(value, location):
        for key, values in value.items():
            allowed = {'category': CATEGORIES, 'qualification': ORIGINS, 'degree': LEVELS}.get(key)
            if not allowed or not isinstance(values, list) or not values or any(v not in allowed for v in values):
                raise ValueError(f'Invalid applicant conditions: {location}/{key}')
    for rid, route in data['routes'].items():
        conditions(route.get('conditions', {}), rid)
        if not route.get('scope'):
            raise ValueError(f'Route must state applicant scope: {rid}')
        fact = route.get('fact', {})
        D.validate_fact(fact, f'route {rid}')
        if fact.get('value') != 'Not confirmed' and not fact.get('source_urls'):
            raise ValueError(f'Route value lacks source: {rid}')
        for event in fact.get('events', []):
            if not D.is_current(fact):
                raise ValueError(f'Non-current event in profile deadline route: {rid}')
            date.fromisoformat(event['date'])
    for rid, rule in data['tuition_rules'].items():
        conditions(rule.get('conditions', {}), rid)
        if rule.get('type') not in {'fixed', 'band', 'rule-only', 'not confirmed'}:
            raise ValueError(f'Invalid tuition type: {rid}')
        if rule['type'] == 'not confirmed':
            continue
        if not rule.get('regulation_url') or rule['regulation_url'] not in rule.get('source_urls', []):
            raise ValueError(f'Tuition rule lacks its official regulation/fee-notice URL: {rid}')
        D.validate_fact(rule, f'tuition rule {rid}')
        if rule['type'] == 'fixed' and not isinstance(rule.get('amount'), (int, float)):
            raise ValueError(f'Fixed tuition lacks a published amount: {rid}')
        if rule['type'] == 'band' and (not isinstance(rule.get('minimum'), (int, float)) or not isinstance(rule.get('maximum'), (int, float)) or not rule.get('calculation_basis')):
            raise ValueError(f'Band lacks published bounds/basis: {rid}')
        if rule['type'] == 'rule-only' and rule.get('amount') != 'Not confirmed':
            raise ValueError(f'Rule-only tuition must keep its amount unconfirmed: {rid}')
    for owner in ('programs', 'universities'):
        for record in data[owner].values():
            for field, ids in record.get('routes', {}).items():
                if field not in FIELDS:
                    raise ValueError(f'Unknown profile field: {field}')
                pool = data['tuition_rules'] if field == 'tuition' else data['routes']
                if any(rid not in pool for rid in ids):
                    raise ValueError(f'Missing profile route reference: {ids}')
    for key, fact in data.get('national_rules', {}).items():
        D.validate_fact(fact, f'national rule {key}')


def routes_for(data, program_id, field):
    p = data['programs'][program_id]
    ids = p.get('routes', {}).get(field)
    if ids is None:
        ids = data['universities'][p['university_id']].get('routes', {}).get(field, [])
    pool = data['tuition_rules'] if field == 'tuition' else data['routes']
    return [pool[rid] for rid in ids if not pool[rid].get('program_ids') or program_id in pool[rid]['program_ids']]


def select(data, program_id, field, profile):
    p = normalise(profile)
    applicable = [r for r in routes_for(data, program_id, field) if matches(r.get('conditions', {}), p) and D.is_current(r if field == 'tuition' else r.get('fact', {}))]
    if not applicable:
        return D.unknown('No confirmed source-backed value for this selected combination; another route is never substituted.')
    score = max(len(r.get('conditions', {})) for r in applicable)
    selected = [r for r in applicable if len(r.get('conditions', {})) == score]
    if len(selected) != 1:
        return D.unknown('Multiple applicable routes require clarification; no arbitrary route is selected.')
    route = selected[0]
    if route.get('partial_profile_coverage'):
        fact = D.unknown('The selected category is broader than the published route. '+route.get('coverage_reason', route['scope']))
        evidence = route if field == 'tuition' else route['fact']
        fact['checked_urls'] = evidence.get('source_urls', [])
        fact['checked_at'] = evidence.get('verified_date')
        return fact
    fact = copy.deepcopy(route if field == 'tuition' else route['fact'])
    fact['covered_scope'] = route['scope']
    fact['route_id'] = route.get('id', '')
    return fact


def tuition_state(data, program_id, profile=None):
    rules = [select(data, program_id, 'tuition', profile)] if profile else routes_for(data, program_id, 'tuition')
    current = [r for r in rules if D.is_current(r)]
    if any(r.get('type') in {'fixed', 'band'} and not r.get('partial_profile_coverage') for r in current):
        return 'documented'
    return 'rule-only' if any(r.get('type') == 'rule-only' for r in current) else 'pending'


def client_data(data, program_id=None):
    """Hash/passage guards run at build time; the browser gets compact facts."""
    kept = {'value','short_value','cycle_status','academic_cycle','source_urls','verified_date','missing_components','covered_scope','events','answer','program_ids','type','amount','minimum','maximum','currency','period','calculation_basis','known_components','regulation_url','reason','national_rule_ref'}
    def fact(value):
        return {k:v for k,v in value.items() if k in kept}
    result = {k:copy.deepcopy(data[k]) for k in ('categories','qualifications','degrees','fields','programs','universities')}
    if program_id:
        p = result['programs'][program_id]
        result['programs'] = {program_id:p}
        result['universities'] = {p['university_id']:result['universities'][p['university_id']]}
        needed = {rid for r in [p, result['universities'][p['university_id']]] for ids in r.get('routes', {}).values() for rid in ids}
    else:
        needed = set(data['routes']) | set(data['tuition_rules'])
    result['routes'] = {}
    for rid, route in data['routes'].items():
        if rid not in needed:
            continue
        item = {k:v for k,v in route.items() if k != 'fact'}
        if not route.get('fact_ref') or program_id:
            item['fact'] = fact(route['fact'])
            item.pop('fact_ref', None)
            item.pop('overrides', None)
        result['routes'][rid] = item
    result['tuition_rules'] = {rid:{**fact(r), **{k:copy.deepcopy(r[k]) for k in ('id','scope','conditions','program_ids','partial_profile_coverage','coverage_reason') if k in r}} for rid,r in data['tuition_rules'].items() if rid in needed}
    result['national_rules'] = {key:fact(value) for key,value in data['national_rules'].items()}
    return result
