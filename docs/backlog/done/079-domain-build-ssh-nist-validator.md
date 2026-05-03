# SSH NIST 800-171 Validator

## Status
Open

## Priority
Medium — required for government contractor compliance

## Summary
Build a NIST 800-171 validator for SSH hardening checks against Rocky Linux 9. Implements ~10 rules covering access control (3.1.x), identification/authentication (3.5.x), and system protection (3.13.x) families. Produces enhanced results with rule IDs (NIST-001 through NIST-010), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/nist_rules.json`
- Cover NIST 800-171 Rev 2 controls relevant to SSH
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `nist`, Framework name: `NIST 800-171`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- NIST SP 800-171 Rev 2 families: 3.1 Access Control, 3.5 Identification and Authentication, 3.13 System and Communications Protection

## Task Builder Input
- **Deliverable:** NISTValidator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
