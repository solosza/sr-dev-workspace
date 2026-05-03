# Write Self-Extension Section (Anchor Moment 3)

## Context
The Self-Extension section is the third anchor moment. Workspaces producing new capabilities from conversational intent — tasks, backlog, website cloner. The loop extending what future intent can produce. The key evidence is the website cloner skill that extracted the design tokens for this very site.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-build-html-growth

## Phase Gate
- [ ] Growth section content written in `index.html`

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Replace self-extension stub with content:
  - Section number: "03"
  - Title: "Self-Extension"
  - Subtitle: "The system now produces new capabilities from conversation — capabilities that extend what future conversations can produce."
  - Narrative paragraph: the loop extending itself. New skills, new commands, new workflows — all produced by the system, all becoming part of the system.
  - Evidence grid with 3 cards:
    1. **Task Builder** — "Decomposes any goal into atomic, verifiable tasks. Gate contracts ensure mechanical verification. 150+ tasks executed autonomously."
    2. **Website Cloner** — "Extracts design tokens from any live site via Playwright. The design tokens for this page were extracted by this skill."
    3. **Attestation Pipeline** — "Signs every pipeline run with Sigstore. Logs to Rekor for public verification. The provenance section below uses real attestations."
- Reference: `docs/backlog/047-market-build-portfolio-site-loop-theme/theme-and-narrative.md` (Section 3: Self-Extension)

## Acceptance Criteria
- [ ] `index.html` self-extension section contains "Self-Extension" heading
- [ ] `index.html` self-extension section contains 3 `.evidence-card` elements
- [ ] `index.html` self-extension section contains "Website Cloner" text

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
