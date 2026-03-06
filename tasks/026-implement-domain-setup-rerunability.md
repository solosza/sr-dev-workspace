# Implement Domain-Setup Rerunability Fix

## Context
Apply the fixes identified in task 025 to make domain-setup support layered installs. Changes go to the canonical kernel repo on a feature branch.

## Dependencies
- **025** — rerunability audit complete with fix strategy

## Phase Gate
- [ ] `research/025-domain-setup-rerunability.md` exists with Required Changes section

## Requirements

### Work in canonical kernel repo
Repo: `D:\my_ai_projects\isagawa-kernel`

### Create feature branch
```
git checkout -b feature/domain-setup-rerunability
```
**NEVER commit directly to main on the canonical kernel.**

### Apply fixes
Implement every change from the Required Changes section of 025:
- Update domain-setup step files to check for existing state before writing
- Make protocol creation additive (merge domain protocol into existing, don't overwrite kernel protocol)
- Make hook registration additive (append to settings.local.json, don't overwrite)
- Make CLAUDE.md updates additive (append domain-specific sections, don't overwrite kernel sections)
- Make state files merge-safe

### Test locally
After implementing fixes, verify by reading through the modified step files and confirming the logic handles both scenarios:
1. First run (kernel spec, clean workspace) — should work as before
2. Second run (domain spec, kernel already present) — should layer on top

### Commit and push feature branch
- Commit message: `feat: make domain-setup rerunnable for layered spec installs`
- Push feature branch (NOT main): `git push -u origin feature/domain-setup-rerunability`
- Do NOT merge to main yet — merging happens after testing in tasks 035-036

## Output
- Feature branch `feature/domain-setup-rerunability` on `isagawa-co/isagawa-kernel`
- Modified domain-setup step files

## Validation
- [ ] Feature branch created (not on main)
- [ ] All changes from 025 Required Changes implemented
- [ ] No kernel functionality broken (existing step logic preserved for first-run case)
- [ ] Feature branch pushed to GitHub
- [ ] No changes on main branch

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
