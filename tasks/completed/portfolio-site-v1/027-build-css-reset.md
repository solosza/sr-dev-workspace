# Build CSS Reset and Base Styles

## Context
Writes the CSS reset/normalize block and base body styles immediately after the `:root` block in `styles.css`. This ensures consistent cross-browser rendering and applies the design tokens to the document root.

## Type
BUILD

## Execution
inline

## Dependencies
- 026 (all design tokens written to :root block)

## Requirements
- Append the following after the `:root` closing brace in `D:\my_ai_projects\isagawa-portfolio-site\styles.css`:
- CSS reset rules:
  - `*, *::before, *::after { box-sizing: border-box; }`
  - `* { margin: 0; padding: 0; }`
- Base body styles using design tokens:
  - `font-family: var(--font-body)`
  - `background-color: var(--bg-primary)`
  - `color: var(--text-primary)`
  - `line-height: 1.6` (or value from extraction data if available)
  - `font-size: var(--text-base)`
- Base heading styles:
  - `font-family: var(--font-heading)`
- Base link/anchor styles:
  - `color: var(--accent)`
  - `text-decoration: none`
- Do NOT modify the `:root` block

## Acceptance Criteria
- [ ] CSS reset block is present after `:root`
- [ ] Body styles reference design token variables
- [ ] Box-sizing border-box is applied universally
- [ ] Margin and padding are reset
- [ ] `:root` block and all tokens are unchanged

## Gates Satisfied
BUILD-21

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
