# Deploy Portfolio Site V1 to GitHub Pages

## Status
Open

## Priority
High — site is built and attested, needs to go live

## Summary
Deploy the current Isagawa portfolio site (v1, pipeline 047 + 053 visual refactor) to GitHub Pages. Use the existing `isagawa-co` GitHub organization or create the repo under it. The site is a single index.html + styles.css with embedded JS, no build step required.

## Requirements
- Create repo `isagawa-co/isagawa-co.github.io` (or `isagawa-co.github.io` if org doesn't exist yet)
- Copy `D:\my_ai_projects\isagawa-portfolio-site\` contents into the repo
- Enable GitHub Pages on main branch
- Verify the site loads at `https://isagawa-co.github.io`
- Confirm attestation badge Rekor verification works from the live URL (CORS)

## References
- Source: `D:\my_ai_projects\isagawa-portfolio-site\`
- Pipeline 047 (initial build): Rekor #1387966928
- Pipeline 053 (visual refactor): Rekor #1388628067

## Task Builder Input
- **Deliverable:** Live portfolio site on GitHub Pages
- **Location:** new-repo:D:\my_ai_projects\isagawa-co.github.io
- **Scope:** BUILD
- **Constraints:** No build tools, static HTML/CSS/JS only. GitHub Pages must serve from root of main branch.
