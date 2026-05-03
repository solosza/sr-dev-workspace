# Theme and Narrative Structure

## Status
Reference — defines the site's story arc and success criterion

## Theme

**Make the loop visible in 90 seconds to someone who has never heard of Isagawa.**

The site itself is the proof — it was built by the systems it describes. The chain (Kernel → Specs → Spec Factory → Workspace → Tasks → Backlog → Website Cloner → This Page) is the story. The visitor is standing on the most recent output of the loop. The medium is the message.

## 90-Second Test

Show the landing page to one person who has never heard of Isagawa. After 90 seconds, ask "What does Alain do?"

- **Passed:** "He builds systems that build themselves from what he tells them"
- **Failed:** "He builds AI agents" or "he builds governance tools"

The positioning tells you what the product is. The theme tells you what the site does. Both need to be said.

## Narrative Structure — 4 Anchor Moments

Compress the 8-step chain into 4 scroll sections:

### 1. Seed
The original kernel — hooks, commands, session-start, anchor. The smallest thing that carries the idea. Show what was built by hand (minimal) and what it enabled (everything else).

### 2. Growth
Everything the kernel produced that's now part of its normal operation — specs, spec factory, workspaces. The system building its own capabilities. Evidence: 27+ domain specs, 12-step factory pipeline, all produced by the harness from conversational intent.

### 3. Self-Extension
Workspaces producing new capabilities from conversational intent — tasks, backlog, website cloner. The loop extending what future intent can produce. Evidence: the website cloner skill that extracted the design tokens for this very site.

### 4. This Page
The current output at the top of the chain. The punchline. The visitor must know this page is the last link — "You are reading the eighth thing. The first seven produced this one." The reveal that the site itself is evidence.

All 8 original steps appear as sub-evidence inside the 3 layers. The 4th moment is the reveal.

## Content Rules
- No jargon in first 90 seconds of scroll — stranger must grok the loop before seeing technical detail
- Technical detail (kernel mechanisms, gate enforcers, spec factory steps) becomes supporting evidence under each anchor moment, not lead content
- Each section earns the next scroll — if a visitor stops reading at any point, they should still have learned the core idea
- Explicit punchline at bottom — the loop closing is the point, don't leave it implied

## Provenance Component Spec

Dedicated section (not just a footer link) showing real Sigstore attestation bundles. This is the proof that the loop is a system, not a stunt.

### Dual Attestation Display

Show TWO attestation bundles side by side — the site's own pipeline attestation + a second from a different pipeline run (e.g., #050 run-task.sh fix). Two proves a system; one proves a stunt. Build this modularly so any bundle can be swapped in.

### Layout Per Bundle

Each bundle displays as a card:

1. **Intent text leads** — the human-readable intent string (from `raw_input_hash` → resolved via the backlog title) is the first thing the visitor's eye hits. Not file hashes. The story is "someone said this in words, and the system produced that."
2. **Key metadata** — backlog number, task count, completed count, timestamp
3. **Verified badge** — client-side JS fetches the Rekor entry, computes the bundle hash locally, compares, shows ✓ verified or ✗ mismatch. Real cryptographic verification in the browser.
4. **Interactive elements:**
   - "View on Rekor" — links to `search.sigstore.dev/?logIndex=N`
   - "View full bundle" — expandable JSON viewer showing the full attestation bundle

### Build-Time Embedding

Bundle JSON is embedded at build time (baked into the HTML as a `<script type="application/json">` block), NOT fetched at runtime. The Rekor verification fetch is the only network call. This keeps the site static while still enabling live verification.

### Modularity Requirement

The provenance component must accept any attestation bundle as input. The two bundles displayed are configuration, not code. Swapping a bundle means changing one JSON blob, not rewriting the component. This enables:
- Updating the site's own attestation when the site is rebuilt
- Showcasing different pipeline runs as the portfolio of evidence grows
- A/B testing which attestations resonate most with visitors
