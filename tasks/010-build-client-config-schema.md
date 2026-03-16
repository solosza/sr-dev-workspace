# Build Client Config Schema

## Context
The thin layer that personalizes the domain spec per investor. Not knowledge — identity. Takes 10 minutes to fill out during onboarding. All output goes into the creative-finance-spec repo.

## Dependencies
- **006** — schemas (config references field names from seller lead, tenant-buyer, and deal schemas)
- **007** — seller pipeline (deal thresholds reference qualification criteria)
- **008** — buyer pipeline (buyer list import maps to tenant-buyer schema)

## Requirements

Read these files before building:
- `creative-finance-spec/pipeline/interfaces/schemas.json`
- `creative-finance-spec/pipeline/seller/qualification.md`
- `creative-finance-spec/pipeline/buyer/list_management.md`

Build into: `D:\my_ai_projects\project_test_repos\specs\creative-finance-spec\pipeline\config\`

### schema.md
Define the client configuration schema. Keep it to **15 or fewer required fields**:

**Identity (required):**
- `investor_name` (string) — their name for email signatures
- `business_name` (string) — company name
- `email` (string) — their Gmail address (system sends from this)
- `phone` (string) — for calendar events and email signatures

**Market (required):**
- `target_markets` (array of strings) — cities/regions they operate in
- `preferred_structures` (array of enum) — ["lease_option"] for MVP, extensible to ["sub_to", "seller_finance"] later

**Deal thresholds (required):**
- `min_equity_pct` (number) — minimum seller equity % to qualify
- `max_purchase_price` (number) — ceiling for deals
- `min_monthly_spread` (number) — minimum monthly $ difference between what seller accepts and what buyer pays
- `min_assignment_fee` (number) — won't do a deal below this

**Communication (required):**
- `tone` (enum) — "professional" / "casual" / "direct"
- `email_signature` (string) — appended to all outgoing emails

**HITL preferences (required with defaults):**
- `auto_send_first_touch` (boolean, default: false) — if false, all first touches go as draft
- `auto_send_threshold` (number, default: 80) — score above which auto-send is allowed (if auto_send_first_touch is true)
- `auto_disposition` (boolean, default: false) — if false, disposition emails go as draft

**Optional fields:**
- `calendar_link` (string) — Calendly or similar for self-scheduling
- `crm_webhook_url` (string) — webhook to push updates back to their CRM
- `excluded_zips` (array of strings) — zip codes to never operate in
- `max_option_period_months` (number) — longest option period they'll accept

### sample_config.json
Realistic example for a Phoenix-area lease option wholesaler.

### buyer_import_template.csv
CSV template with headers mapped to tenant-buyer schema:
`name,email,phone,target_areas,min_bedrooms,max_price,max_monthly_payment,option_fee_budget,credit_score_current,timeline_months,notes`

## Output
- `creative-finance-spec/pipeline/config/schema.md`
- `creative-finance-spec/pipeline/config/sample_config.json`
- `creative-finance-spec/pipeline/config/buyer_import_template.csv`

## Validation (check ALL before completing)
- [ ] All 3 files exist at their output paths
- [ ] schema.md has 15 or fewer required fields
- [ ] Every field has: name, type, required/optional flag, description, default (if applicable)
- [ ] HITL preferences have sensible defaults (conservative = draft mode)
- [ ] sample_config.json is valid JSON with realistic values
- [ ] buyer_import_template.csv headers match tenant-buyer schema field names from 006
- [ ] No sensitive fields in the config that shouldn't be stored in plain text

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
