# Website Cloner — Skill-as-App Architecture Analysis

## Overview

The website-cloner is a 6-stage extraction+generation pipeline invoked via `/clone <url>`. It uses Playwright MCP as its runtime — the agent IS the execution engine, calling browser tools in sequence to extract page data and generate a self-contained HTML/CSS clone.

## Pipeline Stages

| Stage | Action | Tools Used | Output |
|-------|--------|-----------|--------|
| 1 | Navigate & screenshot | `browser_navigate`, `browser_resize`, `browser_take_screenshot` | Reference screenshots (desktop + mobile) |
| 2 | Extract page structure | `browser_snapshot`, `browser_evaluate` | DOM tree, computed styles, fonts, breakpoints, images/SVGs |
| 3 | Generate HTML/CSS | Agent reasoning + Write | `index.html`, `styles.css` from extracted data |
| 4 | Download assets | `browser_evaluate` (fetch-as-base64) or `curl` | `assets/images/`, `assets/fonts/` |
| 5 | Assemble output | Write | Complete self-contained directory |
| 6 | Visual QA | `browser_navigate` (file://), `browser_take_screenshot` | Comparison screenshots, iterative fixes |

## Input/Output Contract

**Input:** URL string + optional output directory path
**Output:** Self-contained directory (`index.html`, `styles.css`, `assets/`) that opens in browser with no build step or dependencies

The contract is deliberately minimal — one string in, one directory out. No config files, no dependency installation, no build toolchain.

## Agent-as-Runtime Model

The website-cloner has no traditional runtime. There is no Python process, no Node server, no compiled binary. The agent itself is the runtime:

1. **Decision engine:** The agent decides which sections to extract, which fallback strategies to apply (hydration wait, SVG text, canvas detection), and how to map extracted data to semantic HTML.
2. **Error recovery:** The sanity check (Step 4f) detects non-DOM rendering and triggers a fallback cascade — hydration wait → SVG text extraction → canvas detection. This is branching logic that lives in the skill instructions, not in code.
3. **Quality loop:** Stage 6 (QA) is a visual comparison loop where the agent screenshots its output, compares to the reference, identifies discrepancies, and iterates. No test framework — the agent IS the test runner.
4. **Tool orchestration:** The agent sequences 10+ MCP tool calls per stage, passing data between them via its own context window. The "state" is the agent's working memory.

## Reusability

The skill is reusable across any website without modification:
- No site-specific configuration or selectors hardcoded
- Fallback strategies cover edge cases (canvas, SVG text, deferred hydration, dark mode)
- Output structure is always the same (`index.html` + `styles.css` + `assets/`)
- The `/clone` command is the universal entry point

However, the skill cannot be composed INTO other pipelines easily — it's a standalone end-to-end workflow. There's no way to call "just the extraction stage" from another skill.

## What Would Break as a Traditional App

| Aspect | As Skill | As Traditional App |
|--------|----------|-------------------|
| **Fallback logic** | Agent reads instructions, decides which fallback to try based on sanity check results | Would need a decision tree in code, with every branch pre-programmed |
| **Visual QA** | Agent compares screenshots using vision, identifies "colors don't match" or "layout shifted" | Would need image diffing library, pixel threshold config, structured error classification |
| **Semantic mapping** | Agent understands that a large text block at the top is a "hero section" and maps to `<section class="hero">` | Would need ML model or complex heuristics to classify DOM regions |
| **CSS generation** | Agent synthesizes clean CSS with variables from raw computed style data, choosing what to group as variables vs inline | Would need CSS optimization/deduplication logic, variable extraction algorithms |
| **Edge case handling** | New edge cases handled by updating skill instructions (plain text) | New edge cases require code changes, tests, deployment |
| **Error messages** | Agent explains what went wrong in natural language | Would need error code taxonomy, user-facing message mapping |

The core insight: the website-cloner's value is in the JUDGMENT calls — deciding what's a hero section, choosing which CSS values to extract as variables, knowing when extracted values look wrong (sanity check). These are tasks where an LLM agent dramatically outperforms deterministic code.

## Architecture Characteristics

- **No installation:** No `npm install`, no `pip install`, no binary. The skill is markdown files.
- **No state management:** No database, no files between runs. Agent context window IS the state.
- **No error handling code:** Fallback strategies are described in prose, not try/catch blocks.
- **No tests:** QA is visual comparison by the agent, not automated test suites.
- **No versioning complexity:** Updating the skill = editing markdown. No build, no deploy, no migration.
- **Tight coupling to MCP:** Completely dependent on Playwright MCP tools being available. No MCP = no skill.

## Key Insight for Architecture Research

The website-cloner represents the **purest skill-as-app pattern**: zero traditional code, 100% agent-executed, with the LLM providing the judgment layer that would require ML models or complex heuristics in a traditional app. Its weakness is composability — it's monolithic (all 6 stages or nothing) and non-decomposable by external callers.
