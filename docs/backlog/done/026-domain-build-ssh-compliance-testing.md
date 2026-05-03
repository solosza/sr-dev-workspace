# SSH Platform — Compliance Testing Extension

## Status
Done

## Priority
High — CIQ client contact flagged NIST 800-171 / CMMC 2.0 deadline approaching; this is the delivery vehicle for that work

## Summary
Extend the SSH platform (isagawa-qa/platform-ssh) to support compliance testing against DISA STIG, CIS Benchmarks, FIPS 140-3, and NIST 800-171. Compliance rules are data-driven JSON fixtures injected via conftest.py — same pattern the platform already uses for host_configs.json and the browser platforms use for test_users.json. Per-client config files allow different organizations to define their compliance requirements without changing framework code. The AI generates validators and tests from compliance framework documentation using the existing 5-layer pattern.

## Requirements
- Add compliance-specific validators (L2) following existing validator pattern:
  - STIGValidator — checks per STIG rule ID (V-XXXXX), delegates to ConfigValidator/PackageValidator/ServiceValidator
  - CISValidator — checks per CIS benchmark ID, supports Level 1 and Level 2
  - FIPSValidator — crypto module checks, algorithm verification, FIPS mode enabled
  - NIST800171Validator — maps 110 CUI protection controls to SSH commands
- Compliance rules are JSON fixture data, not hardcoded in validators:
  - `fixtures/compliance/stig-rocky9.json` — STIG rules for Rocky Linux 9
  - `fixtures/compliance/cis-rocky9-l1.json` — CIS Level 1 benchmarks
  - `fixtures/compliance/nist-800-171.json` — 110 controls mapped to checks
  - `fixtures/compliance/fips-140-3.json` — crypto validation checks
- Per-client config files in fixtures:
  - `fixtures/clients/ciq-rlc-pro.json` — CIQ Rocky Linux Pro (host config + which compliance frameworks apply)
  - `fixtures/clients/ciq-rlc-pro-ai.json` — CIQ AI/HPC variant
  - Pattern: any new client = new JSON file, no code changes
- conftest.py loads compliance fixtures and injects via pytest fixtures (same pattern as existing host_configs)
- Check results include compliance metadata (framework, rule ID, severity) alongside existing {check, passed, evidence} format
- Existing validators (PackageValidator, KernelValidator, ServiceValidator, ConfigValidator) remain unchanged — compliance validators compose them
- 5-layer architecture preserved: Test → Role → Task → Validator → SSHInterface
- Reference implementations in `framework/_reference/` for AI generation pattern
- Domain spec updated so `/ssh-workflow` can generate compliance tests from natural language

## References
- SSH platform repo: isagawa-qa/platform-ssh
- SSH platform local master: C:/Users/solos/my_ai_projects/platform-ssh-master/
- Docker spec (structural template): isagawa-co/docker-spec
- Existing compliance domain specs (requirements source): isagawa-co/pci-dss-spec, aml-kyc-spec, sox-audit-spec, incident-response-spec, hipaa-audit-spec, soc-automation-spec
- CIQ client context: Rocky Linux enterprise distributor, serves DoD/federal, NIST 800-171 / CMMC 2.0 deadline approaching
- Industry research: InSpec (4-layer, closest comparable), Testinfra (3-layer), OSCAL (NIST data model for compliance)
- Backlog 020: original SSH platform build

## Task Builder Input
- **Deliverable:** SSH platform with compliance validators, data-driven compliance fixtures, per-client configs, updated conftest.py, reference implementations, and updated domain spec — all committed to isagawa-qa/platform-ssh
- **Scope:** REFACTOR
- **Constraints:** Work in platform-ssh repo (cross-repo from sr-dev-workspace). Existing validators must not break. Existing tests must still pass. First compliance frameworks: DISA STIG + CIS Level 1 + NIST 800-171. FIPS 140-3 can follow. Need actual STIG/CIS rule data to populate fixtures — agent can research from public STIG viewer and CIS documentation. Production testing (L3) requires SSH target — use existing Docker+SSH infrastructure from prod-test skill.
