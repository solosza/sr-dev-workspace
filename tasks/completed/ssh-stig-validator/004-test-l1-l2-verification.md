# 004 — L1+L2 Structural and Import Verification

**Type:** TEST
**Depends on:** 001, 002, 003

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`

## Requirements
Run all BUILD gates and FUNC gates from gate contract:

```bash
# L1 structural
test -f framework/_reference/fixtures/stig_rules.json
test -f framework/_reference/validators/stig_validator.py
test -f framework/_reference/tests/test_stig_validator.py
grep -q 'class STIGValidator' framework/_reference/validators/stig_validator.py
grep -q 'ComplianceValidator' framework/_reference/validators/stig_validator.py

# L2 functional
python -c "import json; json.load(open('framework/_reference/fixtures/stig_rules.json'))"
python -c "import sys; sys.path.insert(0,'framework/_reference'); from validators.stig_validator import STIGValidator"
```

All must exit 0.

## Acceptance Criteria
- [ ] All 7 checks pass (exit 0)

## Gates
BUILD-01 through BUILD-06, FUNC-01
