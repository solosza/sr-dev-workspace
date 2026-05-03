# SSH ISO 27001 Validator

## Status
Open

## Priority
Medium — required for international information security compliance

## Summary
Build an ISO 27001 validator for SSH hardening checks against Rocky Linux 9. Implements ~10 rules covering ISO 27001:2022 Annex A controls: access control (A.9), cryptography (A.10), communications security (A.13), and operations security (A.12) as they apply to SSH configuration. Produces enhanced results with rule IDs (ISO-001 through ISO-010), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/iso27001_rules.json`
- Cover ISO 27001:2022 Annex A controls mapped to SSH configuration
- Focus areas: A.9.1 access control policy, A.9.4 system access control, A.10.1 cryptographic controls, A.13.1 network security
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `iso27001`, Framework name: `ISO 27001`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- ISO/IEC 27001:2022 Annex A controls

## Task Builder Input
- **Deliverable:** ISO27001Validator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
