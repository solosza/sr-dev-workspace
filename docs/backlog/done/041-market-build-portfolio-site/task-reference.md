# Task Reference — 70-Task Atomic Breakdown

## Status
NEW — reference for task builder during decomposition

## Overview
Pre-decomposed task breakdown for the portfolio site build. The task builder should use this as a reference during Step 5 (decompose) to ensure proper granularity and ordering. Each task is atomic — one action, one verification.

## Phase 1: Clone Suero Studio (Structure) — Tasks 001-010

| # | Task | Action | Output |
|---|------|--------|--------|
| 001 | Navigate to Suero | Playwright: navigate to ethansuero.com | Browser loaded |
| 002 | Screenshot Suero desktop | Playwright: full-page screenshot at 1440px | `suero-desktop.png` |
| 003 | Screenshot Suero mobile | Playwright: resize to 375px + screenshot | `suero-mobile.png` |
| 004 | Extract Suero hero | Playwright: snapshot hero section DOM + computed styles | `suero-hero.json` |
| 005 | Extract Suero process | Playwright: snapshot process/steps section | `suero-process.json` |
| 006 | Extract Suero testimonials | Playwright: snapshot testimonials/social proof section | `suero-testimonials.json` |
| 007 | Extract Suero CTA | Playwright: snapshot CTA section | `suero-cta.json` |
| 008 | Extract Suero footer | Playwright: snapshot footer section | `suero-footer.json` |
| 009 | Extract Suero nav | Playwright: snapshot navigation component | `suero-nav.json` |
| 010 | Extract Suero spacing | Playwright: evaluate JS to get computed paddings, margins, gaps, max-widths, grid values | `suero-spacing.json` |

## Phase 1: Clone Shader Development Studio (Skin) — Tasks 011-020

| # | Task | Action | Output |
|---|------|--------|--------|
| 011 | Navigate to Shader | Playwright: navigate to shader.se | Browser loaded |
| 012 | Screenshot Shader desktop | Playwright: full-page screenshot at 1440px | `shader-desktop.png` |
| 013 | Screenshot Shader mobile | Playwright: resize to 375px + screenshot | `shader-mobile.png` |
| 014 | Extract Shader colors | Playwright: evaluate JS — getComputedStyle on body, cards, surfaces, text, accents | `shader-colors.json` |
| 015 | Extract Shader typography | Playwright: evaluate JS — font families, weights, sizes from headings + body | `shader-typography.json` |
| 016 | Extract Shader surfaces | Playwright: evaluate JS — background layers, card vs elevated vs base | `shader-surfaces.json` |
| 017 | Extract Shader borders | Playwright: evaluate JS — border colors, widths, radii, shadow/glow effects | `shader-borders.json` |
| 018 | Extract Shader animations | Playwright: snapshot hover states, transitions, timing functions | `shader-animations.json` |
| 019 | Extract Shader terminal effects | Playwright: check for scan-line, phosphor glow, CRT, code-block styling | `shader-terminal.json` |
| 020 | Extract Shader buttons | Playwright: snapshot button styles, hover states, focus states | `shader-buttons.json` |

## Phase 2: Merge Design Tokens — Tasks 021-030

| # | Task | Action | Output |
|---|------|--------|--------|
| 021 | Create output directory | Create `isagawa-portfolio-site/` with `assets/images/`, `assets/fonts/` | Directory structure |
| 022 | Build color variables | Read shader-colors.json → write CSS `:root` color tokens | `styles.css` (color section) |
| 023 | Build typography variables | Read shader-typography.json → write CSS font tokens | `styles.css` (typography section) |
| 024 | Build spacing variables | Read suero-spacing.json → write CSS spacing tokens | `styles.css` (spacing section) |
| 025 | Build component tokens | Derive button, card, badge tokens from color + spacing | `styles.css` (component section) |
| 026 | Build badge tokens | Create BUILD/WORKSPACE/OPERATE badge color variants | `styles.css` (badge section) |
| 027 | Write CSS reset | Write normalize/reset + base body styles using tokens | `styles.css` (reset section) |
| 028 | Write grid system | Read suero-spacing.json → write container, grid, max-width utilities | `styles.css` (layout section) |
| 029 | Write responsive breakpoints | Read suero-spacing.json → write media query skeleton (1024/768) | `styles.css` (responsive section) |
| 030 | Assemble styles.css | Combine all CSS sections into single ordered file | `styles.css` (complete) |

## Phase 3: Build HTML — Tasks 031-055

