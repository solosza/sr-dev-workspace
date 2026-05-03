# 006 — Write System Architecture Proposal

## Type
BUILD

## Action
Based on MVP scope (task 004) and opportunity assessment (task 002), write the system architecture proposal.

Include:
1. **High-level architecture** — components, data flow, integration points
2. **Agent design** — how agents are structured (Isagawa kernel powered? Standalone? Hybrid?)
3. **Carrier integrations** — USPS Web Tools, UPS Developer Kit, FedEx REST API, DHL Express API — auth methods, rate limits, data formats
4. **Notification layer** — Twilio SMS, SendGrid email, or alternatives
5. **Data layer** — database schema concepts, what gets stored, retention
6. **Deployment model** — cloud-hosted SaaS, self-hosted, or hybrid? Multi-tenant architecture?
7. **Security** — PII handling (customer addresses, IDs), CMRA form data, payment info

## Target File
`docs/research/mailbox-store-ai-architecture.md`

## Acceptance
- [ ] Architecture diagram (text-based, mermaid, or ASCII)
- [ ] At least 2 carrier API integration points detailed
- [ ] Data flow described
- [ ] Security considerations addressed

## Dependencies
002, 004
