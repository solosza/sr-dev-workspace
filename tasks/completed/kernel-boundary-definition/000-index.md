# Kernel Boundary Definition — Task Index

## Goal
Define kernel boundary, create manifest, separate extensions, resolve three-way drift between sr_dev_workspace, isagawa-kernel, and hmsa-healthcare-qa.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-kernel-research-diff-three-repos]] | RESEARCH | none | pending |
| 002 | [[002-kernel-build-kernel-manifest]] | BUILD | 001 | pending |
| 003 | [[003-kernel-build-sync-script]] | BUILD | 002 | pending |
| 004 | [[004-kernel-refactor-strip-extensions]] | BUILD | 002 | pending |
| 005 | [[005-kernel-build-update-domain-setup]] | BUILD | 002 | pending |
| 006 | [[006-kernel-test-verify-boundary]] | TEST | 003, 004, 005 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- kernel-manifest.json in isagawa-kernel root
- kernel-sync.sh script
- Extensions removed from kernel namespace
- domain-setup updated to use manifest
- All three repos aligned on core kernel files
