# Design

A reassessment of the trick from the method up. `METHOD.md` is unchanged: the
funnel, the letters and the questions are the book's. Everything a spectator
sees or hears was rebuilt.

## What was wrong before

**The frame fought the method.** One long file in a media player, pausing
itself and waiting. A recording that stops and waits for input is already
behaving like a program.

**The secret press was visible in principle.** Left half of the button for no,
right half for yes. A different place for a different answer is the one thing
a suspicious spectator can watch for, and a press near the middle was a coin
toss.

**The voice was winking.** Gerald announced up front that he would "know", and
every line was a joke about being a tape. Each no was treated as the student's
failure. That tells the audience the recording is reacting, which is the one
thing it must not seem to do.

**The look was a joke skin.** A fake shareware player with a nag banner. The
trick needs the spectator to believe in a fixed set of old recordings.

## What it is now

**A course in separate tapes.** Each tape gives one step and ends. A tape
ending is what tapes do. The student does the step, then takes the next tape
out of the case. The numbered tapes going back into the case one by one are
the proof that this is a fixed sequence.

**Every tape was meant to be.** Each tape opens by stating what just happened
as the next step of the course. After a yes it builds on it. After a no, the
no was the purpose of the step, and the student did it right. Nothing ever
goes wrong and nobody is told to recover. Each no has its own purpose:

| After | Why the course wanted it |
|---|---|
| No A | The first letter is always a test: it shows they answer honestly, and what a no looks like on this person. |
| No A, then no S | The result it was looking for: a picture thinker, the easiest kind to read. Forget letters. |
| No T, after a yes | After a first hit the course always gives a letter that isn't there. It is the signal to move on. |
| No R | The signal that the letters are finished. They always run out. |
| "Not a living thing" corrected | That is what the step is for: people correct a mistake faster than they answer a question. |
| Can't touch it | The most useful answer in lesson one. |

Each tape also gives the student something to do: fingers on the temple, a
slow breath, hands out palms up. That gives every tape the shape of a lesson
step, and gives the no-tapes something to adjust ("ask them to focus harder").

**The pick is the input.** The next tape is taken from the case by touching
it. A tap is yes; a finger rested on it until it lifts is no. Same tape, same
finger, same place. The lift is the confirmation: it happens as the finger
leaves, or under it. Only the next tape in order responds, so nothing can be
played out of sequence. Every version of a tape is identical for its first
three seconds, and REWIND in that window puts it back in the case unplayed.

**The red tape.** It sits in the case from the start and tape 1 says to save
it for last. The final question on every route ends "whatever they answer,
don't say a word; play the red tape". The red tape tells the student to put
their hands in their lap, speaks to the participant, describes two features of
the drawing, names it, and sends them to the last page of the booklet.

Routes differ in length (three to five answers), so tape 8 is often skipped.
The tape says so. Two routes resolve before a final question and get a short
tape that says "That is everything you need."

**The voice.** A friendly how-to instructor: encouraging, clear, never
surprised, never joking. The tapes talk to the participant directly for the
two steps whose wording carries the method, with a reason given ("this part
has to be done just right, so I will talk to them myself"). The voice never
recites what has been learned. Rules are at the top of `tools/tapes.py`.

**The look.** The inside of a cassette album: a paper title plate, the tape in
the player, nine tapes on edge in the tray, the typed booklet, three keys.
Flat printed and moulded surfaces, two typefaces (Libre Franklin for printed
labels, Courier Prime for the typed booklet), one spot colour plus the red.
Played tapes go back the other way round. The booklet shows the line the
student has to say. Its last page is a leaf from a school notebook with the
doodle in pencil, which is where tape 2 told the participant they drew it.

## Method notes

- The tree is the book's, with the "not a living thing" check kept on the no-T
  branch.
- Tape 3 adds "use the simple word, the one a kid would use", to pull people
  off ROSE and towards FLOWER.
- Red-tape details are chosen to be true of nearly any child's version (fish
  from the side, crescent moon, lines on the ball).
- Not solved: a drawing outside the seventeen. The frame covers it, since a
  first-lesson student is allowed to fail, but the red tape will still name
  the wrong thing.

## Not verified

The recordings were checked by phoneme output, level and timing, not by ear.
Listen to a full route before performing. The letter A is respelled for the
synthesiser (`LETTER_A` in `tools/build_audio.py`), since it otherwise reads
"an A" as "an uh".
