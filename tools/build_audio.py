#!/usr/bin/env python3
"""Record the tapes: tapes.py -> docs/audio/*.mp3 + docs/data/tapes.json

Voice: Kokoro TTS (kokoro-v1.0.onnx + voices-v1.0.bin in tools/voices/).
Then a cassette chain: band-limit, light saturation, wow and flutter, hiss.

Usage:  python3 tools/build_audio.py [--voice bm_george] [--only ID ...] [--fx-only]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
from scipy.signal import butter, sosfilt

sys.path.insert(0, str(Path(__file__).parent))
from tapes import S, ORDER, START, COURSE  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = ROOT / "docs" / "audio"
DATA_DIR = ROOT / "docs" / "data"
VOICES = ROOT / "tools" / "voices"

SR = 24000
SPEED = 1.0           # the instructor
SPEED_SAY = 0.88      # lines the student repeats: dictation pace
LEADER = 1.4          # blank tape before he speaks
AFTER_NUMBER = 0.7    # pause after "Tape five." Every version of a tape is identical up to here
RUNOUT = 1.0          # blank tape after he stops, then the deck shuts off
HISS = 0.0050

# The phonemizer reads a lone capital A as the article. Respell the letter.
LETTER_A = re.compile(r"(?<=\b(?:an|An|no|No) )A\b|(?<=\b(?:the|The) )A\b")


def synth_factory(voice: str):
    from kokoro_onnx import Kokoro
    k = Kokoro(str(VOICES / "kokoro-v1.0.onnx"), str(VOICES / "voices-v1.0.bin"))
    lang = "en-gb" if voice[0] == "b" else "en-us"
    cache: dict = {}

    def synth(text: str, speed: float) -> np.ndarray:
        key = (text, speed)
        if key not in cache:
            spoken = LETTER_A.sub("eh", text)
            samples, sr = k.create(spoken, voice=voice, speed=speed, lang=lang)
            assert sr == SR, f"unexpected sample rate {sr}"
            cache[key] = samples.astype(np.float32)
        return cache[key]

    return synth


def silence(sec: float) -> np.ndarray:
    return np.zeros(int(SR * sec), dtype=np.float32)


def bandpass(x, lo, hi, order=2):
    sos = butter(order, [lo, hi], btype="bandpass", fs=SR, output="sos")
    return sosfilt(sos, x).astype(np.float32)


def knock(freq: float, dur: float, level: float, seed: int) -> np.ndarray:
    """One plastic-on-plastic knock: a damped thump under a short rattle."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = np.arange(n, dtype=np.float32) / SR
    thump = np.sin(2 * np.pi * freq * t) * np.exp(-t * 55)
    rattle = bandpass(rng.standard_normal(n), 900, 4200) * np.exp(-t * 140)
    return ((thump * 0.9 + rattle * 0.5) * level).astype(np.float32)


def fx_key() -> np.ndarray:
    """A piano key latching down."""
    return np.concatenate([knock(95, 0.11, 0.9, 1), silence(0.03)])


def fx_stop() -> np.ndarray:
    """The key springing back up: lighter, two-part."""
    return np.concatenate([knock(140, 0.05, 0.5, 2), silence(0.025), knock(110, 0.09, 0.7, 3)])


def fx_swap() -> np.ndarray:
    """Door open, cassette out, cassette in, door shut."""
    rng = np.random.default_rng(4)
    n = int(SR * 0.16)
    t = np.arange(n, dtype=np.float32) / SR
    slide = bandpass(rng.standard_normal(n), 1500, 5000) * np.sin(np.pi * t / t[-1]) * 0.10
    return np.concatenate([
        knock(170, 0.07, 0.6, 5), silence(0.07), slide.astype(np.float32), silence(0.05),
        knock(210, 0.05, 0.45, 6), silence(0.09), slide[::-1].astype(np.float32), silence(0.04),
        knock(120, 0.10, 0.8, 7), silence(0.05),
    ])


def fx_rew() -> np.ndarray:
    """Rewind: spool whine rising, then the clunk at the start of the tape."""
    rng = np.random.default_rng(8)
    n = int(SR * 0.62)
    t = np.arange(n, dtype=np.float32) / SR
    f = 260 + 520 * (t / t[-1]) ** 1.6
    whine = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.10
    hush = bandpass(rng.standard_normal(n), 700, 3800) * 0.12
    env = np.minimum(1, t / 0.05) * np.minimum(1, (t[-1] - t) / 0.03)
    return np.concatenate([((whine + hush) * env).astype(np.float32), knock(100, 0.10, 0.8, 9), silence(0.04)])


def band_limit(x: np.ndarray) -> np.ndarray:
    sos_hp = butter(2, 160, btype="highpass", fs=SR, output="sos")
    sos_lp = butter(4, 5600, btype="lowpass", fs=SR, output="sos")
    return sosfilt(sos_lp, sosfilt(sos_hp, x)).astype(np.float32)


