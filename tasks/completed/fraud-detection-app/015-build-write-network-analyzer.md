# Write Network Analyzer

## Type
BUILD

## Description
Cross-entity network analysis — detect shared addresses, shared officers, related-party transactions.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\entity\network_analyzer.py` with class `NetworkAnalyzer`:
- `__init__(self)` — initialize entity graph (dict-based, no external graph DB needed)
- `add_entity(self, profile: EntityProfile)` — add entity to the graph
- `find_shared_addresses(self) -> list[AddressCluster]` — entities at same address
- `find_shared_officers(self) -> list[OfficerCluster]` — officers serving multiple entities
- `find_related_parties(self, ein: str) -> list[EntityProfile]` — entities related via 990 Schedule R
- `get_network_map(self, entity_id: str) -> NetworkMap` — full network visualization data
- `NetworkMap` pydantic model: nodes (entities), edges (relationships with type: shared_address, shared_officer, related_party), clusters
- Geographic clustering: flag entities in same zip receiving separate awards for same program

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/entity/network_analyzer.py`
- [ ] `grep -q "class NetworkAnalyzer" D:/my_ai_projects/fraud-detection-app/src/entity/network_analyzer.py`
- [ ] `grep -q "find_shared_addresses" D:/my_ai_projects/fraud-detection-app/src/entity/network_analyzer.py`
