# Build CSS Responsive Media Query Skeleton

## Context
Reads the breakpoint extraction data and writes empty media query blocks at the bottom of `styles.css`. These serve as the responsive skeleton that Phase 3 component styles will populate.

## Type
BUILD

## Execution
inline

## Dependencies
- 028 (grid and layout utilities written)

## Requirements
- Read `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-breakpoints.json` for breakpoint values
- Append media query skeleton at the bottom of `D:\my_ai_projects\isagawa-portfolio-site\styles.css`:
  ```css
  /* Tablet and below */
  @media (max-width: 1024px) {
  }

  /* Mobile */
  @media (max-width: 768px) {
  }
  ```
- Use breakpoint values from the extraction data if they differ from 1024px/768px
- Add comment headers for each breakpoint
- Do NOT modify any preceding CSS

## Acceptance Criteria
- [ ] At least two `@media` blocks exist at the bottom of `styles.css`
- [ ] Breakpoint values are sourced from extraction data (or sensible defaults)
- [ ] Media query blocks are empty (ready for Phase 3 population)
- [ ] Preceding CSS blocks are unchanged

## Gates Satisfied
BUILD-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
