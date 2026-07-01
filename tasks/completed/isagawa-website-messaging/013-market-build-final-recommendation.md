# Write Final Recommended Copy Package

## Context
Synthesize all copy variants, supporting copy, and audience alignment into a single recommended copy package ready for implementation on isagawa.co.

## Type
BUILD

## Execution
inline

## Dependencies
- 008-market-build-hero-variant-a
- 009-market-build-hero-variant-b
- 010-market-build-hero-variant-c
- 011-market-build-supporting-copy
- 012-market-build-audience-alignment

## Phase Gate
- [ ] `projects/isagawa-website-messaging/copy-variants/variant-a-technical.md` exists
- [ ] `projects/isagawa-website-messaging/copy-variants/variant-b-business.md` exists
- [ ] `projects/isagawa-website-messaging/copy-variants/variant-c-future.md` exists
- [ ] `projects/isagawa-website-messaging/supporting-copy.md` exists
- [ ] `projects/isagawa-website-messaging/audience-alignment.md` exists

## Requirements
- Read all copy variants, supporting copy, and audience alignment
- Write `projects/isagawa-website-messaging/final-recommendation.md` with:
  - **Recommended Hero Copy** — select best variant or synthesize from multiple, with rationale
  - **Recommended Subheader** — selected from supporting-copy.md options
  - **Recommended Section Copy** — rewritten versions of each homepage section
  - **Recommended CTAs** — selected from supporting-copy.md options
  - **Implementation Notes** — what needs to change in the HTML, alignment with backlog 124 aesthetic directive
  - **Audience Coverage Verification** — confirm all 3 audiences are addressed
- This is the final deliverable — it should be actionable for implementation

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/final-recommendation.md` exists
- [ ] File contains "Recommended" copy for hero, subheader, sections, CTAs
- [ ] File contains implementation notes
- [ ] File addresses all 3 audience segments

## Gates Satisfied
BUILD-09, FUNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
