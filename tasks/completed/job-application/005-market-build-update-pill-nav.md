# Update Pill-Nav: Add Job Application to Products Dropdown

## Context
All existing HTML pages have a Products dropdown in their pill-nav. Job Application must be added as a menu item to every page's dropdown so users can navigate to it from anywhere on the site.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-build-job-application-html

## Phase Gate
- [ ] `D:/my_ai_projects/isagawa-co.github.io/job-application.html` exists

## Requirements

Add `<a href="job-application.html" role="menuitem">Job Application</a>` to the `pill-nav__dropdown-menu` Products dropdown in each of the following files:

1. `D:/my_ai_projects/isagawa-co.github.io/index.html`
2. `D:/my_ai_projects/isagawa-co.github.io/feed.html`
3. `D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html`
4. `D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html`
5. `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html`
6. `D:/my_ai_projects/isagawa-co.github.io/story.html`
7. `D:/my_ai_projects/isagawa-co.github.io/attestation.html`

**Position:** Insert after the last existing `<a role="menuitem">` entry in the dropdown, before the closing `</div>` of `pill-nav__dropdown-menu`.

**Read each file before editing it** to confirm the exact insertion point.

**Also ensure job-application.html itself has Job Application in its own nav dropdown** (this was written in task 002, but verify it's present).

## Acceptance Criteria
- [ ] `index.html` contains `job-application.html` in pill-nav dropdown
- [ ] `feed.html` contains `job-application.html` in pill-nav dropdown
- [ ] `qa-platforms.html` contains `job-application.html` in pill-nav dropdown
- [ ] `ssh-compliance.html` contains `job-application.html` in pill-nav dropdown
- [ ] `vibe-coder.html` contains `job-application.html` in pill-nav dropdown
- [ ] `story.html` contains `job-application.html` in pill-nav dropdown
- [ ] `attestation.html` contains `job-application.html` in pill-nav dropdown

## Gates Satisfied
- FUNC-13, FUNC-14, FUNC-15, FUNC-16, FUNC-17, FUNC-18, FUNC-19

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
