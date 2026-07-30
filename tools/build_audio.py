#!/usr/bin/env python3
"""Render Gerald's tape: segments.py -> docs/audio/*.mp3 + docs/data/segments.json

Voice: Kokoro TTS (kokoro-v1.0.onnx + voices-v1.0.bin in tools/voices/).
Post: band-limit + soft saturation + constant hiss bed + transport clicks,
so the cheap TTS reads as a deliberately lo-fi cassette dub.

Usage:  python3 tools/build_audio.py [--voice am_michael] [--only SEGID]
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.signal import butter, sosfilt

sys.path.insert(0, str(Path(__file__).parent))
from gerald_script import SEGMENTS, ORDER, FAKE_RUNTIME, TRACK_NAME  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = ROOT / "docs" / "audio"
DATA_DIR = ROOT / "docs" / "data"
VOICES = ROOT / "tools" / "voices"

SR = 24000
SPEED_NORMAL = 0.96   # Gerald's narration — flat, unhurried, deadpan
SPEED_QUOTE = 0.88    # lines the magician must repeat: slower, dictation-like
HISS_LEVEL = 0.0055
WAIT_TAIL = 1.1       # hiss after the cue, then the deck "auto-stops" (clunk)


def synth_factory(voice: str):
    from kokoro_onnx import Kokoro
    k = Kokoro(str(VOICES / "kokoro-v1.0.onnx"), str(VOICES / "voices-v1.0.bin"))

    def synth(text: str, speed: float) -> np.ndarray:
        samples, sr = k.create(text, voice=voice, speed=speed)
        assert sr == SR, f"unexpected sample rate {sr}"
        return samples.astype(np.float32)

    return synth


def silence(sec: float) -> np.ndarray:
    return np.zeros(int(SR * sec), dtype=np.float32)


def click() -> np.ndarray:
    """Tape transport click: tiny noise burst + low-frequency pop."""
    rng = np.random.default_rng(7)
    n = int(SR * 0.014)
    burst = rng.standard_normal(n).astype(np.float32) * np.exp(-np.linspace(0, 9, n))
    t = np.linspace(0, 0.010, int(SR * 0.010), dtype=np.float32)
    pop = 0.9 * np.sin(2 * np.pi * 70 * t) * np.exp(-t * 260)
    out = np.concatenate([burst * 0.5, pop, silence(0.05)])
    return out * 0.55


def flap() -> np.ndarray:
    """End-of-reel flap: a few flutter slaps."""
    parts = []
    for i in range(4):
        parts.append(click() * (0.9 - i * 0.15))
        parts.append(silence(0.085))
    return np.concatenate(parts)


def band_limit(x: np.ndarray) -> np.ndarray:
    sos_hp = butter(2, 200, btype="highpass", fs=SR, output="sos")
    sos_lp = butter(4, 5200, btype="lowpass", fs=SR, output="sos")
    return sosfilt(sos_lp, sosfilt(sos_hp, x)).astype(np.float32)


def saturate(x: np.ndarray) -> np.ndarray:
    k = 1.6
    return (np.tanh(k * x) / np.tanh(k)).astype(np.float32)


def hiss_bed(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    noise = rng.standard_normal(n).astype(np.float32)
    sos = butter(2, 6000, btype="lowpass", fs=SR, output="sos")
    noise = sosfilt(sos, noise).astype(np.float32)
    # slow wobble so the bed breathes like a real dub
    t = np.arange(n, dtype=np.float32) / SR
    wobble = 1.0 + 0.18 * np.sin(2 * np.pi * 0.31 * t + seed)
    return noise * wobble * HISS_LEVEL


def assemble(seg: dict, synth) -> np.ndarray:
    chunks: list[np.ndarray] = [silence(0.25)]
    for part in seg["parts"]:
        if isinstance(part, str):
            chunks.append(synth(part, SPEED_NORMAL))
        elif part[0] == "q":
            chunks.append(synth(part[1], SPEED_QUOTE))
        elif part[0] == "beat":
            chunks.append(silence(float(part[1])))
        elif part[0] == "click":
            chunks.append(silence(0.15))
            chunks.append(click())
            chunks.append(silence(0.15))
        elif part[0] == "flap":
            chunks.append(flap())
        else:
            raise ValueError(f"unknown part {part!r}")
    if seg["kind"] == "wait":
        # hiss tail, then the deck stops itself: a soft transport clunk
        chunks.append(silence(WAIT_TAIL))
        chunks.append(click() * 0.8)
        chunks.append(silence(0.12))
    else:
        chunks.append(silence(0.35))
    return np.concatenate(chunks)


def master(x: np.ndarray, seed: int) -> np.ndarray:
    speech = saturate(band_limit(x) * 1.25)
    out = speech + hiss_bed(len(speech), seed)
    # edge fades
    f = int(SR * 0.03)
    out[:f] *= np.linspace(0, 1, f, dtype=np.float32)
    out[-f:] *= np.linspace(1, 0, f, dtype=np.float32)
    peak = float(np.max(np.abs(out))) or 1.0
    return (out / peak * 0.84).astype(np.float32)


def encode_mp3(x: np.ndarray, path: Path) -> None:
    import lameenc
    enc = lameenc.Encoder()
    enc.set_bit_rate(64)
    enc.set_in_sample_rate(SR)
    enc.set_channels(1)
    enc.set_quality(2)
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2").tobytes()
    data = enc.encode(pcm)
    data += enc.flush()
    path.write_bytes(bytes(data))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--only", default=None, help="rebuild a single segment id")
    args = ap.parse_args()

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    synth = synth_factory(args.voice)

    manifest_path = DATA_DIR / "segments.json"
    manifest = {"runtime": FAKE_RUNTIME, "track": TRACK_NAME, "segments": {}}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())

    ids = [args.only] if args.only else ORDER
    for i, sid in enumerate(ORDER):
        if sid not in ids:
            continue
        seg = SEGMENTS[sid]
        fname = f"t{ORDER.index(sid) + 1:02d}.mp3"
        raw = assemble(seg, synth)
        final = master(raw, seed=ORDER.index(sid) + 11)
        encode_mp3(final, AUDIO_DIR / fname)
        dur = round(len(final) / SR, 2)
        manifest["segments"][sid] = {
            "kind": seg["kind"],
            "yes": seg.get("yes"),
            "no": seg.get("no"),
            "art": seg.get("art"),
            "caption": seg["caption"],
            "file": f"audio/{fname}",
            "dur": dur,
        }
        print(f"[{sid:>9}] {fname}  {dur:6.1f}s", flush=True)

    manifest["runtime"] = FAKE_RUNTIME
    manifest["track"] = TRACK_NAME
    manifest_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False))
    total = sum(s["dur"] for s in manifest["segments"].values())
    print(f"done: {len(manifest['segments'])} segments, {total/60:.1f} min of tape")


if __name__ == "__main__":
    main()
