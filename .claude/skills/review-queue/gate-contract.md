# Review Queue — Gate Contract

## Per-Step Gates

| Step | Gate | Pass Criteria |
|------|------|--------------|
| 1. Discover | Unreviewed list computed | At least 0 items found (empty = report "all reviewed") |
| 2. Present | Review card formatted | Card includes: number, title, scope, summary, actions |
| 3. Act | Action parsed | Valid action: accept, iterate, reject, skip, defer |
| 4. Update State | State written | review-status.json updated, stats recomputed |
| 5. Report | Stats displayed | Total, reviewed, unreviewed counts shown |

## Soft Validation Rules

1. Review card must show backlog number, title, and scope
2. Stats must sum correctly (reviewed + unreviewed = total_completed)
3. Iterate action must include notes for the follow-up backlog

## Mechanical Validations

1. review-status.json is valid JSON after every write
2. `/kernel/backlog` is invoked (not direct file write) for iterate follow-ups
3. State transitions only move forward (no accepted → unreviewed reversals)
