# Task 006: Phase 1e - Create common.py Utilities Module

**Deliverable:** isagawa-kernel/lib/validators/common.py (shared utilities)

**Type:** BUILD (extract and refactor)

**Dependencies:** Task 002 (lib/validators/ directory exists)

**Status:** ⏳ PENDING

---

## Summary

Create a shared utilities module with helper functions used by all validators and workspace hooks. Extract common patterns from sr_dev-gate-enforcer.py and create reusable functions for:
- File skipping logic (skip infrastructure, tests, etc.)
- File extension detection
- Violation blocking and error message formatting
- State block formatting
- Bash block formatting

---

## Utilities to Implement

### 1. should_skip(file_path: str) -> bool

Check if a file should be skipped from validation (infrastructure, tests, generated files, etc.).

**Files to skip:**
- `.claude/` subdirectories (hooks, state, commands, etc.)
- `.git/` directories
- `__pycache__/`
- `.venv/`, `venv/`, `env/`
- `node_modules/`
- `.egg-info/`
- Test files: `test_*.py`, `*_test.py`, `tests.py`
- Generated files: `.pyc`, `.pyo`, `.so`
- Lock files: `package-lock.json`, `poetry.lock`, `Pipfile.lock`
- Vendor directories: `vendor/`, `dist/`, `build/`

**Signature:**

```python
def should_skip(file_path: str) -> bool:
    """
    Check if file should be skipped from validation.

    Args:
        file_path: Path to the file

    Returns:
        True if file should be skipped, False otherwise

    Examples:
        >>> should_skip(".claude/hooks/test.py")
        True

        >>> should_skip("tests/unit_test.py")
        True

        >>> should_skip("src/main.py")
        False
    """
```

---

### 2. get_extension(file_path: str) -> str

Get file extension.

**Signature:**

```python
def get_extension(file_path: str) -> str:
    """
    Get file extension.

    Args:
        file_path: Path to the file

    Returns:
        Extension (with dot) or empty string

    Examples:
        >>> get_extension("script.py")
        ".py"

        >>> get_extension(".gitignore")
        ".gitignore"  # No extension
    """
```

---

### 3. smart_block(violations: list[str], category: str) -> None

Format and output a code quality violation, then exit with code 2 (blocked).

**Signature:**

```python
def smart_block(violations: list[str], category: str) -> None:
    """
    Format and block on code quality violations.

    Args:
        violations: List of violation strings
        category: Category name (e.g., "Code quality", "Syntax")

    Returns:
        None (exits with code 2)

    Examples:
        >>> smart_block(["Debug statement: print() at line 5"], "Code quality")
        # Outputs error message and exits with code 2
    """
```

**Behavior:**
- Print error header: `BLOCKED: [category]`
- Print each violation on new line
- Print footer: "Fix violations and retry"
- Exit with code 2

**Example output:**

```
BLOCKED: Code quality

  • Debug statement: print() at line 5
  • Hardcoded secret: password at line 12

Fix violations and retry.
```

---

### 4. state_block(violations: list[str]) -> None

Format and block on state validation violations (anchor ceremony failures).

**Signature:**

```python
def state_block(violations: list[str]) -> None:
    """
    Format and block on state validation violations.

    Args:
        violations: List of violation strings

    Returns:
        None (exits with code 2)

    Examples:
        >>> state_block(["Anchor ceremony incomplete: missing protocol_read_timestamp"])
        # Outputs error message and exits with code 2
    """
```

**Behavior:**
- Print error header: `BLOCKED: Anchor ceremony violation`
- Print each violation on new line
- Print footer: "Invoke /kernel/anchor to reset ceremony"
- Exit with code 2

**Example output:**

```
BLOCKED: Anchor ceremony violation

  • Anchor ceremony incomplete: missing protocol_read_timestamp

Invoke /kernel/anchor to reset ceremony.
```

---

### 5. bash_block(violations: list[str]) -> None

Format and block on bash validation violations.

**Signature:**

```python
def bash_block(violations: list[str]) -> None:
    """
    Format and block on bash validation violations.

    Args:
        violations: List of violation strings

    Returns:
        None (exits with code 2)

    Examples:
        >>> bash_block(["Bash command uses 'cd' (breaks hook path resolution)"])
        # Outputs error message and exits with code 2
    """
```

**Behavior:**
- Print error header: `BLOCKED: Bash safety violation`
- Print each violation on new line
- Print footer: "Use absolute paths, avoid cd"
- Exit with code 2

**Example output:**

```
BLOCKED: Bash safety violation

  • Bash command uses 'cd' (breaks hook path resolution)

Use absolute paths, avoid cd.
```

---

## Acceptance Criteria

- [x] File created at: `isagawa-kernel/lib/validators/common.py`
- [x] Function `should_skip(file_path)` implemented
- [x] Function `get_extension(file_path)` implemented
- [x] Function `smart_block(violations, category)` implemented
- [x] Function `state_block(violations)` implemented
- [x] Function `bash_block(violations)` implemented
- [x] All functions have docstrings with examples
- [x] should_skip covers all infrastructure directories
- [x] Block functions print helpful messages and exit(2)
- [x] Block functions handle multiple violations
- [x] No hard-coded workspace names
- [x] Utilities extracted from sr_dev-gate-enforcer.py preserve behavior

---

## Verification (Gate L1)

```bash
cd /d/my_ai_projects/isagawa-kernel

# Check file exists
test -f lib/validators/common.py && echo "✓ File exists"

# Check syntax
python3 -m py_compile lib/validators/common.py && echo "✓ Syntax valid"

# Check functions exist
python3 << 'EOF'
from lib.validators.common import (
    should_skip,
    get_extension,
    smart_block,
    state_block,
    bash_block
)
print("✓ All functions importable")
EOF
```

**Expected Output:**
```
✓ File exists
✓ Syntax valid
✓ All functions importable
```

---

## Source Reference

Original sr_dev-gate-enforcer.py:
- File: `sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py`
- Utility functions scattered throughout (lines 1-30, 330-343)

Extract utilities and refactor into organized common.py module.

---

## Locations

- **Target:** `/d/my_ai_projects/isagawa-kernel/lib/validators/common.py`
- **Source:** `/d/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

---

## Notes

- This is Phase 1, subtask e (create common.py)
- Shared utilities imported by all workspace hooks
- Output will be imported by workspace thin orchestrators in Phases 2-5

