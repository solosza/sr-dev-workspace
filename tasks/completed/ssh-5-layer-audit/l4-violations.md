# L4 Violations Report

**Audited:** `framework/_reference/roles/ssh_batch_executor.py`
**Reference:** `tasks/ssh-5-layer-audit/5-layer-reference-checklist.md` (Layer 4 section)
**Date:** 2026-07-05

## Summary

| Total Checks | Passed | Violations |
|--------------|--------|------------|
| 4 | 1 | 3 |

## Violations

### V-L4-001: No L3 task imports (HIGH)

**Reference pattern:** `from tasks.<module> import <task_function>` — L4 roles import and call L3 task functions.

**Actual:** Zero import statements in the file. The role receives `validators` via constructor injection and calls `v.validate()` on them. These validators come from `framework/_reference/validators/` — a non-standard layer outside the 5-layer model.

**Impact:** L4 role bypasses L3 entirely. The orchestration pattern (L4 calls L3 task functions which compose L2 metrics) is not followed.

### V-L4-002: Constructor does not receive L1 interface (MEDIUM)

**Reference pattern:** `__init__(self, deepeval_interface)` — L4 receives the L1 interface and passes it down.

**Actual:** `__init__(self, ssh, validators=None)` — receives raw SSH connection object and a validators list. No L1 interface abstraction.

**Impact:** L4 role is coupled directly to the SSH transport layer instead of working through the L1 interface abstraction. The SSH connection should be encapsulated by L1.

### V-L4-003: Orchestrates validators instead of L3 tasks (HIGH)

**Reference pattern:** L4 role "discovers content, builds test cases (via L1 `create_test_case()`), calls L3 task functions, collects results."

**Actual:** `execute_all()` iterates over `self.validators` and calls `v.validate()`. No test case creation, no L3 task function calls, no result collection via L1 patterns.

**Impact:** The role acts as a validator batch runner rather than a proper L4 orchestrator. It operates on a parallel hierarchy (`validators/`) instead of the 5-layer stack.

## Passing Checks

### Single class per file: PASS
- File contains one class (`SSHBatchExecutor`) with clear orchestration responsibility.

## Root Cause Analysis

The SSH platform uses a `validators/` pattern (6 validator files) as its primary abstraction. The L4 role orchestrates these validators rather than L3 tasks. This is architecturally consistent with the L3 finding (V-L3-002: `run_ssh_command.py` is a thin L1 wrapper, not a composable task function). The entire L3-L4 pipeline is bypassed — validators do the domain work, and the role just batch-runs them.

## Import Direction

```
Expected:  L4 (roles) → imports → L3 (tasks), L2 (constants)
Actual:    L4 (roles) → imports → nothing (receives validators via DI)
           validators → import → L1 (ssh_interface) directly
```

**Direction violation:** L4 should import from L3, but has no imports at all. The validators (non-standard layer) import from L1 directly, creating a shortcut that skips L2 and L3.