def saturate(x: np.ndarray) -> np.ndarray:
    k = 1.5
    return (np.tanh(k * x) / np.tanh(k)).astype(np.float32)


def wow(x: np.ndarray, seed: int) -> np.ndarray:
    """Speed drift of a worn transport: slow wow plus a little flutter."""
    n = np.arange(len(x), dtype=np.float64)
    ph = seed * 0.7
    drift = 9.0 * np.sin(2 * np.pi * 0.55 * n / SR + ph) + 0.35 * np.sin(2 * np.pi * 6.8 * n / SR + ph * 2)
    return np.interp(n + drift, n, x).astype(np.float32)


def hiss_bed(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    noise = bandpass(rng.standard_normal(n), 500, 7000, order=1)
    hum = 0.25 * np.sin(2 * np.pi * 50 * np.arange(n, dtype=np.float32) / SR)
    return ((noise + hum) * HISS).astype(np.float32)


def assemble(seg: dict, synth):
    """Returns (dry audio, time the versions of this tape start to differ,
    page-turn time or None, transcript lines as [start, end, text, is_say])."""
    chunks = [silence(LEADER)]
    lines = []
    at = lambda: sum(len(c) for c in chunks) / SR

    def speak(text, speed, say=0):
        t0 = at()
        chunks.append(synth(text, speed))
        lines.append([round(t0, 2), round(at(), 2), text, say])

    parts = list(seg["parts"])
    # "Tape five. They said no." -> announce the number on its own, then wait.
    head, sep, rest = parts[0].partition(". ")
    if head.startswith("Tape ") and sep:
        speak(head + ".", SPEED)
        chunks.append(silence(AFTER_NUMBER))
        parts[0] = rest
    else:
        speak(parts.pop(0), SPEED)
        chunks.append(silence(0.18))
    safe_until = at()
    page_at = None
    for part in parts:
        if isinstance(part, str):
            speak(part, SPEED)
            chunks.append(silence(0.18))
        elif part[0] == "say":
            speak(part[1], SPEED_SAY, 1)
        elif part[0] == "beat":
            chunks.append(silence(float(part[1])))
        elif part[0] == "page":
            page_at = at()
        else:
            raise ValueError(f"unknown part {part!r}")
    chunks.append(silence(RUNOUT))
    return np.concatenate(chunks), safe_until, page_at, lines


def master(x: np.ndarray, seed: int) -> np.ndarray:
    speech = saturate(wow(band_limit(x), seed) * 1.2)
    peak = float(np.max(np.abs(speech))) or 1.0
    out = speech / peak * 0.82 + hiss_bed(len(speech), seed)
    out = np.concatenate([out, fx_stop() * 0.7])       # end of tape: the deck shuts off
    f = int(SR * 0.04)
    out[:f] *= np.linspace(0, 1, f, dtype=np.float32)
    return out.astype(np.float32)


def encode_mp3(x: np.ndarray, path: Path, bitrate: int = 64) -> None:
    import lameenc
    enc = lameenc.Encoder()
    enc.set_bit_rate(bitrate)
    enc.set_in_sample_rate(SR)
    enc.set_channels(1)
    enc.set_quality(2)
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2").tobytes()
    path.write_bytes(bytes(enc.encode(pcm) + enc.flush()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--only", nargs="*", default=None, help="re-record these segment ids")
    ap.add_argument("--fx-only", action="store_true")
    args = ap.parse_args()

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for name, make in (("key", fx_key), ("stop", fx_stop), ("swap", fx_swap), ("rew", fx_rew)):
        encode_mp3(make() * 0.8, AUDIO_DIR / f"fx-{name}.mp3", bitrate=96)
    if args.fx_only:
        return

    manifest_path = DATA_DIR / "tapes.json"
    manifest = {"segs": {}}
    if args.only and manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())

    synth = synth_factory(args.voice)
    for i, sid in enumerate(ORDER):
        if args.only and sid not in args.only:
            continue
        seg = S[sid]
        fname = f"{i + 1:02d}.mp3"
        dry, safe_until, page_at, lines = assemble(seg, synth)
        final = master(dry, seed=i + 11)
        encode_mp3(final, AUDIO_DIR / fname)
        entry = {
            "tape": seg["tape"],
            "next": seg["next"],
            "file": f"audio/{fname}",
            "dur": round(len(final) / SR, 2),
            "safe": round(safe_until - 0.25, 2),
            "lines": lines,
        }
        if seg["art"]:
            entry["art"] = seg["art"]
            entry["page"] = round(page_at, 2)
        manifest["segs"][sid] = entry
        print(f"[{sid:>10}] {fname}  {entry['dur']:5.1f}s", flush=True)

    manifest["course"] = COURSE
    manifest["start"] = START
    manifest["segs"] = {sid: manifest["segs"][sid] for sid in ORDER if sid in manifest["segs"]}
    manifest_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    total = sum(s["dur"] for s in manifest["segs"].values())
    print(f"done: {len(manifest['segs'])} recordings, {total / 60:.1f} min")


if __name__ == "__main__":
    main()
