# SSH HIPAA Validator

## Status
Open

## Priority
Medium — required for healthcare data protection compliance

## Summary
Build a HIPAA validator for SSH hardening checks against Rocky Linux 9. Implements ~10 rules covering HIPAA Technical Safeguards: access control (164.312a), audit controls (164.312b), integrity (164.312c), person authentication (164.312d), and transmission security (164.312e). Produces enhanced results with rule IDs (HIPAA-001 through HIPAA-010), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/hipaa_rules.json`
- Cover HIPAA Technical Safeguards mapped to SSH configuration
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `hipaa`, Framework name: `HIPAA`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- HIPAA Security Rule 45 CFR 164.312

## Task Builder Input
- **Deliverable:** HIPAAValidator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
