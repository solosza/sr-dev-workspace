# Fix Safe Bash Counter Skip in Master Kernel

## Status
Open

## Priority
Medium — working fix deployed in sr-dev-workspace, needs sync to master

## Summary
The universal-gate-enforcer.py in the master kernel (isagawa-co/isagawa-kernel) skips the action counter for safe bash commands (pwd, ls, git status, etc.). Safe commands should skip gate checks (never blocked) but still increment the counter so anchor frequency reflects actual activity.

## Root Cause
In the master kernel's universal-gate-enforcer.py, safe bash commands hit `sys.exit(0)` at line 102-103 before reaching the counter increment logic at lines 144-148. The early exit bypasses both gates AND counting.

## Fix Applied (sr-dev-workspace)
Restructured the hook:
- `.claude/` Write/Edit: skip everything (no gate, no increment) — unchanged
- Safe Bash: skip gate checks, still increment counter — **fixed**
- Everything else: gate checks + increment — unchanged

## Implementation

Replace the master kernel's `universal-gate-enforcer.py` with this version. Key changes from the original:

1. **Extracted `increment_counter()` helper** — separated counting from gate logic so they can run independently
2. **Moved safe bash exit** — no longer `sys.exit(0)` before counter; instead sets `safe_bash` flag
3. **Gate checks wrapped in `if not safe_bash:`** — safe commands skip gates 1-3 but flow through to counter
4. **Counter runs for ALL non-.claude actions** — line 177 runs unconditionally after gates
5. **Gate 4 (action limit) only blocks non-safe** — safe bash increments but never triggers the anchor block

```python
# OLD (master kernel) — safe bash exits before counter
if tool_name == 'Bash':
    command = tool_input.get('command', '')
    if is_safe_bash(command):
        sys.exit(0)  # <-- counter never reached

# NEW — safe bash flag, counter always runs
safe_bash = False
if tool_name == 'Bash':
    command = tool_input.get('command', '')
    safe_bash = is_safe_bash(command)

# Gate checks — safe bash skips these
if not safe_bash:
    # ... gates 1-3 ...

# Counter runs for ALL actions (including safe bash)
actions_since = increment_counter(session_state)

# Gate 4 — only blocks non-safe
if not safe_bash and actions_since > actions_limit:
    smart_block(...)
```

Full working file: `sr-dev-workspace/.claude/hooks/universal-gate-enforcer.py`

## Files to Update
- `isagawa-kernel/.claude/hooks/universal-gate-enforcer.py` — replace with sr-dev-workspace version
- Then sync to all repos per sync rule

## Testing
Deployed in sr-dev-workspace 2026-03-22. Counter confirmed incrementing for both safe (`pwd`) and non-safe (`date`) bash commands. Soak testing before pushing to master.
