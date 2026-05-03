# Isagawa Portfolio Site — The AI Management Layer

## Status
Open

## Priority
High — first distribution artifact, needed before customer conversations and CIQ proposal

## Summary
Build the Isagawa portfolio site by cloning two Awwwards-winning sites and merging them: Suero Studio (ethansuero.com) for B2B conversion structure and Shader Development Studio (shader.se) for dark/terminal developer aesthetic. The site showcases the connected Isagawa architecture — Kernel → Spec Factory → Managed Agents → QA Platforms — as a single coherent system. Uses the website cloner skill (Playwright MCP) for extraction, then builds sections linearly. Static HTML/CSS output.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[041-market-build-portfolio-site/clone-targets]] | What to extract from Suero (structure) and Shader (skin) |
| [[041-market-build-portfolio-site/design-tokens]] | Merged color palette, typography, spacing, CSS variables |
| [[041-market-build-portfolio-site/site-architecture]] | Section order, navigation, page layout, responsive strategy |
| [[041-market-build-portfolio-site/content-spec]] | All section content — hero, kernel, factory, catalog, QA platforms, loop, CTA |
| [[041-market-build-portfolio-site/catalog-data]] | Full spec catalog organized by vertical with type badges |
| [[041-market-build-portfolio-site/pipeline]] | How the build executes — clone phases, build phases, QA phase |
| [[041-market-build-portfolio-site/task-reference]] | 70-task atomic breakdown for task builder reference |

## Architecture

```
Phase 1: CLONE (extract from donor sites via Playwright MCP)
  ethansuero.com → structure, layout, section patterns, component CSS
  shader.se → color palette, typography, dark theme, terminal aesthetic
       |
       v
Phase 2: MERGE (design tokens)
  Suero spacing + grid + breakpoints
  Shader colors + fonts + dark surfaces
  → CSS variables, typography scale, component tokens
       |
       v
Phase 3: BUILD (sections, one at a time)
  HTML skeleton → nav → hero → architecture diagram → kernel →
  factory → catalog → QA platforms → loop → CTA → footer
       |
       v
Phase 4: POLISH
  Responsive breakpoints → asset download → visual QA
```

## Requirements
- Uses website cloner skill (Playwright MCP) for extraction — tasks must have MCP access
- Static HTML/CSS output (no build step, no framework dependency)
- Dark mode, monochrome + one accent color
- Terminal/CLI personality — signals technical depth
- B2B conversion flow — problem → solution → proof → process → CTA
- Must show the connected system, not a list of products
- Must show versatility — 27+ specs across 6+ verticals
- Must show the 3 spec output types (BUILD/WORKSPACE/OPERATE)
- Must show the 5 QA platforms sharing one architecture
- Mobile responsive
- Self-contained output folder (works when opened in browser)

## References
- Website cloner skill: `.claude/skills/website-cloner/SKILL.md`
- Suero Studio: https://ethansuero.com (Awwwards nominee, B2B brand/web design)
- Shader Development Studio: https://shader.se (Awwwards SOTD, dev studio, retro terminal)
- Awwwards portfolio category: https://www.awwwards.com/websites/portfolio/
- Old portfolio backlog (job-focused): `docs/backlog/030-market-build-portfolio-site.md`
- Strategy document: user-provided (Isagawa Personal Strategy Document, April 22 2026)
- isagawa-co repos: https://github.com/orgs/isagawa-co/repositories
- isagawa-qa repos: https://github.com/orgs/isagawa-qa/repositories

## Task Builder Input
- **Deliverable:** Static HTML/CSS portfolio site in self-contained output folder
- **Location:** `new-repo:D:\my_ai_projects\isagawa-portfolio-site`
- **Scope:** BUILD
- **Constraints:** Requires Playwright MCP for clone/extraction tasks. Pipeline executes linearly (not swarm). Each spawned agent via run-task.sh inherits MCP from .mcp.json. Timeout may need bump to 600s for extraction tasks. Clone targets are live external sites — extraction depends on site availability.
