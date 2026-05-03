# 001 — Write ComplianceValidator Base Class

**Type:** BUILD
**Depends on:** —

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\validators\compliance_validator.py`

## Requirements
Write the abstract base class that all 8 framework validators will inherit from. Must include:

- `FRAMEWORK = ""` and `FRAMEWORK_ID = ""` class attributes
- `__init__(self, ssh, rules=None)` constructor
- `default_rules(self)` method that loads from fixture file
- `check_config_value(self, file, directive, expected, rule_id, severity)` — grep config file, parse actual value
- `check_config_absent(self, file, directive, rule_id, severity)` — verify directive not present
- `check_package_installed(self, package, rule_id, severity)` — `rpm -q` check
- `check_service_status(self, service, expected_status, rule_id, severity)` — systemctl + pgrep fallback
- `make_result(self, rule_id, check, passed, expected, actual, evidence, severity, remediation)` — produce enhanced result dict
- `validate(self)` — run all rules, return list of results

Enhanced result schema per `make_result`:
```json
{
  "rule_id": "STIG-001",
  "framework": "DISA STIG",
  "severity": "high",
  "check": "PermitRootLogin must be no",
  "passed": false,
  "expected": "no",
  "actual": "yes",
  "evidence": "PermitRootLogin yes",
  "remediation": "Set PermitRootLogin no in /etc/ssh/sshd_config"
}
```

Rules are data-driven: `validate()` iterates `self.rules`, dispatches to the correct `check_*` method based on `check_type` field.

## Acceptance Criteria
- [ ] `framework/_reference/validators/compliance_validator.py` exists
- [ ] File contains `class ComplianceValidator`
- [ ] File contains `FRAMEWORK =` class attribute
- [ ] File contains `def make_result`
- [ ] File contains `def check_config_value`
- [ ] File contains `def validate`

## Gates
BUILD-01, BUILD-02, BUILD-03, BUILD-04, BUILD-05
