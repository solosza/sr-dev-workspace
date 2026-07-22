# 018 — Rewrite Task Layer

**Type:** BUILD
**Phase:** 4 — Task + Role
**Depends on:** 005-017 (all validators must exist)

## What

Rewrite `run_ssh_command.py` from a 3-line function to a class-based Layer 3 Task.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\tasks\run_ssh_command.py`

## Contract Rules (5-layer-contract.md)

**Layer 3 — Task:**
- Constructor takes Interface instance, creates Component instances internally
- `@automation_logger("Task")` on all methods, NOT on constructor
- One domain operation per method
- Uses fluent Component chaining inside methods
- Method parameters are domain values, not UI/SDK objects
- Only imports from Component and Interface layers
- No knowledge of Roles or Tests
- Task methods return `None` — side effects only (command pattern)

## Requirements

- Rename conceptually to `ComplianceTask` class (file can stay `run_ssh_command.py` or rename)
- Module docstring: "Layer 3: Compliance Task — domain operations for SSH compliance scanning."
- Constructor: `__init__(self, ssh: SSHInterface)` — creates validator instances internally
- `@automation_logger("Task")` on methods
- Methods: `run_compliance_scan(framework: str) -> None`, `run_single_command(command: str) -> None`
- Method params are domain values (framework name, command string)
- Returns `None` — results stored on validator Components
- Import from validators and ssh_interface only

## Acceptance Criteria

- [ ] Class-based (`class ComplianceTask`)
- [ ] Constructor takes `ssh: SSHInterface`
- [ ] Creates validator instances internally in constructor
- [ ] `@automation_logger("Task")` on methods (not constructor)
- [ ] Methods return `None`
- [ ] Module docstring mentions "Layer 3"
- [ ] No imports from roles or tests