| # | Task | Action | Output |
|---|------|--------|--------|
| 031 | Write HTML skeleton | DOCTYPE, head (meta, title, CSS link), empty body | `index.html` |
| 032 | Build navigation | Sticky header: logo + Kernel / Factory / Catalog / Platforms / Contact links | `index.html` nav section |
| 033 | Build hero section | "The AI Management Layer" headline + subheadline + CTA button | `index.html` hero section |
| 034 | Style hero | Hero CSS — full viewport, centered text, terminal feel | `styles.css` hero styles |
| 035 | Build architecture section | Flow diagram: Kernel → Factory → Agents + 6 vertical branches | `index.html` architecture section |
| 036 | Build output type cards | Three cards: BUILD / WORKSPACE / OPERATE with descriptions | `index.html` within architecture |
| 037 | Style architecture | Architecture CSS — diagram layout, cards grid, type badges | `styles.css` architecture styles |
| 038 | Build kernel section | Heading + 4 mechanism cards (anchor token, gate enforcer, learn loop, self-audit) | `index.html` kernel section |
| 039 | Style kernel cards | Card grid CSS — 2x2 or 4-col layout, card styling | `styles.css` kernel styles |
| 040 | Build factory section | Pipeline visual (INPUT → ANALYZE → DESIGN → BUILD → VALIDATE) | `index.html` factory section |
| 041 | Build factory proof line | Throughput stats + 3 output type badges below pipeline | `index.html` within factory |
| 042 | Style factory | Pipeline CSS — horizontal flow, stage boxes, badges | `styles.css` factory styles |
| 043 | Build catalog section heading | "Managed Agents — Every Domain" + subheading | `index.html` catalog heading |
| 044 | Build catalog IT cards | 9 IT & Security spec cards with type badges | `index.html` catalog IT |
| 045 | Build catalog Healthcare cards | 4 Healthcare Operations spec cards | `index.html` catalog Healthcare |
| 046 | Build catalog QA cards | 5 QA & Test Automation platform cards | `index.html` catalog QA |
| 047 | Build catalog DevOps cards | 6 DevOps & CI/CD spec cards | `index.html` catalog DevOps |
| 048 | Build catalog remaining cards | Real Estate (1) + Creative (4) + AI/Agent Ops (3) cards | `index.html` catalog remaining |
| 049 | Style catalog | Catalog CSS — vertical group headings, card grid, badge colors | `styles.css` catalog styles |
| 050 | Build QA platforms section | 5 platform cards (Selenium, Playwright, Docker, DeepEval, SSH) | `index.html` platforms section |
| 051 | Build shared architecture visual | 5-layer architecture diagram (Test → Role → Task → Page → Interface) | `index.html` within platforms |
| 052 | Style QA platforms | Platforms CSS — card layout, architecture diagram styling | `styles.css` platforms styles |
| 053 | Build loop section | Compounding flywheel circular diagram + key message | `index.html` loop section |
| 054 | Style loop | Loop CSS — circular flow layout, connecting arrows | `styles.css` loop styles |
| 055 | Build CTA section | "What domain do you need managed?" + contact email + links | `index.html` CTA section |

## Phase 3: Build HTML (continued) — Tasks 056-060

| # | Task | Action | Output |
|---|------|--------|--------|
| 056 | Build footer | Copyright, GitHub/LinkedIn/Email links, "Built with the Isagawa Kernel" | `index.html` footer |
| 057 | Style CTA + footer | CTA CSS — full-width, centered, button. Footer CSS — link columns | `styles.css` CTA + footer |
| 058 | Add smooth scroll JS | Inline script for anchor link smooth scrolling | `index.html` script tag |
| 059 | Add mobile hamburger JS | Inline script for mobile nav toggle | `index.html` script tag |
| 060 | Style navigation responsive | Nav CSS — sticky header, desktop links, mobile hamburger | `styles.css` nav styles |

## Phase 4: Polish — Tasks 061-070

| # | Task | Action | Output |
|---|------|--------|--------|
| 061 | Responsive hero | Media queries for hero section at tablet + mobile breakpoints | `styles.css` responsive |
| 062 | Responsive cards | Media queries for card grids — 2-col tablet, 1-col mobile | `styles.css` responsive |
| 063 | Responsive catalog | Media queries for catalog section — vertical stack on mobile | `styles.css` responsive |
| 064 | Responsive diagrams | Media queries for architecture + pipeline + loop diagrams | `styles.css` responsive |
| 065 | Typography responsive | Media queries for font sizes at each breakpoint | `styles.css` responsive |
| 066 | Visual QA desktop | Playwright: navigate to file:// URL at 1440px, screenshot all sections | Desktop screenshots |
| 067 | Visual QA tablet | Playwright: resize to 768px, screenshot all sections | Tablet screenshots |
| 068 | Visual QA mobile | Playwright: resize to 375px, screenshot all sections | Mobile screenshots |
| 069 | Accessibility check | Verify semantic HTML, alt text, contrast ratios, focus states | Accessibility notes |
| 070 | Final validation | Open in browser, verify all sections render, links work, scroll behavior | Validation report |

## Task Builder Notes

- **Phase boundaries are hard** — Phase 2 cannot start until Phase 1 extractions complete, Phase 3 cannot start until Phase 2 tokens exist
- **Within phases, tasks are sequential** — each task builds on prior output (same files)
- **Extraction tasks need Playwright MCP** — ensure spawned agents inherit from `.mcp.json`
- **Build tasks reference content-spec.md** — the task builder should include wikilinks to content-spec and catalog-data in relevant task descriptions
- **CSS tasks accumulate in one file** — `styles.css` grows across tasks 022-030 and 034-065
- **HTML tasks accumulate in one file** — `index.html` grows across tasks 031-060
- **Visual QA tasks use file:// protocol** — Playwright navigates to local file path
- **Timeout consideration** — extraction tasks (001-020) may need 600s timeout; build tasks (021-065) should be fine at 300s

## Summary

| Phase | Tasks | Count | Key Tool |
|-------|-------|-------|----------|
| Clone Suero | 001-010 | 10 | Playwright MCP |
| Clone Shader | 011-020 | 10 | Playwright MCP |
| Merge Tokens | 021-030 | 10 | Read + Write |
| Build HTML | 031-060 | 30 | Write + Edit |
| Polish | 061-070 | 10 | Edit + Playwright MCP |
| **Total** | | **70** | |
