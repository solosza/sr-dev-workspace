# SSH Platform 5-Layer Compliance Report

**Platform:** SSH (`D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`)
**Reference:** platform-deepeval 5-layer architecture
**Date:** 2026-07-06
**Auditor:** Isagawa Kernel (backlog 175)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Python files audited | 13 |
| Files in standard 5-layer directories | 6 |
| Files in non-standard directories | 7 |
| Total violations | 21 |
| Critical (HIGH) | 10 |
| Medium (MEDIUM) | 5 |
| Low (LOW) | 6 |
| Layers fully compliant | 0 of 5 |
| Layers partially compliant | 3 (L1, L4, L5) |
| Layers absent | 1 (L2) |
| Import direction — upward violations | 0 |
| Import direction — skip-layer violations | 4 |

**Verdict: NON-COMPLIANT.** The SSH platform has correct SDK isolation (paramiko confined to L1) and no upward imports, but the absence of L2 (metrics) creates a cascade of skip-layer violations through L3 and L4. The non-standard `validators/` layer operates outside the 5-layer model entirely.

---

## Per-Layer Violation Tables

### L1 — Interface (`ssh_interface.py`)

| # | File:Line | Violation | Current | Required | Severity |
|---|-----------|-----------|---------|----------|----------|
| V1 | `ssh_interface.py` (root) | Wrong directory | At `_reference/` root | `interfaces/ssh_interface.py` | LOW |
| V2 | `ssh_interface.py:5` | Constructor signature | `__init__(self, hc, retries=3, timeout=10)` | `__init__(self, config: dict, logger: logging.Logger)` | MEDIUM |
| V3 | `ssh_interface.py` | Missing persistence | No `save_results()` | `save_results()`, `_save_failure_report()` | LOW |
| V4 | `tests/conftest.py` | No L1 import in fixture | `MockSSH` reimplemented inline | `from interfaces.ssh_interface import SSHInterface` | MEDIUM |

**SDK isolation: PASS** — All paramiko imports in `ssh_interface.py:10` only.

### L2 — Metrics (ABSENT)

| # | File:Line | Violation | Current | Required | Severity |
|---|-----------|-----------|---------|----------|----------|
| V1 | — | Layer missing | No `metrics/` directory | `metrics/` with metric classes | HIGH |
| V2 | `validators/*.py` | Wrong API | `validate()` → `List[Dict]` | `evaluate()` → self (fluent), `is_above_threshold()`, `get_score()`, `get_detail()` | HIGH |
| V3 | `validators/*.py` | No constants | No criteria/thresholds | `METRIC_CRITERIA`, `METRIC_THRESHOLDS` dicts | MEDIUM |

### L3 — Tasks (`tasks/run_ssh_command.py`)

| # | File:Line | Violation | Current | Required | Severity |
|---|-----------|-----------|---------|----------|----------|
| V1 | `run_ssh_command.py:2` | No L2 composition | `ssh.execute(cmd)` (calls L1) | `from metrics.<mod> import <Metric>; metric.evaluate()` | HIGH |
| V2 | `run_ssh_command.py:3` | Returns result | `return r` | Return `None`, use `test_case._eval_results` | MEDIUM |
| V3 | `run_ssh_command.py` | No imports | Zero import statements | `from metrics.<module> import <MetricClass>` | HIGH |
| V4 | `run_ssh_command.py:2` | Skip-layer L3→L1 | `ssh` param is L1 interface | L3 should compose L2, not call L1 | HIGH |

### L4 — Roles (`roles/ssh_batch_executor.py`)

| # | File:Line | Violation | Current | Required | Severity |
|---|-----------|-----------|---------|----------|----------|
| V1 | `ssh_batch_executor.py` | No L3 imports | Zero imports, DI validators | `from tasks.<mod> import <task_fn>` | HIGH |
| V2 | `ssh_batch_executor.py` | Wrong constructor | `__init__(self, ssh, validators=None)` | `__init__(self, deepeval_interface)` (L1 interface) | MEDIUM |
| V3 | `ssh_batch_executor.py` | Orchestrates validators | `v.validate()` loop | Discover content → build test cases → call L3 tasks → collect results | HIGH |

### L5 — Tests (`tests/`)

