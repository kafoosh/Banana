# Gerald's tape — full script, segment by segment

Generated from `tools/gerald_script.py` (single source of truth). Track: `MindAerobics_Tape2_SideB.mp3`, printed fake runtime `11:47`. 41 segments — 4 setup, 5 letter, 1 man-check, 11 probe, 18 reveal (17 outcomes; STICKMAN has two entrances), 2 outro.

## How to use this file

Rewrite the text inside each segment block. Conventions:

| Notation | Meaning | Renders as |
|---|---|---|
| `GERALD  …` | Gerald narrating to the performer | TTS at speed 0.96, flat |
| `SAY     "…"` | a line the performer must repeat aloud | TTS at speed 0.88, dictation pace |
| `(beat N)` | silence, N seconds, hiss continues | silence |
| `(click)` | tape transport click | SFX |
| `(flap)` | end-of-reel flutter | SFX |

Each segment also carries a **caption** — the on-screen text shown while it plays (captions can be toggled off). `<b>…</b>` is the only markup used; it bolds the line the performer says out loud.

**Segment kinds:** `wait` = ends, deck auto-stops, awaiting a hidden YES/NO press (right half of ▶ = yes, left half = no). `auto` = chains straight on. `reveal` = flips the cassette art, then the finale auto-plays. `end` = stops.

---

## Answer 1 — the maximum number of NOs is **4**

Longest run of nos on any path: **4**, and it is the MOON path — all four consecutive, no yes in between:

```
Q1  A?                     → NO      (20 → 24)
Q2  …then an S?            → NO      (24 → 28)
Q3  Is it ALIVE?           → NO      (28 → 35)
Q4  Can you TOUCH it?      → NO      (35 → 42 = MOON)
```

Longest question run of any kind: **5 questions** (e.g. CAT, GLASS, PLANE, BOAT). Every leaf resolves in 3–5 questions.

Distribution across all 18 outcome paths:

| NOs on the path | Paths | Outcomes |
|---|---|---|
| 0 | 1 | STAR |
| 1 | 4 | CAT, FISH, GLASS, HEART |
| 2 | 8 | BALL, CAR, HOUSE, STICKMAN, SUN, TABLE, TREE |
| 3 | 4 | BOAT, FLOWER, PENCIL, PLANE |
| 4 | 1 | MOON |

(8 paths at 2 nos, 7 names — STICKMAN is reachable twice, via `31`→`48` and via the man-check objection `25m`→`rman`.)

**The load-bearing fact for the refactor:** every NO edge sits at a *fixed* depth. There is no branch where the same no can be the 2nd on one path and the 3rd on another. So a dynamically-inserted no can always be written knowing exactly which no it is:

| No # | How many edges | Where |
|---|---|---|
| 1st no | 4 | `20`→`24`, `21`→`25m`, `22`→`26`, `23`→`51` |
| 2nd no | 8 | `24`→`28`, `25`→`30`, `25m`→`rman`, `26`→`32`, `27`→`38`, `29`→`44`, `31`→`48`, `33`→`37` |
| 3rd no | 4 | `28`→`35`, `30`→`46`, `32`→`50`, `34`→`40` |
| 4th no | 1 | `35`→`42` |

17 NO edges total (and 17 YES edges). 7 of the NO edges land on another question; the rest land straight on a reveal.

---

## Answer 2 — where the NOs currently live

Right now every reaction is welded to the front of the segment it leads into, which is why there are 17 hand-written no-reactions and no way to vary them. Below, each segment marks its reaction opener with a `··· end of reaction opener ···` rule — that is the text that would be lifted out into a separately-rendered **no clip** played *before* the segment audio.

Blockers worth knowing before the split:

- **9 of the 17 no-reactions are outcome-bound**, not generic. `Can't touch it. Nobody can. That's rather the point.` *is* the SUN reveal's logic; `Not hard. Soft skin, full of air.` is the BALL's. These can't be swapped for a generic no clip without gutting the reveals — they need re-scoping as reveal copy, with the generic no inserted in front of them.
- **8 are genuinely generic and are the real extraction targets** — the 7 that land on another question (`24`, `25m`, `26`, `28`, `30`, `32`, `35`) plus `37`, whose opener (`A no. Felt it in the flywheel.`) is generic even though it lands on the HOUSE reveal.
- `33` has its reaction fused into one spoken line and needs a manual split.
- Audio consequence: a no clip played in front of a segment means **two files back to back**, so the hiss bed, fades, and levels have to match across the join, or the seam is audible. Today each segment is mastered independently (`master()` normalises per file), so this needs the mastering to be shared or the join to be crossfaded under the hiss.

---

## The segments

### Act 1 & 2 — setup and induction

#### `intro` — ACT 1 — Rules & setup

**Kind:** `wait`  ·  **Audio:** `t01.mp3`

**Entered via:** — (start of tape)

**Exits:** any press → `ind1` (linear checkpoint, no hidden input)

