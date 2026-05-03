# Write Materiality Filter

## Type
BUILD

## Description
3-tier filter that routes entities based on risk score: LOW (log only), MEDIUM (queue for human review), HIGH (auto-generate evidence package).

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\scoring\materiality_filter.py` with class `MaterialityFilter`:
- `__init__(self, thresholds: dict)` — load from settings
- `route(self, risk_score: RiskScore) -> FilterDecision` — determine action based on score tier
- `FilterDecision` pydantic model: action ("log"|"review"|"evidence_package"), reason (str), priority (int 1-10)
- `log_decision(self, entity_id, decision)` — append to data/filter_log.jsonl
- Feedback loop method: `record_rejection(self, entity_id, reason)` — attorney rejection feeds back into future scoring

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/scoring/materiality_filter.py`
- [ ] `grep -q "class MaterialityFilter" D:/my_ai_projects/fraud-detection-app/src/scoring/materiality_filter.py`
