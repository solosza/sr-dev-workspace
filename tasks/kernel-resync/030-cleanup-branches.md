# Delete merged feature branches

## Context
Clean up old branches locally + remote.

## Type
BUILD

## Execution
inline

## Dependencies
- 026

## Phase Gate
- [ ] All merges complete (026)

## Requirements
- Delete local: `git -C C:/Users/solos/my_ai_projects/isagawa-kernel branch -d feature/learn-indexed-protocol feature/domain-setup-rerunability feature/hook-fixes feature/task-builder-audit`
- Delete remote: `git -C C:/Users/solos/my_ai_projects/isagawa-kernel push origin --delete feature/learn-indexed-protocol feature/domain-setup-rerunability feature/hook-fixes feature/task-builder-audit feature/autonomous-cycling`

## Acceptance Criteria
- [ ] No old feature branches remain (verify: git branch -a)

## Gates Satisfied
CLEAN-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
