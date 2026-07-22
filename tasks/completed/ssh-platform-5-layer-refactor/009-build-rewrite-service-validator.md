# 009 — Rewrite ServiceValidator (standalone)

**Type:** BUILD
**Phase:** 2 — Refactor Existing Validators
**Depends on:** 003, 004

## What

Rewrite `service_validator.py` as a standalone Layer 2 Component.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\validators\service_validator.py`

## Requirements

- Same pattern as ConfigValidator (task 006)
- Module docstring: "Layer 2: Service Validator — systemd service status checks."
- Constructor: `__init__(self, ssh: SSHInterface)`
- Class-level constant identifiers for expected services
- Atomic check methods, state-check methods, `validate() -> self`
- Full docstrings, type hints, section headers, no decorators

## Acceptance Criteria

- [ ] Standalone class, no ABC import
- [ ] Constructor takes `ssh: SSHInterface` only
- [ ] Module docstring mentions "Layer 2"
- [ ] Type hints on all methods
