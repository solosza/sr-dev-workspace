# Write Layer 1 — Awards Ingest

## Type
BUILD

## Description
Layer 1: Daily ingestion of new federal awards from USASpending.gov API.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer1_awards_ingest.py` with class `AwardsIngest`:
- `__init__(self, usaspending_client, focus_sectors)` — takes API client and sector filter
- `ingest_new_awards(self, since_date=None) -> list[Award]` — pull new awards since date (default: yesterday)
- `filter_by_sector(self, awards, sectors) -> list[Award]` — filter to focus sectors (NTEE codes)
- `save_awards(self, awards, output_path)` — save to data/awards/YYYY-MM-DD.jsonl
- `get_last_ingest_date(self) -> date` — read from data/ingest_state.json
- `update_ingest_state(self, date)` — write last successful ingest date
- Focus sectors from settings: Phase 1 = homeless services (NTEE L, P), Phase 2 = healthcare, etc.

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer1_awards_ingest.py`
- [ ] `grep -q "class AwardsIngest" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer1_awards_ingest.py`
