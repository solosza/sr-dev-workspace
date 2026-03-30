# SSH Image Testing Platform for CIQ — Task Index

## Goal
Build a new QA platform (isagawa-qa/platform-ssh) that tests OS images via SSH interface, adapted for CIQ's Rocky Linux products.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-ssh-research-ciq-products]] | RESEARCH | none | pending |
| 002 | [[002-ssh-build-repo-scaffolding]] | BUILD | 001 | pending |
| 003 | [[003-ssh-build-interface-layer]] | BUILD | 002 | pending |
| 004 | [[004-ssh-build-validators]] | BUILD | 003 | pending |
| 005 | [[005-ssh-build-tasks-roles]] | BUILD | 003, 004 | pending |
| 006 | [[006-ssh-build-tests-fixtures]] | BUILD | 004, 005 | pending |
| 007 | [[007-ssh-build-domain-spec]] | BUILD | 002 | pending |
| 008 | [[008-ssh-test-dry-run]] | TEST | 003, 004, 005, 006 | pending |
| 009 | [[009-ssh-test-kernel-integration]] | TEST | 007, 008 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- New repo with SSH interface + CIQ-adapted test suites
- 5-layer framework (_reference/ with all layers)
- Kernel domain spec (SKILL.md + workflow + gate-contract)
- Passing test suite (dry-run or against real CIQ image)
- Validation report at `_test/validation-report.json`
