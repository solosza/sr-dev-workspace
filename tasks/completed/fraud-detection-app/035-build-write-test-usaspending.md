# Write USASpending API Tests

## Type
BUILD

## Description
Unit tests for the USASpending API client — mock HTTP responses, test parsing.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\tests\test_usaspending.py` with:
- `test_search_awards_returns_list` — mock API response, verify list of Award objects returned
- `test_search_new_awards_filters_by_date` — verify date filtering works
- `test_get_award_detail_parses_correctly` — verify full award record parsing
- `test_get_recipient_parses_correctly` — verify recipient profile parsing
- `test_rate_limiting` — verify rate limiter pauses when limit exceeded
- `test_cache_hit` — verify cached response returned without API call
- `test_api_error_raises` — verify custom APIError on 4xx/5xx
- Use `unittest.mock.patch` to mock requests.get/post
- Use fixtures from conftest.py

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/tests/test_usaspending.py`
- [ ] `grep -q "test_search_awards" D:/my_ai_projects/fraud-detection-app/tests/test_usaspending.py`
- [ ] `grep -q "mock" D:/my_ai_projects/fraud-detection-app/tests/test_usaspending.py`
