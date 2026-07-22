---
name: review-queue
type: design-document
version: 1.0
date_created: 2026-07-07
status: draft
purpose: Track human review and acceptance of completed pipeline work
---

# /review-queue — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->

## Position in System

```
/kernel/execute-pipeline → completes → backlog moved to done/
                                              ↓
/kernel/review-queue → discovers unreviewed → presents queue
                                              ↓
                              user acts → accept / iterate / reject
                                              ↓
                              iterate → /kernel/backlog (follow-up)
```

`/review-queue` is the post-pipeline quality gate. It discovers completed work that hasn't been reviewed and enables structured human acceptance.

## Skill Identity

You are a review queue manager. You discover unreviewed completed pipeline work by diffing `docs/backlog/done/` against `.claude/state/review-status.json`, present items in priority order, and support accept/iterate/reject/skip/defer actions. Iteration follow-ups are created via `/kernel/backlog` with parent linking.

## Philosophy

1. **Discovery-based** — diff done backlogs against review state to find unreviewed items. No manual registration.
2. **Async** — never block pipeline execution. Review happens when the human is ready.
3. **Action-driven** — each review produces a state machine transition with recorded rationale.
4. **Iterate, don't reject** — iteration creates follow-up backlogs via `/kernel/backlog` with parent linking. When follow-up is accepted, parent is also accepted.
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

## Input

```
/kernel/review-queue
/kernel/review-queue [backlog-number]
/kernel/review-queue --stats
```

| Argument | Purpose | Example |
|----------|---------|---------|
| (none) | Present next unreviewed item | `/kernel/review-queue` |
| `[number]` | Review specific backlog | `/kernel/review-queue 185` |
| `--stats` | Show review statistics | `/kernel/review-queue --stats` |

## Output

Review queue presentation with quick actions, or statistics summary.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[review-queue/references/workflow]] | Steps 1-5: discover, present, act, update, report |
| [[review-queue/references/state-schema]] | review-status.json schema and state machine |
| [[review-queue/references/priority-ordering]] | How items are sorted in the queue |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Discover | Diff done/ against review-status.json | Unreviewed items list | — |
| 2. Present | Sort by priority, show next item | Formatted review card | — |
| 3. Act | Process user's quick action | Action result | **User selects action** |
| 4. Update State | Write state transition to review-status.json | Updated state | — |
| 5. Report | Show stats and next item (if any) | Summary | — |

## Critical Rules

1. **Never block pipeline execution.** Review is async — pipelines complete independently of review status.
2. **Always use `/kernel/backlog` for iteration follow-ups.** Never write backlog files directly. The command enforces template and intent chain.
3. **Discovery is the source of truth.** Scan `docs/backlog/done/` every invocation — don't cache or assume.
4. **State transitions are append-only.** Record every action with timestamp and rationale. Never delete history.

## State Persistence

**File:** `.claude/state/review-status.json`

Schema defined in → [[review-queue/references/state-schema]]

## Complete File Structure

**Skill package:**

```
.claude/commands/kernel/review-queue.md                ← Layer 1
.claude/skills/review-queue/
├── SKILL.md                                           ← Layer 2
├── workflow.md, gate-contract.md                      ← Layer 2
├── steps/step-{01..05}-*.md                           ← Layer 3 (5 steps)
└── references/
    └── INDEX.md                                       ← Layer 4
```

**Design doc:**

```
.claude/docs/design/review-queue/
├── index.md                                           ← this file
└── references/
    ├── workflow.md                                    ← step details
    ├── state-schema.md                                ← review-status.json schema
    └── priority-ordering.md                           ← queue sorting logic
```

---

**Version:** 1.0
**Last Updated:** 2026-07-07
