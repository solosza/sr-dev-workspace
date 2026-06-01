# Write job-application.css

## Context
The CSS for job-application.html. Must be a copy of vibe-coder.css with no structural changes — same CSS variables, same class definitions, same layout rules, same scroll reveal rules. The agent MUST read vibe-coder.css in full before writing.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-build-feature-branch

## Phase Gate
- [ ] Branch `feature/job-application-page` is checked out

## Requirements

**CRITICAL — READ FIRST:** Read `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.css` in full before writing.

**File:** `D:/my_ai_projects/isagawa-co.github.io/job-application.css`

**Copy vibe-coder.css exactly.** Do not change:
- `:root` CSS variables block
- Any layout class (`.page-section`, `.hero`, `.flow-grid`, `.flow-card`, `.evidence-grid`, `.evidence-card`, `.results-grid`, `.result-card`, `.cta`, `.footer__grid`, etc.)
- Scroll reveal rules (`.reveal`, `.reveal.visible`, `.reveal-delay-1/2/3`)
- Hero entrance rules (`.hero`, `.hero.entered`)
- Responsive media queries

The only change allowed: if vibe-coder.css references any vibe-coder-specific image/font that would break, adapt the reference. Otherwise copy verbatim.

## Acceptance Criteria
- [ ] `D:/my_ai_projects/isagawa-co.github.io/job-application.css` exists
- [ ] File contains `:root` block with CSS variables
- [ ] File contains `.reveal` class definition
- [ ] File contains `.hero.entered` rule
- [ ] File is at least 100 lines (ensures it's not a stub)

## Gates Satisfied
- BUILD-03, FUNC-09, FUNC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
