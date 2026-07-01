# Kernel Rollback Mechanism — Research Report

**Backlog:** 167-kernel-research-rollback-mechanism
**Date:** 2026-06-28
**Status:** Complete

## Executive Summary

The kernel's lessons are append-only with no mechanism to say "lesson X was wrong, undo it." A rollback mechanism would version protocol/hook changes, link each lesson to its associated code modifications, and enable reverting changes that made things worse. The recommended approach: git-based versioning (the kernel already lives in git) with a compensation pattern (forward-only rollback, like Flyway community edition) and experiment-driven rollback triggers (from backlog 165).

## Part 1: The Problem

Current state:
- Lessons are append-only in `lessons.md`
- `/kernel/learn` modifies hooks and protocol files
- No record of which lesson caused which code change
- No mechanism to revert a change that made things worse
- User corrects manually when a lesson or memory entry is wrong

What's needed:
- **Versioning:** Track what changed, when, and why
- **Linking:** Connect lessons → code changes (1:many relationship)
- **Triggers:** Detect when a change made things worse
- **Reversal:** Undo the change without breaking dependent changes
- **Recording:** Log why the rollback happened for future learning

## Part 2: Prior Art

### Database Migrations (Alembic / Flyway)

| Pattern | Kernel Equivalent |
|---------|------------------|
| `upgrade()` / `downgrade()` | Apply lesson / revert lesson |
| Version numbering (V001, V002) | Lesson timestamp + experiment ID |
| One change per migration | One lesson per learn event |
| Compensation migration | New lesson that reverses prior lesson |

**Key insight from Flyway Community:** The free edition doesn't support `undo` — instead, you write a new forward migration that reverses the effect. This is the compensation pattern: rollback = new forward change that undoes the prior change. This is safer because:
- History is always forward-moving (append-only audit trail)
- No destructive operations on existing files
- Each reversal is itself a tracked, versioned change

**Alembic's approach:** `upgrade()` and `downgrade()` functions in each migration. More powerful but requires writing the downgrade at the time of the upgrade — overhead the kernel can't afford for every learn event.

### AI Agent Rollback (2026 State of Art)

**Event sourcing pattern:** Every write is logged with agent ID and run ID. Rollback = replay log in reverse. The kernel already does this with `actions.jsonl` — every action is logged with timestamp and tool.

**Soft deletes:** Rather than removing a lesson, mark it as `deprecated` or `superseded_by`. The lesson remains in the audit trail but is no longer applied.

**Cascade prevention through backward compatibility:** When rolling back lesson A, check if lessons B and C depend on A. If they do, the rollback must address all three — or be blocked.

**Diffback tool (GitHub):** Snapshots file state before AI agent changes, enables selective rollback of individual file changes. The kernel could snapshot hook/protocol files before each learn event.

### Reinforcement Learning Rollback (ArXiv 2510.14503)

"Learning to Undo: Rollback-Augmented RL with Reversibility Signals" — agents learn when to rollback based on outcome signals. Directly relevant: the kernel could learn which types of changes are reversible vs irreversible.

## Part 3: Versioning Design

### Option A: Git-Based (Recommended)

The kernel already lives in a git repo. Each `/kernel/learn` event that modifies files is a potential git commit. Version tracking is free.

**Implementation:**
```bash
# Before /kernel/learn modifies files:
git stash  # or snapshot current state

# After /kernel/learn completes:
# The modified files are the diff
# Link: lesson entry → git diff → experiment ID
```

**Advantages:**
- Zero new infrastructure
- Full diff history via `git log`
- Rollback via `git checkout` of specific files
- Already familiar pattern

**Disadvantage:**
- Commits clutter git history (mitigated by using a convention like `learn: [topic]` commit messages)

### Option B: Snapshot-Based

Before each learn event, snapshot the files that will be modified:

```json
{
  "snapshot_id": "snap-2026-06-28-001",
  "timestamp": "2026-06-28T19:30:00Z",
  "files": {
    ".claude/hooks/sr_dev-gate-enforcer.py": "<full content>",
    ".claude/lessons/lessons.md": "<full content>"
  },
  "learn_trigger": "test_failure",
  "lesson_topic": "cd-blocker"
}
```

