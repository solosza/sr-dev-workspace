# Task 001: IP-Safe Disclosure Audit (section 13)
**Type:** TEST | **Gates:** RS-01
## Action
ONE script: fetch the full live https://solosza.github.io/ (cache-busted) AND scan the portfolio-site repo. Grep for keep-private terms: state-schema field names, hook filenames/event names (session_state, universal-gate-enforcer, KERNEL_AGENT_ID, PreCompact, run-task.sh, actions.jsonl), command protocol names, meta-factory/domain-compilation terms, private absolute paths, internal repo identifiers. Strip <style> blocks; for any hit, print CONTEXT and classify real-leak vs benign.
## Acceptance
0 real leaks (each hit context-verified benign or fixed). Exit 0. Red: fix live page then /kernel/learn.
