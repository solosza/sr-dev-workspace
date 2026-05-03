# L3 — Live Extraction Non-Breaking Test

## Context
Production verification that the updated extraction reference doesn't break normal DOM-based extraction. Run the full extraction pipeline against a known-good site (example.com) and verify it completes without errors.

## Type
TEST

## Execution
agent

## Dependencies
- 001, 002, 003, 004, 005, 006

## Phase Gate
- [ ] Tasks 001-006 complete

## Requirements
- Use Playwright MCP to navigate to `https://example.com`
- Run the full extraction pipeline as documented in extraction.md:
  - Step 1: Navigate
  - Step 2: Screenshot
  - Step 3: Snapshot
  - Step 4a-4g: All extraction steps including the new ones
- The sanity check should return `flagged: false` (example.com uses standard DOM rendering)
- The fallback strategies should be skipped (since sanity check passes)
- Canvas detection should find no canvas elements
- SVG text extraction should find no SVG text
- CSS divergence check should find no divergences (or minimal ones)

## Acceptance Criteria
- [ ] `browser_navigate` to example.com succeeds
- [ ] `browser_snapshot` returns content
- [ ] Sanity check returns `flagged: false`
- [ ] No JavaScript errors during extraction steps

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
