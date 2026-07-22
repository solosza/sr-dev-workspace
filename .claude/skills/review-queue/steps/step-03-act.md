# Step 3: Act

## Purpose

Process the user's selected quick action on the current review item. Includes merge gate for worktree-backed items.

## Pre-generation Checkpoint

- Read: user's action input
- Read: `.claude/state/review-status.json` (current state for validation)

## Procedure

1. Parse user action:
   - `accept` — mark item as accepted (+ merge if worktree branch exists)
   - `iterate [notes]` — mark as needs-iteration, create follow-up
   - `reject [reason]` — mark as rejected with reason (+ remove worktree if exists)
   - `skip` — no state change, proceed to next item
   - `defer` — mark as deferred, push to end of queue
2. Validate action:
   - Action must be one of the 5 valid actions
   - `iterate` must include notes (at least one word)
   - `reject` must include reason (at least one word)
3. **Check for worktree branch** in review-status.json entry:
   - If `worktree_branch` exists → this is a worktree-backed item, apply merge gate
   - If no `worktree_branch` → standard (non-worktree) flow, no merge step
4. For `accept` action **with worktree branch (merge gate)**:
   a. Verify branch exists: `git branch --list [branch]`
   b. Dry-run merge check: `git merge --no-commit --no-ff [branch]` then `git merge --abort`
   c. If conflicts detected → report to user, do NOT auto-resolve, offer: resolve manually, rebase, or reject
   d. If clean merge: `git merge [branch] --no-edit`
   e. Remove worktree: `git worktree remove [worktree_path]`
   f. Delete branch: `git branch -d [branch]`
   g. Update entry: `merge_status → "merged"`
5. For `accept` action **without worktree branch**:
   - Standard accept — mark as accepted, no merge step
6. For `iterate` action:
   - Invoke `/kernel/backlog` with:
     - Title derived from parent backlog + iteration notes
     - Description referencing parent backlog number
     - `parent_backlog: NNN` link
   - If worktree branch exists: follow-up pipeline reuses the SAME worktree (extends branch)
   - Record `reuse_worktree: true` and existing branch name in follow-up backlog
   - Record the new backlog number as `followup_backlog`

6b. **Batch execution routing (after all actions in this review session are processed):**
   - If the session produced 2+ `iterate` follow-up backlogs → invoke `/spawn-agent-swarm [followup-numbers]` to build and run them in parallel (isolated per-agent state, no shared-file contention — this is the standing swarm path, not a one-off script)
   - If exactly 1 follow-up → `/kernel/execute-pipeline [number]` as usual, no swarm overhead
   - Never hand-roll parallel `run-task.sh` invocations outside `/spawn-agent-swarm` — the skill already provides the manifest + per-agent isolation + monitor this needs
7. For `reject` action **with worktree branch**:
   a. Remove worktree: `git worktree remove [worktree_path]` (force if needed)
   b. Delete branch: `git branch -D [branch]` (force delete, work is being discarded)
   c. Update entry: `merge_status → "rejected"`
8. For `reject` action **without worktree branch**:
   - Standard reject — mark as rejected with reason
9. Record action with ISO timestamp

## Acceptance Criteria

- [ ] Action parsed correctly
- [ ] Invalid actions rejected with helpful error
- [ ] Iterate action creates follow-up via `/kernel/backlog`
- [ ] Accept with worktree branch merges feature branch to main
- [ ] Reject with worktree branch removes worktree + deletes branch
- [ ] Merge conflicts reported to user (never auto-resolved)
- [ ] Action recorded with timestamp
