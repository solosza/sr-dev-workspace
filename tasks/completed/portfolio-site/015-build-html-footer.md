# Write Footer

## Context
The footer closes the page. It should reinforce the loop theme with a final tagline and provide contact/link information. Keep it minimal — the punchline was already delivered in "This Page."

## Type
BUILD

## Execution
inline

## Dependencies
- 014-build-css-provenance

## Phase Gate
- [ ] Provenance section CSS written in `styles.css`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Replace footer stub with:
  - Tagline: "Built by the system it describes."
  - Contact section: email link or "Get in touch" placeholder
  - Links: GitHub (if applicable)
  - Copyright: "© 2026 Isagawa"
- Use `<footer>` semantic element
- Keep minimal — no navigation duplication

## Acceptance Criteria
- [ ] `index.html` contains `<footer` element
- [ ] `index.html` footer contains "Built by the system it describes"
- [ ] `index.html` footer contains "© 2026"

## Gates Satisfied
- BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
