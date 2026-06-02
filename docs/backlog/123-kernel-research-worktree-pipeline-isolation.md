# Kernel: Research Worktree Pipeline Isolation

## Status
Open

## Priority
High — state contention between interactive sessions and background pipeline agents is a recurring pain point; worktrees solve it at the source

## Summary
Research and design git worktree isolation for the execute-pipeline loop. Each pipeline run would create a dedicated worktree branch, execute all tasks inside it, and merge back on completion. This eliminates `.claude/state/` file contention between the interactive session and one-shot run-task.sh agents — the root cause of the `session_started: false` resets and `session_state.json` write conflicts we hit repeatedly.

## Requirements
- Understand how `EnterWorktree` (Claude Code native tool) behaves vs raw `git worktree` commands
- Determine whether `.claude/state/` files are isolated per worktree (they should be — working tree files, not git objects)
- Design the lifecycle: create worktree at pipeline start, run all tasks inside it, merge or cherry-pick back to main, delete worktree
- Identify what happens to state files post-merge (do `.claude/state/` changes need to be kept or discarded?)
- Assess whether worktrees need to be on a named branch or can use detached HEAD
- Identify edge cases: pipeline fails mid-run, worktree already exists, merge conflicts on state files
- Evaluate whether this changes how run-task.sh invokes `claude -p` (does it need to know the worktree path?)

## References
- `projects/superpowers-research/worktree-assessment.md` — original skill assessment
- `projects/superpowers-research/research-report.md` — Section 4 (worktree), Section 8 (#2 integration plan)
- `.claude/skills/execute-pipeline/SKILL.md` — integration point is step 0 (before task-builder)
- Claude Code `EnterWorktree` built-in tool

## Task Builder Input
- **Deliverable:** Research report + integration design at `projects/worktree-research/` covering lifecycle design, EnterWorktree behavior, state isolation confirmation, and recommended execute-pipeline changes
- **Location:** `subproject:worktree-research`
- **Scope:** RESEARCH
- **Constraints:** Must confirm `.claude/state/` isolation empirically (not assumed); design must not break run-task.sh one-shot mode; merge strategy must handle state file conflicts gracefully
