# Research: Automatic Evaluation — Closing the Loop

## Status
Open

## Priority
High — the eval platform exists but doesn't trigger protocol changes automatically

## Summary
Research how to close the loop between evaluation and protocol improvement. After N pipelines, the system should auto-evaluate: "Are failure rates declining? Are tasks completing faster? Are lessons repeating?" The DeepEval eval platform (platform-deepeval) is a step toward this — it measures harness quality. But there's no closed loop: eval results don't automatically trigger protocol changes. This research explores how to wire eval output back into the kernel's learn cycle.

## Requirements
- Research how to trigger eval runs automatically (after N pipelines, after learn events, on schedule)
- Research how to interpret eval results programmatically (pass/fail thresholds, trend detection)
- Research how eval failures should feed back into the kernel: auto-create backlog items? Auto-invoke /kernel/learn?
- Research the safety boundary: which changes can be auto-applied vs which need human approval?
- Research how the existing platform-deepeval test suite maps to kernel health indicators
- Research pattern detection in lessons: "this same lesson has been recorded 3 times — the fix isn't working"
- Consider: should the eval loop run as a scheduled pipeline or as part of /kernel/anchor?

## References
- `D:/my_ai_projects/project_test_repos/platform-deepeval/` — existing eval platform
- `.claude/lessons/lessons.md` — shows recurring violations
- Backlog 164 (metrics database), 165 (experiment tracking) — dependencies
- DeepEval GEval architecture (criteria + notes + context)

## Task Builder Input
- **Deliverable:** Research report with auto-evaluation architecture and feedback loop design
- **Location:** subproject:kernel-auto-eval-research
- **Scope:** RESEARCH
- **Constraints:** Must respect safety boundaries — not all changes should be auto-applied. Depends on metrics (164) and experiment tracking (165) for full capability.
