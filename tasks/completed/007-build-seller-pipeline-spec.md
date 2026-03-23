# Build Seller Pipeline Spec

## Context
The seller side of the pipeline: lead comes in → qualify → score → first-touch → follow-up. Gate: qualification must pass before any outreach. All output goes into the creative-finance-spec repo.

## Dependencies
- **006** — schemas must exist (seller lead schema referenced throughout)
- **001** — qualification criteria and scoring from deal structure research
- **003** — communication patterns for email generation

## Requirements

Read these files before building:
- `creative-finance-spec/research/001-lease-option-structure.md`
- `creative-finance-spec/research/003-communication-patterns.md`
- `creative-finance-spec/pipeline/interfaces/schemas.json`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\seller\`

### qualification.md
- Input: Seller Lead data (from schema)
- Process: Evaluate each qualification criterion from 001 research
- Output: qualified (yes/no) + reason
- Hard disqualifiers: list each one from research, any single one = reject
- Soft factors: list each, contribute to score
- GATE: If not qualified → log reason, do NOT proceed to outreach. Optionally notify investor of rejected lead with reason.

### scoring.md
- Input: Qualified seller lead
- Output: Score tier (strong / moderate / weak) with numeric score
- Scoring rubric:
  - Strong (80-100): high equity + motivated + flexible + good rental market
  - Moderate (50-79): meets most criteria, one weakness
  - Weak (30-49): meets minimum bar, multiple soft factors missing
- Each criterion: weight (1-10), how to evaluate, data source
- Example: walk through one real scenario and show how score is calculated

### first_touch.md
- Input: Qualified + scored seller lead
- Output: Personalized first-touch email
- Rules: reference voice guidelines from 003 research
- Personalization points: property address, seller's situation (from motivation field), proposed structure
- Template structure: subject line formula, opening hook (acknowledge situation), body (explain option simply), CTA (schedule call), signature
- Score-based variation: strong leads get more direct CTA, weak leads get softer educational approach
- HITL gate: define when draft requires investor approval vs auto-send
  - Default: ALL first touches go as draft for investor review (MVP safety)
  - Configurable: investor can unlock auto-send for scored leads above threshold

### follow_up.md
- Input: Sent first-touch with no response
- Output: Follow-up email sequence
- Cadence from 003 research: Day 1 → Day 3 → Day 7 → Day 14 → nurture or stop
- Each touch: different angle, escalating value (not just "checking in")
- Escalation triggers: seller replies, opens email multiple times, visits website again
- Stop triggers: hard bounce, explicit no, unsubscribe
- "Deal locked" trigger: when investor marks a lead as under contract → status changes to "locked" → triggers buyer matching (task 009)

## Output
- `creative-finance-spec/pipeline/seller/qualification.md`
- `creative-finance-spec/pipeline/seller/scoring.md`
- `creative-finance-spec/pipeline/seller/first_touch.md`
- `creative-finance-spec/pipeline/seller/follow_up.md`

## Validation (check ALL before completing)
- [ ] All 4 files exist at their output paths
- [ ] qualification.md lists specific hard disqualifiers with clear yes/no logic
- [ ] qualification.md defines the gate: not qualified = no outreach
- [ ] scoring.md has numeric scoring rubric with weights per criterion
- [ ] scoring.md includes a worked example
- [ ] first_touch.md has template structure with personalization points
- [ ] first_touch.md defines HITL gate (draft vs auto-send)
- [ ] follow_up.md has specific cadence with day numbers
- [ ] follow_up.md defines escalation triggers and stop triggers
- [ ] follow_up.md defines the "deal locked" trigger that connects to buyer matching
- [ ] All files reference the seller lead schema from 006

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
