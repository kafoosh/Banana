# Proteus / "MindPeek" — Method Specification

> **Purpose of this file.** Complete, self-contained specification of the drawing-divination
> method from *Proteus* by Phedon Bilek, documented so that an AI (or human) working on this
> repo can implement the web app without access to the source book. Compiled from the owner's
> photos of the book's interactive demo (pages ~17–52) and explanation chapter (pages ~54–67).
>
> **Attribution / sensitivity.** The method is Phedon Bilek's commercial work. This file
> paraphrases the system for the owner's personal project; keep the repo private and do not
> republish the book's text or reveal the method in any user-facing copy. The entire product
> is the secret: the app must never explain *how* it works to the spectator.

---

## 1. The effect

The spectator imagines drawing a simple childhood doodle (they never write or say anything).
They answer a short series of YES/NO questions. The app then reveals the exact drawing they
were merely thinking of.

The book performs this as a "choose your own adventure": each page makes one statement or
question with "Yes → turn to page X / No → turn to page Y", terminating on a full-page image
of the spectator's drawing. **The web app replicates exactly this experience.**

It is a trick, not statistics-at-runtime: the opening script *funnels* the spectator into a
closed set of **17 outcomes**, and the questions traverse a fixed decision tree (a
**progressive anagram** plus a few property probes) that identifies which one.

---

## 2. Principle A — The funnel (priming script)

Delivered BEFORE any questions. Every element is load-bearing:

1. **Regression framing:** "Imagine you're in school, about **ten to twelve years old**,
   waiting for the end of a boring class. You're holding a pencil and find yourself doodling."
   → restricts the repertoire to child-level doodles.
2. **Effort bounds:** "A simple drawing that takes **five to ten seconds**, nothing too
   complicated."
3. **The exclusion list:** "Something like a **SMILEY FACE**, a **MOUNTAIN**, or even a
   **BICYCLE** — don't pick these, of course, and please **no geometrical shapes** like
   circles or triangles. Something **anybody would easily recognize**."
   - Openly discards those exact answers, AND covertly sets difficulty bounds. The spectator
     unconsciously calibrates: `SMILEY < their drawing < BICYCLE` in complexity.
   - Bilek's claim from experience: with this framing, essentially everyone lands inside the
     17 outs. (A determined artist might draw a horse — the framing prevents that thought.)
4. **The word pre-commitment (critical):** "Picture the object depicted in your doodle in
   front of you, **in real size**. Also think of it **AS A WORD** — if you'd drawn a smiley
   face you'd think of a real face and the word SMILEY. In your mind, please **review the
   letters in the word one by one**... good... again."
   - Real-size visualization enables later size/touch probes.
   - Letter review makes the letter questions answerable and feels innocent because it is
     requested before the spectator knows letters will matter.
5. If the spectator hesitates, apply mild pressure: "Don't make it complicated."

---

## 3. Principle B — The A(S)TRS progressive anagram

Letter sequence **A → T → R → S**, with a side branch **S** used when A misses.

- **YES on a letter → move vertically** (ask the next letter in the sequence).
- **NO on a letter → move horizontally** (stop asking letters; you now know the outcome
  *group*; finish with property probes).
- Letters are **stated as confident impressions, never asked**: "I can feel an **A** among
  the letters you just saw... correct?" A miss is absorbed by showmanship (see §6).
- At most 4 letter steps ever occur. Most spectators' drawings resolve on A or S, so T/R are
  rarely reached.

### The graph and the 17 outs

| Letter path | Group (outs, in descending likelihood) | Outs |
|---|---|---|
| A✗ → S✓ | **House / Sun / Fish** | 3 |
| A✗ → S✗ | **Tree / Flower / Pen-Pencil / Moon** | 4 |
| A✓ → T✗ | **Car / Ball / Plane / Glass** | 4 |
| A✓ → T✓ → R✗ | **Boat / Stickman / Cat / Table** | 4 |
| A✓ → T✓ → R✓ → S✓ | **Star** | 1 |
| A✓ → T✓ → R✓ → S✗ | **Heart** | 1 |

Sanity check (letters of each word vs. its path): FISH, HOUSE, SUN contain S but no A.
TREE, FLOWER, PEN/PENCIL, MOON contain neither A nor S. GLASS, BALL, CAR, PLANE contain A
but no T. BOAT, STICKMAN, CAT, TABLE contain A+T but no R. HEART contains A+T+R but no S.
STAR contains A+T+R+S. ✓

Groups are listed above in the book's "order of likeliness"; within each group the outs are
also ordered by likelihood (House > Sun > Fish, etc.). A live performer uses this ordering to
lead with the strongest guess; in the strict yes/no tree it has no mechanical role.

