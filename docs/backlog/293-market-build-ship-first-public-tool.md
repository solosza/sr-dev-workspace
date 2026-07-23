# Ship One Hardened Factory Output as a First Public Tool — Kun Footsteps

## Status
Open

## Priority
High — this is the visibility play made concrete. Everything else is *building*; this is *shipping*. One 400-star tool moves your reputation more than the entire private kernel has (Kun proved it four times).

## Summary
Pick the single cleanest asset, harden it to provably-complete on the fixed runner, package it for five-minute adoption, and **publish it publicly**. The point is distribution, not more building — turn the higher-abstraction factory edge from a private research system into a public tool with a star count. Directly closes the "nobody knows my work" gap ([[282-...visibility-strategy]]) and follows Kun Chen's model (sharp, single-purpose, trivially adoptable tools).

## Candidate assets (pick one)
- **A factory output** — `pci-dss` (26/26 gates + 8/8 anti-tests) or `iac-security` (30/30) are the cleanest. Regenerate on the hardened runner (281) so it is provably complete, then ship as a standalone governed-compliance spec/tool.
- **The render loop** — closest analog to Kun's Lavish (which it already cites). Standalone "capture-surface → route-through-your-command" primitive; genuinely nice and small.
- **kernel-minimal** — the canonical governed-agent runner; already prod-tested (286). The most infrastructure-y option.

## Requirements
- **Choose the asset** (owner decision) — recommend the render loop (most distinctive, smallest surface, direct Kun-analog) or pci-dss (proves the factory's output quality).
- **Harden to provably-complete:** regenerate/finish on the hardened runner; all gates green; no 15/31 gaps.
- **Package for adoption:** one clear README (what it does in one sentence), a five-minute install, one job it does well, a short demo (gif/asciinema). No sprawl — a person adopts a tool, not a worldview.
- **Publish public:** new public repo (or make an existing one public), clean-room verified (no client/proprietary leakage), MIT or similar.
- **Announce (ties to 282):** a short write-up / post positioning it against the current agentic-engineering conversation.

## References
- Reliability + visibility discussion 2026-07-23 (Kun Chen: gnhf 2k / no-mistakes 1.3k / lavish-axi 425 — sharp single-purpose tools).
- [[282-...visibility-strategy]] (the "get known" plan this executes) · factory outputs in `domain-spec-factory/output/` (pci-dss, iac-security) · the render skill (`.claude/skills/render`).
- Depends on a trustworthy substrate: cleanest after the reliability set (290/291/292) + 281 (done) so the shipped artifact is provably solid.

## Task Builder Input
- **Deliverable:** One public repo containing a hardened, provably-complete, five-minute-adoptable tool + README + demo, clean-room verified, announced.
- **Location:** new-repo:D:\my_ai_projects\[chosen-tool-name]
- **Scope:** BUILD
- **Constraints:** Owner picks the asset first. Clean-room (no proprietary/client leakage). Distribution-first — resist adding scope; ship the smallest thing that works. Best after the reliability set lands so "reliable" is true, not aspirational.
