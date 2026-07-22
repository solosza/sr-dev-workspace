# Step 1: Parse Input

Parse the user input to extract backlog numbers. Two modes:

## Direct Numbers Mode

**Input:** Space-separated backlog numbers
```
/spawn-agent-swarm 128 131 132
/spawn-agent-swarm 125 126 127 129 130
```

**Processing:**
1. Split input by whitespace
2. Validate each is a number
3. Return list of backlog numbers

## File Mode

**Input:** Path to file containing backlog numbers
```
/spawn-agent-swarm backlogs-to-run.txt
```

**Processing:**
1. Read file
2. Extract lines (one backlog number per line, ignore comments `#`)
3. Validate each is a number
4. Return list of backlog numbers

## Validation

For each extracted backlog number:

1. **Number validation:** Must be numeric (1-999)
2. **Backlog exists:** Check `docs/backlog/{N}-*.md` exists
3. **Not already archived:** Backlog should not be in `docs/backlog/done/`
4. **Not already running:** Check `agent-swarm.json` — number shouldn't be in active list

**Error cases:**
- Invalid number → reject with error message
- Backlog doesn't exist → ask user to create it first
- Already archived → skip with warning
- Already running → skip with warning

## Wave Sorting (DAG Support)

After validating backlog numbers, extract execution waves from task dependencies (if declared):

**For each backlog number:**
1. **Resolve task folder:** Glob `docs/backlog/{N}-*.md`, read the backlog file, extract `Location:` field
2. **Read task index:** Open `{location}/000-index.md` from resolved folder
3. **Parse dependencies:** Extract `Dependencies` column from task table (see `01-metadata-and-sorting.md`)
   - If column missing or all `none` → single wave (backward compatible)
   - If dependencies declared → parse adjacency list
4. **Run Kahn's algorithm:** Topological sort with cycle detection via `lib/wave_sort.get_waves()`
5. **Error on cycle:** If cycle detected, reject with clear error BEFORE spawning any agents

**Wave output structure:**
```python
{
  "wave_plan": [
    {
      "wave_id": 0,
      "backlog": 128,
      "task_folder": "tasks/reference-tests-db/",
      "tasks": [1, 2, 3]
    },
    {
      "wave_id": 1,
      "backlog": 128,
      "task_folder": "tasks/reference-tests-db/",
      "tasks": [4, 5]
    }
  ]
}
```

**Backward compatibility:** Backlogs without dependency declarations produce a single wave (all tasks together). Current flat-parallel behavior unchanged.

## Output

Return ordered list of backlog numbers and wave plan:
```python
{
  "backlogs": [128, 131, 132],
  "wave_plan": [
    {"wave_id": 0, "backlog": 128, "task_folder": "tasks/reference-tests-db/", "tasks": [1, 2, 3]},
    {"wave_id": 1, "backlog": 128, "task_folder": "tasks/reference-tests-db/", "tasks": [4, 5]},
    {"wave_id": 0, "backlog": 131, "task_folder": "tasks/other-project/", "tasks": [1, 2, 3, 4, 5]},
    {"wave_id": 0, "backlog": 132, "task_folder": "tasks/another-project/", "tasks": [1, 2]}
  ]
}
```
