# Write Evidence Package Builder

## Type
BUILD

## Description
Generate the complete evidence package for a flagged entity — all files needed for attorney review and filing.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\evidence\package_builder.py` with class `EvidencePackageBuilder`:
- `__init__(self, evidence_base_path)` — base path
- `build_package(self, entity_profile, risk_score, pattern_matches, network_map) -> PackagePath` — generate all files
- Generated files per the evidence package format:
  - `summary.md` — executive summary: entity, fraud type, estimated amount, top patterns
  - `timeline.md` — chronological: formation date -> awards -> spending anomalies -> evidence
  - `financial-analysis.md` — 990 analysis, award vs spending, compensation ratios
  - `network-map.md` — connected entities, shared officers, same-address matches
  - `source-index.md` — every claim mapped to source URL + retrieval date
- Package directory: `evidence-packages/[entity-name-kebab]/`
- Each file uses markdown with sourced citations (URL + date for every claim)

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/package_builder.py`
- [ ] `grep -q "class EvidencePackageBuilder" D:/my_ai_projects/fraud-detection-app/src/evidence/package_builder.py`
- [ ] `grep -q "summary.md" D:/my_ai_projects/fraud-detection-app/src/evidence/package_builder.py`
