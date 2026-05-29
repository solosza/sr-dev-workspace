# Fix Feed Generator — Null-Safe task_count

## Context
`generate-feed.py` reads `task_count` from attestation bundle metadata using `meta.get("task_count", 0)`. This passes `None` through if the bundle has `"task_count": null` (same key-present-with-null bug as attest.py). The generator then writes null into `feed-data.json`, which the renderer displays as "null tasks". This task makes the generator null-safe so existing null bundles are handled gracefully.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (attest.py fixed — understanding of root cause confirmed)

## Phase Gate
- [ ] `001-build-fix-attest-writer.md` marked complete

## Requirements
- File: `D:/my_ai_projects/isagawa-co.github.io/generate-feed.py`
- In `parse_bundle`, change the `task_count` line from:
  ```python
  "task_count": meta.get("task_count", 0),
  ```
  to:
  ```python
  "task_count": meta.get("task_count") or 0,
  ```
- This makes `None` (from null bundles) coerce to `0`, matching what a zero-task run would show

## Acceptance Criteria
- [ ] `generate-feed.py` `parse_bundle` function uses `meta.get("task_count") or 0` (grep match)
- [ ] No `meta.get("task_count", 0)` pattern remains
- [ ] File is valid Python (no syntax errors)

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
