# Clone sr-dev-workspace as Testbed

## Context
Clone the local sr-dev-workspace to create a realistic testbed. This simulates a developer who already has a workspace and wants to use the QA framework.

## Type
BUILD
## Execution
inline

## Dependencies
- None

## Requirements
- Run `git clone C:/Users/solos/my_ai_projects/sr-dev-workspace C:/Users/solos/my_ai_projects/qa-dual-mode-testbed`

## Acceptance Criteria
- [ ] Testbed exists at `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/` (verify: `test -d C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/`)

## Gates Satisfied
BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
