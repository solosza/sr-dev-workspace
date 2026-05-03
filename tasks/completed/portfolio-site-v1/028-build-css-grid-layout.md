# Build CSS Grid and Layout Utilities

## Context
Reads the spacing extraction data and writes container, section, and grid utility classes to `styles.css`. These layout primitives provide the structural foundation for all page sections.

## Type
BUILD

## Execution
inline

## Dependencies
- 027 (CSS reset and base styles written)

## Requirements
- Read `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-spacing.json` for container/grid patterns
- Append layout utility classes after the base styles in `D:\my_ai_projects\isagawa-portfolio-site\styles.css`:
- Container class:
  ```css
  .container {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 0 var(--space-md);
  }
  ```
- Section class:
  ```css
  .section {
    padding: var(--space-section) 0;
  }
  ```
- Grid utility (if grid patterns are present in extraction data):
  ```css
  .grid {
    display: grid;
    gap: var(--grid-gap);
  }
  ```
- Do NOT modify any preceding CSS (`:root`, reset, base styles)

## Acceptance Criteria
- [ ] `.container` class exists with max-width, auto margins, and horizontal padding
- [ ] `.section` class exists with vertical section padding
- [ ] `.grid` class exists with display grid and gap
- [ ] All classes reference design token variables
- [ ] Preceding CSS blocks are unchanged

## Gates Satisfied
BUILD-22

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
