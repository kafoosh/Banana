# The Amazing Gerald — full performance script + branch graph.
# Single source of truth: build_audio.py renders TTS from `parts` and emits
# docs/data/segments.json (captions, graph, file map, durations) for the app.
#
# Part syntax:
#   "text"            spoken by Gerald at normal pace
#   ("q", "text")     a line the magician must repeat — spoken slower, deliberate
#   ("beat", 0.8)     silence (hiss bed continues underneath)
#   ("click",)        tape transport click
#   ("flap",)         end-of-reel flap/flutter
#
# Graph semantics (the whole secret):
#   kind "wait":  segment ends -> player auto-stops, AWAITING PERFORMANCE.
#                 play -> SEGMENTS[play]  (spectator said YES / ready)
#                 rew  -> SEGMENTS[rew]   (spectator said NO) — visually just a -10s rewind
#                 rew=None -> a genuine rewind: replay the segment tail, wait again.
#   kind "auto":  chains into `play` with no stop.
#   kind "reveal": at end, the cassette art flips to `art`; then finale auto-plays.
#   kind "end":   stops. From finale, play -> extras (easter egg), then nothing.
#
# NO-arrival segments open by repeating the tail of the previous line, then a
# click — sells the illusion that the tape simply rewound and replayed.

FAKE_RUNTIME = "11:47"  # printed on the player; no path comes close to filling it
TRACK_NAME = "02_SideB_FirstPerformance.mp3"

