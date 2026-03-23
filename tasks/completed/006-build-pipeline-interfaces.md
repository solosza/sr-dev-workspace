# Build Pipeline Interfaces

## Context
Foundation layer for the pipeline — data schemas and interaction patterns. Equivalent to ImageInterface in docker-spec. Everything else composes on top of these. All output goes into the creative-finance-spec repo.

## Dependencies
- **005** — repo must exist
- **001** — seller lead fields come from deal structure research
- **002** — buyer profile fields come from buyer types research
- **004** — Gmail and webhook patterns come from integration research

## Requirements

Read these research files before building:
- `creative-finance-spec/research/001-lease-option-structure.md`
- `creative-finance-spec/research/002-buyer-types-matching.md`
- `creative-finance-spec/research/004-integration-surface.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\interfaces\`

### schemas.json
Define all data schemas with field names, types, required/optional, and descriptions:
- **Seller Lead**: name, phone, email, property_address, city, state, zip, motivation, equity_estimate_pct, existing_loan_balance, monthly_payment, property_value_estimate, lead_source, timestamp, status, score, notes
- **Tenant-Buyer Profile**: name, phone, email, target_areas (array), min_bedrooms, max_price, max_monthly_payment, option_fee_budget, credit_score_current, credit_score_target, income_type (W2/1099), monthly_income, timeline_months, segment (from 002 research), referral_source, last_contact, notes
- **Deal**: property_address, city, state, zip, seller_lead_id, asking_price, estimated_value, monthly_payment, option_period_months, option_fee, assignment_fee_target, status (new/qualified/locked/matched/assigned/closed), matched_buyers (array), locked_date, notes
- **Session**: session_id, lead_id, lead_type (seller/buyer), created_at, last_interaction, interaction_count, status

### gmail_patterns.md
Reference patterns for Gmail operations via gws CLI (or alternative from 004 research):
- Search: find prior contact by email, find threads by subject
- Send: first-touch email, follow-up, disposition outreach
- Draft: create draft for HITL review before sending
- Thread: reply to existing thread vs new thread
- Include exact command syntax from 004 research

### webhook_schemas.md
Payload format reference for inbound lead data:
- Generic JSON (minimal: name, email, phone, property_address)
- Typeform webhook payload structure
- Zapier webhook payload structure
- Field mapping: how each source maps to the Seller Lead schema

## Output
- `creative-finance-spec/pipeline/interfaces/schemas.json`
- `creative-finance-spec/pipeline/interfaces/gmail_patterns.md`
- `creative-finance-spec/pipeline/interfaces/webhook_schemas.md`

## Validation (check ALL before completing)
- [ ] All 3 files exist at their output paths (Glob to confirm)
- [ ] schemas.json has all 4 schemas (seller_lead, tenant_buyer, deal, session)
- [ ] Every schema field has: name, type, required/optional flag
- [ ] Seller lead schema has all fields listed in requirements
- [ ] Tenant-buyer schema has all fields listed in requirements
- [ ] Deal schema has status enum with all values
- [ ] gmail_patterns.md covers search, send, draft, thread operations with syntax
- [ ] webhook_schemas.md has at least 3 payload formats with field mappings

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
