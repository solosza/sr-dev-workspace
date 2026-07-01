# Phased Delivery Plan

## Phase 1: Emission + Metrics Foundation
**Tiers:** 1 + partial 3
**Dependency:** None

| Deliverable | Location | Description |
|-------------|----------|-------------|
| Emit learn events | isagawa-kernel learn.md | 1-2 lines added |
| Emit pipeline_complete events | isagawa-kernel complete.md | 1-2 lines added |
| Emit anchor events | isagawa-kernel anchor.md | 1-2 lines added |
| metrics.jsonl schema | kernel-observatory | Schema definition |
| aggregate.py | kernel-observatory | Basic trend reporting |
| Repo creation | kernel-observatory | `gh repo create isagawa-co/kernel-observatory` |

**Exit criteria:** metrics.jsonl populated after a learn/complete/anchor cycle. aggregate.py produces output.

## Phase 2: Regression Gate
**Tiers:** 2
**Dependency:** Phase 1

| Deliverable | Location | Description |
|-------------|----------|-------------|
| Baseline snapshot in learn.md | isagawa-kernel learn.md | Pre-learn structural test capture |
| Post-learn regression check | isagawa-kernel learn.md | Compare baseline to post-change |
| eval-results.jsonl logging | platform-deepeval / workspace | Results stored for trend analysis |
| Structural test tagging | platform-deepeval | Ensure -k structural works |

**Exit criteria:** After /kernel/learn, structural tests run and regressions are detected. eval-results.jsonl is populated.

## Phase 3: Experiment Tracking + Rollback
**Tiers:** 3
**Dependency:** Phase 1 + 2

| Deliverable | Location | Description |
|-------------|----------|-------------|
| experiments.jsonl schema | kernel-observatory | Experiment lifecycle schema |
| learn-events.jsonl schema | kernel-observatory | Lesson-to-change linking schema |
| evaluate_experiments.py | kernel-observatory | Verdict computation |
| /kernel/eval command | kernel-observatory | Full suite eval on demand |
| /kernel/rollback command | kernel-observatory | Manual rollback with cascade detection |
| Learn event recording | isagawa-kernel learn.md | Append to learn-events.jsonl |

**Exit criteria:** Experiments can be created, evaluated, and rolled back. /kernel/eval runs full suite.

## Phase 4: Backfill + Integration
**Tiers:** 3
**Dependency:** Phase 3

| Deliverable | Location | Description |
|-------------|----------|-------------|
| Backfill from 433 anchor-logs | kernel-observatory | Historical metrics from existing data |
| Backfill from lessons.md | kernel-observatory | Retroactive experiment creation |
| Wire eval into periodic trigger | workspace extension | Every 5th pipeline runs full eval |

**Exit criteria:** Historical data integrated. Periodic evaluation running.
