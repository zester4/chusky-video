# Production steps — Before it goes out

## Successful steps

1. Created the film as an independent HyperFrames subproject at `films/before-it-goes-out/` so the first launch film remains intact.
2. Reused the supplied Chusky wordmark, Instrument Sans, Instrument Serif, and JetBrains Mono files. Kept the monochrome palette and designed a distinct dossier / evidence-led layout.
3. Reused the already licensed “Meanwhile” music track and its CC BY 4.0 attribution; no unsupported sound effects were added.
4. Authored an eight-scene, 90-second storyboard and expanded narration. Every simulated product screen is labeled “Illustrative workflow.”
5. Generated eight local Kokoro `am_michael` WAV clips at speed 0.96. Total spoken audio is about 71 seconds, leaving quiet reading space in the 90-second film.
6. Added a sentence-level SRT caption file and a HyperFrames caption track. Kokoro provides no word timestamps, so captions are timed to each generated clip rather than presented as word-synced.
7. Built frame packets, delegated one scene per worker, assembled the eight sub-compositions, voice, music, and captions through the installed HyperFrames workflow.
8. Corrected the frame 5 timed-element clip classes after the first assembly validation caught the issue; the assembly then passed.

## Local voice setup and workaround

Install the offline dependencies in a temporary environment (they are not committed to the project):

```powershell
py -3.14 -m venv "$env:TEMP\chusky-video-kokoro-venv"
& "$env:TEMP\chusky-video-kokoro-venv\Scripts\python.exe" -m pip install kokoro-onnx soundfile
```

The first CLI TTS attempt reported that `kokoro-onnx` was missing because its Python import probe timed out on this machine. The package is present in the temporary environment, but importing it took about 31 seconds, beyond the CLI probe's 10-second limit. The successful route used the Kokoro Python API once for the eight lines:

```powershell
& "$env:TEMP\chusky-video-kokoro-venv\Scripts\python.exe" tools\generate_voiceover.py
```

The model and voice files must already exist in `~/.cache/hyperframes/tts/`. Generated speech files live in `assets/voice/`; the script writes measured clip durations to `kokoro_voice_durations.json`.

## Build and review commands

Run from this folder using the pinned project version:

```powershell
node C:\Users\mseyy\.agents\skills\product-launch-video\scripts\frame-packets.mjs --project .
node C:\Users\mseyy\.agents\skills\product-launch-video\scripts\captions.mjs build --storyboard STORYBOARD.md --audio-meta audio_meta.json --hyperframes .
node C:\Users\mseyy\.agents\skills\product-launch-video\scripts\assemble-index.mjs --storyboard STORYBOARD.md --audio-meta audio_meta.json --hyperframes .
npx --yes hyperframes@0.8.168 check --snapshots
npx --yes hyperframes@0.8.168 snapshot --composition main --frames 8
npx --yes hyperframes@0.8.168 preview --background
```

The final MP4 must be rendered only after the user reviews the Studio preview and approves. This version has not been rendered yet.
