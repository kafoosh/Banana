# MIND-AEROBICS™ with Gerald — full performance script + branch graph.
# Register: an 80s/90s home-workout cassette, delivered bone-dry. Gerald has
# recorded thousands of these, believes in none of the branding, and is
# quietly certain of everything. No exclamation points. No pep. The performer
# is addressed plainly — never "apprentice", never nicknames.
#
# Single source of truth: build_audio.py renders TTS from `parts` and emits
# docs/data/segments.json (captions, graph, file map, durations) for the app.
#
# Part syntax:
#   "text"            spoken by Gerald — flat, measured
#   ("q", "text")     a line the magician must repeat — slower, dictation-like
#   ("beat", 0.8)     silence (hiss bed continues underneath)
#   ("click",)        tape transport click
#   ("flap",)         end-of-reel flap/flutter
#
# Graph semantics (the whole secret):
#   kind "wait":  segment ends -> player auto-stops, AWAITING PERFORMANCE.
#                 The play button is secretly split: a press on its RIGHT half
#                 continues to `yes`, a press on its LEFT half to `no`.
#                 no=None -> any press continues to `yes` (linear checkpoint).
#   kind "auto":  chains into `yes` with no stop.
#   kind "reveal": at end, the cassette art flips to `art`; then finale auto-plays.
#   kind "end":   stops. From finale, play -> extras (easter egg), then nothing.
#
# Because the input is invisible, Gerald reacts to answers he was "never told."
# On a NO, he knew — the way one knows weather. Stated flatly, never explained.

FAKE_RUNTIME = "11:47"  # printed on the player; no path comes close to filling it
TRACK_NAME = "MindAerobics_Tape2_SideB.mp3"

