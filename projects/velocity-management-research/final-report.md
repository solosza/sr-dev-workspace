# Velocity Management and Review System — Research Report

**Backlog:** 181
**Date:** 2026-07-06
**Status:** Complete

---

## Problem Statement

Execute-pipeline and agent swarms complete backlogs faster than the user can review, iterate, and accept results. Work accumulates without a review loop, acceptance gate, or iteration tracking. As of this report: 212 completed backlogs, 10+ active concurrent agents, and no systematic way to track what's been reviewed vs. what's piling up.

The gap is between **pipeline completion** (agent marks done) and **human acceptance** (user reviews, iterates, accepts or rejects).

---

## Research Question Answers

### 1. What's the right abstraction?

**A review queue** — not a dashboard, kanban, or report.

Rationale:
- The user's workflow is already sequential review: look at completed work, decide accept/reject/iterate
- A queue naturally orders by priority and surfaces the next item to review
- Dashboards show everything at once — wrong for high-velocity output where you need to focus on one thing at a time
- Kanban adds ceremony (columns, drag/drop) without value — the only states are: `unreviewed`, `in-review`, `accepted`, `needs-iteration`, `rejected`

**Implementation:** A `/kernel/review-queue` command that reads completed-but-unaccepted work and presents the highest-priority item for review action.

### 2. What state already exists?

Significant state infrastructure is already in place:

| State Source | What It Tracks | Gap |
|-------------|---------------|-----|
| `docs/backlog/done/*.md` | Completed backlogs (212 items) | No "reviewed" vs "unreviewed" distinction |
| `agent-swarm.json` | Active/completed agents | No review status per deliverable |
| `completed_tasks` in workflow JSONs | Per-pipeline task completion | Task-level, not deliverable-level |
| `anchor-logs/` | Action history per anchor cycle | Audit trail, not review state |
| `tasks/completed/` | Archived task folders | No review metadata |
| `projects/*/` | Research outputs, reports | No acceptance status |

**Key gap:** Nothing tracks whether a human has reviewed, accepted, or requested changes on completed work. The system knows what's done but not what's been looked at.

### 3. How do other systems handle this?

| System | Pattern | Applicable? |
|--------|---------|-------------|
| **GitHub PR Review** | Author submits, reviewer approves/requests changes, author iterates | Yes — async, non-blocking, iteration-native |
| **CI/CD Deployment Pipeline** | Build → stage → manual approval gate → production | Partially — approval gate is blocking, not async |
| **Jira/Linear Review** | Status transitions: Done → In Review → Accepted | Yes — simple state machine |
| **Code Review Queues (Reviewpad, Graphite)** | Priority-ordered queue, reviewer picks top item | Yes — matches the "focus on one thing" pattern |
| **Merge Queues (GitHub, Bors)** | Automated validation + human approval | Partially — automated checks already exist (gate contracts) |

