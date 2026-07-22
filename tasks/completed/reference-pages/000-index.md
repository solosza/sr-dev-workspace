# _reference Pages vs Orderly — Task Index

## Goal
Build _reference/pages/ per the 2.1.1 design doc, locators bound to the REAL Orderly DOM, on branch build/204-qa-build-reference-pages. Gate contract includes the contract-semantics gates from lesson 2026-07-15.

## Design Sources (read before building)
- projects/hmsa-qa-platform/02-reference-patterns/page-objects.md
- framework/docs/5-layer-contract.md in the target repo (L2 rules + Browser addendum)
- The live Orderly templates (harness/orderly/templates/) — locators bind to actual data-testids

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-feature-branch]] | BUILD | none | pending |
| 002 | [[002-build-login-page]] | BUILD | 001 | pending |
| 003 | [[003-build-customers-page]] | BUILD | 001 | pending |
| 004 | [[004-build-orders-page]] | BUILD | 001 | pending |
| 005 | [[005-build-order-detail-page]] | BUILD | 001 | pending |
| 006 | [[006-test-contract-semantics]] | TEST | 002, 003, 004, 005 | pending |
| 007 | [[007-test-live-against-orderly]] | TEST | 002, 003, 004, 005 | pending |
| 008 | [[008-build-commit-branch]] | BUILD | 006, 007 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- framework/_reference/pages/: login_page.py, customers_page.py, orders_page.py, order_detail_page.py — every locator a real Orderly data-testid, contract-compliant, live-tested
