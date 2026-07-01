# Self-Improvement Observability — Task Index

## Goal
Build the kernel's self-improvement observability system: 3-tier architecture with emission hooks, regression gate, and observatory repo.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-observatory-repo]] | BUILD | none | pending |
| 002 | [[002-build-metrics-jsonl-schema]] | BUILD | 001 | pending |
| 003 | [[003-build-experiments-jsonl-schema]] | BUILD | 001 | pending |
| 004 | [[004-build-learn-events-jsonl-schema]] | BUILD | 001 | pending |
| 005 | [[005-build-aggregate-py]] | BUILD | 002 | pending |
| 006 | [[006-build-learn-emission-hook]] | BUILD | none | pending |
| 007 | [[007-build-complete-emission-hook]] | BUILD | none | pending |
| 008 | [[008-build-anchor-emission-hook]] | BUILD | none | pending |
| 009 | [[009-test-tier1-emission]] | TEST | 006, 007, 008 | pending |
| 010 | [[010-build-baseline-snapshot-in-learn]] | BUILD | 009 | pending |
| 011 | [[011-build-post-learn-regression-check]] | BUILD | 010 | pending |
| 012 | [[012-build-eval-results-logging]] | BUILD | 011 | pending |
| 013 | [[013-test-tier2-regression-gate]] | TEST | 010, 011, 012 | pending |
| 014 | [[014-build-evaluate-experiments-py]] | BUILD | 003, 005 | pending |
| 015 | [[015-build-learn-event-recording]] | BUILD | 004 | pending |
| 016 | [[016-build-eval-command]] | BUILD | 005, 014 | pending |
| 017 | [[017-build-rollback-command]] | BUILD | 004, 015 | pending |
| 018 | [[018-build-observatory-readme]] | BUILD | 001-017 | pending |
| 019 | [[019-test-tier3-observatory]] | TEST | 014, 016, 017 | pending |
| 020 | [[020-test-end-to-end-pipeline]] | TEST | all | pending |

## Phases

- **Phase 1 (Tier 1 + 3 foundation):** Tasks 001-009
- **Phase 2 (Tier 2 regression gate):** Tasks 010-013
- **Phase 3 (Tier 3 completion):** Tasks 014-019
- **Phase 4 (Integration):** Task 020

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- isagawa-kernel emits learn/complete/anchor events to metrics.jsonl
- platform-deepeval structural tests run as regression gate after /kernel/learn
- kernel-observatory repo with aggregate.py, evaluate_experiments.py, /kernel/eval, /kernel/rollback
