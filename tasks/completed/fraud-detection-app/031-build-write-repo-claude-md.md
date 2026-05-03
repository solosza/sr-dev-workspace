# Write CLAUDE.md for Fraud Detection Repo

## Type
BUILD

## Description
Write the CLAUDE.md that governs agent behavior in the fraud-detection-app repo.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\CLAUDE.md` with:
- Project identity: "Fraud Detection App — AI-powered government spending analyzer"
- Key directories: src/ (source), tests/, config/, evidence-packages/, data/, research/
- Python conventions: pydantic models for all data structures, type hints, logging via Python logging
- API client pattern: all clients inherit from BaseAPIClient
- Pipeline architecture: 7 layers (0-6), each in src/pipeline/
- Evidence rules: SHA-256 hash all evidence, timestamp in UTC, never delete evidence
- Testing: pytest, mock external APIs in tests
- Legal warning: evidence packages are for attorney review only — never share case details without counsel

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/CLAUDE.md`
- [ ] `grep -q "Fraud Detection" D:/my_ai_projects/fraud-detection-app/CLAUDE.md`
- [ ] `grep -q "BaseAPIClient" D:/my_ai_projects/fraud-detection-app/CLAUDE.md`
