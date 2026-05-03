# 001 — Write STIG Rules Fixture

**Type:** BUILD
**Depends on:** —

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\fixtures\stig_rules.json`

## Requirements
Write DISA STIG rules for SSH hardening on Rocky Linux 9. ~15 rules covering sshd_config directives mandated by DISA STIG V-series checks.

Rules to include (rule_id STIG-001 through STIG-015):

| Rule ID | check_type | directive | expected | severity |
|---------|-----------|-----------|----------|----------|
| STIG-001 | config_value | PermitRootLogin | no | high |
| STIG-002 | config_value | MaxAuthTries | 4 | medium |
| STIG-003 | config_value | ClientAliveInterval | 600 | medium |
| STIG-004 | config_value | ClientAliveCountMax | 0 | medium |
| STIG-005 | config_value | LoginGraceTime | 60 | medium |
| STIG-006 | config_value | PermitEmptyPasswords | no | high |
| STIG-007 | config_value | X11Forwarding | no | medium |
| STIG-008 | config_value | IgnoreRhosts | yes | medium |
| STIG-009 | config_value | HostbasedAuthentication | no | high |
| STIG-010 | config_value | UsePAM | yes | medium |
| STIG-011 | config_value | StrictModes | yes | medium |
| STIG-012 | config_absent | PermitUserEnvironment yes | | critical |
| STIG-013 | config_value | LogLevel | VERBOSE | medium |
| STIG-014 | service_status | sshd | active | high |
| STIG-015 | package_installed | openssh-server | | high |

Each rule includes `remediation` text describing how to fix.

## Acceptance Criteria
- [ ] `framework/_reference/fixtures/stig_rules.json` exists
- [ ] File is valid JSON with 15 rule objects

## Gates
BUILD-01, BUILD-02
