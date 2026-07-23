# Task 005: Reproduce This Session's Failures
**Type:** TEST | **Gates:** OBS-05
## Action
Write + RUN L2/L3 tests that reproduce this session's four failure cases and assert the observability layer catches each.
## Spec
Throwaway fixtures under mktemp (never touch real state). Four cases: (a) claimed-done-no-artifact (routed state complete but deliverable path has no commit/empty) -> OBS-01 flags it; (b) banner-says-failed-but-completed (state+artifacts complete, banner 'failed') -> OBS-02 alerts; (c) complete-but-unmerged worktree (branch with committed deliverable + complete state, not merged) -> OBS-03 lists it; (d) stale-heartbeat stall -> OBS-03 flags it. Portable fixtures (absolute paths, explicit PYTHONPATH, lesson #47). LIVE runs, not simulations.
## Acceptance
4/4 session-failure cases reproduced and caught live by the observability helpers.
