# Actions-Log Retention — Append-Only Audit Trail

## Status
Open

## Priority
High — if the agent can freely prune the log, it's a scratchpad, not an audit trail

## Summary
The actions log in `session_state.json` is getting truncated under pressure (context compaction, agent cleanup). There is no explicit retention policy and no guard preventing the agent from pruning entries. Either the retention policy needs to be explicit (keep last N, rotate to a daily log), or the log needs to be append-only with the hook guarding direct edits. The log must function as an audit trail, not a scratchpad.

## Finding Source
Dogfooding — discovered while running the system against itself on real work (backlog 009 execution).

## Requirements

1. **The gap:** Agent can freely clear or truncate `actions_log` in `session_state.json`. The anchor command instructs the agent to clear the log after review, but there's no verification that the review actually happened before the clear.

2. **Options to fix (pick one or combine):**
   - **Explicit retention policy:** Keep last N entries (e.g., 50). Rotate overflow to a daily log file (`actions_log_YYYY-MM-DD.jsonl`). Hook enforces minimum retention.
   - **Append-only guard:** Hook blocks any Edit/Write to `session_state.json` that reduces the `actions_log` array length, unless the edit is from a verified anchor invocation.
   - **Separate log file:** Move actions log out of `session_state.json` into its own append-only file (`.claude/state/actions.jsonl`). Hook appends entries; agent cannot edit the file directly.

3. **Whichever mechanism:**
   - Must preserve audit trail across anchor cycles
   - Must survive context compaction (log entries don't disappear)
   - Must be queryable (agent can read the log during anchor review)
   - Should not bloat state files unboundedly (rotation or cap needed)

## References
- `.claude/state/session_state.json` — current actions_log location
- `.claude/commands/kernel/anchor.md` — Part B reviews the log, Part C clears it
- `.claude/hooks/universal-gate-enforcer.py` — hook that increments the counter
- Backlog 009 — where this gap was discovered

## Task Builder Input
- **Deliverable:** Retention policy + hook enforcement for actions log integrity
- **Location:** workspace:.claude/state/ and .claude/hooks/
- **Scope:** REFACTOR
- **Constraints:** Must not break existing anchor flow. Must work with current hook architecture. Log must remain readable by the agent during anchor review.
