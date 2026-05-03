# Write Evidence Archiver

## Type
BUILD

## Description
Evidence preservation system — download, hash, timestamp, and archive all evidence at discovery time. Chain of custody for legal proceedings.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\evidence\evidence_archiver.py` with class `EvidenceArchiver`:
- `__init__(self, evidence_base_path)` — base path for evidence storage
- `archive_document(self, url, content, entity_id) -> EvidenceRecord` — save document locally with SHA-256 hash + timestamp
- `archive_webpage(self, url, entity_id) -> EvidenceRecord` — download HTML + take screenshot placeholder (Playwright integration point)
- `verify_integrity(self, evidence_record) -> bool` — re-hash and compare to stored hash
- `EvidenceRecord` pydantic model: url, retrieval_date (ISO 8601), sha256_hash, local_path, file_type, entity_id
- Storage structure: `evidence-packages/[entity-name]/attachments/[type]/[filename]`
- Source index: append every record to `evidence-packages/[entity-name]/source-index.md` with URL + date + hash
- All timestamps in UTC

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/evidence_archiver.py`
- [ ] `grep -q "class EvidenceArchiver" D:/my_ai_projects/fraud-detection-app/src/evidence/evidence_archiver.py`
- [ ] `grep -q "sha256" D:/my_ai_projects/fraud-detection-app/src/evidence/evidence_archiver.py`
