# Clone Targets

## Status
NEW

## Overview
Two donor sites, each contributing different aspects to the final portfolio.

## Donor 1: Suero Studio (ethansuero.com) — Structure

**What it is:** Solo B2B brand/web designer. Dark mode, bold typography, professional. Awwwards nominee.

**Extract these structural patterns:**

| Section | What to Extract |
|---------|----------------|
| Hero | Layout, headline placement, subheadline hierarchy, CTA button position |
| Problem/Solution | Two-part narrative flow — problem statement then solution positioning |
| Process | Numbered steps (01, 02, 03), vertical layout, step descriptions |
| Client Logos | Marquee/grid pattern, logo strip |
| Testimonials | Card structure with name, role, company, quote, business outcome |
| FAQ | Accordion component — question/answer expand/collapse |
| CTA | Full-width section with headline + action (schedule call, contact form) |
| Footer | Link columns, social links, copyright |
| Navigation | Left-aligned numbered nav items, sticky behavior |

**Extract these CSS patterns:**
- Spacing scale (padding, margins, gap values between sections)
- Grid system (columns, max-width, container centering)
- Breakpoints (responsive media queries)
- Component patterns (buttons, cards, accordions, marquee)
- Section rhythm (how sections alternate, separator patterns)

**Do NOT extract:**
- Colors (using Shader's palette instead)
- Typography/fonts (using Shader's fonts instead)
- Images/assets (replacing with Isagawa content)
- Copy/text content

## Donor 2: Shader Development Studio (shader.se) — Skin

**What it is:** Creative development studio. Retro CRT/terminal aesthetic. Dark purple/blue. Awwwards SOTD (7.73).

**Extract these visual patterns:**

| Element | What to Extract |
|---------|----------------|
| Color palette | Background colors, text colors, accent colors, surface/card colors via getComputedStyle |
| Typography | Font families, weights, sizes — especially any monospace/code fonts |
| Dark theme | Surface layers (how they differentiate card vs background vs elevated), border colors, shadow/glow effects |
| Terminal aesthetic | Any scan-line effects, phosphor glow, CRT curvature, code-block styling |
| Animations | Hover states, transition timing, scroll-triggered effects |

**Do NOT extract:**
- Layout/structure (using Suero's structure instead)
- Section order or content organization
- 3D/WebGL effects (too heavy for a static site)

## Extraction Method

Use the website cloner skill pipeline:
1. Navigate to URL via Playwright MCP
2. Take viewport + full-page screenshots (reference images)
3. Extract DOM structure and computed styles per section
4. Extract CSS variables, color values, font declarations

Each extraction step is its own atomic task. See [[041-market-build-portfolio-site/task-reference]] for the full breakdown.

## Dependencies
- Playwright MCP must be available (configured in `.mcp.json`)
- Both sites must be live and accessible at build time
