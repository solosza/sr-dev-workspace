# Gate Contract — Pulsia Design Patterns

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | 07-command-skill-pattern.md exists | file_exists | `test -f projects/pulsia-research/07-command-skill-pattern.md` | Create file |
| BUILD-02 | 08-tiered-index-architecture.md exists | file_exists | `test -f projects/pulsia-research/08-tiered-index-architecture.md` | Create file |
| BUILD-03 | 09-loop-architecture.md exists | file_exists | `test -f projects/pulsia-research/09-loop-architecture.md` | Create file |
| BUILD-04 | README.md lists all 9 deliverables | grep | `grep -q '09-loop-architecture' projects/pulsia-research/README.md` | Update README |
| BUILD-05 | research-report.md has design patterns section | grep | `grep -q 'Design Patterns' projects/pulsia-research/research-report.md` | Update report |
| DOC-01 | 07 references command-skill-pattern source | grep | `grep -q 'command-skill-pattern' projects/pulsia-research/07-command-skill-pattern.md` | Add source reference |
| DOC-02 | 08 references tiered-index-architecture source | grep | `grep -q 'tiered-index-architecture' projects/pulsia-research/08-tiered-index-architecture.md` | Add source reference |
| DOC-03 | 09 references loop-architecture source | grep | `grep -q 'loop-architecture' projects/pulsia-research/09-loop-architecture.md` | Add source reference |
| DOC-04 | 07 cross-references 04-architectural-blueprint | grep | `grep -q '04-architectural-blueprint' projects/pulsia-research/07-command-skill-pattern.md` | Add cross-reference |
| DOC-05 | 08 cross-references 04-architectural-blueprint | grep | `grep -q '04-architectural-blueprint' projects/pulsia-research/08-tiered-index-architecture.md` | Add cross-reference |
| DOC-06 | 09 cross-references 04-architectural-blueprint | grep | `grep -q '04-architectural-blueprint' projects/pulsia-research/09-loop-architecture.md` | Add cross-reference |
| DOC-07 | 07 has synthesis content (not just copy) | grep | `grep -q 'Pulsia' projects/pulsia-research/07-command-skill-pattern.md` | Add synthesis |
| DOC-08 | 08 has synthesis content (not just copy) | grep | `grep -q 'Pulsia' projects/pulsia-research/08-tiered-index-architecture.md` | Add synthesis |
| DOC-09 | 09 has synthesis content (not just copy) | grep | `grep -q 'Pulsia' projects/pulsia-research/09-loop-architecture.md` | Add synthesis |
| DOC-10 | 07 has 6-layer architecture section | grep | `grep -q 'Layer' projects/pulsia-research/07-command-skill-pattern.md` | Add layers section |
| DOC-11 | 08 has three-layer architecture section | grep | `grep -q 'Layer' projects/pulsia-research/08-tiered-index-architecture.md` | Add layers section |
| DOC-12 | 09 has loop primitive section | grep | `grep -q 'loop' projects/pulsia-research/09-loop-architecture.md` | Add loop primitive section |

## Requirements Coverage

Each gate maps to a task acceptance criterion:
- BUILD-01 through BUILD-03: Tasks 001-003 (file creation)
- BUILD-04, BUILD-05: Tasks 004-005 (updates)
- DOC-01 through DOC-12: Tasks 001-003 (content quality)
