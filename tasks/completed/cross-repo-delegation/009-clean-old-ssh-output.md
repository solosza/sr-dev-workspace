# Clean old SSH spec output from factory

## Context
Remove the incorrectly-built SSH spec so factory can rebuild fresh.

## Type
BUILD

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Factory step test passed (008)

## Requirements
- Run `rm -rf C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing`
- Verify directory is gone

## Acceptance Criteria
- [ ] ssh-image-testing output dir does not exist (verify: test ! -d)

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
