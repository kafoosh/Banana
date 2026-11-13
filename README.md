# Banana

A magic trick that runs in a phone browser.

On screen is an open cassette album: *How to Read Minds, a home course in eight
cassettes*. Seven numbered tapes, one red. The performer has never done this
before and says so. They put on tape 1 and follow it, with a spectator as the
practice volunteer.

The volunteer thinks of a drawing and never says what it is. Each tape gives
the student one step and one line to say, then stops. The tapes never mention
what the volunteer answered; they only give the next step, and it is always the
right one. The red tape finishes the reading itself and names the drawing, which
then appears on the paper as a pencil doodle. The paper types out what the voice
says as it says it.

- `METHOD.md`: how the drawing is found. Private.
- `DESIGN.md`: why the trick is built this way.
- `docs/`: the app. Static files, no backend, works offline once loaded.
- `tools/`: the script and the audio build.

## Performing it

Read the slip that opens the first time you load the app. In short:

1. Phone between you and your volunteer, ringer on, volume up.
2. Touch tape 1 in the case. It goes into the player and plays. When a tape
   stops, do the step, then take the next tape from the case.
3. From tape 3 on, the volunteer's answer goes into how you pick up the next
   tape. **Yes: tap it. No: rest your finger on it until it lifts** (0.4 s).
   On a tap it lifts as your finger leaves; on a hold it lifts under your
   finger. That is your confirmation.
4. Wrong one? REWIND immediately. Every version of a tape is identical for its
   first three seconds (leader, then its number), so nothing has been given
   away. The tape goes back in the case; pick it again.
5. REWIND later than that takes the tape back to its start. PLAY restarts it.

Only the next tape in order responds to a touch. Hold a finger on the player
for one second to reopen the slip, which also has **Start over**. After the
red tape the same button appears on the paper.

Keyboard, for rehearsal at a desk: Space picks the next tape (tap or hold),
S stops, R rewinds.

A full run is about three minutes of tape. If it misses, you have the
best out available: you are on lesson one.

## Dev

```bash
python3 -m http.server -d docs 8080
```

`?debug` adds an overlay with the current recording, the drawings still
possible, and yes / no / skip-to-end buttons. It also keeps the service worker
off. If the audio files are missing the app runs silently on timers.

```bash
python3 tools/tapes.py
```

prints all eighteen routes.

## Re-recording

The script and the graph are in `tools/tapes.py`. Its header has the rules the
instructor's lines are written to. The voice is Kokoro TTS run through a
cassette chain (band limit, saturation, wow and flutter, hiss).

```bash
pip install kokoro-onnx soundfile numpy scipy lameenc
```

Put `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the kokoro-onnx
`model-files-v1.0` release in `tools/voices/` (git-ignored, 340 MB). Then:

```bash
python3 tools/build_audio.py
```

```bash
python3 tools/build_audio.py --only t5n t6nn
```

```bash
python3 tools/build_audio.py --voice bm_george
```

Files are written as `docs/audio/01.mp3`… so the folder says nothing, and the
graph goes to `docs/data/tapes.json`. After changing anything in `docs/`, bump
`VERSION` in `docs/sw.js` or installed copies keep the old one.

## Deploying

Serve `docs/` from anywhere static. GitHub Pages sites are public even when the
repo is private, and `docs/` contains the performer's slip and the graph, so
anyone given the URL can work out the pick. Keep `METHOD.md` out of it either way.

Fonts: Libre Franklin and Courier Prime, both SIL Open Font License.
