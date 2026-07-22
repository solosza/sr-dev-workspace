# Task 004: Empty-Output Timeout Root Cause
**Type:** BUILD | **Gates:** RH-04
## Action
Investigate the 600s empty-output-at-timeout case the 262 EMPTY-RETRY papers over. Determine whether it is model-side (no tokens produced) or harness-side (stream/stdout not captured — cf. the 261 sweep's "no stdin data received in 3s" + empty stdout false-failure). Write findings to `tasks/runner-hardening-v2/EMPTY-OUTPUT-FINDINGS.md`. If harness-side, fix the stdout/stream capture in run-task.sh.
## Spec
READ the EMPTY-RETRY block + the claude -p invocation (stdin/stdout handling) first. Cite the 261 evidence (wrapper saw empty stdout though subprocess completed + wrote state). Distinguish "subprocess produced no output" from "wrapper failed to capture output". State a clear verdict and, if harness-side, the capture fix applied.
## Acceptance
EMPTY-OUTPUT-FINDINGS.md exists with a model-side-vs-harness-side verdict citing evidence; capture fix applied if harness-side.
