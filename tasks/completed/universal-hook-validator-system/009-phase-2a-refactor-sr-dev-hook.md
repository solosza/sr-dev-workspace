# Task 009: Phase 2a - Refactor sr_dev Hook to Thin Orchestrator

**Deliverable:** sr_dev-gate-enforcer.py refactored from ~343 lines to ~45 lines (thin orchestrator)

**Type:** BUILD (refactor)

**Dependencies:** Task 008 (L1 tests pass for all validators)

**Status:** ⏳ PENDING

---

## Summary

Replace the monolithic sr_dev-gate-enforcer.py with a thin orchestrator that imports shared validators from isagawa-kernel/lib/validators/. Reduces code duplication, enables pattern reuse for other workspaces.

---

## Location

- **Target:** `sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py`
- **Backup:** `sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py.backup`
- **Remove:** `sr_dev_workspace/.claude/hooks/validators/` directory

---

## New Hook Code (~45 lines)

```python
#!/usr/bin/env python3
"""Sr Dev Gate Enforcer — thin orchestrator using shared validators."""

import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[3]))
try:
    from isagawa_kernel.lib.validators import code_quality, state_validation, bash_validation, common
except ImportError:
    sys.exit(0)

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})

    if tool_name in ('Write', 'Edit'):
        file_path = tool_input.get('file_path', '').replace('\\', '/')
        if not common.should_skip(file_path):
            content = tool_input.get('content', '') or tool_input.get('new_string', '')
            if content:
                violations = code_quality.check(file_path, content)
                if violations:
                    common.smart_block(violations, "Code quality")

        session_state_path = Path('.claude/state/session_state.json')
        violations = state_validation.check(str(session_state_path))
        if violations:
            common.state_block(violations)

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

## Atomic Actions

1. Backup current hook file
2. Create new thin orchestrator
3. Remove validators/ directory

---

## Acceptance Criteria

- [x] New hook file created and syntax valid
- [x] sys.path resolves to isagawa-kernel
- [x] Shared validators import without errors
- [x] Behavior identical to original (regression test)
- [x] Backup saved
- [x] Local validators/ removed

---

## Locations

- **Workspace:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\`
- **Hook:** `.\.claude\hooks\sr_dev-gate-enforcer.py`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

