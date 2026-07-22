# Review Queue — Workflow

## Phases

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Discover | Glob done/, read review state, compute diff | Unreviewed items list | — |
| 2. Present | Sort by priority, format review card | Formatted review card | — |
| 3. Act | Parse and execute user action | Action result | **User selects action** |
| 4. Update State | Write transition to review-status.json | Updated state file | — |
| 5. Report | Compute stats, show next item or summary | Stats report | — |

## State Schema

State is tracked in `.claude/state/review-status.json`:

```json
{
  "reviewed": {
    "NNN": {
      "status": "accepted | needs-iteration | rejected | deferred",
      "reviewed_at": "ISO timestamp",
      "notes": "optional user notes",
      "followup_backlog": "NNN or null"
    }
  },
  "stats": {
    "total_completed": 0,
    "reviewed": 0,
    "unreviewed": 0,
    "accepted": 0,
    "needs_iteration": 0,
    "rejected": 0,
    "deferred": 0
  }
}
```

## State Machine

```
unreviewed → accepted       (accept action)
           → needs-iteration (iterate action — creates follow-up backlog)
           → rejected        (reject action)
           → deferred        (defer action — re-enters queue at end)
```

## HITL Stops

| Step | Gate | User Action |
|------|------|-------------|
| 3 | Action selection | User picks: accept, iterate [notes], reject [reason], skip, defer |

## Resume Support

No resume needed — stateless per invocation. review-status.json persists across invocations.
