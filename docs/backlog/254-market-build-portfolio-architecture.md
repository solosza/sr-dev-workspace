# Portfolio Site - High-Level Architecture

## Status
Open

## Priority
Medium - hiring-manager validation section

## Summary
Build guide section 6: four public concepts (structured intent, domain-aware workflow, governed execution, independent validation/review), conceptual flow diagram, short engineering principles.

## Requirements
- Conceptual flow: Intent to Structured specification to Domain-aware execution to Validation evidence to Reviewable artifact
- Principles: externalized state, bounded work, tool-aware controls, explicit gates
- Avoid: raw state diagrams, enforcement paths, internal command/hook names, orchestration sequences

## References
- Format guide: `projects/portfolio-site/format-guide-v1.2.md` (workspace copy of GitHub_Portfolio_Format_Guide_v1.2.md)
- Sibling portfolio backlogs 250-261 (build in numeric order; 250 first, 261 last)

## Task Builder Input
- **Deliverable:** Architecture section live on the deployed page
- **Location:** new-repo:D:\my_ai_projects\portfolio-site
- **Scope:** BUILD
- **Constraints:** IP-safe disclosure checklist (guide section 13) governs ALL copy: never publish state schemas, hook logic/names, gate rules, command protocols, meta-factory internals, or full domain contracts. NO absolute claims ('100%', 'guaranteed', 'unbypassable', 'zero drift'). NO invented metrics - [INSERT] placeholders remain until the user supplies verified numbers; never ship a page presenting unfilled placeholders as final copy. Depends on backlog 250 scaffold. Single static page (guide section 14).
