# Minimalize Kernel — Task Index

## Goal
Establish feature freeze policy and strip non-governance items from the kernel. The kernel governs. It does not build, test, deploy, or orchestrate.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-kernel-build-feature-freeze-policy]] | BUILD | none | pending |
| 002 | [[002-kernel-refactor-strip-extensions-from-claudemd]] | REFACTOR | 001 | pending |
| 003 | [[003-kernel-refactor-document-core-vs-extension]] | BUILD | 001 | pending |
| 004 | [[004-kernel-test-verify-minimal-kernel]] | TEST | 002, 003 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- Feature freeze policy document
- CLAUDE.md stripped to core governance only
- Core vs extension classification document
- Verification that minimal kernel is complete and consistent
