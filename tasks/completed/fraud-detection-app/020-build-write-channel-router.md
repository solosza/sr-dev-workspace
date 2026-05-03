# Write Channel Router

## Type
BUILD

## Description
Route each case to the appropriate filing channel(s): qui tam, FinCEN, Treasury OIG, or multiple.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\evidence\channel_router.py` with class `ChannelRouter`:
- `__init__(self)` — initialize routing rules
- `route(self, entity_profile, pattern_matches, risk_score) -> list[ChannelDecision]` — determine applicable channels
- `ChannelDecision` pydantic model: channel ("qui_tam"|"fincen"|"treasury_oig"|"gao"), applicable (bool), reason (str), priority (int)
- Routing logic:
  - False claims to government? → qui_tam (always primary)
  - Money laundering, foreign transfers, sanctions? → fincen (complementary)
  - Both? → file both
  - Below qui tam threshold but still fraud? → treasury_oig / gao
  - Systemic issues (audit gaps)? → gao
- `generate_filing_plan(self, decisions) -> str` — markdown summary of which channels to file with and in what order

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/channel_router.py`
- [ ] `grep -q "class ChannelRouter" D:/my_ai_projects/fraud-detection-app/src/evidence/channel_router.py`
