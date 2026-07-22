# Portfolio Site - Current Limitations

## Status
Open

## Priority
Medium - credibility through honest scope

## Summary
Build guide section 11: public-safe limitations (executor dependence, incomplete external benchmarking, model-assisted semantic review, concurrency hardening) plus a short current-work list.

## Requirements
- Use guide sample copy tone: factual, not apologetic
- Avoid: security-sensitive weaknesses, calling planned features completed

## References
- Format guide: `projects/portfolio-site/format-guide-v1.2.md` (workspace copy of GitHub_Portfolio_Format_Guide_v1.2.md)
- Sibling portfolio backlogs 250-261 (build in numeric order; 250 first, 261 last)

## Task Builder Input
- **Deliverable:** Limitations section live on the deployed page
- **Location:** new-repo:D:\my_ai_projects\portfolio-site
- **Scope:** BUILD
- **Constraints:** IP-safe disclosure checklist (guide section 13) governs ALL copy: never publish state schemas, hook logic/names, gate rules, command protocols, meta-factory internals, or full domain contracts. NO absolute claims ('100%', 'guaranteed', 'unbypassable', 'zero drift'). NO invented metrics - [INSERT] placeholders remain until the user supplies verified numbers; never ship a page presenting unfilled placeholders as final copy. Depends on backlog 250 scaffold. Single static page (guide section 14).