```
GERALD  Side B. Your first performance, with a live subject.
(beat 0.7)
GERALD  I'm Gerald. The box calls this Mind-Aerobics. We're both going to live with that.
(beat 0.9)
GERALD  You'll need one subject, seated. A quiet room. And a working relationship with instructions.
(beat 0.8)
GERALD  Rules. One: you say only the lines I give you, word for word. You are, for our purposes, a speaker with legs.
(beat 0.6)
GERALD  Two: when the tape stops, that's you. Say the line. Get their answer.
(beat 0.6)
GERALD  Three. Don't tell me the answer. Don't say it, don't mouth it, don't tap it out in code. Press play.
(beat 0.6)
GERALD  I'll know.
(beat 0.8)
GERALD  I always know. Try not to think about it.
(beat 0.9)
GERALD  Seat your subject across from you. Phone flat on the table, face up, where they can watch it. It's a tape. Let them watch the tape.
(beat 0.6)
GERALD  Press play when you're both sitting comfortably. I'll be here.
```

*Caption:*

```html
Side B. Rule 1: say only Gerald's lines, word for word. Rule 2: when the tape stops, say the line and get their answer. Rule 3: <b>don't tell Gerald the answer — press play. He'll know.</b> Seat your subject, phone flat between you, face up. <b>Play when you're both ready.</b>
```

#### `ind1` — ACT 2 — Induction: the doodle

**Kind:** `wait`  ·  **Audio:** `t02.mp3`

**Entered via:** `intro` (linear, any press)

**Exits:** any press → `ind2` (linear checkpoint, no hidden input)

```
GERALD  Warm-up. Subject — hello. I'm Gerald. Don't answer; it never helps.
(beat 0.7)
GERALD  Close your eyes.
(beat 1.2)
GERALD  You're in school. Ten years old. Maybe twelve. Last period. The clock isn't moving, and the teacher's voice is coming from somewhere else entirely.
(beat 0.8)
GERALD  There's a pencil in your hand. And without deciding anything, you're doodling. The same small doodle you always drew. Five seconds of pencil. Ten, if you were feeling ambitious.
(beat 0.9)
GERALD  Not a smiley face — we've all moved past it. Not a mountain. Not a bicycle; nobody's impressed. And no empty geometry — no circles, no triangles. A real thing. Something anyone would recognize on sight.
(beat 1.0)
GERALD  Look at it. Small. In pencil. Unmistakably yours.
(beat 0.9)
GERALD  Don't say what it is. Not now. Not later. This is the only rule you have, so make it count.
(beat 0.7)
GERALD  The tape stops here. When your subject nods, press play. That was the warm-up. You're supposedly warmer now.
```

*Caption:*

```html
「TO YOUR SUBJECT」 Close your eyes. You're in school — ten, maybe twelve, last period, pencil in hand — doodling the same small doodle you always drew. Five, ten seconds of pencil. Not a smiley face. Not a mountain. Not a bicycle. No circles or triangles. A real thing anyone would recognize on sight. Look at it. Never say it. <b>Play when they nod.</b>
```

#### `ind2` — ACT 2 — Induction: the word

**Kind:** `wait`  ·  **Audio:** `t03.mp3`

**Entered via:** `ind1` (linear, any press)

**Exits:** any press → `preflight` (linear checkpoint, no hidden input)

```
GERALD  Eyes open.
(beat 0.6)
GERALD  Subject: take the doodle, and set the real thing here in the room. Actual size. Between the two of you.
(beat 1.0)
GERALD  Now think of it as a word. If you'd drawn a smiley face — which you didn't; we discussed it — you'd see a face, and think the word smiley.
(beat 0.7)
GERALD  Find your word. Walk its letters, one at a time. First letter.
(beat 1.2)
GERALD  Next. Keep going, to the end.
(beat 1.3)
GERALD  Again. Slower. The letters aren't going anywhere.
(beat 1.4)
GERALD  Good.
(beat 0.6)
GERALD  Ask them if they have it. A nod is enough. If it's taking a while, remind them, gently: it's a doodle, not a mortgage.
(beat 0.5)
GERALD  Play when they nod.
```

*Caption:*

```html
「TO YOUR SUBJECT」 Set the real thing in the room — actual size, between you. Now think of it as a WORD (a smiley face would be the word SMILEY). Walk its letters one at a time… and again, slower. 「TO YOU」 Ask: <b>“Do you have it?”</b> A nod is enough. <b>Play when they nod.</b>
```

#### `preflight` — ACT 2 — Handoff

**Kind:** `auto`  ·  **Audio:** `t04.mp3`

**Entered via:** `ind2` (linear, any press)

**Exits:** auto-chains → `20`

```
GERALD  From here, only my words.
(beat 0.6)
GERALD  Straighten up. Try to look like someone things happen to on purpose.
(beat 0.6)
GERALD  Here we go.
```

*Caption:*

```html
From here, only Gerald's words. Straighten up. Look like someone things happen to on purpose. Here we go.
```

---

### The letters

#### `20` — LETTER A

**Kind:** `wait`  ·  **Audio:** `t05.mp3`

**Entered via:** `preflight` (linear, any press)

**Exits:** YES → `21` · NO → `24`

```
GERALD  First one. It's a letter. Say it the way you'd read a menu:
(beat 0.4)
SAY     "I can feel a letter in your word. An A. There's an A — correct?"
(beat 0.6)
GERALD  Get their answer. You know the procedure.
```

*Caption:*

