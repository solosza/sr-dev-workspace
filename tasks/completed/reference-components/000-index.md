# _reference Shared Components — Task Index

## Goal
Build modal_component.py (lead exemplar) + grid_component.py (flagship) per the 2.1.5 design doc — locator-contract injection, EXACTLY two components (set deferred) — on branch build/205-qa-build-reference-components.

## Design Sources (read before building)
- projects/hmsa-qa-platform/02-reference-patterns/shared-components.md (canonical GridLocators/GridComponent examples + membership rules)
- framework/_reference/pages/orders_page.py on the branch — its grid/modal locator VALUE constants (built in 204) are what fixtures inject
- framework/docs/5-layer-contract.md (L2 rules incl. v2.3 rule-1 injection clause)

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-feature-branch]] | BUILD | none | pending |
| 002 | [[002-build-modal-component]] | BUILD | 001 | pending |
| 003 | [[003-build-grid-component]] | BUILD | 001 | pending |
| 004 | [[004-build-locator-configs]] | BUILD | 002, 003 | pending |
| 005 | [[005-test-contract-semantics-ast]] | TEST | 002, 003, 004 | pending |
| 006 | [[006-test-live-against-orderly]] | TEST | 002, 003, 004 | pending |
| 007 | [[007-build-commit-branch]] | BUILD | 005, 006 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- framework/_reference/components/: modal_component.py + grid_component.py (mechanics only, injected identifier configs, genericity scope declared), live-proven on Orderly's real grid + modal
