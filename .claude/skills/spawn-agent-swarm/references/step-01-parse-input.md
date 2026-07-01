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

## Output

Return ordered list of backlog numbers ready to spawn:
```python
[128, 131, 132]
```
