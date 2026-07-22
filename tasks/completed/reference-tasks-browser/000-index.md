# Task Index — 206 _reference Browser Tasks (COPY-FIRST)

Backlog: docs/backlog/206-qa-build-reference-tasks-browser.md
Branch: build/206-qa-build-reference-tasks-browser (target repo)
Copy source: D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/tasks/ (own IP)
Design: projects/hmsa-qa-platform/02-reference-patterns/tasks-browser.md (governs divergence)

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-order-workup-tasks]] | BUILD | 001 |
| 003 | [[003-test-contract-semantics-ast]] | TEST | 002 |
| 004 | [[004-test-sequence-spy]] | TEST | 002 |
| 005 | [[005-test-live-env-gated]] | TEST | 003, 004 |
| 006 | [[006-build-commit-branch]] | BUILD | 005 |

Gate contract: [[gate-contract]]
