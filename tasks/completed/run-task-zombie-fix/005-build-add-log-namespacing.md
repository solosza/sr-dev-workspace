# 005 — Add Pipeline-Run Log Namespacing

## Type
BUILD

## Description
Ensure iteration logs from different pipeline runs don't overwrite each other.

## Requirements
- Verify `LOG_PREFIX` (lines 77-81 in run-task.sh) namespaces logs by task subfolder
- Check if multiple runs of the SAME subfolder overwrite each other (e.g., retry of pipeline 043)
- If same-subfolder overwrites are possible, add a timestamp or run-ID suffix:
  - Option A: `${LOG_PREFIX}${RUN_ID}_iteration_${i}.log` where RUN_ID is `date +%Y%m%d_%H%M%S`
  - Option B: Archive previous logs to a `previous/` subfolder before starting
- If LOG_PREFIX already prevents cross-pipeline overwrites and same-subfolder retries are acceptable, verify and mark as no-op

## Acceptance Criteria
- [ ] Cross-pipeline log overwrites prevented
- [ ] Same-subfolder retry behavior documented or fixed

## Gates
BUILD-04
