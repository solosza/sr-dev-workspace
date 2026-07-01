# Phase 2: AI-Native Government Contracting App

## Status
NEW — depends on Phase 1 go decision

## Location
`D:\my_ai_projects\govcon-ai`

## Architecture
AI-native app using Isagawa Kernel pattern: commands + skills + references + data contracts + compliance hooks.

## Commands

| Command | Purpose |
|---------|---------|
| `/govcon/scan-opportunities` | Pull opportunities from SAM.gov, filter by NAICS, set-aside type, dollar range, location |
| `/govcon/analyze-solicitation` | AI reads solicitation PDF, extracts requirements, flags risks, checks past performance needs |
| `/govcon/find-subcontractors` | Search for subs by capability, verify SAM registration, check "similarly situated" status |
| `/govcon/draft-proposal` | Generate proposal sections from solicitation analysis + sub quotes |
| `/govcon/check-compliance` | Validate a bid against FAR rules before submission |
| `/govcon/track-contract` | Track active contracts, deadlines, deliverables, payments |

## Skills

| Skill | Purpose |
|-------|---------|
| `solicitation-analyzer/` | Deep analysis of government solicitation documents (PDF parsing, requirement extraction, risk scoring) |
| `proposal-generator/` | Template-driven proposal generation with compliance checks |
| `opportunity-scanner/` | SAM.gov integration, filtering, ranking |

## References (Structured Data)

| Reference | Format | Purpose |
|-----------|--------|---------|
| `far-rules.json` | JSON | FAR rules relevant to small business contracting (52.219-14, thresholds, set-aside types) |
| `naics-codes.json` | JSON | NAICS code database with descriptions, size standards |
| `set-aside-types.json` | JSON | Set-aside categories, eligibility requirements, subcontracting limits |
| `proposal-templates/` | Markdown | Proposal section templates (technical approach, past performance, pricing) |
| `compliance-checklist.json` | JSON | Pre-submission compliance checklist |

## Data Contracts

| Contract | Schema | Purpose |
|----------|--------|---------|
| `opportunity.json` | SAM.gov opportunity schema | Standardized opportunity record |
| `solicitation-analysis.json` | Analysis output schema | Parsed solicitation with extracted requirements |
| `subcontractor.json` | Sub profile schema | Subcontractor capabilities, rates, SAM status |
| `proposal.json` | Proposal package schema | Complete proposal with all required sections |
| `bid-decision.json` | Go/no-go schema | Bid decision with risk score, margin estimate, compliance status |

## Compliance Hooks (Non-Bypassable)
- **Block proposal if 50% rule violated** — calculates personnel cost split, blocks if prime share < 50%
- **Block proposal if missing certs** — checks required registrations (SAM, NAICS, set-aside eligibility)
- **Block proposal if past performance required but not provided** — checks contract value vs simplified acquisition threshold
- **Warn if margin below threshold** — flags bids where spread is too thin after sub costs

## Dependencies
- Phase 1 research report (go decision)
- SAM.gov API access (may require entity registration)
- PDF parsing capability (for solicitation documents)
