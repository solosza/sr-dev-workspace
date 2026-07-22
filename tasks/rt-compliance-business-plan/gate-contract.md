# Gate Contract — 274 RT Compliance Business Plan

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| BP-01 | research-notes.md: ROI/pricing/competitive comparables gathered (denial/clawback cost context, SNF-compliance-tool pricing models, PCC Advisor Suite positioning) — cited w/ source + date; self-reported vs independent flagged; the two unverified SNF-RT numbers marked owner/expert-to-confirm, NOT fabricated | file_exists + content | 001 | cited notes, gaps flagged |
| BP-02 | business-plan.md has Problem (owner-facing, anchored to catching errors PRE-submission + ranked error modes, NOT billing-labor), Solution (the validate-and-flag gate + explicit scope boundary), Proof/accuracy (det-vs-judgment split, human-in-the-loop guarantee) | file_exists + content | 002 | 3 sections, owner framing |
| BP-03 | business-plan.md adds ROI (clawback/denial avoidance + audit-defensibility modeled vs manual cost, using 269 cited figures), Pricing (per-facility/per-claim/rev-share evaluated, one recommended for the single-facility pilot), GTM (admin champion -> owner approval, pilot-first, liability-not-speed positioning) | file_exists + content | 003 | 3 sections, cited |
| BP-04 | business-plan.md adds Risk & compliance posture (HIPAA/BAA, never-auto-bill boundary, human-review guarantee) + the four gating preconditions from go-no-go.md stated as honest open items; full-doc coherence pass (narrowed RT-specific differentiation, not general AI-native billing) | file_exists + content | 004 | posture + 4 preconditions + coherent |
| BP-05 | SCOPE-BOUNDARY GATE: business-plan.md explicitly states never-auto-bill AND never-auto-chart; contains NO claim of automating billing submission, charting, or patient filtering; positions on liability/audit-defensibility not automation speed | grep + read | 005 | boundary present, no auto-workflow claims |

## Rules
- READ the four 269 research reports in the output dir FIRST (RULE ZERO) — ground every claim in them; do not re-derive the domain
- The scope boundary (validate-and-flag, never auto-bill/chart) is LOAD-BEARING — it is the liability firewall, present in Solution AND Risk sections
- Web research for comparables only; cite source + date; flag self-reported vs independent; NEVER fabricate the unverified SNF-RT clawback/labor numbers — mark them owner/expert-to-confirm
- Owner-facing tone (revenue integrity, audit exposure, cost) — administrators champion, owners approve
- Honest: feasibility optimism AND the liability/PHI/preconditions reality; no mush
- Any RED (missing section, uncited claim, fabricated number, auto-workflow claim) -> fix -> /kernel/learn
