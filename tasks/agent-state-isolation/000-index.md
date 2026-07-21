# Task Index — 244 Per-Agent Session-State Isolation

Backlog: docs/backlog/244-kernel-build-agent-state-isolation.md
Design: projects/kernel-ephemeral-subagents-research/03-integration-design.md + external review items 25/26
Execution: worktree pipeline — all edits land on the worktree branch; merge via /kernel/review-queue accept

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-write-identity-model-doc]] | BUILD | — |
| 002 | [[002-build-export-agent-id-runtask]] | BUILD | 001 |
| 003 | [[003-build-seed-agent-session-state]] | BUILD | 002 |
| 004 | [[004-build-write-atomic-state-helper]] | BUILD | 001 |
| 005 | [[005-build-route-universal-enforcer]] | BUILD | 004 |
| 006 | [[006-build-route-domain-enforcer]] | BUILD | 004 |
| 007 | [[007-build-route-actions-appender]] | BUILD | 004 |
| 008 | [[008-build-route-test-failure-detector]] | BUILD | 004 |
| 009 | [[009-build-update-session-start-doc]] | BUILD | 005 |
| 010 | [[010-build-update-anchor-doc]] | BUILD | 005 |
| 011 | [[011-test-l1-routing-present]] | TEST | 010 |
| 012 | [[012-test-l2-routing-and-atomicity]] | TEST | 011 |
| 013 | [[013-test-l3-concurrent-isolation]] | TEST | 012 |

Gate contract: [[gate-contract]]
