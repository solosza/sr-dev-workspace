# 022 — Rewrite test_ssh_batch.py

**Type:** BUILD
**Phase:** 5 — Tests
**Depends on:** 020

## What

Rewrite `test_ssh_batch.py` to full Layer 5 compliance — class-based AAA through Role.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\tests\test_ssh_batch.py`

## Requirements

- Class-based: `class TestSSHBatchExecution:`
- `setup` fixture creates MockSSH and SSHBatchExecutor Role
- `@automation_logger("Test")` on test methods
- `@pytest.mark.batch` tag
- AAA pattern through Role
- Test methods: test_full_scan_all_frameworks, test_single_framework_scan, test_scan_with_failures

## Acceptance Criteria

- [ ] Class-based test (`class TestSSHBatchExecution`)
- [ ] `@automation_logger("Test")` on test methods
- [ ] `@pytest.mark.batch` present
- [ ] Tests use Role in Act phase
- [ ] One AAA block per method
