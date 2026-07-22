# Import Direction Violations Report

**Platform:** SSH (`D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`)
**Audited against:** 5-layer reference checklist import direction rules
**Date:** 2026-07-06

## Reference Import Direction

```
L5 (tests) → imports → L4 (roles), L2 (metrics), L1 (via fixtures)
L4 (roles) → imports → L3 (tasks), L2 (constants)
L3 (tasks) → imports → L2 (metrics)
L2 (metrics) → imports → deepeval.metrics.GEval, deepeval.test_case (ONLY these)
L1 (interface) → imports → SDK (paramiko)
```

**Rule:** Higher layers import lower layers. Never upward (L1→L2, L2→L3, etc.). No skip-layer imports (L3 should not import L1 directly; L5 should not import non-standard layers).

## Full Import Graph

### L1 — `ssh_interface.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 2 | `import time` | stdlib | OK |
| 10 | `import paramiko` | SDK | OK — L1 is the SDK boundary |

**Verdict:** CLEAN — no upward imports.

### L2 — (missing)

No `metrics/` directory. No L2 files to audit.

### L3 — `tasks/run_ssh_command.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| — | No import statements | — | — |
| 2 | `ssh.execute(cmd)` via parameter | L1 (SSHInterface) | **SKIP-LAYER: L3→L1** |

**Verdict:** VIOLATION — L3 calls L1 directly via injected parameter, skipping L2.

### L4 — `roles/ssh_batch_executor.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| — | No import statements | — | — |
| (DI) | `validators` via constructor | Non-standard layer | **SKIP-LAYER: L4→validators (bypasses L3)** |

**Verdict:** VIOLATION — L4 has zero imports. Receives validators via DI instead of importing L3 tasks.

### L5 — Tests

#### `tests/conftest.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 2 | `import sys, pytest` | stdlib | OK |
| 3 | `from pathlib import Path` | stdlib | OK |
| 4 | `from unittest.mock import MagicMock` | stdlib | OK |

**Verdict:** CLEAN — but missing L1 interface import (should import SSHInterface for fixture).

#### `tests/test_ssh_batch.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 2 | `import pytest` | stdlib | OK |
| 7 | `from validators.package_validator import PackageValidator` | Non-standard | **SKIP-LAYER: L5→validators** |
| 10 | `from validators.package_validator import PackageValidator` | Non-standard | **SKIP-LAYER: L5→validators** (duplicate, different scope) |
| 11 | `from roles.ssh_batch_executor import SSHBatchExecutor` | L4 | OK — L5→L4 is allowed |

**Verdict:** VIOLATION — imports from non-standard `validators/` layer.

#### `tests/test_stig_validator.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 2 | `import sys` | stdlib | OK |
| 3 | `import os` | stdlib | OK |
| 4 | `import pytest` | stdlib | OK |
| 5 | `from unittest.mock import MagicMock` | stdlib | OK |
| 7 | `sys.path.insert(...)` | path hack | — |
| 8 | `from validators.stig_validator import STIGValidator` | Non-standard | **SKIP-LAYER: L5→validators** |
| 62 | `from ssh_interface import SSHInterface` | L1 | **DIRECT L1 IMPORT** (should use conftest fixture) |

**Verdict:** VIOLATION — imports from non-standard `validators/` layer + direct L1 import bypassing fixture pattern.

### Non-Standard Layer — `validators/`

#### `validators/compliance_validator.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 9 | `import re` | stdlib | OK |
| 10 | `from abc import ABC` | stdlib | OK |
| 11 | `from typing import List, Dict, Any, Optional` | stdlib | OK |

**Verdict:** CLEAN — stdlib only, no cross-layer imports.

#### `validators/config_validator.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 2 | `import os as _os` | stdlib | OK |

**Verdict:** CLEAN — stdlib only.

#### `validators/stig_validator.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| 2 | `import json` | stdlib | OK |
| 3 | `import os` | stdlib | OK |
| 4 | `from .compliance_validator import ComplianceValidator` | validators (intra-layer) | OK |

