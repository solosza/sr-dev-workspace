# Task Index — 212 _reference REST Tasks (V2 Layer 3)

Backlog: docs/backlog/212-qa-build-reference-tasks-rest-api.md
Branch: build/212-qa-build-reference-tasks-rest-api (target repo, from main ed5153d+)
Design: projects/hmsa-qa-platform/02-reference-patterns/tasks-rest-api.md (GOVERNING — lexicon pre-swept clean 2026-07-17) + 5-layer-contract.md L3

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-order-management-tasks]] | BUILD | 001 |
| 003 | [[003-test-contract-semantics-ast]] | TEST | 002 |
| 004 | [[004-test-sequence-spy]] | TEST | 002 |
| 005 | [[005-test-l3-live]] | TEST | 003, 004 |
| 006 | [[006-build-commit-branch]] | BUILD | 005 |

Gate contract: [[gate-contract]]
