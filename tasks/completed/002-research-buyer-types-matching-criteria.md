# Research Buyer Types and Matching Criteria for Lease Options

## Context
The disposition side of lease option wholesaling. When a deal is locked, the system needs to match it against a buyer list. This task defines what a lease option tenant-buyer looks like and how to match deals to buyers.

## Dependencies
- **001** — needs deal structure knowledge to understand what buyers are matching against

## Requirements
- Use **WebSearch** to research tenant-buyer demographics and lease option buyer behavior
- Document **tenant-buyer profiles** (at least 4 distinct segments):
  - Credit repair candidates (recent negative events, on path to recovery)
  - Self-employed / 1099 workers (income hard to document for traditional lending)
  - Recent immigrants (limited credit history)
  - Divorcees rebuilding (assets split, credit dinged)
  - First-time buyers priced out of traditional market
  - Other segments discovered in research
- For each segment: typical situation, what they're looking for, what they can afford, timeline expectations
- Document **matching criteria** with specific fields and data types:
  - Property: bedrooms, bathrooms, square footage, location/neighborhood, school district
  - Financial: price range, monthly payment capacity, option fee budget
  - Timeline: months to mortgage-ready, preferred option period
  - Preferences: must-haves vs nice-to-haves
- Document **ranking logic**: how to score buyer-to-deal fit
  - Exact match (all criteria met) = score X
  - Partial match (location + price, but bedrooms off) = score Y
  - Stretch (one major criterion off) = score Z
  - Define which criteria are hard filters vs soft preferences
- Document **messaging differentiation** per buyer segment: how the same deal gets framed differently for a first-time buyer vs someone rebuilding credit
- Document **buyer list schema**: required fields (name, email, phone, criteria) and optional fields (notes, referral source, last contact)

## Output
- File: `D:\my_ai_projects\project_test_repos\sr_dev_test\research\002-buyer-types-matching.md`

## Validation (check ALL before completing)
- [ ] File exists at the output path
- [ ] At least 4 distinct buyer segments documented with situational context
- [ ] Matching criteria defined with specific field names and data types
- [ ] Ranking logic documented with numeric scoring weights
- [ ] Hard filters vs soft preferences clearly distinguished
- [ ] Messaging differentiation shown for at least 3 segments (same deal, different framing)
- [ ] Buyer list schema defined with required vs optional fields

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
