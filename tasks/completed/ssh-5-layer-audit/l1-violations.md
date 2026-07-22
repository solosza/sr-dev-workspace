# L1 Interface Compliance — Violations Report

**Platform:** SSH (`D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`)
**Audited against:** platform-deepeval 5-layer reference checklist
**Date:** 2026-07-06

## SDK Import Audit

The SSH platform's external SDK is `paramiko` (equivalent to `deepeval` in platform-deepeval).

### Direct SDK Import Scan

| Pattern | Files Found |
|---------|-------------|
| `import paramiko` / `from paramiko` | 1 file: `framework/_reference/ssh_interface.py:10` |
| `import deepeval` / `from deepeval` | 0 files |

**Result: PASS** — All paramiko SDK imports are concentrated in the L1 interface file (`ssh_interface.py:10`). No SDK leakage into L2-L5.

## Structural Violations

### V1: Interface file location deviates from reference pattern

- **File:** `framework/_reference/ssh_interface.py`
- **Reference pattern:** `framework/interfaces/deepeval_interface.py` (dedicated `interfaces/` subdirectory)
- **Current:** Interface lives at `_reference/` root, not in an `interfaces/` subdirectory
- **Severity:** Low (structural, not functional)
- **Remediation:** Move to `framework/_reference/interfaces/ssh_interface.py` to match the 5-layer directory convention

### V2: Constructor signature deviates from reference pattern

- **File:** `framework/_reference/ssh_interface.py:5`
- **Current:** `__init__(self, hc, retries=3, timeout=10)` — `hc` is a raw dict, no logger
- **Reference pattern:** `__init__(self, config: dict, logger: logging.Logger)` — typed config + logger
- **Severity:** Medium (no logging capability, parameter naming unclear)
- **Remediation:** Add `logger` parameter; rename `hc` to `config` for clarity; add type hints

### V3: No result persistence methods

- **File:** `framework/_reference/ssh_interface.py`
- **Reference pattern:** L1 interface should have `save_results()`, `_save_failure_report()` for result persistence
- **Current:** No result persistence — `execute()` returns dict but nothing is saved
- **Severity:** Low (SSH results are consumed by L4 batch executor)
- **Remediation:** Add `save_results(results, path)` method if persistent audit trails are needed

### V4: No `from interfaces.ssh_interface import SSHInterface` in conftest.py

- **File:** `framework/_reference/tests/conftest.py`
- **Reference pattern:** `from interfaces.deepeval_interface import DeepEvalInterface` — L5 imports L1 via fixture
- **Current:** conftest.py creates a `MockSSH` class inline instead of importing and wrapping the real L1 interface
- **Severity:** Medium (test fixture is decoupled from actual interface — changes to SSHInterface won't break tests, which means tests might pass while production fails)
- **Remediation:** Import `SSHInterface` in conftest.py; create mock by wrapping/patching it rather than reimplementing

## Summary

| Check | Status | Details |
|-------|--------|---------|
| SDK imports concentrated in L1 | PASS | paramiko only in ssh_interface.py:10 |
| No SDK leakage to L2-L5 | PASS | Zero paramiko imports outside L1 |
| Interface in `interfaces/` dir | FAIL | At `_reference/` root (V1) |
| Constructor matches reference | FAIL | Missing logger, unclear param names (V2) |
| Result persistence methods | FAIL | Missing save_results (V3) |
| L5 imports L1 via fixture | FAIL | MockSSH reimplemented inline (V4) |

**Total violations: 4** (0 critical, 2 medium, 2 low)