```html
First one — say it like you're reading a menu: <b>“I can feel a letter in your word. An A. There's an A… correct?”</b> Get their answer, then play.
```

#### `21` — LETTER T

**Kind:** `wait`  ·  **Audio:** `t06.mp3`

**Entered via:** `20` on **YES**

**Exits:** YES → `22` · NO → `25m`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  There's the A. There's always an A. I'd act surprised, but we agreed to be honest with each other.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Next:
(beat 0.4)
SAY     "I see a T as well. Yes?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
There's the A — there's always an A. Next: <b>“I see a T as well… yes?”</b> Go.
```

#### `22` — LETTER R

**Kind:** `wait`  ·  **Audio:** `t07.mp3`

**Entered via:** `21` on **YES**

**Exits:** YES → `23` · NO → `26`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Two for two. Don't let it change you.
(beat 0.5)
···················· end of reaction opener ····················
GERALD  Softer now:
(beat 0.4)
SAY     "Is that… an R?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Two for two — don't let it change you. Softer: <b>“Is that… an R?”</b> Go.
```

#### `23` — LETTER S (final)

**Kind:** `wait`  ·  **Audio:** `t08.mp3`

**Entered via:** `22` on **YES**

**Exits:** YES → `52` · NO → `51`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Three in a row. Statistically, you're due.
(beat 0.5)
···················· end of reaction opener ····················
GERALD  Last letter. Say it like you barely trust it:
(beat 0.4)
SAY     "Now I'm not sure about this one. An S?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Three in a row — statistically, you're due. Last letter, barely trust it: <b>“Now I'm not sure about this one… an S?”</b> Go.
```

#### `24` — LETTER S (recovery, after A missed)

**Kind:** `wait`  ·  **Audio:** `t09.mp3`

**Entered via:** `20` on **NO** — always the **1st no** of the run

**Exits:** YES → `27` · NO → `28`

> **Reaction opener:** first 8 part(s) — extraction candidate.

```
GERALD  That was a no.
(beat 0.7)
GERALD  Don't ask how I know. I recorded this in 1987. The no arrived before you did.
(beat 0.7)
GERALD  It's not the tape. It's not the subject. I'll leave the remaining option with you.
(beat 0.8)
GERALD  It's fine. A miss is information. Write that down somewhere you'll never look.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Say this:
(beat 0.4)
SAY     "No… no, it's leaning. It's an S. There is an S."
(beat 0.5)
GERALD  Deliver it like a man who has never been wrong. You've seen one.
```

*Caption:*

```html
That was a no — the no arrived before you did. Not the tape's fault; not the subject's. Say: <b>“No… no, it's leaning. It's an S. There IS an S.”</b> Like a man who has never been wrong. You've seen one.
```

---

### The man check

#### `25m` — MAN CHECK — “it is NOT a living thing” (Stickman safety valve)

**Kind:** `wait`  ·  **Audio:** `t10.mp3`

**Entered via:** `21` on **NO** — always the **1st no** of the run

**Exits:** YES → `25` · NO → `rman`

> **Reaction opener:** first 4 part(s) — extraction candidate.

```
GERALD  A no. I felt it coming, the way one feels weather.
(beat 0.7)
GERALD  It's useful, actually. I understand if it doesn't feel that way from where you're sitting.
(beat 0.7)
···················· end of reaction opener ····················
GERALD  The next one is said as a fact. Not a question. A fact:
(beat 0.4)
SAY     "This thing you drew — it is NOT a living thing."
(beat 0.7)
GERALD  If they nod, that's a yes. If they argue with you, that's a no.
(beat 0.5)
GERALD  Either way, press play. I'll take it from there.
```

*Caption:*

```html
A no — Gerald felt it coming, the way one feels weather. Say this as a FACT, not a question: <b>“This thing you drew — it is NOT a living thing.”</b> Nod = yes. Argument = no. Either way, press play.
```

---

### The probes

#### `25` — PROBE — hold in one hand

**Kind:** `wait`  ·  **Audio:** `t11.mp3`

**Entered via:** `25m` on **YES**

**Exits:** YES → `29` · NO → `30`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Agreed. Not alive. Progress — the small kind, but I've learned not to be picky.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Say:
(beat 0.4)
SAY     "Hold out your hand. Imagine it there. Could you HOLD it in one hand?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Agreed — not alive. Progress, the small kind. Say: <b>“Hold out your hand. Imagine it there. Could you HOLD it in one hand?”</b> Go.
```

#### `26` — PROBE — alive?

**Kind:** `wait`  ·  **Audio:** `t12.mp3`

**Entered via:** `22` on **NO** — always the **1st no** of the run

**Exits:** YES → `31` · NO → `32`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  No R. I know. I felt it through the magnetic particles. They don't lie. It's most of what I like about them.
(beat 0.7)
···················· end of reaction opener ····················
GERALD  New approach. Say:
(beat 0.4)
SAY     "Leave the letters. Let me touch the thing itself. Is it ALIVE?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
No R — felt through the magnetic particles, which don't lie. New approach: <b>“Leave the letters. Let me touch the thing itself. Is it ALIVE?”</b> Go.
```

#### `27` — PROBE — can you touch it?

**Kind:** `wait`  ·  **Audio:** `t13.mp3`

**Entered via:** `24` on **YES**

**Exits:** YES → `33` · NO → `38`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  The S. There it is. We're back, and we will never speak of the A again.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Letters are done. Now the senses. Say:
(beat 0.4)
SAY     "Reach out in your mind. Can you TOUCH it?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
The S — we're back, and we will never speak of the A again. Now the senses: <b>“Reach out in your mind. Can you TOUCH it?”</b> Go.
```

