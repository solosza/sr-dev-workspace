# 021 — Rewrite test_stig_validator.py

**Type:** BUILD
**Phase:** 5 — Tests
**Depends on:** 020

## What

Rewrite `test_stig_validator.py` to full Layer 5 compliance — class-based AAA through Role.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\tests\test_stig_validator.py`

## Contract Rules (5-layer-contract.md)

**Layer 5 — Test:**
- `@pytest.fixture(autouse=True) def setup` wires dependencies
- Setup fixture creates Component instances on `self` for assertions
- `@automation_logger("Test")` on test methods
- `@pytest.mark` tags for categorization
- Test creates Role(s) in Arrange
- Test calls Role workflow method in Act
- Test asserts via Component state-check methods in Assert
- One AAA block per test method
- Test NEVER calls Task or Component directly — always through Role

## Requirements

- Class-based: `class TestSTIGCompliance:`
- `setup` fixture creates MockSSH, SSHBatchExecutor Role, and STIGValidator (for assertions)
- `@automation_logger("Test")` on each test method
- `@pytest.mark.stig` tag
- AAA pattern: Arrange (Role with mock), Act (Role.run_framework_scan("stig")), Assert (validator.is_compliant())
- Multiple test methods: test_compliant_config, test_non_compliant_config, test_missing_directive

## Acceptance Criteria

- [ ] Class-based test (`class TestSTIGCompliance`)
- [ ] `@automation_logger("Test")` on test methods
- [ ] `@pytest.mark.stig` present
- [ ] Tests use Role in Act phase (not Task or Component directly)
- [ ] Assertions use Component state-check methods
- [ ] One AAA block per method
