# Write requirements.txt

## Type
BUILD

## Description
Write Python dependencies for the fraud detection app.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\requirements.txt` with:
- requests — HTTP client for all API calls
- beautifulsoup4 — HTML parsing for web scraping
- lxml — XML/HTML parser backend
- python-dateutil — date parsing for timelines
- hashlib is stdlib (no install needed) — SHA-256 evidence hashing
- pytest — testing
- pytest-asyncio — async test support
- aiohttp — async HTTP for batch API calls
- pydantic — data models for entities, patterns, evidence

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/requirements.txt`
- [ ] `grep -q "requests" D:/my_ai_projects/fraud-detection-app/requirements.txt`
- [ ] `grep -q "pydantic" D:/my_ai_projects/fraud-detection-app/requirements.txt`
