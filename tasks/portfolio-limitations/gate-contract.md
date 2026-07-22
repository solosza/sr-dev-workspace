# Gate Contract - 259 Current Limitations

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| PL-01 | Section per guide 11: public-safe limitations (executor dependence, incomplete external benchmarking, model-assisted semantic review, ongoing concurrency hardening) + a short 'current work' list; factual tone (sample copy: 'early-stage proprietary implementation exercised extensively by its builder; external reproduction, broader executor support, comparative benchmarking are active validation areas') | grep | 001 | limitations + current-work list present |
| PL-02 | Avoid clean: no security-sensitive weaknesses, no apologetic tone, no calling planned features completed | run_test | 001 | 0 hits |
| PL-03 | Pushed; Pages rebuilt | run_code | 002 | push clean |
| PL-04 | L3 GATE (cache-busted): live page shows the limitations section; IP-safety + absolute-claims greps clean (exclude <style> blocks + check context - lessons 255/256/258) | run_test | 003 | live green |

## Rules
- READ guide section 11 + current index.html FIRST (RULE ZERO); factual not apologetic
- Do NOT expose exploitable/security-sensitive detail; do NOT call planned features done
- Any red: fix then /kernel/learn
