# 001 — Write autologger.py

**Type:** BUILD
**Phase:** 1 — Foundation
**Depends on:** None

## What

Create `framework/_reference/utilities/autologger.py` — the shared logging decorator used by all platforms.

## Requirements

Copy from platform-selenium `framework/resources/utilities/autologger.py`. Platform-agnostic (pure Python: logging, functools, datetime). Same implementation across all platforms.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\utilities\autologger.py`

Create the `utilities/` directory if it doesn't exist.

## Reference

- Source: `D:\my_ai_projects\project_test_repos\platform-selenium\framework\resources\utilities\autologger.py`
- Contract: 5-layer-contract.md → Decorator Usage section

## Acceptance Criteria

- [ ] `framework/_reference/utilities/` directory exists
- [ ] `framework/_reference/utilities/__init__.py` exists
- [ ] `framework/_reference/utilities/autologger.py` exists with `automation_logger` function
