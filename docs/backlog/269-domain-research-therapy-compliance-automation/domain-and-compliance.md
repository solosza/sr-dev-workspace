# Domain & Compliance Logic

**Status:** NEW — research
**Location (research output):** projects/therapy-compliance-automation/domain-and-compliance.md
**Source of truth:** projects/therapy-compliance-automation/medicare-part-b-eligibility-source.docx (READ FIRST)

## What it needs to capture
- The eligibility decision logic from the source doc, structured as rules:
  - **Eligible-if** set (SNF not under Part A skilled stay / Part B coverage; valid MD/NP order; supporting diagnosis + medical necessity; skilled service required; documentation of findings/intervention/response/continued need).
  - **Do-NOT-bill-if** set (active Part A covered stay; no active Part B/payor; no order; no diagnosis/necessity; treatment refused; charting does not support the CPT; routine/custodial/not-skilled; CPT requires manual/physician review).
  - The **three checks**: (1) need for the therapy, (2) diagnosis supports the intervention, (3) documentation supports billing the CPT code.
  - The eligible-service examples + diagnosis->intervention mappings (e.g., COPD/asthma/SOB -> nebulizer; atelectasis/pneumonia/weak cough -> IS/CPT; desat/COPD/CHF/OSA -> overnight oximetry).
- The **manual workflow today**: who does charting, who does billing, who does compliance checks, where the incumbent corrects errors by hand.
- The **human-error modes** the PTs/RTs report (wrong CPT for the charting, billing under Part A when it should be Part B, missing order, missing medical necessity, refused-treatment billed) — these are the accuracy value prop.
- RT-vs-PT resolution: confirm the discipline; if PT, the eligibility rules + CPT set differ (research the PT Part B equivalents) and note the source doc is RT-specific.

## Output
A structured compliance-rules document: the decision tree, the deterministic-vs-judgment split per rule, and the top error modes ranked by frequency/impact (the "why automate" evidence).
