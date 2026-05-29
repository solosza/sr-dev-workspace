# Gate Contract — AI Business Formation

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/ai-business-formation/` | Create dir |
| DOC-01 | LLC research file exists | file_exists | `test -f projects/ai-business-formation/01-llc-formation.md` | Create file |
| DOC-02 | Multi-stream file exists | file_exists | `test -f projects/ai-business-formation/02-multi-stream-structure.md` | Create file |
| DOC-03 | Tax advantages file exists | file_exists | `test -f projects/ai-business-formation/03-tax-advantages.md` | Create file |
| DOC-04 | SAM.gov requirements file exists | file_exists | `test -f projects/ai-business-formation/04-sam-gov-requirements.md` | Create file |
| DOC-05 | AI business models file exists | file_exists | `test -f projects/ai-business-formation/05-ai-business-models.md` | Create file |
| DOC-06 | Final report exists | file_exists | `test -f projects/ai-business-formation/06-final-report.md` | Create file |
| DOC-07 | Final report has decision | grep | `grep -q 'Decision\|Recommendation\|Go/No-Go' projects/ai-business-formation/06-final-report.md` | Add decision |

## Requirements Coverage
Each gate maps to a task acceptance criterion. All acceptance criteria must have a corresponding gate.
