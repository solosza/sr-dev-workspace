# Backlog Execution — Task Index

Autonomous orchestration of backlog items 029 (job search) and 030 (portfolio site).

## Tasks

| # | Task | Type | Depends On |
|---|------|------|------------|
| 001 | [[001-task-builder-029.md]] | BUILD | — |
| 002 | [[002-task-builder-030.md]] | BUILD | — |
| 003 | [[003-execute-ai-job-search.md]] | BUILD | 001 |
| 004 | [[004-execute-portfolio-site.md]] | BUILD | 002 |

## Flow

```
001 (task-builder 029) → 003 (run-task.sh ai-job-search)
002 (task-builder 030) → 004 (run-task.sh portfolio-site)
```

## Constraints

- Tasks 001 and 002 invoke /kernel/task-builder but STOP after step 8 (write tasks only, no auto-execute)
- Tasks 003 and 004 execute the resulting task folders via run-task.sh
- Each subtask inside 003/004 gets its own one-shot agent with fresh context
