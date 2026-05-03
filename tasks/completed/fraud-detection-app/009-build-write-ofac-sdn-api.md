# Write OFAC SDN List Client

## Type
BUILD

## Description
Client for OFAC Specially Designated Nationals list — sanctioned entities cross-reference.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\apis\ofac_sdn.py` with class `OFACSDNClient(BaseAPIClient)`:
- `search_sdn(self, name=None, type=None)` — search SDN list by name or entity type
- `check_name(self, name)` — fuzzy match a name against the SDN list (returns match score)
- `download_sdn_list(self)` — download full SDN XML/CSV for local searching
- `load_local_sdn(self)` — load cached SDN list for offline matching
- Base URL: `https://sanctionssearch.ofac.treas.gov/`
- Also support: `https://www.treasury.gov/ofac/downloads/sdn.xml` for bulk download
- Returns pydantic models: `SDNEntry` with fields: name, type, program, aliases, addresses

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/apis/ofac_sdn.py`
- [ ] `grep -q "class OFACSDNClient" D:/my_ai_projects/fraud-detection-app/src/apis/ofac_sdn.py`
