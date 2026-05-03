# Create GitHub Remote - HUMAN REQUIRED

## Context
Add remote. User must create repo if missing.

## Type
BUILD

## Dependencies
- 098

## Phase Gate
- [ ] Git initialized (task 098)

## Requirements
- `git -C C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing remote add origin git@github.com:isagawa-qa/platform-ssh.git`
- HUMAN REQUIRED: create repo if missing

## Acceptance Criteria
- [ ] `git remote -v` shows origin (verify: run_code)

## Gates Satisfied
PKG-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
