# Gate Contract — Pulsia Market Research

## Verification Methods
- **file_exists** — structural check that a file exists at a specific path
- **grep** — content verification that key terms appear in a document
- **manual** — semantic review by LLM for quality and completeness

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|----|--------|----|----|
| STRUCT-01 | Project dir exists | file_exists | `test -d projects/pulsia-research` | Create dir |
| RESEARCH-01 | Company overview | file_exists | `test -f projects/pulsia-research/01-company-overview.md` | Write file |
| RESEARCH-02 | Architecture docs | file_exists | `test -f projects/pulsia-research/02-architecture.md` | Write file |
| RESEARCH-03 | Harness applicability | file_exists | `test -f projects/pulsia-research/03-harness-applicability.md` | Write file |
| RESEARCH-04 | Blueprint | file_exists | `test -f projects/pulsia-research/04-architectural-blueprint.md` | Write file |
| RESEARCH-05 | Scalability assessment | file_exists | `test -f projects/pulsia-research/05-scalability-assessment.md` | Write file |
| RESEARCH-06 | Comparison analysis | file_exists | `test -f projects/pulsia-research/06-comparison-analysis.md` | Write file |
| DOC-01 | Blueprint includes specs | grep | `grep -qi 'yaml\|json\|loop' projects/pulsia-research/04-architectural-blueprint.md` | Add loop specs |
| DOC-02 | Final report | file_exists | `test -f projects/pulsia-research/research-report.md` | Write file |
| DOC-03 | Report has TOC | grep | `grep -q '##' projects/pulsia-research/research-report.md` | Add sections |
| SEMANTIC-01 | Content quality | manual | All 7 research sections properly consolidated and coherent | Revise content |
| SEMANTIC-02 | Loop specs complete | manual | All 5+ proposed harness loops have detailed specifications | Add specs |

## Requirements Coverage
Each gate maps to a task acceptance criterion. All acceptance criteria have corresponding gates.
