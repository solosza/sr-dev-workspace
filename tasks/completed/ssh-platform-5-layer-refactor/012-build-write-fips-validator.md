# 012 — Write FIPS Validator

**Type:** BUILD
**Phase:** 3 — New Compliance Validators
**Depends on:** 005, 010

## What

Create `fips_validator.py` — Layer 2 Component for FIPS 140-3 compliance checks.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\fips_validator.py`

## Requirements

- Same structure as STIGValidator. `FRAMEWORK = "FIPS 140-3"`, `FRAMEWORK_ID = "fips"`
- Loads `fixtures/fips_rules.json`
- Full Layer 2 compliance (docstrings, type hints, section headers, no decorators, composition)

## Acceptance Criteria

- [ ] File exists at target path
- [ ] Loads `fips_rules.json` fixture
- [ ] Standalone, Layer 2 compliant