SEGMENTS = {

    # ---------------------------------------------------------------- ACT 1+2
    "intro": {
        "kind": "wait", "yes": "ind1", "no": None,
        "parts": [
            "Side B. Your first performance, with a live subject.",
            ("beat", 0.7),
            "I'm Gerald. The box calls this Mind-Aerobics. We're both going to live with that.",
            ("beat", 0.9),
            "You'll need one subject, seated. A quiet room. And a working relationship with instructions.",
            ("beat", 0.8),
            "Rules. One: you say only the lines I give you, word for word. You are, for our purposes, a speaker with legs.",
            ("beat", 0.6),
            "Two: when the tape stops, that's you. Say the line. Get their answer.",
            ("beat", 0.6),
            "Three. Don't tell me the answer. Don't say it, don't mouth it, don't tap it out in code. Press play.",
            ("beat", 0.6),
            "I'll know.",
            ("beat", 0.8),
            "I always know. Try not to think about it.",
            ("beat", 0.9),
            "Seat your subject across from you. Phone flat on the table, face up, where they can watch it. It's a tape. Let them watch the tape.",
            ("beat", 0.6),
            "Press play when you're both sitting comfortably. I'll be here.",
        ],
        "caption": ("Side B. Rule 1: say only Gerald's lines, word for word. Rule 2: when the tape stops, say the line and get their answer. "
                    "Rule 3: <b>don't tell Gerald the answer — press play. He'll know.</b> "
                    "Seat your subject, phone flat between you, face up. <b>Play when you're both ready.</b>"),
    },

    "ind1": {
        "kind": "wait", "yes": "ind2", "no": None,
        "parts": [
            "Warm-up. Subject — hello. I'm Gerald. Don't answer; it never helps.",
            ("beat", 0.7),
            "Close your eyes.",
            ("beat", 1.2),
            "You're in school. Ten years old. Maybe twelve. Last period. The clock isn't moving, and the teacher's voice is coming from somewhere else entirely.",
            ("beat", 0.8),
            "There's a pencil in your hand. And without deciding anything, you're doodling. The same small doodle you always drew. Five seconds of pencil. Ten, if you were feeling ambitious.",
            ("beat", 0.9),
            "Not a smiley face — we've all moved past it. Not a mountain. Not a bicycle; nobody's impressed. And no empty geometry — no circles, no triangles. A real thing. Something anyone would recognize on sight.",
            ("beat", 1.0),
            "Look at it. Small. In pencil. Unmistakably yours.",
            ("beat", 0.9),
            "Don't say what it is. Not now. Not later. This is the only rule you have, so make it count.",
            ("beat", 0.7),
            "The tape stops here. When your subject nods, press play. That was the warm-up. You're supposedly warmer now.",
        ],
        "caption": ("「TO YOUR SUBJECT」 Close your eyes. You're in school — ten, maybe twelve, last period, pencil in hand — "
                    "doodling the same small doodle you always drew. Five, ten seconds of pencil. "
                    "Not a smiley face. Not a mountain. Not a bicycle. No circles or triangles. A real thing anyone would recognize on sight. "
                    "Look at it. Never say it. <b>Play when they nod.</b>"),
    },

    "ind2": {
        "kind": "wait", "yes": "preflight", "no": None,
        "parts": [
            "Eyes open.",
            ("beat", 0.6),
            "Subject: take the doodle, and set the real thing here in the room. Actual size. Between the two of you.",
            ("beat", 1.0),
            "Now think of it as a word. If you'd drawn a smiley face — which you didn't; we discussed it — you'd see a face, and think the word smiley.",
            ("beat", 0.7),
            "Find your word. Walk its letters, one at a time. First letter.",
            ("beat", 1.2),
            "Next. Keep going, to the end.",
            ("beat", 1.3),
            "Again. Slower. The letters aren't going anywhere.",
            ("beat", 1.4),
            "Good.",
            ("beat", 0.6),
            "Ask them if they have it. A nod is enough. If it's taking a while, remind them, gently: it's a doodle, not a mortgage.",
            ("beat", 0.5),
            "Play when they nod.",
        ],
        "caption": ("「TO YOUR SUBJECT」 Set the real thing in the room — actual size, between you. Now think of it as a WORD "
                    "(a smiley face would be the word SMILEY). Walk its letters one at a time… and again, slower. "
                    "「TO YOU」 Ask: <b>“Do you have it?”</b> A nod is enough. <b>Play when they nod.</b>"),
    },

    "preflight": {
        "kind": "auto", "yes": "20",
        "parts": [
            "From here, only my words.",
            ("beat", 0.6),
            "Straighten up. Try to look like someone things happen to on purpose.",
            ("beat", 0.6),
            "Here we go.",
        ],
        "caption": "From here, only Gerald's words. Straighten up. Look like someone things happen to on purpose. Here we go.",
    },

    # ---------------------------------------------------------------- LETTERS
    "20": {
        "kind": "wait", "yes": "21", "no": "24",
        "parts": [
            "First one. It's a letter. Say it the way you'd read a menu:",
            ("beat", 0.4),
            ("q", "I can feel a letter in your word. An A. There's an A — correct?"),
            ("beat", 0.6),
            "Get their answer. You know the procedure.",
        ],
        "caption": "First one — say it like you're reading a menu: <b>“I can feel a letter in your word. An A. There's an A… correct?”</b> Get their answer, then play.",
    },

    "21": {
        "kind": "wait", "yes": "22", "no": "25m",
        "parts": [
            "There's the A. There's always an A. I'd act surprised, but we agreed to be honest with each other.",
            ("beat", 0.6),
            "Next:",
            ("beat", 0.4),
            ("q", "I see a T as well. Yes?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "There's the A — there's always an A. Next: <b>“I see a T as well… yes?”</b> Go.",
    },

    "22": {
        "kind": "wait", "yes": "23", "no": "26",
        "parts": [
            "Two for two. Don't let it change you.",
            ("beat", 0.5),
            "Softer now:",
            ("beat", 0.4),
            ("q", "Is that… an R?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Two for two — don't let it change you. Softer: <b>“Is that… an R?”</b> Go.",
    },

    "23": {
        "kind": "wait", "yes": "52", "no": "51",
        "parts": [
            "Three in a row. Statistically, you're due.",
            ("beat", 0.5),
            "Last letter. Say it like you barely trust it:",
            ("beat", 0.4),
            ("q", "Now I'm not sure about this one. An S?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Three in a row — statistically, you're due. Last letter, barely trust it: <b>“Now I'm not sure about this one… an S?”</b> Go.",
    },

    "24": {  # A missed -> claim S
        "kind": "wait", "yes": "27", "no": "28",
        "parts": [
            "That was a no.",
            ("beat", 0.7),
            "Don't ask how I know. I recorded this in 1987. The no arrived before you did.",
            ("beat", 0.7),
            "It's not the tape. It's not the subject. I'll leave the remaining option with you.",
            ("beat", 0.8),
            "It's fine. A miss is information. Write that down somewhere you'll never look.",
            ("beat", 0.6),
            "Say this:",
            ("beat", 0.4),
            ("q", "No… no, it's leaning. It's an S. There is an S."),
            ("beat", 0.5),
            "Deliver it like a man who has never been wrong. You've seen one.",
        ],
        "caption": ("That was a no — the no arrived before you did. Not the tape's fault; not the subject's. "
                    "Say: <b>“No… no, it's leaning. It's an S. There IS an S.”</b> Like a man who has never been wrong. You've seen one."),
    },

    # ---------------------------------------------------------------- MAN CHECK
    "25m": {  # T missed -> assert not-alive (Stickman safety valve)
        "kind": "wait", "yes": "25", "no": "rman",
        "parts": [
            "A no. I felt it coming, the way one feels weather.",
            ("beat", 0.7),
            "It's useful, actually. I understand if it doesn't feel that way from where you're sitting.",
            ("beat", 0.7),
            "The next one is said as a fact. Not a question. A fact:",
            ("beat", 0.4),
            ("q", "This thing you drew — it is NOT a living thing."),
            ("beat", 0.7),
            "If they nod, that's a yes. If they argue with you, that's a no.",
            ("beat", 0.5),
            "Either way, press play. I'll take it from there.",
        ],
        "caption": ("A no — Gerald felt it coming, the way one feels weather. Say this as a FACT, not a question: "
                    "<b>“This thing you drew — it is NOT a living thing.”</b> Nod = yes. Argument = no. Either way, press play."),
    },

    # ---------------------------------------------------------------- PROBES
    "25": {
        "kind": "wait", "yes": "29", "no": "30",
        "parts": [
            "Agreed. Not alive. Progress — the small kind, but I've learned not to be picky.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Hold out your hand. Imagine it there. Could you HOLD it in one hand?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Agreed — not alive. Progress, the small kind. Say: <b>“Hold out your hand. Imagine it there. Could you HOLD it in one hand?”</b> Go.",
    },

    "26": {
        "kind": "wait", "yes": "31", "no": "32",
        "parts": [
            "No R. I know. I felt it through the magnetic particles. They don't lie. It's most of what I like about them.",
            ("beat", 0.7),
            "New approach. Say:",
            ("beat", 0.4),
            ("q", "Leave the letters. Let me touch the thing itself. Is it ALIVE?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": ("No R — felt through the magnetic particles, which don't lie. New approach: "
                    "<b>“Leave the letters. Let me touch the thing itself. Is it ALIVE?”</b> Go."),
    },

    "27": {
        "kind": "wait", "yes": "33", "no": "38",
        "parts": [
            "The S. There it is. We're back, and we will never speak of the A again.",
            ("beat", 0.6),
            "Letters are done. Now the senses. Say:",
            ("beat", 0.4),
            ("q", "Reach out in your mind. Can you TOUCH it?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "The S — we're back, and we will never speak of the A again. Now the senses: <b>“Reach out in your mind. Can you TOUCH it?”</b> Go.",
    },

    "28": {
        "kind": "wait", "yes": "34", "no": "35",
        "parts": [
            "Also a no.",
            ("beat", 0.7),
            "I knew yesterday. I knew in 1987. At some point we should discuss what you knew, and when.",
            ("beat", 0.8),
            "Letters are not your event. That's allowed. Some athletes are sprinters. Some are distance runners.",
            ("beat", 0.7),
            "Moving on.",
            ("beat", 0.6),
            "We'll use raw impressions now. My field. And, as of today, yours. Say:",
            ("beat", 0.4),
            ("q", "Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": ("Also a no — Gerald knew in 1987. Letters are not your event; that's allowed. Raw impressions now: "
                    "<b>“Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?”</b> Go."),
    },

    "29": {
        "kind": "wait", "yes": "43", "no": "44",
        "parts": [
            "Held it. I felt the grip from in here. It's a strange life, being a tape.",
            ("beat", 0.6),
            "The surface. Say:",
            ("beat", 0.4),
            ("q", "Squeeze it. Is it HARD?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Held it — Gerald felt the grip from in there. It's a strange life, being a tape. Say: <b>“Squeeze it. Is it HARD?”</b> Go.",
    },

    "30": {
        "kind": "wait", "yes": "45", "no": "46",
        "parts": [
            "No. Too big for a hand. I knew — and so did you, if we're generous with the word.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It's bigger than both of us. Tell me — do you OWN one?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "A no — too big for a hand. Say: <b>“It's bigger than both of us. Tell me — do you OWN one?”</b> Go.",
    },

    "31": {
        "kind": "wait", "yes": "47", "no": "48",
        "parts": [
            "Alive. I can hear it moving from here.",
            ("beat", 0.5),
            "Say:",
            ("beat", 0.4),
            ("q", "Stand next to it in your mind. Is it SMALLER than you?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Alive — Gerald can hear it moving from here. Say: <b>“Stand next to it in your mind. Is it SMALLER than you?”</b> Go.",
    },

    "32": {
        "kind": "wait", "yes": "49", "no": "50",
        "parts": [
            "A no. You're surprised. One of us is surprised.",
            ("beat", 0.6),
            "Not alive. But say this part gently:",
            ("beat", 0.4),
            ("q", "It relates to life… it's part of a day."),
            ("beat", 0.6),
            "Let it land. Then:",
            ("beat", 0.4),
            ("q", "Do you have one at HOME?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "A no — one of us is surprised. Gently: <b>“It relates to life… it's part of a day.”</b> Let it land. Then: <b>“Do you have one at HOME?”</b> Go.",
    },

    "33": {
        "kind": "wait", "yes": "36", "no": "37",
        "parts": [
            "Touchable. Reach further. Say:",
            ("beat", 0.4),
            ("q", "I'm touching it with you… wait. I sense… LIFE. Is it alive?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Touchable — reach further. Say: <b>“I'm touching it with you… wait. I sense… LIFE. Is it alive?”</b> Go.",
    },

    "34": {
        "kind": "wait", "yes": "39", "no": "40",
        "parts": [
            "Alive. The impressions like you. The letters said nothing, which, for them, is warm.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Stand next to it. Is it BIGGER than you?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "Alive — the impressions like you. Say: <b>“Stand next to it. Is it BIGGER than you?”</b> Go.",
    },

    "35": {
        "kind": "wait", "yes": "41", "no": "42",
        "parts": [
            "No. I knew — the same way I know you skipped Side A. We don't have to do this dance, you and I.",
            ("beat", 0.7),
            "Not alive. We're close. I can feel corners. Say:",
            ("beat", 0.4),
            ("q", "Reach for it. Can you TOUCH it?"),
            ("beat", 0.5),
            "Go.",
        ],
        "caption": "A no — Gerald knew, the same way he knows you skipped Side A. Close now; he can feel corners. Say: <b>“Reach for it. Can you TOUCH it?”</b> Go.",
    },

    # ---------------------------------------------------------------- REVEALS
    # Cooldown choreography: Gerald feeds the description, the magician
    # announces the drawing, THEN "turn the screen around" -> art flips.

    "36": {
        "kind": "reveal", "art": "fish",
        "parts": [
            "Alive. And — hold on.",
            ("beat", 0.7),
            "Wet.",
            ("beat", 0.7),
            "It's wet. I'd stand up for this one if I could.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Scales. A little bubble over its head."),
            ("beat", 0.8),
            "Then finish it:",
            ("beat", 0.4),
            ("q", "You drew a FISH."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Wet. Gerald would stand up for this one if he could. Say: <b>“Scales. A little bubble over its head.”</b> Then: <b>“You drew a FISH.”</b> Turn the screen around.",
    },

    "37": {
        "kind": "reveal", "art": "house",
        "parts": [
            "A no. Felt it in the flywheel.",
            ("beat", 0.6),
            "Listen carefully, because this next part is the whole job. Say it exactly:",
            ("beat", 0.4),
            ("q", "It's not alive — but it is FULL of life. It's where the life lives."),
            ("beat", 0.7),
            "Watch their face. There it is.",
            ("beat", 0.6),
            "Now:",
            ("beat", 0.4),
            ("q", "Square walls. A triangle roof. Smoke from the chimney."),
            ("beat", 0.7),
            ("q", "You drew a HOUSE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": ("A no — felt in the flywheel. This next part is the whole job; say it exactly: <b>“It's not alive — but it is FULL of life. It's where the life lives.”</b> "
                    "Watch their face. Then: <b>“Square walls. A triangle roof. Smoke from the chimney. You drew a HOUSE.”</b> Turn the screen around."),
    },

    "38": {
        "kind": "reveal", "art": "sun",
        "parts": [
            "Can't touch it. Nobody can. That's rather the point.",
            ("beat", 0.6),
            "Very few things can't be touched. All of them headline. Say:",
            ("beat", 0.4),
            ("q", "Of course you can't touch it. It's ninety-three million miles away — and you drew it in the corner of the page, with little lines coming off it."),
            ("beat", 0.7),
            ("q", "You drew the SUN."),
            ("beat", 0.8),
            "Turn the screen around. Feel free to take credit for the warmth.",
        ],
        "caption": ("Can't touch it — nobody can; that's rather the point. Say: <b>“Of course you can't touch it. It's ninety-three million miles away — "
                    "you drew it in the corner of the page with little lines coming off it. You drew the SUN.”</b> Turn the screen around."),
    },

    "39": {
        "kind": "reveal", "art": "tree",
        "parts": [
            "Bigger. Alive. And older than everyone involved.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Roots down. Branches up. You drew the leaves as one big cloud, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a TREE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Bigger, alive, and older than everyone involved. Say: <b>“Roots down. Branches up. The leaves were one big cloud, weren't they. You drew a TREE.”</b> Turn the screen around.",
    },

    "40": {
        "kind": "reveal", "art": "flower",
        "parts": [
            "Smaller. I felt petals. I don't examine how.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A stem. Petals in a ring. You pressed harder on the middle."),
            ("beat", 0.7),
            ("q", "You drew a FLOWER."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Smaller — Gerald felt petals; he doesn't examine how. Say: <b>“A stem. Petals in a ring. You pressed harder on the middle. You drew a FLOWER.”</b> Turn the screen around.",
    },

    "41": {
        "kind": "reveal", "art": "pencil",
        "parts": [
            "Touchable. And somebody in this story has been holding its cousin the whole time.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Long. Thin. A point at one end. You drew the thing you were drawing WITH."),
            ("beat", 0.7),
            ("q", "You drew a PENCIL."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Touchable — and someone in this story has been holding its cousin the whole time. Say: <b>“Long. Thin. A point at one end. You drew the thing you were drawing WITH. You drew a PENCIL.”</b> Turn the screen around.",
    },

    "42": {
        "kind": "reveal", "art": "moon",
        "parts": [
            "Can't touch it. I called that one from inside a cassette, which is where I live.",
            ("beat", 0.6),
            "Far away. Cold. Silver. Say:",
            ("beat", 0.4),
            ("q", "You drew it as a crescent — a little banana in the sky — with stars around it."),
            ("beat", 0.7),
            ("q", "You drew the MOON."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Untouchable — called from inside a cassette, which is where Gerald lives. Say: <b>“You drew it as a crescent — a little banana in the sky — with stars around it. You drew the MOON.”</b> Turn the screen around.",
    },

    "43": {
        "kind": "reveal", "art": "glass",
        "parts": [
            "Hard. And cold. They didn't mention cold. They didn't have to.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A stem. A bowl. A toast at the end of a long week."),
            ("beat", 0.7),
            ("q", "You drew a GLASS."),
            ("beat", 0.8),
            "Turn the screen around. Cheers.",
        ],
        "caption": "Hard — and cold. They didn't mention cold; they didn't have to. Say: <b>“A stem. A bowl. A toast at the end of a long week. You drew a GLASS.”</b> Turn the screen around. Cheers.",
    },

    "44": {
        "kind": "reveal", "art": "ball",
        "parts": [
            "Not hard. Soft skin, full of air. I had it the moment they squeezed.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It wants to be thrown. It spends its whole life leaving."),
            ("beat", 0.7),
            ("q", "You drew a BALL."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Not hard — soft skin, full of air. Say: <b>“It wants to be thrown. It spends its whole life leaving. You drew a BALL.”</b> Turn the screen around.",
    },

    "45": {
        "kind": "reveal", "art": "car",
        "parts": [
            "They own one. I've ridden in it, in the sense that matters least.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Four wheels. Windows. Parked outside a childhood house."),
            ("beat", 0.7),
            ("q", "You drew a CAR."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "They own one — Gerald has ridden in it, in the sense that matters least. Say: <b>“Four wheels. Windows. Parked outside a childhood house. You drew a CAR.”</b> Turn the screen around.",
    },

    "46": {
        "kind": "reveal", "art": "plane",
        "parts": [
            "They don't own one. Nobody owns one. It belongs to the sky, and to a leasing company.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew it with little windows down the side, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a PLANE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Nobody owns one — it belongs to the sky, and to a leasing company. Say: <b>“You drew it with little windows down the side, didn't you. You drew a PLANE.”</b> Turn the screen around.",
    },

    "47": {
        "kind": "reveal", "art": "cat",
        "parts": [
            "Smaller. Warm. And profoundly uninterested in either of us.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Whiskers. Pointed ears. It is ignoring you right now."),
            ("beat", 0.7),
            ("q", "You drew a CAT."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Smaller, warm, and profoundly uninterested in either of us. Say: <b>“Whiskers. Pointed ears. It's ignoring you right now. You drew a CAT.”</b> Turn the screen around.",
    },

    "48": {
        "kind": "reveal", "art": "stickman",
        "parts": [
            "Not smaller. Of course not. It's exactly your size. It has always been exactly your size.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A round head. Stick arms, straight out. A self-portrait, age ten."),
            ("beat", 0.7),
            ("q", "You drew a little STICKMAN. You drew YOU."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Not smaller — it's exactly your size. It always was. Say: <b>“A round head. Stick arms straight out. A self-portrait, age ten. You drew a STICKMAN — you drew YOU.”</b> Turn the screen around.",
    },

    "rman": {  # Stickman via the man-check objection
        "kind": "reveal", "art": "stickman",
        "parts": [
            "They argued.",
            ("beat", 0.8),
            "Good. Arguments have pulses.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew a person. A round head. Stick arms, straight out."),
            ("beat", 0.7),
            ("q", "That's YOU, isn't it. You drew yourself."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "They argued. Good — arguments have pulses. Say: <b>“You drew a person. Round head, stick arms straight out. That's YOU, isn't it.”</b> Turn the screen around.",
    },

    "49": {
        "kind": "reveal", "art": "table",
        "parts": [
            "At home. Naturally. You ate off yours this evening. We'll leave it there.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Four legs. A flat top. The whole family around it."),
            ("beat", 0.7),
            ("q", "You drew a TABLE."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "At home, naturally — you ate off yours this evening; we'll leave it there. Say: <b>“Four legs. A flat top. The whole family around it. You drew a TABLE.”</b> Turn the screen around.",
    },

    "50": {
        "kind": "reveal", "art": "boat",
        "parts": [
            "Not at home. It lives on the water. Most of the good ones do.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A little hull. A sail. And you always drew the waves as tiny letter W's, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a BOAT."),
            ("beat", 0.8),
            "Turn the screen around.",
        ],
        "caption": "Not at home — it lives on the water. Most of the good ones do. Say: <b>“A little hull. A sail. You always drew the waves as tiny W's, didn't you. You drew a BOAT.”</b> Turn the screen around.",
    },

    "51": {
        "kind": "reveal", "art": "heart",
        "parts": [
            "No S.",
            ("beat", 0.8),
            "For once, a no is the best possible news. A. T. R. And no S.",
            ("beat", 0.7),
            "I know this one. Stand up straight.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It's not letters anymore. I can FEEL this one. It's beating."),
            ("beat", 0.7),
            ("q", "You drew a HEART."),
            ("beat", 0.8),
            "Turn the screen around. Take your time.",
        ],
        "caption": "No S — and for once, a no is the best possible news. Stand up straight: <b>“It's not letters anymore. I can FEEL this one. It's beating. You drew a HEART.”</b> Turn the screen around. Take your time.",
    },

    "52": {
        "kind": "reveal", "art": "star",
        "parts": [
            "Four for four. It happens. Rarely, and to other people, but it happens.",
            ("beat", 0.7),
            "Slowly now. Say:",
            ("beat", 0.4),
            ("q", "You were ten years old, bored out of your mind… and you reached for the sky."),
            ("beat", 0.7),
            ("q", "You drew a STAR."),
            ("beat", 0.8),
            "Turn the screen around. That one's yours.",
        ],
        "caption": "Four for four. It happens — rarely, and to other people. Slowly: <b>“You were ten years old, bored out of your mind… and you reached for the sky. You drew a STAR.”</b> Turn the screen around. That one's yours.",
    },

    # ---------------------------------------------------------------- OUTRO
    "finale": {
        "kind": "end", "yes": "extras",
        "parts": [
            ("flap",),
            ("beat", 0.8),
            "That's the routine. Let them have the moment.",
            ("beat", 0.6),
            "Don't explain anything. You couldn't. But don't.",
            ("beat", 0.8),
            "You were adequate. That's my second-highest grade. No one has received the first.",
            ("beat", 0.8),
            "The rest of this side is licensing information. Press stop, and rewind the whole tape for your next subject.",
            ("beat", 0.7),
            "Hydrate. It won't fix anything, but it's good for you.",
            ("beat", 0.7),
            "Gerald out.",
        ],
        "caption": ("That's the routine. Don't explain anything — you couldn't, but don't. You were adequate: Gerald's second-highest grade. No one has received the first. "
                    "<b>Press ■ to rewind for your next subject.</b>"),
    },

    "extras": {  # easter egg: they kept playing into the "licensing information"
        "kind": "end", "yes": None,
        "parts": [
            "This recording is the property of Gerald Enterprises, Reseda, California.",
            ("beat", 0.6),
            "Mind-Aerobics is a registered trademark of a company that no longer exists.",
            ("beat", 0.6),
            "Results not typical. No results are typical.",
            ("beat", 0.6),
            "No refunds. Side A is sold separately. It has always been sold separately.",
            ("beat", 1.4),
            "You're still listening.",
            ("beat", 0.8),
            "The workout is over. Go outside.",
            ("beat", 0.8),
            ("flap",),
        ],
        "caption": ("This recording is the property of Gerald Enterprises, Reseda, CA. Mind-Aerobics is a registered trademark of a company that no longer exists. "
                    "Results not typical. No refunds. Side A is sold separately. It has always been sold separately. … You're still listening. The workout is over. Go outside."),
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
