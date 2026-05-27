# Task 013: Update ssh_batch_executor.py

**Type:** BUILD
**Action:** Replace ssh_batch_executor.py with enhanced version from platform-ssh-test (includes by_framework grouping)

## What

```bash
cp "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh-test/framework/_reference/roles/ssh_batch_executor.py" "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/roles/ssh_batch_executor.py"
```

## Acceptance Criteria

- [ ] File at `platform-ssh/framework/_reference/roles/ssh_batch_executor.py` contains `by_framework` grouping
- [ ] `grep -q 'by_framework' "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/roles/ssh_batch_executor.py"` exits 0
