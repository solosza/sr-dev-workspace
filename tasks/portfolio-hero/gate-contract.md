# Gate Contract - 251 Portfolio Hero

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PH-01 | Stack badge list verified: every badge tool confirmed present in actual repos (grep evidence per tool recorded in task output); no aspirational tools | run_code | 001 | evidence per badge |
| PH-02 | Resume PDF copied into the repo (e.g. assets/resume.pdf) and linked | file_exists | 002 | PDF present, link wired |
| PH-03 | Hero per guide section 3: name, role identity line, one-line value prop, personal-ownership statement, badge row, Resume/GitHub/LinkedIn/Email buttons, one-line hiring target; Avoid-list clean (no logo-first, no Founder-only, no keyword stuffing) | grep + html parse | 003 | all includes present |
| PH-04 | Pushed to main; Pages rebuild triggered | run_code | 004 | push clean |
| PH-05 | L3 GATE: live https://solosza.github.io/ shows the full hero (poll up to 10 min for rebuild): all buttons resolve (resume PDF 200, mailto present, GitHub/LinkedIn hrefs), badge row rendered, no [INSERT] visible | run_test | 005 | live asserts green |

## Rules
- READ guide section 3 fully + profile.json + the existing index.html BEFORE editing (RULE ZERO)
- Contact links from profile.json (email alain@isagawa.co per profile; GitHub solosza; LinkedIn from profile if present - if absent, omit the button rather than inventing a URL)
- Badge verification: for each guide-example tool (Python, TypeScript, Selenium, Playwright, Docker, Paramiko, pyodbc, Claude Code) grep the user's real repos (hmsa-qa-platform, isagawa-qa platform-selenium path, sr_dev workspace, isagawa-kernel) - include ONLY tools with hits; mssql-python may replace pyodbc if that reflects reality better
- No absolute claims; no kernel internals
- Any red: fix then /kernel/learn
