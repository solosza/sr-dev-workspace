# 003 — Write STIG Validator Tests

**Type:** BUILD
**Depends on:** 001, 002

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\tests\test_stig_validator.py`

## Requirements
Write pytest tests for the STIG validator.

### TestSTIGValidatorUnit (no SSH needed)
- `test_framework_attributes` — verify FRAMEWORK = "DISA STIG" and FRAMEWORK_ID = "stig"
- `test_default_rules_loads_fixture` — verify default_rules() returns list with 15 rules
- `test_rule_ids_prefix` — verify all rule IDs start with "STIG-"

### TestSTIGValidatorLive (requires SSH, mark with `@pytest.mark.live`)
- `test_live_stig_validation` — connect to localhost:2222, run validate(), verify results are list of dicts with enhanced schema fields (rule_id, framework, severity, etc.)
- `test_live_stig_result_count` — verify 15 results returned

Use a mock SSH object for unit tests. Use conftest.py ssh_connection fixture for live tests.

## Acceptance Criteria
- [ ] `framework/_reference/tests/test_stig_validator.py` exists
- [ ] File contains `class TestSTIGValidatorUnit`
- [ ] File contains `class TestSTIGValidatorLive`

## Gates
BUILD-06
