# Write Seed Section (Anchor Moment 1)

## Context
The Seed section is the first anchor moment. It tells the story of the original kernel — the smallest thing that carries the idea. Show what was built by hand (minimal) and what it enabled (everything else). The 4 kernel mechanisms (hooks, commands, session-start, anchor) are the evidence.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-build-html-rewrite-skeleton

## Phase Gate
- [ ] `index.html` contains `id="seed"` section stub

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Replace seed stub with content:
  - Section number: "01"
  - Title: "The Seed"
  - Subtitle: "A minimal kernel — hooks, commands, and a protocol — that governs everything built after it."
  - Narrative paragraph: explain what the kernel IS, not how it works. Built by hand. Four mechanisms. Cannot be bypassed.
  - Evidence grid with 4 cards:
    1. **Anchor Token** — every 10 actions, forces re-centering. UUID proves compliance.
    2. **Gate Enforcer** — blocks writes until prerequisites met. Hook at the tool-call boundary.
    3. **Learn Loop** — every failure records a lesson. Protocol updates mechanically.
    4. **Session Protocol** — start → anchor → work → complete. Same loop, every session.
  - Each card: h3 title + p description. Class `evidence-card`.
  - Wrap cards in `evidence-grid` div.
- No jargon in the narrative paragraph — technical detail goes in the evidence cards
- Reference: `docs/backlog/047-market-build-portfolio-site-loop-theme/theme-and-narrative.md` (Section 1: Seed)

## Acceptance Criteria
- [ ] `index.html` seed section contains "The Seed" heading
- [ ] `index.html` seed section contains 4 `.evidence-card` elements
- [ ] `index.html` seed section contains "Anchor Token" text

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
