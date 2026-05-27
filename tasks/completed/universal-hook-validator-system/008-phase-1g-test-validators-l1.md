# Task 008: Phase 1g - Test Validators (L1: Imports)

**Deliverable:** All 4 validator modules + common utilities import without errors

**Type:** TEST (Level 1 - structural)

**Dependencies:** Tasks 003-006 (all validators and common.py created)

**Status:** ⏳ PENDING

---

## Summary

Level 1 test: Verify that all validator modules exist, have correct syntax, and are importable. This is a sanity check that the code structure is valid before testing functionality.

---

## Test Cases (L1: Does it exist?)

### Test 1.1: code_quality module imports

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 -c "
from lib.validators import code_quality
print('✓ code_quality module imports')
"
```

**Expected Output:** `✓ code_quality module imports`
**Expected Exit Code:** 0

### Test 1.2: state_validation module imports

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 -c "
from lib.validators import state_validation
print('✓ state_validation module imports')
"
```

**Expected Output:** `✓ state_validation module imports`
**Expected Exit Code:** 0

### Test 1.3: bash_validation module imports

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 -c "
from lib.validators import bash_validation
print('✓ bash_validation module imports')
"
```

**Expected Output:** `✓ bash_validation module imports`
**Expected Exit Code:** 0

### Test 1.4: common module imports

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 -c "
from lib.validators import common
print('✓ common module imports')
"
```

**Expected Output:** `✓ common module imports`
**Expected Exit Code:** 0

### Test 1.5: All validators + common together

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 << 'EOF'
from lib.validators import (
    code_quality,
    state_validation,
    bash_validation,
    common
)
print("✓ All modules import successfully")
EOF
```

**Expected Output:** `✓ All modules import successfully`
**Expected Exit Code:** 0

### Test 1.6: Each module has check() function

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 << 'EOF'
from lib.validators import code_quality, state_validation, bash_validation

# Verify check() functions exist
assert hasattr(code_quality, 'check'), "code_quality.check missing"
assert hasattr(state_validation, 'check'), "state_validation.check missing"
assert hasattr(bash_validation, 'check'), "bash_validation.check missing"

print("✓ All validators have check() function")
EOF
```

**Expected Output:** `✓ All validators have check() function`
**Expected Exit Code:** 0

### Test 1.7: common module has all utility functions

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 << 'EOF'
from lib.validators import common

# Verify utility functions exist
assert hasattr(common, 'should_skip'), "common.should_skip missing"
assert hasattr(common, 'get_extension'), "common.get_extension missing"
assert hasattr(common, 'smart_block'), "common.smart_block missing"
assert hasattr(common, 'state_block'), "common.state_block missing"
assert hasattr(common, 'bash_block'), "common.bash_block missing"

print("✓ All common utility functions exist")
EOF
```

**Expected Output:** `✓ All common utility functions exist`
**Expected Exit Code:** 0

### Test 1.8: EXTENSIBILITY.md exists and readable

```bash
cd /d/my_ai_projects/isagawa-kernel

test -f lib/validators/EXTENSIBILITY.md && \
test -s lib/validators/EXTENSIBILITY.md && \
echo "✓ EXTENSIBILITY.md exists and has content"
```

**Expected Output:** `✓ EXTENSIBILITY.md exists and has content`
**Expected Exit Code:** 0

---

## Comprehensive L1 Test Script

Create and run this test script:

```bash
cd /d/my_ai_projects/isagawa-kernel

python3 << 'EOF'
import sys

def test_imports():
    """Test L1: All modules import without errors."""
    try:
        from lib.validators import (
            code_quality,
            state_validation,
            bash_validation,
            common
        )
        print("✓ All modules import successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_functions():
    """Test L1: All required functions exist."""
    try:
        from lib.validators import (
            code_quality,
            state_validation,
            bash_validation,
            common
        )

        # Validator functions
        assert hasattr(code_quality, 'check')
        assert hasattr(state_validation, 'check')
        assert hasattr(bash_validation, 'check')

        # Common utility functions
        assert hasattr(common, 'should_skip')
        assert hasattr(common, 'get_extension')
        assert hasattr(common, 'smart_block')
        assert hasattr(common, 'state_block')
        assert hasattr(common, 'bash_block')

        print("✓ All required functions exist")
        return True
    except AssertionError as e:
        print(f"✗ Function missing: {e}")
        return False

def test_documentation():
    """Test L1: EXTENSIBILITY.md exists."""
    from pathlib import Path
    ext_file = Path('lib/validators/EXTENSIBILITY.md')
    if ext_file.exists() and ext_file.stat().st_size > 0:
        print("✓ EXTENSIBILITY.md exists and has content")
        return True
    else:
        print("✗ EXTENSIBILITY.md missing or empty")
        return False

if __name__ == '__main__':
    results = [
        test_imports(),
        test_functions(),
        test_documentation()
    ]

    if all(results):
        print("\n✅ All L1 tests PASSED")
        sys.exit(0)
    else:
        print("\n❌ Some L1 tests FAILED")
        sys.exit(1)
EOF
```

---

## Acceptance Criteria

- [x] All 4 validator modules import without errors
- [x] common module imports without errors
- [x] Each validator has check() function
- [x] common module has all 5 utility functions
- [x] EXTENSIBILITY.md file exists and has content
- [x] No syntax errors in any module
- [x] No missing dependencies or imports

---

## Verification (Gate L1)

Run the comprehensive test script above. Expected:
- All imports succeed
- All functions found
- Documentation file present
- Exit code 0

---

## Locations

- **Validators:** `/d/my_ai_projects/isagawa-kernel/lib/validators/`
- **Test location:** Run from `/d/my_ai_projects/isagawa-kernel/`
- **Task folder:** `D:\my_ai_projects\project_test_repos\sr_dev_workspace\tasks\universal-hook-validator-system\`

---

## Notes

- This is Phase 1, subtask g (L1 testing)
- Level 1 is structural: does code exist and load?
- If L1 passes, proceed to L2 (functional testing)
- If L1 fails: fix imports, syntax, missing functions

