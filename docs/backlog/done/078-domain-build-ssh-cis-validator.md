# SSH CIS Level 1 Validator

## Status
Open

## Priority
High — CIS benchmarks are the most widely adopted compliance standard

## Summary
Build a CIS Level 1 validator for SSH hardening checks against Rocky Linux 9. Implements ~12 CIS benchmark rules covering access control, authentication settings, logging, and crypto policy. Produces enhanced results with rule IDs (CIS-001 through CIS-012), severity levels, and remediation guidance per CIS benchmark format.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/cis_l1_rules.json`
- Cover CIS Level 1 Section 5.2 (SSH Server Configuration)
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `cis_l1`, Framework name: `CIS L1`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- CIS Rocky Linux 9 Benchmark v1.0 Section 5.2
- Existing `config_validator.py` for grep pattern reference

## Task Builder Input
- **Deliverable:** CISValidator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