**Verdict:** CLEAN — intra-layer import only.

#### `validators/kernel_validator.py`, `package_validator.py`, `service_validator.py`

Not audited individually (no imports found in grep scan beyond stdlib). Assumed clean.

### Non-Standard — `resources/eval_config.py`

| Line | Import | Target | Direction |
|------|--------|--------|-----------|
| — | No imports | — | — |

**Verdict:** CLEAN — constants only.

---

## Upward Import Violations

No upward imports found (e.g., L1→L2, L2→L3, L3→L4). The SSH platform does not have any case where a lower layer imports from a higher layer.

**Result: PASS — zero upward imports.**

---

## Skip-Layer Import Violations

### V-ID-001: L3 calls L1 directly (skips L2)

- **File:** `framework/_reference/tasks/run_ssh_command.py:2`
- **Import:** `ssh.execute(cmd)` — `ssh` parameter is the L1 SSHInterface
- **Expected:** L3 should import and compose L2 metrics: `from metrics.<module> import <MetricClass>`
- **Actual:** L3 calls L1 directly. No L2 layer exists to import from.
- **Severity:** HIGH
- **Root cause:** L2 (metrics/) layer is entirely absent. L3 cannot compose what doesn't exist.

### V-ID-002: L4 bypasses L3, orchestrates non-standard validators

- **File:** `framework/_reference/roles/ssh_batch_executor.py`
- **Import:** No imports. Receives `validators` list via constructor DI.
- **Expected:** `from tasks.<module> import <task_function>` — L4 imports L3 tasks
- **Actual:** L4 iterates over injected validators (non-standard layer), calling `v.validate()`
- **Severity:** HIGH
- **Root cause:** L3 is a thin L1 wrapper; validators do the real work outside the 5-layer model.

### V-ID-003: L5 imports from non-standard `validators/` layer

- **File:** `framework/_reference/tests/test_ssh_batch.py:7,10`
- **Import:** `from validators.package_validator import PackageValidator`
- **File:** `framework/_reference/tests/test_stig_validator.py:8`
- **Import:** `from validators.stig_validator import STIGValidator`
- **Expected:** L5 imports from L4 (roles), L2 (metrics), or L1 (via fixtures)
- **Actual:** Tests import directly from `validators/`, a layer outside the 5-layer model
- **Severity:** HIGH

### V-ID-004: L5 imports L1 directly (bypasses fixture pattern)

- **File:** `framework/_reference/tests/test_stig_validator.py:62`
- **Import:** `from ssh_interface import SSHInterface`
- **Expected:** L1 interface provided via conftest fixture (e.g., `@pytest.fixture def ssh_interface(): ...`)
- **Actual:** Direct inline import inside a test class method
- **Severity:** MEDIUM

---

## Summary

| Violation Type | Count | Severity |
|---------------|-------|----------|
| Upward imports (lower→higher) | 0 | — |
| Skip-layer imports | 4 | 3 HIGH, 1 MEDIUM |
| **Total** | **4** | |

### Structural Root Cause

The SSH platform's import direction violations stem from two architectural gaps:

1. **Missing L2 (metrics/):** Without a metrics layer, L3 cannot compose metrics and instead calls L1 directly. L4 cannot import L3 task functions that compose metrics, so it orchestrates validators instead.

2. **Non-standard `validators/` layer:** The 6 validator files operate outside the 5-layer model. Both L4 (roles) and L5 (tests) import from this non-standard layer, creating skip-layer shortcuts that bypass the intended L2→L3→L4 pipeline.

### Remediation Path

1. Create `metrics/` layer wrapping validator logic with L2-compliant API (`evaluate()`, `is_above_threshold()`, `get_score()`)
2. Refactor `tasks/run_ssh_command.py` to compose L2 metrics instead of calling L1 directly
3. Refactor `roles/ssh_batch_executor.py` to import and call L3 task functions
4. Update test imports to use L4 roles or L2 metrics instead of `validators/` directly
5. Move L1 import in `test_stig_validator.py:62` to conftest fixture
