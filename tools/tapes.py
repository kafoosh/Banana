# How to Read Minds: a home course on cassette.
# The full script and the graph that decides which recording plays next.
#
# What the spectator sees: one tape after another, numbered in order.
# What is true: every tape after the third exists in several recordings, and
# the way the performer presses NEXT chooses one.
#
# Writing rules for the voice (keep to these when editing):
#   - A coach on a how-to cassette. Short orders, plainly put: "Hand down."
#     "Eyes on your volunteer." "Slow down." It coaches what to do with the
#     body and the voice, and says nothing it doesn't need to.
#   - No pep talk and no commentary: nothing like "now the real reading
#     starts", "stay with it", "you have everything you need". If a sentence
#     gives the student nothing to do or say, cut it.
#   - Every tape must sound like the only version of that tape.
#   - The voice does not know what the volunteer answered. It never says
#     "they said yes", "it is alive", "no R". It only gives the next step.
#     The single exception is first_no(): the tape after the first no to a
#     letter on a route, whichever letter that is.
#   - Each tape gives the student something to do, then one line to say.
#   - The last tape coaches the student to make the reveal. The student says
#     it; the tape does not take over.
#
# Part syntax:
#   "text"           spoken
#   ("say", "text")  a line the student repeats; spoken slower
#   ("beat", 1.0)    silence, tape still running
#   ("page",)        the drawing appears here (last tapes only)
#
# Segment fields:
#   tape   the number on the label while it plays. Always one more than the
#          tape before it; routes differ in length, so the last tape is
#          number 6, 7 or 8.
#   next   "id"                    one recording follows, however NEXT is pressed
#          {"yes": id, "no": id}   a tap picks yes, a hold picks no
#          None                    end of the lesson
#   say    the line the student speaks
#   art    last tapes: which drawing appears

COURSE = "How to Read Minds"
NEXT = "Then play the next tape."
WAIT = "Wait for their answer. " + NEXT

S = {}


def seg(sid, tape, next, parts, say=None, art=None):
    S[sid] = {"tape": tape, "next": next, "parts": parts, "say": say, "art": art}


def ask(line, lead="Then ask:", after=WAIT):
    return [lead, ("beat", 0.4), ("say", line), ("beat", 0.9), after]


# ------------------------------------------------------------------ setting up

seg("t1", 1, "t2", [
    "Welcome to How to Read Minds, tape one. By the end of these lessons, you will read your first mind.",
    ("beat", 0.5),
    "It's easy! Just play the tapes and follow along.",
    ("beat", 0.6),
    "Sit your volunteer down in front of you, and play the next tape when you're ready!",
])

seg("t2", 2, "t3", [
    "Tape two. Ask your volunteer to imagine they are back in school.",
    ("beat", 0.5),
    "You're ten, maybe twelve, stuck in a boring class with a pencil in your hand, and you start to doodle.",
    ("beat", 0.5),
    "Something simple, that takes five or ten seconds. Like a smiley face, a mountain, or even a bicycle. Don't use those.",
    ("beat", 0.4),
    "And no plain shapes, like circles or triangles. Just a little drawing anybody would recognize. Keep it simple.",
    ("beat", 2.6),
    "Got it? Don't say it out loud.",
    ("beat", 0.7),
    "When you're ready, play the next tape.",
])

seg("t3", 3, {"yes": "t4y", "no": "t4n"}, [
    "Tape three. Your volunteer has a drawing. Good.",
    ("beat", 0.6),
    "Volunteer, picture the real thing in front of you, life size.",
    ("beat", 1.5),
    "Now think of it as a word. The simple word, the one a kid would use. If you drew a smiley face, you'd see a face, and think the word smiley.",
    ("beat", 0.6),
    "Spell the word in your head, one letter at a time.",
    ("beat", 3.0),
    "Again.",
    ("beat", 3.0),
    "Okay, mind reader. Your turn.",
    ("beat", 0.4),
    "Sit up. Two fingers on your temple. Look your volunteer in the eye.",
    ("beat", 0.5),
] + ask("There is an A in your word.", "Tell them:"), say="There is an A in your word.")

