# Walkthrough — Reference Index

Routing table only — content lives in the design doc. No duplication.

## Design Doc References

| Reference | Path | Content |
|-----------|------|---------|
| Design index | `.claude/docs/design/walkthrough/index.md` | Identity, philosophy, rules, workflow summary, state schema |
| Workflow (step specs) | `.claude/docs/design/walkthrough/references/workflow.md` | Per-step purpose + procedure, loop mechanics, resume, composability contract |
| Format contract | `.claude/docs/design/walkthrough/references/format-contract.md` | The seven-part explanation format — per-part rules, hard rules, anti-patterns |
| Decomposition strategies | `.claude/docs/design/walkthrough/references/decomposition-strategies.md` | Section derivation per input type + worked example |
| Depth modes | `.claude/docs/design/walkthrough/references/depth-modes.md` | Plain vs terse rendering, mid-loop dials |
| Ledger spec | `.claude/docs/design/walkthrough/references/ledger-spec.md` | Entry schema, durable file format, handoff contract |
| Contract definitions | `.claude/docs/design/walkthrough/references/contracts.md` | Soft + mechanical validation source definitions |

## By Step

| Step | Reads |
|------|-------|
| 1. Resolve Input | design workflow.md (Step 1) |
| 2. Ground | design workflow.md (Step 2) |
| 3. Decompose | decomposition-strategies.md; `contracts/step-03-contract.json` |
| 4. Explain | format-contract.md; depth-modes.md |
| 5. Settle | depth-modes.md |
| 6. Record | ledger-spec.md; `contracts/step-06-contract.json` |
| 7. Exit | ledger-spec.md; `contracts/step-07-contract.json` |

## By Artifact Type

| Artifact | Governing reference |
|----------|--------------------|
| Section map + state file | decomposition-strategies.md + contracts/step-03-contract.json |
| Explanation message | format-contract.md + depth-modes.md |
| Ledger entry / durable ledger file | ledger-spec.md |
