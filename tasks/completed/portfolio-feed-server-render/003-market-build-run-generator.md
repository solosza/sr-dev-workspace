# Run generate-feed.py to Produce Updated feed.html

## Context
With the static renderer added in task 002, running `generate-feed.py` now both writes `feed-data.json` and injects pre-rendered HTML entries into `feed.html`. This task runs the generator to produce the updated files.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-build-add-static-renderer.md

## Phase Gate
- [ ] `generate-feed.py` contains `inject_static_feed` function
- [ ] `generate-feed.py` contains call to `inject_static_feed(entries, OUTPUT_DIR)` in `main()`

## Requirements
- Run: `python "D:\my_ai_projects\isagawa-co.github.io\generate-feed.py"`
- No cd — use absolute path
- Command must exit 0
- Expected stdout: `Generated feed-data.json with N entries`

## Acceptance Criteria
- [ ] `python "D:\my_ai_projects\isagawa-co.github.io\generate-feed.py"` exits 0
- [ ] Stdout contains `Generated feed-data.json with`
- [ ] No Python errors or tracebacks in output

## Gates Satisfied
- FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
