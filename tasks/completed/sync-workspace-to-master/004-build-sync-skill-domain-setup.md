# Task 004: Build — Sync kernel-domain-setup Skill References

## Objective
Replace 5 differing reference files in the kernel-domain-setup skill.

## Instructions

1. Copy each differing file:
   ```bash
   for f in step-02-discover.md step-04-extract.md step-05-enforcement.md step-10-state.md step-11-report.md; do
     cp "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/kernel-domain-setup/references/$f" "D:/my_ai_projects/isagawa-kernel/.claude/skills/kernel-domain-setup/references/"
   done
   ```
2. Verify zero diff on all 5 files

## Acceptance Criteria
- All 5 reference files match sr_dev (zero diff)
- 7 unchanged files still intact

## Gate
BUILD-04
