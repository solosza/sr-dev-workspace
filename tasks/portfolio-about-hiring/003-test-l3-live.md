# Task 003: L3 - Live (GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives.
**Gates:** PA-04
## Action
ONE script: poll https://solosza.github.io/?cb=260 up to 10 min; assert about/hiring section + role families + location/auth present; resume PDF URL returns 200; mailto present; strip <style>; kernel-internal grep 0; absolute-claims grep - context-checked (ignore CSS 100%).
## Acceptance
Live asserts PASS, exit 0. Red: fix then /kernel/learn.
