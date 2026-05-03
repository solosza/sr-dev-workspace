# Fix one_shot State Leakage into Parent Session

## Status
Open

## Priority
Medium — causes manual cleanup after every pipeline run, but doesn't break execution

## Summary
Sub-agents spawned by `run-task.sh` set `one_shot: true` in `session_state.json` during their `pre_init_state` step. Since `session_state.json` is shared (same file), the parent session's `one_shot` field gets overwritten to `true`. After the pipeline finishes (or is killed), the parent session inherits `one_shot: true`, which changes its behavior (e.g., skipping anchor resets). Currently requires manual fix after every pipeline run. Same class of bug as backlog 040 (state contention between parent and sub-agents).

## The Bug

1. Parent session has `one_shot: false` in `session_state.json`
2. `run-task.sh` calls `pre_init_state "session_started=True,one_shot=True"` before each `claude -p`
3. This writes `one_shot: true` to the shared `session_state.json`
4. Parent session now reads `one_shot: true` — wrong identity

## Requirements
- Sub-agent `one_shot` flag must not leak into the parent's session state
- Options:
  - `run-task.sh` saves and restores `one_shot` after each iteration
  - `one_shot` moves to a session-scoped location (per backlog 040's pattern)
  - `pre_init_state` writes to a separate one-shot state file that `claude -p` reads
- Must not break existing `run-task.sh` or `session-start.md` behavior
- Related to backlog 040 (state session scoping) — may be fixable as part of that pattern

## References
- `run-task.sh` line 142: `pre_init_state "session_started=True,one_shot=True"`
- `lib/common.sh`: `pre_init_state` function
- `.claude/commands/kernel/session-start.md`: reads `one_shot` to skip anchor reset
- Backlog 040 (done): state session scoping — same bug class

## Task Builder Input
- **Deliverable:** `run-task.sh` and/or `session_state.json` handling that isolates one_shot flag from parent session
- **Location:** workspace
- **Scope:** REFACTOR
- **Constraints:** Must not break existing pipeline execution. Must work with current `pre_init_state` mechanism or replace it.
