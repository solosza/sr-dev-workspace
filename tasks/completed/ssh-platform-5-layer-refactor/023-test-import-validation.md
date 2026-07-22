# 023 — Import Validation (L2 test)

**Type:** TEST
**Phase:** Verification
**Depends on:** 001-022

## What

Run `pytest --collect-only` to verify all test files are discoverable and all imports resolve.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\tests\`

## Requirements

```bash
python -m pytest "D:/my_ai_projects/project_test_repos/platform-ssh/framework/_reference/tests/" --collect-only --rootdir="D:/my_ai_projects/project_test_repos/platform-ssh"
```

## Acceptance Criteria

- [ ] pytest --collect-only exits 0
- [ ] All test classes and methods are collected
- [ ] No import errors