### Optional group mnemonics (performer memory aids)

- A house under the sun, with a pond (fish) near it.
- A tree whose branches are pencils, flowers stemming from its bark, the moon above.
- A car with soccer-ball wheels racing a giant flying champagne glass.
- A boat with a stickman skipping on the deck, and a table with a cat on top.

---

## 4. Principle C — Within-group property probes

After a NO drops you into a group, 1–2 sensory-sounding questions isolate the drawing. All
are phrased as psychic impressions ("Imagine you're touching it... I sense life..."), never
as elimination logic. The objects were visualized **in real size** (per the script), which is
what makes touch/hold/size questions meaningful.

- **House / Sun / Fish:** "Can you TOUCH it?" — NO → **SUN** (untouchable).
  YES → "Is it ALIVE?" — YES → **FISH**, NO → **HOUSE**.
- **Tree / Flower / Pencil / Moon:** "Is it ALIVE?" — YES → "Compared to you, is it
  BIGGER?" — YES → **TREE**, NO → **FLOWER**. NO (not alive) → "Can you TOUCH it?" —
  YES → **PEN/PENCIL**, NO → **MOON**.
- **Car / Ball / Plane / Glass:** "Can you HOLD it in your hand?" — YES → "Is its surface
  HARD?" — YES → **GLASS** (cold, hard), NO → **BALL**. NO (can't hold) → "Do you OWN
  one?" — YES → **CAR**, NO → **PLANE**.
- **Boat / Stickman / Cat / Table:** "Is it ALIVE?" — YES → "Compared to you, is it
  SMALLER?" — YES → **CAT**, NO → **STICKMAN**. NO (not alive) → "Do you have one at
  HOME?" — YES → **TABLE**, NO → **BOAT**.
- **Heart / Star:** no probe needed; the final S letter already splits them
  (S✓ → STAR, S✗ → HEART).

Live-performance adaptations (not needed for a strict yes/no app, but good to know):
- OWN-a-car depends on demographics; alternatives: "Do you use one often?" / "When did you
  last use one?" (A wealthy spectator may own a plane — adapt.)
- A "hard ball" (bowling ball) is a rare spoiler the author jokes about; ignored.

---

## 5. The exact book tree (canonical spec for the app)

Node ids are the book's page numbers, for traceability. `L:` = letter statement,
`P:` = property probe, `R:` = reveal.

```json
{
  "start": 20,
  "nodes": {
    "20": { "kind": "letter",  "ask": "A",                      "yes": 21, "no": 24 },
    "21": { "kind": "letter",  "ask": "T",                      "yes": 22, "no": 25 },
    "22": { "kind": "letter",  "ask": "R",                      "yes": 23, "no": 26 },
    "23": { "kind": "letter",  "ask": "S",                      "yes": 52, "no": 51 },
    "24": { "kind": "letter",  "ask": "S",                      "yes": 27, "no": 28 },
    "25": { "kind": "probe",   "ask": "hold_in_hands",          "yes": 29, "no": 30 },
    "26": { "kind": "probe",   "ask": "alive",                  "yes": 31, "no": 32 },
    "27": { "kind": "probe",   "ask": "can_touch",              "yes": 33, "no": 38 },
    "28": { "kind": "probe",   "ask": "alive",                  "yes": 34, "no": 35 },
    "29": { "kind": "probe",   "ask": "surface_hard",           "yes": 43, "no": 44 },
    "30": { "kind": "probe",   "ask": "own_one",                "yes": 45, "no": 46 },
    "31": { "kind": "probe",   "ask": "smaller_than_you",       "yes": 47, "no": 48 },
    "32": { "kind": "probe",   "ask": "have_one_at_home",       "yes": 49, "no": 50 },
    "33": { "kind": "probe",   "ask": "alive",                  "yes": 36, "no": 37 },
    "34": { "kind": "probe",   "ask": "bigger_than_you",        "yes": 39, "no": 40 },
    "35": { "kind": "probe",   "ask": "can_touch",              "yes": 41, "no": 42 },
    "36": { "kind": "reveal",  "out": "FISH" },
    "37": { "kind": "reveal",  "out": "HOUSE" },
    "38": { "kind": "reveal",  "out": "SUN" },
    "39": { "kind": "reveal",  "out": "TREE" },
    "40": { "kind": "reveal",  "out": "FLOWER" },
    "41": { "kind": "reveal",  "out": "PENCIL" },
    "42": { "kind": "reveal",  "out": "MOON" },
    "43": { "kind": "reveal",  "out": "GLASS" },
    "44": { "kind": "reveal",  "out": "BALL" },
    "45": { "kind": "reveal",  "out": "CAR" },
    "46": { "kind": "reveal",  "out": "PLANE" },
    "47": { "kind": "reveal",  "out": "CAT" },
    "48": { "kind": "reveal",  "out": "STICKMAN" },
    "49": { "kind": "reveal",  "out": "TABLE" },
    "50": { "kind": "reveal",  "out": "BOAT" },
    "51": { "kind": "reveal",  "out": "HEART" },
    "52": { "kind": "reveal",  "out": "STAR" }
  }
}
```

