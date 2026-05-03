# Analyze Repo Source Code

## Type
RESEARCH

## Description
Read the actual source code of the open source website cloner skill. Understand exactly what Playwright MCP calls it makes.

## Requirements
- Read the skill file(s) from the repo (via GitHub raw or gh CLI)
- Document: what MCP tools does it call? (browser_navigate, browser_snapshot, browser_evaluate, etc.)
- Document: how does it extract styles? (getComputedStyle? stylesheet parsing? DOM traversal?)
- Document: how does it extract fonts? (font-face declarations? Google Fonts detection?)
- Document: how does it handle layout? (flexbox/grid detection? fixed positioning?)
- Document: what's the output format? (single HTML? separate CSS? assets folder?)
- Document: what are the limitations? (SPAs, JS-heavy sites, auth walls)
- Append findings to `.claude/skills/website-cloner/research/repo-analysis.md`

## Acceptance Criteria
- [ ] `grep -q "MCP" .claude/skills/website-cloner/research/repo-analysis.md`
- [ ] `grep -q "extract" .claude/skills/website-cloner/research/repo-analysis.md`
