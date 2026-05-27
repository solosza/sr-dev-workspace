# Task 027: Phase 6b — Integration L2 Consistency Tests

**Phase:** 6 (Integration Validation)
**Type:** TEST
**Status:** DONE

---

## Objective

Create L2 consistency tests verifying all 4 hooks produce identical blocking behavior for the same violations. Feed identical bad inputs to sr_dev, hmsa, gamedev, and ssh hooks — verify all block consistently.

## Action

Create `tests/test_hooks/test_integration_l2_consistency.py` with tests for:
1. **Secret detection** — all 4 hooks block `api_key = "sk_live_12345"`
2. **Wildcard import** — all 4 hooks block `from os import *`
3. **Skipped test** — all 4 hooks block `@pytest.mark.skip`
4. **Valid code passes** — all 4 hooks exit 0 for clean code (Write + Bash)
5. **Consistent error messaging** — all hooks mention the violation type in stderr

## Acceptance Criteria

- [x] Test file created at `tests/test_hooks/test_integration_l2_consistency.py`
- [x] All tests pass (8/8 — all 4 hooks block identically for each violation type)
- [x] Tests cover: secrets, wildcard imports, skipped tests (spec files), test file skipping, valid code
- [x] Run tests and report results — 8 passed, 0 failed

**Finding:** `common.should_skip()` intentionally skips `test_` prefixed files, which prevents `check_skipped_tests` from running on test files. Skipped test detection works on `spec` files instead. Tests adjusted to verify this design behavior.

## Gate

Phase 6.2: All 4 workspaces block identical violations identically