Storage: `.claude/state/snapshots/` — one JSON file per snapshot.

**Advantages:** Self-contained, no git dependency, can snapshot non-git-tracked files
**Disadvantages:** Storage grows with file sizes, redundant data

### Option C: Diff-Based

Store only the diff (patch) for each learn event:

```json
{
  "diff_id": "diff-2026-06-28-001",
  "timestamp": "2026-06-28T19:30:00Z",
  "patches": [
    {
      "file": ".claude/hooks/sr_dev-gate-enforcer.py",
      "added_lines": [45, 46, 47],
      "removed_lines": [],
      "patch": "--- a/...\n+++ b/...\n@@ ...\n+ new_code"
    }
  ]
}
```

**Advantages:** Compact storage, precise change tracking
**Disadvantages:** Requires patch application logic, merge conflicts possible

### Recommendation: Git-Based + Lesson Metadata

Use git for the actual versioning (zero infrastructure cost). Add metadata to each lesson entry that links it to the git state:

```json
{
  "lesson_id": "L-2026-06-28-001",
  "timestamp": "2026-06-28T19:30:00Z",
  "topic": "cd-blocker",
  "trigger": "test_failure",
  "files_modified": [".claude/hooks/sr_dev-gate-enforcer.py"],
  "experiment_id": "exp-2026-06-28-cd-blocker",
  "git_commit_before": "abc1234",
  "git_commit_after": "def5678",
  "status": "active",
  "superseded_by": null
}
```

## Part 4: Lesson-to-Change Linking

### The Linking Problem

Currently, when `/kernel/learn` runs:
1. It reads the failure context
2. It appends to `lessons.md`
3. It may modify a hook or protocol file
4. There's no record linking step 2 to step 3

### Solution: Learn Event Record

Add a `learn-events.jsonl` file that records each learn invocation:

```json
{
  "event_id": "learn-2026-06-28-001",
  "timestamp": "2026-06-28T19:30:00Z",
  "trigger": "test_failure",
  "lesson_added": "Never use cd in bash commands",
  "lesson_file": ".claude/lessons/lessons.md",
  "lesson_line_range": [16, 16],
  "files_modified": [
    ".claude/hooks/sr_dev-gate-enforcer.py"
  ],
  "experiment_id": "exp-2026-06-28-cd-blocker",
  "status": "active"
}
```

This creates a 1:many relationship: one learn event → one lesson entry + N file modifications.

## Part 5: Rollback Triggers

### Manual Rollback

User says "undo that lesson" or "that change made things worse":

```
/kernel/rollback learn-2026-06-28-001
```

Agent:
1. Reads the learn event record
2. Shows what will be reverted (lesson entry + file changes)
3. User confirms
4. Applies compensation (remove lesson lines, revert file changes)
5. Records rollback as a new learn event

### Automatic Rollback (Experiment-Driven)

From backlog 165 — when an experiment's evaluation window closes and verdict is DEGRADED:

```
Experiment exp-2026-06-28-cd-blocker:
  Hypothesis: cd violations drop to zero
  Window: 10 pipelines
  Baseline: 2.3 violations/pipeline
  Post-change: 3.1 violations/pipeline
  Verdict: DEGRADED

  → Auto-trigger rollback of learn-2026-06-28-001
  → Requires human approval (medium-risk: hook modification)
```

### Eval-Driven Rollback

From backlog 166 — when regression tests detect a decline after a learn event:

```
Regression detected:
  test_hook_coverage score dropped from 0.92 to 0.71
  Last learn event: learn-2026-06-28-001

  → Signal rollback candidate
  → Human reviews
```

## Part 6: Cascade Prevention

### The Cascade Problem

If lesson A adds a hook, and lesson B adds a gate that depends on that hook, rolling back A breaks B.

### Detection

Before executing a rollback, check for dependent changes:

