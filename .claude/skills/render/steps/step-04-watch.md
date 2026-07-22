# Step 4: Watch

## Purpose
Arrange the wake-up without polling; give the user their pace.

## Pre-generation Checkpoint
- Read: `render-session.json` (annotations_file path)

## Procedure
1. Spawn a background watcher (Bash, `run_in_background: true`) that blocks until `annotations.json` exists (or changes, on re-render), then exits 0. Its exit re-invokes the session via the standard task-notification — the same rhythm as pipeline completions.
2. Record `watcher_task` in state.
3. RETURN CONTROL to the user immediately. Do not wait, do not poll (RND-04).

## Acceptance Criteria
- [ ] RND-04 satisfied: watcher spawned + recorded, session non-blocking
