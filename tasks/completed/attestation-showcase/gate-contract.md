## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Feature branch exists | run_code | `git -C D:/my_ai_projects/isagawa-co.github.io branch --list feature/showcase-attestation` returns non-empty | Create branch |
| BUILD-02 | attestation.css exists | file_exists | `test -f D:/my_ai_projects/isagawa-co.github.io/attestation.css` | Create file |
| BUILD-03 | CSS uses design variables | grep | `grep -q '\-\-bg-primary' D:/my_ai_projects/isagawa-co.github.io/attestation.css` | Fix CSS |
| BUILD-04 | attestation.html exists | file_exists | `test -f D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Create file |
| BUILD-05 | HTML has hero section | grep | `grep -q 'Prove your AI agent' D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Add hero |
| BUILD-06 | HTML has how-it-works | grep | `grep -q 'How It Works' D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Add section |
| BUILD-07 | HTML has bundle anatomy | grep | `grep -q 'predicateType' D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Add section |
| BUILD-08 | HTML has setup steps | grep | `grep -q 'pip install sigstore' D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Add section |
| BUILD-09 | HTML links feed-count.txt | grep | `grep -q 'feed-count.txt' D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Add counter |
| BUILD-10 | HTML links back to index | grep | `grep -q 'index.html' D:/my_ai_projects/isagawa-co.github.io/attestation.html` | Add nav |
| BUILD-11 | index.html attestation link | grep | `grep -q 'attestation.html' D:/my_ai_projects/isagawa-co.github.io/index.html` | Update link |
| FUNC-01 | CSS under 300 lines | run_code | `test $(wc -l < D:/my_ai_projects/isagawa-co.github.io/attestation.css) -lt 300` | Condense |
| TEST-01 | Page loads without errors | manual | Playwright screenshot shows content | Fix page |
