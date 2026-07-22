# Task 004: L2 — Contract Semantics + Negative Path

**Type:** TEST (L2) | **Gates:** SI3-05, SI3-06, SI3-08

## Action

Run ONE test script:

1. AST semantics audit (body-scoped, docstring-excluded, decorator-aware — lessons #39/#44): every `except` block either re-raises or is a documented bool/primitive state-check return (list each block with its classification)
2. Return-type verification against the design doc's Return Types section (execute a lightweight in-memory/mocked call path or inspect annotations)
3. Negative path LIVE: instantiate the interface with a valid connection (native SQL Server, db `orderly`), execute intentionally bad SQL → assert the SDK exception PROPAGATES to the caller (pytest.raises or try/except in the script) AND a log line was emitted before the raise
4. Closed-connection path: close then execute → propagation again

## Acceptance

All asserts PASS, exit 0. Red → fix → /kernel/learn.
