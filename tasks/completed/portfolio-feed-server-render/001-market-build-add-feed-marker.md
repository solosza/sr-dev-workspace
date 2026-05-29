# Add FEED_STATIC Marker to feed.html

## Context
The feed page currently has `<div class="feed-entries" id="feed-entries"></div>` — an empty div that JavaScript fills at runtime. To enable static pre-rendering, we add a `<!-- FEED_STATIC -->` marker inside this div. The marker is the injection point used by generate-feed.py in task 002 to bake entries into the HTML. The JS still works — it overwrites the div content for browser users. Crawlers and no-JS fetchers see the pre-rendered content.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- File: `D:\my_ai_projects\isagawa-co.github.io\feed.html`
- Change: `<div class="feed-entries" id="feed-entries"></div>`
- To: `<div class="feed-entries" id="feed-entries"><!-- FEED_STATIC --></div>`
- No other changes to feed.html

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\feed.html` contains the string `<!-- FEED_STATIC -->`
- [ ] The div `<div class="feed-entries" id="feed-entries">` is present (not removed or renamed)
- [ ] No other structural changes to feed.html

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
