# Phase 2: Refactor sr_dev_workspace to Use Shared Lib

**Status:** Depends on Phase 1 completion

**Deliverable:** sr_dev-gate-enforcer.py refactored to thin orchestrator using shared validators + L1/L2/L3 validation

---

## What Changes

### Current File
- `.claude/hooks/sr_dev-gate-enforcer.py` (343 lines)
- Contains: debug checks, secret checks, wildcard checks, skipped test checks, file size check, anchor ceremony check, block functions

### New Structure
- `.claude/hooks/sr_dev-gate-enforcer.py` (~45 lines — thin orchestrator only)
- Imports: `from isagawa_kernel.lib.validators import code_quality, state_validation, bash_validation, common`
- No local validators directory (removed)

### New Hook Code

```python
#!/usr/bin/env python3
"""Sr Dev Gate Enforcer — thin orchestrator using shared validators."""

import json
import sys
from pathlib import Path

# Import shared validators from kernel lib
sys.path.insert(0, str(Path(__file__).parents[3] / 'isagawa-kernel'))
from lib.validators import code_quality, state_validation, bash_validation, common

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})
    domain = 'sr_dev'  # Domain configuration for this workspace

    # Code quality checks (Write/Edit only)
    if tool_name in ('Write', 'Edit'):
        file_path = tool_input.get('file_path', '').replace('\\', '/')

        if not common.should_skip(file_path):
            content = tool_input.get('content', '')
            if not content and 'new_string' in tool_input:
                content = tool_input.get('new_string', '')

            if content:
                violations = code_quality.check(file_path, content)
                if violations:
                    common.smart_block(violations, "Code quality")

        # State validation (anchor ceremony)
        session_state_path = Path('.claude/state/session_state.json')
        violations = state_validation.check(session_state_path)
        if violations:
            common.state_block(violations)

    # Bash command validation
    elif tool_name == 'Bash':
        command = tool_input.get('command', '')
        violations = bash_validation.check(command)
        if violations:
            common.bash_block(violations)

    sys.exit(0)

if __name__ == '__main__':
    main()
```

---

## Tasks for Phase 2

| Task | Action |
|------|--------|
| 1 | Backup current sr_dev-gate-enforcer.py |
| 2 | Create new sr_dev-gate-enforcer.py (thin orchestrator above) |
| 3 | Remove validators/ subdirectory from sr_dev hooks (no longer needed) |
| 4 | Update sys.path logic to point to isagawa-kernel/lib/validators |
| 5 | Test: Hook runs without errors (L1) |
| 6 | Test: Hook blocks debug statements correctly (L2) |
| 7 | Test: Hook blocks secrets correctly (L2) |
| 8 | Test: Hook blocks wildcard imports correctly (L2) |
| 9 | Test: Hook blocks cd in bash correctly (L2) |
| 10 | Test: Hook enforces anchor ceremony (L2) |
| 11 | Integration: Feed test suite of violations, verify all blocked (L3) |
| 12 | Verify existing Claude Code hooks still work (PreToolUse invocation) |

---

## Acceptance Criteria

- [ ] New hook file created and syntax is valid (L1)
- [ ] Hook imports shared validators without errors (L1)
- [ ] All 5 validator types work correctly (debug, secrets, wildcard, skipped, size) (L2)
- [ ] Anchor ceremony validation works (L2)
- [ ] Bash cd detection works (L2)
- [ ] Unknown tool types pass through gracefully (L2)
- [ ] L3: Test suite with known violations all blocked correctly
- [ ] Behavior identical to original hook (regression test)
- [ ] sys.path points correctly to isagawa-kernel
- [ ] No validators/ subdirectory needed in sr_dev hooks

---

## Rollback Plan

If issues found:
1. Restore backed up sr_dev-gate-enforcer.py
2. Document the issue in a lesson
3. Fix shared lib and retry

---

## References

- Source hook: `.claude/hooks/sr_dev-gate-enforcer.py` (original, 343 lines)
- Shared lib: `isagawa-kernel/lib/validators/` (created in Phase 1)
- Workspace path: `sr_dev_workspace/`
- Domain: `sr_dev`

