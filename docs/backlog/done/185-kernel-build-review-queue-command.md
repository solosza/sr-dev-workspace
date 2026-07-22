# Build /kernel/review-queue Command

## Status
Open

## Priority
High — closes the review gap between pipeline completion and human acceptance; 210+ completed backlogs have no review tracking

## Summary
Build a `/kernel/review-queue` command backed by a `review-status.json` state file to track human review and acceptance of completed pipeline work. The system discovers unreviewed items by diffing `docs/backlog/done/` against review state, presents items in priority order, and supports accept/iterate/reject/skip/defer actions. Iteration creates follow-up backlogs via `/kernel/backlog` with parent linking. Based on velocity-management-research (backlog 181).

## Requirements
- Discovery-based: diff `docs/backlog/done/` against `review-status.json` to find unreviewed items (no manual registration)
- Per-backlog review unit (not per-file — gate contracts handle file-level verification)
- State machine: unreviewed → in-review → accepted / needs-iteration / rejected
- Quick actions: accept, iterate [notes], reject [reason], skip, defer
- Iterate action creates follow-up backlog via `/kernel/backlog` with `parent_backlog` link
- When follow-up is accepted, parent backlog also marked accepted
- Priority ordering: iteration follow-ups first, then recent completions, then high-priority, then older
- Async — never blocks pipeline execution
- `review-status.json` schema: `{ reviewed: { "NNN": { status, reviewed_at, notes, followup_backlog } }, stats: { total_completed, reviewed, unreviewed, accepted, needs_iteration, rejected } }`
- Command-driven (terminal), not dashboard/web UI

## References
- [[181-kernel-research-velocity-management-review-system]] — research report with full design
- `projects/velocity-management-research/final-report.md` — detailed architecture, state machine, anti-patterns

## Task Builder Input
- **Deliverable:** `/kernel/review-queue` command + `review-status.json` state file + review-queue skill (if command exceeds index threshold)
- **Location:** workspace:.claude/commands/kernel/review-queue.md and .claude/skills/review-queue/
- **Scope:** BUILD
- **Constraints:** Must follow kernel command patterns (command.md as entry point, skill for detailed logic). Must use `/kernel/backlog` for iteration follow-ups (not write directly). State file in `.claude/state/review-status.json`.
