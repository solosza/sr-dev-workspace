# Research QA Platform Site Integration

## Status
Open

## Priority
Medium — depends on portfolio site being stable, strategic for showcasing QA work

## Summary
Figure out how to present the QA platforms (Selenium/Playwright for UI/API testing, Docker/SSH image testing) as polished web properties. Decide whether to integrate them into the existing portfolio site or build separate product sites that the portfolio links to. Use the web cloner to follow the same design process as the portfolio site — find reference sites, clone visual patterns, adapt to our content.

## Requirements

### Decision: Integrate vs Separate Sites
- **Option A:** Add QA platform pages/sections to the existing portfolio site (isagawa.co)
- **Option B:** Build separate product sites (e.g., qa.isagawa.co or standalone domains) that the portfolio references as "featured work"
- Research which approach competing QA tool companies use (Playwright.dev, Cypress.io, Sauce Labs)
- Consider: does a portfolio site with product pages feel cohesive, or does it dilute the personal brand?

### QA Platforms to Showcase
- **Selenium/Playwright platform** — UI/API test automation, cross-browser, reporting
- **Docker/SSH image testing** — infrastructure compliance, server hardening validation
- Each platform needs its own visual identity and clear value prop

### Design Process (same as portfolio site)
- Use web cloner skill to find and clone reference sites for QA/DevOps tool landing pages
- Identify visual patterns from best-in-class tool sites (Playwright.dev, Cypress.io, Vercel, Linear)
- Adapt cloned patterns to our content and branding
- Desktop + mobile responsive

### Open Questions
- Do the QA platforms have enough maturity to warrant their own sites, or is a portfolio showcase sufficient for now?
- Should these be static sites (GitHub Pages) or do they need dynamic elements (live demos, API playgrounds)?
- Naming/domain strategy — subdomains of isagawa.co vs separate domains?

## References
- Portfolio site: [isagawa.co](https://www.isagawa.co) / backlog [047](done/047-market-build-portfolio-site-loop-theme.md), [053](done/053-market-refactor-portfolio-site-visual-layer.md), [055](done/055-market-build-portfolio-site-v2-terminal.md)
- QA platform (Selenium): `D:\my_ai_projects\project_test_repos\isagawa-qa-platform`
- SSH image testing: backlog [020](done/020-domain-build-ssh-image-testing-platform.md), [026](done/026-domain-build-ssh-compliance-testing.md)
- Website cloner skill: `.claude/skills/website-cloner/`
- Playwright saucedemo suite: backlog [024](done/024-test-build-playwright-saucedemo-suite.md)

## Task Builder Input
- **Deliverable:** Research report with site strategy decision, reference site analysis, wireframes/mockups, and recommended next steps
- **Location:** subproject:qa-platform-site
- **Scope:** RESEARCH
- **Constraints:** Depends on web cloner skill for reference site analysis. Portfolio site (isagawa.co) is the existing property. QA platforms exist but may need maturity assessment before building public-facing sites. Design process should mirror the portfolio site workflow (clone references → adapt → build).