```python
def check_cascade(rollback_target):
    # Find all learn events after the target
    subsequent = get_learn_events_after(rollback_target.timestamp)

    # Check if any modify the same files
    conflicts = [e for e in subsequent
                 if set(e.files_modified) & set(rollback_target.files_modified)]

    if conflicts:
        return CascadeWarning(
            target=rollback_target,
            conflicts=conflicts,
            message=f"Rolling back {rollback_target.event_id} may break "
                    f"{len(conflicts)} subsequent changes"
        )
    return None
```

### Resolution Strategies

| Strategy | When to Use |
|----------|-------------|
| **Block** | Conflicts exist, human must decide |
| **Cascade rollback** | Roll back target + all dependents (dangerous) |
| **Compensation** | Write a new forward change that addresses the problem without reverting |
| **Soft deprecation** | Mark lesson as deprecated, leave code in place, add TODO |

**Recommendation: Block + Compensation.** Never cascade automatically. If conflicts exist, block and present the dependency chain to the user. Prefer compensation (new forward change) over destructive rollback.

## Part 7: Lesson Confidence / Validation Flag

### Current State

All lessons are treated equally — no distinction between:
- A lesson validated by 10 successful pipelines
- A lesson added 5 minutes ago and never tested
- A lesson that's been violated 4 times (indicating it doesn't work)

### Proposed: Lesson Status

| Status | Meaning |
|--------|---------|
| `provisional` | Just added, no post-change data yet |
| `validated` | Experiment window passed, verdict IMPROVED or NO_CHANGE |
| `deprecated` | Superseded or rolled back |
| `ineffective` | Recorded 3+ times (the fix isn't working) |

This maps directly to experiment tracking (backlog 165): each lesson starts as `provisional`, gets evaluated, and transitions to `validated` or `ineffective`.

## Part 8: Implementation Plan

| Phase | Work | Dependency |
|-------|------|-----------|
| 1 | Add `learn-events.jsonl` recording to `/kernel/learn` | None |
| 2 | Link learn events to git state (commit hashes) | Phase 1 |
| 3 | Build `/kernel/rollback` command (manual trigger) | Phase 2 |
| 4 | Add cascade detection | Phase 3 |
| 5 | Wire experiment verdicts to rollback signals | Phase 4 + backlog 165 |
| 6 | Add lesson confidence/status tracking | Phase 1 |
| 7 | Wire regression test failures to rollback candidates | Phase 4 + backlog 168 |

### Manual Rollback (Phase 3) is Independent

Manual rollback (`/kernel/rollback learn-ID`) can ship without metrics (164), experiments (165), or auto-eval (166). It only needs:
- Learn event records (Phase 1)
- Git state linking (Phase 2)
- The rollback command itself (Phase 3)

Automatic rollback (Phases 5-7) requires the full dependency chain.

## Conclusion

The kernel needs rollback, but the right approach is compensation-forward (new changes that undo prior effects) rather than destructive rollback (deleting/reverting files). Git provides free versioning. Learn event records provide the lesson-to-change linking. Cascade detection prevents breaking dependent changes. Manual rollback can ship independently. Automatic rollback depends on the metrics/experiment/eval pipeline.

## Sources

- [Database Migration Tools: Alembic, Flyway, Liquibase](https://aidev.fit/en/database/database-migration-tools.html)
- [Rolling Back Migrations with Flyway (Baeldung)](https://www.baeldung.com/flyway-roll-back)
- [The Data Rollback Problem: Undoing What Your AI Agent Wrote](https://tianpan.co/blog/2026-04-20-ai-agent-data-rollback-production)
- [AI Agent Rollback Strategy 2026 (Fast.io)](https://fast.io/resources/ai-agent-rollback-strategy/)
- [Versioning, Rollback & Lifecycle Management of AI Agents](https://medium.com/@nraman.n6/versioning-rollback-lifecycle-management-of-ai-agents-treating-intelligence-as-deployable-deac757e4dea)
- [Learning to Undo: Rollback-Augmented RL (ArXiv)](https://arxiv.org/pdf/2510.14503)
- [Diffback: Instant AI Agent Undo (GitHub)](https://github.com/A386official/diffback)
