# SSH DISA STIG Validator

## Status
Open

## Priority
High — first framework validator, proves the compliance architecture works

## Summary
Build a DISA STIG validator for SSH hardening checks against Rocky Linux 9. Implements ~15 STIG rules covering PermitRootLogin, Protocol, MaxAuthTries, ClientAliveInterval, Banner, and other DISA-mandated SSH settings. Produces enhanced results with rule IDs (STIG-001 through STIG-015), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/stig_rules.json`
- Cover DISA STIG V-series checks for sshd_config
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `stig`, Framework name: `DISA STIG`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- DISA STIG for RHEL 9 SSH: V-257844 through V-258000 series
- Existing `config_validator.py` for grep pattern reference
- Showcase page claims STIG-001 through STIG-015

## Task Builder Input
- **Deliverable:** STIGValidator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
