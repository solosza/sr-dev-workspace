# Fix generate-feed.py — Use FEED_STATIC_START/END Markers

## Context
The `inject_static_feed` function in `generate-feed.py` currently looks for a single `<!-- FEED_STATIC -->` marker and replaces it with rendered HTML (line 161-168). This approach has two problems:
1. Once replaced, the marker is gone — re-running the script won't find it
2. The script doesn't update the static `feed-count` text or `nav-count` value

After task 003, `feed.html` uses `<!-- FEED_STATIC_START -->` and `<!-- FEED_STATIC_END -->` markers wrapping the entries block. The script needs to replace the content BETWEEN these markers (preserving the markers themselves) instead of replacing a single marker.

The script also needs to update:
- `<!-- FEED_COUNT -->` marker: replace the text immediately before it with `{N} attested pipeline runs`
- `<!-- NAV_COUNT -->` marker: replace the text immediately before it with `{N}`

## Type
BUILD

## Execution
inline

## Dependencies
- 003-market-fix-feed-js-guard.md

## Phase Gate
- [ ] `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 (task 003 complete)

## Requirements
- Edit `D:/my_ai_projects/isagawa-co.github.io/generate-feed.py`
- Update `inject_static_feed` function to:
  - Use regex or string replace to find content between `<!-- FEED_STATIC_START -->` and `<!-- FEED_STATIC_END -->`
  - Replace that content with freshly rendered HTML
  - Preserve both markers (they are NOT removed after replacement)
  - Log warning if neither marker is found (backward compat)
- Add logic to update `<!-- FEED_COUNT -->` marker: replace preceding text with `{count} attested pipeline runs<!-- FEED_COUNT -->`
- Add logic to update `<!-- NAV_COUNT -->` marker: replace preceding text with `{count}<!-- NAV_COUNT -->`
- The replacement should use Python's `re.sub` with a pattern that matches from marker to marker

## Acceptance Criteria
- [ ] `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0
- [ ] `grep -q "FEED_STATIC_END" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0
- [ ] `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0
- [ ] `grep -q "FEED_COUNT\|NAV_COUNT" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0

## Gates Satisfied
- BUILD-07, BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
