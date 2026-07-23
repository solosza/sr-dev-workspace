# Task 002: Banner-vs-Reality Reconciliation
**Type:** BUILD | **Gates:** OBS-02
## Action
Add a helper that computes a run's TRUE outcome from authoritative signals and surfaces disagreement with the wrapper banner.
## Spec
Compute outcome from: routed workflow state (complete/completed_tasks/skipped) + output artifacts + iteration logs (non-empty, STEP_COMPLETE/ALL_TASKS_COMPLETE markers). Compare to what the wrapper banner reported (Completed/Failed counts). When they DISAGREE (e.g., the 261 case: banner '3 failed' while state shows all complete + artifacts written; or empty-stdout false-fail), emit a first-class ALERT naming the disagreement. This is the anti-'banner lies' primitive.
## Acceptance
A helper that returns true-outcome + a disagreement alert when the banner contradicts authoritative evidence.
