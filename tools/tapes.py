# How to Read Minds: a home course in eight cassettes.
# The full script and the graph that decides which recording plays next.
#
# What the spectator sees: seven numbered tapes and a red one, played in order.
# What is true: every tape after the third exists in several recordings, and
# the way the performer picks it out of the case chooses one.
#
# Writing rules for the voice (keep to these when editing):
#   - An upbeat how-to instructor. Encouraging, brisk, never surprised, never
#     joking, never aware of being a recording.
#   - Every tape must sound like the only version of that tape.
#   - The voice does not know what the volunteer answered. It never says
#     "they said yes", "it is alive", "no R". It only gives the next step.
#     The single exception is the tape after a no to the first letter.
#   - Each tape gives the student something to do, then one line to say.
#   - The red tape names the drawing. It does not describe it.
#
# Part syntax:
#   "text"           spoken
#   ("say", "text")  a line the student repeats; spoken slower
#   ("beat", 1.0)    silence, tape still running
#   ("page",)        the drawing appears here (red tapes only)
#
# Segment fields:
#   tape   1..7, or RED for the red tape: the label shown while it plays
#   next   "id"                    one recording follows, however it is picked
#          {"yes": id, "no": id}   a tap picks yes, a hold picks no
#          None                    end of the lesson
#   say    the line the student speaks, shown on screen while the tape plays
#   art    red tapes: which drawing is on the last page

COURSE = "How to Read Minds"
RED = 8      # tapes 1..7 are numbered; the eighth is the red one

S = {}


def seg(sid, tape, next, parts, say=None, art=None):
    S[sid] = {"tape": tape, "next": next, "parts": parts, "say": say, "art": art}


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
    "Tape three. Nice work! Your volunteer has a picture in mind. Now let's make it stronger.",
    ("beat", 0.6),
    "Volunteer, imagine the real thing, right in front of you, life size.",
    ("beat", 1.5),
    "Now think of it as a word. The simple word, the one a kid would use. If you had drawn a smiley face, you would see a face, and think the word smiley.",
    ("beat", 0.6),
    "Spell your word in your head, one letter at a time.",
    ("beat", 3.0),
    "And once more.",
    ("beat", 3.0),
    "Great. Now, mind reader, it's your turn.",
    ("beat", 0.4),
    "Put two fingers on your temple. Look your volunteer in the eye. Tell them:",
    ("beat", 0.4),
    ("say", "There is an A in your word."),
    ("beat", 0.9),
    "Wait for the answer. Then play tape four.",
], say="There is an A in your word.")

# ---------------------------------------------------------------------- letters
# From here on the voice does not say what the volunteer answered. The one
# exception is the no to the first letter.

seg("t4y", 4, {"yes": "t5yy", "no": "t5yn"}, [
    "Tape four. Keep your fingers on your temple. Ask your volunteer to picture the whole word again.",
    ("beat", 1.4),
    "Say:",
    ("beat", 0.4),
    ("say", "And there is a T."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape five.",
], say="And there is a T.")

seg("t4n", 4, {"yes": "t5ny", "no": "t5nn"}, [
    "Tape four. Your volunteer said no to the A. Don't worry, they are supposed to.",
    ("beat", 0.6),
    "The first letter in this course is always a test. It tells you they are answering honestly, and it shows you what a no looks like on this person's face.",
    ("beat", 0.7),
    "Now the real reading starts. Ask your volunteer to focus harder on the word. Fingers on your temple. Say:",
    ("beat", 0.4),
    ("say", "There is an S."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape five.",
], say="There is an S.")

seg("t5yy", 5, {"yes": "t6s", "no": "t6r"}, [
    "Tape five. Take a slow breath, and ask your volunteer to do the same.",
    ("beat", 1.6),
    "This time, be a little less certain. Say:",
    ("beat", 0.4),
    ("say", "I think there's an R."),
    ("beat", 0.9),
    "Then play tape six.",
], say="I think there's an R.")

seg("t5yn", 5, {"yes": "t6hold", "no": "t6man"}, [
    "Tape five. Perfect. Lower your hand. Now you are going to pick up the thing itself.",
    ("beat", 0.5),
    "Look at the space between the two of you, and tell them, firmly:",
    ("beat", 0.4),
    ("say", "What you drew is not a living thing."),
    ("beat", 0.9),
    "If they agree, fine. If they correct you, that is fine too. Then play tape six.",
], say="What you drew is not a living thing.")

seg("t5ny", 5, {"yes": "t6live", "no": "t6sun"}, [
    "Tape five. Lower your hand. Now you are going to pick up the thing itself.",
    ("beat", 0.5),
    "Ask your volunteer to keep seeing it, right in front of them, life size.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Can you touch it?"),
    ("beat", 0.9),
    "Then play tape six.",
], say="Can you touch it?")

seg("t5nn", 5, {"yes": "t6big", "no": "t6touch"}, [
    "Tape five. Now forget the letters. Lower your hand.",
    ("beat", 0.5),
    "Ask your volunteer to look at the thing itself, right in front of them.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    "Then play tape six.",
], say="Is it alive?")

# --------------------------------------------------------------- the thing itself

LAST = "Whatever they answer, don't say a word. You can skip tape seven. Play the red tape."
LAST7 = "Whatever they answer, don't say a word. Play the red tape."
ENOUGH = "That is everything you need. Don't ask anything else. You can skip tape seven. Play the red tape."

seg("t6s", 6, {"yes": "r_star", "no": "r_heart"}, [
    "Tape six. One more letter. This time, ask it as a question. Say:",
    ("beat", 0.4),
    ("say", "I'm not sure about this one. Is there an S?"),
    ("beat", 0.9),
    LAST,
], say="I'm not sure about this one. Is there an S?")

seg("t6r", 6, {"yes": "t7small", "no": "t7home"}, [
    "Tape six. Lower your hand. Now you are going to pick up the thing itself.",
    ("beat", 0.5),
    "Ask your volunteer to see it, right in front of them.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    "Then play tape seven.",
], say="Is it alive?")

seg("t6hold", 6, {"yes": "t7hard", "no": "t7own"}, [
    "Tape six. Hold out your hands, palms up. Then ask:",
    ("beat", 0.4),
    ("say", "Could you pick it up and hold it in your hands?"),
    ("beat", 0.9),
    "Then play tape seven.",
], say="Could you pick it up and hold it in your hands?")

seg("t6man", 6, "r_stickman", ["Tape six. " + ENOUGH])

seg("t6live", 6, {"yes": "r_fish", "no": "r_house"}, [
    "Tape six. One last question. Ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    LAST,
], say="Is it alive?")

seg("t6sun", 6, "r_sun", ["Tape six. " + ENOUGH])

seg("t6big", 6, {"yes": "r_tree", "no": "r_flower"}, [
    "Tape six. Ask your volunteer to stand right next to it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it bigger than you?"),
    ("beat", 0.9),
    LAST,
], say="Is it bigger than you?")

