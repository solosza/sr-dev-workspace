# Audit Fixes — Task Index

## Goal
Fix top 3 gaps from e2e workflow audit: actions_log hook, complete.md cycling logic, fix.md cycling guard.

## Tasks

| # | Task | Dependencies | Status |
|---|------|-------------|--------|
| 001 | [[001-kernel-build-actions-log-hook]] | none | pending |
| 002 | [[002-kernel-fix-complete-cycling]] | none | pending |
| 003 | [[003-kernel-fix-autonomous-fix]] | none | pending |

## Deliverables
- `actions-log-appender.py` hook wired and appending to actions_log
- `complete.md` with full cycling state advancement
- `fix.md` with cycling-aware approval gate
