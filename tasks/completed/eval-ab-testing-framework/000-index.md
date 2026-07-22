# A/B Testing Framework for DeepEval — Task Index

**Backlog:** `docs/backlog/171-kernel-build-eval-ab-testing-framework.md`
**Scope:** BUILD
**Tasks:** 19

## Phase 1: Framework Components (platform-deepeval)

| Task | Description |
|------|-------------|
| 001 | Create ab_testing package with __init__.py |
| 002 | Build variant_generator.py — flattening algorithm |
| 003 | Build runner.py — execution isolation + output capture |
| 004 | Build scorer.py — DeepEval GEval paired scoring |
| 005 | Build reporter.py — statistical summary + verdict + report |
| 006 | Build experiment_config.py — config schema + defaults |

## Phase 2: Eval Skill Integration (workspace)

| Task | Description |
|------|-------------|
| 007 | Update step-00 — add --ab flag detection |
| 008 | Create step-ab-1-generate-variants.md |
| 009 | Create step-ab-2-build-prompt.md |
| 010 | Create step-ab-3-run-iterations.md |
| 011 | Create step-ab-4-score-outputs.md |
| 012 | Create step-ab-5-compare-report.md |
| 013 | Update workflow.md — AB state machine branch |
| 014 | Update SKILL.md — AB mode vocabulary + summary |
| 015 | Update gate-contract.md — AB-mode gates |
| 016 | Update eval.md command — --ab usage docs |

## Phase 3: Test

| Task | Description |
|------|-------------|
| 017 | L1 — verify all files exist |
| 018 | L2 — run variant_generator against check-data-engine |
| 019 | L3 — full A/B experiment (1 run, verify scores) |
