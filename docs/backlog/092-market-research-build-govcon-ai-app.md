# Government Contracting AI App — Research + Build

## Status
Open

## Priority
High — high-margin opportunity with clear automation surface; research phase validates before build commitment

## Summary
Two-phase project: (1) Research whether the "Natalie model" of government contracting is viable — bidding on SAM.gov contracts, subcontracting the work, capturing the spread. The X post (1.1M views) claims six figures from 1-2 hours/week, but the community note flags FAR 52.219-14 (50% rule on service contracts). Research must validate the legal constraints, actual economics, and viable contract types. (2) Build an AI-native government contracting app using the Isagawa Kernel pattern (commands/skills/references/data contracts) that automates opportunity scanning, solicitation analysis, subcontractor discovery, and proposal drafting.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[092-market-research-build-govcon-ai-app/phase-1-research]] | Validate the model — FAR rules, economics, legal constraints |
| [[092-market-research-build-govcon-ai-app/phase-2-app-architecture]] | AI-native app design — commands, skills, references, data contracts |
| [[092-market-research-build-govcon-ai-app/compliance-rules]] | FAR/SBA rules as structured data — the compliance engine |
| [[092-market-research-build-govcon-ai-app/sam-gov-integration]] | SAM.gov API/scraping — opportunity pipeline |

## Phases

1. **Research** — Validate viability, legal constraints, economics
2. **Build** — AI-native govcon app with full Kernel infrastructure

## Requirements
- Research must answer: Is the subcontract-and-spread model legal? Under what conditions?
- App must enforce FAR compliance (50% rule, set-aside requirements) via hooks
- App must integrate with SAM.gov for opportunity discovery
- Solicitation analysis must handle 20+ page PDFs
- Proposal generation must produce submission-ready documents
- All rules stored as visible JSON/markdown (auditable, updatable)

## References
- Source: X post by @mhp_guy (Chris Koerner), May 9, 2026, 1.1M views
- Podcast: Spotify episode with "Natalie" — government contracting deep dive
- FAR 52.219-14: Limitations on Subcontracting (sba.gov/federal-contra, acquisition.gov/far/52.219-14)
- SAM.gov: Federal contract opportunity database
- Pattern: Same 3-layer architecture as RT Automation (Config JSON + Validators + Kernel enforcement)

## Task Builder Input
- **Deliverable:** Phase 1: Research report with go/no-go decision. Phase 2: Working govcon AI app with commands, skills, compliance hooks
- **Location:** Phase 1: `subproject:govcon-research`. Phase 2: `new-repo:D:\my_ai_projects\govcon-ai`
- **Scope:** RESEARCH (Phase 1), BUILD (Phase 2)
- **Constraints:** Phase 2 depends on Phase 1 go decision. SAM.gov API access may require registration. FAR rules must be verified against actual federal regulations, not just the X post. The 50% rule (FAR 52.219-14) is a hard constraint that shapes the entire business model.
