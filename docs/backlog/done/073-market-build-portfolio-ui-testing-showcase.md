# Build Portfolio Showcase — AI-Native Test Automation

## Status
Open

## Priority
High — the QA platform family (Selenium, Playwright, Docker, DeepEval) is the most mature product line. Multiple platforms, multiple stacks, all governed. Targets QA leads, engineering managers, and teams evaluating AI-assisted test automation.

## Summary
Build a product showcase page for the isagawa-qa platform family on isagawa.co. This isn't one framework — it's a family of AI-native test automation platforms across multiple stacks: Selenium (Python), Playwright (TypeScript), Docker image testing, and DeepEval (LLM evaluation). The "built by the loop" message leads (every platform was produced from a domain spec by the same factory), then the products stand on their own. The key selling point: describe what you want to test in plain English, get production-grade 4-layer test code that follows strict architecture — every time, every engineer, every platform.

## Framing

### Up front — built by the loop
Every platform below was produced from a domain spec. The factory read the spec, decomposed it, and built the entire test automation infrastructure — page objects, tasks, roles, tests, fixtures, configs. Different stacks. Same loop. One sentence, one link back to the main site.

### The product family — what it does for YOU
- **AI tests are brittle. Every engineer writes tests differently. Selectors break. Suites become unmaintainable.**
- Describe what you want to test in plain English. The AI agent generates complete test code following a strict 4-layer architecture (Page Object → Task → Role → Test). Every test follows the same patterns. Every locator lives in one place. Every change propagates predictably.
- Works with Claude Code, Cursor, or Windsurf via MCP.

### The platforms

| Platform | Stack | GitHub |
|----------|-------|--------|
| platform-selenium | Python / Selenium / pytest | isagawa-qa/platform-selenium |
| platform-playwright | TypeScript / Playwright | isagawa-qa/platform-playwright |
| platform-docker | Docker container image testing | isagawa-qa/platform-docker |
| platform-deepeval | LLM evaluation with DeepEval | isagawa-qa/platform-deepeval |
| platform-ssh | SSH compliance testing (see backlog 072) | isagawa-qa/platform-ssh |

### Target users
- QA leads evaluating test automation frameworks
- Engineering managers wanting consistent test patterns across teams
- Teams adopting AI-assisted testing who need guardrails, not chaos
- DevOps engineers needing container and infrastructure testing

## Requirements

### Content Sections
- **Built by the loop** — one line + link establishing all platforms came from the factory
- **Hero:** "Describe what to test. Get production-grade test code." + terminal showing AI generating a test from a plain English description
- **Problem:** UI tests are brittle. Every engineer writes them differently. Selectors break on every deploy. Test suites grow unmaintainable. AI-generated tests make it worse — more code, same chaos, no architecture.
- **The architecture:** 4-layer diagram (Page Object → Task → Role → Test) with data flow. Explain each layer's single responsibility. Show how locators live only in Page Objects, composition replaces inheritance, assertions use state-check methods.
- **Multi-platform:** Grid showing all platforms — same architecture, different stacks. Each card: platform name, stack, what it tests, link to GitHub.
- **How it works:** "You describe → AI discovers → AI generates → You run" flow with example at each step
- **Demo:** Terminal or GIF showing a real test generation from plain English description, then pytest execution with green passes
- **Tech stack:** Python, TypeScript, Selenium, Playwright, pytest, MCP — badges
- **Results:** Platform count, total test coverage across platforms, page objects built, pass rates

### Design Constraints
- Match existing isagawa.co visual language (dark theme, terminal aesthetic)
- Mobile responsive
- Static (GitHub Pages compatible)
- **Feature branch:** `feature/showcase-qa-platforms` in `isagawa-co.github.io` repo. Do not merge to main until user approves.
- Links back to main site Self-Extension section and to the live feed page (from 075)
- Cross-links to SSH compliance showcase (072) since platform-ssh is in the family

### Reference Designs
- Playwright.dev (testing tool presentation — particularly relevant)
- Cypress.io (test automation product page)
- Linear.app case studies

## References
- Portfolio site (live): `D:\my_ai_projects\isagawa-co.github.io` (deploys to www.isagawa.co)
- isagawa-qa org (all platforms): `https://github.com/orgs/isagawa-qa/repositories`
- Platform Selenium: `https://github.com/isagawa-qa/platform-selenium`
- Platform Playwright: `https://github.com/isagawa-qa/platform-playwright`
- Platform Docker: `https://github.com/isagawa-qa/platform-docker`
- Platform DeepEval: `https://github.com/isagawa-qa/platform-deepeval`
- Platform SSH: `https://github.com/isagawa-qa/platform-ssh`
- QA framework architecture: `D:\my_ai_projects\py_sel_framework_mcp\ARCHITECTURE.md`
- QA framework README: `D:\my_ai_projects\py_sel_framework_mcp\README.md`
- Selenium spec: `https://github.com/isagawa-co/selenium-spec`
- Playwright spec: `https://github.com/isagawa-co/playwright-spec`
- Docker spec: `https://github.com/isagawa-co/docker-spec`
- Live feed page: backlog [075](075-market-build-portfolio-live-feed-update.md) (ships first)
- Website cloner skill: `.claude/skills/website-cloner/`

## Task Builder Input
- **Deliverable:** AI-native test automation showcase page on isagawa.co — product page with "built by the loop" lead-in, hero, problem, 4-layer architecture diagram, multi-platform grid, how-it-works flow, demo, results. On feature branch `feature/showcase-qa-platforms`.
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Feature branch only — do not merge to main. Must match existing dark theme terminal aesthetic. Static HTML/CSS (GitHub Pages). Content written from platform-selenium's ARCHITECTURE.md, README.md, and the isagawa-qa org repos. Product-first framing — the QA platform family is its own product line, not just a kernel demo. Showcase all platforms in the family, not just Selenium.
