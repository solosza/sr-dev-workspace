# 019 — Rewrite Role Layer

**Type:** BUILD
**Phase:** 4 — Task + Role
**Depends on:** 018

## What

Rewrite `ssh_batch_executor.py` as a proper Layer 4 Role.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\roles\ssh_batch_executor.py`

## Contract Rules (5-layer-contract.md)

**Layer 4 — Role:**
- Constructor takes Interface instance (pass-through) + workflow config
- Creates Task instances in constructor (passes Interface to each Task)
- Workflow methods call MULTIPLE Tasks — orchestrates across Task modules
- Stores workflow config on `self` — does NOT store Interface on `self` (pass-through only)
- Only imports from Task layer (type annotation imports from Interface permitted)
- No knowledge of Tests
- `@automation_logger("Role")` on workflow methods
- `@automation_logger("Role Constructor")` on `__init__`
- Role workflow methods return `None`

## Requirements

- Module docstring: "Layer 4: SSH Batch Executor — orchestrates compliance scanning workflows."
- Constructor: `__init__(self, ssh: SSHInterface, config: Dict[str, Any])` — creates ComplianceTask internally, stores config on self, does NOT store ssh on self
- `@automation_logger("Role Constructor")` on `__init__`
- `@automation_logger("Role")` on workflow methods
- Workflow methods: `run_full_scan() -> None`, `run_framework_scan(framework: str) -> None`
- Workflow methods call Task methods — orchestrate across operations
- Results observable via Component state-checks (validators stored on Tasks)

## Acceptance Criteria

- [ ] `@automation_logger("Role Constructor")` on `__init__`
- [ ] `@automation_logger("Role")` on workflow methods
- [ ] Constructor does NOT store `self.ssh`
- [ ] Constructor creates Task instances (passes Interface)
- [ ] Workflow methods return `None`
- [ ] Module docstring mentions "Layer 4"
- [ ] No imports from tests
