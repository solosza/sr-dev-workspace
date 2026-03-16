# Build Buyer Pipeline Spec

## Context
The buyer side of the pipeline: maintain buyer list → match deals → personalized outreach → assignment education sequence → calendar scheduling. All output goes into the creative-finance-spec repo.

## Dependencies
- **006** — schemas must exist (tenant-buyer and deal schemas referenced throughout)
- **002** — buyer types and matching criteria from research
- **003** — communication patterns for outreach and education sequence

## Requirements

Read these files before building:
- `creative-finance-spec/research/002-buyer-types-matching.md`
- `creative-finance-spec/research/003-communication-patterns.md`
- `creative-finance-spec/pipeline/interfaces/schemas.json`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\buyer\`

### list_management.md
- How buyer profiles are imported: CSV upload (mapped to schema), manual entry, webhook from buyer registration form
- How profiles are updated: new interaction updates `last_contact`, credit score updates, criteria changes
- Segmentation logic: auto-segment based on schema fields → buyer segment (from 002 research)
- Deduplication: match on email, flag duplicates for merge

### matching.md
- Trigger: deal status changes to "locked" (from seller pipeline task 007)
- Algorithm: compare deal attributes against each buyer's criteria
- Hard filters: location match (buyer's target_areas contains deal's city/zip), price ≤ buyer's max_price, monthly ≤ buyer's max_monthly_payment
- Soft scoring: bedrooms match, timeline alignment, option fee vs budget
- Output: ranked list of matching buyers with scores
- Reference ranking logic from 002 research

### disposition.md
- Input: ranked buyer list for a locked deal
- Output: personalized outreach email per buyer
- Personalization: buyer's name, their specific criteria that matched, deal details, why this fits them
- Messaging differentiation per segment (from 002 research): first-time buyer gets educational framing, credit repair candidate gets encouragement framing
- Batch rules: send to top 5-10 matches, stagger sends (not all at once), track opens/replies

### education_sequence.md
- Trigger: buyer responds with interest but hasn't done a lease option before
- Multi-step email flow (from 003 research):
  - Email 1: What is a lease option (plain English, no jargon)
  - Email 2: How the money works (option fee, monthly, purchase price)
  - Email 3: Your timeline (credit repair path, what they need to do)
  - Email 4: FAQ (common concerns from 003 objection map)
  - Email 5: Next steps (schedule a call with investor)
- Timing: one email every 2-3 days
- Exit conditions: buyer schedules call (success), buyer goes cold (back to nurture), buyer opts out (stop)

### scheduling.md
- Trigger: buyer wants to talk (replies to email or clicks scheduling link)
- Calendar integration: create calendar event via gws CLI (from 004 research)
- Event details: investor name, buyer name, deal reference, prep notes for investor
- Confirmation email to buyer: time, what to expect on the call, what to bring (income docs, credit report)
- Reminder: 24 hours before the call

### nurture.md
- Target: buyers in the list with no current deal match
- Cadence: every 2-4 weeks
- Content: market updates in their target areas, new listings that might become lease options, credit repair tips, success stories
- Purpose: keep them warm until a matching deal comes in
- Exit: buyer matches a new deal (move to matching), buyer requests removal (stop)

## Output
- `creative-finance-spec/pipeline/buyer/list_management.md`
- `creative-finance-spec/pipeline/buyer/matching.md`
- `creative-finance-spec/pipeline/buyer/disposition.md`
- `creative-finance-spec/pipeline/buyer/education_sequence.md`
- `creative-finance-spec/pipeline/buyer/scheduling.md`
- `creative-finance-spec/pipeline/buyer/nurture.md`

## Validation (check ALL before completing)
- [ ] All 6 files exist at their output paths
- [ ] list_management.md defines import, update, segmentation, and dedup
- [ ] matching.md defines hard filters vs soft scoring with specific fields
- [ ] matching.md references the deal schema status field for trigger
- [ ] disposition.md defines personalization per buyer segment
- [ ] disposition.md defines batch rules (how many, stagger timing)
- [ ] education_sequence.md has 3-5 emails with content summary per email
- [ ] education_sequence.md defines timing and exit conditions
- [ ] scheduling.md defines calendar integration with event details
- [ ] nurture.md defines cadence, content types, and exit conditions
- [ ] All files reference tenant-buyer and deal schemas from 006

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
