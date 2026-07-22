# Task Index — 207 _reference UI Roles (COPY-FIRST)

Backlog: docs/backlog/207-qa-build-reference-roles-ui.md
Branch: build/207-qa-build-reference-roles-ui (target repo)
Copy source: D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/roles/ + tasks/ login shape (own IP)
Design: projects/hmsa-qa-platform/02-reference-patterns/roles-ui.md (governs divergence)

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-common-tasks]] | BUILD | 001 |
| 003 | [[003-build-order-clerk-role]] | BUILD | 002 |
| 004 | [[004-build-order-manager-role]] | BUILD | 002 |
| 005 | [[005-test-contract-semantics-ast]] | TEST | 002, 003, 004 |
| 006 | [[006-test-sequence-spy]] | TEST | 003, 004 |
| 007 | [[007-test-live-env-gated]] | TEST | 005, 006 |
| 008 | [[008-build-commit-branch]] | BUILD | 007 |

Gate contract: [[gate-contract]]
