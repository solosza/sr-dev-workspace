# 008 — L2 Import and Functional Verification

**Type:** TEST
**Depends on:** 007

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`

## Requirements
Verify all FUNC gates. Run each check from the gate contract (FUNC-01 through FUNC-04) plus the existing test regression check (FUNC-05).

Commands to run (all from the target repo root):
```bash
python -c "import sys; sys.path.insert(0,'framework/_reference'); from validators.compliance_validator import ComplianceValidator"
python -c "import sys; sys.path.insert(0,'framework/_reference'); from validators.service_validator import ServiceValidator"
python -c "import sys; sys.path.insert(0,'framework/_reference'); from roles.ssh_batch_executor import SSHBatchExecutor"
python -c "import json; json.load(open('framework/_reference/fixtures/compliance_rules_test.json'))"
pytest framework/_reference/tests/test_ssh_batch.py -v --rootdir=.
```

All must exit 0.

## Acceptance Criteria
- [ ] All 4 import checks pass (exit 0)
- [ ] Existing test suite still passes (no regressions)

## Gates
FUNC-01 through FUNC-05
