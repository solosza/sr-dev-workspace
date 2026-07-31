# Launch — Governed [niche] automation MVP

**Date:** 2026-07-30 · **Business:** governed automation for a regulated local niche
**MVP:** ONE governed automation for ONE niche (e.g. dental recall + booking) with an audit log + human-approval — the smallest thing that delivers "compliant, done-for-you, hours saved."

## Reuse vs build
| Piece | Reuse / build / buy |
|-------|--------------------|
| Audit trail + mandatory HITL | **reuse** — the kernel (this is the edge) |
| Workflow engine + LLM | **buy** — n8n + Claude |
| Niche workflow (recall/booking logic) | **build** — the only real build |
| Integration to their system (PMS/CRM) | **build/buy** — connector |

## HITL / automation line
Automation **prepares** (drafts the message, proposes the booking); the office **approves** before anything touches a patient/record. Auto-act on a regulated decision = banned. This line carries straight into `/operate`.

## Go-live test
Run ONE real recall/booking cycle end-to-end for one pilot client: trigger → proposal → human approval → action → **audit log intact**. Prove the value once + zero compliance gaps.

**HITL:** approve the MVP scope · trim · kill. Building happens on approval, on a branch.
