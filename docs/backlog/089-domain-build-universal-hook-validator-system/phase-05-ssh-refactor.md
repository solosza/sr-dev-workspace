# Phase 5: Refactor platform-ssh to Use Shared Lib

**Status:** Depends on Phase 1 + Phase 2 completion

**Deliverable:** platform-ssh hook refactored to thin orchestrator using shared validators + L1/L2/L3 validation

---

## Workspace Details

- **Path:** `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh`
- **Domain:** `ssh`
- **Current hook:** `.claude/hooks/ssh-gate-enforcer.py` (exists, structure similar to sr_dev)

---

## Current Hook Analysis

platform-ssh likely has similar structure to sr_dev-gate-enforcer.py because:
- Both are domain specs in isagawa-qa org
- Both created around same time (2026-03-23)
- Both have gate-contract.md defining validation rules

**Discovery tasks:**
- List current validators in ssh-gate-enforcer.py
- Identify any SSH-specific validation rules beyond standard code quality
- Document findings

---

## Refactoring (Standard Pattern + SSH Specifics)

Follow same pattern as Phase 2/3/4 with one enhancement:

If ssh-gate-enforcer.py has **SSH-specific validators** (e.g., sshd_config syntax checks, key format validation):
- Document them as findings
- Note for Phase 6 / future backlog as potential shared validator enhancements
- Keep them in thin orchestrator for now (they're domain-specific)

**Standard refactoring:**

1. Backup current ssh-gate-enforcer.py
2. Extract shared validators (code quality, state, bash) to use from lib/validators
3. Keep any SSH-specific validators local
4. Create thin orchestrator
5. Test L1/L2/L3
6. Verify Claude Code integration

**Orchestrator template (with potential SSH-specific validators):**

```python
#!/usr/bin/env python3
"""SSH Gate Enforcer — thin orchestrator using shared validators."""

import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[3] / 'isagawa-kernel'))
from lib.validators import code_quality, state_validation, bash_validation, common

# Local SSH-specific validators (if any)
def check_ssh_config(file_path, content):
    """SSH-specific validation (e.g., sshd_config syntax)."""
    # SSH-specific rules go here
    return []

def main():
    data = json.load(sys.stdin) if sys.stdin else {}
    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})
    domain = 'ssh'

    if tool_name in ('Write', 'Edit'):
        file_path = tool_input.get('file_path', '').replace('\\', '/')

        if not common.should_skip(file_path):
            content = tool_input.get('content', '') or tool_input.get('new_string', '')
            if content:
                violations = code_quality.check(file_path, content)
                if violations: common.smart_block(violations, "Code quality")

                # SSH-specific checks
                if 'sshd_config' in file_path:
                    violations = check_ssh_config(file_path, content)
                    if violations: common.smart_block(violations, "SSH config")

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

## Tasks for Phase 5

| Task | Sequence |
|------|----------|
| 1 | Analyze: Review current ssh-gate-enforcer.py |
| 2 | Identify: Document any SSH-specific validators |
| 3 | Backup: Copy current hook file |
| 4 | Create: Thin orchestrator (ssh-gate-enforcer.py) |
| 5 | Remove: Local validators/ directory if exists |
| 6 | Update: sys.path to point to isagawa-kernel/lib/validators |
| 7 | Implement: Any SSH-specific validators locally (if discovered) |
| 8 | Test L1: Hook imports without errors |
| 9 | Test L2: Verify all validators work (shared + local) |
| 10 | Test L3: Feed known violations, verify blocking |
| 11 | Verify: Claude Code hook integration works |

---

## Acceptance Criteria

- [ ] Current hook backed up
- [ ] New thin orchestrator created and valid
- [ ] Hook imports shared validators without errors (L1)
- [ ] All validators work correctly (L2)
- [ ] SSH-specific validators work if discovered (L2)
- [ ] L3: Test suite with known violations all blocked
- [ ] Behavior preserves original validation rules
- [ ] sys.path resolves correctly to isagawa-kernel

---

## Notes

- Can execute **in parallel with Phase 3 and Phase 4** (all depend on Phase 1 only)
- Platform-ssh is a domain spec: may have been tested more thoroughly than other workspaces
- Any SSH-specific validators discovered are candidates for Phase 6 / future backlog

