# Cross-Repo Pytest Invocation

## 2026-04-08 — pytest rootdir mismatch
- **Issue:** `python -m pytest D:/other-repo/tests/test_foo.py` failed with `ModuleNotFoundError: No module named 'src'`
- **Root Cause:** pytest was invoked from workspace cwd, so `src` was not on sys.path. The target repo needs to be the rootdir for relative imports to resolve.
- **Fix:** Always use `--rootdir=D:/my_ai_projects/fraud-detection-app` (or the target repo path) when running pytest on tests outside the current working directory.
- **Anti-Pattern:** Running `python -m pytest <path>` without `--rootdir` when cwd differs from the test's package root.
- **Quality Gate:** Before running pytest on a cross-repo test file, verify the rootdir matches the repo containing the `src/` package.

## 2026-06-22 — Nested experiment tests need sys.path fix
- **Issue:** `ModuleNotFoundError: No module named 'framework'` when running pytest on `tests/experiments/tiered-index-ab/test_ab_experiment.py` in test-platform-deepeval. Even with `--rootdir` set, deeply nested test directories can't resolve top-level package imports.
- **Root Cause:** test-platform-deepeval is not installed as a pip package. Tests at `tests/` level work because pytest adds the rootdir to sys.path, but tests in `tests/experiments/tiered-index-ab/` are too nested — the conftest.py resolution doesn't propagate the repo root.
- **Fix:** Add `sys.path.insert(0, repo_root)` in the experiment's `conftest.py` to explicitly add the repo root. Use `Path(__file__).resolve().parents[N]` to compute the repo root relative to the conftest location.
- **Anti-Pattern:** Writing test files in nested subdirectories of a non-packaged repo without adding sys.path in conftest.
- **Quality Gate:** When creating tests in `tests/experiments/*/`, always include a `conftest.py` with `sys.path.insert(0, repo_root)` for the repo root.
