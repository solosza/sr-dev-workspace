# Phase 4: Refactor Task + Role Layers

## Status
EXISTS — needs refactor

## Location
`platform-ssh/framework/_reference/tasks/`
`platform-ssh/framework/_reference/roles/`

## Current State
- `run_ssh_command.py` — 3-line function (not a class)
- `ssh_batch_executor.py` — 44 lines, no decorators, stores `self.ssh`, returns results

## What Needs to Happen

### 4.1 Refactor Task Layer
- Convert `run_ssh_command.py` to class-based `SSHCommandTask`
- Constructor takes SSHInterface, creates validator instances internally
- `@automation_logger("Task")` on all methods (NOT constructor)
- Methods return `None` (command pattern)
- One domain operation per method: `run_compliance_scan()`, `run_single_command()`
- Method params are domain values (validator_name, command_string), not SDK objects
- Add `ComplianceTask` class for running validator scans

### 4.2 Refactor Role Layer
- Rewrite `SSHBatchExecutor` as proper Role
- Constructor takes SSHInterface (pass-through) + workflow config (hosts, credentials, scan settings)
- Creates Task instances in constructor (passes Interface to each)
- Does NOT store `self.ssh` — Interface is pass-through only
- `@automation_logger("Role")` on workflow methods, `@automation_logger("Role Constructor")` on `__init__`
- Workflow methods return `None`
- Methods call MULTIPLE Tasks — orchestrates across Task modules

## Dependencies
- Phase 2 + 3 (validators must exist for Tasks to compose them)

## Contract Rules
- Layer 3, Rules 1-7
- Layer 4, Rules 1-6
- Decorator Usage table (Task + Role rows)
