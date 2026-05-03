# Build CSS Badge Tokens

## Context
Creates badge color variant tokens for the three spec types used in the portfolio: BUILD, WORKSPACE, and OPERATE. These tokens enable visually distinct badges that categorize portfolio items by spec type.

## Type
BUILD

## Execution
inline

## Dependencies
- 025 (component tokens appended to styles.css)

## Requirements
- Append badge tokens inside the existing `:root` block in `D:\my_ai_projects\isagawa-portfolio-site\styles.css`:
  - `--badge-build-bg` — background color for BUILD spec badges
  - `--badge-build-text` — text color for BUILD spec badges
  - `--badge-workspace-bg` — background color for WORKSPACE spec badges
  - `--badge-workspace-text` — text color for WORKSPACE spec badges
  - `--badge-operate-bg` — background color for OPERATE spec badges
  - `--badge-operate-text` — text color for OPERATE spec badges
- Colors should be derived from the accent palette in the extraction data, using distinct but harmonious variants for each spec type
- Existing tokens in `:root` must be preserved

## Acceptance Criteria
- [ ] `:root` block contains all 6 badge tokens (3 bg + 3 text)
- [ ] Badge colors are visually distinct across the three spec types
- [ ] Existing tokens in `:root` are preserved

## Gates Satisfied
BUILD-20

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
