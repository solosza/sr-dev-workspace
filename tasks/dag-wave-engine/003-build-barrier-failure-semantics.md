# Task 003: Notification-Driven Barrier + Failure Semantics
**Type:** BUILD | **Gates:** DW-03
## Action
Implement the wave barrier per D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/kernel-dag-wave-research/02-barrier-monitor-and-failures.md (READ it first).
## Spec
Notification-driven (task-completion wake, NOT polling) barrier that dispatches Wave N+1 when Wave N completes. Failure decision table: a failed/skipped agent blocks ONLY its downstream dependents; independent agents proceed. 30-minute per-wave timeout. Orchestrator-restart resume reads the manifest to know which wave is live.
## Acceptance
Barrier logic present; failure semantics match the doc's decision table; resume-from-manifest present.
