# Chusky launch film deliverables

## Editable HyperFrames projects

- `index.html` — landscape master, 1920×1080, 30 fps, 60 seconds.
- `deliverables/vertical-1080x1920/` — separately composed portrait master, 1080×1920, 30 fps, 60 seconds.
- `deliverables/cutdown-15s/` — landscape 15-second cutdown, 1920×1080, 30 fps.

## Final rendered MP4s with music

- `renders/chusky-launch-landscape-60s-music.mp4` — 1920×1080, 30 fps, 60 seconds.
- `deliverables/vertical-1080x1920/renders/chusky-launch-vertical-60s-music.mp4` — 1080×1920, 30 fps, 60 seconds.
- `deliverables/cutdown-15s/renders/chusky-launch-cutdown-15s-music.mp4` — 1920×1080, 30 fps, 15 seconds.

Each render contains the Kokoro synthetic voiceover and the licensed music bed “Meanwhile” by Scott Buckley. The bed is faded and ducked under narration. No sound effects are included.

## Music credit and license

The track is offered under Creative Commons Attribution 4.0, which permits commercial use with attribution. Keep `CREDITS.txt` with the project. For YouTube or similar publishing, include its paste-ready credit in the video description. The track is modified for length and mix.

## Script and review

- `STORYBOARD.md` — approved ten-beat storyboard and animation timing.
- `narration.txt` — clean-text 60-second narration.
- `captions.srt` — 60-second caption sidecar, timed to each spoken clip.
- `deliverables/vertical-1080x1920/captions.srt` — portrait caption sidecar.
- `deliverables/cutdown-15s/narration.txt` and `captions.srt` — cutdown script and caption sidecar.
- `ASSET_INVENTORY.md` — supplied, generated, missing, and excluded assets.
- `AUDIO_CUE_SHEET.md` — voiceover and licensed music details; unused optional sound cues.
- `CREDITS.txt` — music attribution, source, license, and changes made.

All reconstructed interface scenes are illustrative and use generic prospect labels. No customer-result claims or personal contact data are present.

## Asset limits

The narration is synthetic (Kokoro ONNX, `am_michael`, speed 0.96). Product footage and a booking URL were not supplied. The video labels simulated interface scenes as illustrative and shows “Book a pilot” without a fabricated URL.

## Validation

HyperFrames 0.8.168 checks passed for all three projects. Landscape has no warnings. Portrait and cutdown retain 11 and 7 lint warnings, respectively, about dense self-contained scene markup; there are no runtime errors, layout or motion issues, or contrast failures.

FFprobe confirms H.264 video at 30 fps, expected dimensions and duration, and 48 kHz stereo audio in each final MP4. Rendering used FFmpeg 9.
