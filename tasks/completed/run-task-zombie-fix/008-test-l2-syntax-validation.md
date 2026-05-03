# 008 — L2 Dry-Run Syntax Validation

## Type
TEST

## Description
Verify both shell scripts pass syntax validation.

## Requirements
- Run `bash -n run-task.sh` and verify exit code 0
- Run `bash -n lib/common.sh` and verify exit code 0
- Run `shellcheck run-task.sh` if available (informational, not blocking)
- Run `shellcheck lib/common.sh` if available (informational, not blocking)

## Acceptance Criteria
- [ ] `bash -n run-task.sh` exits 0
- [ ] `bash -n lib/common.sh` exits 0

## Gates
FUNC-02
