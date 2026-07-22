# Tiered Index Threshold Research — Task Index

## Goal
Design and run a 60K+ token A/B experiment to find where flat document structure degrades vs tiered indexing across 3 task types.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-build-create-experiment-dir]] | BUILD | none | pending |
| 003 | [[003-build-assemble-flat-corpus]] | BUILD | 002 | pending |
| 004 | [[004-build-assemble-tiered-corpus]] | BUILD | 002 | pending |
| 005 | [[005-test-verify-corpus-size]] | TEST | 003, 004 | pending |
| 006 | [[006-build-write-sequential-task]] | BUILD | 002 | pending |
| 007 | [[007-build-write-precision-task]] | BUILD | 002 | pending |
| 008 | [[008-build-write-crossref-task]] | BUILD | 002 | pending |
| 009 | [[009-build-write-experiment-config]] | BUILD | 002 | pending |
| 010 | [[010-build-prompt-flat-sequential]] | BUILD | 003, 006 | pending |
| 011 | [[011-build-prompt-tiered-sequential]] | BUILD | 004, 006 | pending |
| 012 | [[012-build-prompt-flat-precision]] | BUILD | 003, 007 | pending |
| 013 | [[013-build-prompt-tiered-precision]] | BUILD | 004, 007 | pending |
| 014 | [[014-build-prompt-flat-crossref]] | BUILD | 003, 008 | pending |
| 015 | [[015-build-prompt-tiered-crossref]] | BUILD | 004, 008 | pending |
| 016 | [[016-build-run-sequential-ab]] | BUILD | 010, 011 | pending |
| 017 | [[017-build-run-precision-ab]] | BUILD | 012, 013 | pending |
| 018 | [[018-build-run-crossref-ab]] | BUILD | 014, 015 | pending |
| 019 | [[019-build-score-all-results]] | BUILD | 016, 017, 018 | pending |
| 020 | [[020-build-statistical-report]] | BUILD | 019 | pending |
| 021 | [[021-build-baseline-comparison]] | BUILD | 019 | pending |
| 022 | [[022-build-final-report]] | BUILD | 001, 020, 021 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- 60K+ token flat and tiered corpora from hmsa-healthcare-qa skills
- 3 task prompts exercising different failure modes
- 30 Claude outputs (3 tasks × 2 variants × 5 runs)
- GEval scores via gpt-4o judge
- Statistical report with Cohen's d, win rates, per-task breakdown
- Comparison against prior N=3 baseline at 12K tokens
