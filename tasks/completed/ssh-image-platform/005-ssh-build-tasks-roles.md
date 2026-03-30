# Build Tasks + Roles (Layer 3 + 4)

## Type
BUILD

## Context
Layer 3 tasks compose validators with SSH results. Layer 4 roles orchestrate across hosts.

## Dependencies
- 003 (interface), 004 (validators)

## Phase Gate
- [ ] `framework/_reference/ssh_interface.py` imports cleanly
- [ ] `framework/_reference/validators/package_validator.py` imports cleanly

## Requirements
- Create `framework/_reference/tasks/run_ssh_command.py`:
  - `run_ssh_command(ssh_interface, host_config, command, validator_class)` → returns None
  - Composes validator, stores `_ssh_results` on host_config
- Create `framework/_reference/roles/ssh_batch_executor.py`:
  - `SSHBatchExecutor` class with `execute_suite(host_list, test_suite)`
  - Loops over hosts × commands, calls `run_ssh_command` for each
  - Returns summary: hosts_processed, pass/fail counts

## Acceptance Criteria
- [ ] `framework/_reference/tasks/run_ssh_command.py` exists
- [ ] `framework/_reference/roles/ssh_batch_executor.py` exists
- [ ] `python -c "from framework._reference.tasks.run_ssh_command import run_ssh_command"` exits 0
- [ ] `python -c "from framework._reference.roles.ssh_batch_executor import SSHBatchExecutor"` exits 0

## Gates Satisfied
BUILD-13, BUILD-14, FUNC-03, FUNC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
