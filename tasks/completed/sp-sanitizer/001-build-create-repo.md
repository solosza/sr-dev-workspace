# Create GitHub Repo

## Context
Create the private GitHub repo and clone it locally. Foundation for all other tasks.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create private repo `solosza/sp-sanitizer` on GitHub
- Clone to `D:/my_ai_projects/sp-sanitizer/`

## Acceptance Criteria
- [ ] `gh repo view solosza/sp-sanitizer` exits 0
- [ ] `D:/my_ai_projects/sp-sanitizer/.git` exists

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