#### `28` — PROBE — alive?

**Kind:** `wait`  ·  **Audio:** `t14.mp3`

**Entered via:** `24` on **NO** — always the **2nd no** of the run

**Exits:** YES → `34` · NO → `35`

> **Reaction opener:** first 8 part(s) — extraction candidate.

```
GERALD  Also a no.
(beat 0.7)
GERALD  I knew yesterday. I knew in 1987. At some point we should discuss what you knew, and when.
(beat 0.8)
GERALD  Letters are not your event. That's allowed. Some athletes are sprinters. Some are distance runners.
(beat 0.7)
GERALD  Moving on.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  We'll use raw impressions now. My field. And, as of today, yours. Say:
(beat 0.4)
SAY     "Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Also a no — Gerald knew in 1987. Letters are not your event; that's allowed. Raw impressions now: <b>“Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?”</b> Go.
```

#### `29` — PROBE — is it hard?

**Kind:** `wait`  ·  **Audio:** `t15.mp3`

**Entered via:** `25` on **YES**

**Exits:** YES → `43` · NO → `44`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Held it. I felt the grip from in here. It's a strange life, being a tape.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  The surface. Say:
(beat 0.4)
SAY     "Squeeze it. Is it HARD?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Held it — Gerald felt the grip from in there. It's a strange life, being a tape. Say: <b>“Squeeze it. Is it HARD?”</b> Go.
```

#### `30` — PROBE — do you own one?

**Kind:** `wait`  ·  **Audio:** `t16.mp3`

**Entered via:** `25` on **NO** — always the **2nd no** of the run

**Exits:** YES → `45` · NO → `46`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  No. Too big for a hand. I knew — and so did you, if we're generous with the word.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Say:
(beat 0.4)
SAY     "It's bigger than both of us. Tell me — do you OWN one?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
A no — too big for a hand. Say: <b>“It's bigger than both of us. Tell me — do you OWN one?”</b> Go.
```

#### `31` — PROBE — smaller than you?

**Kind:** `wait`  ·  **Audio:** `t17.mp3`

**Entered via:** `26` on **YES**

**Exits:** YES → `47` · NO → `48`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Alive. I can hear it moving from here.
(beat 0.5)
···················· end of reaction opener ····················
GERALD  Say:
(beat 0.4)
SAY     "Stand next to it in your mind. Is it SMALLER than you?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Alive — Gerald can hear it moving from here. Say: <b>“Stand next to it in your mind. Is it SMALLER than you?”</b> Go.
```

#### `32` — PROBE — one at home?

**Kind:** `wait`  ·  **Audio:** `t18.mp3`

**Entered via:** `26` on **NO** — always the **2nd no** of the run

**Exits:** YES → `49` · NO → `50`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  A no. You're surprised. One of us is surprised.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Not alive. But say this part gently:
(beat 0.4)
SAY     "It relates to life… it's part of a day."
(beat 0.6)
GERALD  Let it land. Then:
(beat 0.4)
SAY     "Do you have one at HOME?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
A no — one of us is surprised. Gently: <b>“It relates to life… it's part of a day.”</b> Let it land. Then: <b>“Do you have one at HOME?”</b> Go.
```

#### `33` — PROBE — alive?

**Kind:** `wait`  ·  **Audio:** `t19.mp3`

**Entered via:** `27` on **YES**

**Exits:** YES → `36` · NO → `37`

> **Note:** opener is fused into the instruction line (`Touchable. Reach further. Say:`) — needs splitting by hand.

```
GERALD  Touchable. Reach further. Say:
(beat 0.4)
SAY     "I'm touching it with you… wait. I sense… LIFE. Is it alive?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Touchable — reach further. Say: <b>“I'm touching it with you… wait. I sense… LIFE. Is it alive?”</b> Go.
```

#### `34` — PROBE — bigger than you?

**Kind:** `wait`  ·  **Audio:** `t20.mp3`

**Entered via:** `28` on **YES**

**Exits:** YES → `39` · NO → `40`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Alive. The impressions like you. The letters said nothing, which, for them, is warm.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Say:
(beat 0.4)
SAY     "Stand next to it. Is it BIGGER than you?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
Alive — the impressions like you. Say: <b>“Stand next to it. Is it BIGGER than you?”</b> Go.
```

#### `35` — PROBE — can you touch it?

**Kind:** `wait`  ·  **Audio:** `t21.mp3`

**Entered via:** `28` on **NO** — always the **3rd no** of the run

**Exits:** YES → `41` · NO → `42`

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  No. I knew — the same way I know you skipped Side A. We don't have to do this dance, you and I.
(beat 0.7)
···················· end of reaction opener ····················
GERALD  Not alive. We're close. I can feel corners. Say:
(beat 0.4)
SAY     "Reach for it. Can you TOUCH it?"
(beat 0.5)
GERALD  Go.
```

