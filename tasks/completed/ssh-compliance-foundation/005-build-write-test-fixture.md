# 005 — Write Compliance Test Fixture

**Type:** BUILD
**Depends on:** —

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\fixtures\compliance_rules_test.json`

## Requirements
Write a test fixture with sample compliance rules for testing the base ComplianceValidator. Use a small set of rules (~5) that exercise all check types:

```json
[
  {
    "rule_id": "TEST-001",
    "check_type": "config_value",
    "file": "/etc/ssh/sshd_config",
    "directive": "PermitRootLogin",
    "expected": "no",
    "severity": "high",
    "remediation": "Set PermitRootLogin no in /etc/ssh/sshd_config"
  },
  {
    "rule_id": "TEST-002",
    "check_type": "config_absent",
    "file": "/etc/ssh/sshd_config",
    "directive": "PermitEmptyPasswords yes",
    "severity": "critical",
    "remediation": "Remove PermitEmptyPasswords yes from sshd_config"
  },
  {
    "rule_id": "TEST-003",
    "check_type": "package_installed",
    "package": "openssh-server",
    "severity": "high",
    "remediation": "Install openssh-server"
  },
  {
    "rule_id": "TEST-004",
    "check_type": "service_status",
    "service": "sshd",
    "expected_status": "active",
    "severity": "high",
    "remediation": "Start sshd service"
  },
  {
    "rule_id": "TEST-005",
    "check_type": "config_value",
    "file": "/etc/ssh/sshd_config",
    "directive": "Protocol",
    "expected": "2",
    "severity": "critical",
    "remediation": "Set Protocol 2 in /etc/ssh/sshd_config"
  }
]
```

## Acceptance Criteria
- [ ] `framework/_reference/fixtures/compliance_rules_test.json` exists
- [ ] File is valid JSON
- [ ] Contains at least 4 rules with different `check_type` values

## Gates
BUILD-09, FUNC-04
