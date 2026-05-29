# Commit, Push, PR — Feed Server Render Fix

## Context
All changes are on `feat/feed-server-render` branch in `D:/my_ai_projects/isagawa-co.github.io`. This task commits the modified files, pushes the branch, creates a PR against main, and merges it.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-market-test-verify-no-js-fetch.md

## Phase Gate
- [ ] `python -c "h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert h.count('class=\"feed-entry ') > 5; print('PASS')"` exits 0 (test task 005 passed)
- [ ] `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --show-current` returns `feat/feed-server-render`

## Requirements
- Stage: `feed.html` and `generate-feed.py` in `D:/my_ai_projects/isagawa-co.github.io`
- Commit message: `fix: server-render feed entries — remove JS innerHTML overwrite, add static count`
- Push branch to origin
- Create PR: `gh pr create --repo isagawa-co/isagawa-co.github.io --base main --head feat/feed-server-render`
- Merge PR: `gh pr merge --repo isagawa-co/isagawa-co.github.io --merge --delete-branch`
- Pull main: `git -C "D:/my_ai_projects/isagawa-co.github.io" fetch origin && git -C "D:/my_ai_projects/isagawa-co.github.io" checkout main && git -C "D:/my_ai_projects/isagawa-co.github.io" pull`

## Acceptance Criteria
- [ ] `git -C "D:/my_ai_projects/isagawa-co.github.io" log --oneline -1` shows commit with "fix: server-render feed"
- [ ] `gh pr list --repo isagawa-co/isagawa-co.github.io --state merged` shows the PR in merged state
- [ ] `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --show-current` returns `main`

## Gates Satisfied
(Delivery gate — confirms all changes shipped to main)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
