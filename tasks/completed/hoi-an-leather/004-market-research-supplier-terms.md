# Research: Supplier Formalization — Spec Sheet, Pricing Tiers, Outreach Template

## Context
Research how to formalize the supplier relationship with the Da Nang family workshop. Produce a spec sheet template, pricing tier structure, payment method guidance, and WhatsApp outreach message.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-leather/` directory exists

## Requirements
- Research what a leather bag spec sheet includes (dimensions, hardware, zipper brand, stitching, color, lining, weight)
- Research pricing tier norms for small batch leather imports (10/25/50 units)
- Research payment methods Vietnamese family workshops accept for international B2B orders
- Research realistic lead times for 25-unit batch vs 1-off custom
- Research whether Da Nang workshops typically ship DHL/FedEx or need a freight forwarder
- Produce: spec sheet template (fillable, all required fields)
- Produce: pricing tier table to propose (10/25/50 unit columns)
- Produce: WhatsApp outreach message template (warm, references the trip, proposes next steps)
- Write all to `projects/hoi-an-leather/supplier-terms.md`

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/supplier-terms.md` exists
- [ ] Contains spec sheet template with at least 6 fields
- [ ] Contains pricing tier table with 10/25/50 unit columns
- [ ] Contains WhatsApp outreach message template
- [ ] Contains payment method section

## Gates Satisfied
- BUILD-04, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
