# Portfolio Site V2 — Floating Terminal + Scroll Animations

## Status
Open

## Priority
Medium — creative upgrade, v1 is already live

## Summary
Build an alternative version of the Isagawa portfolio site with a floating terminal hero and scroll-driven animations. Same content and structure as v1 (seed, growth, self-extension, this page, provenance) but with a dynamic presentation layer that brings the page to life. The terminal shows a real conversation loop: natural language in, structured output out, feeding back into itself. This is the visual equivalent of Shader.se's retro CRT — an honest representation of what the system does.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[055-market-build-portfolio-site-v2-terminal/floating-terminal]] | Hero terminal component: 3D perspective, typing animation, conversation loop |
| [[055-market-build-portfolio-site-v2-terminal/scroll-animations]] | IntersectionObserver reveals, staggered card entrances, section transitions |
| [[055-market-build-portfolio-site-v2-terminal/parallax-depth]] | Section number parallax, terminal float, layered scroll speeds |
| [[055-market-build-portfolio-site-v2-terminal/content-carry-forward]] | What carries over from v1 (typography, tags, bold emphasis, stats, em dash cleanup, attestation cards) |

## Requirements
- Own directory, separate from v1 (`isagawa-portfolio-site-v2`)
- Floating terminal in hero showing a live-looking conversation loop
- Scroll-triggered section reveals (fade/slide on viewport entry)
- Staggered card entrance animations
- Parallax depth on section numbers
- Same content structure as v1 (all 4 sections + provenance + footer)
- All v1 visual refactor work carries forward (pipeline 053 changes)
- Vanilla CSS + JS only, no frameworks or libraries
- Mobile responsive (terminal simplifies on small screens)
- All three attestation cards with embedded bundles

## References
- V1 source: `D:\my_ai_projects\isagawa-portfolio-site\`
- Design reference: https://www.shader.se (floating quality, scroll-driven reveals)
- Design reference: https://suero.co (typography, bold emphasis, tag patterns)
- Pipeline 047 (v1 build): Rekor #1387966928
- Pipeline 053 (v1 visual refactor): Rekor #1388628067

## Task Builder Input
- **Deliverable:** Complete portfolio site v2 with terminal hero and scroll animations
- **Location:** new-repo:D:\my_ai_projects\isagawa-portfolio-site-v2
- **Scope:** BUILD
- **Constraints:** Vanilla HTML/CSS/JS only. No Three.js or WebGL. Must work without a build step. Content identical to v1, presentation layer is what changes.