seg("t6touch", 6, {"yes": "r_pencil", "no": "r_moon"}, [
    "Tape six. One last question. Ask your volunteer to reach out toward it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Can you touch it?"),
    ("beat", 0.9),
    LAST,
], say="Can you touch it?")

seg("t7small", 7, {"yes": "r_cat", "no": "r_stickman"}, [
    "Tape seven. Ask your volunteer to stand right next to it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it smaller than you?"),
    ("beat", 0.9),
    LAST7,
], say="Is it smaller than you?")

seg("t7home", 7, {"yes": "r_table", "no": "r_boat"}, [
    "Tape seven. One last question. Ask:",
    ("beat", 0.4),
    ("say", "Is there one in your home?"),
    ("beat", 0.9),
    LAST7,
], say="Is there one in your home?")

seg("t7hard", 7, {"yes": "r_glass", "no": "r_ball"}, [
    "Tape seven. Ask your volunteer to close their hands around it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it hard?"),
    ("beat", 0.9),
    LAST7,
], say="Is it hard?")

seg("t7own", 7, {"yes": "r_car", "no": "r_plane"}, [
    "Tape seven. One last question. Ask:",
    ("beat", 0.4),
    ("say", "Do you own one?"),
    ("beat", 0.9),
    LAST7,
], say="Do you own one?")

# --------------------------------------------------------------------- red tape
# One recording per drawing. It names the drawing and nothing else.

DRAWINGS = {
    "fish": "You drew a fish.",
    "house": "You drew a house.",
    "sun": "You drew the sun.",
    "tree": "You drew a tree.",
    "flower": "You drew a flower.",
    "pencil": "You drew a pencil.",
    "moon": "You drew the moon.",
    "glass": "You drew a glass.",
    "ball": "You drew a ball.",
    "car": "You drew a car.",
    "plane": "You drew an airplane.",
    "cat": "You drew a cat.",
    "stickman": "You drew a person. A stick figure.",
    "table": "You drew a table.",
    "boat": "You drew a boat.",
    "heart": "You drew a heart.",
    "star": "You drew a star.",
}

for key, name in DRAWINGS.items():
    seg("r_" + key, RED, None, [
        "This is the red tape.",
        ("beat", 0.7),
        "You have done your part, and you did great. Hands in your lap. I will finish this one, so you can see how it should feel.",
        ("beat", 0.9),
        "Volunteer: you never said what you drew. Not to my student, and not to me.",
        ("beat", 1.3),
        name,
        ("page",),
        ("beat", 2.0),
        "And that is how you read a mind! Congratulations on finishing lesson one.",
    ], art=key)

# File order. Names on disk are just numbers, so the folder says nothing.
ORDER = list(S)
START = "t1"


def check():
    for sid, s in S.items():
        n = s["next"]
        targets = [] if n is None else [n] if isinstance(n, str) else [n["yes"], n["no"]]
        for t in targets:
            assert t in S, f"{sid} -> missing {t}"
            step = S[t]["tape"] - s["tape"]
            assert step >= 1, f"{sid} -> {t} goes backwards"
            assert step == 1 or S[t]["tape"] == RED, f"{sid} -> {t} skips to a numbered tape"
    reached = set()

    def walk(sid):
        reached.add(sid)
        n = S[sid]["next"]
        for t in ([] if n is None else [n] if isinstance(n, str) else n.values()):
            walk(t)
    walk(START)
    assert reached == set(S), f"unreachable: {set(S) - reached}"
    assert {s["art"] for s in S.values() if s["art"]} == set(DRAWINGS)


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
