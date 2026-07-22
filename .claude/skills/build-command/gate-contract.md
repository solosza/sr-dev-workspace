# Gate Contract

## Phase Gates

| Gate | Trigger | Check | On Fail |
|------|---------|-------|---------|
| Phase 1 → 2 | After Step 1 | Design doc passes completeness (7/7 required). User confirms `proceed`. | STOP — user must update design doc or confirm `proceed anyway` |
| Phase 2 → 3 | After Step 2 | SKILL.md written. User confirms `approve`. | STOP — user provides corrections, agent re-generates |
| Phase 3 → 4 | After Step 7 | All layer files written (L1-L5). | Re-run failed step |
| Phase 4 done | After Step 8 | All files pass checks. 200-line threshold met. | Report failures, keep state for re-run |

## Step Gates

| Step | Output | Validation |
|------|--------|-----------|
| 1 | Completeness report | All 7 required sections found in design doc (index + payloads) |
| 2 | `.claude/skills/[name]/SKILL.md` | Has Identity, Philosophy, Vocabulary, Critical Rules, File Index sections |
| 3 | `workflow.md` + `gate-contract.md` | workflow has Phases + State Persistence; gate-contract has Phase Gates + Step Gates |
| 4 | `steps/step-NN-[name].md` × N | Count matches design doc step count. Each has Purpose + Procedure |
| 5 | `references/INDEX.md` | Has wikilinks to all design doc reference files |
| 6 | `contracts/step-NN-contract.json` | Valid JSON. Has contract_metadata + validations arrays |
| 7 | `.claude/commands/kernel/[name].md` | Has Usage + Design Reference + Skill Reference sections |
| 8 | Verification report | All per-layer checks pass. All files ≤ 200 lines |
