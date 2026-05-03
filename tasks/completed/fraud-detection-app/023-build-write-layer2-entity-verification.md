# Write Layer 2 — Entity Verification

## Type
BUILD

## Description
Layer 2: Cross-reference award recipients against IRS 990, SAM.gov, and state incorporation records.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer2_entity_verification.py` with class `EntityVerification`:
- `__init__(self, propublica_client, sam_client)` — takes API clients
- `verify_entity(self, award: Award) -> EntityProfile` — build entity profile from multiple sources
- `check_990_exists(self, entity_name, ein) -> bool` — does this entity have IRS 990 filings?
- `check_revenue_mismatch(self, entity_profile) -> bool` — is award amount >> prior revenue?
- `check_registration_age(self, entity_profile, award_date) -> bool` — was entity created shortly before award?
- `check_sam_exclusion(self, entity_profile) -> bool` — is entity excluded/debarred?
- Each check returns a flag that gets added to entity_profile.flags

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer2_entity_verification.py`
- [ ] `grep -q "class EntityVerification" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer2_entity_verification.py`