# ---------------------------------------------------------------------- letters
# From here on the voice does not say what the volunteer answered. The one
# exception is the first no to a letter, wherever on a route it comes.


def first_no(tape, letter):
    """Opens the tape that follows the first no on a route."""
    return [
        f"Tape {tape}. Your volunteer said no to the {letter}. Don't worry, they are supposed to.",
        ("beat", 0.6),
        "One letter in this course is always wrong on purpose. It's a test. Now you know they are telling you the truth.",
        ("beat", 0.7),
    ]


PICTURE = "Ask your volunteer to picture the thing in front of them again, life size."

seg("t4y", 4, {"yes": "t5yy", "no": "t5yn"}, [
    "Tape four. Keep your fingers where they are. Ask your volunteer to think of the whole word again.",
    ("beat", 1.4),
] + ask("And there is a T.", "Say:"), say="And there is a T.")

seg("t4n", 4, {"yes": "t5ny", "no": "t5nn"}, first_no("four", "A") + [
    "Fingers on your temple. Ask your volunteer to concentrate on the word.",
    ("beat", 1.2),
] + ask("There is an S.", "Say:"), say="There is an S.")

seg("t5yy", 5, {"yes": "t6s", "no": "t6r"}, [
    "Tape five. Slow down. Take a breath, and have your volunteer take one too.",
    ("beat", 1.6),
] + ask("I think there's an R.", "Don't sound so sure this time. Say:"), say="I think there's an R.")

seg("t5yn", 5, {"yes": "t6hold", "no": "final_stickman6"}, first_no("five", "T") + [
    "Hand down. No more letters.",
    ("beat", 0.5),
    "Look at the space between you, as if the thing were sitting there.",
    ("beat", 0.8),
] + ask("What you drew is not a living thing.", "Say this flat out:",
        "They may agree. They may correct you. Either is fine. " + NEXT),
    say="What you drew is not a living thing.")

seg("t5ny", 5, {"yes": "t6live", "no": "final_sun"}, [
    "Tape five. Hand down. No more letters.",
    ("beat", 0.5),
    PICTURE,
    ("beat", 1.2),
] + ask("Can you touch it?"), say="Can you touch it?")

seg("t5nn", 5, {"yes": "t6big", "no": "t6touch"}, [
    "Tape five. Hand down. Forget the letters.",
    ("beat", 0.5),
    PICTURE,
    ("beat", 1.2),
] + ask("Is it alive?"), say="Is it alive?")

# --------------------------------------------------------------- the thing itself

seg("t6s", 6, {"yes": "final_star", "no": "final_heart"}, [
    "Tape six. One more letter. Ask this one as a question.",
    ("beat", 0.5),
] + ask("I'm not sure about this one. Is there an S?", "Say:"),
    say="I'm not sure about this one. Is there an S?")

seg("t6r", 6, {"yes": "t7small", "no": "t7home"}, first_no("six", "R") + [
    "Hand down. No more letters.",
    ("beat", 0.5),
    PICTURE,
    ("beat", 1.2),
] + ask("Is it alive?"), say="Is it alive?")

seg("t6hold", 6, {"yes": "t7hard", "no": "t7own"}, [
    "Tape six. Hold your hands out, palms up.",
    ("beat", 0.9),
] + ask("Could you pick it up and hold it in your hands?"),
    say="Could you pick it up and hold it in your hands?")

seg("t6live", 6, {"yes": "final_fish", "no": "final_house"}, [
    "Tape six. Eyes on your volunteer. One more question.",
    ("beat", 0.6),
] + ask("Is it alive?", "Ask:"), say="Is it alive?")

seg("t6big", 6, {"yes": "final_tree", "no": "final_flower"}, [
    "Tape six. Ask your volunteer to stand next to it.",
    ("beat", 1.2),
] + ask("Is it bigger than you?"), say="Is it bigger than you?")

seg("t6touch", 6, {"yes": "final_pencil", "no": "final_moon"}, [
    "Tape six. Ask your volunteer to reach out toward it.",
    ("beat", 1.2),
] + ask("Can you touch it?"), say="Can you touch it?")

