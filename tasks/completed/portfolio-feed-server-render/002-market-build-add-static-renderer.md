# Add Static Renderer to generate-feed.py

## Context
`generate-feed.py` currently writes `feed-data.json` and `feed-count.txt`. We extend it to also render entries as HTML and inject them into feed.html. This adds Python equivalents of the JS `renderEntry`/`renderGroup`/`groupEntries` functions plus an `inject_static_feed()` function that reads feed.html, replaces `<!-- FEED_STATIC -->` with the rendered HTML, and writes feed.html back.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-build-add-feed-marker.md

## Phase Gate
- [ ] `D:\my_ai_projects\isagawa-co.github.io\feed.html` contains `<!-- FEED_STATIC -->`

## Requirements
- File: `D:\my_ai_projects\isagawa-co.github.io\generate-feed.py`
- Add these functions (in this order, before `main()`):
  1. `format_date_html(iso)` — mirrors JS `formatDate()`. Uses `datetime` from stdlib. Returns formatted string like `"May 29, 2026 14:30 UTC"`.
  2. `render_entry_html(e)` — mirrors JS `renderEntry()`. Returns HTML string for one entry dict. Handles null task_count with `"—"`. Includes rekor link if present.
  3. `group_entries(entries)` — mirrors JS `groupEntries()`. Returns list of `(title, [entries])` tuples, consecutive entries with same title grouped.
  4. `render_group_html(group)` — mirrors JS `renderGroup()`. Single-entry group returns `render_entry_html()`. Multi-entry group returns `<details>/<summary>` HTML.
  5. `inject_static_feed(entries, output_dir)` — reads `feed.html` from output_dir, replaces `<!-- FEED_STATIC -->` with rendered HTML, writes back. Prints warning to stderr if marker not found.
- Add call `inject_static_feed(entries, OUTPUT_DIR)` in `main()` after writing feed-count.txt

## Acceptance Criteria
- [ ] `generate-feed.py` contains function `render_entry_html`
- [ ] `generate-feed.py` contains function `inject_static_feed`
- [ ] `generate-feed.py` contains function `format_date_html`
- [ ] `generate-feed.py` contains function `group_entries`
- [ ] `generate-feed.py` contains function `render_group_html`
- [ ] `generate-feed.py` `main()` calls `inject_static_feed(entries, OUTPUT_DIR)`
- [ ] `render_entry_html` handles `task_count` being None (renders `"—"` not `"None"`)
- [ ] `inject_static_feed` warns to stderr if `<!-- FEED_STATIC -->` not found (does not crash)

## Gates Satisfied
- BUILD-02, BUILD-03, BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
