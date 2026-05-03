# Build Responsive Typography

## Context
Heading and body font sizes need to scale down proportionally at each breakpoint. This is the final responsive build task before visual QA testing begins.

## Type
BUILD

## Execution
inline

## Dependencies
- 064-build-responsive-diagrams

## Requirements
- Add media queries for all heading sizes (h1 through h4) at each breakpoint
- Tablet (`max-width: 1024px`): scale headings down proportionally
- Mobile (`max-width: 768px`): scale headings down further
- Ensure body text remains readable (minimum ~14px effective size)
- Badge and label text should also scale if needed

## Acceptance Criteria
- [ ] All heading levels have responsive font-size rules at tablet breakpoint
- [ ] All heading levels have responsive font-size rules at mobile breakpoint
- [ ] Font sizes scale down proportionally (not arbitrarily)
- [ ] Body text remains at least 14px equivalent at mobile
- [ ] `@media` queries are present in `styles.css` for typography

## Gates Satisfied
BUILD-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
