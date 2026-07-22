# Pipeline 172: A/B Testing 5-Layer Conformance

Refactor A/B testing framework to follow the 5-layer eval architecture.

## Tasks

| # | Task | Phase |
|---|------|-------|
| 001 | Build ABMetrics class (L2) | Framework |
| 002 | Build run_ab_eval task (L3) | Framework |
| 003 | Build ABEvaluator role (L4) | Framework |
| 004 | Refactor ABScorer to use L1+L2 | Refactor |
| 005 | Update ab_testing __init__.py exports | Integration |
| 006 | Build pytest test suite (L5) | Testing |
| 007 | L1 test — verify all files exist and imports work | Verification |
