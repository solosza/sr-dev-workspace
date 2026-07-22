# References — check-5-layer

## Design Document

> `.claude/docs/design/check-5-layer/index.md`

## Contract (Source of Truth)

> `.claude/docs/design/check-5-layer/references/5-layer-contract.md`

The 5-layer architecture contract v1.0. All compliance checks derive from this document.

## Design Payloads

| Document | Purpose | Link |
|----------|---------|------|
| Workflow | Steps 1-5 procedure details | `[[check-5-layer/references/workflow]]` |
| Layer Classification | Directory + AST classification rules | `[[check-5-layer/references/layer-classification]]` |
| AST Checks | Per-rule AST implementation details | `[[check-5-layer/references/ast-checks]]` |

## Cross-References

- `/gap` — same fix-mode UX (approve/modify/skip/approve all/stop)
- `/kernel/prod-test` Step 3 — can invoke check-5-layer as inner loop
- `/build-command` Step 8 — can invoke check-5-layer to verify new platform code
