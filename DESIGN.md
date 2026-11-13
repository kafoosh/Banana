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
ending is what tapes do. The student does the step, then takes the next tape
out of the case. The numbered tapes going back into the case one by one are
the proof that this is a fixed sequence.

**The tape does not know.** No tape says what the volunteer answered. There
is no "you got the A", no "it is alive", no "no R". Each tape gives the next
step and the next line, and that step is always the right one. The spectator
hears a recording that never reacts and still ends up exactly where it should.

The one exception is the first no to a letter on a route, whichever letter it
is (A, T or R): "Your volunteer said no to the T. Don't worry, they are
supposed to. One of the letters in this course is always a test." It is the
moment a first-time student would otherwise look lost, and it is said once.

Each tape also gives the student something to do: fingers on the temple, a
slow breath, hands out palms up.

**The pick is the input.** The next tape is taken from the case by touching
it. A tap is yes; a finger rested on it until it lifts is no. Same tape, same
finger, same place. The lift is the confirmation: it happens as the finger
leaves, or under it. Only the next tape in order responds, so nothing can be
played out of sequence. Every version of a tape is identical for its first
three seconds, and REWIND in that window puts it back in the case unplayed.

**The red tape.** It sits in the case from the start and tape 1 says to save
it for last. The final question on every route ends "whatever they answer,
don't say a word; play the red tape". The red tape tells the student to put
their hands in their lap, speaks to the volunteer, names the drawing, and the drawing appears on the paper.

Routes differ in length (three to five answers), so tape 7 is often skipped.
The tape says so. Two routes resolve before a final question and get a short
tape that says "That is everything you need."

**The voice.** An upbeat how-to instructor: encouraging, brisk, never
surprised, never joking. The tape talks to the
volunteer directly for the passages whose wording carries the method
("Volunteer, imagine the real thing"), so a first-timer cannot get them wrong. The voice never
recites what has been learned. Rules are at the top of `tools/tapes.py`.

**The look.** A player, a sheet of paper, the tapes on edge, three keys. Flat
printed and moulded surfaces, two typefaces (Libre Franklin for print, Courier
Prime for the typed sheet), one spot colour plus the red. Nothing is labelled
unless the object itself would carry the label: the cassette has the course
title and its number, the keys have their symbols, and that is all. Played
tapes go back the other way round.

**The paper.** Before the first tape it is the cover. While a tape plays it is
a transcript, typed out in time with the voice, with the line the student has
to repeat set heavier. At the end it is a leaf from a school notebook with the
doodle in pencil.

**Any screen.** Upright it is one column: player, paper, tapes, keys. Wider
than tall (a phone on its side, a tablet, a laptop) the player and keys go on
the left, the paper and tapes on the right. Sizes scale
with the height of the screen.

## Method notes

- The tree is the book's, with the "not a living thing" check kept on the no-T
  branch.
- Tape 3 adds "use the simple word, the one a kid would use", to pull people
  off ROSE and towards FLOWER.
- Not solved: a drawing outside the seventeen. The frame covers it, since a
  first-lesson student is allowed to fail, but the red tape will still name
  the wrong thing.

## Not verified

The recordings were checked by phoneme output, level and timing, not by ear.
Listen to a full route before performing. The letter A is respelled for the
synthesiser (`LETTER_A` in `tools/build_audio.py`), since it otherwise reads
"an A" as "an uh".
