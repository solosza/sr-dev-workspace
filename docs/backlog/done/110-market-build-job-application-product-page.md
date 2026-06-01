# Add Job Application Product Page to isagawa.co

## Status
Open

## Priority
High — clear buyer (active job seekers), product is published and polished, fits the site's portfolio-of-factory-outputs story

## Summary
Add a product page for `job-application-spec` to www.isagawa.co. The product does AI execution management for job applications — universal form discovery, profile-driven auto-fill, and human-in-the-loop review before submit. The hook is already strong: "AI can fill forms. But can you trust it to apply correctly?" Needs a page matching the site's existing product page pattern (structure, CSS, pill-nav, footer).

## Requirements
- Page follows the same HTML/CSS/JS structure as `vibe-coder.html` or `qa-platforms.html`
- Uses `pill-nav.css` + `pill-nav.js` for navigation
- Includes the "loop badge" ("Every platform below was produced from an agent by the same system...")
- Sections: hero, problem, how it works, who this is for, CTA to GitHub
- Add `job-application.html` to the Products dropdown in `pill-nav` across all existing pages
- CTA links to `https://github.com/isagawa-co/job-application-spec`
- Consistent footer with other product pages

## References
- GitHub repo: `isagawa-co/job-application-spec`
- Description: "AI execution management for job applications. Universal form discovery, profile-driven filling, and human-in-the-loop review before submit."
- Pattern reference: `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html`
- Pattern reference: `D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html`

## UI Matching Requirement (CRITICAL)
The new page must be **pixel-identical in structure and rendering** to existing product pages. This means:
- Copy the exact same HTML skeleton from `vibe-coder.html` (same element order, same class names, same attributes)
- Copy `vibe-coder.css` as the CSS base — rename to `job-application.css`, change only product-specific copy/colors if needed
- Copy `vibe-coder.js` as the JS base — rename to `job-application.js`, adapt only what changes
- Same `<header class="site-header">`, same `<nav class="pill-nav">`, same `.factory-origin`, same `.loop-badge`, same section structure (`.hero`, `.page-section`, `.flow-grid`, `.flow-card`, etc.), same footer pattern
- Do NOT invent new CSS classes or new layout patterns — reuse what exists exactly
- Agent MUST read `vibe-coder.html`, `vibe-coder.css`, and `vibe-coder.js` in full before writing a single line

## Task Builder Input
- **Deliverable:** `job-application.html` + `job-application.css` + `job-application.js` in `isagawa-co.github.io`, plus pill-nav updates across all product pages
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Must match existing site design system exactly (pixel-identical structure to vibe-coder.html/css/js). All changes on a feature branch. Nav update touches 6+ existing HTML files. Agent must read source files before writing.
