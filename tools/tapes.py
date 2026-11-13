# How to Read Minds: a home course in seven cassettes.
# The full script and the graph that decides which recording plays next.
#
# What the spectator sees: six numbered tapes and a red one, played in order.
# What is true: every tape after the second exists in several recordings, and
# the way the performer picks it out of the case chooses one.
#
# Writing rules for the voice (keep to these when editing):
#   - An upbeat how-to instructor. Encouraging, brisk, never surprised, never
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
#   ("page",)        the drawing appears here (red tapes only)
#
# Segment fields:
#   tape   1..6, or RED for the red tape: the label shown while it plays
#   next   "id"                    one recording follows, however it is picked
#          {"yes": id, "no": id}   a tap picks yes, a hold picks no
#          None                    end of the lesson
#   say    the line the student speaks, shown on screen while the tape plays
#   art    red tapes: which drawing is on the last page

COURSE = "How to Read Minds"
RED = 7      # tapes 1..6 are numbered; the seventh is the red one

S = {}


def seg(sid, tape, next, parts, say=None, art=None):
    S[sid] = {"tape": tape, "next": next, "parts": parts, "say": say, "art": art}


# ------------------------------------------------------------------ setting up

seg("t1", 1, "t2", [
    "Welcome to How to Read Minds! This is tape one. By the end of the red tape, you will have read your first mind.",
    ("beat", 0.5),
    "It's easy. Each tape gives you one step. Do the step, then play the next tape. Save the red one for last.",
    ("beat", 0.6),
    "Sit your partner down in front of you. Partner, this part is for you.",
    ("beat", 0.7),
    "Think back to school. You're ten, maybe twelve, stuck in a boring class with a pencil in your hand, and you start to doodle.",
    ("beat", 0.5),
    "Something simple, that takes five or ten seconds. Like a smiley face, a mountain, or even a bicycle. Don't use those. I just said them.",
    ("beat", 0.4),
    "And no plain shapes, like circles or triangles. Just a little drawing anybody would recognize. Keep it simple.",
    ("beat", 2.6),
    "Got it? Don't say it out loud.",
    ("beat", 0.7),
    "When your partner is ready, play tape two.",
])

# ---------------------------------------------------------------------- letters

seg("t2", 2, {"yes": "t3y", "no": "t3n"}, [
    "Tape two. Nice work! Your partner has a picture in mind. Now let's make it stronger.",
    ("beat", 0.6),
    "Partner, imagine the real thing, right in front of you, life size.",
    ("beat", 1.5),
    "Now think of it as a word. The simple word, the one a kid would use. If you had drawn a smiley face, you would see a face, and think the word smiley.",
    ("beat", 0.6),
    "Spell your word in your head, one letter at a time.",
    ("beat", 3.0),
    "And once more.",
    ("beat", 3.0),
    "Great. Now, mind reader, it's your turn.",
    ("beat", 0.4),
    "Put two fingers on your temple. Look your partner in the eye. Don't ask. Tell them:",
    ("beat", 0.4),
    ("say", "There is an A in your word."),
    ("beat", 0.9),
    "Wait for the answer. Then play tape three.",
], say="There is an A in your word.")

seg("t3y", 3, {"yes": "t4yy", "no": "t4yn"}, [
    "Tape three. You got the A! Now that you have one letter, the next comes easier.",
    ("beat", 0.5),
    "Keep your fingers on your temple. Ask your partner to picture the whole word again.",
    ("beat", 1.4),
    "Say:",
    ("beat", 0.4),
    ("say", "And there is a T."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape four.",
], say="And there is a T.")

seg("t3n", 3, {"yes": "t4ny", "no": "t4nn"}, [
    "Tape three. Your partner said no to the A. Perfect. They are supposed to.",
    ("beat", 0.6),
    "The first letter in this course is always a test. It tells you they are answering honestly, and it shows you what a no looks like on this person's face.",
    ("beat", 0.7),
    "Now the real reading starts. Ask your partner to focus harder on the word. Fingers on your temple. Say:",
    ("beat", 0.4),
    ("say", "There is an S."),
    ("beat", 0.9),
    "Wait for their answer. Then play tape four.",
], say="There is an S.")

seg("t4yy", 4, {"yes": "t5s", "no": "t5r"}, [
    "Tape four. An A and a T! You have a real connection going, so don't rush it.",
    ("beat", 0.5),
    "Take a slow breath, and ask your partner to do the same.",
    ("beat", 1.6),
    "This time, be a little less certain. Say:",
    ("beat", 0.4),
    ("say", "I think there's an R."),
    ("beat", 0.9),
    "Then play tape five.",
], say="I think there's an R.")

seg("t4yn", 4, {"yes": "t5hold", "no": "t5man"}, [
    "Tape four. That one was a no. Good.",
    ("beat", 0.5),
    "After your first hit, this course always gives you a letter that isn't there. It keeps you from getting carried away, and it is your signal to move on from letters.",
    ("beat", 0.7),
    "Lower your hand. Now you are going to pick up the thing itself. Look at the space between the two of you, and tell them, firmly:",
    ("beat", 0.4),
    ("say", "What you drew is not a living thing."),
    ("beat", 0.9),
    "If they agree, fine. If they correct you, that is fine too. Then play tape five.",
], say="What you drew is not a living thing.")

seg("t4ny", 4, {"yes": "t5live", "no": "t5sun"}, [
    "Tape four. There's your S! One letter is all we need from the word.",
    ("beat", 0.6),
    "Lower your hand. Now you are going to pick up the thing itself. Ask your partner to keep seeing it, right in front of them, life size.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Can you touch it?"),
    ("beat", 0.9),
    "Then play tape five.",
], say="Can you touch it?")

