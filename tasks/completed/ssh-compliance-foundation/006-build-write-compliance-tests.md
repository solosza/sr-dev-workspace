# 006 — Write Compliance Foundation Tests

**Type:** BUILD
**Depends on:** 001, 002, 003, 004, 005

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\tests\test_compliance_foundation.py`

## Requirements
Write pytest tests for the compliance foundation. Three test classes:

### TestComplianceValidatorUnit (no SSH needed)
- `test_make_result_schema` — verify make_result produces dict with all 8 fields (rule_id, framework, severity, check, passed, expected, actual, evidence, remediation)
- `test_make_result_types` — verify field types (all strings except passed=bool)
- `test_default_rules_loads_fixture` — verify default_rules loads from fixture file

### TestServiceValidatorFallback (no SSH needed, mock)
- `test_systemctl_active` — mock ssh.execute to return "active", verify passes
- `test_pgrep_fallback` — mock systemctl failure + pgrep success, verify passes with pid
- `test_both_fail` — mock both failing, verify fails with "not running"

### TestComplianceLive (requires SSH, mark with `@pytest.mark.live`)
- `test_live_compliance_check` — connect to localhost:2222, load test fixture rules, run validate(), verify results have enhanced schema fields
- `test_live_batch_executor_framework_grouping` — run batch executor with compliance validator, verify by_framework in results

Use conftest.py's existing `ssh_connection` fixture for live tests.

## Acceptance Criteria
- [ ] `framework/_reference/tests/test_compliance_foundation.py` exists
- [ ] File contains `class TestComplianceValidatorUnit`
- [ ] File contains `class TestServiceValidatorFallback`
- [ ] File contains `class TestComplianceLive`
- [ ] File contains `@pytest.mark.live`

## Gates
BUILD-10, TEST-01
