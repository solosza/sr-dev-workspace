# Task 004: Phase 1c - Create state_validation.py Validator

**Deliverable:** isagawa-kernel/lib/validators/state_validation.py (extracted from sr_dev-gate-enforcer.py)

**Type:** BUILD (extract and refactor)

**Dependencies:** Task 002 (lib/validators/ directory exists)

**Status:** ⏳ PENDING

---

## Summary

Extract state validation logic from sr_dev-gate-enforcer.py (lines 258-329) and create a modular validator that enforces the anchor ceremony protocol. This module checks:
- Anchor ceremony completion (anchor_ceremony object present)
- Required fields in anchor_ceremony: protocol_read_timestamp, lessons_read_timestamp, actions_reviewed_count, violations_found, next_action_stated, ceremony_output_generated
- Session state consistency (future enhancement)
- Protocol hash verification (future enhancement)

---

## Validator Signature

```python
def check(session_state_path: str) -> list[str]:
    """
    Check session state for protocol and ceremony compliance.

    Args:
        session_state_path: Path to .claude/state/session_state.json

    Returns:
        List of violation strings (empty = compliant)

    Examples:
        >>> check(".claude/state/session_state.json")
        []  # All required fields present

        >>> check(".claude/state/session_state.json")  # Missing anchor_ceremony
        ["Anchor ceremony incomplete: missing anchor_ceremony object"]
    """
```

---

## Violations to Check

### 1. Anchor Ceremony Missing

Patterns:
- `anchor_ceremony` object not present in session_state.json
- Error: "Anchor ceremony incomplete: missing anchor_ceremony object"

### 2. Anchor Ceremony Incomplete (Missing Required Fields)

Required fields:
- `protocol_read_timestamp` — when protocol was last read
- `lessons_read_timestamp` — when lessons were last read
- `actions_reviewed_count` — number of actions reviewed since anchor
- `violations_found` — number of violations found
- `next_action_stated` — what's the next action?
- `ceremony_output_generated` — was ceremony output generated?

If any missing: "Anchor ceremony incomplete: missing required field [field_name]"

### 3. Session State File Not Found

If session_state.json doesn't exist: "Session state not found at [path]"

### 4. Session State Invalid JSON

If JSON parse fails: "Session state JSON invalid: [error]"

---

## Implementation Strategy

1. Read source from sr_dev-gate-enforcer.py (lines 258-329)
2. Create check() function following signature above
3. Load session_state.json and validate structure
4. Check for anchor_ceremony object
5. Verify all required fields present
6. Return empty list if compliant, violation list if issues found
7. Make requirements configurable per domain (future)

---

## Acceptance Criteria

- [x] File created at: `isagawa-kernel/lib/validators/state_validation.py`
- [x] Function `check(session_state_path) -> list[str]` implemented
- [x] Checks for anchor_ceremony object presence
- [x] Checks for all required fields in anchor_ceremony
- [x] Returns empty list when session state is compliant
- [x] Returns violation strings when issues found
- [x] Handles missing/invalid session_state.json gracefully
- [x] Handles JSON parse errors gracefully
- [x] Patterns match original sr_dev-gate-enforcer.py behavior
- [x] Docstring includes signature and examples
- [x] No hard-coded workspace names

---

## Verification (Gate L1)

```bash
cd /d/my_ai_projects/isagawa-kernel

# Check file exists
test -f lib/validators/state_validation.py && echo "✓ File exists"

# Check syntax
python3 -m py_compile lib/validators/state_validation.py && echo "✓ Syntax valid"

# Check function exists
python3 -c "from lib.validators.state_validation import check; print('✓ Function importable')"
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
- Lines: 258-329 (anchor ceremony checks)

Extract anchor ceremony validation logic and refactor into check() signature.

---

## Locations

- **Target:** `/d/my_ai_projects/isagawa-kernel/lib/validators/state_validation.py`
- **Source:** `/d/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

---

## Notes

- This is Phase 1, subtask c (create state_validation.py)
- Enforces the anchor ceremony protocol (CLAUDE.md: First Action Rule)
- Output will be imported by workspace thin orchestrators in Phases 2-5

