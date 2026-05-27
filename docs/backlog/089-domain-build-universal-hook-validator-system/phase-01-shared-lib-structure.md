# Phase 1: Create Shared Lib/Validators Structure

**Status:** Ready for task-builder decomposition

**Deliverable:** `isagawa-kernel/lib/validators/` with 4 modular validators + extensibility guide

---

## What Gets Built

### File Structure

```
isagawa-kernel/
├── lib/
│   ├── __init__.py
│   └── validators/
│       ├── __init__.py
│       ├── code_quality.py         (extracted from sr_dev-gate-enforcer.py)
│       ├── state_validation.py     (extracted from sr_dev-gate-enforcer.py)
│       ├── bash_validation.py      (extracted from sr_dev-gate-enforcer.py + cd check)
│       ├── common.py               (shared utilities, block functions)
│       └── EXTENSIBILITY.md        (how to add new validators)
```

### Module 1: code_quality.py

Checks for development anti-patterns:
- Debug statements (print, console.log, debugger, etc.)
- Hardcoded secrets (password=, api_key=, etc.)
- Wildcard imports (from X import *)
- Skipped tests (.skip, @pytest.mark.skip, xit, etc.)
- File size > 300 lines

**Source:** Extract from sr_dev-gate-enforcer.py (lines 31-244, with utilities refactored)

**Input:** `tool_input` dict with file_path, content
**Output:** `list[str]` of violations (empty = pass)

### Module 2: state_validation.py

Checks for protocol and ceremony compliance:
- Anchor ceremony completion (anchor_ceremony object present with all required fields)
- Protocol hash verification (future enhancement)
- Session state consistency (future enhancement)

**Source:** Extract from sr_dev-gate-enforcer.py (lines 258-329, anchor ceremony validation)

**Input:** `tool_input` dict + path to session_state.json
**Output:** `list[str]` of violations

### Module 3: bash_validation.py

Checks bash command safety:
- No `cd` in commands (breaks hook path resolution)
- Future: no force push, no dangerous pipe chains, etc.

**Source:** New module (add cd detection + extensible framework)

**Input:** `command` string from bash tool_input
**Output:** `list[str]` of violations

### Module 4: common.py

Shared utilities:
- `should_skip(file_path)` — check if file should be skipped (infrastructure, tests, etc.)
- `get_extension(file_path)` — file extension helper
- `smart_block(violations, category)` — format and output violation message
- `state_block(violations)` — format state validation error
- `bash_block(violations)` — format bash validation error

**Source:** Extract from sr_dev-gate-enforcer.py utility functions

---

## How Validators Are Used

Each workspace's thin hook calls them:

```python
from validators.code_quality import check as check_code_quality
from validators.state_validation import check as check_state
from validators.bash_validation import check as check_bash

# In main():
if tool_name in ('Write', 'Edit'):
    violations = check_code_quality(tool_input, domain_config)
    if violations: smart_block(violations, "Code quality")

    violations = check_state(tool_input, session_state_path)
    if violations: state_block(violations)

elif tool_name == 'Bash':
    command = tool_input.get('command', '')
    violations = check_bash(command)
    if violations: bash_block(violations)
```

---

## Extensibility Pattern (EXTENSIBILITY.md)

Guide for adding new validators:

1. **Create new module** in `validators/new_check.py`
2. **Follow signature:** `def check(input_data, config) -> list[str]`
3. **Return list of violations** (empty = pass)
4. **Add to common.py** if it has a new block type
5. **Document in EXTENSIBILITY.md** with example
6. **Update workspace hooks** to call it (if desired)

Example: Adding a git validator

```python
# validators/git_validation.py
def check(tool_input, config):
    """Check git command safety."""
    command = tool_input.get('command', '')

    if '--force' in command or '-f' in command:
        return ["Bash command uses '--force' (dangerous in shared repos)"]

    return []
```

Then workspace hooks add: `violations = check_git(tool_input)`

---

## Tasks for Phase 0 + Phase 1

This phase decomposes into atomic tasks:

| Task | Action |
|------|--------|
| 0.1 | Create feature branch in isagawa-kernel (e.g., feature/089-universal-validators) |
| 1.1 | Create `isagawa-kernel/lib/` directory structure |
| 1.2 | Create `validators/__init__.py` (empty) |
| 1.3 | Extract `code_quality.py` from sr_dev (debug, secrets, wildcards, skipped, size checks) |
| 1.4 | Extract `state_validation.py` from sr_dev (anchor ceremony checks) |
| 1.5 | Create `bash_validation.py` with cd detection + framework |
| 1.6 | Create `common.py` with shared utilities (skip, extension, block functions) |
| 1.7 | Create `EXTENSIBILITY.md` guide with examples |
| 1.8 | Test: Import all modules, verify no errors (L1) |
| 1.9 | Test: Run validators on sample input, verify behavior (L2) |
| 1.10 | Test: Run validators on known-bad input, verify violations (L3) |

---

## Acceptance Criteria

- [ ] All 4 modules exist and are importable
- [ ] Each validator follows consistent signature: `check(input, config) -> list[str]`
- [ ] No hard-coded workspace names or domain-specific logic
- [ ] All existing rules from sr_dev-gate-enforcer.py are preserved (behavior parity)
- [ ] common.py utilities work across all validators
- [ ] EXTENSIBILITY.md clearly documents how to add new validators
- [ ] L1 test: Import succeeds
- [ ] L2 test: Validators run without errors on valid input
- [ ] L3 test: Validators correctly identify violations

---

## References

- Source: `sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py` (343 lines)
- SOLID: Single Responsibility Principle (each validator = one concern)
- Similar patterns: pytest plugins, Django validators, eslint rules