*Caption:*

```html
A no — Gerald knew, the same way he knows you skipped Side A. Close now; he can feel corners. Say: <b>“Reach for it. Can you TOUCH it?”</b> Go.
```

---

### The reveals

#### `36` — REVEAL — FISH

**Kind:** `reveal`  ·  **Audio:** `t22.mp3`  ·  **Art:** `fish`

**Entered via:** `33` on **YES**

**Exits:** flips art, then `finale` auto-plays

> **Note:** reaction is outcome-specific (wet/alive) — reads as reveal copy, not a generic YES beat.

```
GERALD  Alive. And — hold on.
(beat 0.7)
GERALD  Wet.
(beat 0.7)
GERALD  It's wet. I'd stand up for this one if I could.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "Scales. A little bubble over its head."
(beat 0.8)
GERALD  Then finish it:
(beat 0.4)
SAY     "You drew a FISH."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Wet. Gerald would stand up for this one if he could. Say: <b>“Scales. A little bubble over its head.”</b> Then: <b>“You drew a FISH.”</b> Turn the screen around.
```

#### `37` — REVEAL — HOUSE

**Kind:** `reveal`  ·  **Audio:** `t23.mp3`  ·  **Art:** `house`

**Entered via:** `33` on **NO** — always the **2nd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  A no. Felt it in the flywheel.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Listen carefully, because this next part is the whole job. Say it exactly:
(beat 0.4)
SAY     "It's not alive — but it is FULL of life. It's where the life lives."
(beat 0.7)
GERALD  Watch their face. There it is.
(beat 0.6)
GERALD  Now:
(beat 0.4)
SAY     "Square walls. A triangle roof. Smoke from the chimney."
(beat 0.7)
SAY     "You drew a HOUSE."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
A no — felt in the flywheel. This next part is the whole job; say it exactly: <b>“It's not alive — but it is FULL of life. It's where the life lives.”</b> Watch their face. Then: <b>“Square walls. A triangle roof. Smoke from the chimney. You drew a HOUSE.”</b> Turn the screen around.
```

#### `38` — REVEAL — SUN

**Kind:** `reveal`  ·  **Audio:** `t24.mp3`  ·  **Art:** `sun`

**Entered via:** `27` on **NO** — always the **2nd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `Can't touch it. Nobody can.` is a NO reaction, but it is also the SUN's whole logic — outcome-bound.

```
GERALD  Can't touch it. Nobody can. That's rather the point.
(beat 0.6)
GERALD  Very few things can't be touched. All of them headline. Say:
(beat 0.4)
SAY     "Of course you can't touch it. It's ninety-three million miles away — and you drew it in the corner of the page, with little lines coming off it."
(beat 0.7)
SAY     "You drew the SUN."
(beat 0.8)
GERALD  Turn the screen around. Feel free to take credit for the warmth.
```

*Caption:*

```html
Can't touch it — nobody can; that's rather the point. Say: <b>“Of course you can't touch it. It's ninety-three million miles away — you drew it in the corner of the page with little lines coming off it. You drew the SUN.”</b> Turn the screen around.
```

#### `39` — REVEAL — TREE

**Kind:** `reveal`  ·  **Audio:** `t25.mp3`  ·  **Art:** `tree`

**Entered via:** `34` on **YES**

**Exits:** flips art, then `finale` auto-plays

```
GERALD  Bigger. Alive. And older than everyone involved.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "Roots down. Branches up. You drew the leaves as one big cloud, didn't you."
(beat 0.7)
SAY     "You drew a TREE."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Bigger, alive, and older than everyone involved. Say: <b>“Roots down. Branches up. The leaves were one big cloud, weren't they. You drew a TREE.”</b> Turn the screen around.
```

#### `40` — REVEAL — FLOWER

**Kind:** `reveal`  ·  **Audio:** `t26.mp3`  ·  **Art:** `flower`

**Entered via:** `34` on **NO** — always the **3rd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `Smaller. I felt petals.` — NO reaction fused with the FLOWER reveal.

```
GERALD  Smaller. I felt petals. I don't examine how.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "A stem. Petals in a ring. You pressed harder on the middle."
(beat 0.7)
SAY     "You drew a FLOWER."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Smaller — Gerald felt petals; he doesn't examine how. Say: <b>“A stem. Petals in a ring. You pressed harder on the middle. You drew a FLOWER.”</b> Turn the screen around.
```

#### `41` — REVEAL — PENCIL

**Kind:** `reveal`  ·  **Audio:** `t27.mp3`  ·  **Art:** `pencil`

**Entered via:** `35` on **YES**

**Exits:** flips art, then `finale` auto-plays

```
GERALD  Touchable. And somebody in this story has been holding its cousin the whole time.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "Long. Thin. A point at one end. You drew the thing you were drawing WITH."
(beat 0.7)
SAY     "You drew a PENCIL."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Touchable — and someone in this story has been holding its cousin the whole time. Say: <b>“Long. Thin. A point at one end. You drew the thing you were drawing WITH. You drew a PENCIL.”</b> Turn the screen around.
```

