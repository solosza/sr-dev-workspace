# Write Risk Scorer

## Type
BUILD

## Description
Composite risk scoring engine that aggregates pattern matches into a single risk score.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\scoring\risk_scorer.py` with class `RiskScorer`:
- `__init__(self, thresholds: dict)` — load scoring thresholds from settings (LOW <30, MEDIUM 30-70, HIGH >70)
- `score_entity(self, pattern_matches: list[PatternMatch]) -> RiskScore` — compute composite score
- `RiskScore` pydantic model: total_score (0-100), tier ("LOW"|"MEDIUM"|"HIGH"), pattern_count, top_patterns (list), estimated_fraud_amount (if calculable)
- Scoring logic:
  - Each pattern match contributes points based on pattern severity (HIGH=20, MEDIUM=10, LOW=5)
  - Confidence weighting: score *= (confidence/100)
  - Cap at 100
  - Multiple HIGH patterns = escalation bonus (+10)
- `explain_score(self, risk_score: RiskScore) -> str` — human-readable explanation of why entity scored this way

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/scoring/risk_scorer.py`
- [ ] `grep -q "class RiskScorer" D:/my_ai_projects/fraud-detection-app/src/scoring/risk_scorer.py`
- [ ] `grep -q "class RiskScore" D:/my_ai_projects/fraud-detection-app/src/scoring/risk_scorer.py`
