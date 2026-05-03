# Sigstore Attestation Pipeline — Task Index

**Backlog:** `docs/backlog/046-kernel-build-sigstore-attestation-pipeline.md`
**Location:** workspace (`lib/attestation/`, `.claude/commands/`, `.claude/skills/execute-pipeline/`)

## Phase 1: Research + Setup

| # | Task | Type | Dependencies |
|---|------|------|-------------|
| 001 | [[001-research-nono-attest-cosign]] | RESEARCH | — |
| 002 | [[002-build-install-cosign]] | BUILD | 001 |
| 003 | [[003-build-create-attestations-dir]] | BUILD | — |

## Phase 2: Core Modules

| # | Task | Type | Dependencies |
|---|------|------|-------------|
| 004 | [[004-build-write-schema]] | BUILD | 001 |
| 005 | [[005-build-write-hash-collector]] | BUILD | 004 |
| 006 | [[006-build-write-signer]] | BUILD | 002, 004 |
| 007 | [[007-build-write-rekor-logger]] | BUILD | 006 |
| 008 | [[008-build-write-attest-orchestrator]] | BUILD | 005, 006, 007 |

## Phase 3: Integration

| # | Task | Type | Dependencies |
|---|------|------|-------------|
| 009 | [[009-build-write-attest-command]] | BUILD | 008 |
| 010 | [[010-build-update-pipeline-step05]] | BUILD | 008 |

## Phase 4: Testing

| # | Task | Type | Dependencies |
|---|------|------|-------------|
| 011 | [[011-test-l1-verify-files-exist]] | TEST | 003-010 |
| 012 | [[012-test-l2-hash-collection]] | TEST | 005 |
| 013 | [[013-test-l2-validate-bundle-schema]] | TEST | 004, 005 |
| 014 | [[014-test-l3-full-attestation]] | TEST | 008 |

## Gate Contract

→ [[gate-contract]]
