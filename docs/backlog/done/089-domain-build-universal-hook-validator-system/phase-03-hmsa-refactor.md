# Phase 3: Refactor hmsa-healthcare-qa to Use Shared Lib

**Status:** Depends on Phase 1 + Phase 2 completion

**Deliverable:** hmsa-healthcare-qa hook refactored to thin orchestrator using shared validators + L1/L2/L3 validation

---

## Workspace Details

- **Path:** `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa`
- **Domain:** `healthcare-qa`
- **Current hooks:** To be discovered in Phase 1.1 (discovery task)

---

## Discovery Phase (1.1)

First, need to determine:
1. Does hmsa-healthcare-qa have existing hooks in `.claude/hooks/`?
2. If yes, what validators are implemented?
3. What domain name is used?
4. Are there domain-specific validation rules beyond standard code quality?

**Discovery tasks:**
- List `.claude/` directory structure
- Identify existing hook files
- Read current hook(s) to understand what validators are in place
- Document findings in task description

---

## Refactoring (Standard Pattern)

Once discovery complete, follow same pattern as Phase 2:

1. Backup current hooks
2. Create thin orchestrator that imports shared validators
3. Remove local validators directory
4. Configure domain name for this workspace
5. Test L1/L2/L3

**Orchestrator template:**

```python
#!/usr/bin/env python3
"""Healthcare QA Gate Enforcer — thin orchestrator using shared validators."""

import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[3] / 'isagawa-kernel'))
from lib.validators import code_quality, state_validation, bash_validation, common

def main():
    data = json.load(sys.stdin) if sys.stdin else {}
    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})
    domain = 'healthcare-qa'  # This workspace's domain

    # Standard validation pattern (same as Phase 2)
    if tool_name in ('Write', 'Edit'):
        file_path = tool_input.get('file_path', '').replace('\\', '/')
        if not common.should_skip(file_path):
            content = tool_input.get('content', '') or tool_input.get('new_string', '')
            if content:
                violations = code_quality.check(file_path, content)
                if violations: common.smart_block(violations, "Code quality")

        session_state_path = Path('.claude/state/session_state.json')
        violations = state_validation.check(session_state_path)
        if violations: common.state_block(violations)

    elif tool_name == 'Bash':
        command = tool_input.get('command', '')
        violations = bash_validation.check(command)
        if violations: common.bash_block(violations)

    sys.exit(0)

if __name__ == '__main__': main()
```

---

## Tasks for Phase 3

| Task | Sequence |
|------|----------|
| 1 | Discover: List `.claude/` structure in hmsa-healthcare-qa |
| 2 | Discover: Identify current hook files |
| 3 | Discover: Document current validators in use |
| 4 | Backup: Copy current hook file(s) to safe location |
| 5 | Create: Thin orchestrator (healthcare-qa-gate-enforcer.py) |
| 6 | Remove: Local validators/ directory |
| 7 | Update: sys.path to point to isagawa-kernel/lib/validators |
| 8 | Test L1: Hook imports without errors |
| 9 | Test L2: Verify all validators work (code quality, state, bash) |
| 10 | Test L3: Feed known violations, verify blocking |
| 11 | Verify: Claude Code hook integration still works |

---

## Acceptance Criteria

- [ ] Current hooks backed up safely
- [ ] New thin orchestrator created and valid
- [ ] Hook imports shared validators without errors (L1)
- [ ] All validators work correctly (L2)
- [ ] L3: Test suite with known violations all blocked
- [ ] Behavior preserves original validation rules (regression test)
- [ ] sys.path resolves correctly to isagawa-kernel

---

## Notes

- If discovery reveals no existing hooks, create basic orchestrator with all validators enabled
- If discovery reveals domain-specific validators, document in findings (may become future enhancement to shared lib)
- Workspace is self-contained: doesn't depend on sr_dev but can run in parallel

