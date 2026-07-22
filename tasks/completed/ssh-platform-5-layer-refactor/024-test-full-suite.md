# 024 — Full Test Suite (L3 test)

**Type:** TEST
**Phase:** Verification
**Depends on:** 023

## What

Run the full test suite to verify all tests pass with MockSSH.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\tests\`

## Requirements

```bash
python -m pytest "D:/my_ai_projects/project_test_repos/platform-ssh/framework/_reference/tests/" -v --rootdir="D:/my_ai_projects/project_test_repos/platform-ssh"
```

## Acceptance Criteria

- [ ] All tests pass (exit 0)
- [ ] No warnings about missing imports
- [ ] Test output shows AAA pattern working (Role -> Task -> Component -> Interface chain)
