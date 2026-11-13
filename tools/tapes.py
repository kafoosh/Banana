# How to Read Minds: a home course in nine cassettes.
# The full script and the graph that decides which recording plays next.
#
# What the spectator sees: eight numbered tapes and a red one, played in order.
# What is true: every tape after the fourth exists in several recordings, and
# the way the performer picks it out of the case chooses one.
#
# Writing rules for the voice (keep to these when editing):
#   - A friendly how-to instructor. Encouraging, clear, never surprised, never
#     joking, never aware of being a recording.
#   - Every tape must sound like the only version of that tape. It opens by
#     saying what just happened as the step the course always takes next.
#   - After a YES the lesson builds on it.
#   - After a NO, the no was the point of the step: a test, a signal, a sorting
#     question. The student did it right. Each NO has its own purpose, and no
#     purpose is used twice on one route.
#   - Each tape gives the student something to do (hands, breath, where to
#     look) and then one line to say.
#   - Nothing ever "goes wrong", and the voice never tells the student to
#     recover, cover, or carry on.
#
# Part syntax:
#   "text"           spoken
#   ("say", "text")  a line the student repeats; spoken slower
#   ("beat", 1.0)    silence, tape still running
#   ("page",)        the booklet turns to its last page here (red tapes only)
#
# Segment fields:
#   tape   1..8, or 9 for the red tape: the label shown while it plays
#   next   "id"                    one recording follows, however it is picked
#          {"yes": id, "no": id}   a tap picks yes, a hold picks no
#          None                    end of the lesson
#   note   booklet text for this tape
#   say    the line the student speaks, printed in the booklet
#   art    red tapes: which drawing is on the last page

COURSE = "How to Read Minds"

S = {}


def seg(sid, tape, next, parts, note="", say=None, art=None):
    S[sid] = {"tape": tape, "next": next, "parts": parts,
              "note": note, "say": say, "art": art}


# ------------------------------------------------------------------ setting up

seg("t1", 1, "t2", [
    "Welcome to How to Read Minds. This is lesson one, tape one.",
    ("beat", 0.6),
    "In this lesson, you will read one thought from one person: a simple picture they are thinking of. You don't need any experience. Just follow the tapes.",
    ("beat", 0.6),
    "There are nine cassettes in your case. Eight are numbered, and one is red. Save the red one for last.",
    ("beat", 0.6),
    "Each tape gives you one step. When the tape stops, do the step. Then play the next tape. Always in order.",
    ("beat", 0.6),
    "First, find a participant. Sit them across from you, with the player between you.",
    ("beat", 0.7),
    "When they are ready, play tape two.",
], note="Find a participant. Sit them across from you, with the player between you. Then play tape 2.")

seg("t2", 2, "t3", [
    "Tape two. The first step is to put a clear picture in your participant's mind.",
    ("beat", 0.4),
    "This part has to be done just right, so I will talk to them myself. Listen to how I do it.",
    ("beat", 0.9),
    "Hello, and thank you for helping out.",
    ("beat", 0.5),
    "I'd like you to think back to school. You are about ten years old, maybe twelve. It's a long, boring afternoon in class. There is a pencil in your hand, and you start to doodle in the margin of your notebook.",
    ("beat", 0.8),
    "It's a simple little drawing. It takes five seconds, maybe ten. Nothing complicated.",
    ("beat", 0.6),
    "Something like a smiley face, or a mountain, or even a bicycle. Don't use those. I just said them.",
    ("beat", 0.4),
    "And no plain shapes, like circles or triangles. Draw a real thing. Something anybody would recognize.",
    ("beat", 2.2),
    "If you're stuck, you are making it too complicated.",
    ("beat", 1.5),
    "Keep it to yourself. Don't say it out loud.",
    ("beat", 0.8),
    "When your participant nods, play tape three.",
], note="Let the tape talk to your participant. When they nod, play tape 3.")

