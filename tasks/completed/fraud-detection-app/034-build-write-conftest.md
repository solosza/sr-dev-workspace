# Write Test Conftest

## Type
BUILD

## Description
Write pytest conftest.py with shared fixtures for testing — mock API responses, sample entities.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\tests\conftest.py` with:
- `mock_usaspending_response` fixture — sample award JSON matching USASpending API format
- `mock_990_response` fixture — sample ProPublica 990 response
- `mock_sam_response` fixture — sample SAM.gov entity response
- `sample_entity_profile` fixture — pre-built EntityProfile for testing scoring/patterns
- `sample_pattern_matches` fixture — list of PatternMatch objects for testing
- `fraud_patterns_path` fixture — path to fraud_patterns.json
- All fixtures use realistic data based on the Feeding Our Future case pattern (known fraud case for test validation)
- Use `@pytest.fixture` decorator, scope="session" for expensive fixtures

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/tests/conftest.py`
- [ ] `grep -q "mock_usaspending_response" D:/my_ai_projects/fraud-detection-app/tests/conftest.py`
- [ ] `grep -q "@pytest.fixture" D:/my_ai_projects/fraud-detection-app/tests/conftest.py`
