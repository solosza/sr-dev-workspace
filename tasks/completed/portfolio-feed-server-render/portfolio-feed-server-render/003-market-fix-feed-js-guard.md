# Fix feed.html — Guard JS from Overwriting Static Entries

## Context
Currently `feed.html` lines 99-110 contain a JS block that:
1. Fetches `feed-data.json`
2. On success, OVERWRITES `#feed-entries` innerHTML with freshly-rendered HTML (line 105)

This is fine for browsers (JS runs, entries get refreshed from live data), but it means every time `generate-feed.py` runs and regenerates `feed-data.json`, the JS will overwrite the static pre-rendered entries at runtime.

More importantly for this fix: the static pre-rendered entries already contain the correct data. The JS overwrite is redundant AND it means the page looks broken during the JS fetch (static entries flash, then get replaced). Remove line 105 (`document.getElementById('feed-entries').innerHTML = ...`).

Also add `<!-- FEED_STATIC_START -->` and `<!-- FEED_STATIC_END -->` markers wrapping the pre-rendered entries block in the `<div id="feed-entries">...</div>` so generate-feed.py can identify and replace the block.

The current structure is:
```html
<div class="feed-entries" id="feed-entries">[all entries inline]</div>
```

It should become:
```html
<div class="feed-entries" id="feed-entries"><!-- FEED_STATIC_START -->[all entries inline]<!-- FEED_STATIC_END --></div>
```

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-fix-feed-count-static.md

## Phase Gate
- [ ] `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 (task 002 complete)

## Requirements
- Edit `D:/my_ai_projects/isagawa-co.github.io/feed.html`
- Remove line 105: `document.getElementById('feed-entries').innerHTML = groupEntries(entries).map(renderGroup).join('');`
- Keep lines 103-104 (update nav-count and feed-count textContent from JSON)
- Add `<!-- FEED_STATIC_START -->` immediately after the opening `<div class="feed-entries" id="feed-entries">`
- Add `<!-- FEED_STATIC_END -->` immediately before the closing `</div>` of the feed-entries div
- The JS still updates the count display from the live fetch — only the innerHTML overwrite of entries is removed

## Acceptance Criteria
- [ ] `grep -c "feed-entries.*innerHTML" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` outputs 0
- [ ] `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0
- [ ] `grep -q "FEED_STATIC_END" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0
- [ ] `grep -q "nav-count.*textContent\|textContent.*nav-count" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 (count updates still present)

## Gates Satisfied
- BUILD-04, BUILD-05, BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
