# Chusky Launch Video — Successful Production Steps

This log records the production path that produced the current final videos with narration and background music. It includes successful operations and the checks that passed; it omits failed attempts.

Project folder: `videos/chusky-launch/`

## 1. Start from the approved HyperFrames project

- Used the approved storyboard and scene layouts in `STORYBOARD.md`, `index.html`, and the separate portrait and 15-second projects under `deliverables/`.
- Kept the existing Chusky wordmark and supplied Instrument Sans, Instrument Serif, and JetBrains Mono font files.
- Product footage and a booking URL were not available. The reconstructed product scenes remain labeled illustrative; no customer outcomes, personal contact details, or invented URL were added.
- Used the approved three-format plan: 1920×1080 landscape, 1080×1920 portrait, and 1920×1080 15-second cutdown.

## 2. Prepare the audio

### Narration

- Used local Kokoro ONNX speech synthesis with the `am_michael` voice at speed `0.96`.
- Kept the narration in separate WAV clips aligned to the storyboard beats: 10 clips for each 60-second version and 6 for the cutdown.
- Copied the matching clips into each editable project’s `assets/voice/` folder.
- Kept the clean narration in `narration.txt` and the timed captions in `captions.srt` (with separate sidecars for portrait and cutdown).

### Licensed music

- Selected “Meanwhile” by Scott Buckley from the composer’s official library.
- Downloaded the source MP3 to `assets/music/meanwhile-scott-buckley.mp3`:

```powershell
curl.exe -L --fail --retry 2 'https://www.scottbuckley.com.au/library/wp-content/uploads/2025/01/Meanwhile.mp3' -o assets/music/meanwhile-scott-buckley.mp3
```

- The track is offered under CC BY 4.0. Its source, license, required attribution, and edits are recorded in `CREDITS.txt`. The music is trimmed to each video duration, faded at the beginning and end, and mixed beneath narration. Keep the credit with any public release.
- Copied the music asset into the portrait and cutdown projects so each project remains self-contained.
- No sound effects were available or used. The optional sound cues in `AUDIO_CUE_SHEET.md` are suggestions only, not sounds included in these renders.

## 3. Put music and narration into the three timelines

- Used HyperFrames 0.8.168 and FFmpeg 9.0.2.
- Installed the audio carve script’s matching local dependency without changing the project manifest or lockfile:

```powershell
npm install --no-save --package-lock=false @hyperframes/core@0.8.168
```

- Added the music bed and narration clips to each composition. The bed uses a restrained base level, fades, and voiceover carve; the voice clips share a `voiceover` audio group so the music makes room while narration is speaking.
- Generated the voiceover carve with the installed HyperFrames audio skill script. The landscape invocation was:

```powershell
node C:\Users\mseyy\.agents\skills\hyperframes-audio\scripts\carve.mjs --comp index.html --bed el-music-bed --voice el-01-request-voice --voice el-02-mission-voice --voice el-03-research-voice --voice el-04-saved-work-voice --voice el-05-approval-voice --voice el-06-conversation-voice --voice el-07-next-actions-voice --voice el-08-later-voice --voice el-09-summary-voice --voice el-10-end-card-voice
```

- For portrait, used the equivalent `el-vertical-voice-01` through `el-vertical-voice-10` voice IDs from its project folder. For cutdown, used `el-cutdown-voice-01` through `el-cutdown-voice-06`. Those standalone projects used `--core C:\Users\mseyy\Downloads\tg-agent\videos\chusky-launch` to resolve the shared HyperFrames core.
- Recorded the audio metadata and licensing details in `audio_meta.json`, `AUDIO_CUE_SHEET.md`, and `CREDITS.txt`.

## 4. Check each project, then render

Ran the documented HyperFrames check and render commands from each project directory. FFmpeg was available on PATH in the rendering shell.

Check:

```powershell
npx --yes hyperframes@0.8.168 check
```

Render landscape from the project root:

```powershell
npx --yes hyperframes@0.8.168 render --skill=product-launch-video --quality high --output renders/chusky-launch-landscape-60s-music.mp4
```

Render portrait from `deliverables/vertical-1080x1920/`:

```powershell
npx --yes hyperframes@0.8.168 render --skill=product-launch-video --quality high --output renders/chusky-launch-vertical-60s-music.mp4
```

Render the cutdown from `deliverables/cutdown-15s/`:

```powershell
npx --yes hyperframes@0.8.168 render --skill=product-launch-video --quality high --output renders/chusky-launch-cutdown-15s-music.mp4
```

## 5. Successful validation and final files

- HyperFrames checks passed for all three projects. Landscape reported no warnings. Portrait and cutdown passed with 11 and 7 structure lint warnings about dense, self-contained scene markup. All three reported no runtime errors, layout or motion issues, or contrast failures.
- FFprobe confirmed the expected dimensions, durations, 30 fps video, and 48 kHz stereo audio in each final MP4.
- Audio level inspection on the landscape mix confirmed a peak of about -1.3 dBFS and an average overall level of about -25 dBFS. Sampled music-only sections were lower than narration sections, consistent with the intended unobtrusive bed.

Final renders:

- `renders/chusky-launch-landscape-60s-music.mp4`
- `deliverables/vertical-1080x1920/renders/chusky-launch-vertical-60s-music.mp4`
- `deliverables/cutdown-15s/renders/chusky-launch-cutdown-15s-music.mp4`

Supporting script, captions, asset inventory, cue sheet, and attribution are listed in `DELIVERABLES.md`.

