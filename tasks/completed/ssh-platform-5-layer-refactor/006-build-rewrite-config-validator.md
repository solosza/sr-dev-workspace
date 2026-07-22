# 006 — Rewrite ConfigValidator (standalone)

**Type:** BUILD
**Phase:** 2 — Refactor Existing Validators
**Depends on:** 003, 004

## What

Rewrite `config_validator.py` as a standalone Layer 2 Component. Same pattern as STIGValidator but with inline identifiers (few enough to be class constants).

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\config_validator.py`

## Requirements

- Module docstring: "Layer 2: Config Validator — SSH configuration file checks."
- Constructor: `__init__(self, ssh: SSHInterface)` — composition only
- Identifiers as class-level constants (config paths, expected values)
- Atomic check methods using domain vocabulary
- State-check methods: `is_compliant() -> bool`, `get_findings() -> List[Dict]`
- `validate() -> self`
- Full docstrings, type hints, section headers
- No decorators, no inheritance

## Acceptance Criteria

- [ ] Standalone class, no ABC import
- [ ] Constructor takes `ssh: SSHInterface` only
- [ ] Has class-level constant identifiers
- [ ] Module docstring mentions "Layer 2"
- [ ] Type hints on all methods
