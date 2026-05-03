# Clone Reference Sites for Portfolio Build

## Status
Open

## Priority
High — extraction produces the design tokens that feed the site build (backlog 047). Supersedes 041's extraction phase.

## Summary
Use the website cloner skill (Playwright MCP) to extract design tokens, structure, spacing, and components from two reference sites: Suero Studio (ethansuero.com) for B2B section structure and Shader Development Studio (shader.se) for dark/terminal aesthetic. Produces structured JSON/CSS token files that backlog 047 consumes. This is extraction only — no HTML/CSS generation.

## Lessons from 041's Extraction Run

### Suero — Thorough (keep same approach)
041 extracted Suero accurately: 17-section audit, CSS selectors with computed dimensions, spacing data for 16 sections + 20 containers + 7 wrappers + 16 grids, nav component with animation notes, six breakpoints. This data is reusable and the same extraction approach works.

### Shader — Thin (needs improved strategy)
041's Shader extraction returned honest but incomplete data. Typography samples all came back 16px/24px/400 — wrong for a site with aggressive large headlines. Root cause: shader.se likely renders headlines as canvas elements, SVG text, or deferred-hydration React components. `getComputedStyle()` on semantic heading selectors returned defaults.

### Extraction Strategy for Shader (this run)
- Try `document.styleSheets` API to extract from stylesheets directly instead of computed styles
- Target `::before`/`::after` pseudo-elements and meta styles
- Use `browser_evaluate` to inspect canvas/SVG text nodes
- If programmatic extraction still fails, extract from screenshots manually — the dark/terminal aesthetic matters more than pixel-perfect token matching
- Validate `--background`/`--foreground` conflict (#fff vs rgb(0,0,0)) before merging

## Requirements
- Clone Suero (ethansuero.com): structure, sections, spacing, nav, breakpoints, components, screenshots
- Clone Shader (shader.se): colors, typography, surfaces, borders, animations, terminal component, screenshots
- Improve Shader typography extraction with alternate strategies (see lessons above)
- Output all extraction data to `data/portfolio-site/suero/` and `data/portfolio-site/shader/`
- Verify extraction completeness — check that `suero-components.json` actually produces data (was empty/skipped in 041)
- Do NOT merge tokens — that's part of the build (backlog 047)
- Do NOT generate any HTML/CSS — extraction only

## References
- Website cloner skill: `.claude/skills/website-cloner/`
- Backlog 041: `docs/backlog/041-market-build-portfolio-site.md` (prior extraction, superseded)
- Prior extraction artifacts: `suero-desktop-1440x900.png`, `shader-desktop-1440x900.png` (screenshots from 041 run)

## Task Builder Input
- **Deliverable:** Complete design token extraction from both reference sites — JSON/CSS files in `data/portfolio-site/`
- **Location:** workspace:data/portfolio-site/
- **Scope:** BUILD
- **Constraints:** Requires Playwright MCP (configured in `.mcp.json`). Shader extraction needs alternate strategy for canvas-rendered typography. Run-task.sh timeout should be 600s for extraction tasks.
