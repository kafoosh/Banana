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
failure, and each yes was celebrated. That tells the audience the recording is reacting, which is the one
thing it must not seem to do.

**The look was a joke skin.** A fake shareware player with a nag banner. The
trick needs the spectator to believe in a fixed set of old recordings.

## What it is now

**A course in separate tapes.** Each tape gives one step and ends. A tape
ending is what tapes do. The student does the step, then puts on the next
tape. The number on the label goes up by one each time. Routes differ in
length, so the last tape is number 6, 7 or 8; nothing is skipped and nothing
on screen says how many there are.

**The tape does not know.** No tape says what the volunteer answered. There
is no "you got the A", no "it is alive", no "no R". Each tape gives the next
step and the next line, and that step is always the right one.

The one exception is the first no to a letter on a route, whichever letter it
is (A, T or R): "Your volunteer said no to the T. Don't worry, they are
supposed to. One of the letters in this course is always a test." It is the
moment a first-time student would otherwise look lost, and it is said once.

**A coach.** The voice coaches the delivery: sit up straight, fingers on the
temple, don't mumble, sound a little less certain this time, relax your
shoulders, ask gently. That gives every tape something to say that has nothing
to do with the answer.

**The student makes the reveal.** The last tape says it is the last one, has
the student lower their hands, look the volunteer in the eye and take a
breath, and then gives the line: "You drew a fish." The student says it. The
drawing appears on the paper a moment later. The tape does not take over.

**One key.** NEXT TAPE. A tap is yes; a press held until the key latches is
no. Same key, same thumb, same place. The click is the confirmation: it comes
as the thumb lifts, or under it. Every version of a tape is identical for its
first three seconds, and REWIND in that window takes it back out.

**The look.** A player, a sheet of paper, four keys. Flat printed and moulded
surfaces, two typefaces (Libre Franklin for print, Courier Prime for the typed
sheet), one spot colour. Nothing is labelled unless the object itself would
carry the label: the cassette has the course title and its number, the keys
have their symbols.

**The paper.** Before the first tape it is the cover. While a tape plays it is
a transcript, typed out in time with the voice, with the line the student has
to repeat set heavier. At the end it is a leaf from a school notebook with the
doodle in pencil.

**Any screen.** Upright it is one column: player, paper, keys. Wider than tall
the player and keys go on the left and the paper on the right.

## Method notes

- The tree is the book's, with the "not a living thing" check kept on the no-T
  branch.
- Tape 3 adds "use the simple word, the one a kid would use", to pull people
  off ROSE and towards FLOWER.
- Not solved: a drawing outside the seventeen. The frame covers it, since a
  first-lesson student is allowed to fail, but the last tape will still give
  the wrong line.

## Not verified

The recordings were checked by phoneme output, level and timing, not by ear.
Listen to a full route before performing. The letter A is respelled for the
synthesiser (`LETTER_A` in `tools/build_audio.py`), since it otherwise reads
"an A" as "an uh".
