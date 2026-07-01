# Add Spec Catalog Page to isagawa.co

## Status
Open

## Priority
High — the isagawa-co org has 40+ published specs; a catalog page turns invisible breadth into visible proof of range

## Summary
Add a single `catalog.html` page to www.isagawa.co that shows every vertical domain spec published under the isagawa-co GitHub org, organized by category. Each spec gets a card with its name, description, and a GitHub link. This is not a collection of individual product pages — it is one browsable index that communicates the full scope of what the factory has produced. The goal is for a visitor to land here and immediately understand the range: security, games, career tools, healthcare, DevOps, real estate.

## Requirements
- Single page: `catalog.html` + `catalog.css` — matches site design system
- Specs organized into category sections with section headers
- Each spec card: name, one-line description (from GitHub repo description), GitHub link
- Categories and initial specs:
  - **Security / Compliance:** pci-dss-spec, aml-kyc-spec, sox-audit-spec, hipaa-audit-spec, incident-response-spec, iac-security-spec
  - **Games:** dnd-game-engine, terminal-game-builder-spec, ai-football-game
  - **Career:** job-application-spec
  - **Healthcare:** healthcare-qa-spec, claims-testing-spec, edi-testing-spec
  - **DevOps / CI-CD:** github-actions-spec, gitlab-ci-spec, azure-devops-spec, network-automation-spec
  - **Real Estate:** lease-option-spec
- Uses `pill-nav.css` + `pill-nav.js` (matches other pages)
- Add "Catalog" link to pill-nav across all existing pages
- Loop badge: "Every spec below was produced from an agent by the same system described on the homepage."
- CTA at bottom links to `https://github.com/isagawa-co` (full org)

## References
- GitHub org: `https://github.com/isagawa-co`
- Pattern reference: `D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html`
- Related backlog: 110-market-build-job-application-product-page.md

## Task Builder Input
- **Deliverable:** `catalog.html` + `catalog.css` in `isagawa-co.github.io`, plus pill-nav updates across all existing product pages
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Descriptions pulled from GitHub repo metadata (or hardcoded from current descriptions). Nav update touches 6+ existing HTML files. All changes on a feature branch.
