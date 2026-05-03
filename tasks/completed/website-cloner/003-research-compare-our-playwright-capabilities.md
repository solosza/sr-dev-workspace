# Compare With Our Playwright MCP Capabilities

## Type
RESEARCH

## Description
Evaluate what our existing Playwright MCP setup can already do vs. what the open source repo adds.

## Requirements
- Read our `.mcp.json` to see what Playwright MCP tools are available
- List all Playwright MCP tools we have access to (browser_navigate, browser_snapshot, browser_evaluate, browser_run_code, etc.)
- For each extraction capability the open source repo uses, check: can we do this with our existing tools?
- Gap analysis: what does the repo do that we CAN'T already do with a good prompt?
- Assessment: is the open source skill just a well-crafted prompt, or does it add actual functionality?
- Save to `.claude/skills/website-cloner/research/gap-analysis.md`

## Acceptance Criteria
- [ ] `test -f .claude/skills/website-cloner/research/gap-analysis.md`
- [ ] `grep -q "Playwright" .claude/skills/website-cloner/research/gap-analysis.md`
