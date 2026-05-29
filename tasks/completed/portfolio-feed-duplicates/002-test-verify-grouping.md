# Verify Feed Grouping via Playwright MCP

## Context
After the grouping UI is deployed, use Playwright MCP to verify: (1) at least one `<details>` group is visible on the feed page, (2) all Rekor links (`<a class="rekor-link">`) are present — none lost during grouping, (3) no entries were deleted (total entry count in DOM matches or exceeds expected), (4) no "null tasks" text remains.

## Type
TEST

## Execution
agent

## Dependencies
- 001 (feed.html + feed.css deployed with grouping)

## Phase Gate
- [ ] `001-build-group-feed-entries.md` marked complete
- [ ] GitHub Pages has deployed (allow up to 5 min for propagation after push)

## Requirements
- Navigate to https://www.isagawa.co/feed.html using Playwright MCP
- Wait for `.feed-entries` to be non-empty (entries loaded)
- Assert at least one `<details class="feed-group">` element is present
- Count all `<a class="rekor-link">` elements — assert count ≥ 1 (Rekor links survive grouping)
- Assert no `.feed-meta` span contains "null tasks" text
- Screenshot the grouped section as visual confirmation

## Acceptance Criteria
- [ ] Playwright navigates and renders feed successfully
- [ ] At least one `<details>` group element present in DOM
- [ ] All `<a class="rekor-link">` anchors present (count ≥ 1, not reduced by grouping)
- [ ] No "null tasks" text in any entry (residual check from 099)

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
