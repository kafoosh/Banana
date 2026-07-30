# Design Directions — "Guide to Reading Minds" webapp

> Companion to `METHOD.md`. Visual pitch lives in `designs/mockups.html`
> (self-contained; open in any browser). Status: **awaiting owner approval — no app code yet.**

## The frame

The app is not the mind reader — it's a **cheesy mail-order mind-reading course**, and the
user is a first-time magician performing straight out of the box. The kit gives instructions
(visible/audible to the spectator too), the magician relays them, the spectator answers.
Secretly the kit walks METHOD.md §5's tree.

Why this frame is strong, method-wise:

- The phone being out and visible is justified — it *is* the instructions.
- Every spectator NO is reframed as **the magician's failure** ("concentration failure
  detected in: OPERATOR"), so misses become comedy beats and the branching reads as
  error-handling, never as information-gathering. This implements METHOD.md §6's
  "misses become transitions" at the frame level.
- The funnel (§2) is delivered **by the kit itself** (audio or on-screen), so a first-timer
  can't butcher the load-bearing script.
- Copperfield banana/bandana lineage: "this is a dumb linear recording, it can't possibly
  respond" — which is exactly what the audio design weaponizes.

## Shared flow (all skins)

1. **ACT 1 — Unboxing.** "Congratulations on your purchase." Rules, cover story, optional
   name entry (kit chastises you by name later).
2. **ACT 2 — Induction.** The kit delivers the §2 funnel verbatim (age regression, 5–10s
   effort bound, exclusion list, real-size + word + letter-review pre-commitment).
3. **ACT 3 — Reading.** 3–5 beats traversing the §5 tree. Letters stated as impressions,
   probes as sharpening feelings, per §6.
4. **ACT 4 — Reveal.** Kit coaches the magician through claiming the miracle; art confirms.
5. **ACT 5 — Diploma.** "You are now 4% psychic." Doubles as reset/encore hook.

## The four skins

| # | Name | Era | Input disguise | Deception |
|---|------|-----|----------------|-----------|
| 1 | **The Cassette** — "Read Minds in 30 Minutes," Tape 2 Side B, The Amazing Gerald, played in fake shareware "AudioMaster 98" | '89 audio / '03 shareware | Linear media: YES = ▶, NO = ⏪10s then ▶ | ★★★★★ |
| 2 | **The GeoCities Page** — MIND MASTER 3000™ by Mystic Ron | 1997 web | Buttons disguised as bookkeeping: [YES — CONFIRMED] / [NO — RECALIBRATE] + PSYCHIC FAULT dialogs | ★★★ |
| 3 | **The VHS Course** — PSYCHIC ACADEMY™ Tape 2, Dr. Lance Marvello Ps.D. | 1991 VHS | Linear media: on-screen VCR remote, REW = NO, branch hidden in tracking glitch | ★★★★ |
| 4 | **The Photocopy** — Prof. Marvo's Mail-Order Mentalism, Lesson Seven | 1973 print, photocopied | Worksheet checkboxes ☐ CONFIRMED / ☐ DENIED; NOs come back graded in red pen | ★★★ |

Design 1 has a **boring-player variant** (stock system-player look, "it's literally an mp3")
— max deniability, all cheese lives in the audio. Shippable as a toggle.

## Audio design mechanics (Design 1, the flagship candidate)

- One fake file: `02_SideB_FirstPerformance.mp3`, fake fixed runtime 24:31. Playhead always
  advances during playback; all branches "end" exactly at end-of-side.
- **One audio segment per tree edge** (reaction to previous answer + next instruction), plus
  induction and finale segments ≈ **~50 short clips** (5–25s each). Entirely feasible to
  pre-generate.
- Each clip ends with "pause the tape" + a few seconds of hiss, so slow pausing leaks
  nothing. Auto-pause at hiss end as backup.
- **YES = press ▶.** **NO = press ⏪ ("let me re-hear the instructions") then ▶** — the NO
  branch opens by repeating the tail of the previous line (sells the rewind), then the voice
  "anticipates" the failure, chastises, and pivots. Period-authentic: cassette courses really
  did "if you answered B, fast-forward to…".
- Reveal: voice cues the magician to announce the drawing; cassette label art flips to the
  clip-art drawing as printed proof.
- Captions strip (CC) optional — accessibility + noisy rooms.

## Voice / TTS options (decision pending)

Pre-baked clips strongly preferred over live `speechSynthesis` (consistent across devices,
can be post-processed). Post-process with ffmpeg/sox: band-limit ~300–4kHz, mild saturation,
tape-hiss bed, click/clunk transport sounds — the lo-fi treatment also masks TTS cheapness.

- **Piper** — open source, runs locally, decent male voices. Cleanest licensing.
- **Kokoro** — open weights, best open quality.
- **edge-tts** — free tool over Microsoft neural voices; most "announcer"; ToS gray area.
- **Web Speech API** — zero build, robotic, device-dependent; dev-fallback only.
- Owner-recorded voice — maximum charm, most effort.

## Proposed stack

Static single-page app (Vite + vanilla TS), no backend. Tree from METHOD.md §5 as data.
Pre-baked audio in `public/audio/`. Deployable to GitHub Pages. PWA manifest so it installs
to the home screen and runs full-screen/offline (no browser chrome during performance).
Hidden debug mode (`?debug=1`) showing current node + remaining candidates, per §8.
Man/Stickman contingency (§7) on by default. No method words anywhere user-visible.

## Open decisions (owner)

1. Which skin(s) to build. **Recommendation: 1 (Cassette) as flagship**, GeoCities later as
   an alternate costume if wanted.
2. Secret NO input for audio: ⏪ rewind (recommended) vs hidden tap zones vs long-press.
3. TTS engine choice.
4. Reveal style: coached announcement + art flip (recommended) vs voice names it directly.
