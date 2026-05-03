# Remove Absolute Paths

## Context
Replace C:/Users paths with relative paths.

## Type
BUILD

## Dependencies
- 094

## Phase Gate
- [ ] validation-report.json exists (task 094)

## Requirements
- Scan all .md and .py in `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/` for `C:/Users`
- Replace with relative paths

## Acceptance Criteria
- [ ] `grep -rq 'C:/Users'` returns exit 1 (verify: run_code)

## Gates Satisfied
PKG-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
