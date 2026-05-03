# Write Disclosure Statement Generator

## Type
BUILD

## Description
Generate qui tam disclosure statement — the critical legal document for False Claims Act filing.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\evidence\disclosure_statement.py` with class `DisclosureStatementGenerator`:
- `__init__(self)` — initialize templates
- `generate(self, entity_profile, risk_score, pattern_matches, evidence_records) -> str` — generate full disclosure statement markdown
- Disclosure statement must cover all required elements (per reporting-channels.md):
  - **Falsity** — specific false claims submitted to government
  - **Knowledge** — evidence defendant knew claims were false
  - **Materiality** — government relied on false claims in making payment
  - **Who** — specific defendants (names, roles, entities)
  - **What** — specific false claims (award numbers, amounts)
  - **When** — timeline of fraudulent activity
  - **Where** — jurisdiction (federal district)
  - **How much** — quantified damages + treble damage calculation
  - **Witnesses** — people with knowledge (from OSINT)
  - **Supporting docs** — list of all archived evidence with hashes
- Output: `evidence-packages/[entity]/disclosure-statement.md`

Read `D:\my_ai_projects\project_test_repos\sr_dev_workspace\docs\backlog\025-domain-build-government-spending-tracker\reporting-channels.md` for the full disclosure statement requirements.

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/evidence/disclosure_statement.py`
- [ ] `grep -q "class DisclosureStatementGenerator" D:/my_ai_projects/fraud-detection-app/src/evidence/disclosure_statement.py`
- [ ] `grep -q "Falsity" D:/my_ai_projects/fraud-detection-app/src/evidence/disclosure_statement.py`
