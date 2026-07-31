# Gate Contract: Render Integration

Paths relative to repo root `D:/my_ai_projects/project_test_repos/sr_dev_workspace`. Skill root shorthand `R = .claude/skills/render`.

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Adapter module exists | file_exists | `test -f R/adapters/loop_to_leaderboard.py` | Create file |
| BUILD-02 | Adapter has a to_items function | grep | `grep -qE 'def (to_items|build_items|adapt)' R/adapters/loop_to_leaderboard.py` | Add function |
| BUILD-03 | Adapter has a jargon ban-list | grep | `grep -qiE 'wedge|jargon|ban' R/adapters/loop_to_leaderboard.py` | Add plain-vocab guard |
| BUILD-04 | Adapter INDEX exists | file_exists | `test -f R/adapters/INDEX.md` | Create file |
| BUILD-05 | Launcher exists | file_exists | `test -f R/lib/serve_and_watch.py` | Create file |
| BUILD-06 | Launcher has no print() | run_code | `! grep -nE '(^|\s)print\(' R/lib/serve_and_watch.py` | Remove debug prints (write to file) |
| BUILD-07 | Render-step spec exists | file_exists | `test -f R/steps/step-serve-and-watch.md` | Create file |
| BUILD-08 | Routing spec exists | file_exists | `test -f R/steps/step-route-annotations.md` | Create file |
| FUNC-01 | Adapter emits schema-valid items.json | run_code | sample loop output → items.json has title+items[] with id,rank,name,desc,rec,tag | Fix adapter |
| FUNC-02 | Adapter output has no em dash | run_code | emitted JSON contains no `—` / `--` em usage | Fix strings |
| FUNC-03 | Launcher generates page.html | run_code | serve_and_watch produces page.html in session dir | Fix launcher |
| FUNC-04 | Server serves the page | run_code | GET / returns 200 with the leaderboard title | Fix serve |
| FUNC-05 | Server teardown leaves no listener | run_code | after teardown, port not listening | Fix teardown |
| TEST-01 | Adapter functional test passes | run_test | task 006 verification exits 0 | Fix adapter |
| TEST-02 | Launcher serve test passes | run_test | task 007 verification exits 0 | Fix launcher |
| TEST-03 | E2E render test passes | run_test | task 008 verification exits 0 | Fix flow |
| WIRE-01 | assay references render step | grep | `grep -q 'step-serve-and-watch' R/../assay/**` | Add pointer |
| WIRE-02 | competition references render step | grep | competition SKILL references step-serve-and-watch | Add pointer |
| WIRE-03 | deep-dive references render step | grep | deep-dive SKILL references step-serve-and-watch | Add pointer |
| WIRE-04 | expand references render step | grep | expand SKILL references step-serve-and-watch | Add pointer |
| WIRE-05 | small references render step | grep | small SKILL references step-serve-and-watch | Add pointer |
| WIRE-06 | lateral references render step | grep | lateral SKILL references step-serve-and-watch | Add pointer |
| WIRE-07 | source references render step | grep | source SKILL references step-serve-and-watch | Add pointer |
| DOC-01 | Plan-shaped loops documented | grep | render templates/INDEX.md notes offer/gtm/launch/operate need own template | Add note |
| TEST-04 | Wiring grep test passes | run_test | task 017 verification exits 0 | Fix wiring |
