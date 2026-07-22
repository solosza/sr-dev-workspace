# Task Index — 211 _reference API Objects (V2 Layer 2)

Backlog: docs/backlog/211-qa-build-reference-api-objects.md
Branch: build/211-qa-build-reference-api-objects (target repo)
Design: projects/hmsa-qa-platform/02-reference-patterns/api-objects.md (GOVERNING — read canonical examples before writing anything) + 5-layer-contract.md L2 rules

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-create-feature-branch]] | BUILD | — |
| 002 | [[002-build-pydantic-models]] | BUILD | 001 |
| 003 | [[003-build-orders-api-object]] | BUILD | 002 |
| 004 | [[004-build-soap-object-exemplar]] | BUILD | 002 |
| 005 | [[005-test-contract-semantics-ast]] | TEST | 003, 004 |
| 006 | [[006-test-l2-l3-live]] | TEST | 005 |
| 007 | [[007-build-commit-branch]] | BUILD | 006 |

Gate contract: [[gate-contract]]
