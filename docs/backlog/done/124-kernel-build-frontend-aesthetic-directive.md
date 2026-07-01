# Kernel: Build Frontend Aesthetic Directive

## Status
Open

## Priority
Medium — prevents aesthetic drift on new pages; one-time effort with ongoing protection

## Summary
Extract the useful parts of the Anthropic `frontend-design` skill and codify them as a site-specific aesthetic directive for the isagawa site. The Anthropic skill's "choose a bold fresh direction" mechanic conflicts with an established brand identity — replace it with "continue the isagawa aesthetic" backed by explicit design tokens and anti-patterns. This eliminates CSS token drift and regression to generic fonts/layouts on new pages.

## Requirements
- Add `## Frontend Aesthetic` section to `D:/my_ai_projects/isagawa-co.github.io/CLAUDE.md`
- Codify design tokens from `projects/frontend-design-research/research-report.md` section 2 (colors, fonts, grain, motion, spacing)
- Include anti-pattern list extracted from the Anthropic skill (no Inter/Roboto/Arial, no purple gradients, no generic layouts)
- Add isagawa-specific anti-patterns (no light themes, no sans-serif headings, no bright accent colors)
- Add rule: new pages MUST import `styles.css` — do not duplicate CSS variables
- Add rule: terminal/code elements use `--badge-workspace-text` for success green, not arbitrary values
- Fix the existing drift: `job-application.html` uses `rgb(34, 197, 94)` instead of `rgb(134, 239, 172)` for terminal green

## Portability Note

The directive pattern itself — "extract anti-patterns + quality bar from a generic skill, replace fresh-direction mechanic with established identity rules" — is reusable beyond UI. Consider whether this generalizes to:

- **Writing / copy style** — isagawa brand voice directive for marketing copy, email, proposals
- **API / SDK design** — code style directive for any SDK we publish (naming, error handling, interface patterns)
- **Report / document formatting** — research report template (headers, tables, summary format)
- **Email tone** — outreach directive for job applications, client proposals, warm contacts

The pattern is: take a generic Anthropic skill → strip the "choose fresh" mechanic → replace with "our established conventions" → add it to the relevant repo's CLAUDE.md. A future backlog could formalize this as a kernel skill template.

## References
- `projects/frontend-design-research/research-report.md` — full analysis + style guide content already written
- `D:/my_ai_projects/isagawa-co.github.io/CLAUDE.md` — target file
- `D:/my_ai_projects/isagawa-co.github.io/styles.css` — token source of truth

## Task Builder Input
- **Deliverable:** `## Frontend Aesthetic` section in `isagawa-co.github.io/CLAUDE.md` + terminal green fix in `job-application.html`
- **Location:** `new-repo:D:/my_ai_projects/isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Style guide content already written in research report — copy and adapt, don't reinvent; fix must match existing design token, not introduce new values
