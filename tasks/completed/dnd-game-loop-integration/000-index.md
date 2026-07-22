# D&D Game Loop Integration — Task Index

## Goal
Build generalized loop template + fix all 11 game loops with DDD structure, contracts, gates, and integration.

## Source
-> [[docs/backlog/180-domain-build-dnd-game-loop-integration.md]]

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-execute-pipeline]] | BUILD | none | in_progress |
| **Phase 1: Generalized Loop Template** | | | | |
| 002 | [[002-build-create-loop-template-dir]] | BUILD | none | pending |
| 003 | [[003-build-write-loop-template-skill]] | BUILD | 002 | pending |
| 004 | [[004-build-write-input-contract-template]] | BUILD | 002 | pending |
| 005 | [[005-build-write-output-contract-template]] | BUILD | 002 | pending |
| 006 | [[006-build-write-rules-contract-template]] | BUILD | 002 | pending |
| 007 | [[007-build-write-integration-contract-template]] | BUILD | 002 | pending |
| 008 | [[008-build-write-gate-contract-template]] | BUILD | 002 | pending |
| 009 | [[009-build-write-test-fixture-template]] | BUILD | 002 | pending |
| 010 | [[010-test-verify-loop-template]] | TEST | 003-009 | pending |
| **Phase 2A: Legacy Python Cleanup** | | | | |
| 011 | [[011-build-remove-campaign-python]] | BUILD | none | pending |
| 012 | [[012-build-remove-challenge-python]] | BUILD | none | pending |
| 013 | [[013-build-remove-rest-python]] | BUILD | none | pending |
| 014 | [[014-build-remove-atomic-ops-python]] | BUILD | none | pending |
| 015 | [[015-test-verify-no-python-in-loops]] | TEST | 011-014 | pending |
| **Phase 2B: Tier 1 — Leaf Loops** | | | | |
| 016 | [[016-build-write-ability-saves-input-contract]] | BUILD | 010 | pending |
| 017 | [[017-build-write-ability-saves-output-contract]] | BUILD | 010 | pending |
| 018 | [[018-build-write-ability-saves-rules-contract]] | BUILD | 010 | pending |
| 019 | [[019-build-write-ability-saves-integration-contract]] | BUILD | 010 | pending |
| 020 | [[020-build-update-item-use-skill]] | BUILD | 010 | pending |
| 021 | [[021-build-write-item-use-input-contract]] | BUILD | 020 | pending |
| 022 | [[022-build-write-item-use-output-contract]] | BUILD | 020 | pending |
| 023 | [[023-build-write-item-use-rules-contract]] | BUILD | 020 | pending |
| 024 | [[024-build-write-item-use-integration-contract]] | BUILD | 020 | pending |
| 025 | [[025-build-write-item-use-gate-contract]] | BUILD | 020 | pending |
| 026 | [[026-build-create-item-use-test-fixture]] | BUILD | 020 | pending |
| 027 | [[027-test-verify-tier1-loops]] | TEST | 016-026 | pending |
| **Phase 2C: Tier 2 — Mid-level Loops** | | | | |
| 028 | [[028-build-write-combat-input-contract]] | BUILD | 027 | pending |
| 029 | [[029-build-write-combat-output-contract]] | BUILD | 027 | pending |
| 030 | [[030-build-write-combat-rules-contract]] | BUILD | 027 | pending |
| 031 | [[031-build-write-combat-integration-contract]] | BUILD | 027 | pending |
| 032 | [[032-build-write-combat-gate-contract]] | BUILD | 027 | pending |
| 033 | [[033-build-create-combat-test-fixture]] | BUILD | 027 | pending |
| 034 | [[034-build-write-social-input-contract]] | BUILD | 027 | pending |
| 035 | [[035-build-write-social-output-contract]] | BUILD | 027 | pending |
| 036 | [[036-build-write-social-rules-contract]] | BUILD | 027 | pending |
| 037 | [[037-build-write-social-integration-contract]] | BUILD | 027 | pending |
| 038 | [[038-build-write-social-gate-contract]] | BUILD | 027 | pending |
| 039 | [[039-build-update-challenge-skill]] | BUILD | 012, 027 | pending |
| 040 | [[040-build-write-challenge-input-contract]] | BUILD | 039 | pending |
| 041 | [[041-build-write-challenge-output-contract]] | BUILD | 039 | pending |
| 042 | [[042-build-write-challenge-rules-contract]] | BUILD | 039 | pending |
| 043 | [[043-build-write-challenge-integration-contract]] | BUILD | 039 | pending |
| 044 | [[044-build-write-challenge-gate-contract]] | BUILD | 039 | pending |
| 045 | [[045-build-create-challenge-test-fixture]] | BUILD | 039 | pending |
| 046 | [[046-build-write-env-hazards-input-contract]] | BUILD | 027 | pending |
| 047 | [[047-build-write-env-hazards-output-contract]] | BUILD | 027 | pending |
| 048 | [[048-build-write-env-hazards-rules-contract]] | BUILD | 027 | pending |
| 049 | [[049-build-write-env-hazards-integration-contract]] | BUILD | 027 | pending |
| 050 | [[050-build-write-downtime-input-contract]] | BUILD | 027 | pending |
| 051 | [[051-build-write-downtime-output-contract]] | BUILD | 027 | pending |
| 052 | [[052-build-write-downtime-rules-contract]] | BUILD | 027 | pending |
| 053 | [[053-build-write-downtime-integration-contract]] | BUILD | 027 | pending |
| 054 | [[054-test-verify-tier2-loops]] | TEST | 028-053 | pending |
| **Phase 2D: Tier 3 — Complex Loops** | | | | |
| 055 | [[055-build-update-travel-skill]] | BUILD | 054 | pending |
| 056 | [[056-build-write-travel-input-contract]] | BUILD | 055 | pending |
| 057 | [[057-build-write-travel-output-contract]] | BUILD | 055 | pending |
| 058 | [[058-build-write-travel-rules-contract]] | BUILD | 055 | pending |
| 059 | [[059-build-write-travel-integration-contract]] | BUILD | 055 | pending |
| 060 | [[060-build-write-travel-gate-contract]] | BUILD | 055 | pending |
| 061 | [[061-build-create-travel-test-fixture]] | BUILD | 055 | pending |
| 062 | [[062-build-move-rest-contract]] | BUILD | 054 | pending |
| 063 | [[063-build-update-rest-skill]] | BUILD | 013, 062 | pending |
| 064 | [[064-build-write-rest-input-contract]] | BUILD | 063 | pending |
| 065 | [[065-build-write-rest-output-contract]] | BUILD | 063 | pending |
| 066 | [[066-build-write-rest-rules-contract]] | BUILD | 063 | pending |
| 067 | [[067-build-write-rest-integration-contract]] | BUILD | 063 | pending |
| 068 | [[068-build-write-rest-gate-contract]] | BUILD | 063 | pending |
| 069 | [[069-build-create-rest-test-fixture]] | BUILD | 063 | pending |
| 070 | [[070-test-verify-tier3-loops]] | TEST | 055-069 | pending |
| **Phase 2E: Tier 4 — Outer Loops** | | | | |
| 071 | [[071-build-write-orch-routing-contract]] | BUILD | 070 | pending |
| 072 | [[072-build-write-orch-integration-spec]] | BUILD | 070 | pending |
| 073 | [[073-build-write-orch-gate-contract]] | BUILD | 070 | pending |
| 074 | [[074-build-create-orch-test-fixture]] | BUILD | 070 | pending |
| 075 | [[075-build-rewrite-campaign-skill]] | BUILD | 011, 070 | pending |
| 076 | [[076-build-write-campaign-input-contract]] | BUILD | 075 | pending |
| 077 | [[077-build-write-campaign-output-contract]] | BUILD | 075 | pending |
| 078 | [[078-build-write-campaign-rules-contract]] | BUILD | 075 | pending |
| 079 | [[079-build-write-campaign-integration-contract]] | BUILD | 075 | pending |
| 080 | [[080-build-write-campaign-gate-contract]] | BUILD | 075 | pending |
| 081 | [[081-build-create-campaign-test-fixture]] | BUILD | 075 | pending |
| 082 | [[082-test-verify-tier4-loops]] | TEST | 071-081 | pending |
| **Phase 3: Integration Testing** | | | | |
| 083 | [[083-build-write-integration-turn-walkthrough]] | BUILD | 082 | pending |
| 084 | [[084-build-write-integration-contract-chain]] | BUILD | 082 | pending |
| 085 | [[085-build-write-integration-downstream-spec]] | BUILD | 082 | pending |
| 086 | [[086-test-structural-audit-all-loops]] | TEST | 083-085 | pending |

## Gate Contract
-> [[gate-contract.md]]

## Deliverables
- Generalized loop template in workspace (`.claude/skills/loop-template/`)
- All 11 game loops with DDD SKILL.md, 4 contracts each, gate contract, test fixtures
- No legacy Python in loop directories
- Integration test specifications
