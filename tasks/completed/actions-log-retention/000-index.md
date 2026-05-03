# Actions-Log Retention — Task Index

## Goal
Make the actions log an append-only audit trail by moving it to a separate JSONL file with retention policy and hook enforcement.

## Source
> [[docs/backlog/038-kernel-fix-actions-log-retention.md]]

## Approach
Separate log file — move actions log from `actions_log` array in session_state.json to `.claude/state/actions.jsonl` as append-only. Hook appends one JSON line per action. Anchor reads from JSONL for review, archives to daily log, then truncates. Retention: 200-line cap in actions.jsonl.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-edit-appender-hook]] | BUILD | none | pending |
| 002 | [[002-build-edit-anchor-command]] | BUILD | none | pending |
| 003 | [[003-build-edit-gate-enforcer-log-read]] | BUILD | none | pending |
| 004 | [[004-test-l1-verify-changes]] | TEST | 001, 002, 003 | pending |
| 005 | [[005-test-l2-hook-smoke-test]] | TEST | 001 | pending |
| 006 | [[006-test-l3-appender-writes-jsonl]] | TEST | 001 | pending |

## Gate Contract
> [[gate-contract.md]]