SEGMENTS = {

    # ---------------------------------------------------------------- ACT 1+2
    "intro": {
        "kind": "wait", "play": "ind1", "rew": None,
        "parts": [
            "Side B. Your first performance.",
            ("beat", 0.9),
            "If you have not listened to Side A: pause now, go back, and do the work.",
            ("beat", 0.7),
            "You're not going to. Fine.",
            ("beat", 0.9),
            "The rules, then. Rule one. From here on, you repeat only the lines I give you, word for word. You are a beautiful, empty megaphone.",
            ("beat", 0.6),
            "Rule two. When I say pause the tape, you pause the tape.",
            ("beat", 0.6),
            "Rule three — and this is the one that matters. When something goes wrong — and apprentice, with you, something will go wrong — do not panic. Wind me back ten seconds and listen again. This course anticipates everything.",
            ("beat", 0.5),
            "Even you.",
            ("beat", 1.0),
            "Now. Seat your subject across from you. Lay the phone between you, face up, where they can watch it. It's just a tape. Let them see it's just a tape.",
            ("beat", 0.6),
            "Pause here. Press play when you're both sitting comfortably.",
        ],
        "caption": ("Side B. Your first performance. … Rule one: repeat only the lines I give you. "
                    "Rule two: when I say pause, pause. Rule three: when something goes wrong, wind me back ten seconds and listen again — "
                    "this course anticipates everything. Even you. … Seat your subject across from you, phone between you, face up. "
                    "<b>Pause here. Play when you're both ready.</b>"),
    },

    "ind1": {
        "kind": "wait", "play": "ind2", "rew": None,
        "parts": [
            "Hello, subject. I'm Gerald. You can't answer me. Don't try. Ignore my apprentice — they're new.",
            ("beat", 0.8),
            "Close your eyes.",
            ("beat", 1.2),
            "You're in school again. Ten years old. Maybe twelve. Last period. The clock has stopped moving, and the teacher's voice is very far away.",
            ("beat", 0.8),
            "There's a pencil in your hand. And without ever deciding to, you're doodling. The same small doodle you always drew. Simple. Five seconds of pencil. Ten, at most. You're a child, not an artist.",
            ("beat", 0.9),
            "Not a smiley face. Not a mountain. Not a bicycle — you were better than that. And none of those empty shapes — no circles, no triangles. A real thing. A thing anybody would recognize the instant they saw it.",
            ("beat", 1.0),
            "See it on the page. Small. In pencil. Yours.",
            ("beat", 0.9),
            "Do not say it out loud. Never say it.",
            ("beat", 0.7),
            "Apprentice: pause the tape. When your subject nods, press play.",
        ],
        "caption": ("「TO YOUR SUBJECT」 Close your eyes. You're in school again — ten, maybe twelve. Last period. A pencil in your hand, "
                    "and without deciding to, you're doodling the same small doodle you always drew. Five, ten seconds of pencil. "
                    "Not a smiley face. Not a mountain. Not a bicycle. No circles or triangles. A real thing anybody would recognize. "
                    "See it on the page. Don't say it. <b>Pause — play when they nod.</b>"),
    },

    "ind2": {
        "kind": "wait", "play": "preflight", "rew": None,
        "parts": [
            "Eyes open.",
            ("beat", 0.6),
            "Subject: take that little drawing, and put the real thing here in the room. Real size. Sitting right there between you and my apprentice.",
            ("beat", 1.0),
            "Now think of it as a word. If you had drawn a smiley face — which you did not, because I told you not to — you would see a face, and the word would be SMILEY.",
            ("beat", 0.7),
            "See your word. Walk along its letters, one at a time. Slowly.",
            ("beat", 1.4),
            "And once more. Slower.",
            ("beat", 1.4),
            "Good.",
            ("beat", 0.6),
            "Apprentice, ask them: do you have it? A nod is enough. If they take longer than a minute, remind them gently: it's a doodle, not a mortgage.",
            ("beat", 0.5),
            "Pause. Play when they nod.",
        ],
        "caption": ("「TO YOUR SUBJECT」 Put the real thing in the room — real size, right there between you. Now think of it as a WORD "
                    "(a smiley face would be the word SMILEY). Walk its letters one at a time… again, slower… good. "
                    "「TO YOU」 Ask: <b>“Do you have it?”</b> A nod is enough. <b>Pause — play when they nod.</b>"),
    },

    "preflight": {
        "kind": "auto", "play": "20",
        "parts": [
            "From here, you say only my words.",
            ("beat", 0.6),
            "Deep breath, apprentice. Straight back. Dead eyes.",
            ("beat", 0.7),
            "Here we go.",
        ],
        "caption": "From here, you say only Gerald's words. Deep breath. Straight back. Dead eyes. Here we go.",
    },

    # ---------------------------------------------------------------- LETTERS
    "20": {
        "kind": "wait", "play": "21", "rew": "24",
        "parts": [
            "First impression coming. It's a letter.",
            ("beat", 0.5),
            "Say this, exactly, with the calm of a man reading a menu:",
            ("beat", 0.4),
            ("q", "I can feel a letter in your word. An A. There's an A — correct?"),
            ("beat", 0.6),
            "Say it now. Then pause the tape.",
        ],
        "caption": "First impression. Say it calm, like you're reading a menu: <b>“I can feel a letter in your word. An A. There's an A… correct?”</b> Then pause.",
    },

    "21": {
        "kind": "wait", "play": "22", "rew": "25m",
        "parts": [
            "Of course there's an A. There is always an A when I'm involved.",
            ("beat", 0.5),
            "Next. Say:",
            ("beat", 0.4),
            ("q", "I see a T as well. Yes?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Of course there's an A. There always is, with Gerald. Now say: <b>“I see a T as well… yes?”</b> Pause.",
    },

    "22": {
        "kind": "wait", "play": "23", "rew": "26",
        "parts": [
            "Two for two. Careful, apprentice — confidence is for closers, and you are not one yet.",
            ("beat", 0.5),
            "Say it a little softer:",
            ("beat", 0.4),
            ("q", "Is that… an R?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Two for two. Don't get cocky. Softer this time: <b>“Is that… an R?”</b> Pause.",
    },

    "23": {
        "kind": "wait", "play": "52", "rew": "51",
        "parts": [
            "Look at you. Almost dangerous.",
            ("beat", 0.5),
            "Last letter. Say it like you barely believe it yourself:",
            ("beat", 0.4),
            ("q", "Now I'm not sure about this one. An S?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Look at you. Almost dangerous. Last letter — barely believe it: <b>“Now I'm not sure about this one… an S?”</b> Pause.",
    },

    "24": {  # A missed -> claim S
        "kind": "wait", "play": "27", "rew": "28",
        "parts": [
            ("q", "There's an A — correct?"),
            ("click",),
            ("beat", 0.6),
            "You rewound me. Which means they said no.",
            ("beat", 0.8),
            "Fine. FINE. First misses happen — to students. Shoulders down; doubt has a smell, and subjects can smell it.",
            ("beat", 0.6),
            "Try this instead. Say:",
            ("beat", 0.4),
            ("q", "No… no, it's leaning. It's an S. There IS an S."),
            ("beat", 0.5),
            "I have never been more sure of a letter. Go.",
        ],
        "caption": ("[click] You rewound me — so they said no. Fine. FINE. Shoulders down; doubt has a smell. "
                    "Say: <b>“No… no, it's leaning — it's an S. There IS an S.”</b> Pause."),
    },

    # ---------------------------------------------------------------- MAN CHECK
    "25m": {  # T missed -> assert not-alive (Stickman safety valve)
        "kind": "wait", "play": "25", "rew": "rman",
        "parts": [
            ("q", "I see a T as well. Yes?"),
            ("click",),
            ("beat", 0.6),
            "Hm. No T.",
            ("beat", 0.6),
            "Interesting, actually. That narrows things beautifully — not that you'd know.",
            ("beat", 0.6),
            "Steady. Say this next one as a fact. Not a question. A fact:",
            ("beat", 0.4),
            ("q", "This thing you drew — it is NOT a living thing."),
            ("beat", 0.7),
            "If they agree — even a small nod — press play.",
            ("beat", 0.4),
            "If they argue with you… well. You know the rule. Ten seconds back.",
        ],
        "caption": ("[click] No T. Interesting — steady. Say it as a FACT, not a question: <b>“This thing you drew — it is NOT a living thing.”</b> "
                    "If they agree: play. If they argue: you know the rule."),
    },

    # ---------------------------------------------------------------- PROBES
    "25": {
        "kind": "wait", "play": "29", "rew": "30",
        "parts": [
            "Agreed. Not alive. See how easy this is when you listen?",
            ("beat", 0.5),
            "Now say:",
            ("beat", 0.4),
            ("q", "Hold out your hand. Imagine it there. Could you HOLD it in one hand?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Agreed — not alive. See how easy? Say: <b>“Hold out your hand. Imagine it there. Could you HOLD it in one hand?”</b> Pause.",
    },

    "26": {
        "kind": "wait", "play": "31", "rew": "32",
        "parts": [
            ("q", "Is that… an R?"),
            ("click",),
            ("beat", 0.6),
            "No R. Don't look at the subject like that — they're doing fine. You are doing… adequately.",
            ("beat", 0.6),
            "New angle. Say:",
            ("beat", 0.4),
            ("q", "Leave the letters. Let me touch the thing itself. Is it ALIVE?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "[click] No R. They're fine — YOU are 'adequate'. New angle: <b>“Leave the letters. Let me touch the thing itself. Is it ALIVE?”</b> Pause.",
    },

    "27": {
        "kind": "wait", "play": "33", "rew": "38",
        "parts": [
            "There it is. We're back, and it never even looked like we left.",
            ("beat", 0.5),
            "The letters have done their work. Now we use the body. Say:",
            ("beat", 0.4),
            ("q", "Reach out in your mind. Can you TOUCH it?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "There it is — we're back. Now the body does the work. Say: <b>“Reach out in your mind. Can you TOUCH it?”</b> Pause.",
    },

    "28": {
        "kind": "wait", "play": "34", "rew": "35",
        "parts": [
            ("q", "There IS an S."),
            ("click",),
            ("beat", 0.8),
            "No A. No S.",
            ("beat", 1.0),
            "Apprentice. Whatever you are doing with your face: stop doing it.",
            ("beat", 0.6),
            "We are done with letters. Letters are clearly not your instrument. We go to raw impressions — my specialty and, as of this moment, yours.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": ("[click] No A. No S. Whatever you're doing with your face — stop. Letters are not your instrument; we go to RAW IMPRESSIONS. "
                    "Say: <b>“Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?”</b> Pause."),
    },

    "29": {
        "kind": "wait", "play": "43", "rew": "44",
        "parts": [
            "I thought so. I felt it in the palm too.",
            ("beat", 0.5),
            "Now the surface. Say:",
            ("beat", 0.4),
            ("q", "Squeeze it. Is it HARD?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "I thought so — I felt it in the palm too. Say: <b>“Squeeze it. Is it HARD?”</b> Pause.",
    },

    "30": {
        "kind": "wait", "play": "45", "rew": "46",
        "parts": [
            ("q", "Could you HOLD it in one hand?"),
            ("click",),
            ("beat", 0.6),
            "Too big for a hand. Believe it or not, apprentice, we are exactly where I want us.",
            ("beat", 0.5),
            "Say:",
            ("beat", 0.4),
            ("q", "It's bigger than both of us. Tell me — do you OWN one?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "[click] Too big for a hand — exactly where Gerald wants us. Say: <b>“It's bigger than both of us. Tell me — do you OWN one?”</b> Pause.",
    },

    "31": {
        "kind": "wait", "play": "47", "rew": "48",
        "parts": [
            "Alive. I can hear it moving from here.",
            ("beat", 0.5),
            "Say:",
            ("beat", 0.4),
            ("q", "Stand next to it in your mind. Is it SMALLER than you?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Alive — Gerald can hear it moving. Say: <b>“Stand next to it in your mind. Is it SMALLER than you?”</b> Pause.",
    },

    "32": {
        "kind": "wait", "play": "49", "rew": "50",
        "parts": [
            ("q", "Is it ALIVE?"),
            ("click",),
            ("beat", 0.6),
            "Not alive. But it relates to life — tell them that. Say:",
            ("beat", 0.4),
            ("q", "It relates to life… it's part of a day."),
            ("beat", 0.6),
            "Now say:",
            ("beat", 0.4),
            ("q", "Do you have one at HOME?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "[click] Not alive — but it relates to life, tell them: <b>“It relates to life… it's part of a day.”</b> Then: <b>“Do you have one at HOME?”</b> Pause.",
    },

    "33": {
        "kind": "wait", "play": "36", "rew": "37",
        "parts": [
            "Touchable. Good. Reach further. Say:",
            ("beat", 0.4),
            ("q", "I'm touching it with you… wait. I sense… LIFE. Is it alive?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Touchable — reach further. Say: <b>“I'm touching it with you… wait. I sense… LIFE. Is it alive?”</b> Pause.",
    },

    "34": {
        "kind": "wait", "play": "39", "rew": "40",
        "parts": [
            "Alive! See? The impressions like you better than the letters did.",
            ("beat", 0.5),
            "Say:",
            ("beat", 0.4),
            ("q", "Stand next to it. Is it BIGGER than you?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Alive! The impressions like you better than the letters did. Say: <b>“Stand next to it. Is it BIGGER than you?”</b> Pause.",
    },

    "35": {
        "kind": "wait", "play": "41", "rew": "42",
        "parts": [
            ("q", "Is it ALIVE?"),
            ("click",),
            ("beat", 0.6),
            "Not alive. We're close now — I can feel edges. Say:",
            ("beat", 0.4),
            ("q", "Reach for it. Can you TOUCH it?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "[click] Not alive. Close now — Gerald can feel edges. Say: <b>“Reach for it. Can you TOUCH it?”</b> Pause.",
    },

    # ---------------------------------------------------------------- REVEALS
    # Reveal choreography: Gerald feeds the description, the magician announces
    # the drawing, THEN "turn the screen around" -> art flips at segment end.

    "36": {
        "kind": "reveal", "art": "fish",
        "parts": [
            "Alive, and — hold on.",
            ("beat", 0.5),
            "Wet? WET. Apprentice, this is a good one.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Scales. A little bubble over its head."),
            ("beat", 0.8),
            "Now tell them. Say:",
            ("beat", 0.4),
            ("q", "You drew a FISH."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Wet? WET. Say: <b>“Scales. A little bubble over its head.”</b> … <b>“You drew a FISH.”</b> Now turn the screen around.",
    },

    "37": {
        "kind": "reveal", "art": "house",
        "parts": [
            ("q", "Is it alive?"),
            ("click",),
            ("beat", 0.6),
            "Not alive itself. But say this, exactly:",
            ("beat", 0.4),
            ("q", "It's not alive — but it is FULL of life. It's where the life lives."),
            ("beat", 0.7),
            "Watch their face change.",
            ("beat", 0.7),
            "Now. Say:",
            ("beat", 0.4),
            ("q", "Square walls. A triangle roof. Smoke from the chimney."),
            ("beat", 0.7),
            ("q", "You drew a HOUSE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": ("[click] Say exactly: <b>“It's not alive — but it is FULL of life. It's where the life lives.”</b> Watch their face. "
                    "Then: <b>“Square walls. Triangle roof. Smoke from the chimney. You drew a HOUSE.”</b> Turn the screen around."),
    },

    "38": {
        "kind": "reveal", "art": "sun",
        "parts": [
            ("q", "Can you TOUCH it?"),
            ("click",),
            ("beat", 0.6),
            "It can't be touched. Careful, apprentice — very few things can't be touched, and every one of them is magnificent.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Of course you can't touch it. It's ninety-three million miles away — and you drew it in the corner of the page, with little lines coming off it."),
            ("beat", 0.7),
            ("q", "You drew the SUN."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": ("[click] Untouchable — and everything untouchable is magnificent. Say: <b>“Of course you can't touch it. It's ninety-three million miles away — "
                    "you drew it in the corner of the page with little lines coming off it. You drew the SUN.”</b> Turn the screen around."),
    },

    "39": {
        "kind": "reveal", "art": "tree",
        "parts": [
            "Bigger. Alive. And older than everyone in the room.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Roots down. Branches up. You drew the leaves as one big cloud, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a TREE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Bigger, alive, older than everyone here. Say: <b>“Roots down. Branches up. The leaves were one big cloud, weren't they. You drew a TREE.”</b> Turn the screen around.",
    },

    "40": {
        "kind": "reveal", "art": "flower",
        "parts": [
            ("q", "Is it BIGGER than you?"),
            ("click",),
            ("beat", 0.6),
            "Smaller. Delicate, even. This is my favorite kind of thought.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A stem. Petals in a ring. You pressed harder on the middle."),
            ("beat", 0.7),
            ("q", "You drew a FLOWER."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] Smaller. Delicate. Say: <b>“A stem. Petals in a ring. You pressed harder on the middle. You drew a FLOWER.”</b> Turn the screen around.",
    },

    "41": {
        "kind": "reveal", "art": "pencil",
        "parts": [
            "You can touch it. Apprentice — in this very story, someone is already holding one of its cousins.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Long. Thin. A point at one end. You drew the thing you were drawing WITH."),
            ("beat", 0.7),
            ("q", "You drew a PENCIL."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Touchable — and someone in this story is holding its cousin. Say: <b>“Long. Thin. A point at one end. You drew the thing you were drawing WITH. You drew a PENCIL.”</b> Turn the screen around.",
    },

    "42": {
        "kind": "reveal", "art": "moon",
        "parts": [
            ("q", "Can you TOUCH it?"),
            ("click",),
            ("beat", 0.6),
            "Untouchable. Far away. Cold silver.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew it as a crescent — a little banana in the sky — with stars around it."),
            ("beat", 0.7),
            ("q", "You drew the MOON."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] Untouchable, far away, cold silver. Say: <b>“You drew it as a crescent — a little banana in the sky — with stars around it. You drew the MOON.”</b> Turn the screen around.",
    },

    "43": {
        "kind": "reveal", "art": "glass",
        "parts": [
            "Hard. And cold — they didn't say cold, but I felt it, and between us, that was the giveaway.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A stem. A bowl. A toast at the end of a long week."),
            ("beat", 0.7),
            ("q", "You drew a GLASS."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Hard — and cold, which is the giveaway. Say: <b>“A stem. A bowl. A toast at the end of a long week. You drew a GLASS.”</b> Turn the screen around.",
    },

    "44": {
        "kind": "reveal", "art": "ball",
        "parts": [
            ("q", "Is it HARD?"),
            ("click",),
            ("beat", 0.6),
            "Soft skin. Full of air. I had it the moment they squeezed.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It wants to be thrown. It spends its whole life leaving."),
            ("beat", 0.7),
            ("q", "You drew a BALL."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] Soft skin, full of air. Say: <b>“It wants to be thrown. It spends its whole life leaving. You drew a BALL.”</b> Turn the screen around.",
    },

    "45": {
        "kind": "reveal", "art": "car",
        "parts": [
            "They own one. Then, in a manner of speaking, I have sat in it.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Four wheels. Windows. Parked outside a childhood house."),
            ("beat", 0.7),
            ("q", "You drew a CAR."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "They own one — Gerald has, in a manner of speaking, sat in it. Say: <b>“Four wheels. Windows. Parked outside a childhood house. You drew a CAR.”</b> Turn the screen around.",
    },

    "46": {
        "kind": "reveal", "art": "plane",
        "parts": [
            ("q", "Do you OWN one?"),
            ("click",),
            ("beat", 0.6),
            "They don't own one. Nobody owns one. It belongs to the sky.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew it with little windows down the side, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a PLANE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] Nobody owns one — it belongs to the sky. Say: <b>“You drew it with little windows down the side, didn't you. You drew a PLANE.”</b> Turn the screen around.",
    },

    "47": {
        "kind": "reveal", "art": "cat",
        "parts": [
            "Small. Warm. And — there it is — completely indifferent to both of us.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Whiskers. Pointed ears. It is ignoring you right now."),
            ("beat", 0.7),
            ("q", "You drew a CAT."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Small, warm, and completely indifferent to us both. Say: <b>“Whiskers. Pointed ears. It's ignoring you right now. You drew a CAT.”</b> Turn the screen around.",
    },

    "48": {
        "kind": "reveal", "art": "stickman",
        "parts": [
            ("q", "Is it SMALLER than you?"),
            ("click",),
            ("beat", 0.6),
            "Not smaller. Of course not. Because it is exactly your size. It always was.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A round head. Stick arms, straight out. A self-portrait, age ten."),
            ("beat", 0.7),
            ("q", "You drew a little STICKMAN. You drew YOU."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] Not smaller — exactly your size. It always was. Say: <b>“A round head. Stick arms straight out. A self-portrait, age ten. You drew a STICKMAN — you drew YOU.”</b> Turn the screen around.",
    },

    "rman": {  # Stickman via the man-check objection
        "kind": "reveal", "art": "stickman",
        "parts": [
            ("q", "It is NOT a living thing."),
            ("click",),
            ("beat", 0.6),
            "They argued?",
            ("beat", 0.8),
            "Good. Arguing means we found something with a pulse.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew a person. A round head. Stick arms, straight out."),
            ("beat", 0.7),
            ("q", "That's YOU, isn't it. You drew yourself."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] They ARGUED? Good — arguing means a pulse. Say: <b>“You drew a person. Round head, stick arms straight out. That's YOU, isn't it.”</b> Turn the screen around.",
    },

    "49": {
        "kind": "reveal", "art": "table",
        "parts": [
            "At home. Naturally. You've eaten off yours tonight, I'd wager.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Four legs. A flat top. The whole family around it."),
            ("beat", 0.7),
            ("q", "You drew a TABLE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "At home — you've eaten off yours tonight. Say: <b>“Four legs. A flat top. The whole family around it. You drew a TABLE.”</b> Turn the screen around.",
    },

    "50": {
        "kind": "reveal", "art": "boat",
        "parts": [
            ("q", "Do you have one at HOME?"),
            ("click",),
            ("beat", 0.6),
            "Not at home. Because it lives on the water.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A little hull. A sail. And you always drew the waves as tiny letter W's, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a BOAT."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] Not at home — it lives on the water. Say: <b>“A little hull. A sail. You always drew the waves as tiny W's, didn't you. You drew a BOAT.”</b> Turn the screen around.",
    },

    "51": {
        "kind": "reveal", "art": "heart",
        "parts": [
            ("q", "An S?"),
            ("click",),
            ("beat", 0.7),
            "No S.",
            ("beat", 0.7),
            "No S… after A… T… R…",
            ("beat", 0.6),
            "Oh. OH. Apprentice, stand up straighter, because I know exactly what this is.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It's not letters anymore. I can FEEL this one. It's beating."),
            ("beat", 0.7),
            ("q", "You drew a HEART."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "[click] No S… after A, T, R… oh. OH. Stand up straighter. Say: <b>“It's not letters anymore — I can FEEL this one. It's beating. You drew a HEART.”</b> Turn the screen around.",
    },

    "52": {
        "kind": "reveal", "art": "star",
        "parts": [
            "And there it is. Four letters, four hits. This is what Side A was FOR, apprentice.",
            ("beat", 0.6),
            "Now finish it. Slowly. Say:",
            ("beat", 0.4),
            ("q", "You were ten years old, bored out of your mind… and you reached for the sky."),
            ("beat", 0.7),
            ("q", "You drew a STAR."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Four letters, four hits — this is what Side A was FOR. Slowly: <b>“You were ten years old, bored out of your mind… and you reached for the sky. You drew a STAR.”</b> Turn the screen around.",
    },

    # ---------------------------------------------------------------- OUTRO
    "finale": {
        "kind": "end", "play": "extras",
        "parts": [
            ("flap",),
            ("beat", 0.8),
            "Let them have their moment. Don't explain anything.",
            ("beat", 0.5),
            "Not that you could.",
            ("beat", 0.9),
            "Apprentice: you were adequate. That is Gerald's highest grade.",
            ("beat", 0.7),
            "Side B ends here — the rest of this side is licensing information. Stop the tape, and rewind the whole thing for your next subject.",
            ("beat", 0.8),
            "You're welcome.",
            ("beat", 0.6),
            "Gerald out.",
        ],
        "caption": ("Let them have their moment. Don't explain anything — not that you could. You were adequate: Gerald's highest grade. "
                    "The rest of this side is licensing information. <b>Press ■ to rewind for your next subject.</b>"),
    },

    "extras": {  # easter egg: they kept playing into the "licensing information"
        "kind": "end", "play": None,
        "parts": [
            "This recording is the property of Gerald Enterprises, Reseda, California.",
            ("beat", 0.5),
            "Unauthorized duplication is flattering, but forbidden.",
            ("beat", 0.6),
            "AudioMaster 98 is shareware. Gerald has not registered it either.",
            ("beat", 0.6),
            "No refunds. Side A is sold separately. It has always been sold separately.",
            ("beat", 1.2),
            ("flap",),
        ],
        "caption": "This recording is the property of Gerald Enterprises, Reseda, CA. Unauthorized duplication is flattering, but forbidden. No refunds. Side A is sold separately. It has always been sold separately.",
    },
}

# Display order also fixes the neutral on-disk file names (t01, t02, ...) so
# nothing in the audio folder hints at branches or outcomes.
ORDER = [
    "intro", "ind1", "ind2", "preflight",
    "20", "21", "22", "23", "24", "25m", "25", "26", "27", "28",
    "29", "30", "31", "32", "33", "34", "35",
    "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
    "46", "47", "48", "rman", "49", "50", "51", "52",
    "finale", "extras",
]

assert set(ORDER) == set(SEGMENTS), "ORDER and SEGMENTS out of sync"
