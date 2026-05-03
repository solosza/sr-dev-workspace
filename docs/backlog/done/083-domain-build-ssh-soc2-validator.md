# SSH SOC 2 Validator

## Status
Open

## Priority
Medium — required for SaaS and cloud service provider compliance

## Summary
Build a SOC 2 validator for SSH hardening checks against Rocky Linux 9. Implements ~10 rules covering SOC 2 Trust Services Criteria: security (CC6/CC7), availability, and confidentiality controls as they apply to SSH configuration. Produces enhanced results with rule IDs (SOC2-001 through SOC2-010), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/soc2_rules.json`
- Cover SOC 2 Type II controls mapped to SSH configuration
- Focus areas: logical access (CC6.1-CC6.3), system operations (CC7.1-CC7.2), change management
- Each rule has: rule_id, check_type, file, directive, expected, severity, remediation
- Framework ID: `soc2`, Framework name: `SOC 2`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- AICPA SOC 2 Trust Services Criteria (CC6, CC7)

## Task Builder Input
- **Deliverable:** SOC2Validator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
