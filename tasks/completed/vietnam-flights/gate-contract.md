# Gate Contract — Vietnam Flights

## Gates

| ID | Check | Method | Task |
|----|-------|--------|------|
| BUILD-01 | projects/vietnam-trip/ directory exists | file_exists | 001 |
| RESEARCH-01 | flight1-hnd-sgn.md contains airline + price + arrival time | grep | 002 |
| RESEARCH-02 | flight2-dad-lax.md contains Starlux 704 or alternative | grep | 003 |
| BUILD-02 | recommendation.md exists with both flights summarized | file_exists | 004 |
