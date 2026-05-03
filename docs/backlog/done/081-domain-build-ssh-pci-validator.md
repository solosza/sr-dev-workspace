# SSH PCI DSS Validator

## Status
Open

## Priority
Medium — required for payment card industry compliance

## Summary
Build a PCI DSS validator for SSH hardening checks against Rocky Linux 9. Implements ~10 rules covering PCI DSS v4.0 requirements for secure remote access, strong cryptography, access control, and audit logging. Produces enhanced results with rule IDs (PCI-001 through PCI-010), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/pci_rules.json`
- Cover PCI DSS v4.0 requirements: Req 2.2 (secure config), Req 4.2 (strong crypto), Req 8.3 (authentication), Req 10.2 (audit trails)
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `pci`, Framework name: `PCI DSS`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- PCI DSS v4.0 Requirements 2, 4, 8, 10

## Task Builder Input
- **Deliverable:** PCIValidator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
