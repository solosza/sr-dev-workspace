# Write Hero Copy Variant A — Technical Depth

## Context
Write hero section copy variant targeting technical decision-makers. Emphasizes architectural sophistication, enforcement mechanisms, and engineering rigor.

## Type
BUILD

## Execution
inline

## Dependencies
- 007-market-build-positioning-report

## Phase Gate
- [ ] `projects/isagawa-website-messaging/positioning-report.md` exists

## Requirements
- Read positioning report for strategic direction
- Write `projects/isagawa-website-messaging/copy-variants/variant-a-technical.md` with:
  - **Hero Headline** — main headline (5-10 words)
  - **Hero Subheadline** — supporting line (10-20 words)
  - **Hero Description** — 2-3 sentences expanding the value prop
  - **CTA** — primary call-to-action text
  - **Rationale** — why this variant works for technical audiences
- Tone: precise, architectural, no buzzwords
- Must reference actual Isagawa capabilities (hooks, anchor tokens, gate enforcers, learn loops)

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/copy-variants/variant-a-technical.md` exists
- [ ] File contains "Hero" section with headline, subheadline, description
- [ ] File references at least 2 actual Isagawa mechanisms

## Gates Satisfied
BUILD-04, FUNC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