#### `42` — REVEAL — MOON

**Kind:** `reveal`  ·  **Audio:** `t28.mp3`  ·  **Art:** `moon`

**Entered via:** `35` on **NO** — always the **4th no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `Can't touch it.` — NO reaction fused with the MOON reveal.

```
GERALD  Can't touch it. I called that one from inside a cassette, which is where I live.
(beat 0.6)
GERALD  Far away. Cold. Silver. Say:
(beat 0.4)
SAY     "You drew it as a crescent — a little banana in the sky — with stars around it."
(beat 0.7)
SAY     "You drew the MOON."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Untouchable — called from inside a cassette, which is where Gerald lives. Say: <b>“You drew it as a crescent — a little banana in the sky — with stars around it. You drew the MOON.”</b> Turn the screen around.
```

#### `43` — REVEAL — GLASS

**Kind:** `reveal`  ·  **Audio:** `t29.mp3`  ·  **Art:** `glass`

**Entered via:** `29` on **YES**

**Exits:** flips art, then `finale` auto-plays

```
GERALD  Hard. And cold. They didn't mention cold. They didn't have to.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "A stem. A bowl. A toast at the end of a long week."
(beat 0.7)
SAY     "You drew a GLASS."
(beat 0.8)
GERALD  Turn the screen around. Cheers.
```

*Caption:*

```html
Hard — and cold. They didn't mention cold; they didn't have to. Say: <b>“A stem. A bowl. A toast at the end of a long week. You drew a GLASS.”</b> Turn the screen around. Cheers.
```

#### `44` — REVEAL — BALL

**Kind:** `reveal`  ·  **Audio:** `t30.mp3`  ·  **Art:** `ball`

**Entered via:** `29` on **NO** — always the **2nd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `Not hard. Soft skin, full of air.` — NO reaction fused with the BALL reveal.

```
GERALD  Not hard. Soft skin, full of air. I had it the moment they squeezed.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "It wants to be thrown. It spends its whole life leaving."
(beat 0.7)
SAY     "You drew a BALL."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Not hard — soft skin, full of air. Say: <b>“It wants to be thrown. It spends its whole life leaving. You drew a BALL.”</b> Turn the screen around.
```

#### `45` — REVEAL — CAR

**Kind:** `reveal`  ·  **Audio:** `t31.mp3`  ·  **Art:** `car`

**Entered via:** `30` on **YES**

**Exits:** flips art, then `finale` auto-plays

```
GERALD  They own one. I've ridden in it, in the sense that matters least.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "Four wheels. Windows. Parked outside a childhood house."
(beat 0.7)
SAY     "You drew a CAR."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
They own one — Gerald has ridden in it, in the sense that matters least. Say: <b>“Four wheels. Windows. Parked outside a childhood house. You drew a CAR.”</b> Turn the screen around.
```

#### `46` — REVEAL — PLANE

**Kind:** `reveal`  ·  **Audio:** `t32.mp3`  ·  **Art:** `plane`

**Entered via:** `30` on **NO** — always the **3rd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `They don't own one.` — NO reaction fused with the PLANE reveal.

```
GERALD  They don't own one. Nobody owns one. It belongs to the sky, and to a leasing company.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "You drew it with little windows down the side, didn't you."
(beat 0.7)
SAY     "You drew a PLANE."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Nobody owns one — it belongs to the sky, and to a leasing company. Say: <b>“You drew it with little windows down the side, didn't you. You drew a PLANE.”</b> Turn the screen around.
```

#### `47` — REVEAL — CAT

**Kind:** `reveal`  ·  **Audio:** `t33.mp3`  ·  **Art:** `cat`

**Entered via:** `31` on **YES**

**Exits:** flips art, then `finale` auto-plays

```
GERALD  Smaller. Warm. And profoundly uninterested in either of us.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "Whiskers. Pointed ears. It is ignoring you right now."
(beat 0.7)
SAY     "You drew a CAT."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Smaller, warm, and profoundly uninterested in either of us. Say: <b>“Whiskers. Pointed ears. It's ignoring you right now. You drew a CAT.”</b> Turn the screen around.
```

#### `48` — REVEAL — STICKMAN

**Kind:** `reveal`  ·  **Audio:** `t34.mp3`  ·  **Art:** `stickman`

**Entered via:** `31` on **NO** — always the **2nd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `Not smaller. Of course not.` — NO reaction fused with the STICKMAN reveal.

```
GERALD  Not smaller. Of course not. It's exactly your size. It has always been exactly your size.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "A round head. Stick arms, straight out. A self-portrait, age ten."
(beat 0.7)
SAY     "You drew a little STICKMAN. You drew YOU."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Not smaller — it's exactly your size. It always was. Say: <b>“A round head. Stick arms straight out. A self-portrait, age ten. You drew a STICKMAN — you drew YOU.”</b> Turn the screen around.
```

#### `rman` — REVEAL — STICKMAN (via the man-check objection)

**Kind:** `reveal`  ·  **Audio:** `t35.mp3`  ·  **Art:** `stickman`

**Entered via:** `25m` on **NO** — always the **2nd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Reaction opener:** first 4 part(s) — extraction candidate.

