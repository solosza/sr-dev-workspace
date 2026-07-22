# Portfolio Site - Evidence Section

## Status
Open

## Priority
High - the proof section; metrics must be defensible

## Summary
Build guide section 7: 3-4 sanitized evidence cards (governed workflow, independent validation, controlled delivery, evaluation routing), one with a sanitized 10-15s CLI trace GIF or screenshot. Every metric slot stays an [INSERT] placeholder until the user supplies a verified number.

## Requirements
- Card layout responsive two-column per guide section 14
- Sanitized visuals: capture from real kernel runs, scrub paths/identifiers/internal names before embedding
- NO metric invented - [INSERT] slots clearly marked pending user verification (page may ship with the mechanism DESCRIBED and the number omitted, per guide)
- Avoid: raw state files, full contracts, credentials, internal identifiers

## References
- Format guide: `projects/portfolio-site/format-guide-v1.2.md` (workspace copy of GitHub_Portfolio_Format_Guide_v1.2.md)
- Sibling portfolio backlogs 250-261 (build in numeric order; 250 first, 261 last)

## Task Builder Input
- **Deliverable:** Evidence section live with sanitized cards + one CLI trace visual; placeholder metrics flagged for user fill-in
- **Location:** new-repo:D:\my_ai_projects\portfolio-site
- **Scope:** BUILD
- **Constraints:** HUMAN INPUT (async, non-blocking): verified metric numbers - build everything else and list needed numbers in the completion report. IP-safe disclosure checklist (guide section 13) governs ALL copy: never publish state schemas, hook logic/names, gate rules, command protocols, meta-factory internals, or full domain contracts. NO absolute claims ('100%', 'guaranteed', 'unbypassable', 'zero drift'). NO invented metrics - [INSERT] placeholders remain until the user supplies verified numbers; never ship a page presenting unfilled placeholders as final copy. Depends on backlog 250 scaffold. Single static page (guide section 14).
