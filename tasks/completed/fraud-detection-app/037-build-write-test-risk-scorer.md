# Write Risk Scorer Tests

## Type
BUILD

## Description
Unit tests for the risk scoring engine.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\tests\test_risk_scorer.py` with:
- `test_low_risk_entity` — entity with 1 low-severity match scores LOW
- `test_medium_risk_entity` — entity with 2-3 medium matches scores MEDIUM
- `test_high_risk_entity` — entity with multiple HIGH matches scores HIGH
- `test_score_caps_at_100` — verify score never exceeds 100
- `test_confidence_weighting` — low confidence reduces pattern contribution
- `test_escalation_bonus` — multiple HIGH patterns get +10 bonus
- `test_explain_score` — verify human-readable explanation includes top patterns
- Use sample_pattern_matches from conftest.py

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/tests/test_risk_scorer.py`
- [ ] `grep -q "test_low_risk_entity" D:/my_ai_projects/fraud-detection-app/tests/test_risk_scorer.py`
- [ ] `grep -q "test_high_risk_entity" D:/my_ai_projects/fraud-detection-app/tests/test_risk_scorer.py`