```
GERALD  They argued.
(beat 0.8)
GERALD  Good. Arguments have pulses.
(beat 0.6)
···················· end of reaction opener ····················
GERALD  Say:
(beat 0.4)
SAY     "You drew a person. A round head. Stick arms, straight out."
(beat 0.7)
SAY     "That's YOU, isn't it. You drew yourself."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
They argued. Good — arguments have pulses. Say: <b>“You drew a person. Round head, stick arms straight out. That's YOU, isn't it.”</b> Turn the screen around.
```

#### `49` — REVEAL — TABLE

**Kind:** `reveal`  ·  **Audio:** `t36.mp3`  ·  **Art:** `table`

**Entered via:** `32` on **YES**

**Exits:** flips art, then `finale` auto-plays

```
GERALD  At home. Naturally. You ate off yours this evening. We'll leave it there.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "Four legs. A flat top. The whole family around it."
(beat 0.7)
SAY     "You drew a TABLE."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
At home, naturally — you ate off yours this evening; we'll leave it there. Say: <b>“Four legs. A flat top. The whole family around it. You drew a TABLE.”</b> Turn the screen around.
```

#### `50` — REVEAL — BOAT

**Kind:** `reveal`  ·  **Audio:** `t37.mp3`  ·  **Art:** `boat`

**Entered via:** `32` on **NO** — always the **3rd no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Note:** `Not at home.` — NO reaction fused with the BOAT reveal.

```
GERALD  Not at home. It lives on the water. Most of the good ones do.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "A little hull. A sail. And you always drew the waves as tiny letter W's, didn't you."
(beat 0.7)
SAY     "You drew a BOAT."
(beat 0.8)
GERALD  Turn the screen around.
```

*Caption:*

```html
Not at home — it lives on the water. Most of the good ones do. Say: <b>“A little hull. A sail. You always drew the waves as tiny W's, didn't you. You drew a BOAT.”</b> Turn the screen around.
```

#### `51` — REVEAL — HEART

**Kind:** `reveal`  ·  **Audio:** `t38.mp3`  ·  **Art:** `heart`

**Entered via:** `23` on **NO** — always the **1st no** of the run

**Exits:** flips art, then `finale` auto-plays

> **Reaction opener:** first 4 part(s) — extraction candidate.

```
GERALD  No S.
(beat 0.8)
GERALD  For once, a no is the best possible news. A. T. R. And no S.
(beat 0.7)
···················· end of reaction opener ····················
GERALD  I know this one. Stand up straight.
(beat 0.6)
GERALD  Say:
(beat 0.4)
SAY     "It's not letters anymore. I can FEEL this one. It's beating."
(beat 0.7)
SAY     "You drew a HEART."
(beat 0.8)
GERALD  Turn the screen around. Take your time.
```

*Caption:*

```html
No S — and for once, a no is the best possible news. Stand up straight: <b>“It's not letters anymore. I can FEEL this one. It's beating. You drew a HEART.”</b> Turn the screen around. Take your time.
```

#### `52` — REVEAL — STAR

**Kind:** `reveal`  ·  **Audio:** `t39.mp3`  ·  **Art:** `star`

**Entered via:** `23` on **YES**

**Exits:** flips art, then `finale` auto-plays

> **Reaction opener:** first 2 part(s) — extraction candidate.

```
GERALD  Four for four. It happens. Rarely, and to other people, but it happens.
(beat 0.7)
···················· end of reaction opener ····················
GERALD  Slowly now. Say:
(beat 0.4)
SAY     "You were ten years old, bored out of your mind… and you reached for the sky."
(beat 0.7)
SAY     "You drew a STAR."
(beat 0.8)
GERALD  Turn the screen around. That one's yours.
```

*Caption:*

```html
Four for four. It happens — rarely, and to other people. Slowly: <b>“You were ten years old, bored out of your mind… and you reached for the sky. You drew a STAR.”</b> Turn the screen around. That one's yours.
```

---

### Outro

#### `finale` — OUTRO — finale

**Kind:** `end`  ·  **Audio:** `t40.mp3`

**Entered via:** — (start of tape)

**Exits:** stops; play → `extras`

```
(flap)
(beat 0.8)
GERALD  That's the routine. Let them have the moment.
(beat 0.6)
GERALD  Don't explain anything. You couldn't. But don't.
(beat 0.8)
GERALD  You were adequate. That's my second-highest grade. No one has received the first.
(beat 0.8)
GERALD  The rest of this side is licensing information. Press stop, and rewind the whole tape for your next subject.
(beat 0.7)
GERALD  Hydrate. It won't fix anything, but it's good for you.
(beat 0.7)
GERALD  Gerald out.
```

*Caption:*

```html
That's the routine. Don't explain anything — you couldn't, but don't. You were adequate: Gerald's second-highest grade. No one has received the first. <b>Press ■ to rewind for your next subject.</b>
```

#### `extras` — OUTRO — licensing easter egg

**Kind:** `end`  ·  **Audio:** `t41.mp3`

**Entered via:** — (start of tape)

**Exits:** stops (end of tape)

