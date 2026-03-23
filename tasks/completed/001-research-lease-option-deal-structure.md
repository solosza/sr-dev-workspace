# Research Lease Option Wholesaling Deal Structure

## Context
Foundation task for the creative finance wholesaling domain spec. Lease option wholesaling is the MVP structure — simplest to qualify, clearest two-sided matching (seller → tenant-buyer). All downstream tasks depend on this domain knowledge.

## Dependencies
None — this is the first task.

## Requirements
- Use **WebSearch** to research lease option wholesaling from public sources: Pace Morby / SubTo content, BiggerPockets forums, wholesaling communities, YouTube educational content, Reddit r/realestateinvesting
- Document how lease option wholesaling works end-to-end: lock seller contract → assign to tenant-buyer → collect assignment fee
- Document **seller qualification criteria** with specific thresholds:
  - Equity position (minimum %)
  - Motivation signals (behind on payments, relocation, divorce, inherited property)
  - Flexibility on price and timeline
  - Property condition and rental market viability
  - Existing loan terms (if any)
- Document **seller disqualifiers**: what makes a property NOT a lease option candidate (e.g., no equity, HOA restrictions, property condition too poor, seller needs immediate cash)
- Document **tenant-buyer qualification criteria** with specific thresholds:
  - Income stability (W-2 vs 1099, minimum income-to-payment ratio)
  - Credit repair trajectory (current score, projected timeline to 620+)
  - Down payment / option fee capacity (typical % range)
  - Timeline to mortgage-ready (12, 24, 36 months)
- Document **tenant-buyer disqualifiers**: recent bankruptcy, no income verification, unrealistic timeline
- Document **scoring logic**: how to rank a seller lead as strong / moderate / weak / not a fit — with specific criteria per tier
- Document **deal economics**: option fee ranges, monthly spread, purchase price markup, assignment fee structure — with example numbers on a real scenario
- Document **common objections** from sellers (at least 5) and tenant-buyers (at least 5) specific to lease options

## Output
- File: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\001-lease-option-structure.md`

## Validation (check ALL before completing)
- [ ] File exists at the output path
- [ ] Seller qualification criteria documented with **numeric thresholds** (not vague like "good equity")
- [ ] Seller disqualifiers documented (at least 5)
- [ ] Tenant-buyer qualification criteria documented with **numeric thresholds**
- [ ] Tenant-buyer disqualifiers documented (at least 4)
- [ ] Scoring logic documented with clear tier definitions (strong/moderate/weak/not a fit)
- [ ] Deal economics documented with at least one worked example using real numbers
- [ ] Objection map has at least 5 seller + 5 tenant-buyer objections with responses
- [ ] All content sourced from public domain knowledge (cite sources where possible)
- [ ] File is well-organized with clear headings per section

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
