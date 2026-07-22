# Portfolio Site - Engineering Decisions and Trade-offs

## Status
Open

## Priority
Medium - the table hiring managers validate against

## Summary
Build guide section 10: the five-row decision/reason/trade-off table exactly as structured in the guide (persist state outside chat, bounded work units, mechanical vs semantic checks, controlled integration, domain adaptation).

## Requirements
- Responsive table styling per section 14
- Avoid: internal enforcement implementation, universal-optimality claims

## References
- Format guide: `projects/portfolio-site/format-guide-v1.2.md` (workspace copy of GitHub_Portfolio_Format_Guide_v1.2.md)
- Sibling portfolio backlogs 250-261 (build in numeric order; 250 first, 261 last)

## Task Builder Input
- **Deliverable:** Decisions table section live on the deployed page
- **Location:** new-repo:D:\my_ai_projects\portfolio-site
- **Scope:** BUILD
- **Constraints:** IP-safe disclosure checklist (guide section 13) governs ALL copy: never publish state schemas, hook logic/names, gate rules, command protocols, meta-factory internals, or full domain contracts. NO absolute claims ('100%', 'guaranteed', 'unbypassable', 'zero drift'). NO invented metrics - [INSERT] placeholders remain until the user supplies verified numbers; never ship a page presenting unfilled placeholders as final copy. Depends on backlog 250 scaffold. Single static page (guide section 14).
