# Task 017: Commit and Merge

**Type:** BUILD
**Action:** Commit all changes on feature branch and merge to main

## What

```bash
# Stage all new/modified files
git -C "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh" add framework/_reference/fixtures/ framework/_reference/validators/ framework/_reference/tests/ framework/_reference/roles/

# Commit
git -C "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh" commit -m "feat: add compliance infrastructure — 8 frameworks, base validator, STIG example

- Add 8 compliance fixture JSONs (STIG, CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001)
- Add ComplianceValidator base class + STIGValidator example
- Add test_stig_validator.py example test
- Enhance ssh_batch_executor.py with by_framework grouping
- Enhance host_configs.json with frameworks field

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Merge to main
git -C "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh" checkout main
git -C "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh" merge --no-ff feature/088-ssh-compliance-migration -m "Merge feature/088-ssh-compliance-migration: compliance infrastructure"
```

## Acceptance Criteria

- [ ] All files committed on feature branch
- [ ] Feature branch merged to main with --no-ff
- [ ] `git -C [target] log --oneline -1` shows merge commit
