# Regenerate feed-data.json

## Context
After patching `generate-feed.py`, the existing `feed-data.json` still contains null task_count values from the previous generator run. This task runs the generator to produce a clean feed-data.json where all null values are replaced with 0. Also commits and pushes the updated file to GitHub Pages.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (feed.html renderer fixed)

## Phase Gate
- [ ] `003-build-fix-feed-renderer.md` marked complete
- [ ] `generate-feed.py` exists at `D:/my_ai_projects/isagawa-co.github.io/generate-feed.py`

## Requirements
- Run: `python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"`
- Verify `feed-data.json` updated: no entry has `"task_count": null`
- Commit and push the updated `feed-data.json` and `feed-count.txt` to the repo

## Acceptance Criteria
- [ ] Generator runs without errors
- [ ] `feed-data.json` contains no `"task_count": null` entries — Python assertion passes:
  ```
  python -c "import json; d=json.load(open('D:/my_ai_projects/isagawa-co.github.io/feed-data.json')); assert all(e['task_count'] is not None for e in d)"
  ```
- [ ] `git -C D:/my_ai_projects/isagawa-co.github.io log --oneline -1` shows a new commit

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