seg("t3", 3, "t4", [
    "Tape three. Now we make the picture stronger. I'll keep talking to your participant.",
    ("beat", 0.8),
    "Take your drawing off the page. Imagine the real thing, right in front of you, life size.",
    ("beat", 1.6),
    "Now think of it as a word. Use the simple word, the one a kid would use. If you drew a smiley face, you would be seeing a face, and thinking the word smiley.",
    ("beat", 0.7),
    "Spell your word in your mind. See each letter, one at a time.",
    ("beat", 3.0),
    "One more time. Slowly.",
    ("beat", 3.2),
    "Good. Hold on to that word.",
    ("beat", 0.8),
    "When they tell you they have it, play tape four.",
], note="When they tell you they have their word, play tape 4.")

# ---------------------------------------------------------------------- letters

seg("t4", 4, {"yes": "t5y", "no": "t5n"}, [
    "Tape four. Now it's your turn. Beginners pick up letters before pictures, so we start with the word.",
    ("beat", 0.6),
    "Put two fingers on your temple. Look at your participant. You are not going to ask. You are going to tell them. Say:",
    ("beat", 0.4),
    ("say", "There is an A in your word."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape five.",
], note="Two fingers on your temple. Tell them, don't ask. Wait for their answer, then play tape 5.",
   say="There is an A in your word.")

seg("t5y", 5, {"yes": "t6yy", "no": "t6yn"}, [
    "Tape five. Now that you have the A, the next letter comes easier.",
    ("beat", 0.5),
    "Keep your fingers on your temple. Ask your participant to picture the whole word again.",
    ("beat", 1.4),
    "Say:",
    ("beat", 0.4),
    ("say", "And there is a T."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape six.",
], note="Fingers on your temple. Have them picture the whole word again. Then play tape 6.",
   say="And there is a T.")

seg("t5n", 5, {"yes": "t6ny", "no": "t6nn"}, [
    "Tape five. Your participant said no to the A. They are supposed to.",
    ("beat", 0.6),
    "The first letter in this course is always a test. It tells you they are answering honestly, and it shows you what a no looks like on this person's face.",
    ("beat", 0.7),
    "Now the real reading starts. Ask your participant to focus harder on the word. Fingers on your temple. Say:",
    ("beat", 0.4),
    ("say", "There is an S."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape six.",
], note="That was the test letter. Ask them to focus harder. Then play tape 6.",
   say="There is an S.")

seg("t6yy", 6, {"yes": "t7s", "no": "t7r"}, [
    "Tape six. An A and a T. You have a real connection going, so don't rush it.",
    ("beat", 0.5),
    "Take a slow breath, and ask your participant to do the same.",
    ("beat", 1.6),
    "This time, be a little less certain. Say:",
    ("beat", 0.4),
    ("say", "I think there's an R."),
    ("beat", 0.9),
    "Then play tape seven.",
], note="A slow breath, both of you. Be a little less certain. Then play tape 7.",
   say="I think there's an R.")

seg("t6yn", 6, {"yes": "t7hold", "no": "t7man"}, [
    "Tape six. That one was a no. Good.",
    ("beat", 0.5),
    "After your first hit, this course always gives you a letter that isn't there. It keeps you from getting carried away, and it is your signal to move on from letters.",
    ("beat", 0.7),
    "Lower your hand. Now you are going to pick up the thing itself. Look at the space between the two of you, and tell them, firmly:",
    ("beat", 0.4),
    ("say", "What you drew is not a living thing."),
    ("beat", 0.9),
    "If they agree, fine. If they correct you, that is fine too. Then play tape seven.",
], note="Lower your hand. Say it firmly. Agree or correct, either is fine. Then play tape 7.",
   say="What you drew is not a living thing.")

seg("t6ny", 6, {"yes": "t7live", "no": "t7sun"}, [
    "Tape six. There is your S. One letter is all we need from the word.",
    ("beat", 0.6),
    "Lower your hand. Now you are going to pick up the thing itself. Ask your participant to keep seeing it, right in front of them, life size.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Can you touch it?"),
    ("beat", 0.9),
    "Then play tape seven.",
], note="Lower your hand. Have them see it in front of them, life size. Then play tape 7.",
   say="Can you touch it?")

seg("t6nn", 6, {"yes": "t7big", "no": "t7touch"}, [
    "Tape six. Two no's in a row. That is the result we were looking for.",
    ("beat", 0.6),
    "It tells you your participant thinks in pictures, not in words. Picture thinkers are the easiest people to read.",
    ("beat", 0.7),
    "So forget the letters. Lower your hand. Ask your participant to look at the thing itself, right in front of them.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    "Then play tape seven.",
], note="A picture thinker. Forget the letters. Have them look at the thing itself. Then play tape 7.",
   say="Is it alive?")

# --------------------------------------------------------------- the thing itself

LAST = "Whatever they answer, don't say a word. You can skip tape eight. Play the red tape."
LAST8 = "Whatever they answer, don't say a word. Play the red tape."
ENOUGH = "That is everything you need. Don't ask anything else. You can skip tape eight. Play the red tape."
NOTE_LAST = "Whatever they answer, don't say a word. Skip tape 8. Play the red tape."
NOTE_LAST8 = "Whatever they answer, don't say a word. Play the red tape."
NOTE_ENOUGH = "Don't ask anything else. Skip tape 8. Play the red tape."

seg("t7s", 7, {"yes": "r_star", "no": "r_heart"}, [
    "Tape seven. A, T, and R. Three letters is as far as lesson one goes, and you got there.",
    ("beat", 0.6),
    "One more. This time, ask it as a question. Say:",
    ("beat", 0.4),
    ("say", "I'm not sure about this one. Is there an S?"),
    ("beat", 0.9),
    LAST,
], note=NOTE_LAST, say="I'm not sure about this one. Is there an S?")

seg("t7r", 7, {"yes": "t8small", "no": "t8home"}, [
    "Tape seven. No R. That is your signal that the letters are finished.",
    ("beat", 0.5),
    "They always run out, and when they do, you switch to the thing itself. Lower your hand. Ask your participant to see it, right in front of them.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    "Then play tape eight.",
], note="The letters are finished. Lower your hand. Then play tape 8.", say="Is it alive?")

seg("t7hold", 7, {"yes": "t8hard", "no": "t8own"}, [
    "Tape seven. They agreed. It is not alive. You are reading the thing itself now.",
    ("beat", 0.6),
    "Hold out your hands, palms up. Then ask:",
    ("beat", 0.4),
    ("say", "Could you pick it up and hold it in your hands?"),
    ("beat", 0.9),
    "Then play tape eight.",
], note="Hold out your hands, palms up. Then play tape 8.",
   say="Could you pick it up and hold it in your hands?")

seg("t7man", 7, "r_stickman", [
    "Tape seven. They corrected you. That is what that step is for.",
    ("beat", 0.6),
    "People answer a question slowly, but they correct a mistake right away. Now they have told you it is alive.",
    ("beat", 0.8),
    ENOUGH,
], note=NOTE_ENOUGH)

seg("t7live", 7, {"yes": "r_fish", "no": "r_house"}, [
    "Tape seven. They can touch it. So it is close, and it is solid.",
    ("beat", 0.6),
    "One last question. Ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    LAST,
], note=NOTE_LAST, say="Is it alive?")

seg("t7sun", 7, "r_sun", [
    "Tape seven. They can't touch it. That is the most useful answer in lesson one.",
    ("beat", 0.8),
    ENOUGH,
], note=NOTE_ENOUGH)

seg("t7big", 7, {"yes": "r_tree", "no": "r_flower"}, [
    "Tape seven. It is alive. Ask your participant to stand right next to it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it bigger than you?"),
    ("beat", 0.9),
    LAST,
], note=NOTE_LAST, say="Is it bigger than you?")

seg("t7touch", 7, {"yes": "r_pencil", "no": "r_moon"}, [
    "Tape seven. Not alive. That's fine. Most drawings aren't.",
    ("beat", 0.6),
    "One last question. Ask your participant to reach out toward it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Can you touch it?"),
    ("beat", 0.9),
    LAST,
], note=NOTE_LAST, say="Can you touch it?")

