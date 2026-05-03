# Add Smooth Scroll

## Context
Nav links point to section IDs (#seed, #growth, etc.). Add CSS-only smooth scrolling and scroll-margin-top to account for the fixed header height.

## Type
BUILD

## Execution
inline

## Dependencies
- 016-build-css-nav-footer

## Phase Gate
- [ ] Nav CSS written in `styles.css`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Add `html { scroll-behavior: smooth; }`
- Add `scroll-margin-top` to all anchor sections to account for fixed header height (~60px)
- Targets: `#seed, #growth, #self-extension, #this-page, #provenance`

## Acceptance Criteria
- [ ] `styles.css` contains `scroll-behavior: smooth`
- [ ] `styles.css` contains `scroll-margin-top`

## Gates Satisfied
- BUILD-16

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
