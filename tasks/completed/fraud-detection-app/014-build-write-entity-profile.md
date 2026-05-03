# Write Entity Profile

## Type
BUILD

## Description
Entity profile builder that aggregates data from multiple sources into a unified entity view.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\entity\entity_profile.py` with class `EntityProfileBuilder`:
- `__init__(self, api_clients: dict)` — takes dict of API client instances
- `build_profile(self, entity_name: str, ein: str = None, uei: str = None) -> EntityProfile` — aggregate from all sources
- `EntityProfile` pydantic model with sections:
  - `identity`: name, EIN, UEI, address, state_of_incorporation, formation_date, entity_type
  - `financial`: total_revenue, total_expenses, officer_compensation, program_spending (from 990)
  - `awards`: list of federal awards (amount, program, date) from USASpending
  - `registration`: SAM.gov registration date, expiration, exclusion status
  - `officers`: list of officers/directors (from 990 + state records)
  - `flags`: list of red flags identified (anomalies before pattern scoring)
- `enrich_profile(self, profile, additional_data)` — add OSINT/PACER data later

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/entity/entity_profile.py`
- [ ] `grep -q "class EntityProfile" D:/my_ai_projects/fraud-detection-app/src/entity/entity_profile.py`
- [ ] `grep -q "class EntityProfileBuilder" D:/my_ai_projects/fraud-detection-app/src/entity/entity_profile.py`
