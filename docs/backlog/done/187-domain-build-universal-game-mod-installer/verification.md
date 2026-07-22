# Verification

## Status
NEW

## What It Does
After installation, verifies that mod files are in the correct locations, have expected sizes, and produces a summary report.

## Verification Checks
| Check | Method |
|-------|--------|
| Files exist | `test -f` on expected paths |
| File sizes reasonable | Compare to expected size from download |
| No empty files | Check file size > 0 |
| Config files valid | Parse XML/JSON config files where applicable |
| Game launches | Optional — launch game and check for mod menu/load screen |

## Report Format
```
MOD INSTALLATION COMPLETE

Game: Football Manager 2024
Install path: D:/SteamLibrary/steamapps/common/Football Manager 2024
Mod folder: C:/Users/solos/Documents/Sports Interactive/Football Manager 2024

Installed:
  ✓ Sortitoutsi Data Update (62 .fmf files)
  ✓ Japan Database Fix (3 .fmf files)
  ✓ Cut-Out Faces Megapack (550,000 faces)
  ✓ FMG Standard Logos (84,000 logos)
  ✓ SAS24 Skin
  ✓ Daveincid Increase Realism

Warnings:
  ⚠ Japan.fmf from Data Update may conflict with Japan Database Fix

Action required:
  Start a NEW game to apply editor data changes.
```

## Dependencies
- Game detection (for paths)
- Download engine (for file manifest)
