# Gate Contract - 260 About & Hiring Intent

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PA-01 | Section per guide 12: 2-4 sentences about the builder, core technical strengths, EXACT role families targeted (agent runtimes, AI infrastructure, developer tooling, evaluation systems, applied AI architecture), location/work-authorization (Las Vegas NV, US Citizen per profile.json), and resume PDF + LinkedIn + GitHub + email links | grep + html parse | 001 | about + strengths + role families + auth + all 4 links |
| PA-02 | Links resolve: resume PDF present, mailto from profile, GitHub (solosza), LinkedIn (from profile if present) | run_test | 001 | links wired |
| PA-03 | Pushed; Pages rebuilt | run_code | 002 | push clean |
| PA-04 | L3 GATE (cache-busted): live page shows about/hiring section; resume link 200; mailto present; IP-safety + absolute-claims greps clean (strip <style>, check context) | run_test | 003 | live green |

## Rules
- READ guide section 12 + profile.json + current index.html FIRST (RULE ZERO)
- Real data from profile.json - no placeholders; role families exactly per guide sample
- Any red: fix then /kernel/learn
