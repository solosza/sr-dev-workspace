# Task 003: Phase 1b - Create code_quality.py Validator

**Deliverable:** isagawa-kernel/lib/validators/code_quality.py (extracted from sr_dev-gate-enforcer.py)

**Type:** BUILD (extract and refactor)

**Dependencies:** Task 002 (lib/validators/ directory exists)

**Status:** ⏳ PENDING

---

## Summary

Extract code quality validation logic from sr_dev-gate-enforcer.py (lines 31-244) and create a modular, reusable validator. This module checks for:
- Debug statements (print, console.log, debugger, etc.)
- Hardcoded secrets (password=, api_key=, etc.)
- Wildcard imports (from X import *)
- Skipped tests (.skip, @pytest.mark.skip, xit, etc.)
- File size > 300 lines

---

## Validator Signature

```python
def check(file_path: str, content: str) -> list[str]:
    """
    Check code for quality violations.

    Args:
        file_path: Path to the file being checked
        content: File content as string

    Returns:
        List of violation strings (empty = no violations)

    Examples:
        >>> check("test.py", "print('debug')")
        ["Debug statement: print() at line N"]

        >>> check("app.py", "password = 'secret123'")
        ["Hardcoded secret: password at line N"]

        >>> check("clean.py", "import os")
        []
    """
```

---

## Violations to Check

### 1. Debug Statements

Patterns:
- `print(` (not in strings)
- `console.log(` (JavaScript)
- `debugger` (JavaScript keyword)
- `pdb.set_trace()` (Python debugging)
- `ipdb.set_trace()` (IPython debugging)
- `logger.debug(` (but allow for structured logging)

### 2. Hardcoded Secrets

Patterns:
- `password =` or `password:` (case-insensitive)
- `api_key =` or `api_key:`
- `secret =` or `secret:`
- `token =` or `token:` (but exclude comments like `# token: `)
- `sk_live_` or `sk_test_` (Stripe keys)
- `pk_live_` or `pk_test_`

### 3. Wildcard Imports

Patterns:
- `from X import *` (any module)
- `from * import X` (invalid Python, catch if present)

### 4. Skipped Tests

Patterns:
- `.skip` (pytest.mark.skip, unittest.skip)
- `@pytest.mark.skip`
- `@skip` (decorator)
- `xit(` or `xdescribe(` (Jasmine)
- `xit` (mocha)
- `it.skip(` (mocha)

### 5. File Size

- Files > 300 lines should trigger warning: "File exceeds 300 lines (N lines) — consider breaking into modules"

---

## Implementation Strategy

1. Read source from sr_dev-gate-enforcer.py (lines 31-244)
2. Extract pattern lists into module-level constants
3. Create check() function following signature above
4. Handle edge cases:
   - Skip comments (lines starting with # or //)
   - Skip string literals (content in quotes)
   - Handle multi-line strings gracefully
5. Preserve all original validation rules (no behavior changes)
6. Make module-level constants configurable per domain (future)

---

## Acceptance Criteria

- [x] File created at: `isagawa-kernel/lib/validators/code_quality.py`
- [x] Function `check(file_path, content) -> list[str]` implemented
- [x] All 5 violation types checked (debug, secrets, wildcard, skipped, size)
- [x] Returns empty list for clean code
- [x] Returns list of violation strings for bad code
- [x] Patterns match original sr_dev-gate-enforcer.py behavior (regression test)
- [x] No hard-coded workspace names or domain-specific logic
- [x] Docstring includes signature and examples
- [x] Comment-aware: doesn't flag violations in comments or strings
- [x] Line number reported for each violation (if possible)

---

## Verification (Gate L1)

```bash
cd /d/my_ai_projects/isagawa-kernel

# Check file exists
test -f lib/validators/code_quality.py && echo "✓ File exists"

# Check syntax
python3 -m py_compile lib/validators/code_quality.py && echo "✓ Syntax valid"

# Check function exists
python3 -c "from lib.validators.code_quality import check; print('✓ Function importable')"
```

**Expected Output:**
```
✓ File exists
✓ Syntax valid
✓ Function importable
```

---

## Source Reference

Original sr_dev-gate-enforcer.py:
- File: `sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py`
- Lines: 31-244 (code quality checks)
- Total lines: 343

Extract these functions/patterns and refactor into check() signature.

---

## Locations

- **Target:** `/d/my_ai_projects/isagawa-kernel/lib/validators/code_quality.py`
- **Source:** `/d/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

---

## Notes

- This is Phase 1, subtask b (create code_quality.py)
- Follows modular validator pattern: one concern per module
- Output will be imported by workspace thin orchestrators in Phases 2-5