**Best fit:** GitHub PR review model adapted for agent output. Key properties:
- Async (doesn't block pipeline)
- Supports iteration (request changes → agent fixes → re-review)
- Has clear terminal states (accepted, rejected)
- Author (agent) and reviewer (user) are distinct roles

### 4. What's the minimum viable version?

**MVP: A `/kernel/review-queue` command + a `review-status.json` state file.**

The command:
1. Reads `docs/backlog/done/` for all completed backlogs
2. Cross-references `review-status.json` for review state
3. Filters to unreviewed items
4. Sorts by priority (most recent first, or user-defined priority)
5. Presents the top item with: backlog summary, deliverable location, quick-action options

The state file (`review-status.json`):
```json
{
  "reviewed": {
    "162": { "status": "accepted", "reviewed_at": "2026-07-06T10:00:00Z", "notes": null },
    "161": { "status": "needs-iteration", "reviewed_at": "2026-07-06T10:05:00Z", "notes": "Missing edge case for cross-repo links", "followup_backlog": 185 }
  },
  "stats": {
    "total_completed": 212,
    "reviewed": 2,
    "unreviewed": 210,
    "accepted": 1,
    "needs_iteration": 1,
    "rejected": 0
  }
}
```

Quick actions during review:
- **accept** — marks reviewed + accepted, no further action
- **iterate [notes]** — marks needs-iteration, creates follow-up backlog via `/kernel/backlog`
- **reject [reason]** — marks rejected, archives
- **skip** — moves to next item in queue, doesn't change status
- **defer** — marks as low-priority, moves to bottom of queue

### 5. Should review be per-backlog or per-deliverable?

**Per-backlog.** Reasons:

- Backlogs are the unit of work the user creates and thinks in
- A backlog may produce multiple files, but the user's mental model is "did backlog 162 produce what I wanted?"
- Per-deliverable (per-file) review is too granular — 212 backlogs already, each producing 5-20 files = 1000-4000 review items
- Gate contracts already verify per-file correctness mechanically; human review is about intent and quality at the backlog level
- Iteration naturally maps to "redo this backlog" not "redo this file"

**Exception:** Large backlogs that produce entire repos (e.g., SSH compliance platform) could support optional drill-down into sub-deliverables, but the primary review unit remains the backlog.

### 6. How does iteration work?

**Iteration creates a follow-up backlog, not an edit-in-place.**

Flow:
1. User reviews backlog 162 output
2. User says "iterate — missing edge case for cross-repo links"
3. `/kernel/review-queue iterate "missing edge case for cross-repo links"` does:
   a. Marks 162 as `needs-iteration` in review-status.json
   b. Creates a new backlog (e.g., 185) with scope "Fix backlog 162: missing edge case for cross-repo links"
   c. Links 185 to 162 via `parent_backlog: 162` field
   d. New backlog enters the pipeline normally — `/kernel/execute-pipeline 185`
4. When 185 completes, review-queue shows it linked to 162
5. User reviews 185 → accepts → both 185 and 162 marked accepted

**Why not edit-in-place:**
- Edit-in-place requires the agent to understand the full context of the original work
- A new backlog goes through the full pipeline (decompose, execute, validate) — same quality guarantees
- Traceability: you can see the iteration chain (162 → 185 → accepted)
- No risk of breaking the original output during iteration

---

## Recommended System Design

### Architecture

```
User invokes /kernel/review-queue
        │
        ▼
┌─────────────────────┐
│  review-queue.md    │  ← Skill command
│  (reads state,      │
│   presents item,    │
│   handles actions)  │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ review-status.json  │  ← State file (.claude/state/)
│ {reviewed: {...},   │
│  stats: {...}}      │
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│ docs/backlog/done/  │  ← Source of truth for completions
│ agent-swarm.json    │  ← Active/completed agents
│ projects/*/         │  ← Deliverable outputs
└─────────────────────┘
```

### Components

| Component | Location | Purpose |
|-----------|----------|---------|
| `/kernel/review-queue` command | `.claude/commands/kernel/review-queue.md` | Entry point — reads state, presents items, handles actions |
| Review status state | `.claude/state/review-status.json` | Tracks per-backlog review status |
| Review skill | `.claude/skills/review-queue/SKILL.md` | Detailed step logic (if command exceeds index threshold) |

### State Machine

```
                    ┌──────────┐
  Pipeline done ──▶ │unreviewed│
                    └────┬─────┘
                         │ user opens review
                         ▼
                    ┌──────────┐
                    │in-review │
                    └──┬───┬───┘
            accept │   │   │ reject
                   ▼   │   ▼
            ┌────────┐ │ ┌────────┐
            │accepted│ │ │rejected│
            └────────┘ │ └────────┘
                       │ iterate
                       ▼
              ┌────────────────┐
              │needs-iteration │──▶ creates follow-up backlog
              └───────┬────────┘
                      │ follow-up accepted
                      ▼
               ┌────────────┐
               │  accepted  │
               └────────────┘
```

### Integration Points

1. **`/kernel/complete` integration:** When a pipeline finishes and moves a backlog to `done/`, it could auto-register the item in review-status.json as `unreviewed`. This is optional — the review-queue command can discover unregistered items by diffing `done/` against `review-status.json`.

2. **`/kernel/execute-pipeline` integration:** When iteration creates a follow-up backlog, it enters the normal pipeline. No special handling needed — the pipeline is already the execution engine.

3. **Session start integration:** `/kernel/session-start` could optionally report: "N items awaiting review" as a status line. Non-blocking, informational only.

4. **Agent swarm integration:** When reviewing a backlog completed by an agent swarm, the review-queue can show which agents contributed (from `agent-swarm.json`).

### Priority Ordering

Default queue order (configurable):
1. **Needs-iteration follow-ups** — highest priority (user already reviewed once, waiting for fix)
2. **Recent completions** — newer work first (freshest context)
3. **High-priority backlogs** — based on priority field in backlog .md
4. **Older unreviewed** — catch-up items

---

## Minimum Viable Version — Implementation Backlog

The following backlogs would implement the MVP:

| # | Title | Type | Scope |
|---|-------|------|-------|
| 1 | Build `/kernel/review-queue` command | BUILD | Command file + review-status.json schema |
| 2 | Build review-queue skill (if command exceeds threshold) | BUILD | SKILL.md + step references |
| 3 | Integrate review registration into `/kernel/complete` | BUILD | Add auto-register to complete.md |
| 4 | Add review stats to `/kernel/session-start` | BUILD | "N items awaiting review" line |

**Estimated effort:** 1-2 pipelines (backlog 1-2 are the core, 3-4 are integration).

---

## Key Design Decisions

1. **Async, not blocking.** Review never gates pipeline execution. Agents keep working; review happens when the user has time.

2. **Per-backlog, not per-file.** The backlog is the review unit. Gate contracts handle per-file mechanical verification.

3. **Iteration via new backlog.** No edit-in-place. Full pipeline guarantees on iteration work.

4. **State in JSON, not in backlog files.** Review status lives in `review-status.json`, not as metadata in backlog .md files. Keeps backlog files clean and review state queryable.

5. **Command-driven, not dashboard.** `/kernel/review-queue` is a terminal command, not a web UI. Fits the existing kernel workflow (commands → state → commands).

6. **Discovery-based, not registration-based.** The command discovers unreviewed items by diffing `done/` against `review-status.json`. No registration step required — anything in `done/` that's not in `review-status.json` is unreviewed.

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | What To Do Instead |
|-------------|---------------|-------------------|
| Review as a pipeline gate | Blocks agent velocity — the whole point is async | Review is decoupled from execution |
| Per-file review items | 1000+ items overwhelm the user | Per-backlog review |
| Dashboard/web UI | Adds infrastructure complexity, breaks terminal workflow | Command-line review queue |
| Edit-in-place iteration | Loses traceability, risks breaking original | New backlog with parent link |
| Manual registration of review items | Adds friction, items get missed | Auto-discovery from `done/` folder |
| Review status in backlog .md files | Mixes concerns, makes querying hard | Separate `review-status.json` |

---

## Conclusion

The velocity management problem is a **review queue gap** — the kernel has strong execution infrastructure (backlogs → pipelines → tasks → agents) but no acceptance infrastructure. The fix is a lightweight `/kernel/review-queue` command backed by a `review-status.json` state file, following the same patterns as the rest of the kernel: command-driven, state-tracked, JSON-backed, and async by default.

The 212 unreviewed completed backlogs represent a significant backlog of their own. The review queue's first job will be triaging this accumulated work — likely by letting the user bulk-accept older items and focus review on recent high-priority completions.
