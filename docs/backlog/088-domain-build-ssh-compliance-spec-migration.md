# SSH Compliance Spec Migration — Phase 1 Implementation

## Status
Open

## Priority
High — Unblocks universal validator system (backlog 089) and completes hybrid architecture implementation

## Summary

Migrate SSH compliance infrastructure from research phase (backlog 085) to public platform-ssh spec. Execute Phase 1 of hybrid architecture: ship all 8 fixture JSON files (authoritative compliance data), base ComplianceValidator class + ONE example (STIGValidator), ONE example test (test_stig_validator.py), and enhanced orchestrator. Agent generates remaining 7 validators from pattern on first run. Enables modular compliance testing across 8 frameworks (STIG, CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001) with 88 rules.

---

## Design Documents

| Document | Purpose |
|----------|---------|
| [[088-domain-build-ssh-compliance-spec-migration/phase-01-spec-updates]] | Add validators, fixtures, tests, orchestrator enhancements to platform-ssh |
| [[088-domain-build-ssh-compliance-spec-migration/phase-02-validation]] | Validate spec generates correctly using /kernel/prod-test |
| [[088-domain-build-ssh-compliance-spec-migration/phase-03-sync]] | Sync updated spec back to platform-ssh-test |

---

## Architecture Overview

### Hybrid Approach (Option C)

**Ship as-is (data, not code):**
- All 8 framework rule JSONs (fixtures/) — authoritative compliance data, 88 rules total
- Covers: STIG, CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001

**Ship as templates (code):**
- Base `ComplianceValidator` class (validators/compliance_validator.py)
- ONE example validator: `STIGValidator` (validators/stig_validator.py)
- ONE example test: `test_stig_validator.py`

**Agent pattern (generated on first run):**
- Remaining 7 validators (CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001)
- Teaches agent to extend framework without spec updates

### What Gets Modified

| File | Change | Rationale |
|------|--------|-----------|
| `validators/compliance_validator.py` | NEW — base class | Template for agent to generate remaining validators |
| `validators/stig_validator.py` | NEW — example | Demonstrates pattern |
| `fixtures/stig_rules.json` | NEW — ship as-is | Authoritative rules, immutable reference |
| `fixtures/cis_l1_rules.json` | NEW — ship as-is | Authoritative rules |
| `fixtures/nist_rules.json` | NEW — ship as-is | Authoritative rules |
| `fixtures/fips_rules.json` | NEW — ship as-is | Authoritative rules |
| `fixtures/pci_dss_rules.json` | NEW — ship as-is | Authoritative rules |
| `fixtures/hipaa_rules.json` | NEW — ship as-is | Authoritative rules |
| `fixtures/soc2_rules.json` | NEW — ship as-is | Authoritative rules |
| `fixtures/iso27001_rules.json` | NEW — ship as-is | Authoritative rules |
| `tests/test_stig_validator.py` | NEW — example | Test template for agent |
| `ssh_batch_executor.py` | EDIT — add by_framework grouping | Organize validators by framework |
| `host_configs.json` | EDIT — add frameworks field | Enable framework selection per host |
| `workflow.md` step-03 to step-05 | EDIT — reference compliance validators | Document compliance validation flow |

---

## High-Level Flow

```
Phase 0: Git Setup
  └─ Create feature branch (e.g., feature/088-ssh-compliance-migration)

Phase 1: Update spec
  ├─ Copy 8 fixture JSONs to validators/fixtures/
  ├─ Write validators/compliance_validator.py (base class)
  ├─ Write validators/stig_validator.py (example)
  ├─ Write tests/test_stig_validator.py (example test)
  ├─ Edit ssh_batch_executor.py: add by_framework grouping
  ├─ Edit host_configs.json: add frameworks field
  └─ Edit workflow.md: document compliance flow

Phase 2: Validate
  └─ Run /kernel/prod-test on platform-ssh
     ├─ Verify spec structure correct
     ├─ Verify fixtures load
     ├─ Verify validators instantiate
     └─ Run L1/L2/L3 tests

Phase 3: Sync
  └─ Pull updated spec from platform-ssh to platform-ssh-test
     ├─ Merge fixtures
     ├─ Merge validators
     ├─ Run integration tests
     └─ Confirm agent can generate remaining 7 validators

Phase 4: Merge
  └─ Merge feature branch to origin/main after all testing passes
```

---

## Acceptance Criteria

- [ ] Phase 0: Feature branch created (e.g., feature/088-ssh-compliance-migration)
- [ ] Phase 1 all 8 fixtures shipped to `validators/fixtures/`
- [ ] Phase 1 compliance_validator.py created (base class pattern)
- [ ] Phase 1 stig_validator.py created (example)
- [ ] Phase 1 test_stig_validator.py created (example test)
- [ ] Phase 1 ssh_batch_executor.py enhanced with by_framework grouping
- [ ] Phase 1 host_configs.json enhanced with frameworks field
- [ ] Phase 1 workflow.md updated (steps 03-05 reference compliance validators)
- [ ] Phase 2 prod-test passes (spec generates correctly)
- [ ] Phase 2 all 8 fixtures load in test environment
- [ ] Phase 2 base validator and example instantiate without errors
- [ ] Phase 2 example test passes
- [ ] Phase 3 spec synced back to platform-ssh-test
- [ ] Phase 3 integration tests pass
- [ ] Phase 3 agent can generate CIS validator from pattern (proof of concept)
- [ ] Phase 4: All tests pass and feature branch merged to origin/main

---

## Research Reference

Research completed in backlog 085:
- Decision: Hybrid approach (Option C) chosen over fully-shipped or fully-generated alternatives
- Architecture: Fixtures (ship as-is) + Template (base class) + Pattern (example) + Agent (generates rest)
- Rationale: Fixtures are authoritative (88 rules across 8 frameworks) — ship immutable; Validators are trivial 10-line implementations — safe to generate; Teaches agent to extend without spec updates

See: `projects/kernel-architecture/ssh-compliance-spec-decomposition.md`

---

## Task Builder Input

- **Deliverable:** Public platform-ssh spec updated with compliance infrastructure (Phase 1: fixtures, base validator, example validator + test, orchestrator enhancements; Phase 2: validation via prod-test; Phase 3: sync to platform-ssh-test)
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\platform-ssh`
- **Scope:** BUILD
- **Constraints:**
  - Phase 1 deliverables must be exact copies of fixtures from platform-ssh-test (byte-identical)
  - Base ComplianceValidator class pattern must match format in platform-ssh-test
  - stig_validator.py must be pedagogically clear (teaches the agent)
  - Phase 2 validation uses /kernel/prod-test (modular, reusable)
  - Phase 3 sync must verify agent can generate CIS validator as proof of concept

---

## References

- Backlog 085: SSH Compliance Spec Decomposition — completed research, hybrid decision, migration plan
- File: `projects/kernel-architecture/ssh-compliance-spec-decomposition.md` — full architecture docs
- Backlog 089: Universal Hook Validator System — depends on this migration for reference implementation
- Validator research: 13 validators, 88 rules across 8 frameworks in platform-ssh-test
