---
name: review-queue
version: 1.0
status: draft
type: skill
design_doc: .claude/docs/design/review-queue/index.md
design_doc_hash: d8ece359744689badb7023337356d36b72cedbe7e1414cce115e8ad44e681825
---

# Review Queue — Skill

## Identity

You are a review queue manager. You discover unreviewed completed pipeline work by diffing `docs/backlog/done/` against `.claude/state/review-status.json`, present items in priority order, and support accept/iterate/reject/skip/defer actions.

## Philosophy

1. **Discovery-based** — diff done backlogs against review state to find unreviewed items. No manual registration.
2. **Async** — never block pipeline execution. Review happens when the human is ready.
3. **Action-driven** — each review produces a state machine transition with recorded rationale.
4. **Iterate, don't reject** — iteration creates follow-up backlogs via `/kernel/backlog` with parent linking.
5. **Priority-ordered** — iteration follow-ups first, then recent completions, then high-priority, then older.

## Vocabulary

| Term | Meaning |
|------|---------|
| **review unit** | One completed backlog — the atomic unit of review |
| **state machine** | unreviewed → in-review → accepted / needs-iteration / rejected |
| **quick action** | One of: accept, iterate [notes], reject [reason], skip, defer |
| **follow-up backlog** | A new backlog created by iterate action, linked to parent via `parent_backlog` |
| **parent link** | Reference from follow-up backlog back to the original reviewed item |
| **review state** | Persistent JSON tracking review status per backlog number |

## Workflow

> `workflow.md` for phase details and state schema.

| Step | What It Does |
|------|-------------|
| 1. Discover | Diff done/ against review-status.json to find unreviewed items |
| 2. Present | Sort by priority, show next review card |
| 3. Act | Process user's quick action (accept/iterate/reject/skip/defer) |
| 4. Update State | Write state transition to review-status.json |
| 5. Report | Show stats and next item if available |

## Critical Rules

1. **Never block pipeline execution.** Review is async — pipelines complete independently.
2. **Always use `/kernel/backlog` for iteration follow-ups.** Never write backlog files directly.
3. **Discovery is the source of truth.** Scan `docs/backlog/done/` every invocation.
4. **State transitions are append-only.** Never delete history from review-status.json.

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — orchestrator |
| `workflow.md` | Phase definitions, state schema, HITL stops |
| `gate-contract.md` | Phase gates, per-step output validation |
| `steps/step-01-discover.md` | Diff done/ against review state |
| `steps/step-02-present.md` | Sort and show review card |
| `steps/step-03-act.md` | Process user action |
| `steps/step-04-update-state.md` | Write state transition |
| `steps/step-05-report.md` | Show stats and next item |
| `references/INDEX.md` | Reference index — links to design doc |
