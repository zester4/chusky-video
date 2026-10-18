from __future__ import annotations

import json
import os
from pathlib import Path

import soundfile as sf
from kokoro_onnx import Kokoro

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path.home() / ".cache" / "hyperframes" / "tts"
MODEL = CACHE / "models" / "kokoro-v1.0.onnx"
VOICES = CACHE / "voices" / "voices-v1.0.bin"
VOICE = "am_michael"
SPEED = 0.96
LINES = [
    "You give Chusky a goal. It can begin the research, gather the evidence, and bring the work back to you in a form you can review.",
    "It starts by looking for people who fit the brief, then checks the reasons behind each match. The list is built from the research, not guesswork.",
    "Each entry gets the useful context: what the company does, why it may fit, and what still needs your judgment. The sources stay close to the work.",
    "From there, Chusky prepares a first message for each person, using the details it found. The drafts are saved in the workspace your team already uses.",
    "And then it pauses. The messages are ready, but this mission is waiting for your approval before anything is sent.",
    "You can review each draft, make changes, approve the next step, or hold the work. Chusky keeps that decision attached to the mission.",
    "Once approved, the follow-up can be scheduled. The record shows what was prepared, what you authorized, when the next step is due, and the evidence behind it.",
    "Your team stays in control while the work keeps moving. Chusky. Give it the goal. Keep your authority.",
]


def main() -> None:
    if not MODEL.is_file() or not VOICES.is_file():
        raise FileNotFoundError(
            "Kokoro model files are missing from ~/.cache/hyperframes/tts; run the HyperFrames TTS setup first."
        )
    out_dir = ROOT / "assets" / "voice"
    out_dir.mkdir(parents=True, exist_ok=True)
    model = Kokoro(str(MODEL), str(VOICES))
    records = []
    for index, text in enumerate(LINES, start=1):
        samples, sample_rate = model.create(text, voice=VOICE, speed=SPEED)
        path = out_dir / f"{index:02d}.wav"
        sf.write(path, samples, sample_rate)
        duration = len(samples) / sample_rate
        records.append(
            {
                "frame": index,
                "path": path.relative_to(ROOT).as_posix(),
                "duration_s": round(duration, 3),
                "words": [],
            }
        )
        print(f"{index:02d}: {duration:.2f}s → {path.name}", flush=True)
    (ROOT / "kokoro_voice_durations.json").write_text(
        json.dumps(records, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
