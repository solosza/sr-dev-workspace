# Write FinCEN Tip Generator

## Type
BUILD

## Description
Generate FinCEN-formatted whistleblower tip for cases with money laundering / sanctions angle.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\evidence\fincen_tip.py` with class `FinCENTipGenerator`:
- `__init__(self)` — initialize
- `generate(self, entity_profile, pattern_matches, evidence_records) -> str` — generate FinCEN tip markdown
- `qualifies_for_fincen(self, pattern_matches) -> bool` — check if case has FinCEN-eligible elements:
  - Money laundering (Pattern 4: funds via money services businesses)
  - Foreign transfers (Feeding Our Future → Somalia pattern)
  - Sanctions evasion (OFAC matches)
  - Foreign influence laundering (Pattern 20: Singham → Shanghai)
- Tip format: summary of suspected BSA/IEEPA violations, supporting evidence, entity details
- Output: `evidence-packages/[entity]/fincen-tip.md`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/fincen_tip.py`
- [ ] `grep -q "class FinCENTipGenerator" D:/my_ai_projects/fraud-detection-app/src/evidence/fincen_tip.py`
- [ ] `grep -q "qualifies_for_fincen" D:/my_ai_projects/fraud-detection-app/src/evidence/fincen_tip.py`
