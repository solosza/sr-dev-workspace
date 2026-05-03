# Write Pattern Scanner

## Type
BUILD

## Description
Pattern scanner that applies all fraud patterns against an entity and returns match scores.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_scanner.py` with class `PatternScanner`:
- `__init__(self, patterns_path)` — load fraud_patterns.json
- `scan_entity(self, entity_data: dict) -> list[PatternMatch]` — run all patterns against entity data, return list of matches with scores
- `scan_award(self, award_data: dict, entity_data: dict) -> list[PatternMatch]` — run patterns against award + entity combo
- `get_applicable_patterns(self, sector: str) -> list` — filter patterns by sector
- `PatternMatch` pydantic model: pattern_id, pattern_name, matched (bool), confidence (0-100), evidence (str describing what triggered)
- Each pattern check is a method: `_check_pattern_001(entity)`, `_check_pattern_002(entity)`, etc.
- Patterns that need cross-referencing (e.g., same address) take additional context

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/patterns/pattern_scanner.py`
- [ ] `grep -q "class PatternScanner" D:/my_ai_projects/fraud-detection-app/src/patterns/pattern_scanner.py`
- [ ] `grep -q "scan_entity" D:/my_ai_projects/fraud-detection-app/src/patterns/pattern_scanner.py`
