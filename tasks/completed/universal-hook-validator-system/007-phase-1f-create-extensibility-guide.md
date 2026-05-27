# Task 007: Phase 1f - Create EXTENSIBILITY.md Guide

**Deliverable:** isagawa-kernel/lib/validators/EXTENSIBILITY.md (documentation)

**Type:** BUILD (documentation)

**Dependencies:** Task 002 (lib/validators/ directory exists)

**Status:** ⏳ PENDING

---

## Summary

Create comprehensive documentation showing how to add new validators to the shared library. This guide enables:
- Future team members to add new validators without modifying core code
- Clear examples and patterns
- Specification of validator signature and behavior
- Examples of adding common validation patterns (git safety, test isolation, etc.)

---

## Document Structure

### 1. Introduction

- What is a validator?
- Why modular validators?
- When to add a new validator
- Design principles (SOLID: Single Responsibility)

### 2. Validator Signature

```python
def check(input_data, config) -> list[str]:
    """
    Validate input and return violations.

    Args:
        input_data: Tool input dict or string (depends on validator)
        config: Domain configuration dict (for future per-workspace config)

    Returns:
        List of violation strings. Empty list = pass.
    """
```

### 3. Validator Template

```python
# validators/my_new_check.py

def check(input_data, config=None) -> list[str]:
    """
    Check for my new concern.

    Args:
        input_data: Input to validate
        config: Optional per-domain config

    Returns:
        List of violation strings (empty = pass)

    Examples:
        >>> check("safe_input")
        []

        >>> check("bad_input")
        ["Violation description"]
    """
    violations = []

    # Your validation logic here
    if bad_condition(input_data):
        violations.append("Violation description with context")

    return violations
```

### 4. Example 1: Adding a git Validator

Full example of adding git safety checks:

**File:** `validators/git_validation.py`

```python
def check(tool_input, config=None) -> list[str]:
    """Check git command safety."""
    violations = []
    command = tool_input.get('command', '')

    # Check for force push
    if '--force' in command or '-f' in command:
        violations.append("Git command uses '--force' (dangerous in shared repos)")

    # Check for force add
    if 'git add --force' in command:
        violations.append("Git command uses '--force' with add (bypasses .gitignore)")

    return violations
```

**Usage in hook:**

```python
from lib.validators import git_validation

# In main():
if tool_name == 'Bash':
    command = tool_input.get('command', '')
    violations = git_validation.check({'command': command})
    if violations:
        common.smart_block(violations, "Git safety")
```

### 5. Example 2: Adding a test Isolation Validator

Example of checking test isolation:

**File:** `validators/test_isolation.py`

```python
def check(file_path, content, config=None) -> list[str]:
    """Check test isolation (no shared state between tests)."""
    violations = []

    # Check for module-level state modifications
    if 'os.environ[' in content and not 'test_' in file_path:
        violations.append("Modifying os.environ outside of test function (bad isolation)")

    return violations
```

### 6. Integration Checklist

When adding a new validator:

1. [ ] Create new file: `validators/my_validator.py`
2. [ ] Implement `check()` function with signature
3. [ ] Add docstring with examples
4. [ ] Test L1: `from lib.validators import my_validator` succeeds
5. [ ] Test L2: Call check() on valid input, expect empty list
6. [ ] Test L3: Call check() on known violations, expect violations
7. [ ] Update workspace hooks to call new validator (if desired)
8. [ ] Document in EXTENSIBILITY.md

### 7. Future Validator Ideas

These are good candidates for future validators:

1. **git_validation.py** — Force push detection, force add detection
2. **test_isolation.py** — Test state leakage, shared fixtures
3. **performance_validation.py** — Slow imports, expensive operations
4. **security_validation.py** — SQL injection patterns, XSS vulnerabilities
5. **architecture_validation.py** — Circular imports, layer violations

---

## Acceptance Criteria

- [x] File created at: `isagawa-kernel/lib/validators/EXTENSIBILITY.md`
- [x] Document includes validator signature specification
- [x] Includes complete template for new validators
- [x] Includes at least 2 full examples (git, test isolation)
- [x] Examples are runnable and correct
- [x] Integration checklist included
- [x] Future validator ideas documented
- [x] Clear explanation of why modular approach matters
- [x] Links to SOLID principles or relevant resources

---

## Verification (Gate L1)

```bash
cd /d/my_ai_projects/isagawa-kernel

# Check file exists
test -f lib/validators/EXTENSIBILITY.md && echo "✓ File exists"

# Check basic structure (file is readable markdown)
test -s lib/validators/EXTENSIBILITY.md && echo "✓ File has content"

# Check for key sections
grep -q "Validator Signature" lib/validators/EXTENSIBILITY.md && echo "✓ Signature documented"
grep -q "Example" lib/validators/EXTENSIBILITY.md && echo "✓ Examples included"
grep -q "Checklist" lib/validators/EXTENSIBILITY.md && echo "✓ Checklist included"
```

**Expected Output:**
```
✓ File exists
✓ File has content
✓ Signature documented
✓ Examples included
✓ Checklist included
```

---

## Locations

- **Target:** `/d/my_ai_projects/isagawa-kernel/lib/validators/EXTENSIBILITY.md`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

---

## Notes

- This is Phase 1, subtask f (create EXTENSIBILITY.md)
- Documentation, not code
- Enables future team members to add validators independently
- Examples should be realistic and tested

