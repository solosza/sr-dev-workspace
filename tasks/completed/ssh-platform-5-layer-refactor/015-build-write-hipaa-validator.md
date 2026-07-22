# 015 — Write HIPAA Validator

**Type:** BUILD
**Phase:** 3 — New Compliance Validators
**Depends on:** 005, 010

## What

Create `hipaa_validator.py` — Layer 2 Component for HIPAA compliance checks.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\hipaa_validator.py`

## Requirements

- Same structure as STIGValidator. `FRAMEWORK = "HIPAA"`, `FRAMEWORK_ID = "hipaa"`
- Loads `fixtures/hipaa_rules.json`
- Full Layer 2 compliance

## Acceptance Criteria

- [ ] File exists at target path
- [ ] Loads `hipaa_rules.json` fixture
- [ ] Standalone, Layer 2 compliant
