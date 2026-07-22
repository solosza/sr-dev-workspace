# 013 — Write NIST Validator

**Type:** BUILD
**Phase:** 3 — New Compliance Validators
**Depends on:** 005, 010

## What

Create `nist_validator.py` — Layer 2 Component for NIST 800-171 compliance checks.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\nist_validator.py`

## Requirements

- Same structure as STIGValidator. `FRAMEWORK = "NIST 800-171"`, `FRAMEWORK_ID = "nist"`
- Loads `fixtures/nist_rules.json`
- Full Layer 2 compliance

## Acceptance Criteria

- [ ] File exists at target path
- [ ] Loads `nist_rules.json` fixture
- [ ] Standalone, Layer 2 compliant
