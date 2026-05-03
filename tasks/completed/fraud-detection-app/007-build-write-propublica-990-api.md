# Write ProPublica 990 API Client

## Type
BUILD

## Description
API client for ProPublica Nonprofit Explorer — IRS 990 filing data for 3M+ nonprofits.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\apis\propublica_990.py` with class `ProPublica990Client(BaseAPIClient)`:
- `search_org(self, name=None, ein=None)` — search by org name or EIN
- `get_org(self, ein)` — full org profile (name, EIN, NTEE code, revenue, assets, filing history)
- `get_filing(self, ein, tax_period)` — specific 990 filing details
- `get_filings_list(self, ein)` — all available filings for an org
- Base URL: `https://projects.propublica.org/nonprofits/api/v2/`
- Key data: total revenue, total expenses, officer compensation, program expenses, formation year
- Returns pydantic models: `NonprofitOrg`, `Filing990`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/apis/propublica_990.py`
- [ ] `grep -q "class ProPublica990Client" D:/my_ai_projects/fraud-detection-app/src/apis/propublica_990.py`
