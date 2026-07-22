# Task 002: Empty-Output Retry

**Type:** BUILD | **Gates:** RH-02

## Action
ONE edit to run-task.sh: when the claude -p invocation ends via timeout kill AND the iteration logfile is 0 bytes, log [EMPTY-RETRY] and retry the same iteration once (do not increment the loop counter for that retry — restructure the for-loop into a while with explicit counter if needed). A second consecutive empty output proceeds through the existing failure path.

## Acceptance
bash -n clean; the retry is bounded at 1 per iteration; existing timeout handling for non-empty outputs unchanged.
