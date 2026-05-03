# Gate Contract — Portfolio Site (047)

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | index.html exists | file_exists | `test -f D:\my_ai_projects\isagawa-portfolio-site\index.html` | Create file |
| BUILD-02 | styles.css exists | file_exists | `test -f D:\my_ai_projects\isagawa-portfolio-site\styles.css` | Create file |
| BUILD-03 | Hero copy correct | grep | `grep -q "conversational agent factory" D:\my_ai_projects\isagawa-portfolio-site\index.html` | Fix hero copy |
| BUILD-04 | Seed section exists | grep | `grep -q 'id="seed"' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add section |
| BUILD-05 | Growth section exists | grep | `grep -q 'id="growth"' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add section |
| BUILD-06 | Self-Extension section exists | grep | `grep -q 'id="self-extension"' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add section |
| BUILD-07 | This Page section exists | grep | `grep -q 'id="this-page"' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add section |
| BUILD-08 | Provenance section exists | grep | `grep -q 'id="provenance"' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add section |
| BUILD-09 | First attestation bundle embedded | grep | `grep -q 'attestation-bundle-1' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Embed bundle |
| BUILD-10 | Second attestation bundle embedded | grep | `grep -q 'attestation-bundle-2' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Embed bundle |
| BUILD-11 | Rekor verification JS exists | grep | `grep -qi 'rekor' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add JS |
| BUILD-12 | Footer exists | grep | `grep -q '<footer' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add footer |
| BUILD-13 | Old architecture section removed | grep | `! grep -q 'id="architecture"' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Remove old section |
| BUILD-14 | Old kernel-cards CSS removed | grep | `! grep -q '.kernel-cards' D:\my_ai_projects\isagawa-portfolio-site\styles.css` | Remove old CSS |
| BUILD-15 | Responsive rules exist | grep | `grep -q '@media' D:\my_ai_projects\isagawa-portfolio-site\styles.css` | Add responsive |
| BUILD-16 | Smooth scroll enabled | grep | `grep -q 'scroll-behavior' D:\my_ai_projects\isagawa-portfolio-site\styles.css` | Add smooth scroll |
| BUILD-17 | Mobile nav JS exists | grep | `grep -q 'menu-toggle\|hamburger' D:\my_ai_projects\isagawa-portfolio-site\index.html` | Add mobile nav |
| BUILD-18 | Dark background in CSS | grep | `grep -q '\-\-bg-primary.*rgb(0' D:\my_ai_projects\isagawa-portfolio-site\styles.css` | Set dark background |
| FUNC-01 | Page loads without JS errors | run_code | Playwright navigate, check console for errors | Fix errors |
| FUNC-02 | All nav links resolve to sections | run_code | Playwright click each nav link, verify target section exists | Fix nav links |
| FUNC-03 | Provenance cards render (2 cards) | run_code | Playwright find `.attestation-card` elements, count >= 2 | Fix rendering |
| TEST-01 | Desktop layout screenshot | run_code | Playwright screenshot at 1440x900 | Fix layout |
| TEST-02 | Mobile layout screenshot | run_code | Playwright screenshot at 375x812 | Fix responsive |
| TEST-03 | Intent text visible in provenance | run_code | Playwright verify `.intent-text` elements have text content | Fix display |
