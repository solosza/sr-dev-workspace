# Task 001: Completion-Truth Oracle
**Type:** BUILD | **Gates:** OBS-01
## Action
Add a helper (lib/observability.py or lib/common.sh function) that reconciles a run's CLAIMED completion against ground-truth evidence and returns divergence.
## Spec
Input: a routed workflow.json (completed_tasks) + the deliverable path(s). Ground-truth = git commits touching the deliverable path on the run's branch + non-empty output artifacts. Return a structured verdict: for each claimed-complete task, is there real evidence (a commit / a non-empty artifact)? Flag any 'claimed done but no evidence' (the 270-collision class where state said done but the code was wiped). Do NOT trust the banner or self-report. Reuse 270's verify_completion_write philosophy (check the artifact, not the stdout).
## Acceptance
A helper that, given routed state + deliverable paths, returns claimed-vs-evidence divergence automatically.
