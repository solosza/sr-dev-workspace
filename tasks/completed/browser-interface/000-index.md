# BrowserInterface — Task Index

## Goal
Build Layer 1 BrowserInterface (copy/adapt platform-selenium's clean 674-line implementation) on branch build/203-qa-build-browser-interface, L3-tested against the live Orderly harness.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-feature-branch]] | BUILD | none | pending |
| 002 | [[002-build-write-browser-interface]] | BUILD | 001 | pending |
| 003 | [[003-test-import-and-primitives]] | TEST | 002 | pending |
| 004 | [[004-test-live-against-orderly]] | TEST | 002 | pending |
| 005 | [[005-build-commit-branch]] | BUILD | 002, 003, 004 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `framework/interfaces/browser_interface.py` — contract-compliant, monolith-guarded, proven against the real app
