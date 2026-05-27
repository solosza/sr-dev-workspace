# Gate Contract — Multi-Model Routing

## Gates

| Gate | Criteria | Verification |
|------|----------|--------------|
| G1 | model-routing-config.json exists and is valid JSON | `python -c "import json; json.load(open('lib/model-routing-config.json'))"` exits 0 |
| G2 | model-router.sh exists and is sourceable | `bash -c "source lib/model-router.sh && type route_model"` exits 0 |
| G3 | run-task.sh calls route_model before claude -p | `grep -q 'route_model' run-task.sh` exits 0 |
| G4 | run-task.sh passes --model to claude | `grep -q '\-\-model' run-task.sh` exits 0 |
| G5 | Router returns valid model IDs | Test script returns opus/sonnet/haiku model IDs for sample tasks |
| G6 | Existing task execution not broken | run-task.sh still works without model-routing-config.json (fallback to opus) |
