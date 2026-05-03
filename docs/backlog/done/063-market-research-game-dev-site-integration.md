# Research Game Dev Site Integration

## Status
Open

## Priority
Medium — strategic for showcasing the game engine / simulation platform

## Summary
Figure out how to present the Game Dev project (game engine + game dev spec) as a polished web property. Decide whether to integrate it into the existing portfolio site or build a separate product site that the portfolio links to. Use the web cloner to follow the same design process as the portfolio site — find reference sites, clone visual patterns, adapt to our content.

## Requirements

### Decision: Integrate vs Separate Site
- **Option A:** Add Game Dev pages/sections to the existing portfolio site (isagawa.co)
- **Option B:** Build a separate product site (e.g., gamedev.isagawa.co or standalone domain) that the portfolio references as "featured work"
- Research which approach competing game engines/frameworks use (Godot, Phaser, PlayCanvas, Unity indie pages)
- Consider: does a portfolio site with product pages feel cohesive, or does it dilute the personal brand?

### Game Dev — What to Showcase
- Core value prop — what the game engine does, target audience (indie devs, simulation, AI-driven gameplay)
- Playable demo or video walkthrough possibilities
- Technical architecture highlights (AI coaching, personality packs, simulation engine)
- The game-dev spec and game-engine-master as building blocks

### Design Process (same as portfolio site)
- Use web cloner skill to find and clone reference sites for game engine/indie game landing pages
- Identify visual patterns from best-in-class game dev sites (Godot, Phaser.io, PlayCanvas, itch.io creator pages)
- Adapt cloned patterns to our content and branding
- Desktop + mobile responsive

### Open Questions
- Does the game engine have enough maturity to warrant its own site, or is a portfolio showcase sufficient for now?
- Should the site include playable demos (WebGL/Canvas) or just screenshots/videos?
- Naming/domain strategy — subdomain of isagawa.co vs separate domain?

## References
- Game Dev repo: `D:\my_ai_projects\project_test_repos\game-dev`
- Game Engine Master: `D:\my_ai_projects\project_test_repos\game-engine-master`
- Portfolio site: [isagawa.co](https://www.isagawa.co) / backlog [047](done/047-market-build-portfolio-site-loop-theme.md), [055](done/055-market-build-portfolio-site-v2-terminal.md)
- Website cloner skill: `.claude/skills/website-cloner/`
- Similar backlog: [060](060-market-research-qa-platform-site-integration.md) (QA platform site integration)

## Task Builder Input
- **Deliverable:** Research report with site strategy decision, reference site analysis, wireframes/mockups, and recommended next steps
- **Location:** `subproject:game-dev-site`
- **Scope:** RESEARCH
- **Constraints:** Depends on web cloner skill for reference site analysis. Portfolio site (isagawa.co) is the existing property. Game engine spans two repos (game-dev, game-engine-master). Design process should mirror the portfolio site workflow (clone references → adapt → build).
