# Write Layer 4 — OSINT

## Type
BUILD

## Description
Layer 4: Open source intelligence — PACER court records, OFAC sanctions, OpenCorporates officer cross-referencing.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer4_osint.py` with class `OSINTInvestigator`:
- `__init__(self, ofac_client)` — takes API clients
- `investigate_officers(self, officers: list) -> list[OfficerReport]` — check each officer against sanctions, court records
- `check_ofac(self, name) -> OFACResult` — check name against OFAC SDN list
- `check_prior_fraud(self, name) -> list[CourtRecord]` — placeholder for PACER integration (log that PACER requires manual lookup at $0.10/page)
- `check_multiple_entities(self, officer_name) -> list[str]` — does this officer appear in multiple grant-receiving entities?
- `OfficerReport` model: name, ofac_match (bool), ofac_score, prior_cases (list), other_entities (list)
- `OFACResult` model: matched (bool), score (0-100), sdn_entry (SDNEntry or None)

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer4_osint.py`
- [ ] `grep -q "class OSINTInvestigator" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer4_osint.py`
