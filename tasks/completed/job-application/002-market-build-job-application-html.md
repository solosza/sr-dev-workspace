# Write job-application.html

## Context
The core deliverable. Must be structurally identical to vibe-coder.html — same element order, same class names, same attributes. Only the product-specific copy, section content, and links differ. The agent MUST read vibe-coder.html in full before writing a single line.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-build-feature-branch

## Phase Gate
- [ ] Branch `feature/job-application-page` is checked out (`git -C "D:/my_ai_projects/isagawa-co.github.io" rev-parse --abbrev-ref HEAD` = `feature/job-application-page`)

## Requirements

**CRITICAL — READ FIRST:** Read `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html` in full before writing. Copy the exact HTML skeleton — do NOT invent structure.

**File:** `D:/my_ai_projects/isagawa-co.github.io/job-application.html`

**Structure to copy exactly from vibe-coder.html:**
- `<head>`: charset, viewport, title (`Isagawa | Job Application Agent`), link `job-application.css`, link `pill-nav.css`
- `<header class="site-header" aria-hidden="true"></header>`
- `<nav class="pill-nav">` with same logo/items/dropdown structure — add `<a href="job-application.html" role="menuitem">Job Application</a>` in the Products dropdown
- `<div class="factory-origin"><a href="index.html">&larr; Built by the factory</a></div>`
- `<div class="loop-badge">` — same text as vibe-coder.html
- `<section class="hero">` with adapted h1 and hero__sub copy
- Product sections using `<section class="page-section">` with `.page-section__label`, h2, `.page-section__narrative`
- Flow cards using `.flow-grid` > `.flow-card` > `.flow-num` + `.flow-content`
- Evidence cards using `.evidence-grid` > `.evidence-card` with `.card-tags`, h3, p
- Tech stack badges using `.badges` > `.badge`
- Results grid using `.results-grid` > `.result-card` with `.result-stat` + `.result-label`
- `<section class="cta reveal">` with `.cta-button` linking to `https://github.com/isagawa-co/job-application-spec`
- Footer with `.footer__grid` > `.footer__col` (same 3-column structure)
- `<script src="job-application.js"></script>` + `<script src="pill-nav.js"></script>` at end of body

**Content to adapt for job application:**
- Hero h1: "Apply smarter. Every form, every time."
- Hero sub: "AI reads job applications automatically. Fills every field from your profile. You review before it submits. No missed fields, no typos, no wasted hours."
- Problem section: The pain of applying to 50 jobs — each with a unique form, repeated copy-paste, constant errors
- How It Works: 4 steps (Discover Form → Match Profile → Fill & Review → Submit)
- Who This Is For: Active job seekers, career changers, recent grads
- Tech stack badges: Isagawa Kernel, Claude Code, Playwright, Python, TypeScript
- Results: 1 agent, Any form, 4 steps, 0 typos
- Footer "More products": qa-platforms.html, vibe-coder.html, ssh-compliance.html, attestation.html

**reveal class:** Apply `.reveal` to elements that should animate in on scroll (same pattern as vibe-coder.html)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/isagawa-co.github.io/job-application.html` exists
- [ ] File contains `pill-nav.css` link tag
- [ ] File contains `pill-nav.js` script tag
- [ ] File contains `class="loop-badge"`
- [ ] File contains `class="hero"`
- [ ] File contains `factory-origin`
- [ ] File contains `page-section` class
- [ ] File contains `github.com/isagawa-co/job-application-spec` in CTA
- [ ] File contains `footer__grid`
- [ ] File references `job-application.css` and `job-application.js`

## Gates Satisfied
- BUILD-02, FUNC-01, FUNC-02, FUNC-03, FUNC-04, FUNC-05, FUNC-06, FUNC-07, FUNC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
