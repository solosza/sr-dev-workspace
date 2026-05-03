# Write Attorney Outreach Document

## Type
BUILD

## Description
Create the attorney outreach template — what to say when contacting qui tam firms, what to share, what to hold back (seal requirements).

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\research\attorney-outreach.md` with:
- **Intro pitch**: Isagawa has built an AI system that autonomously scans federal spending data and generates evidence packages for potential FCA violations
- **What we offer**: Pre-built evidence packages with sourced citations from 8+ public databases, cross-referenced and scored
- **What we need**: Attorney to file qui tam complaints, handle seal requirements, manage government intervention process
- **Fee structure proposal**: Standard contingency (25-40% of our share), or discuss fixed fee for initial review
- **Questions for attorney**:
  - Do you accept AI-generated evidence packages?
  - What's your minimum case size threshold?
  - How do you handle the 60-day seal/intervention period?
  - Can you file in multiple federal districts?
  - Do you handle both FCA and FinCEN filings?
- **Seal warning**: Do NOT share specific entity names or evidence details until engagement letter is signed — seal violation risk

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/research/attorney-outreach.md`
- [ ] `grep -q "seal" D:/my_ai_projects/fraud-detection-app/research/attorney-outreach.md`
- [ ] `grep -q "contingency" D:/my_ai_projects/fraud-detection-app/research/attorney-outreach.md`
