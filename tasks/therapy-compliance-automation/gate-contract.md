# Gate Contract - 269 RT Compliance Automation Research

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| RC-01 | projects/therapy-compliance-automation/domain-and-compliance.md: Medicare Part B RT eligibility logic from the source doc structured as rules (eligible-if / do-not-bill-if / the 3 checks + diagnosis->intervention->CPT mappings); manual workflow + ranked human-error modes; deterministic-vs-judgment split per rule | file_exists + content | 001 | rules + errors + split, cited |
| RC-02 | isagawa-feasibility.md: maps the checks to the 3-layer pattern (ref rt-automation baseline); classifies deterministic (rule) vs model-assisted (LLM+human-review) checks; data-access/EMR + PHI + audit-trail; honest effort estimate + hard parts; technical GO/NO-GO criteria | file_exists + content | 002 | feasibility verdict w/ det-vs-judgment |
| RC-03 | market-and-switching.md: incumbent (manual), switch value levers (denial/clawback reduction, labor, audit-defensibility - quantified w/ cited sources), buyer (admin champion -> owner approver), competitive landscape, and the KILL risks (Medicare billing/false-claim liability, HIPAA/BAA/PHI, EMR friction, CMS drift) | file_exists + content | 003 | market viability + risks, cited |
| RC-04 | go-no-go.md: consolidated GO / NO-GO with an honest explanation synthesizing 001-003; explicit on the liability/human-in-the-loop posture as the make-or-break; if GO, names the next step (business-plan build backlog) | file_exists + content | 004 | clear verdict + rationale |

## Rules
- READ the source docx + projects/rt-automation/ design baseline FIRST (RULE ZERO); do not re-derive the 3-layer pattern
- WebSearch/WebFetch for Medicare Part B RT compliance rules, CPT coding, HIPAA/BAA, false-claim/OIG liability, competitive vendors - cite source + date
- Treat billing-compliance LIABILITY and PHI handling as first-class risks; a probabilistic "eligible" must never auto-bill (human-review gate)
- Honest verdict - feasibility optimism AND market/liability reality; no code build in this pipeline
- Any red (missing dimension / uncited claim) -> fix then /kernel/learn
