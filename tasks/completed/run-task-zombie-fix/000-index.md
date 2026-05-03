# Run-Task Zombie Process Fix — Task Index

**Backlog:** `docs/backlog/050-kernel-fix-run-task-zombie-processes.md`
**Deliverable:** Working `run-task.sh` + `lib/common.sh` on Windows
**Scope:** BUILD
**Tasks:** 9

## Task List

| # | Type | Task | Gates |
|---|------|------|-------|
| 001 | RESEARCH | Audit current fix state against backlog requirements | FUNC-01 |
| 002 | BUILD | Fix output capture reliability on Windows | BUILD-01 |
| 003 | BUILD | Fix process tree cleanup on Windows | BUILD-02 |
| 004 | BUILD | Fix loop exit after ALL_TASKS_COMPLETE | BUILD-03 |
| 005 | BUILD | Add pipeline-run log namespacing | BUILD-04 |
| 006 | BUILD | Add graceful shutdown with SIGTERM propagation | BUILD-05 |
| 007 | TEST | L1: Verify all fixes present in source | BUILD-01..05 |
| 008 | TEST | L2: Dry-run syntax validation on Windows | FUNC-02 |
| 009 | TEST | L3: Live test with a simple task folder | FUNC-03 |
