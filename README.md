# Banana 🍌📼

A webapp magic trick. On screen it's **AudioMaster™ 98**, a crusty shareware
player with one file loaded: *"MIND-AEROBICS™ — Tape 2, Side B: Your First
Mind-Read"*, hosted by Gerald — an 80s workout-cassette instructor gone
completely deadpan. You (the magician) press play and do exactly what the
tape says, live, in front of a spectator. The tape runs the warm-up, feeds
you every line, dryly *calls* every "no" before you could possibly have told
it ("Don't ask how I know. I recorded this in 1987. The no arrived before
you did.")… and then tells you exactly what they drew.

The spectator sees a dumb linear audio file. It is not a dumb linear audio file.

- **Method:** `METHOD.md` (private — the whole product is the secret)
- **Design pitch & alternates:** `DESIGNS.md`, `designs/mockups.html`
- **The app:** `docs/` (static, no backend, PWA)

## Performing it

1. Open the app (phone, full volume). Read the packed-in insert once, alone.
2. Seat your subject, phone flat between you, press ▶, and obey Gerald.
3. When the tape stops, say Gerald's line and get the subject's answer. Then
   resume with your thumb on the correct half of the big ▶ button:
   **right half = YES, left half = NO.** Your thumb covers the whole button,
   so there is nothing to see — and Gerald reacts to an answer he was "never
   told." On air he only ever says: *"Don't tell me the answer. Press play.
   I'll know. I always know. Try not to think about it."*
4. Pressed the wrong half? Tap **◀◀10 immediately** — within ~3 seconds the
   tape rewinds to just before the question, and you simply answer again.
   (After that window, ◀◀10 is an honest 10-second replay, which is also fine.)
5. At the end, Gerald coaches you through announcing the drawing; the cassette
   art flips to the doodle as printed proof. Press ■ to rewind for the next
   spectator.

Emergency bail: triple-tap the title bar (rewinds the whole cassette).
`Playback` menu toggles captions. `Help` reopens the insert.

## Dev

Serve `docs/` statically, e.g.:

```
python3 -m http.server -d docs 8080
```

- `?debug=1` shows a dev overlay: current node, remaining candidate outs, and
  YES/NO/SKIP/MUTE buttons for dry-running the tree without performing.
- If audio files are missing the app runs in silent-rehearsal mode: captions +
  timers, same state machine.

## Rebuilding Gerald's voice

The tape is ~40 pre-rendered MP3 clips — one per branch transition, neutrally
named (`t01.mp3`…) so the audio folder leaks nothing.

```
pip install kokoro-onnx soundfile numpy scipy lameenc
# model files (not committed): tools/voices/kokoro-v1.0.onnx + voices-v1.0.bin
#   from https://github.com/thewh1teagle/kokoro-onnx/releases (model-files-v1.0)
python3 tools/build_audio.py            # all segments, voice am_michael
python3 tools/build_audio.py --only 24  # re-render one segment
python3 tools/build_audio.py --voice bm_george   # different Gerald
```

The script text + branch graph live in `tools/gerald_script.py`; the build
band-limits, saturates and adds tape hiss so the TTS reads as a deliberate
lo-fi cassette dub, then writes `docs/audio/*.mp3` and `docs/data/segments.json`.

## Deploying

`docs/` is plain static files — GitHub Pages (serve `/docs`), Netlify, or any
web server. It registers a service worker, so after one full load it performs
offline. Add to home screen for a chromeless, app-like run.

Note: GitHub Pages sites are public even from private repos. `docs/` contains
no method words and never explains itself — but don't publish `METHOD.md`.
