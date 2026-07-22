# Eval Platform Learning Loop — Task Index

## Goal
Move harness eval system from eval-kernel-minimal-test into platform-deepeval with parameterized harness path and architecture notes via LLMTestCase.context.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-metrics-dir]] | BUILD | none | pending |
| 002 | [[002-build-write-harness-metrics]] | BUILD | 001 | pending |
| 003 | [[003-build-write-architecture-notes]] | BUILD | 001 | pending |
| 004 | [[004-build-write-criteria-changelog]] | BUILD | 001 | pending |
| 005 | [[005-build-write-conftest]] | BUILD | none | pending |
| 006 | [[006-build-write-test-file]] | BUILD | 002, 003, 005 | pending |
| 007 | [[007-test-import-validation]] | TEST | 002, 003 | pending |
| 008 | [[008-test-full-eval-suite]] | TEST | 006 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `framework/metrics/harness_metrics.py` — universal GEval criteria with use_context support
- `framework/metrics/architecture_notes.py` — per-harness context notes
- `framework/metrics/criteria_changelog.md` — criteria evolution audit trail
- `tests/conftest.py` — parameterized harness_root via --harness-root
- `tests/test_eval_kernel_minimal.py` — 17-test eval suite wired with architecture notes
