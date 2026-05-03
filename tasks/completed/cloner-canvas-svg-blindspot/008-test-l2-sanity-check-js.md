# L2 — Sanity Check JS Detects Uniform Defaults

## Context
Functional verification that the sanity check JavaScript correctly detects when all typography values are identical defaults (the Shader-style blind spot).

## Type
TEST

## Execution
agent

## Dependencies
- 001

## Phase Gate
- [ ] `.claude/skills/website-cloner/references/extraction.md` contains "Sanity Check" section

## Requirements
- Read the sanity check JavaScript from extraction.md
- Navigate to a simple page using Playwright MCP (`browser_navigate` to `data:text/html,...` with uniform-styled elements)
- Run the sanity check JS via `browser_evaluate`
- Verify it returns `flagged: true` when all elements have identical typography
- Verify it returns `flagged: false` on a page with varied typography

## Acceptance Criteria
- [ ] Sanity check JS returns `flagged: true` for a page where h1, h2, p all have 16px/24px/400
- [ ] Sanity check JS returns a meaningful `reason` string when flagged

## Gates Satisfied
- FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
