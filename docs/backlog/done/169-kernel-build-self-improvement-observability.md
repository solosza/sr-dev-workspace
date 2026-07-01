# Build: Kernel Self-Improvement Observability System

## Status
Open

## Priority
High — foundational for Level 5 (self-improving with measurable optimization); all research complete (164-168)

## Summary
Build the kernel's self-improvement observability system using a 3-tier architecture. Tier 1 adds lightweight metric emission to isagawa-kernel core commands. Tier 2 wires platform-deepeval into the post-learn cycle as a regression gate. Tier 3 creates a new repo (kernel-observatory) for the metrics infrastructure, experiment tracking, and extension commands. Research reports from backlogs 164-168 provide the complete architecture specs.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[169-kernel-build-self-improvement-observability/tier-1-kernel-emission]] | Metric emission hooks in isagawa-kernel core commands |
| [[169-kernel-build-self-improvement-observability/tier-2-regression-gate]] | Platform-deepeval wired into post-learn regression gate |
| [[169-kernel-build-self-improvement-observability/tier-3-observatory-repo]] | New kernel-observatory repo: metrics, experiments, rollback |
| [[169-kernel-build-self-improvement-observability/phases]] | Phased delivery plan with dependency chain |

## Architecture

```
isagawa-kernel (core)          platform-deepeval           kernel-observatory (new)
┌─────────────────────┐       ┌──────────────────┐       ┌─────────────────────────┐
│ /kernel/learn        │──emit──▶ metrics.jsonl    │       │ aggregate.py            │
│ /kernel/complete     │──emit──▶ learn-events.jsonl│      │ evaluate_experiments.py  │
│ /kernel/anchor       │──emit──▶                  │       │ experiments.jsonl schema │
│                      │       │ structural tests  │◀──run─│ /kernel/eval command     │
│                      │       │ regression gate   │       │ /kernel/rollback command │
└─────────────────────┘       └──────────────────┘       └─────────────────────────┘
         Tier 1                      Tier 2                        Tier 3
     (1-2 line changes)        (regression wiring)          (new infrastructure)
```

## Requirements
- Tier 1 changes to isagawa-kernel MUST be minimal (emission only, no new dependencies)
- Tier 2 uses existing platform-deepeval infrastructure (--harness-root, structural tests)
- Tier 3 repo lives under isagawa-co org (reusable across workspaces)
- All designs follow research reports in projects/kernel-*-research/
- GEval tests require OPENAI_API_KEY — structural tests are zero-cost

## References
- `projects/kernel-metrics-research/00-research-report.md` — metrics schema, JSONL design, instrumentation plan
- `projects/kernel-experiment-tracking-research/00-research-report.md` — experiment lifecycle, success criteria patterns
- `projects/kernel-auto-eval-research/00-research-report.md` — trigger design, safety boundaries, feedback loops
- `projects/kernel-rollback-research/00-research-report.md` — versioning, compensation pattern, cascade prevention
- `projects/kernel-regression-testing-research/00-research-report.md` — smoke tests, baseline snapshots, tiered strategy
- `D:/my_ai_projects/isagawa-kernel` — kernel core (Tier 1 target)
- `D:/my_ai_projects/project_test_repos/platform-deepeval` — eval platform (Tier 2 target)
- Backlogs 164-168 (done) — research foundations

## Task Builder Input
- **Deliverable:** 3-tier observability system: kernel emission hooks, regression gate, observatory repo
- **Location:** Tier 1: `D:\my_ai_projects\isagawa-kernel`, Tier 2: `D:\my_ai_projects\project_test_repos\platform-deepeval`, Tier 3: `new-repo:D:\my_ai_projects\kernel-observatory`
- **Scope:** BUILD
- **Constraints:** Tier 1 must not add dependencies to isagawa-kernel. Tier 2 must not break existing 15/16 passing tests. Tier 3 repo needs `gh repo create`. Phases are sequential (1→2→3). GEval tests cost ~$0.10/run.
