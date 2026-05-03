# Intent Chain Attestation — Task Index

## Backlog
docs/backlog/048-kernel-add-intent-chain-attestation.md

## Phase 1: Build

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | Write intent logger module | BUILD | — |
| 002 | Update backlog command with intent capture | BUILD | 001 |
| 003 | Update attestation schema with intent_chain | BUILD | 001 |
| 004 | Update attestation orchestrator to include intent chain | BUILD | 001, 003 |

## Phase 2: Test

| # | Task | Type | Depends |
|---|------|------|---------|
| 005 | L1: Verify all files exist and modified | TEST | 001-004 |
| 006 | L2: Intent logger record + read unit test | TEST | 001 |
| 007 | L2: Schema validates bundle with intent_chain | TEST | 003 |
| 008 | L3: Full intent flow — record → attest → verify chain in bundle | TEST | 004 |