seg("t8small", 8, {"yes": "r_cat", "no": "r_stickman"}, [
    "Tape eight. It is alive. Ask your participant to stand right next to it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it smaller than you?"),
    ("beat", 0.9),
    LAST8,
], note=NOTE_LAST8, say="Is it smaller than you?")

seg("t8home", 8, {"yes": "r_table", "no": "r_boat"}, [
    "Tape eight. Not alive. That's fine. Most drawings aren't.",
    ("beat", 0.6),
    "One last question. Ask:",
    ("beat", 0.4),
    ("say", "Is there one in your home?"),
    ("beat", 0.9),
    LAST8,
], note=NOTE_LAST8, say="Is there one in your home?")

seg("t8hard", 8, {"yes": "r_glass", "no": "r_ball"}, [
    "Tape eight. They can hold it. Ask your participant to close their hands around it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it hard?"),
    ("beat", 0.9),
    LAST8,
], note=NOTE_LAST8, say="Is it hard?")

seg("t8own", 8, {"yes": "r_car", "no": "r_plane"}, [
    "Tape eight. Too big to hold. Good. That helps.",
    ("beat", 0.6),
    "One last question. Ask:",
    ("beat", 0.4),
    ("say", "Do you own one?"),
    ("beat", 0.9),
    LAST8,
], note=NOTE_LAST8, say="Do you own one?")

