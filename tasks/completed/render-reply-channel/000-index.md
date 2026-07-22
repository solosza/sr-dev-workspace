# Task Index — 233 Render v2 Reply Channel

Backlog: docs/backlog/233-kernel-build-render-reply-channel.md
Governing spec: .claude/docs/design/render/references/annotation-contract.md — "Reply Channel (v2)"
Location: workspace:.claude/skills/render/ (no branch — tests use temp dirs/copies; DO NOT touch the live session on port 52105)

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-server-status-route]] | BUILD | — |
| 002 | [[002-build-page-reply-rendering]] | BUILD | — |
| 003 | [[003-build-template-md-v2]] | BUILD | 002 |
| 004 | [[004-build-skill-docs-v2]] | BUILD | — |
| 005 | [[005-test-server-v2]] | TEST | 001 |
| 006 | [[006-test-page-v2]] | TEST | 002 |
| 007 | [[007-test-full-circle-e2e]] | TEST | 005, 006 |

Gate contract: [[gate-contract]]
