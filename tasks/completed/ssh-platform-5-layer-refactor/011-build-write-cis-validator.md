# 011 — Write CIS Validator

**Type:** BUILD
**Phase:** 3 — New Compliance Validators
**Depends on:** 005 (STIGValidator pattern), 010 (phase gate)

## What

Create `cis_validator.py` — Layer 2 Component for CIS Benchmark compliance checks.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\cis_validator.py`

## Requirements

- Same structure as refactored STIGValidator (task 005)
- Module docstring: "Layer 2: CIS Validator — CIS Benchmark compliance checks for SSH hardening."
- `FRAMEWORK = "CIS Benchmarks"`, `FRAMEWORK_ID = "cis"`
- Constructor: `__init__(self, ssh: SSHInterface)` — loads rules from `fixtures/cis_l1_rules.json`
- Inline check methods: `check_config_value()`, `check_config_absent()`, etc.
- State-check methods: `is_compliant()`, `get_score()`, `get_findings()`
- `validate() -> self`
- Full docstrings, type hints, section headers, no decorators

## Acceptance Criteria

- [ ] File exists at target path
- [ ] Loads `cis_l1_rules.json` fixture
- [ ] Standalone (no ABC import)
- [ ] Module docstring mentions "Layer 2"
