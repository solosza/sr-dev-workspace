# Write Layer 6 — Case Builder

## Type
BUILD

## Description
Layer 6: Build the case — assemble evidence package, generate disclosure statement, route to filing channels.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer6_case_builder.py` with class `CaseBuilder`:
- `__init__(self, package_builder, disclosure_generator, fincen_generator, channel_router, evidence_archiver)`
- `build_case(self, entity_profile, risk_score, pattern_matches, network_report) -> CasePackage` — orchestrate full case assembly
- Steps:
  1. Archive all evidence (evidence_archiver)
  2. Build evidence package (package_builder)
  3. Generate disclosure statement (disclosure_generator)
  4. Check FinCEN eligibility and generate tip if applicable (fincen_generator)
  5. Route to filing channels (channel_router)
  6. Generate filing plan
- `CasePackage` model: entity_id, package_path, channels (list), estimated_fraud_amount, trebled_damages, estimated_reward_range, filing_plan (str)
- Alert: write case summary to `data/alerts/YYYY-MM-DD/[entity].md` for team notification

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer6_case_builder.py`
- [ ] `grep -q "class CaseBuilder" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer6_case_builder.py`
- [ ] `grep -q "build_case" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer6_case_builder.py`
