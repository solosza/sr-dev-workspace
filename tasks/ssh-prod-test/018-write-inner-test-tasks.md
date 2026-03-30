# Write inner test task files in test repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Create `C:/Users/solos/my_ai_projects/platform-ssh-test/tasks/prod-test/` and write the following task files inside it:

### 000-index.md
Task index for inner test execution.

### 001-run-l1-structural-gates.md
Run all 12 structural gates from `.claude/skills/ssh-management-layer/gate-contract.md`. All paths relative to test repo root.

### 002-run-l2-import-checks.md
Run FUNC-01 through FUNC-05 using `PYTHONPATH=framework/_reference`.

### 003-run-l2-pytest-unit-tests.md
Run `pytest framework/_reference/tests/ -v`.

### 004-write-live-host-config.md
Write `_test/fixtures/live_host_config.json` pointing to localhost:2222 with test key at `_test/docker/test_key`.

### 005-l3-test-ssh-interface.md
Python script: import SSHInterface, connect to localhost:2222, run `uname -r`, assert exit 0 + non-empty output.

### 006-l3-test-package-validator.md
Python script: import PackageValidator, validate bash/openssh-server/rocky-release.

### 007-l3-test-kernel-validator.md
Python script: import KernelValidator, check kernel version + modules.

### 008-l3-test-service-validator.md
Python script: import ServiceValidator, check sshd active.

### 009-l3-test-config-validator.md
Python script: import ConfigValidator, check sshd_config PermitRootLogin pattern.

### 010-l3-test-batch-executor-e2e.md
Python script: import SSHBatchExecutor with all 4 validators, run execute_all + get_results, verify total/passed/failed.

### 011-write-validation-report.md
Aggregate results into `_test/validation-report.json`.

Each task file follows the standard template (Type, Executor, Action, Acceptance Criteria). All paths relative to test repo.

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-test/tasks/prod-test/000-index.md` exists
- [ ] 12 task files exist (000-011)
- [ ] All task files use relative paths (no absolute paths to platform-ssh-test)
