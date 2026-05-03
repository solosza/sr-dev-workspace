# Open-Source Attestation Domain Spec Package

## Status
Open

## Priority
High — first-mover opportunity in agent governance, validates monetization thesis

## Summary
Create a public GitHub repo containing a drop-in domain spec that teaches any coding agent to self-build a Sigstore-based attestation pipeline. The spec gives agent users cryptographic proof of what was requested, what was done, and that nothing was tampered with — intent chains, task completion signing, audit trails, and Rekor transparency log integration. Target audience is the coding agent community (Claude Code, Cursor, Windsurf, Copilot). This validates demand and establishes credibility before building paid products (SaaS dashboard, enterprise compliance).

## Requirements

### Core Deliverable
- Domain spec that any agent can consume and self-build from
- Works with Claude Code out of the box, adaptable to other agents
- Produces working Sigstore attestation on first run
- README that explains the value prop to a developer audience

### What the Spec Must Teach the Agent to Build
- **Intent chain** — hash user's raw request at invocation time, append-only log, tamper-evident
- **Task completion attestation** — Sigstore cosign on task artifacts, log entry to Rekor
- **Audit trail** — actions log (append-only JSONL), anchor logs (periodic checkpoints)
- **Protocol hash verification** — detect if governance files were modified between anchors
- **Verification commands** — agent can verify its own prior attestations

### What the Repo Must Contain
- `SKILL.md` + step references (the domain spec itself)
- `README.md` — value prop, quickstart, how it works, who it's for
- `examples/` — sample attestation output, verification walkthrough
- `docs/architecture.md` — how the pieces fit together
- `LICENSE` — MIT or Apache 2.0

### Audience & Positioning
- **Primary:** Claude Code users who want agent accountability
- **Secondary:** Teams adopting coding agents who need audit trails
- **Future:** Enterprise compliance (SOC2, HIPAA, regulated industries)
- **Positioning:** "Prove your agent did what it said it did"
- **Distribution model:** User drops spec into workspace, agent builds the pipeline itself

### Monetization Groundwork (not built now, just designed for)
- SaaS dashboard for viewing/searching attestation history
- Enterprise compliance templates
- The spec is free; the tooling around it is paid

## References
- Existing attestation work: backlog [046](done/046-kernel-build-sigstore-attestation-pipeline.md), [048](done/048-kernel-add-intent-chain-attestation.md), [049](done/049-kernel-fix-attestation-signing.md)
- Sigstore: https://sigstore.dev
- Rekor transparency log: https://search.sigstore.dev
- Our attestation lib: `lib/attestation/`
- Intent chain implementation: `lib/attestation/intent.py`

## Task Builder Input
- **Deliverable:** Public GitHub repo with attestation domain spec, README, examples, architecture doc
- **Location:** new-repo:D:\my_ai_projects\agent-attestation-spec
- **Scope:** BUILD
- **Constraints:** Must extract patterns from our existing attestation pipeline (lib/attestation/, backlog 046/048/049) without leaking internal kernel details. Spec must be agent-agnostic in principle but Claude Code-native in implementation. Needs Sigstore/cosign as a dependency. README must sell the "why" to developers who haven't thought about agent attestation yet.
