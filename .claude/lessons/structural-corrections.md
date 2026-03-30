# Structural Corrections — Lessons

## 2026-03-27 Moving conftest.py breaks reference tests

- **Issue:** Moving conftest.py from `framework/_reference/tests/` to `tests/` broke existing reference tests — pytest couldn't find `mock_ssh_interface` fixture
- **Root Cause:** pytest discovers conftest.py by walking up from the test file directory. When conftest moved to `tests/`, tests in `framework/_reference/tests/` lost access to fixtures. The structural correction task deleted the old conftest without verifying that dependents still worked.
- **Fix:** Add a thin re-export conftest.py back to `framework/_reference/tests/` that imports from `tests/conftest.py`. Reference tests work standalone, actual fixture definitions live in `tests/`.
- **Anti-Pattern Added:** Never delete a shared file (conftest, fixtures, utils) without first checking what depends on it. Run existing tests IMMEDIATELY after structural moves — before writing any new code. The convention check identified the move correctly, but the task ordering was wrong: tasks 005-007 (delete old files) ran before task 028 (verify existing tests). Deletes should come AFTER verification, not before.
- **Quality Gate Added:** When moving shared infrastructure files, always add a re-export stub at the old location OR run existing tests as the FIRST task after the move (before any deletes). Task ordering: move → verify → delete, never move → delete → verify.
