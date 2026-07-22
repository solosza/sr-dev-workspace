# L5 (Tests) Compliance Violations

**Audited:** 2026-07-05
**Files checked:** 3 (conftest.py, test_ssh_batch.py, test_stig_validator.py)
**All located in:** `framework/_reference/tests/`

---

## Violation 1: Import from non-standard `validators/` layer (HIGH)

**Files:** `test_ssh_batch.py` (lines 7, 10), `test_stig_validator.py` (line 8)
**Rule:** L5 tests should import from L4 (roles) or L3 (tasks), not from non-standard layers
**Actual:**
- `from validators.package_validator import PackageValidator`
- `from validators.stig_validator import STIGValidator`
**Expected:** Tests import L4 roles which orchestrate validators internally, or validators are moved into an L3/L4 layer
**Severity:** HIGH — `validators/` is not part of the 5-layer model. Tests directly importing from it bypasses the layer architecture.

## Violation 2: Direct L1 import in test file (MEDIUM)

**File:** `test_stig_validator.py` (line 62)
**Rule:** L5 should import L1 via conftest fixtures, not directly
**Actual:** `from ssh_interface import SSHInterface` inside `TestSTIGValidatorLive.ssh_connection` fixture
**Expected:** L1 interface provided via shared conftest fixture (as reference pattern shows: conftest creates interface, tests receive via fixture injection)
**Severity:** MEDIUM — functional but breaks the fixture-based dependency injection pattern

## Violation 3: `sys.path.insert` in test file (MEDIUM)

**File:** `test_stig_validator.py` (line 7)
**Rule:** Path manipulation should be centralized in conftest.py, not duplicated in test files
**Actual:** `sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))` at module level
**Expected:** conftest.py handles `sys.path` setup (it already does via line 5); test files should not need their own path manipulation
**Severity:** MEDIUM — creates maintenance burden and potential import conflicts

## Violation 4: No AAA pattern comments (LOW)

**Files:** `test_ssh_batch.py` (all tests), `test_stig_validator.py` (all tests)
**Rule:** Tests should follow Arrange/Act/Assert with comments marking each phase
**Actual:** No `# Arrange`, `# Act`, `# Assert` comments in any test
**Expected:** Each test method has clear AAA section comments
**Severity:** LOW — tests are functionally correct but lack structural documentation

## Violation 5: No `@pytest.mark.parametrize` usage (LOW)

**Files:** `test_ssh_batch.py`, `test_stig_validator.py`
**Rule:** Use parametrize where applicable (iterating over rules, validators, test cases)
**Actual:** No parametrize decorators anywhere
**Candidates:**
- `test_stig_validator.py`: rule ID prefix checks, result field checks could parametrize over the 15 rules
- `test_ssh_batch.py`: could parametrize over different validator types
**Severity:** LOW — functional but misses test coverage granularity

## Violation 6: No `_REQ_` naming convention (LOW)

**Files:** `test_ssh_batch.py`, `test_stig_validator.py`
**Rule:** Method naming should follow `test_<what>_REQ_<layer>` pattern
**Actual:** `test_connect`, `test_execute`, `test_framework_attributes`, etc.
**Expected:** `test_connect_REQ_L1`, `test_framework_attributes_REQ_L5`, etc.
**Severity:** LOW — naming convention deviation, no functional impact

---

## Summary

| Severity | Count | Violations |
|----------|-------|------------|
| HIGH | 1 | Import from non-standard `validators/` layer |
| MEDIUM | 2 | Direct L1 import in test, `sys.path.insert` duplication |
| LOW | 3 | No AAA comments, no parametrize, no `_REQ_` naming |
| **Total** | **6** | |

## Compliant Patterns Found

- Both test files use pytest (not unittest) for test discovery and execution
- conftest.py provides fixtures correctly (`mock_ssh_interface`, `sample_host_config`)
- `test_stig_validator.py` uses descriptive test classes (`TestSTIGValidatorUnit`, `TestSTIGValidatorLive`)
- `test_stig_validator.py` uses `@pytest.mark.live` for integration test separation
- `test_ssh_batch.py` correctly imports from L4 (`roles.ssh_batch_executor`)
- No test files found outside `framework/_reference/tests/`
