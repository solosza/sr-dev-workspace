# Walkthrough — Gate Contract

## Phase Gates

| Phase | Gate | Verification |
|-------|------|-------------|
| 1. Setup | State file exists, `sections` non-empty, `cursor: 0`, map user-approved, `sources_read` non-empty (or explicitly external-only) | Read `.claude/state/walkthrough-state.json`; approval visible in conversation |
| 2. Loop (per iteration) | Exactly one section rendered; format parts complete for depth; ledger appended before cursor advanced | `len(ledger) == cursor` after each Record |
| 3. Exit | Durable ledger file written; `status: complete`; `ledger_file` set; no un-revisited DEFERRED entries | `test -f docs/walkthroughs/*[slug]*.md`; read state |

## Step Gates

| Step | Gate | Method |
|------|------|--------|
| 1. Resolve | Mode/type/depth determined; active-state overwrite confirmed by user if applicable | Soft — stated in output |
| 2. Ground | Every grounding source actually Read this session; paths recorded | `sources_read` non-empty; Read calls in transcript |
| 3. Decompose | Map dependency-ordered, one-sitting sections, domain names, user approved | Soft + `contracts/step-03-contract.json` |
| 4. Explain | One section only; correct parts for depth (7 plain / 3 terse); ends with settle prompt; grounding cites only `sources_read` files | Soft — format-contract hard rules |
| 5. Settle | Decision stated by user (or explicit defer) — never assumed from silence | Soft |
| 6. Record | Entry self-contained; append-then-advance order | `len(ledger) == cursor` invariant |
| 7. Exit | File written; handoff offered with all three options | `file_exists` + soft |

## Failure Handling

| Failure | Response |
|---------|----------|
| Explained without grounding (source not in `sources_read`) | Stop; Read the source; re-render the section — do not settle on ungrounded claims |
| Batched two+ sections in one turn | Violation of critical rule 1 — record via /kernel/learn if user flags it; re-render current section alone |
| Cursor/ledger mismatch (`len(ledger) != cursor`) | Reconcile from ledger (source of truth for completed sections); set `cursor = len(ledger)` |
| State lost mid-loop | Rebuild from durable ledger if present; else re-decompose and fast-forward with user confirmation |
| User abandons walkthrough | Leave `status: active`; resume or explicit-overwrite later — never silently discard a ledger |
