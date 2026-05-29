# Git Workflow

## Branches
- `feature/` - New functionality
- `bugfix/` - Bug fixes
- `hotfix/` - Urgent production fixes

## Commits (Conventional)
- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code restructuring
- `test:` - Test additions/changes
- `docs:` - Documentation
- `chore:` - Maintenance

## Rules
- Never commit directly to main
- No force pushes
- Squash before merge

## Portfolio Site (isagawa-co.github.io) — Pipeline Branch Rule

All pipelines that modify `D:\my_ai_projects\isagawa-co.github.io` MUST use a feature branch:

1. `git -C "D:/my_ai_projects/isagawa-co.github.io" checkout -b feat/[pipeline-name]`
2. Commit all changes to the branch
3. Push branch: `git push -u origin feat/[pipeline-name]`
4. Do NOT merge — leave for user to review and merge via GitHub

**Branch naming:** `feat/[backlog-slug]` — e.g. `feat/nav-consistency`, `feat/hub-spoke`

**Applies from pipeline 110 onward.** Pipelines 107, 108, 109 shipped directly to main (pre-rule).
