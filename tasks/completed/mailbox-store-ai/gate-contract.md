# Gate Contract — Mailbox Store AI Research

## L1: Structural Gates

| ID | Check | Method |
|----|-------|--------|
| STRUCT-01 | docs/research/mailbox-store-ai-operations.md exists | file_exists |
| STRUCT-02 | docs/research/mailbox-store-ai-opportunities.md exists | file_exists |
| STRUCT-03 | docs/research/mailbox-store-ai-competitors.md exists | file_exists |
| STRUCT-04 | docs/research/mailbox-store-ai-mvp-scope.md exists | file_exists |
| STRUCT-05 | docs/research/mailbox-store-ai-pricing.md exists | file_exists |
| STRUCT-06 | docs/research/mailbox-store-ai-architecture.md exists | file_exists |
| STRUCT-07 | docs/research/mailbox-store-ai-report.md exists | file_exists |
| STRUCT-08 | docs/research/mailbox-store-ai-proposal.md exists | file_exists |

## L2: Content Gates

| ID | Check | Method |
|----|-------|--------|
| CONTENT-01 | Operations analysis covers all 4 areas (operations, customer service, business mgmt, AI opportunities) | grep |
| CONTENT-02 | MVP scope defines first agent, tech stack, and timeline | grep |
| CONTENT-03 | Pricing model includes at least 2 pricing tiers | grep |
| CONTENT-04 | Architecture includes integration points for at least 2 carrier APIs | grep |
| CONTENT-05 | Proposal is <=2 pages (under 100 lines) | line_count |
