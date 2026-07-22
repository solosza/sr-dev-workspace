# Task Index — 209 Orderly Harness API Slice (V2 first)

Backlog: docs/backlog/209-qa-build-harness-api-slice.md
Branch: build/209-qa-build-harness-api-slice (target repo)
Design: projects/hmsa-qa-platform/04-test-harness/harness-app.md (V2 slice) + data-model.md (statuses, entities)

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-api-customers-routes]] | BUILD | 001 |
| 003 | [[003-build-api-orders-routes]] | BUILD | 001 |
| 004 | [[004-build-register-api-routers]] | BUILD | 002, 003 |
| 005 | [[005-test-api-smoke]] | TEST | 004 |
| 006 | [[006-test-api-e2e-live]] | TEST | 005 |
| 007 | [[007-build-commit-branch]] | BUILD | 006 |

Gate contract: [[gate-contract]]
