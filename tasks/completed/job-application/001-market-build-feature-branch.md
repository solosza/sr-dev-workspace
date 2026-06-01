# Create Feature Branch for Job Application Page

## Context
All changes for the job-application page go on a dedicated feature branch. This isolates the work from main and matches the pattern used for other product page additions.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Create branch `feature/job-application-page` in `D:/my_ai_projects/isagawa-co.github.io`
- Branch off current `main` (or default) branch
- Use: `git -C "D:/my_ai_projects/isagawa-co.github.io" checkout -b feature/job-application-page`
- If branch already exists, check it out: `git -C "D:/my_ai_projects/isagawa-co.github.io" checkout feature/job-application-page`

## Acceptance Criteria
- [ ] Branch `feature/job-application-page` exists in the repo (`git branch --list feature/job-application-page` returns the branch name)
- [ ] Current HEAD is on `feature/job-application-page` (`git -C "D:/my_ai_projects/isagawa-co.github.io" rev-parse --abbrev-ref HEAD` returns `feature/job-application-page`)

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
