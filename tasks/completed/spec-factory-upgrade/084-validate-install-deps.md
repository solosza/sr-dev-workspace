# Install Dependencies

## Context
Install Python deps so functional gates can run.

## Type
TEST

## Dependencies
- 082

## Phase Gate
- [ ] Spec files copied (task 082)

## Requirements
- Run `pip install -r $WORKSPACE/requirements.txt`
- Verify paramiko importable

## Acceptance Criteria
- [ ] `pip list | grep paramiko` shows installed (verify: run_code)

## Gates Satisfied
VAL-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
