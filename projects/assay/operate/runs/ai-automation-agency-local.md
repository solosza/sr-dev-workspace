# Operate — Governed [niche] automation (run-state)

**Date:** 2026-07-30 · **Business:** governed automation for a regulated local niche
**Run-state:** PLAN (not live — pending the pilot commit).

## The operation (repeating cycle)
trigger (recall due / inbound) → automation **PROPOSES** action → **human APPROVES** → act → **log to audit ledger** → repeat.

## HITL checkpoints (mandatory)
Every action touching a patient/client/record requires human sign-off. Auto-*prepare* only; never auto-*act* on a regulated decision. This is the firewall AND the product.

## Metrics to watch
- Hours saved / bookings recovered (the value)
- **Compliance incidents — target 0** (the promise)
- Approval latency (is the human-in-the-loop a bottleneck?)
- Retention

## Exceptions
Anything ambiguous or outside policy → pause + escalate to the human. Never guess in a regulated flow.

## Cadence + improve
Continuous run + weekly review. Feed outcomes (what worked, incidents, time saved) to `/sharpen`.

**HITL:** this loop is continuous approval — nothing acts without a human yes.
