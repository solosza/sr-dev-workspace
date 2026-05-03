# Write USASpending.gov API Client

## Type
BUILD

## Description
API client for USASpending.gov — the primary data source for federal awards.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\apis\usaspending.py` with class `USASpendingClient(BaseAPIClient)`:
- `search_awards(self, filters, page=1, limit=100)` — search awards by filters (recipient name, date range, award type, CFDA program)
- `get_award_detail(self, award_id)` — full award record
- `get_recipient(self, recipient_id)` — recipient profile (name, address, DUNS/UEI, parent org)
- `get_subawards(self, award_id)` — subaward recipients under a prime award
- `search_new_awards(self, since_date)` — awards published since date (for daily scanning)
- Base URL: `https://api.usaspending.gov/api/v2/`
- Key endpoints: `/search/spending_by_award/`, `/awards/{id}/`, `/recipient/{id}/`, `/subawards/`
- Uses POST for search (USASpending API uses POST with JSON body for searches)
- Returns pydantic models: `Award`, `Recipient`, `SubAward`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/apis/usaspending.py`
- [ ] `grep -q "class USASpendingClient" D:/my_ai_projects/fraud-detection-app/src/apis/usaspending.py`
- [ ] `grep -q "search_new_awards" D:/my_ai_projects/fraud-detection-app/src/apis/usaspending.py`
