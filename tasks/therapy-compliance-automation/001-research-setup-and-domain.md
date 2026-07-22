# Task 001: Setup + Domain & Compliance Research
**Type:** RESEARCH | **Gates:** RC-01
## Action
Create projects/therapy-compliance-automation/ (if needed) with a README (scope: RT compliance automation feasibility; CONFIRMED RT; timestamped). Then web-research + write projects/therapy-compliance-automation/domain-and-compliance.md.
## Spec
READ the source docx (projects/therapy-compliance-automation/medicare-part-b-eligibility-source.docx) FIRST. Structure the Medicare Part B RT eligibility logic as rules: eligible-if / do-not-bill-if / the three checks (need, diagnosis-supports-intervention, documentation-supports-CPT) + the diagnosis->intervention->CPT mappings (COPD/asthma->nebulizer; atelectasis/pneumonia->IS/CPT; desat/COPD/CHF/OSA->overnight oximetry). Capture the manual workflow (charting/billing/compliance done by hand, incumbent corrects errors) and rank the human-error modes (wrong CPT, Part A vs B miscoding, missing order/necessity, refused-treatment billed). For EACH rule, mark deterministic vs judgment. Cite CMS/CPT sources with dates.
## Acceptance
domain-and-compliance.md covers rules + workflow + ranked errors + det-vs-judgment, cited. README present.
