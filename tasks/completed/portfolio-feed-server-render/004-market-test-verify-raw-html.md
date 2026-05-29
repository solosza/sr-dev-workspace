# Verify Raw HTML Contains Feed Entries

## Context
The core acceptance criterion for this backlog item: a no-JS fetch of feed.html must return the feed entries in the raw HTML. This task verifies that by reading feed.html directly (simulating what curl/wget/a crawler would see) and asserting entries are present. We do NOT use Playwright MCP — it renders JS and would see entries regardless of whether they're pre-rendered.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-market-build-run-generator.md

## Phase Gate
- [ ] `generate-feed.py` ran successfully (task 003 complete)
- [ ] `D:\my_ai_projects\isagawa-co.github.io\feed.html` was updated by the generator

## Requirements
- Read `D:\my_ai_projects\isagawa-co.github.io\feed.html` as raw text (no browser, no JS)
- Assert: `<!-- FEED_STATIC -->` marker is NOT present (it was replaced by real HTML)
- Assert: string `feed-entry` appears more than 10 times in the raw HTML
- Assert: string `feed-entry__title` appears in the raw HTML (confirms titles rendered)
- All assertions via Python one-liners or inline script — no Playwright MCP

## Acceptance Criteria
- [ ] `python -c "content=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert '<!-- FEED_STATIC -->' not in content, 'marker not replaced'"` exits 0
- [ ] `python -c "content=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert content.count('feed-entry') > 10, f'only {content.count(\"feed-entry\")} entries'"` exits 0
- [ ] `python -c "content=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert 'feed-entry__title' in content"` exits 0

## Gates Satisfied
- FUNC-02, TEST-01, TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
