# 004 — Delete ComplianceValidator ABC

**Type:** BUILD
**Phase:** 2 — Refactor Existing Validators
**Depends on:** 003

## What

Delete `compliance_validator.py` — the ABC base class. 5-layer contract mandates composition over inheritance (Global Rule #6). Each validator will be standalone.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\compliance_validator.py`

## Requirements

- Delete the file entirely
- The check logic (check_config_value, check_service_status, etc.) moves INTO each validator as atomic methods — NOT into a shared utility. Only Layer 2 touches the Interface (5-layer contract).
- The `make_result()` helper becomes a module-level function in a `result_builder.py` utility file (pure data formatting, no Interface calls)

## Acceptance Criteria

- [ ] `framework/_reference/validators/compliance_validator.py` does NOT exist
- [ ] `framework/_reference/validators/result_builder.py` exists with `make_result()` function
