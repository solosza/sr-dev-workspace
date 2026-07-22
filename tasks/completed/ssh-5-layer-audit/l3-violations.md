# L3 (Tasks) Violations Report

**Audited:** `framework/_reference/tasks/run_ssh_command.py`
**Date:** 2026-07-05

## Files Audited

| File | Path |
|------|------|
| run_ssh_command.py | `framework/_reference/tasks/run_ssh_command.py` |

## Violations

### V-L3-001: No L2 metric composition (HIGH)

**File:** `run_ssh_command.py`
**Rule:** L3 tasks must compose L2 metrics — create Metric Object, call `.evaluate()`, attach results to test case.
**Actual:** Function calls `ssh.execute(cmd)` (L1 interface) directly. No L2 metric is instantiated or evaluated. The function is a thin wrapper around L1, skipping L2 entirely.

### V-L3-002: Returns result instead of None (MEDIUM)

**File:** `run_ssh_command.py`
**Rule:** L3 task functions return `None` — results accessed via `test_case._eval_results`.
**Actual:** Function returns `r` (the result dict from `ssh.execute()`). No `test_case` parameter exists.

### V-L3-003: No L2 imports (HIGH)

**File:** `run_ssh_command.py`
**Rule:** Import pattern must be `from metrics.<module> import <MetricClass>`.
**Actual:** No imports at all. File has zero import statements. No L2 metrics module is referenced.

### V-L3-004: Import direction violation — L3 uses L1 directly (HIGH)

**File:** `run_ssh_command.py`
**Rule:** L3 imports from L2 only. L3 should not call L1 interface methods directly.
**Actual:** `ssh.execute(cmd)` calls the L1 SSH interface directly. The `ssh` parameter IS the L1 interface. L3 should receive results via L2 metrics, not by calling L1.

## Summary

| Severity | Count |
|----------|-------|
| HIGH | 3 |
| MEDIUM | 1 |
| **Total** | **4** |

## Root Cause

The SSH platform's L3 layer does not follow the 5-layer metric composition pattern. `run_ssh_command.py` acts as a direct L1 wrapper (execute command → return result) rather than a metric composition layer (instantiate L2 metric → evaluate → attach to test case). This is consistent with the L2 gap (no `metrics/` directory exists) — without L2, L3 cannot compose metrics.

## Compliant Patterns

| Check | Status |
|-------|--------|
| Tasks are functions (not classes) | PASS |
| No class definitions | PASS |
| No direct DeepEval SDK imports | PASS (vacuously — no imports at all) |
| Composes L2 metrics | FAIL |
| Returns None | FAIL |
| Imports from L2 | FAIL |
| Import direction L3 → L2 only | FAIL |
