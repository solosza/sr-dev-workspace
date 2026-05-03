# Write API Base Client

## Type
BUILD

## Description
Write the base HTTP client class that all API clients inherit from. Handles rate limiting, retries, caching, and error handling.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\apis\base_client.py` with:
- `BaseAPIClient` class with:
  - `__init__(self, base_url, rate_limit_rpm)` — sets base URL and rate limit
  - `get(self, endpoint, params)` — GET with rate limiting, retries (3x with exponential backoff), timeout (30s)
  - `_check_cache(self, url)` — check data/cache/ for cached response (cache TTL: 24h)
  - `_save_cache(self, url, response)` — save response to cache with timestamp
  - `_rate_limit(self)` — sleep if requests exceed RPM limit
- Uses `requests` library
- Logging via Python logging module
- All responses return dict (parsed JSON) or raise custom `APIError`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/apis/base_client.py`
- [ ] `grep -q "class BaseAPIClient" D:/my_ai_projects/fraud-detection-app/src/apis/base_client.py`
- [ ] `grep -q "rate_limit" D:/my_ai_projects/fraud-detection-app/src/apis/base_client.py`
