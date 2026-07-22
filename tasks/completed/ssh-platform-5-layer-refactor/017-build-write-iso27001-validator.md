# 017 — Write ISO 27001 Validator

**Type:** BUILD
**Phase:** 3 — New Compliance Validators
**Depends on:** 005, 010

## What

Create `iso27001_validator.py` — Layer 2 Component for ISO 27001 compliance checks.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\iso27001_validator.py`

## Requirements

- Same structure as STIGValidator. `FRAMEWORK = "ISO 27001"`, `FRAMEWORK_ID = "iso27001"`
- Loads `fixtures/iso27001_rules.json`
- Full Layer 2 compliance

## Acceptance Criteria

- [ ] File exists at target path
- [ ] Loads `iso27001_rules.json` fixture
- [ ] Standalone, Layer 2 compliant
