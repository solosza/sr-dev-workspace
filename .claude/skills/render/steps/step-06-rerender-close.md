# Step 6: Re-render / Close

## Purpose
Continue the loop with fresh state, or end the session cleanly.

## Pre-generation Checkpoint
- Read: `render-session.json` (PIDs, session dir, status)

## Procedure
1. After routing, if the artifact still has content (e.g., unreviewed items remain) and the user hasn't closed: regenerate from FRESH state (back to step-02 with the same session dir; watcher re-armed on file CHANGE).
2. On `--close`, exhaustion, or user exit: kill `server_pid` and the watcher — by recorded PID only, never pattern-kill. Set `status: closed`.
3. Preserve the session dir (page, annotations.json, routing log) as the audit trail.
4. Report: rendered / routed / remaining counts + session dir path.

## Acceptance Criteria
- [ ] RND-06 satisfied: processes dead, state closed, audit trail intact
