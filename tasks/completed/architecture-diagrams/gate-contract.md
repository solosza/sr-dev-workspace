# Gate Contract — Architecture Diagrams

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Diagrams directory exists | file_exists | `test -d docs/architecture-diagrams/` | Create dir |
| BUILD-02 | System architecture diagram exists | file_exists | `test -f docs/architecture-diagrams/system-architecture.md` | Create file |
| BUILD-03 | Enforcement loop diagram exists | file_exists | `test -f docs/architecture-diagrams/enforcement-loop.md` | Create file |
| BUILD-04 | Integration architecture diagram exists | file_exists | `test -f docs/architecture-diagrams/integration-architecture.md` | Create file |
| BUILD-05 | Use case scenario diagram exists | file_exists | `test -f docs/architecture-diagrams/use-case-scenario.md` | Create file |
| BUILD-06 | README index exists | file_exists | `test -f docs/architecture-diagrams/README.md` | Create file |
| FUNC-01 | System architecture has mermaid block | grep | `grep -q '```mermaid' docs/architecture-diagrams/system-architecture.md` | Add mermaid block |
| FUNC-02 | Enforcement loop has mermaid block | grep | `grep -q '```mermaid' docs/architecture-diagrams/enforcement-loop.md` | Add mermaid block |
| FUNC-03 | Integration has mermaid block | grep | `grep -q '```mermaid' docs/architecture-diagrams/integration-architecture.md` | Add mermaid block |
| FUNC-04 | Use case has mermaid block | grep | `grep -q '```mermaid' docs/architecture-diagrams/use-case-scenario.md` | Add mermaid block |
| FUNC-05 | System architecture shows domain specs | grep | `grep -q 'Domain Spec' docs/architecture-diagrams/system-architecture.md` | Add component |
| FUNC-06 | Enforcement loop shows hook triggers | grep | `grep -q 'Hook' docs/architecture-diagrams/enforcement-loop.md` | Add hook flow |
| FUNC-07 | Integration shows Playwright | grep | `grep -q 'Playwright' docs/architecture-diagrams/integration-architecture.md` | Add Playwright |
| FUNC-08 | README links all 4 diagrams | grep | `grep -c '\.md' docs/architecture-diagrams/README.md` returns >= 4 | Add links |

## Requirements Coverage
Each gate maps to a task acceptance criterion. All acceptance criteria have a corresponding gate.
