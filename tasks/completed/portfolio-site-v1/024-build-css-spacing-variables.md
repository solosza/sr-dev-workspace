# Build CSS Spacing Variables

## Context
Reads the extracted spacing data and appends spacing, layout, and grid tokens to the existing `:root` block in `styles.css`. These tokens control whitespace, container widths, and grid gaps throughout the site.

## Type
BUILD

## Execution
inline

## Dependencies
- 023 (typography variables appended to styles.css)

## Requirements
- Read `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-spacing.json`
- Append spacing tokens inside the existing `:root` block in `D:\my_ai_projects\isagawa-portfolio-site\styles.css`
- Spacing scale tokens:
  - `--space-xs` — extra small spacing
  - `--space-sm` — small spacing
  - `--space-md` — medium spacing
  - `--space-lg` — large spacing
  - `--space-xl` — extra large spacing
  - `--space-section` — vertical section padding
- Layout tokens:
  - `--max-width` — maximum container width
  - `--grid-gap` — default grid gap
- Values must be derived from the extraction JSON

## Acceptance Criteria
- [ ] `:root` block contains all 6 spacing scale tokens
- [ ] `:root` block contains `--max-width` and `--grid-gap`
- [ ] Token values are sourced from the extraction data
- [ ] Existing color and typography tokens in `:root` are preserved

## Gates Satisfied
BUILD-17

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
