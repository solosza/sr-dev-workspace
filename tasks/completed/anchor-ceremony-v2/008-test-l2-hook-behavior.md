# Task 008: L2 Test — PreCompact Hook Behavior (Simulated Events)

**Type:** TEST (L2 — does it run?)
**Gates Satisfied:** AC-07

## Action

Run ONE test script that exercises `.claude/hooks/precompact-reanchor.py` in a sandbox (scratchpad temp dir, never live state):

1. **Sandbox setup:** temp dir with `.claude/state/session_state.json` (valid, `domain: sr_dev`) + `sr_dev_workflow.json` (`anchored: true`). Copy `state_io.py` + the hook into sandbox hook dir (or set cwd env so the hook resolves sandbox state — read the hook's path resolution first, RULE ZERO).
2. **Auto trigger:** pipe `{"trigger": "auto", ...}` JSON to the hook's stdin → assert exit 0; workflow `anchored == false`; session `compaction_anchor_reason == "auto_compaction"` and `compaction_timestamp` set; both files BOM-free (first 3 bytes != EF BB BF).
3. **Manual trigger:** reset sandbox, pipe `{"trigger": "manual"}` → `compaction_anchor_reason == "manual_compaction"`.
4. **Routing (SI-08):** reset sandbox, add `agent-x-session-state.json` + `agent-x-workflow.json`, run hook with `KERNEL_AGENT_ID=x` → agent files mutated; parent `session_state.json` and `sr_dev_workflow.json` byte-identical before/after.
5. **No-op safety:** empty sandbox (no state files) → exit 0, no crash, no files created. Malformed stdin (empty string) → exit 0.
6. **BOM tolerance:** seed sandbox session state WITH a UTF-8 BOM → hook still works (utf-8-sig read), rewrite is BOM-free.

## Acceptance Criteria

- All 6 sub-checks print PASS, script exits 0
- Live `.claude/state/` files untouched by the test (byte-identical before/after)
- Any red → fix hook → /kernel/learn
