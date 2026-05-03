# State Session Scoping — Isolate Sub-Agent State from Parent

## Status
Open

## Priority
CRITICAL — blocks backlog 037 (anchor integrity). Without this fix, 037 creates a hard deadlock.

## Summary
Background agents spawned via run-task.sh write to the parent's `{domain}_workflow.json` during their own session-start, setting `anchored: false`. This invalidates the parent's anchor state. Currently the parent can work around this by directly writing `anchored: true` back — but once backlog 037 ships (protocol hash verification), this workaround becomes impossible because the hash won't match. The contention then becomes a permanent deadlock: sub-agent resets anchor, parent can't restore it.

## Finding Source
Dogfooding — discovered 2026-04-23 when running `/kernel/execute-pipeline 037 038 039`. Parent tried to prep pipeline 038 tasks while 037's run-task.sh was executing in background. Sub-agents repeatedly set `anchored: false`, blocking the parent via hook enforcement.

## The Bug

1. Parent session anchors → `anchored: true` in `sr_dev_workflow.json`
2. Parent spawns background agent → run-task.sh → `claude -p` per task
3. Each `claude -p` runs session-start → sets `anchored: false` in the SAME `sr_dev_workflow.json`
4. Parent's next action hits gate enforcer → blocked ("Protocol not anchored")
5. Parent flips `anchored: true` directly → **this is the bypass 037 will prevent**

## Requirements

1. **The gap:** `{domain}_workflow.json` is a shared singleton with no session scoping. All agents (parent + sub-agents) read and write the same file.

2. **Options to fix (pick one):**
   - **Session-scoped workflow files:** Each `claude -p` invocation gets its own workflow file (`sr_dev_workflow_{session_id}.json`). Parent's state is never touched by children. Children clean up their file on exit.
   - **Anchor lock:** Sub-agents spawned by run-task.sh skip the `anchored: false` reset in session-start. They still do their own anchor, but write to a separate field or file.
   - **Parent-only anchor:** The `anchored` field is only meaningful for the parent session. Sub-agents check a different field (`sub_anchored`) or skip the anchor gate entirely (they're one-shot — anchor drift isn't a real risk for single-task agents).
   - **one_shot bypass:** If `one_shot: true` in session_state.json (set by run-task.sh), session-start does NOT reset `anchored: false` in workflow state. The one-shot agent still reads protocol but doesn't invalidate the parent's anchor.

3. **Whichever mechanism:**
   - Parent's anchor state must survive sub-agent execution
   - Sub-agents must still be kernel-governed (session-start, work, complete)
   - Must work with the protocol hash verification from backlog 037
   - Must not require architectural changes to run-task.sh

## Sequencing Constraint
**This backlog MUST ship before or alongside backlog 037.** If 037 ships first, the state contention becomes a hard deadlock instead of a soft one.

## References
- `.claude/state/sr_dev_workflow.json` — shared workflow state
- `.claude/hooks/universal-gate-enforcer.py` — checks `anchored` field
- `.claude/commands/kernel/session-start.md` — sets `anchored: false` on fresh start
- `.claude/lessons/state-contention.md` — full incident analysis
- Backlog 037 — anchor integrity (blocked by this)

## Task Builder Input
- **Deliverable:** Session-scoped workflow state that isolates sub-agent writes from parent anchor state
- **Location:** workspace:.claude/
- **Scope:** REFACTOR
- **Constraints:** Must not break run-task.sh. Must not break existing anchor flow. Must be compatible with 037's protocol hash verification. Must ship before or alongside 037.