seg("t4nn", 4, {"yes": "t5big", "no": "t5touch"}, [
    "Tape four. Two no's in a row. That is exactly the result we were looking for.",
    ("beat", 0.6),
    "It tells you your partner thinks in pictures, not in words. Picture thinkers are the easiest people to read.",
    ("beat", 0.7),
    "So forget the letters. Lower your hand. Ask your partner to look at the thing itself, right in front of them.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    "Then play tape five.",
], say="Is it alive?")

# --------------------------------------------------------------- the thing itself

LAST = "Whatever they answer, don't say a word. You can skip tape six. Play the red tape."
LAST8 = "Whatever they answer, don't say a word. Play the red tape."
ENOUGH = "That is everything you need. Don't ask anything else. You can skip tape six. Play the red tape."

seg("t5s", 5, {"yes": "r_star", "no": "r_heart"}, [
    "Tape five. A, T, and R. Three letters is as far as lesson one goes, and you got there.",
    ("beat", 0.6),
    "One more. This time, ask it as a question. Say:",
    ("beat", 0.4),
    ("say", "I'm not sure about this one. Is there an S?"),
    ("beat", 0.9),
    LAST,
], say="I'm not sure about this one. Is there an S?")

seg("t5r", 5, {"yes": "t6small", "no": "t6home"}, [
    "Tape five. No R. That is your signal that the letters are finished.",
    ("beat", 0.5),
    "They always run out, and when they do, you switch to the thing itself. Lower your hand. Ask your partner to see it, right in front of them.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    "Then play tape six.",
], say="Is it alive?")

seg("t5hold", 5, {"yes": "t6hard", "no": "t6own"}, [
    "Tape five. They agreed. It is not alive. You are reading the thing itself now.",
    ("beat", 0.6),
    "Hold out your hands, palms up. Then ask:",
    ("beat", 0.4),
    ("say", "Could you pick it up and hold it in your hands?"),
    ("beat", 0.9),
    "Then play tape six.",
], say="Could you pick it up and hold it in your hands?")

seg("t5man", 5, "r_stickman", [
    "Tape five. They corrected you. That is what that step is for.",
    ("beat", 0.6),
    "People answer a question slowly, but they correct a mistake right away. Now they have told you it is alive.",
    ("beat", 0.8),
    ENOUGH,
])

seg("t5live", 5, {"yes": "r_fish", "no": "r_house"}, [
    "Tape five. They can touch it. So it is close, and it is solid.",
    ("beat", 0.6),
    "One last question. Ask:",
    ("beat", 0.4),
    ("say", "Is it alive?"),
    ("beat", 0.9),
    LAST,
], say="Is it alive?")

seg("t5sun", 5, "r_sun", [
    "Tape five. They can't touch it. That is the most useful answer in lesson one.",
    ("beat", 0.8),
    ENOUGH,
])

seg("t5big", 5, {"yes": "r_tree", "no": "r_flower"}, [
    "Tape five. It is alive. Ask your partner to stand right next to it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it bigger than you?"),
    ("beat", 0.9),
    LAST,
], say="Is it bigger than you?")

seg("t5touch", 5, {"yes": "r_pencil", "no": "r_moon"}, [
    "Tape five. Not alive. That's fine. Most drawings aren't.",
    ("beat", 0.6),
    "One last question. Ask your partner to reach out toward it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Can you touch it?"),
    ("beat", 0.9),
    LAST,
], say="Can you touch it?")

seg("t6small", 6, {"yes": "r_cat", "no": "r_stickman"}, [
    "Tape six. It is alive. Ask your partner to stand right next to it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it smaller than you?"),
    ("beat", 0.9),
    LAST8,
], say="Is it smaller than you?")

seg("t6home", 6, {"yes": "r_table", "no": "r_boat"}, [
    "Tape six. Not alive. That's fine. Most drawings aren't.",
    ("beat", 0.6),
    "One last question. Ask:",
    ("beat", 0.4),
    ("say", "Is there one in your home?"),
    ("beat", 0.9),
    LAST8,
], say="Is there one in your home?")

seg("t6hard", 6, {"yes": "r_glass", "no": "r_ball"}, [
    "Tape six. They can hold it. Ask your partner to close their hands around it.",
    ("beat", 1.2),
    "Then ask:",
    ("beat", 0.4),
    ("say", "Is it hard?"),
    ("beat", 0.9),
    LAST8,
], say="Is it hard?")

seg("t6own", 6, {"yes": "r_car", "no": "r_plane"}, [
    "Tape six. Too big to hold. Good. That helps.",
    ("beat", 0.6),
    "One last question. Ask:",
    ("beat", 0.4),
    ("say", "Do you own one?"),
    ("beat", 0.9),
    LAST8,
], say="Do you own one?")

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
    seg("r_" + key, RED, None, [
        "This is the red tape.",
        ("beat", 0.7),
        "You have done your part, and you did great. Hands in your lap. I will finish this one, so you can see how it should feel.",
        ("beat", 0.9),
        "Partner: you never said what you drew. Not to my student, and not to me.",
        ("beat", 1.0),
        detail,
        ("beat", 1.0),
        name,
        ("beat", 1.2),
        "It is on the last page of the booklet.",
        ("page",),
        ("beat", 1.8),
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
        print(S[r[-1]]["art"].ljust(9), " ".join(r[1:]))
