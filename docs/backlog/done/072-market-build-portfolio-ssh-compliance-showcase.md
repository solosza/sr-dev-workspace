# Build Portfolio Showcase — SSH Compliance Testing

## Status
Open

## Priority
High — SSH compliance testing is the most enterprise-relevant product; directly maps to government/defense contract requirements (STIG, CIS, NIST, FIPS). Targets DevSecOps and compliance teams.

## Summary
Build a product showcase page for platform-ssh on isagawa.co. The page presents the SSH compliance testing platform as its own product: automated SSH hardening validation against four federal compliance frameworks, driven by pytest, fixtures, and purpose-built validators. The "built by the loop" message leads (this entire platform — validators, fixtures, test infrastructure — was produced from a domain spec by the same factory), then the product stands on its own merits.

## Framing

### Up front — built by the loop
This platform was produced from a domain spec. The factory read the spec, decomposed it into tasks, and built the entire compliance testing infrastructure autonomously — validators, fixtures, configs, test harness. One sentence, one link back to the main site. Then move on to the product.

### The product — what it does for YOU
- **SSH configs drift. Manual audits are slow. Compliance gaps hide until the auditor finds them.**
- Point the platform at your hosts. It validates SSH configurations against STIG, CIS Level 1, NIST 800-171, and FIPS 140-3 — automatically. Fixture-driven, so adding new hosts or new compliance frameworks is config, not code.
- pytest-based. Runs in CI/CD. Produces compliance reports you can hand to auditors.

### Target users
- DevSecOps teams maintaining fleet SSH hardening
- Government/defense contractors needing continuous STIG compliance
- Security teams running compliance audits before and during production
- MSPs managing SSH configurations across customer environments

## Requirements

### Content Sections
- **Built by the loop** — one line + link establishing this came from the factory
- **Hero:** "Automated SSH compliance against four federal frameworks." + terminal showing pytest compliance run with pass/fail per framework
- **Problem:** SSH configurations drift from baselines. Manual audits take days. You find out you're non-compliant when the auditor does. Continuous compliance shouldn't require continuous human effort.
- **Frameworks supported:** STIG, CIS Benchmarks Level 1, NIST 800-171, FIPS 140-3 — each with a brief description and what it covers
- **How it works:** Flow diagram — host config (fixture) → validator selection → pytest execution → compliance report per framework
- **Architecture:** Fixture-driven design. Adding a new host = new YAML fixture. Adding a new framework = new validator module. No code changes for new targets.
- **Demo:** Terminal or GIF showing a real compliance run against a host with pass/fail output per framework
- **Tech stack:** Python, pytest, Paramiko, STIG/CIS/NIST/FIPS — badges
- **Results:** Validators per framework, total compliance checks, frameworks supported (4), time per audit

### Design Constraints
- Match existing isagawa.co visual language (dark theme, terminal aesthetic)
- Mobile responsive
- Static (GitHub Pages compatible)
- **Feature branch:** `feature/showcase-ssh-compliance` in `isagawa-co.github.io` repo. Do not merge to main until user approves.
- Links back to main site Self-Extension section and to the live feed page (from 075)

### Reference Designs
- Linear.app case studies
- Vercel customer showcases
- Playwright.dev (developer-focused testing tool presentation)

## References
- Portfolio site (live): `D:\my_ai_projects\isagawa-co.github.io` (deploys to www.isagawa.co)
- SSH compliance platform (GitHub): `https://github.com/isagawa-qa/platform-ssh`
- SSH compliance spec (GitHub): `https://github.com/isagawa-co/docker-spec` (related infra)
- Compliance testing backlog: backlog [026](done/026-domain-build-ssh-compliance-testing.md) (done)
- Live feed page: backlog [075](075-market-build-portfolio-live-feed-update.md) (ships first)
- Website cloner skill: `.claude/skills/website-cloner/`

## Task Builder Input
- **Deliverable:** SSH compliance testing showcase page on isagawa.co — product page with "built by the loop" lead-in, hero, problem, frameworks overview, how-it-works flow, architecture, demo, results. On feature branch `feature/showcase-ssh-compliance`.
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Feature branch only — do not merge to main. Must match existing dark theme terminal aesthetic. Static HTML/CSS (GitHub Pages). Content written from the platform-ssh repo's README and compliance framework docs. Product-first framing — the SSH compliance platform is its own product, not just a kernel demo.
