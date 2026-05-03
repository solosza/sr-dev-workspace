# Build Phases

## Status
Reference — execution plan for task decomposition

## Phase 1: Token Merge (consumes 044 output)
- Read all extraction data from `data/portfolio-site/suero/` and `data/portfolio-site/shader/`
- Merge design tokens: Suero structure/spacing/grid + Shader colors/typography/aesthetic
- Resolve conflicts (e.g., Shader `--background` #fff vs computed #000)
- Produce unified CSS custom properties file (`:root { ... }`)
- Produce unified spacing/grid system
- Dark mode / terminal aesthetic from Shader drives the visual identity — not Suero with a dark tint

## Phase 2: CSS Foundation
- CSS reset
- CSS custom properties from merged tokens
- Grid layout system (from Suero spacing data)
- Responsive skeleton (from Suero breakpoints)
- Typography scale (from Shader — or hand-specified if extraction was thin)
- Component tokens (badges, buttons, cards)

## Phase 3: HTML Sections (4 anchor moments)
Build each section with the loop narrative baked in from the start:

| Section | Anchor Moment | Content |
|---------|--------------|---------|
| Nav | — | Isagawa wordmark + minimal nav |
| Hero | The hook | "Self-extending agent harness" + one-sentence loop description |
| Seed | 1. Seed | The kernel — what was built by hand, what it enabled |
| Growth | 2. Growth | Specs, factory, workspaces — the system building itself |
| Self-Extension | 3. Self-Extension | Tasks, backlog, cloner — the loop producing new capabilities |
| This Page | 4. This Page | The punchline — you're reading the output |
| Provenance | Evidence | Sigstore attestation link (if 046 is done) |
| Footer | — | Contact, links |

## Phase 4: Polish
- Responsive testing (mobile, tablet, desktop)
- Dark terminal aesthetic refinement
- Typography hierarchy verification
- Accessibility basics (semantic HTML, contrast, alt text)
- Final screenshot comparison against reference sites

## Dependencies
- Phase 1 depends on backlog 044 (extraction) completing first
- Provenance section depends on backlog 046 (Sigstore attestation) — build placeholder if not ready
