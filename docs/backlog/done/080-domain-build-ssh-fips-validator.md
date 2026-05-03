# SSH FIPS 140-3 Validator

## Status
Open

## Priority
Medium — required for federal cryptographic compliance

## Summary
Build a FIPS 140-3 validator for SSH cryptographic compliance against Rocky Linux 9. Implements ~8 rules covering approved ciphers, MACs, key exchange algorithms, and FIPS mode enforcement. Produces enhanced results with rule IDs (FIPS-001 through FIPS-008), severity levels, and remediation guidance.

## Requirements
- Inherit from `ComplianceValidator` base class (backlog 076)
- Load rules from `fixtures/fips_rules.json`
- Cover FIPS 140-3 cryptographic requirements for SSH
- Check cipher suites, MACs, KexAlgorithms against FIPS-approved lists
- Check FIPS mode enabled (`fips-mode-setup --check` or `/proc/sys/crypto/fips_enabled`)
- Framework ID: `fips`, Framework name: `FIPS 140-3`
- Pytest tests that validate against live SSH target

## References
- Backlog 076 (foundation) — must be built first
- FIPS 140-3 approved algorithms list
- Rocky Linux 9 FIPS mode documentation
- Showcase page claims FIPS-001 through FIPS-008

## Task Builder Input
- **Deliverable:** FIPSValidator class + fixture + tests
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test
- **Scope:** BUILD
- **Constraints:** Depends on backlog 076 (ComplianceValidator base class must exist first)
