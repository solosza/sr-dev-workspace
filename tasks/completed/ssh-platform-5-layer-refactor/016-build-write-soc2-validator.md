# 016 — Write SOC2 Validator

**Type:** BUILD
**Phase:** 3 — New Compliance Validators
**Depends on:** 005, 010

## What

Create `soc2_validator.py` — Layer 2 Component for SOC 2 compliance checks.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\soc2_validator.py`

## Requirements

- Same structure as STIGValidator. `FRAMEWORK = "SOC 2"`, `FRAMEWORK_ID = "soc2"`
- Loads `fixtures/soc2_rules.json`
- Full Layer 2 compliance

## Acceptance Criteria

- [ ] File exists at target path
- [ ] Loads `soc2_rules.json` fixture
- [ ] Standalone, Layer 2 compliant
