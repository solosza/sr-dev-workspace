# Portfolio Site - Hero Section

## Status
Open

## Priority
High - first screen decides the 10-second recruiter scan

## Summary
Build the hero per guide section 3: name, role identity line, one-line value prop, personal-ownership statement of Isagawa, verified-stack badge row, Resume/GitHub/LinkedIn/Email buttons, one-line hiring target.

## Requirements
- Name + role identity + hiring target from job-application-spec profile.json + resume (real data, not placeholders)
- Stack badge row: ONLY verified tools (guide example: Python, TypeScript, Selenium, Playwright, Docker, Paramiko, pyodbc, Claude Code) - cross-check each against actual repos before including
- Buttons wired: resume PDF anchor, GitHub profile, LinkedIn, mailto
- Guide Avoid list enforced: no logo-first, no Founder-only label, no keyword-stuffed frameworks

## References
- Format guide: `projects/portfolio-site/format-guide-v1.2.md` (workspace copy of GitHub_Portfolio_Format_Guide_v1.2.md)
- Sibling portfolio backlogs 250-261 (build in numeric order; 250 first, 261 last)

## Task Builder Input
- **Deliverable:** Hero section live on the deployed page passing guide section 3 include/avoid lists
- **Location:** new-repo:D:\my_ai_projects\portfolio-site
- **Scope:** BUILD
- **Constraints:** IP-safe disclosure checklist (guide section 13) governs ALL copy: never publish state schemas, hook logic/names, gate rules, command protocols, meta-factory internals, or full domain contracts. NO absolute claims ('100%', 'guaranteed', 'unbypassable', 'zero drift'). NO invented metrics - [INSERT] placeholders remain until the user supplies verified numbers; never ship a page presenting unfilled placeholders as final copy. Depends on backlog 250 scaffold. Single static page (guide section 14).
