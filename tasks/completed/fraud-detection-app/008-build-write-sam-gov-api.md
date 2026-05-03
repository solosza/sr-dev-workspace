# Write SAM.gov API Client

## Type
BUILD

## Description
API client for SAM.gov — entity registration, exclusion/debarment status.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\apis\sam_gov.py` with class `SAMGovClient(BaseAPIClient)`:
- `search_entity(self, name=None, uei=None, cage_code=None)` — search entity registrations
- `get_entity(self, uei)` — full entity record (registration date, address, POC, business type)
- `check_exclusion(self, name=None, uei=None)` — check if entity is excluded/debarred
- `get_exclusion_details(self, exclusion_id)` — exclusion record details
- Base URL: `https://api.sam.gov/`
- Requires API key (from config/settings.py env var SAM_GOV_API_KEY)
- Key data: registration_date, expiration_date, exclusion_status, physical_address, entity_type
- Returns pydantic models: `SAMEntity`, `SAMExclusion`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/apis/sam_gov.py`
- [ ] `grep -q "class SAMGovClient" D:/my_ai_projects/fraud-detection-app/src/apis/sam_gov.py`
