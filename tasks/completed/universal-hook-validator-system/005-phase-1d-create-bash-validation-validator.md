# Task 005: Phase 1d - Create bash_validation.py Validator

**Deliverable:** isagawa-kernel/lib/validators/bash_validation.py (new module)

**Type:** BUILD (create new module)

**Dependencies:** Task 002 (lib/validators/ directory exists)

**Status:** ⏳ PENDING

---

## Summary

Create a new bash command safety validator. This module checks for dangerous or protocol-violating bash commands:
- No `cd` in commands (breaks hook path resolution)
- Future enhancements: no force push, no dangerous pipes, etc.

This is a new module (not extracted from existing code) but follows the modular validator pattern.

---

## Validator Signature

```python
def check(command: str) -> list[str]:
    """
    Check bash command for safety violations.

    Args:
        command: Bash command string from Bash tool input

    Returns:
        List of violation strings (empty = safe)

    Examples:
        >>> check("cd /some/path && git log")
        ["Bash command uses 'cd' (breaks hook path resolution)"]

        >>> check("git log --oneline")
        []  # Safe command
    """
```

---

## Violations to Check

### 1. cd Command (CRITICAL)

Pattern: `cd` as a standalone command or piped chain starter

Examples that should **BLOCK**:
- `cd /path && git log`
- `cd ..; ls -la`
- `cd ~/project; make build`
- ` cd something` (with leading space)

Examples that should **PASS** (not blocked):
- `mkdir -p /path/to/dir` (mkdir, not cd)
- `git commit -m "cd implementation"` (cd in string literal)
- Comments: `# cd to directory first`
- Variable names: `start_directory="/tmp"`

Why `cd` is blocked:
- Hook runs from a specific directory (relative path context)
- If bash changes directory with `cd`, hook loses context
- Subsequent relative path operations fail
- Protocol: Always use absolute paths or do not change directory

---

## Implementation Strategy

1. Create check() function following signature above
2. Detect `cd` command in bash string
3. Distinguish between:
   - Actual `cd` command (block)
   - `cd` in string literals (allow)
   - `cd` in comments (allow)
   - `cd` in variable names (allow)
4. Return violation list if `cd` found, empty list otherwise
5. Make extensible for future checks (git force push, etc.)

---

## Extensibility Pattern

The module should be structured to allow future additions:

```python
def check_cd(command: str) -> list[str]:
    """Check for cd command."""
    # Implementation

def check_force_push(command: str) -> list[str]:
    """Check for force push (future)."""
    # Implementation (stub)

def check(command: str) -> list[str]:
    """Main check function that runs all sub-checks."""
    violations = []
    violations.extend(check_cd(command))
    # violations.extend(check_force_push(command))  # Future
    return violations
```

---

## Acceptance Criteria

- [x] File created at: `isagawa-kernel/lib/validators/bash_validation.py`
- [x] Function `check(command) -> list[str]` implemented
- [x] Detects `cd` command in bash strings
- [x] Returns violation when `cd` is found as standalone command
- [x] Returns empty list for safe commands
- [x] Handles string literals gracefully (doesn't block `cd` in strings)
- [x] Handles comments gracefully (doesn't block `cd` in comments)
- [x] Handles variable names gracefully
- [x] Extensible structure for future validators
- [x] Docstring includes signature and examples
- [x] No hard-coded workspace names

---

## Implementation Notes

**Detecting `cd` command:**

Use regex or simple string matching:

```python
import re

def check_cd(command: str) -> list[str]:
    """Check for cd command in bash."""
    # Skip if cd is in quotes
    # Remove quoted strings first
    cmd_without_quotes = re.sub(r'["\'].*?["\']', '', command)

    # Check for cd as a standalone command or with pipes
    if re.search(r'(^|\s|;|\|)\bcd\b(\s|;|$|\&)', cmd_without_quotes):
        return ["Bash command uses 'cd' (breaks hook path resolution)"]

    return []
```

---

## Verification (Gate L1)

```bash
cd /d/my_ai_projects/isagawa-kernel

# Check file exists
test -f lib/validators/bash_validation.py && echo "✓ File exists"

# Check syntax
python3 -m py_compile lib/validators/bash_validation.py && echo "✓ Syntax valid"

# Check function exists
python3 -c "from lib.validators.bash_validation import check; print('✓ Function importable')"
```

**Expected Output:**
```
✓ File exists
✓ Syntax valid
✓ Function importable
```

---

## Locations

- **Target:** `/d/my_ai_projects/isagawa-kernel/lib/validators/bash_validation.py`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

---

## Notes

- This is Phase 1, subtask d (create bash_validation.py)
- New module (not extracted) but follows modular pattern
- Extensible design allows future checks (git force push, dangerous pipes, etc.)
- Output will be imported by workspace thin orchestrators in Phases 2-5

