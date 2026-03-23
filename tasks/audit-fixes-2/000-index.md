# Audit Fixes Round 2 — Task Index

## Goal
Fix remaining 8 gaps from e2e workflow audit.

## Tasks

| # | Task | Dependencies | Status |
|---|------|-------------|--------|
| 001 | [[001-kernel-fix-counter-off-by-one]] | none | pending |
| 002 | [[002-kernel-fix-test-failure-false-positives]] | none | pending |
| 003 | [[003-kernel-fix-session-start-merge]] | none | pending |
| 004 | [[004-kernel-fix-auto-approve-matcher]] | none | pending |
| 005 | [[005-kernel-fix-context-structured]] | none | pending |
| 006 | [[006-kernel-fix-backlog-in-protocol]] | none | pending |
| 007 | [[007-kernel-fix-remove-deprecated-validate]] | none | pending |
| 008 | [[008-kernel-fix-remove-stale-domain-commands]] | none | pending |

## Deliverables
- Counter off-by-one fixed in universal-gate-enforcer.py
- test-failure-detector.py false positive patterns refined
- session-start.md specifies read→merge→write pattern
- auto-approve matcher narrowed or documented
- context field structured as JSON object
- backlog command added to protocol index
- validate.md removed from CLAUDE.md command tree
- sr_dev-anchor.md and sr_dev-learn.md cleaned up
