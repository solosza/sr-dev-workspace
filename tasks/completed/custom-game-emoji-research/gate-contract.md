# Gate Contract — Custom Game Emoji Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/custom-game-emoji-research/` | Create dir |
| DOC-01 | Existing icon sets doc exists | file_exists | `test -f projects/custom-game-emoji-research/01-existing-icon-sets.md` | Create file |
| DOC-02 | Icon sets doc covers game-icons.net | grep | `grep -q 'game-icons.net' projects/custom-game-emoji-research/01-existing-icon-sets.md` | Add content |
| DOC-03 | Icon sets doc covers itch.io | grep | `grep -q 'itch.io' projects/custom-game-emoji-research/01-existing-icon-sets.md` | Add content |
| DOC-04 | Gap analysis doc exists | file_exists | `test -f projects/custom-game-emoji-research/02-gap-analysis.md` | Create file |
| DOC-05 | Gap analysis references D&D engine | grep | `grep -qi 'dnd\|dungeon\|d&d\|grid' projects/custom-game-emoji-research/02-gap-analysis.md` | Add content |
| DOC-06 | Sales channels and pricing doc exists | file_exists | `test -f projects/custom-game-emoji-research/03-sales-channels-pricing.md` | Create file |
| DOC-07 | Pricing doc has concrete price examples | grep | `grep -qE '\\\$[0-9]|price|pricing' projects/custom-game-emoji-research/03-sales-channels-pricing.md` | Add data |
| DOC-08 | Production pipeline doc exists | file_exists | `test -f projects/custom-game-emoji-research/04-production-pipeline.md` | Create file |
| DOC-09 | Pipeline doc covers AI art tools | grep | `grep -qi 'midjourney\|dall-e\|stable diffusion\|AI' projects/custom-game-emoji-research/04-production-pipeline.md` | Add content |
| DOC-10 | Discord emoji angle doc exists | file_exists | `test -f projects/custom-game-emoji-research/05-discord-emoji-angle.md` | Create file |
| DOC-11 | Discord doc covers monetization angle | grep | `grep -qi 'discord\|monetiz\|revenue' projects/custom-game-emoji-research/05-discord-emoji-angle.md` | Add content |
| DOC-12 | Final research report exists | file_exists | `test -f projects/custom-game-emoji-research/research-report.md` | Create file |
| DOC-13 | Report has build/partner/skip recommendation | grep | `grep -qi 'build\|partner\|skip\|recommend\|decision' projects/custom-game-emoji-research/research-report.md` | Add recommendation |
| DOC-14 | Report references D&D engine use case | grep | `grep -qi 'dnd\|d&d\|dungeon\|grid' projects/custom-game-emoji-research/research-report.md` | Add content |

## Requirements Coverage
- BUILD-01 → task 001 (create project dir)
- DOC-01, DOC-02, DOC-03 → task 002 (existing icon sets research)
- DOC-04, DOC-05 → task 003 (gap analysis)
- DOC-06, DOC-07 → task 004 (sales channels and pricing)
- DOC-08, DOC-09 → task 005 (production pipeline)
- DOC-10, DOC-11 → task 006 (Discord emoji angle)
- DOC-12, DOC-13, DOC-14 → task 007 (final research report)
