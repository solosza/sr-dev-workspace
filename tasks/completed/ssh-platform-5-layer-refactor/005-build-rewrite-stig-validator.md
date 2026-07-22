# 005 — Rewrite STIGValidator (standalone)

**Type:** BUILD
**Phase:** 2 — Refactor Existing Validators
**Depends on:** 003, 004

## What

Rewrite `stig_validator.py` as a standalone Layer 2 Component. No inheritance from ComplianceValidator. Composition only.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\stig_validator.py`

## Contract Rules (5-layer-contract.md)

**Layer 2 — Component:**
- Constructor takes Interface instance only (SSHInterface) — composition, no inheritance
- No decorators on any methods
- Identifiers as class-level constants or externalized to fixture JSON (loaded in constructor)
- One atomic operation or state-check per method
- Method names use domain vocabulary (e.g., `check_protocol`, `check_key_exchange`)
- Only imports from Interface layer or utilities
- No knowledge of Tasks, Roles, or Tests
- Atomic action methods return `self` (fluent API)
- State-check methods return `bool` or primitive

## Requirements

- Module docstring: "Layer 2: STIG Validator — DISA STIG compliance checks for SSH hardening."
- Class docstring listing Layer 2 rules
- `FRAMEWORK = "DISA STIG"` and `FRAMEWORK_ID = "stig"` as class constants
- Constructor: `__init__(self, ssh: SSHInterface)` — loads rules from `fixtures/stig_rules.json`
- Inline the check logic from ComplianceValidator: `check_config_value()`, `check_config_absent()`, `check_package_installed()`, `check_service_status()` — these are atomic operations that call `self.ssh.execute()`
- State-check methods: `is_compliant() -> bool`, `get_score() -> float`, `get_findings() -> List[Dict]`
- `validate() -> self` (runs all rules, stores results internally)
- Use `make_result()` from `result_builder.py`
- `# === IDENTIFIERS ===`, `# === ATOMIC OPERATIONS ===`, `# === STATE CHECKS ===` section headers

## Acceptance Criteria

- [ ] No import of `ComplianceValidator` or `ABC`
- [ ] Constructor takes `ssh: SSHInterface` only
- [ ] Loads rules from `fixtures/stig_rules.json` in constructor
- [ ] Has `check_config_value`, `check_service_status` as methods (not inherited)
- [ ] Has `is_compliant()` returning `bool`
- [ ] Has `validate()` returning `self`
- [ ] Module docstring mentions "Layer 2"
- [ ] Section header comments present
