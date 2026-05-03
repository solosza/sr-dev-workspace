# 001 — Edit Anchor Command to Compute Protocol Hash

## Type
BUILD

## Action
Edit `.claude/commands/kernel/anchor.md` to add protocol hash computation and storage.

## What to Do

In the anchor command's **Part C / Step 14** (Update state), add instructions for the agent to:

1. After reading the protocol file (Part A, step 1), compute a SHA-256 hash of its content
2. In the session_state.json update (step 14), write a `protocol_hash` field:
   ```json
   {
     "protocol_hash": "<sha256 hex digest of protocol file content>",
     "protocol_hash_timestamp": "<ISO timestamp>"
   }
   ```
3. The agent computes the hash by running:
   ```bash
   python -c "import hashlib; print(hashlib.sha256(open('.claude/protocols/[domain]-protocol.md','rb').read()).hexdigest())"
   ```
   and writing the output to `protocol_hash` in session_state.json.

## Target File
`.claude/commands/kernel/anchor.md`

## Acceptance
- [ ] anchor.md step 14 includes protocol_hash field in the state update
- [ ] anchor.md includes instruction to compute SHA-256 of protocol file
- [ ] anchor.md includes the bash command to compute the hash

## Dependencies
None