seg("t7small", 7, {"yes": "final_cat", "no": "final_stickman8"}, [
    "Tape seven. Ask your volunteer to stand next to it.",
    ("beat", 1.2),
] + ask("Is it smaller than you?"), say="Is it smaller than you?")

seg("t7home", 7, {"yes": "final_table", "no": "final_boat"}, [
    "Tape seven. Eyes on your volunteer. One more question.",
    ("beat", 0.6),
] + ask("Is there one in your home?", "Ask:"), say="Is there one in your home?")

seg("t7hard", 7, {"yes": "final_glass", "no": "final_ball"}, [
    "Tape seven. Ask your volunteer to close their hands around it.",
    ("beat", 1.2),
] + ask("Is it hard?"), say="Is it hard?")

seg("t7own", 7, {"yes": "final_car", "no": "final_plane"}, [
    "Tape seven. Eyes on your volunteer. One more question.",
    ("beat", 0.6),
] + ask("Do you own one?", "Ask:"), say="Do you own one?")

# -------------------------------------------------------------------- last tape
# The student makes the reveal. One recording per drawing; its number depends
# on how long the route was. The stick figure can be reached two ways.

WORD = {6: "six", 7: "seven", 8: "eight"}
DRAWINGS = {
    # id suffix: (art, tape number, the line)
    "sun":       ("sun", 6, "You drew the sun."),
    "stickman6": ("stickman", 6, "You drew a stick figure."),
    "fish":      ("fish", 7, "You drew a fish."),
    "house":     ("house", 7, "You drew a house."),
    "tree":      ("tree", 7, "You drew a tree."),
    "flower":    ("flower", 7, "You drew a flower."),
    "pencil":    ("pencil", 7, "You drew a pencil."),
    "moon":      ("moon", 7, "You drew the moon."),
    "star":      ("star", 7, "You drew a star."),
    "heart":     ("heart", 7, "You drew a heart."),
    "cat":       ("cat", 8, "You drew a cat."),
    "stickman8": ("stickman", 8, "You drew a stick figure."),
    "table":     ("table", 8, "You drew a table."),
    "boat":      ("boat", 8, "You drew a boat."),
    "glass":     ("glass", 8, "You drew a glass."),
    "ball":      ("ball", 8, "You drew a ball."),
    "car":       ("car", 8, "You drew a car."),
    "plane":     ("plane", 8, "You drew an airplane."),
}

for key, (art, n, line) in DRAWINGS.items():
    seg("final_" + key, n, None, [
        f"Tape {WORD[n]}. Last tape.",
        ("beat", 0.7),
        "Hands down. Look your volunteer in the eye. Take a breath.",
        ("beat", 1.8),
        "No question this time. Tell them:",
        ("beat", 0.4),
        ("say", line),
        ("beat", 2.4),
        ("page",),
        ("beat", 1.0),
        "That's lesson one. Well done.",
    ], say=line, art=art)

# File order. Names on disk are just numbers, so the folder says nothing.
ORDER = list(S)
START = "t1"


def check():
    for sid, s in S.items():
        n = s["next"]
        for t in ([] if n is None else [n] if isinstance(n, str) else [n["yes"], n["no"]]):
            assert t in S, f"{sid} -> missing {t}"
            assert S[t]["tape"] == s["tape"] + 1, f"{sid} -> {t} is not the next number"
    reached = set()

    def walk(sid):
        reached.add(sid)
        n = S[sid]["next"]
        for t in ([] if n is None else [n] if isinstance(n, str) else n.values()):
            walk(t)
    walk(START)
    assert reached == set(S), f"unreachable: {set(S) - reached}"
    assert len({s["art"] for s in S.values() if s["art"]}) == 17


check()

if __name__ == "__main__":
    # Print every route, to read the script the way one spectator hears it.
    def routes(sid, trail):
        n = S[sid]["next"]
        if n is None:
            yield trail + [sid]
        elif isinstance(n, str):
            yield from routes(n, trail + [sid])
        else:
            yield from routes(n["yes"], trail + [sid + "+"])
            yield from routes(n["no"], trail + [sid + "-"])
    for r in routes(START, []):
        print(S[r[-1]]["art"].ljust(9), " ".join(r[2:]))