| # | File:Line | Violation | Current | Required | Severity |
|---|-----------|-----------|---------|----------|----------|
| V1 | `test_ssh_batch.py:7,10` `test_stig_validator.py:8` | Import from non-standard layer | `from validators.<mod> import ...` | Import from L4/L2/L1-via-fixture | HIGH |
| V2 | `test_stig_validator.py:62` | Direct L1 import | `from ssh_interface import SSHInterface` | L1 via conftest fixture | MEDIUM |
| V3 | `test_stig_validator.py:7` | `sys.path.insert` duplication | Path hack in test file | Centralized in conftest.py | LOW |
| V4 | `test_ssh_batch.py`, `test_stig_validator.py` | No AAA comments | No Arrange/Act/Assert comments | `# Arrange`, `# Act`, `# Assert` per test | LOW |
| V5 | `test_ssh_batch.py`, `test_stig_validator.py` | No `@pytest.mark.parametrize` | No parametrization | Parametrize over rules/validators | LOW |
| V6 | `test_ssh_batch.py`, `test_stig_validator.py` | No `_REQ_` naming | `test_connect`, `test_execute` | `test_connect_REQ_L1`, etc. | LOW |

---

## Import Direction Violations

| # | Source (Layer) | Target | Type | Severity |
|---|---------------|--------|------|----------|
| V-ID-001 | `tasks/run_ssh_command.py` (L3) | L1 via `ssh.execute()` | Skip-layer (L3→L1, bypasses L2) | HIGH |
| V-ID-002 | `roles/ssh_batch_executor.py` (L4) | validators via DI | Skip-layer (L4→validators, bypasses L3) | HIGH |
| V-ID-003 | `tests/test_ssh_batch.py:7,10`, `test_stig_validator.py:8` (L5) | `validators/` | Skip-layer (L5→non-standard) | HIGH |
| V-ID-004 | `tests/test_stig_validator.py:62` (L5) | L1 directly | Bypasses fixture pattern | MEDIUM |

**Upward imports (lower→higher): 0** — No L1→L2, L2→L3, etc. violations found.

---

## Remediation Steps (Priority Order)

### Priority 1: Critical Architecture (HIGH)

**R1. Create L2 metrics layer** (resolves L2-V1, L2-V2, L2-V3)
- Create `framework/_reference/metrics/` directory
- Create metric wrapper classes around existing validators
- Expose `evaluate()`, `is_above_threshold()`, `get_score()`, `get_detail()` API
- Define `METRIC_CRITERIA` and `METRIC_THRESHOLDS` constants
- This unblocks all downstream layer fixes

**R2. Refactor L3 to compose L2 metrics** (resolves L3-V1, L3-V3, L3-V4, V-ID-001)
- Rewrite `run_ssh_command.py` to import from `metrics/`
- Compose L2 metric objects instead of calling L1 directly
- Accept `test_case` parameter, return `None`

**R3. Refactor L4 to import L3 tasks** (resolves L4-V1, L4-V3, V-ID-002)
- Update `ssh_batch_executor.py` to import L3 task functions
- Orchestrate via L3 tasks instead of directly calling validators
- Accept L1 interface in constructor

**R4. Fix L5 imports** (resolves L5-V1, L5-V2, V-ID-003, V-ID-004)
- Replace `from validators.*` imports with L4 role or L2 metric imports
- Move `SSHInterface` import to conftest fixture
- Remove `sys.path.insert` from test files

### Priority 2: Structural Conformance (MEDIUM)

**R5. Move interface to standard directory** (resolves L1-V1)
- Move `ssh_interface.py` to `framework/_reference/interfaces/ssh_interface.py`
- Update all imports referencing the old location

**R6. Fix constructor signatures** (resolves L1-V2, L4-V2)
- Add `logger` parameter to SSHInterface
- Rename `hc` → `config`, add type hints
- Update SSHBatchExecutor constructor to accept L1 interface

**R7. Add result persistence** (resolves L1-V3)
- Add `save_results()` and `_save_failure_report()` to SSHInterface

### Priority 3: Style & Convention (LOW)

**R8. Add test conventions** (resolves L5-V4, L5-V5, L5-V6)
- Add AAA comments to all tests
- Add `@pytest.mark.parametrize` where applicable
- Rename test methods to `test_<what>_REQ_<layer>` pattern

---

## Recommendation

**A remediation backlog item IS needed.** The SSH platform has fundamental 5-layer gaps (missing L2, skip-layer imports throughout) that require coordinated refactoring across all layers. The recommended approach:

1. **Single backlog item** covering R1-R4 (critical architecture fixes)
2. **Second backlog item** for R5-R8 (structural/style conformance)

The R1-R4 fixes are interdependent — L2 must exist before L3 can compose it, and L3 must be correct before L4 can orchestrate it. These should be executed as a single pipeline with ordered tasks.

**What works well:**
- SDK isolation is correct (paramiko only in L1)
- No upward import violations
- L5 test structure is reasonable (pytest, fixtures, class organization)
- Validator logic is sound — just needs L2 wrapping

**Estimated scope:** 8-12 tasks across 4 layers.
