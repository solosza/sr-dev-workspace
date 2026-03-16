# Build Matching Engine Spec

## Context
The core IP connecting seller and buyer sides. When a deal locks, this fires — matching the deal against the buyer list and orchestrating the disposition process. All output goes into the creative-finance-spec repo.

## Dependencies
- **007** — seller pipeline must be defined (deal-locked trigger comes from here)
- **008** — buyer pipeline must be defined (matching logic, disposition, education referenced)

## Requirements

Read these files before building:
- `creative-finance-spec/pipeline/seller/follow_up.md` (deal-locked trigger)
- `creative-finance-spec/pipeline/buyer/matching.md` (matching algorithm)
- `creative-finance-spec/pipeline/buyer/disposition.md` (outreach rules)
- `creative-finance-spec/pipeline/interfaces/schemas.json` (deal + tenant-buyer schemas)

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\matching\`

### engine.md
- **Trigger**: deal status → "locked" in deal schema
- **Input**: deal data (property, price, monthly, option period, location)
- **Process**:
  1. Load all active buyer profiles
  2. Apply hard filters (location, price, monthly payment) — eliminate non-matches
  3. Score remaining buyers on soft criteria (bedrooms, timeline, option fee budget)
  4. Rank by total score descending
  5. Return top N matches with scores and match details
- **Output**: ranked buyer list with: buyer_id, score, matched_criteria, gap_criteria
- **Edge cases**: no matches found → notify investor, expand search radius suggestion. Only 1-2 matches → flag as thin pipeline.
- **State update**: deal schema `matched_buyers` array populated with results

### ranking.md
- Scoring weights (must total 100):
  - Location match: X points (define: exact zip, same city, adjacent area)
  - Price fit: X points (define: under budget, at budget, 5-10% over)
  - Monthly payment fit: X points (same tiers)
  - Bedrooms match: X points
  - Timeline alignment: X points (buyer ready in time for option period)
  - Option fee vs budget: X points
- Tier definitions:
  - Excellent match (85+): contact immediately
  - Good match (65-84): contact in first batch
  - Moderate match (50-64): contact in second batch
  - Below 50: do not contact for this deal

### outreach_rules.md
- Batch logic:
  - Batch 1: excellent matches — send immediately
  - Batch 2: good matches — send 24 hours later (if no batch 1 responses)
  - Batch 3: moderate matches — send 48 hours later (if no batch 1-2 responses)
- Send limits: max 10 outreach emails per deal per day (avoid spam triggers)
- Stagger: 5-10 minute delay between sends (not all at once)
- Personalization: each email must reference the specific criteria that matched
- Template selection: based on buyer segment (from 008 disposition.md)
- Track: opens, replies, clicks — feed back into buyer profile

### response_handling.md
- **Interested reply**: move buyer to education sequence (if new to lease options) or schedule call (if experienced). Update deal `matched_buyers` with response status.
- **Questions**: route to investor with context (deal details + buyer profile + their question). Optionally: agent attempts to answer from objection map (003 research) first.
- **Not interested**: mark in buyer profile, do not contact for this deal again. Keep in nurture for future deals.
- **No response after full sequence**: mark as no-response, keep in nurture.
- **Handoff point**: buyer confirms interest AND either completes education sequence or is experienced → investor takes the call. System provides investor with: buyer profile, deal details, match score, all prior communication.

## Output
- `creative-finance-spec/pipeline/matching/engine.md`
- `creative-finance-spec/pipeline/matching/ranking.md`
- `creative-finance-spec/pipeline/matching/outreach_rules.md`
- `creative-finance-spec/pipeline/matching/response_handling.md`

## Validation (check ALL before completing)
- [ ] All 4 files exist at their output paths
- [ ] engine.md defines trigger, input, process steps, output format, and edge cases
- [ ] engine.md references deal schema status field
- [ ] ranking.md has scoring weights that total 100 with tier definitions
- [ ] ranking.md defines specific score ranges for each tier
- [ ] outreach_rules.md defines batch logic with timing
- [ ] outreach_rules.md defines send limits and stagger timing
- [ ] response_handling.md covers all 4 response types (interested, questions, not interested, no response)
- [ ] response_handling.md defines the investor handoff point with what data is provided
- [ ] All files cross-reference schemas from 006 and pipeline files from 007/008

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
