# 003 — Write vibe-coder.html

## Type
BUILD

## Description
Write the full HTML page for the Vibe Coder Pack showcase at `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html`. Must match the dark theme terminal aesthetic of existing pages (attestation.html, qa-platforms.html).

## Content Sections (in order)

1. **Header nav** — ISAGAWA logo + links (Home, Feed, Attestation, QA Platforms, SSH Compliance)
2. **Loop badge** — "This product was produced from a domain spec by the same system described on the homepage."
3. **Hero** — "You vibe. Your senior dev builds." + subtitle about governed vibe coding for non-technical builders
4. **Problem** — "You have an idea. You don't know code." — Bolt gives throwaway prototypes, freelancers cost $10K+, YouTube tutorials take months
5. **How It Works** — 4-phase flow cards:
   - Phase 1: Discovery — 4 plain English questions about your app
   - Phase 2: Decisions — AI presents stack options with educational explanations, you pick
   - Phase 3: Scaffold — Working project with architecture enforced
   - Phase 4: Features — Describe features in plain English, agent builds within its own rules
6. **The Difference** — Comparison table: Vibe Coder Pack vs Bolt/Lovable/v0 vs Hiring a Dev
   - Rows: What you get, Technical decisions, After v1, Quality enforcement, User learns, Scales
7. **Self-Governing** — Brief explanation of self-binding pattern: agent generates architecture.md, then enforces it on itself. Hooks, gates, lessons.
8. **Demo Terminal** — Animated terminal showing a /vibe session: discovery questions, decision presentation, scaffold output
9. **Tech Stack** — badges: Isagawa Kernel, Claude Code, Sigstore, Python, TypeScript
10. **Results** — stats: "1 spec, any stack", "4 phases", "Self-binding architecture"
11. **Who This Is For** — 3 cards: Solo founders, Small business owners, Teams adopting AI
12. **CTA** — "Get Started" link to GitHub repo
13. **Footer** — Isagawa, contact, GitHub link

## Design Rules
- Use same CSS class names as attestation.html: `.site-header`, `.nav`, `.hero`, `.page-section`, `.flow-grid`, `.flow-card`, `.evidence-grid`, `.evidence-card`, `.badges`, `.results-grid`, `.cta`, `footer`
- Link CSS: `vibe-coder.css`
- Link JS: `vibe-coder.js` (before closing body)
- Language must be accessible to NON-TECHNICAL users — no jargon in hero/problem/how-it-works
- The comparison table is the centerpiece — make it a styled HTML table, not cards
- Do NOT frame as a Bolt/Lovable competitor — frame as "governed vibe coding harness"

## Acceptance Criteria
- [ ] File exists at `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html`
- [ ] All 13 sections present
- [ ] Hero contains "You vibe" or "vibe" in h1
- [ ] Comparison table contains "Bolt" and "Lovable" and "Freelanc"
- [ ] Loop badge with link to homepage#self-extension
- [ ] Links vibe-coder.css and vibe-coder.js
- [ ] No technical jargon in hero or problem sections (no "API", "framework", "React" etc.)
