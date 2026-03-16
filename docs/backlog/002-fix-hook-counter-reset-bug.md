# Backlog 002: Fix Hook Counter Reset Bug in universal-gate-enforcer.py

## Status
Open

## Priority
High — user hitting this frequently

## Summary
The `universal-gate-enforcer.py` hook's anchor counter (`actions_since_anchor`) doesn't properly reset after `/kernel/anchor`. The hook keeps blocking writes even immediately after anchoring, with the counter climbing indefinitely (11 → 13 → 14).

## Root Cause
In `universal-gate-enforcer.py` lines 109-111:
```python
if tool_name in ('Write', 'Edit'):
    if '/.claude/' in file_path or file_path.startswith('.claude/'):
        sys.exit(0)
```

The hook exits early for ALL `.claude/` paths — no increment, no reset. When the anchor command uses Edit on `[domain]_workflow.json` (a `.claude/state/` path), the hook exits before reaching the counter logic at lines 146-160. The counter is never reset to 0.

The counter is only modified at lines 149-153 (increment on non-.claude/ actions). No code in the hook resets it — the hook only increments.

## Current Workaround
Use **Write** (full file rewrite) not **Edit** to reset `actions_since_anchor` in the workflow state file during anchor. Write overwrites the entire file content including the counter, bypassing the hook's increment logic. This is documented in:
- `lessons/cycling-run-3.md` (2026-03-06 Counter Reset Mechanism)
- MEMORY.md (Kernel Lessons: "Anchor counter reset: Use Write not Edit")

## Proper Fix Options
1. **Hook-aware reset:** After the `.claude/` early-exit, detect if the Write/Edit is to a workflow state file and reset the counter in-hook
2. **Explicit reset command:** Add a counter-reset path in the hook triggered by a specific marker (e.g., `"anchor_reset": true` in the JSON)
3. **Remove early exit for state files:** Only skip `.claude/` early exit for non-state paths (commands, hooks, settings, protocols) — let state file writes flow through the full counter logic
4. **Post-anchor verification:** Hook reads counter after anchor Write and verifies it's 0

## Files to Change
- `isagawa-kernel/.claude/hooks/universal-gate-enforcer.py` (canonical source)
- Then sync to all repos per sync rule

## Lesson References
- `lessons/cycling-run-3.md` line 1087: "Counter Reset Mechanism"
- `lessons/kernel-compliance.md`: "Agent Bypassed Hook Enforcement"
- MEMORY.md: "Anchor counter reset: Use Write not Edit for anchor reset"
