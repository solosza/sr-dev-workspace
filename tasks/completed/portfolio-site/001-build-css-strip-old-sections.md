# Strip Old Section CSS

## Context
The existing `styles.css` at `D:\my_ai_projects\isagawa-portfolio-site\styles.css` has section-specific CSS for the old site framing (Architecture, Output Cards, Kernel Cards). These must be removed to make room for the new 4-anchor-moment structure. Keep the `:root` variables, reset, base, layout, hero styles, and responsive skeleton.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Read `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Remove all CSS from `/* Architecture */` through `.kernel-card p` (approximately lines 179-378)
- Remove old responsive rules that reference `.output-cards` and `.kernel-cards`
- Keep: `:root` block, `/* Reset */`, `/* Base */`, `/* Layout */`, `/* Hero */`, and the `@media` skeleton (empty breakpoint blocks)
- Preserve the hero CSS as-is — hero copy changes happen in HTML, not CSS

## Acceptance Criteria
- [ ] `styles.css` has no `.diagram` classes
- [ ] `styles.css` has no `.output-card` classes
- [ ] `styles.css` has no `.kernel-card` classes
- [ ] `styles.css` retains `:root` block with all CSS custom properties
- [ ] `styles.css` retains `/* Hero */` section with `#hero` styles

## Gates Satisfied
- BUILD-13 (partial — old sections removed from CSS)
- BUILD-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
