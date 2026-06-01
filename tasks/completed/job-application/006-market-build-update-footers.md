# Update Footer "More Products" Links

## Context
Product pages have a "More products" column in the footer. Job Application should be added to these footer links so users can cross-navigate between products from the footer.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-build-job-application-html

## Phase Gate
- [ ] `D:/my_ai_projects/isagawa-co.github.io/job-application.html` exists

## Requirements

For each page that contains a `footer__col` with "More products" header, add:
```html
<a href="job-application.html">Job Application</a>
```

Pages to check and update:
1. `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html`
2. `D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html`
3. `D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html`
4. `D:/my_ai_projects/isagawa-co.github.io/attestation.html`
5. `D:/my_ai_projects/isagawa-co.github.io/index.html` (check if it has a "More products" footer)

**Read each file before editing** to confirm the footer structure and exact insertion point.

If a page does not have a "More products" footer column, skip it (don't add one).

For `job-application.html` itself: the footer was already written in task 002 — verify it lists the other product pages.

## Acceptance Criteria
- [ ] `vibe-coder.html` footer contains `<a href="job-application.html">`
- [ ] `qa-platforms.html` footer contains `<a href="job-application.html">`
- [ ] `ssh-compliance.html` footer contains `<a href="job-application.html">`
- [ ] `attestation.html` footer contains `<a href="job-application.html">`

## Gates Satisfied
- DOC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
