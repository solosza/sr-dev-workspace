# Step 4: Update State

## Purpose

Write the state transition to `.claude/state/review-status.json`.

## Pre-generation Checkpoint

- Read: `.claude/state/review-status.json` (current state before modification)

## Procedure

1. Read current `review-status.json`
2. Add or update entry in `reviewed` for the backlog number:
   ```json
   {
     "NNN": {
       "status": "accepted | needs-iteration | rejected | deferred",
       "reviewed_at": "ISO timestamp",
       "notes": "user notes if provided",
       "followup_backlog": "NNN or null",
       "worktree_branch": "branch name or null (preserved from spawn)",
       "worktree_path": "path or null (preserved from spawn)",
       "merge_status": "merged | rejected | pending_review | null",
       "scope": "BUILD | RESEARCH | etc. or null"
     }
   }
   ```
   - `worktree_branch` and `worktree_path` are set by spawn-subagent/execute-pipeline when using worktree mode
   - `merge_status` transitions: `pending_review` → `merged` (accept) or `rejected` (reject)
   - Preserve existing worktree fields when updating — never overwrite with null if already set
3. Recompute stats from `reviewed` entries:
   - `total_completed`: count of all backlogs in done/
   - `reviewed`: count of entries in `reviewed`
   - `unreviewed`: total_completed - reviewed
   - `accepted`: count where status = accepted
   - `needs_iteration`: count where status = needs-iteration
   - `rejected`: count where status = rejected
   - `deferred`: count where status = deferred
4. Write updated review-status.json (merge pattern — read, modify, write)

## Acceptance Criteria

- [ ] Entry added/updated for reviewed backlog
- [ ] Stats recomputed from reviewed entries (not manually incremented)
- [ ] review-status.json is valid JSON after write
- [ ] No existing entries deleted
