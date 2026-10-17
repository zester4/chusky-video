# Chusky Video

Standalone HyperFrames source project for the Chusky launch video.

## Project contents

- `index.html` — editable 60-second landscape composition.
- `deliverables/vertical-1080x1920/` — editable vertical composition and render.
- `deliverables/cutdown-15s/` — editable 15-second cutdown and render.
- `assets/`, `boards/`, `compositions/`, and `capture/` — source media and project material.
- `renders/` — final landscape render.
- `STORYBOARD.md`, `SCRIPT.md`, `narration.txt`, and `captions.srt` — production text and captions.
- `DELIVERABLES.md`, `ASSET_INVENTORY.md`, `AUDIO_CUE_SHEET.md`, `CREDITS.txt`, and `PRODUCTION_STEPS.md` — delivery and production records.

## Working with the project

The project uses HyperFrames 0.8.168. Open a PowerShell terminal in the relevant project folder and run:

```powershell
npx --yes hyperframes@0.8.168 check
npx --yes hyperframes@0.8.168 preview
```

Render with the command documented in `PRODUCTION_STEPS.md`. FFmpeg and FFprobe must be available on PATH for renders and media checks.

## Music attribution

The videos use “Meanwhile” by Scott Buckley under CC BY 4.0. Preserve `CREDITS.txt` and include the supplied attribution when publishing.

## Scope

The simulated product interface is illustrative. Product footage and a booking URL were not supplied. See `ASSET_INVENTORY.md` for the asset record and `DELIVERABLES.md` for render specifications and validation notes.
