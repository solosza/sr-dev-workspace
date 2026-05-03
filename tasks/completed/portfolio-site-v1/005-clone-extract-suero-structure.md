# Extract Suero Studio Page Structure

## Context
Extract the semantic page structure (headings, sections, navigation, footer) from Suero Studio's DOM. This becomes the blueprint for the portfolio site's HTML skeleton.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-clone-screenshot-suero-mobile.md

## Requirements
- Reset viewport: `browser_resize` with `{ "width": 1440, "height": 900 }`
- Use `browser_snapshot` to capture the full accessibility tree / DOM structure
- Analyze the snapshot output for: section headings, landmark regions, navigation structure, content hierarchy
- Write a structured markdown summary to `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-structure.md` containing:
  - Page title
  - List of top-level sections with their purpose (hero, process, testimonials, CTA, footer, etc.)
  - Heading hierarchy (h1, h2, h3 usage)
  - Navigation items
  - Content blocks per section
- Reference: `.claude/skills/website-cloner/references/extraction.md` — Step 3

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-portfolio-site\extraction\suero-structure.md` exists
- [ ] File contains identified section headings (at least 3 sections)

## Gates Satisfied
CLONE-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
