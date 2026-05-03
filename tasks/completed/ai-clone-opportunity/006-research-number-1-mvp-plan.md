# #1 Pick — MVP Plan

## Type
RESEARCH

## Description
For the #1 ranked candidate, create a detailed MVP plan.

## Requirements
1. Select the #1 candidate from the scored matrix
2. Create `projects/ai-clone-opportunity/mvp-plan.md` with:
   - **Product vision** — one paragraph on what this AI-native version IS
   - **MVP feature set** — minimum features to launch (be ruthless, cut scope)
   - **Tech stack** — specific frameworks, APIs, models, hosting
   - **Architecture** — high-level system design (can be text diagram)
   - **Go-to-Market** — first 100 users strategy, pricing, distribution
   - **Timeline** — estimated weeks to MVP, first revenue, product-market fit
   - **Revenue model** — pricing tiers, projected ARR at 6/12/24 months
   - **Risks and mitigations** — top 3 risks with concrete mitigations
3. The plan must be actionable enough to feed directly into a BUILD backlog item
4. Reference backlog 034 (website cloner) — once this pick is made, use the cloner skill to rip the incumbent's UI

## Acceptance Criteria
- [ ] `test -f projects/ai-clone-opportunity/mvp-plan.md`
- [ ] `grep -q "MVP" projects/ai-clone-opportunity/mvp-plan.md`
- [ ] `grep -q "Go-to-Market" projects/ai-clone-opportunity/mvp-plan.md`
- [ ] `grep -q "Tech stack" projects/ai-clone-opportunity/mvp-plan.md`
