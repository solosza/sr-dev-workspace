# Write Layer 5 — Network Analysis

## Type
BUILD

## Description
Layer 5: Cross-entity network analysis — connect the dots between entities via shared addresses, officers, and transactions.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer5_network.py` with class `NetworkAnalysisLayer`:
- `__init__(self, network_analyzer: NetworkAnalyzer)` — takes analyzer instance
- `analyze_entity_network(self, entity_profile: EntityProfile, all_profiles: list) -> NetworkReport` — run full network analysis
- `NetworkReport` model: shared_address_entities (list), shared_officers (list), related_parties (list), geographic_cluster (bool), network_risk_multiplier (float 1.0-3.0)
- Risk multiplier logic:
  - Shared address with other flagged entities: 1.5x
  - Shared officers across 3+ entities: 2.0x
  - Both: 3.0x
- Network risk multiplier gets applied to the risk score by the pipeline runner

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer5_network.py`
- [ ] `grep -q "class NetworkAnalysisLayer" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer5_network.py`
