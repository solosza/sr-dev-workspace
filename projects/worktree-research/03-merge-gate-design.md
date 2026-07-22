# Merge Gate Design — Review-Queue Integration

**Date:** 2026-07-07
**Status:** Design complete

---

## Overview

When execute-pipeline runs in worktree mode (BUILD/REFACTOR scope), the agent's work lives on a feature branch in an isolated worktree. The merge gate prevents untested work from landing on main by routing the feature branch through the review queue.

---

## Flow

```
execute-pipeline (worktree mode)
    │
    ├── Spawns Agent with isolation: "worktree"
    │       │
    │       ├── Agent works on feature branch
    │       ├── Commits changes to feature branch
    │       └── Returns branch name + worktree path
    │
    ├── Records in pipeline_state:
    │       worktree_branch: "worktree/pipeline-183-..."
    │       merge_status: "pending_review"
    │
    ├── Registers in review-status.json:
    │       backlog 183: {
    │         status: "unreviewed",
    │         worktree_branch: "worktree/pipeline-183-...",
    │         worktree_path: ".claude/worktrees/pipeline-183"
    │       }
    │
    └── Reports: "Work complete on branch. Awaiting review."

/kernel/review-queue (user reviews)
    │
    ├── Shows: "Backlog 183 — Worktree Branch Isolation"
    │          Branch: worktree/pipeline-183-...
    │          Files changed: N
    │
    ├── User action: accept
    │       │
    │       ├── git checkout main
    │       ├── git merge worktree/pipeline-183-...
    │       ├── git worktree remove .claude/worktrees/pipeline-183
    │       ├── git branch -d worktree/pipeline-183-...
    │       └── Updates review-status.json: status → "accepted"
    │
    ├── User action: iterate [notes]
    │       │
    │       ├── Creates follow-up backlog with worktree context
    │       ├── Follow-up pipeline runs in SAME worktree (extends branch)
    │       └── Updates review-status.json: status → "needs-iteration"
    │
    └── User action: reject [reason]
            │
            ├── git worktree remove .claude/worktrees/pipeline-183
            ├── git branch -D worktree/pipeline-183-...
            └── Updates review-status.json: status → "rejected"
```

---

## Review-Queue Extensions for Merge Gate

### review-status.json Schema Extension

```json
{
  "reviewed": {
    "183": {
      "status": "unreviewed",
      "reviewed_at": null,
      "notes": null,
      "worktree_branch": "worktree/pipeline-183-worktree-branch-isolation",
      "worktree_path": ".claude/worktrees/pipeline-183",
      "merge_status": "pending_review",
      "scope": "BUILD"
    }
  }
}
```

### Accept Action — Merge Sequence

When the user runs `accept` on a backlog with a worktree branch:

1. Verify the branch exists: `git branch --list [branch]`
2. Check for merge conflicts: `git merge --no-commit --no-ff [branch]` then `git merge --abort`
3. If clean merge: `git merge [branch] --no-edit`
4. Remove worktree: `git worktree remove [path]`
5. Delete branch: `git branch -d [branch]`
6. Update review-status.json: `merge_status → "merged"`

### Conflict Handling

If merge conflicts are detected:
1. Report conflicts to user
2. Offer options: resolve manually, rebase branch, or reject
3. Do NOT auto-resolve — conflicts require human judgment

### Iteration in Worktree

When the user requests iteration on a worktree-backed backlog:
1. The follow-up backlog should reference the existing worktree branch
2. The next pipeline run can reuse the worktree (extend the branch)
3. Pipeline state includes `reuse_worktree: true` and the existing branch name

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| Worktree already removed (manual cleanup) | Accept does merge-only, skip worktree remove |
| Branch already merged (manual merge) | Accept updates status only |
| Concurrent pipelines on same repo | Each gets its own worktree + branch (names are unique) |
| Pipeline fails mid-run in worktree | Worktree preserved with partial work for inspection |
| Main has advanced since worktree creation | Merge may have conflicts — report and let user decide |

---

## Non-Worktree Backlogs

Backlogs without worktree branches (RESEARCH scope, legacy) continue to work as before. The `accept` action simply marks them as accepted without any merge step. The merge gate is additive — it only activates when `worktree_branch` is present in review-status.json.
