# Research: Experiment Tracking / A/B Comparison for Kernel Changes

## Status
Open

## Priority
High — without before/after comparison, protocol changes are faith-based not evidence-based

## Summary
Research how to measure the impact of kernel changes (new lessons, hook updates, protocol modifications). Currently when a lesson changes a protocol or hook, there's no formal before vs after comparison. "Did adding the cd blocker hook reduce cd violations to zero?" "Did the tiered indexing pattern reduce agent drift?" These questions can't be answered today. Need a mechanism to track what changed, when, and whether it measurably improved outcomes.

## Requirements
- Research how to tag kernel state changes (lesson added, hook modified, protocol updated) as "experiments"
- Research how to define success metrics per experiment (e.g., "cd violations = 0 in next 5 pipelines")
- Research how to compare pre-change vs post-change performance windows
- Research lightweight experiment tracking approaches that don't require external infrastructure
- Research how this connects to the metrics database (backlog 164) — experiments consume metrics
- Research prior art: feature flags, A/B testing frameworks, MLflow experiment tracking
- Consider: can anchor-logs serve as the raw data source for before/after comparison?

## References
- `.claude/lessons/lessons.md` — current lesson log (shows when rules were added)
- `.claude/state/anchor-logs/` — timestamped action archives
- Backlog 164 (metrics database — dependency)
- MLflow, LaunchDarkly, Statsig for prior art

## Task Builder Input
- **Deliverable:** Research report with experiment tracking design and integration plan
- **Location:** subproject:kernel-experiment-tracking-research
- **Scope:** RESEARCH
- **Constraints:** Depends on metrics database (164) for quantitative data. Must be lightweight — no external services required.
