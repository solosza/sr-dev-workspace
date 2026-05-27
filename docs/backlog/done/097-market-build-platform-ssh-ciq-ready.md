# Professionalize Platform-SSH for CIQ

## Status
Open

## Priority
High — CIQ contact is waiting for the link; business-critical first impression

## Summary
Get platform-ssh presentation-ready for CIQ's engineering team. The CIQ contact needs an isagawa.co/ssh-compliance link to share internally. That landing page must link to the GitHub repo, and the GitHub repo must look professional with appropriate CTA, contact info, LICENSE, and example output. This is the first external-facing deliverable — it sets the tone for the relationship.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[097-market-build-platform-ssh-ciq-ready/github-repo-professionalization]] | README overhaul, LICENSE, badges, example output, CTA |
| [[097-market-build-platform-ssh-ciq-ready/landing-page-updates]] | ssh-compliance.html updates — GitHub link, contact info, CIQ-ready messaging |
| [[097-market-build-platform-ssh-ciq-ready/quick-wins-checklist]] | Ordered checklist of all changes with priority tiers |

## Current State

**GitHub repo** (`isagawa-qa/platform-ssh`):
- README: 239 lines, solid architecture overview — but no contact info, no CTA, no LICENSE, no badges
- Code: 5-layer architecture, 8 compliance frameworks, validators, tests
- Missing: LICENSE, CI badges, example test output, enterprise messaging

**Landing page** (`isagawa.co/ssh-compliance`):
- Exists with professional styling, compliance ticker, architecture section
- Has "View on GitHub" CTA — needs verification it links correctly
- Missing: prominent contact info, case study/pilot section

## Requirements
- LICENSE file (MIT) in platform-ssh repo
- README updated with: contact CTA, badges (compliance frameworks, Python version), example scan output
- ssh-compliance.html verified/updated with correct GitHub link
- Contact info visible on landing page (not just footer)
- No broken links between landing page and GitHub

## References
- Platform-SSH repo: https://github.com/isagawa-qa/platform-ssh
- Landing page: https://www.isagawa.co/ssh-compliance.html
- Website repo: D:\my_ai_projects\isagawa-co.github.io\

## Task Builder Input
- **Deliverable:** Professional platform-ssh GitHub repo + updated isagawa.co landing page, ready for CIQ to review
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh` + `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Two repos to update (platform-ssh + isagawa-co.github.io). Changes must be committed and pushed to be live. CIQ contact is waiting — speed matters.
