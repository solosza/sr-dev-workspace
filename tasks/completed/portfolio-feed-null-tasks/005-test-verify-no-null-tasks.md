# Verify Feed — No "null tasks" Visible

## Context
Final verification that the live feed no longer displays "null tasks" for any entry. Uses Playwright MCP to navigate to the live feed page, render it with JavaScript (so all entries load), then assert no entry text contains the string "null tasks".

## Type
TEST

## Execution
agent

## Dependencies
- 004 (feed-data.json regenerated and pushed)

## Phase Gate
- [ ] `004-build-regenerate-feed-data.md` marked complete
- [ ] GitHub Pages has deployed the updated feed-data.json (allow up to 5 min for propagation)

## Requirements
- Navigate to https://www.isagawa.co/feed.html using Playwright MCP
- Wait for feed entries to render (wait for `.feed-entry` elements to appear)
- Scrape all `.feed-meta` span text from every rendered entry
- Assert none of the spans contain the string "null tasks"

## Acceptance Criteria
- [ ] Playwright MCP successfully navigates to and renders the feed page
- [ ] All feed entries are visible (at least 1 entry, `#feed-entries` not empty)
- [ ] No `.feed-meta` span contains "null tasks" text
- [ ] At least one entry shows a numeric task count (e.g., "9 tasks") confirming valid data

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
