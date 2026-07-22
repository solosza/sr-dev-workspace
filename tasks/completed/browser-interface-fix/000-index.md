# BrowserInterface Contract Fix — Task Index

## Goal
Fix two contract violations found by orchestrator validation of 203 (branch build/203-qa-build-browser-interface, do NOT create a new branch): 5 exception-swallowing except blocks (error rule 1: catch-log-RERAISE) and 16 screenshot references (screenshots are conftest's job, never the Interface's).

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-fix-error-semantics]] | BUILD | none | pending |
| 002 | [[002-build-remove-screenshot-machinery]] | BUILD | none | pending |
| 003 | [[003-test-rerun-l2-l3]] | TEST | 001, 002 | pending |
| 004 | [[004-build-commit-fix]] | BUILD | 003 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- browser_interface.py contract-compliant: every except re-raises, zero screenshot machinery, L2+L3 still green