```
GERALD  This recording is the property of Gerald Enterprises, Reseda, California.
(beat 0.6)
GERALD  Mind-Aerobics is a registered trademark of a company that no longer exists.
(beat 0.6)
GERALD  Results not typical. No results are typical.
(beat 0.6)
GERALD  No refunds. Side A is sold separately. It has always been sold separately.
(beat 1.4)
GERALD  You're still listening.
(beat 0.8)
GERALD  The workout is over. Go outside.
(beat 0.8)
(flap)
```

*Caption:*

```html
This recording is the property of Gerald Enterprises, Reseda, CA. Mind-Aerobics is a registered trademark of a company that no longer exists. Results not typical. No refunds. Side A is sold separately. It has always been sold separately. … You're still listening. The workout is over. Go outside.
```

---

## Appendix — the 17 no-reactions, pulled out

Every line Gerald currently says in reaction to a no, in one place, so the rewrite can see them as a set. `#` is which no of the run it always is.

| # | Edge | Lands on | Current reaction | Generic? |
|---|---|---|---|---|
| 1st | `20`→`24` | question `24` | That was a no. Don't ask how I know. I recorded this in 1987. The no arrived before you did. It's not the tape. It's not the subject. I'll leave the remaining option with you. It's fine. A miss is information. Write that down somewhere you'll never look. | yes |
| 1st | `21`→`25m` | question `25m` | A no. I felt it coming, the way one feels weather. It's useful, actually. I understand if it doesn't feel that way from where you're sitting. | yes |
| 1st | `22`→`26` | question `26` | No R. I know. I felt it through the magnetic particles. They don't lie. It's most of what I like about them. | yes |
| 1st | `23`→`51` | HEART | No S. For once, a no is the best possible news. A. T. R. And no S. | no — outcome-bound |
| 2nd | `24`→`28` | question `28` | Also a no. I knew yesterday. I knew in 1987. At some point we should discuss what you knew, and when. Letters are not your event. That's allowed. Some athletes are sprinters. Some are distance runners. Moving on. | yes |
| 2nd | `25`→`30` | question `30` | No. Too big for a hand. I knew — and so did you, if we're generous with the word. | yes |
| 2nd | `25m`→`rman` | STICKMAN | They argued. Good. Arguments have pulses. | no — outcome-bound |
| 2nd | `26`→`32` | question `32` | A no. You're surprised. One of us is surprised. | yes |
| 2nd | `27`→`38` | SUN | Can't touch it. Nobody can. That's rather the point. | no — outcome-bound |
| 2nd | `29`→`44` | BALL | Not hard. Soft skin, full of air. I had it the moment they squeezed. | no — outcome-bound |
| 2nd | `31`→`48` | STICKMAN | Not smaller. Of course not. It's exactly your size. It has always been exactly your size. | no — outcome-bound |
| 2nd | `33`→`37` | HOUSE | A no. Felt it in the flywheel. | yes, but lands on a reveal |
| 3rd | `28`→`35` | question `35` | No. I knew — the same way I know you skipped Side A. We don't have to do this dance, you and I. | yes |
| 3rd | `30`→`46` | PLANE | They don't own one. Nobody owns one. It belongs to the sky, and to a leasing company. | no — outcome-bound |
| 3rd | `32`→`50` | BOAT | Not at home. It lives on the water. Most of the good ones do. | no — outcome-bound |
| 3rd | `34`→`40` | FLOWER | Smaller. I felt petals. I don't examine how. | no — outcome-bound |
| 4th | `35`→`42` | MOON | Can't touch it. I called that one from inside a cassette, which is where I live. | no — outcome-bound |

For comparison, the yes-reactions (same structure, same problem — 17 of them, all welded to the front of the segment they lead into):

| # of nos so far | Edge | Current reaction |
|---|---|---|
| 0 | `20`→`21` | There's the A. There's always an A. I'd act surprised, but we agreed to be honest with each other. |
| 0 | `21`→`22` | Two for two. Don't let it change you. |
| 0 | `22`→`23` | Three in a row. Statistically, you're due. |
| 0 | `23`→`52` | Four for four. It happens. Rarely, and to other people, but it happens. |
| 1 | `24`→`27` | The S. There it is. We're back, and we will never speak of the A again. |
| 1 | `25`→`29` | Held it. I felt the grip from in here. It's a strange life, being a tape. |
| 1 | `25m`→`25` | Agreed. Not alive. Progress — the small kind, but I've learned not to be picky. |
| 1 | `26`→`31` | Alive. I can hear it moving from here. |
| 1 | `27`→`33` | Touchable. Reach further. Say: |
| 1 | `29`→`43` | Hard. And cold. They didn't mention cold. They didn't have to. |
| 1 | `31`→`47` | Smaller. Warm. And profoundly uninterested in either of us. |
| 1 | `33`→`36` | Alive. And — hold on. |
| 2 | `28`→`34` | Alive. The impressions like you. The letters said nothing, which, for them, is warm. |
| 2 | `30`→`45` | They own one. I've ridden in it, in the sense that matters least. |
| 2 | `32`→`49` | At home. Naturally. You ate off yours this evening. We'll leave it there. |
| 2 | `34`→`39` | Bigger. Alive. And older than everyone involved. |
| 3 | `35`→`41` | Touchable. And somebody in this story has been holding its cousin the whole time. |

