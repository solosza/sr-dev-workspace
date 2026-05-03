# Write Pattern Scanner Tests

## Type
BUILD

## Description
Unit tests for the pattern scanner — verify pattern matching logic.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\tests\test_pattern_scanner.py` with:
- `test_load_patterns` — verify all 22 patterns load from JSON
- `test_scan_clean_entity` — entity with no red flags returns empty match list
- `test_scan_suspicious_entity` — entity matching Feeding Our Future pattern returns matches
- `test_pattern_001_new_org_large_award` — org created within 12 months of award flags Pattern 1
- `test_pattern_002_no_990` — entity with no IRS filings flags Pattern 2
- `test_pattern_003_revenue_mismatch` — award >> prior revenue flags Pattern 3
- `test_pattern_006_same_address` — multiple orgs at same address flags Pattern 6
- `test_get_applicable_patterns_by_sector` — sector filter returns correct subset
- Use sample_entity_profile and sample_pattern_matches from conftest.py

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/tests/test_pattern_scanner.py`
- [ ] `grep -q "test_load_patterns" D:/my_ai_projects/fraud-detection-app/tests/test_pattern_scanner.py`
- [ ] `grep -q "test_scan_suspicious_entity" D:/my_ai_projects/fraud-detection-app/tests/test_pattern_scanner.py`