# --------------------------------------------------------------------- red tape
# One recording per drawing. Two details a child's version nearly always has,
# then the name. Details are chosen to be safe, not clever.

DRAWINGS = {
    "fish":     ("You drew it from the side. One eye, and a tail like a triangle.", "You drew a fish."),
    "house":    ("A square, with a triangle sitting on top of it. There is a door.", "You drew a house."),
    "sun":      ("A circle, with lines coming away from it all the way round.", "You drew the sun."),
    "tree":     ("Two lines for the trunk, and a round top that could be a cloud.", "You drew a tree."),
    "flower":   ("A single line for the stem. A round middle, and the petals going round it.", "You drew a flower."),
    "pencil":   ("Long and thin, with a point at one end. You were holding one when you drew it.", "You drew a pencil."),
    "moon":     ("A crescent. You drew the thin one, because the full one would only have been a circle.", "You drew the moon."),
    "glass":    ("It is standing upright, open at the top. Something to drink from.", "You drew a glass."),
    "ball":     ("It is a circle. But you were told no circles, so you put lines on it.", "You drew a ball."),
    "car":      ("You drew it from the side. Two wheels showing, and a window.", "You drew a car."),
    "plane":    ("A long body, with a wing on either side of it.", "You drew an airplane."),
    "cat":      ("Two pointed ears, and whiskers.", "You drew a cat."),
    "stickman": ("A circle for the head. Single lines for the body, the arms, and the legs.", "You drew a person. A stick figure."),
    "table":    ("A flat top, with legs underneath it.", "You drew a table."),
    "boat":     ("It is on the water. A hull, with a sail above it.", "You drew a boat."),
    "heart":    ("Two curves, meeting in a point at the bottom.", "You drew a heart."),
    "star":     ("Five points. You may have drawn it in one line, without lifting the pencil.", "You drew a star."),
}

for key, (detail, name) in DRAWINGS.items():
    seg("r_" + key, 9, None, [
        "This is the red tape.",
        ("beat", 0.7),
        "You have done your part. Put your hands in your lap. I will finish this one, so you can see how it should feel.",
        ("beat", 0.9),
        "To your participant: you never said what you drew. Not to my student, and not to me.",
        ("beat", 1.0),
        detail,
        ("beat", 1.0),
        name,
        ("beat", 1.2),
        "It is on the last page of the booklet.",
        ("page",),
        ("beat", 1.8),
        "And that is how you read a mind. Congratulations on finishing lesson one.",
    ], note="Hands in your lap. Let the tape finish.", art=key)

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
            assert step == 1 or S[t]["tape"] == 9, f"{sid} -> {t} skips to a numbered tape"
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
        print(S[r[-1]]["art"].ljust(9), " ".join(r[3:]))
