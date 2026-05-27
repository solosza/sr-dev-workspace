# Task 009: Copy iso27001_rules.json

**Type:** BUILD
**Action:** Copy fixture from platform-ssh-test to platform-ssh

## What

```bash
cp "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh-test/framework/_reference/fixtures/iso27001_rules.json" "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/iso27001_rules.json"
```

## Acceptance Criteria

- [ ] File exists at `platform-ssh/framework/_reference/fixtures/iso27001_rules.json`
- [ ] File is byte-identical to source: `cmp` exits 0
