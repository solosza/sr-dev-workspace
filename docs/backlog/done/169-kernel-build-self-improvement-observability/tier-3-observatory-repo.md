# Tier 3: Kernel Observatory Repo

## Status
NEW

## Location
`new-repo:D:\my_ai_projects\kernel-observatory` (GitHub: isagawa-co/kernel-observatory)

## What It Does
Houses the metrics infrastructure, experiment tracking, and extension commands that consume the emission signals from Tier 1. This is a standalone repo under isagawa-co, reusable across any workspace running isagawa-kernel.

## Components

### Core Infrastructure

**`lib/aggregate.py`** — Metrics aggregator
- Reads `metrics.jsonl`, produces trend reports
- CLI: `python aggregate.py --last 30d`, `--pipeline 164`, `--trend violations`
- Output: JSON or markdown table with computed averages, rates, trends

**`lib/evaluate_experiments.py`** — Experiment evaluator
- Reads `experiments.jsonl` and `metrics.jsonl`
- For each active experiment past its evaluation window, computes verdict
- Updates experiment status (IMPROVED / NO_CHANGE / DEGRADED)
- Optionally signals rollback candidate

**`schemas/metrics.jsonl.schema`** — JSON schema for metrics events
- 3 event types: pipeline_complete, anchor, learn
- Schema version field for forward compatibility

**`schemas/experiments.jsonl.schema`** — JSON schema for experiments
- Experiment lifecycle: created → active → concluded
- Success criteria definitions

**`schemas/learn-events.jsonl.schema`** — JSON schema for learn event records
- Links lessons to code changes (files_modified, git commit hashes)
- Status tracking: active, deprecated, superseded

### Extension Commands (workspace-installable)

**`commands/kernel/eval.md`** — Run full eval suite on demand
- Invokes platform-deepeval with --harness-root
- Logs results to eval-results.jsonl
- Compares to historical trend
- Checks for active experiments to evaluate

**`commands/kernel/rollback.md`** — Manual rollback of learn events
- Takes a learn event ID
- Shows what will be reverted (lesson + file changes)
- Cascade detection (checks for dependent changes)
- Compensation pattern (new forward change, not destructive revert)
- Records rollback as a new learn event

### Documentation

**`README.md`** — What kernel-observatory does, how to install
**`docs/architecture.md`** — Data flow diagram, integration points
**`docs/schemas.md`** — Schema documentation with examples

## Dependencies
- Tier 1 (emission hooks) — metrics.jsonl must exist with data
- Tier 2 (regression gate) — eval-results.jsonl must exist
- isagawa-kernel — provides the emission signals
- platform-deepeval — provides the eval tests

## Constraints
- No external service dependencies (everything runs locally)
- Python 3.10+ only dependency
- Must work with any workspace running isagawa-kernel (not sr_dev-specific)
- Extension commands are copied into workspace `.claude/commands/kernel/` for installation

## Acceptance Criteria
- `aggregate.py` reads metrics.jsonl and produces trend output
- `evaluate_experiments.py` reads experiments.jsonl and computes verdicts
- `/kernel/eval` command runs full eval suite and logs results
- `/kernel/rollback` command reverts a learn event with cascade detection
- Schemas are documented with examples
- README explains installation into any kernel workspace
