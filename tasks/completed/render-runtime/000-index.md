# Task Index — 232 Render Runtime

Backlog: docs/backlog/232-kernel-build-render-runtime.md
Location: workspace:.claude/skills/render/ (NO feature branch — tests must be non-destructive: temp session dirs, COPIES of state data)
Design: .claude/docs/design/render/ (governing; annotation schema FROZEN per annotation-contract.md)

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-render-server]] | BUILD | — |
| 002 | [[002-build-review-board-template-md]] | BUILD | — |
| 003 | [[003-build-review-board-generate]] | BUILD | 002 |
| 004 | [[004-research-lavish-adoption-read]] | RESEARCH | — |
| 005 | [[005-test-server-cycle]] | TEST | 001 |
| 006 | [[006-test-ast-semantics]] | TEST | 001, 003 |
| 007 | [[007-test-closed-loop-e2e]] | TEST | 005, 006 |

Gate contract: [[gate-contract]]
