# Review Queue — State Schema

## File

`.claude/state/review-status.json`

## Schema

```json
{
  "reviewed": {
    "NNN": {
      "status": "accepted | needs-iteration | rejected | deferred",
      "reviewed_at": "2026-07-07T01:00:00Z",
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
unreviewed ──→ accepted
           ──→ needs-iteration ──→ (follow-up created)
           ──→ rejected
           ──→ deferred ──→ (re-enters queue at end)
```

## Transitions

| From | Action | To | Side Effect |
|------|--------|----|------------|
| unreviewed | accept | accepted | — |
| unreviewed | iterate [notes] | needs-iteration | Creates follow-up backlog via `/kernel/backlog` |
| unreviewed | reject [reason] | rejected | Records reason |
| unreviewed | skip | unreviewed | No state change, moves to next |
| unreviewed | defer | deferred | Pushes to end of queue |
| needs-iteration | follow-up accepted | accepted | Parent auto-accepts when follow-up passes |

## Rules

1. **Create on first use** — if review-status.json doesn't exist, create with empty `reviewed` and zero stats.
2. **Stats are computed** — recalculate from `reviewed` entries on every write, never maintain independently.
3. **Append-only history** — never delete entries from `reviewed`. Status can change but entry persists.
4. **Follow-up linking** — `followup_backlog` stores the backlog number created by iterate action. When that backlog completes and is accepted, the parent is also marked accepted.
