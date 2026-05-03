# Portfolio Site — Hybrid Architecture Analysis

## Overview

The portfolio site build spans two pipelines: backlog 047 (70-task initial build) and backlog 053 (25-task visual refactor). Together they represent a **hybrid pattern** — the agent builds the site (skill-orchestrated extraction + ad-hoc generation), but the output is a traditional app (static HTML/CSS that renders in a browser with zero agent involvement).

This is architecturally distinct from both the website-cloner (pure skill, agent-as-runtime) and the fraud detector (pure traditional app, agent-as-builder-only).

## Pipeline Decomposition

### Build 1: Backlog 047 (70 tasks, 4 phases)

| Phase | Tasks | Type | Description |
|-------|-------|------|-------------|
| 1a: Clone Suero | 001-010 | Extraction (skill-based) | Navigate, screenshot, extract structure/sections/spacing/nav/breakpoints/components |
| 1b: Clone Shader | 011-020 | Extraction (skill-based) | Navigate, screenshot, extract colors/typography/surfaces/borders/animations/terminal/buttons |
| 2: Merge Tokens | 021-030 | Generation (ad-hoc) | Merge extracted JSON into CSS variables, reset, grid, responsive skeleton |
| 3: Build HTML | 031-060 | Generation (ad-hoc) | HTML skeleton, sections, CSS per section, JS behaviors (smooth scroll, mobile nav) |
| 4: Polish | 061-070 | Generation + QA | Responsive fixes, visual QA (desktop/tablet/mobile), anchor link tests, final validation |

### Build 2: Backlog 053 (25 tasks, refactor)

| Phase | Tasks | Type | Description |
|-------|-------|------|-------------|
| Refactor | 001-019 | Generation (ad-hoc) | 14 CSS/HTML changes: typography hierarchy, bold emphasis, whitespace, texture, cards, tags, stats, chain list, provenance, nav, CTA, footer, em dashes |
| Test | 020-025 | QA | Phase boundary, L1 structure, L2 visual QA (desktop/mobile), L3 provenance display, final validation |

## The Extraction vs Generation Split

### Skill-Based (Extraction): 20 of 70 tasks (29%)

Tasks 001-020 used the website-cloner skill's extraction stages (navigate, screenshot, extract computed styles). These tasks:
- Called Playwright MCP tools (`browser_navigate`, `browser_snapshot`, `browser_evaluate`)
- Produced structured JSON output (`suero-structure.json`, `shader-colors.json`, etc.)
- Were **reusable** — the same extraction pipeline works on any site
- Required **agent judgment** to identify which CSS values to extract, how to name tokens, how to handle edge cases (canvas-rendered typography came back as defaults)

### Ad-Hoc (Generation): 50 of 70 tasks (71%)

Tasks 021-070 were not skill-based. They were bespoke generation tasks:
- Merging two sets of design tokens with manual conflict resolution (Shader `--background: #fff` vs computed `rgb(0,0,0)`)
- Writing HTML sections with narrative content specific to the Isagawa story
- Hand-crafting CSS that wasn't a mechanical application of tokens but an aesthetic judgment call
- Building provenance section with Sigstore attestation display (cross-pipeline dependency on backlog 046)
- Responsive layout at 5 breakpoints

These tasks were **not reusable** — they're specific to this site, this narrative, this aesthetic.

### The Refactor (Build 2): 100% Ad-Hoc

All 25 tasks in backlog 053 were generation, not extraction. The extraction data from build 1 was sufficient. The gap was in the *aesthetic application* — Shader's canvas-rendered typography came back as `16px/400` defaults, so the visual layer never landed. The refactor was pure design craft: type scale with `clamp()`, bold emphasis patterns from Suero, radial gradient textures, card hover states.

## What This Reveals About Architecture

### The Hybrid Contract

```
Extraction Skill (reusable)       Ad-Hoc Generation (bespoke)
┌─────────────────────────┐      ┌──────────────────────────┐
│ website-cloner stages   │      │ Token merge + conflict   │
│ navigate → screenshot   │──→   │ HTML narrative sections   │
│ extract → JSON tokens   │      │ CSS aesthetic judgment    │
└─────────────────────────┘      │ Responsive, a11y, polish │
                                 └──────────────────────────┘
                                          │
                                          ▼
                                 ┌──────────────────────────┐
                                 │ Static HTML/CSS output    │
                                 │ (traditional app)         │
                                 │ No agent at runtime       │
                                 └──────────────────────────┘
```

### Key Observations

1. **Skill coverage was ~29% of the work.** The extraction skill did its job (structure, tokens, screenshots) but the majority of the build was ad-hoc generation that no skill covered. There is no "site generation" skill.

2. **The extraction-generation boundary is where quality dropped.** Shader's canvas rendering produced garbage token values. The agent dutifully extracted them and moved on. Build 2 (053) exists entirely because the extraction quality wasn't validated before generation started. A skill-level quality gate at the extraction-generation boundary would have caught this.

3. **Ad-hoc generation is the largest category of agent work.** Across the 95 total tasks (70 + 25), approximately 75 were bespoke generation. This work is high-judgment (aesthetic decisions, narrative writing, conflict resolution) but unrepeatable — it can't be packaged as a skill because it's specific to this deliverable.

4. **The output is fully runtime-independent.** Like the fraud detector, the finished product runs without the agent. Unlike the fraud detector, it has no scheduled execution, no API calls, no processing pipeline. It's static files served by a web server.

5. **The refactor proves the extraction gap.** Build 1 shipped with correct structure but no visual hierarchy. Build 2's 14 CSS/HTML changes were all aesthetic — the things the extraction skill couldn't capture from Shader's canvas-rendered pages. This is a known blind spot documented in the website-cloner's lessons (backlog 052).

## Comparison to Other Architectures

| Dimension | Website Cloner | Fraud Detector | Portfolio Site |
|-----------|---------------|---------------|----------------|
| **Agent role** | Runtime (executes) | Builder (generates code) | Builder (extracts + generates) |
| **Skill coverage** | 100% | 0% (task-builder only) | ~29% (extraction only) |
| **Ad-hoc generation** | 0% | 100% (all code was generated) | ~71% (merge, HTML, CSS, content) |
| **Runtime dependency on agent** | Total | None | None |
| **Output type** | HTML/CSS directory | Python application | HTML/CSS files |
| **Reusability of process** | High (any URL) | Low (domain-specific) | Low (site-specific) |
| **Task count** | N/A (single invocation) | 39 | 95 (70+25) |

## Key Insight for Architecture Research

The portfolio site reveals a **generation skill gap**: the kernel has extraction skills (website-cloner) and execution infrastructure (task-builder, run-task.sh, autonomous cycling), but no generation skills — no skill that takes design tokens + narrative intent and produces a polished site. The 75 ad-hoc generation tasks are evidence of work that SHOULD be skill-ifiable but isn't.

The hybrid pattern suggests a third architecture type beyond "skill-as-app" and "traditional app":
- **Skill-assisted build** — extraction via skill, generation via ad-hoc tasks, output is a traditional artifact

The question for the architecture research: can generation be skill-ified? The extraction skill works because the input (URL) and output (JSON tokens) are generic. Generation is harder because the output is bespoke (this specific site, this specific narrative). But the *process* might be generalizable: tokens → CSS foundation → section scaffolding → content injection → responsive polish → QA. That's the 4-phase structure from backlog 047, and it could potentially become a "site builder" skill if the content were parameterized.
