# Gate Contract — Intent Chain Attestation

## Gates

| ID | Gate | Verification |
|----|------|-------------|
| BUILD-01 | `lib/attestation/intent.py` exists with `record_intent()` and `read_intent_chain()` | file exists + functions importable |
| BUILD-02 | `.claude/commands/kernel/backlog.md` has intent capture step | grep for "intent" in backlog.md |
| BUILD-03 | `lib/attestation/schema.py` accepts `intent_chain` parameter in `create_bundle()` | function signature check |
| BUILD-04 | `lib/attestation/attest.py` reads intent chain and passes to `create_bundle()` | grep for "intent_chain" in attest.py |
| TEST-01 | L1 structural: all 4 files exist/modified | file existence check |
| TEST-02 | L2 intent logger: record writes JSONL, read returns entries | python unit test |
| TEST-03 | L2 schema: bundle with intent_chain validates | python schema test |
| TEST-04 | L3 full flow: dry-run attestation includes intent chain | end-to-end test |
