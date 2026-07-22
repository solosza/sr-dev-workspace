# Task 003: L3 - Live (GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives.
**Gates:** PL-04
## Action
ONE script: poll https://solosza.github.io/?cb=259 up to 10 min; assert limitations section + current-work list present; strip <style> blocks before grepping; kernel-internal grep 0; absolute-claims grep - print match CONTEXT, only fail on real claims language (ignore CSS 100%).
## Acceptance
Live asserts PASS, exit 0. Red: fix then /kernel/learn.
