# Cross-Repo Pytest Invocation

## 2026-04-08 — pytest rootdir mismatch
- **Issue:** `python -m pytest D:/other-repo/tests/test_foo.py` failed with `ModuleNotFoundError: No module named 'src'`
- **Root Cause:** pytest was invoked from workspace cwd, so `src` was not on sys.path. The target repo needs to be the rootdir for relative imports to resolve.
- **Fix:** Always use `--rootdir=D:/my_ai_projects/fraud-detection-app` (or the target repo path) when running pytest on tests outside the current working directory.
- **Anti-Pattern:** Running `python -m pytest <path>` without `--rootdir` when cwd differs from the test's package root.
- **Quality Gate:** Before running pytest on a cross-repo test file, verify the rootdir matches the repo containing the `src/` package.
