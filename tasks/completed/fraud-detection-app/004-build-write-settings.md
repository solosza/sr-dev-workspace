# Write Settings Configuration

## Type
BUILD

## Description
Write the central configuration file for API endpoints, rate limits, and focus sectors.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\config\settings.py` with:
- API base URLs: USASpending (api.usaspending.gov), ProPublica Nonprofit Explorer, SAM.gov, OFAC SDN
- Rate limit settings per API (requests per minute)
- Focus sectors list (Phase 1: homeless services NTEE codes L/P, Phase 2: healthcare, Phase 3: COVID relief, Phase 4: political nonprofits 501c4)
- Scoring thresholds: LOW (<30), MEDIUM (30-70), HIGH (>70)
- Evidence paths: evidence-packages/, data/cache/
- All sensitive values (API keys) read from environment variables with `os.environ.get()`
- Create `D:\my_ai_projects\fraud-detection-app\config\__init__.py`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/config/settings.py`
- [ ] `grep -q "USASpending" D:/my_ai_projects/fraud-detection-app/config/settings.py`
- [ ] `grep -q "os.environ" D:/my_ai_projects/fraud-detection-app/config/settings.py`
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/config/__init__.py`
