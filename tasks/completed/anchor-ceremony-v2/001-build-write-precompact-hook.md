# Task 001: Write PreCompact Re-Anchor Hook

**Type:** BUILD
**Gates Satisfied:** AC-01

## Action

Write `.claude/hooks/precompact-reanchor.py` (ONE file). ~40 lines.

## Spec

Design source: `projects/kernel-precompact-reanchor-research/research-report.md` (Integration Design, component 1) and `02-compaction-survival-and-design.md`.

Behavior:
1. Read the PreCompact event JSON from stdin (`json.load(sys.stdin)`); extract `trigger` field (`"auto"` or `"manual"`; tolerate missing → `"unknown"`).
2. Resolve state routing exactly like the other hooks (READ `.claude/hooks/universal-gate-enforcer.py` lines 40-92 first — RULE ZERO):
   - `KERNEL_AGENT_ID` env set → session state is `agent-{id}-session-state.json`, workflow is `agent-{id}-workflow.json` (fall back to shared workflow if agent file missing)
   - else → `session_state.json`; workflow routed via `agent_id` key then `{domain}_workflow.json`
3. Read routed session state (utf-8-sig tolerant). If missing/unparseable or no `domain` → exit 0 silently (no-op safety: one-shot agents and bare repos must never have compaction blocked).
4. Set in routed WORKFLOW state: `anchored: false`. Write via `state_io.atomic_write_json(path, obj, "workflow")`.
5. Set in routed SESSION state: `compaction_anchor_reason: "{trigger}_compaction"`, `compaction_timestamp: <ISO now>`. Write via `state_io.atomic_write_json(path, obj, "session_state")`.
6. Exit 0 on EVERY path (wrap main in try/except → exit 0). A crashing PreCompact hook must never abort compaction.

Import state_io the same way sibling hooks do (`sys.path.insert` of the hook dir, then `from state_io import atomic_write_json, read_json`).

## Constraints

- Do NOT modify Gate 3 or any existing hook file
- No content injection (upstream bug GitHub #15174) — state side-effects only

## Acceptance Criteria (mechanical)

- File exists at `.claude/hooks/precompact-reanchor.py`
- `python -m py_compile` passes
- Greps hit: `state_io`, `KERNEL_AGENT_ID`, `anchored`, `compaction_anchor_reason`, `sys.exit(0)` (or equivalent unconditional-zero pattern)
