# Write Extraction Reference

## Type
BUILD

## Description
Write the reference file for the extraction step — how to pull styles, fonts, layout, images from a live page.

## Requirements
Create `.claude/skills/website-cloner/references/extraction.md` with:
- Step-by-step Playwright MCP calls to extract page data
- Which MCP tools to use: browser_navigate, browser_snapshot, browser_evaluate, browser_run_code
- JavaScript snippets to run via browser_evaluate:
  - Extract all computed styles for visible elements
  - Extract font-face declarations and Google Fonts links
  - Extract CSS custom properties (variables)
  - Extract responsive breakpoints from media queries
  - Extract image URLs and SVG content
- How to handle edge cases: lazy-loaded images, CSS-in-JS, web fonts

## Acceptance Criteria
- [ ] `test -f .claude/skills/website-cloner/references/extraction.md`
- [ ] `grep -q "browser_evaluate" .claude/skills/website-cloner/references/extraction.md`