Reveal art in the book (guides icon choice): fish; house with fence; sun; tree; flower with
leaf; pencil; crescent moon with three stars; martini glass with olive (= "glass");
basketball (= "ball"); car side view; airliner silhouette; cat; restroom-sign person
(= "stickman"); table; sailboat; heart; five-pointed star.

Depth: best case 2 questions (A✗→S✓... actually 3 to reveal for House group; STAR/HEART
resolve after 4 letter statements; worst case 5 questions total). Every leaf is reached in
3–5 questions.

---

## 6. The patter layer (what makes it deceptive)

The book's question pages model the emotional arc; the app's copy should reproduce the
*function* of each beat (paraphrase freely, keep the beats):

1. **Letters are claimed, not queried.** "I can feel an A among the letters you just saw...
   correct?" — then "I see a T as well!", "Is that an R?", each more tentative as the
   sequence deepens ("Now I'm not sure, but... an S?"). Confidence tapers naturally.
2. **Misses become transitions.** After a NO, the performer stumbles *forward*:
   - First miss (A✗): "Oh! Er... maybe that's an S!"
   - Second miss (A✗,S✗): "Really, I'm completely off! **Please forget the letters.**
     I sense... wait... is it ALIVE?" — pivots from letters to "impressions" exactly when
     letters stop paying, disguising that the misses were informative.
   - Property probes open with false continuity: "I thought so...", "I felt so...",
     "Very fuzzy... wait!"
3. **Reframes soften NOs** (Kenton Knepper style): after House is known ("alive? no"):
   "BUT your object can relate to LIFE, right?" — converts a miss-feeling into a hit-feeling.
4. **Misdirection about the mechanism:** the letter statements read as psychic feats, the
   probes read as sharpening impressions; neither reads as binary search.

---

## 7. Known edge cases and contingencies

- **Stickman thought of as "MAN" (no T!).** The book's live fix: after any NO on T, declare
  "It's definitely NOT a living thing!" If the spectator objects, they're thinking of a
  man → treat as the Stickman/person outcome (it "moves" to the Car group). The printed
  CYOA tree does NOT include this safety valve; it silently risks the miss.
  **App decision: add an optional check on the T-NO branch** (e.g. a quick "it is NOT a
  living thing... right?" step where a "wrong, it IS alive" answer reroutes to STICKMAN),
  or faithfully accept the book's risk.
- **HOUSE vs "HOME":** if a spectator words their house doodle as "HOME" the letters derail
  (no A, no S → wrong group). The script's phrasing ("something anybody would recognize",
  childhood doodle) plus the word-review step keep nearly everyone on concrete nouns like
  HOUSE. Accepted residual risk; no fix in the book.
- **Off-list drawings (e.g. DOG):** prevented by the funnel, not the tree. If it happens
  live, the performer steers or fails gracefully; the app can end with a near-miss reveal
  or a playful "your mind is unusually guarded" out. (Book offers no mechanism — the funnel
  is the mechanism.)
- **PEN vs PENCIL** is a single out (either counts; reveal art is a pencil).
- **Spelled variants that still work:** AIRPLANE/AEROPLANE (A✓,T✗ → plane group → can't
  hold, don't own → PLANE ✓), SAILBOAT (A✓,T✓,R✗ → boat group ✓). The tree is robust to
  several synonym spellings because the groups' probes don't depend on exact letters.

---

## 8. App design notes (agreed direction)

- **Spectator-facing web app that plays the book's role**: priming screen(s) with the full
  funnel script → yes/no question flow per §5 tree → full-screen reveal image.
- Include the **Man contingency** as a configurable option (default on).
- Copy should be **paraphrased patter** with the same beats (§6), not the book's verbatim
  text.
- Never expose method words like "anagram", "tree", "elimination" anywhere user-visible.
- Reveal should land as the climax: consider a beat of silence/blank before showing the
  drawing.
- Nice-to-have (from the book's structure): a hidden performer/debug mode showing current
  node + remaining candidates, for development only.
