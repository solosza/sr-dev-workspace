# Task 014: Update host_configs.json

**Type:** BUILD
**Action:** Replace host_configs.json with enhanced version from platform-ssh-test (includes frameworks field)

## What

```bash
cp "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh-test/framework/_reference/fixtures/host_configs.json" "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/host_configs.json"
```

## Acceptance Criteria

- [ ] File at `platform-ssh/framework/_reference/fixtures/host_configs.json` contains `frameworks` field
- [ ] `grep -q 'frameworks' "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/host_configs.json"` exits 0
