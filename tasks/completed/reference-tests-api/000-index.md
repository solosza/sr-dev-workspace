# Task Index — 213 _reference API Tests (V2 Exit Gate)

Backlog: docs/backlog/213-qa-build-reference-tests-api.md
Branch: build/213-qa-build-reference-tests-api (from main 94f87f9+) — MERGE HELD until 208 green (orchestrator enforces; not this pipeline's concern)
Design: projects/hmsa-qa-platform/02-reference-patterns/tests-api.md (GOVERNING; lexicon pre-swept clean) + 5-layer-contract.md L5

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-api-test-exemplar]] | BUILD | 001 |
| 003 | [[003-test-contract-semantics-ast]] | TEST | 002 |
| 004 | [[004-test-run-suite-live]] | TEST | 003 |
| 005 | [[005-build-commit-branch]] | BUILD | 004 |

Gate contract: [[gate-contract]]
