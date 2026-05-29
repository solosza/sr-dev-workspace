# Gate Contract — Govcon Research (Phase 1)

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/govcon-research/` | Create dir |
| DOC-01 | Legal viability doc exists | file_exists | `test -f projects/govcon-research/01-legal-viability.md` | Create file |
| DOC-02 | Legal doc covers FAR 52.219-14 | grep | `grep -q '52.219-14\|50%' projects/govcon-research/01-legal-viability.md` | Add content |
| DOC-03 | Economic viability doc exists | file_exists | `test -f projects/govcon-research/02-economic-viability.md` | Create file |
| DOC-04 | Practical viability doc exists | file_exists | `test -f projects/govcon-research/03-practical-viability.md` | Create file |
| DOC-05 | SAM.gov API doc exists | file_exists | `test -f projects/govcon-research/04-sam-gov-api.md` | Create file |
| DOC-06 | Research report exists | file_exists | `test -f projects/govcon-research/research-report.md` | Create file |
| DOC-07 | Report has go/no-go decision | grep | `grep -q 'Go/No-Go\|Decision\|Recommendation' projects/govcon-research/research-report.md` | Add decision |
