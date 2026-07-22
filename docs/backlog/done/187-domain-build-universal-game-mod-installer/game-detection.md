# Game Detection

## Status
NEW

## What It Does
Detects installed games on the local system and resolves their mod folder paths. Supports Steam, Epic, GOG, and standalone installations.

## Detection Methods
- **Steam:** Read `libraryfolders.vdf` for install paths, scan `steamapps/common/`
- **Epic:** Read `LauncherInstalled.dat` for install paths
- **GOG:** Check registry entries (Windows) or GOG Galaxy paths
- **Standalone:** Check common install locations, allow user override

## Game Config Schema
```json
{
  "game_id": "fm24",
  "display_name": "Football Manager 2024",
  "detection": {
    "steam_app_id": "2252570",
    "exe_name": "fm.exe",
    "common_paths": ["D:/SteamLibrary/steamapps/common/Football Manager 2024"]
  },
  "mod_folders": {
    "editor_data": "{documents}/Sports Interactive/Football Manager 2024/editor data/",
    "graphics": "{documents}/Sports Interactive/Football Manager 2024/graphics/",
    "skins": "{documents}/Sports Interactive/Football Manager 2024/skins/"
  }
}
```

## Supported Games (Initial)
- Football Manager 2024
- Skyrim Special Edition (Steam Workshop + Nexus)
- Cities: Skylines (Steam Workshop)
- Stardew Valley (SMAPI + Nexus)

## Dependencies
- None — pure filesystem detection
