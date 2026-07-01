# /kernel/eval Command Build — Task Index

## Goal
Build `/kernel/eval` as a full command/skill following the 6-layer command-skill-pattern with its own loop, composable (standalone or callable). Tests any LLM artifact using DeepEval. First target: check-data from hmsa-healthcare-qa.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-command-entry-point]] | BUILD | none | pending |
| 002 | [[002-build-skill-md]] | BUILD | none | pending |
| 003 | [[003-build-workflow-md]] | BUILD | none | pending |
| 004 | [[004-build-skill-gate-contract]] | BUILD | none | pending |
| 005 | [[005-build-step-01-create-test-repo]] | BUILD | none | pending |
| 006 | [[006-build-step-02-compile-harness]] | BUILD | none | pending |
| 007 | [[007-build-step-03-copy-artifact]] | BUILD | none | pending |
| 008 | [[008-build-step-04-component-check]] | BUILD | none | pending |
| 009 | [[009-build-step-05-generate-tests]] | BUILD | none | pending |
| 010 | [[010-build-step-06-run-and-score]] | BUILD | none | pending |
| 011 | [[011-build-references-index]] | BUILD | none | pending |
| 012 | [[012-build-ref-kernel-file-list]] | BUILD | none | pending |
| 013 | [[013-build-ref-deepeval-file-list]] | BUILD | none | pending |
| 014 | [[014-build-ref-dependency-resolution]] | BUILD | none | pending |
| 015 | [[015-build-ref-component-decision-table]] | BUILD | none | pending |
| 016 | [[016-build-ref-golden-translation-patterns]] | BUILD | none | pending |
| 017 | [[017-build-ref-metric-selection]] | BUILD | none | pending |
| 018 | [[018-build-ref-report-format]] | BUILD | none | pending |
| 019 | [[019-build-contract-step-02]] | BUILD | none | pending |
| 020 | [[020-build-contract-step-03]] | BUILD | none | pending |
| 021 | [[021-build-contract-step-05]] | BUILD | none | pending |
| 022 | [[022-build-contract-step-06]] | BUILD | none | pending |
| 023 | [[023-test-l1-file-existence]] | TEST | 001-022 | pending |
| 024 | [[024-test-l2-reference-integrity]] | TEST | 023 | pending |
| 025 | [[025-test-l3-live-eval-invocation]] | TEST | 024 | pending |

## Gate Contract
-> [[gate-contract.md]]

## Deliverables
- Command entry point: `.claude/commands/kernel/eval.md`
- Skill: `.claude/skills/eval/SKILL.md`, `workflow.md`, `gate-contract.md`
- Steps: `.claude/skills/eval/steps/step-01-*.md` through `step-06-*.md`
- References: `.claude/skills/eval/references/INDEX.md` + 7 reference files
- Contracts: `.claude/skills/eval/contracts/step-02-contract.json` through `step-06-contract.json`
- Uses existing workspace hooks (Layer 6 — no new hooks needed)

## Architecture
```
Layer 1: .claude/commands/kernel/eval.md (entry point)
Layer 2: .claude/skills/eval/SKILL.md, workflow.md, gate-contract.md
Layer 3: .claude/skills/eval/steps/ (6 step files)
Layer 4: .claude/skills/eval/references/ (INDEX.md + 7 reference files)
Layer 5: .claude/skills/eval/contracts/ (4 contract JSONs)
Layer 6: Existing workspace hooks (universal-gate-enforcer, sr_dev-gate-enforcer)
```

## Source
Backlog: `docs/backlog/157-kernel-build-deepeval-command-testing.md`
Design docs: `docs/backlog/157-kernel-build-deepeval-command-testing/`
