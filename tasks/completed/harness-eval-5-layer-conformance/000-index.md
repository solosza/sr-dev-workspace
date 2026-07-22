# Pipeline 173: Harness Eval 5-Layer Conformance

Refactor harness eval test suite to follow the 5-layer eval architecture, wiring up orphaned harness_metrics.py.

## Tasks

| # | Task | Phase |
|---|------|-------|
| 001 | Build HarnessMetrics class (L2) using existing harness_metrics.py | Framework |
| 002 | Build run_harness_eval task (L3) | Framework |
| 003 | Build HarnessEvaluator role (L4) | Framework |
| 004 | Refactor test_eval_harness.py to use L2+L5 pattern | Refactor |
| 005 | Wire architecture_notes.py into test cases | Integration |
| 006 | L1 test — verify structure, imports, and no orphaned code | Verification |
