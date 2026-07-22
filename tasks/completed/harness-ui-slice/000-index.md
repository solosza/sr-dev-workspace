# Orderly Harness UI Slice — Task Index

## Goal
Build the Orderly demo app's UI slice (FastAPI + Jinja2 + SQLite, orders domain, data-testid convention) per the harness design docs, on branch build/202-qa-build-harness-ui-slice. GENERIC COMMERCE — no healthcare vocabulary anywhere.

## Design Sources (read before building)
- projects/hmsa-qa-platform/04-test-harness/harness-app.md (stack, V1 slice, conventions)
- projects/hmsa-qa-platform/04-test-harness/data-model.md (entities, statuses)

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-feature-branch]] | BUILD | none | pending |
| 002 | [[002-build-db-layer]] | BUILD | 001 | pending |
| 003 | [[003-build-seed-script]] | BUILD | 002 | pending |
| 004 | [[004-build-app-entry-login]] | BUILD | 002 | pending |
| 005 | [[005-build-login-template]] | BUILD | 004 | pending |
| 006 | [[006-build-customer-routes]] | BUILD | 004 | pending |
| 007 | [[007-build-customer-template]] | BUILD | 006 | pending |
| 008 | [[008-build-order-routes]] | BUILD | 004 | pending |
| 009 | [[009-build-orders-template]] | BUILD | 008 | pending |
| 010 | [[010-build-order-detail-template]] | BUILD | 008 | pending |
| 011 | [[011-test-smoke-boot]] | TEST | 003, 005, 007, 009, 010 | pending |
| 012 | [[012-test-testid-audit]] | TEST | 005, 007, 009, 010 | pending |
| 013 | [[013-test-seed-determinism]] | TEST | 003 | pending |
| 014 | [[014-build-commit-branch]] | BUILD | 011, 012, 013 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `harness/orderly/` app in target repo: runnable via `uvicorn` on port 8017, seeded, all pages rendering, every interactive element carrying data-testid
