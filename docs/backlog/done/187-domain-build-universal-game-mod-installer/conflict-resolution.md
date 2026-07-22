# Conflict Resolution

## Status
NEW — future enhancement

## What It Does
Detects and handles mod conflicts: file overwrites, load order requirements, and incompatible combinations.

## Conflict Types
| Type | Example | Resolution |
|------|---------|------------|
| File overwrite | Two facepacks both write to `faces/config.xml` | Warn user, let them choose which to keep |
| Load order | Skyrim mods need specific plugin order | Generate load order based on mod metadata |
| Incompatible | Two database mods that change same records | Warn, recommend one |
| Dependency | Mod A requires Mod B installed first | Install dependencies first |

## Implementation
- Track installed files per mod in a manifest
- Before installing, check manifest for conflicts
- For games with load order (Skyrim, Fallout): generate plugins.txt / loadorder.txt
- For games without load order (FM24): last-write-wins with warning

## Dependencies
- Download engine (knows what files each mod installs)
- Game detection (knows which games need load order)
