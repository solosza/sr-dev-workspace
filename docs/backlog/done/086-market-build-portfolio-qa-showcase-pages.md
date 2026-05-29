# Portfolio QA Showcase Pages

## Status
Open

## Priority
Medium — strengthens personal brand narrative; platforms are mature enough for showcase but not for standalone product sites

## Summary
Add 2-3 project showcase pages to the existing portfolio site (isagawa.co) for the most differentiated QA platforms: attestation pipeline, SSH compliance testing, and optionally UI testing framework. Pages should match the existing dark theme/terminal aesthetic, be static (GitHub Pages compatible), and live under isagawa.co/projects/[name]. This follows the Option C Hybrid approach — portfolio now, separate product sites later if demand materializes.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[086-market-build-portfolio-qa-showcase-pages/attestation-showcase]] | Attestation pipeline showcase page — most differentiated offering |
| [[086-market-build-portfolio-qa-showcase-pages/ssh-compliance-showcase]] | SSH compliance testing showcase page — enterprise niche value |
| [[086-market-build-portfolio-qa-showcase-pages/ui-testing-showcase]] | UI testing framework showcase page — optional, commodity space |
| [[086-market-build-portfolio-qa-showcase-pages/design-constraints]] | Visual language, layout patterns, reference sites, content template |

## Architecture

```
isagawa.co (existing portfolio site)
├── index.html (existing — hero, provenance, terminal sections)
├── projects/
│   ├── attestation/index.html    ← NEW: attestation pipeline showcase
│   ├── ssh-compliance/index.html ← NEW: SSH compliance showcase
│   └── ui-testing/index.html     ← NEW (optional): UI testing showcase
├── styles.css (extend with project page styles)
└── assets/ (screenshots, diagrams, demos)
```

## Requirements
- Match existing isagawa.co visual language (dark theme, terminal aesthetic, monospace fonts)
- Mobile responsive (same breakpoints as portfolio)
- Static HTML/CSS (GitHub Pages compatible — no build step)
- Each page: hero + problem statement + architecture + tech stack + demo/screenshots + results
- Navigation: portfolio homepage links to showcase pages and back
- Clone reference designs for developer project case study pages before building

## References
- Existing portfolio site: `D:\my_ai_projects\isagawa-co.github.io`
- Research report: backlog 060 (QA Platform Site Integration research)
- Attestation pipeline: `lib/attestation/` in sr_dev_workspace
- SSH compliance: `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`
- Reference sites: Linear.app case studies, Vercel showcases, Stripe dev docs

## Task Builder Input
- **Deliverable:** 2-3 project showcase pages added to isagawa.co portfolio site
- **Location:** new-repo:D:\my_ai_projects\isagawa-co.github.io
- **Scope:** BUILD
- **Constraints:** Must use existing design system (dark theme, terminal aesthetic). Static HTML/CSS only. Clone reference designs first. GitHub Pages deployment.
