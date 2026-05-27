# L2 Desktop Visual QA

## Type
TEST

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## Acceptance Criteria
1. Start HTTP server: `python -m http.server 8847` in deliverable root
2. Navigate Playwright to `http://localhost:8847` at 1440x900
3. Take full-page screenshot
4. Verify visually:
   - Hero h1 is large with visible gradient
   - Section numbers (01-04) are massive and nearly invisible
   - Cards have visible borders and spacing
   - Footer has 4 columns
   - Three attestation cards in provenance section
   - Chain list has visual weight
   - Bold emphasis visible in prose paragraphs
   - Tag labels visible above card titles
5. Kill HTTP server

## Gates
TEST-01
