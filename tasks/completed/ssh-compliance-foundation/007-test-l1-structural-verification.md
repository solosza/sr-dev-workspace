# 007 — L1 Structural Verification

**Type:** TEST
**Depends on:** 001, 002, 003, 004, 005, 006

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`

## Requirements
Verify all BUILD gates structurally. Run each check from the gate contract (BUILD-01 through BUILD-10) against the target repo.

Commands to run (all relative to the target repo root):
```bash
test -f framework/_reference/validators/compliance_validator.py
grep -q 'FRAMEWORK =' framework/_reference/validators/compliance_validator.py
grep -q 'def make_result' framework/_reference/validators/compliance_validator.py
grep -q 'def check_config_value' framework/_reference/validators/compliance_validator.py
grep -q 'def validate' framework/_reference/validators/compliance_validator.py
grep -q 'pgrep' framework/_reference/validators/service_validator.py
grep -q 'frameworks' framework/_reference/fixtures/host_configs.json
grep -q 'by_framework' framework/_reference/roles/ssh_batch_executor.py
test -f framework/_reference/fixtures/compliance_rules_test.json
test -f framework/_reference/tests/test_compliance_foundation.py
```

All must exit 0.

## Acceptance Criteria
- [ ] All 10 structural checks pass (exit 0)

## Gates
BUILD-01 through BUILD-10
