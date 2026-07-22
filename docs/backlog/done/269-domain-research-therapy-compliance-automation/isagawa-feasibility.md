# Isagawa Feasibility

**Status:** NEW — research
**Location (research output):** projects/therapy-compliance-automation/isagawa-feasibility.md

## What it needs to answer
- Can Isagawa build the compliance piece, and how hard is it really (the user believes "easy")?
- Map the eligibility/compliance logic to the **3-layer pattern** from projects/rt-automation/ (Config JSON rules + Python validators + Kernel enforcement) — which checks are:
  - **Deterministic / rule-based** (coverage status, order presence, CPT-vs-charting match, refused-flag) — high confidence, auditable, the strength of the pitch.
  - **Model-assisted / probabilistic** (does the free-text charting support medical necessity for this CPT; does the diagnosis support the intervention) — needs an LLM judge AND a human-review gate (never auto-bill a probabilistic "eligible").
- Where the data comes from (EMR integration? Playwright-driven UI automation like the QA platform / rt-automation? manual export?) and the data-access constraint.
- The audit-trail requirement: every eligibility decision must be explainable + logged (Isagawa attestation/state persistence is a natural fit — cite it as a differentiator, without exposing internals per IP rules).
- Honest effort estimate + the hard parts (EMR access, PHI handling, keeping rules current with CMS changes, liability for a wrong flag).

## Output
A technical feasibility verdict (buildable? how much? biggest risks?) that feeds the consolidated GO/NO-GO. Reference the rt-automation design baseline; do not re-derive it.
