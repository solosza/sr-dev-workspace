# Anchor Integrity — Task Index

## Goal
Add protocol hash verification to the anchor system so that `anchored: true` is machine-verified, not self-reported.

## Source
> [[docs/backlog/037-kernel-fix-anchor-integrity.md]]

## Approach
Protocol hash — anchor command computes SHA-256 of the protocol file, writes hash + timestamp to state. Hook verifies the hash matches current protocol content before allowing work.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-edit-anchor-command]] | BUILD | none | pending |
| 002 | [[002-build-edit-gate-enforcer]] | BUILD | none | pending |
| 003 | [[003-test-l1-verify-changes]] | TEST | 001, 002 | pending |
| 004 | [[004-test-l2-hook-smoke-test]] | TEST | 002 | pending |
| 005 | [[005-test-l3-full-anchor-cycle]] | TEST | 001, 002 | pending |

## Gate Contract
> [[gate-contract.md]]
