# Task Index — 208 _reference UI Tests (V1 Exit Gate)

Backlog: docs/backlog/208-qa-build-reference-tests-ui.md
Branch: build/208-qa-build-reference-tests-ui (from main 8a23917+) — merge via /kernel/review-queue accept only, never direct to main
Design: projects/hmsa-qa-platform/02-reference-patterns/tests-ui.md (GOVERNING; lexicon swept 2026-07-21) + 5-layer-contract.md L5

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-ui-test-exemplar]] | BUILD | 001 |
| 003 | [[003-test-contract-semantics-ast]] | TEST | 002 |
| 004 | [[004-test-run-suite-live]] | TEST | 003 |
| 005 | [[005-build-commit-branch]] | BUILD | 004 |

Gate contract: [[gate-contract]]
