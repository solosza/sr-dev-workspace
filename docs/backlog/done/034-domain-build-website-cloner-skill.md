# Website Cloner — Research Existing Repo + Evaluate Against Our QA Platforms

## Status
Open

## Priority
High — proven concept (someone already shipped this open source), but we may already have the capability via our Playwright MCP QA platforms

## Summary
Someone built an open source Claude Code skill that clones any website perfectly in one prompt using browser MCP. Before building anything, we need to: (1) find and analyze that repo to understand exactly what it does, (2) compare against what our existing QA platforms with Playwright MCP can already do, (3) decide whether to fork/adapt the repo, wrap it as a skill, or just use our existing tools. The goal is website cloning capability — the path to get there is TBD.

## Requirements
- **Phase 1 — Research the open source repo:**
  - Find the repo (Claude Code skill, website cloner, browser MCP based)
  - Read the source: what Playwright MCP calls does it make? How does it extract styles/fonts/layout?
  - What's the prompt structure? Single skill file or multi-step?
  - What are its limitations? (SPAs, auth walls, dynamic content, responsive)
  - How good is the output quality? (clean code vs. messy dump)

- **Phase 2 — Compare with our existing capabilities:**
  - Our QA platforms already have Playwright MCP — what can they already do?
  - Gap analysis: what does the open source repo do that we can't already do with a good prompt?
  - Is this really a "skill" or just a well-crafted prompt on top of Playwright MCP?

- **Phase 3 — Decision + build:**
  - Option A: Fork/adapt the open source repo as-is (if it's good enough)
  - Option B: Build a thin skill/command wrapper that leverages our existing Playwright MCP (if the gap is small)
  - Option C: Build from scratch using lessons from the repo (if their approach is flawed but the idea is sound)
  - Whichever option: deliver a `/clone` command that works in one prompt

## References
- Prior art: open source Claude Code skill for website cloning (browser MCP approach) — need to find the actual repo
- Our Playwright MCP is already configured (`.mcp.json`)
- Our QA platforms (saucedemo, etc.) already use Playwright MCP for browser interaction
- Backlog 035: AI clone product opportunity — this skill accelerates the UI cloning phase
- Existing skills pattern: `.claude/skills/` + `.claude/commands/`

## Task Builder Input
- **Deliverable:** Phase 1-2: Research report comparing open source repo vs. our existing capabilities. Phase 3: Working `/clone` command (method determined by research).
- **Location:** `workspace:.claude/skills/website-cloner/`
- **Scope:** BUILD
- **Constraints:** Research first, build second. Don't reinvent the wheel — if the open source repo works, use it. Must use existing Playwright MCP (not install new tools). Output must be clean hand-editable code. If building a skill, follow kernel skill structure (SKILL.md + references/).
