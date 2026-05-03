# Gate Contract — Autonomous Game Content Pipeline

| Gate ID | Task | Method | Check | Expected |
|---------|------|--------|-------|----------|
| RESEARCH-01 | 004 | file_exists | `projects/game-content-pipeline/autonomous-game-content-research.md` | exists |
| RESEARCH-02 | 004 | grep | `grep -c "Recommended" projects/game-content-pipeline/autonomous-game-content-research.md` | >= 1 |
