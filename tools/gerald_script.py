# MIND-AEROBICS™ with Gerald — full performance script + branch graph.
# Register: 80s/90s home-workout cassette. Relentlessly peppy, turns
# sarcastic on misses. The performer is "champ" / "superstar" — never
# anything else.
#
# Single source of truth: build_audio.py renders TTS from `parts` and emits
# docs/data/segments.json (captions, graph, file map, durations) for the app.
#
# Part syntax:
#   "text"            spoken by Gerald at workout pace
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
# On a NO he *called it* — he's been sure since 1987. That knowledge is played
# as workout-guru showboating, never explained.

FAKE_RUNTIME = "11:47"  # printed on the player; no path comes close to filling it
TRACK_NAME = "MindAerobics_Tape2_SideB.mp3"

SEGMENTS = {

    # ---------------------------------------------------------------- ACT 1+2
    "intro": {
        "kind": "wait", "yes": "ind1", "no": None,
        "parts": [
            "Side B! Your first performance — with a real, live subject! I'm Gerald, and THIS is Mind-Aerobics.",
            ("beat", 0.7),
            "Equipment check! You'll need: one subject, seated. One brain — yours. Optional, but encouraged.",
            ("beat", 0.8),
            "House rules, champ. Rule one! You repeat only the lines I give you, word for word. You are my echo. I am your burn.",
            ("beat", 0.6),
            "Rule two! When I stop the tape — and I will, I stop whenever it's time for YOU to work — you say the line, and you get their answer.",
            ("beat", 0.6),
            "Rule three! Do NOT tell me their answer. Don't say it, don't mouth it, don't tap it out in code. Just press play.",
            ("beat", 0.5),
            "I'll know.",
            ("beat", 0.7),
            "I always know. And that is not the weird part of this tape.",
            ("beat", 0.9),
            "Now! Seat your subject across from you. Phone flat on the table, face up, where they can watch it. It's just a tape. Let them see it's just a tape.",
            ("beat", 0.6),
            "Get set. I'll wait. I'm a tape — waiting is my whole life. Press play when you're both ready!",
        ],
        "caption": ("Side B — your first performance! Rule 1: repeat only Gerald's lines, word for word. "
                    "Rule 2: when the tape stops, say the line and get their answer. Rule 3: <b>don't tell Gerald the answer — just press play. He'll know.</b> "
                    "Seat your subject, phone flat between you, face up. <b>Play when you're both ready!</b>"),
    },

    "ind1": {
        "kind": "wait", "yes": "ind2", "no": None,
        "parts": [
            "WARM-UP TIME! Subject! Yes, you — hello! I'm Gerald. Don't answer me; nobody answers me. Eyes closed!",
            ("beat", 1.0),
            "We are jogging backwards — through TIME. You're ten years old. Maybe twelve. Last class of the day. The clock is crawling, and the teacher's voice is a hundred miles away.",
            ("beat", 0.8),
            "There's a pencil in your hand. And look at you go — without ever deciding to, you're doodling! The same little doodle you always drew. Simple! Five seconds of pencil, ten tops. You're a kid, not Leonardo.",
            ("beat", 0.9),
            "And DON'T you dare make it a smiley face — too easy, no burn! No mountains! No bicycles — this is a workout, not a race! And none of those empty shapes — no circles, no triangles. A REAL thing. A thing anybody would recognize the instant they saw it!",
            ("beat", 1.0),
            "See it on the page. Small. In pencil. Yours. Hold it! Hooold it!",
            ("beat", 0.9),
            "Do not say it out loud. Not now. Not ever.",
            ("beat", 0.7),
            "Champ: the tape stops HERE. When your subject nods, press play. Great hustle!",
        ],
        "caption": ("「TO YOUR SUBJECT」 Eyes closed — we're jogging backwards through time! You're ten, maybe twelve, last class of the day, "
                    "pencil in hand, doodling the same little doodle you always drew — five, ten seconds of pencil. "
                    "NOT a smiley face, NO mountains, NO bicycles, no circles or triangles — a REAL thing anybody would recognize! "
                    "See it. Hold it. Never say it. <b>Press play when they nod!</b>"),
    },

    "ind2": {
        "kind": "wait", "yes": "preflight", "no": None,
        "parts": [
            "Eyes open! Beautiful.",
            ("beat", 0.6),
            "Subject — take that little doodle and BLOW IT UP! The real thing, real size, sitting right there in the room between you two. Feel the presence!",
            ("beat", 1.0),
            "Now — think of it as a WORD. If you'd drawn a smiley face — which you did NOT, because I said so — you'd see a face, and the word would be SMILEY.",
            ("beat", 0.7),
            "Got your word? Time for LETTER LUNGES! Walk those letters, one at a time. First letter… aaand the next… keep going… all the way to the end!",
            ("beat", 1.4),
            "And AGAIN! Slower! Feel every letter!",
            ("beat", 1.4),
            "Beautiful.",
            ("beat", 0.6),
            "Champ: ask them — do you have it? A nod is enough. If they're taking forever, remind them gently: it's a doodle, not a dissertation.",
            ("beat", 0.5),
            "Tape stops here. Play when they nod!",
        ],
        "caption": ("「TO YOUR SUBJECT」 Blow the doodle up — real thing, real size, right there between you! Now think of it as a WORD "
                    "(a smiley face would be SMILEY). LETTER LUNGES: walk its letters one at a time… and again, slower! "
                    "「TO YOU」 Ask: <b>“Do you have it?”</b> A nod is enough. <b>Play when they nod!</b>"),
    },

    "preflight": {
        "kind": "auto", "yes": "20",
        "parts": [
            "From here on, you say ONLY my words — you're the echo, champ.",
            ("beat", 0.5),
            "Shake out those shoulders. Big smile. Psychic posture!",
            ("beat", 0.5),
            "Here! We! GO!",
        ],
        "caption": "From here you say ONLY Gerald's words. Shake out the shoulders. Big smile. Psychic posture. Here! We! GO!",
    },

    # ---------------------------------------------------------------- LETTERS
    "20": {
        "kind": "wait", "yes": "21", "no": "24",
        "parts": [
            "First rep! It's a letter. Say it like you own it:",
            ("beat", 0.4),
            ("q", "I can feel a letter in your word. An A. There's an A — correct?"),
            ("beat", 0.6),
            "Say it! Get their answer! You know what to do.",
        ],
        "caption": "First rep — say it like you own it: <b>“I can feel a letter in your word. An A. There's an A… correct?”</b> Get their answer, then play.",
    },

    "21": {
        "kind": "wait", "yes": "22", "no": "25m",
        "parts": [
            "HA! There's the A! One rep down — feeling loose?",
            ("beat", 0.5),
            "Don't answer. Next rep:",
            ("beat", 0.4),
            ("q", "I see a T as well. Yes?"),
            ("beat", 0.5),
            "Go get it!",
        ],
        "caption": "HA — there's the A! Next rep: <b>“I see a T as well… yes?”</b> Go get it!",
    },

    "22": {
        "kind": "wait", "yes": "23", "no": "26",
        "parts": [
            "Two for two, superstar! Don't peak too early on me.",
            ("beat", 0.5),
            "Little softer now:",
            ("beat", 0.4),
            ("q", "Is that… an R?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "Two for two, superstar! Softer now: <b>“Is that… an R?”</b> Go!",
    },

    "23": {
        "kind": "wait", "yes": "52", "no": "51",
        "parts": [
            "THREE in a row?! Somebody's been doing their mental stretches!",
            ("beat", 0.5),
            "Last letter. Say it like you barely trust it:",
            ("beat", 0.4),
            ("q", "Now I'm not sure about this one. An S?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "THREE in a row! Last letter — barely trust it: <b>“Now I'm not sure about this one… an S?”</b> Go!",
    },

    "24": {  # A missed -> claim S
        "kind": "wait", "yes": "27", "no": "28",
        "parts": [
            "Aaaand that's a no.",
            ("beat", 0.6),
            "Don't ask how I know, champ. I recorded this tape in 1987, and I could feel that no coming from back there.",
            ("beat", 0.6),
            "It's not the tape's fault. It's not the subject's fault. I'll let you do the math.",
            ("beat", 0.7),
            "Shake it off! A miss is just a rep for your ego. Try this one:",
            ("beat", 0.4),
            ("q", "No… no, it's leaning. It's an S. There IS an S."),
            ("beat", 0.5),
            "Say it like you've never been wrong in your life. I believe in you. One of us has to!",
        ],
        "caption": ("Aaaand that's a no — Gerald felt it coming from 1987. Not the tape's fault, not the subject's fault… do the math. "
                    "Shake it off! Say: <b>“No… no, it's leaning — it's an S. There IS an S.”</b> Like you've never been wrong in your life!"),
    },

    # ---------------------------------------------------------------- MAN CHECK
    "25m": {  # T missed -> assert not-alive (Stickman safety valve)
        "kind": "wait", "yes": "25", "no": "rman",
        "parts": [
            "That was a no. I knew it before your finger did.",
            ("beat", 0.6),
            "Doesn't matter — GREAT information! You're doing so much better than you think.",
            ("beat", 0.5),
            "No, wait. You're doing exactly as well as you think.",
            ("beat", 0.6),
            "Moving on! Chest out. Say this next one as a FACT, not a question:",
            ("beat", 0.4),
            ("q", "This thing you drew — it is NOT a living thing."),
            ("beat", 0.7),
            "If they nod along, that's a yes. If they ARGUE with you — champ, that's a no.",
            ("beat", 0.5),
            "Either way: press play. I'll feel it.",
        ],
        "caption": ("A no — Gerald knew before your finger did. Chest out; say it as a FACT: <b>“This thing you drew — it is NOT a living thing.”</b> "
                    "Nod = yes. Argument = no. Either way, press play — he'll feel it."),
    },

    # ---------------------------------------------------------------- PROBES
    "25": {
        "kind": "wait", "yes": "29", "no": "30",
        "parts": [
            "Agreed — not alive! You're on the board, champ!",
            ("beat", 0.5),
            "Next station:",
            ("beat", 0.4),
            ("q", "Hold out your hand. Imagine it there. Could you HOLD it in one hand?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "Agreed — not alive! You're on the board! Next station: <b>“Hold out your hand. Imagine it there. Could you HOLD it in one hand?”</b> Go!",
    },

    "26": {
        "kind": "wait", "yes": "31", "no": "32",
        "parts": [
            "No! Yes — I know. I felt it through the magnetic particles. Tape particles don't lie, champ.",
            ("beat", 0.5),
            "Neither do subjects. Only you, when you told yourself you'd warmed up properly.",
            ("beat", 0.6),
            "New station! Say:",
            ("beat", 0.4),
            ("q", "Leave the letters. Let me touch the thing itself. Is it ALIVE?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": ("A no — Gerald felt it through the magnetic particles, and tape particles don't lie. New station: "
                    "<b>“Leave the letters. Let me touch the thing itself. Is it ALIVE?”</b> Go!"),
    },

    "27": {
        "kind": "wait", "yes": "33", "no": "38",
        "parts": [
            "The S! There's the S! And the crowd goes MILD! We're back, baby!",
            ("beat", 0.5),
            "Letters are done — now we work the SENSES. Say:",
            ("beat", 0.4),
            ("q", "Reach out in your mind. Can you TOUCH it?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "There's the S — the crowd goes MILD! Now we work the SENSES. Say: <b>“Reach out in your mind. Can you TOUCH it?”</b> Go!",
    },

    "28": {
        "kind": "wait", "yes": "34", "no": "35",
        "parts": [
            "No again! I know. I KNOW. I knew before you did — I knew YESTERDAY.",
            ("beat", 0.7),
            "Champ. Buddy. Superstar. Look at me. I'm a tape — look at the speaker.",
            ("beat", 0.6),
            "Letters are not your event. And that's FINE! Some athletes are sprinters. Some are… you.",
            ("beat", 0.6),
            "We pivot to RAW IMPRESSIONS — my specialty, and as of right now, yours! Say:",
            ("beat", 0.4),
            ("q", "Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": ("No again — Gerald knew YESTERDAY. Letters are not your event, and that's FINE. Pivot to RAW IMPRESSIONS: "
                    "<b>“Forget letters. Forget words. I'm getting something warmer. Is it ALIVE?”</b> Go!"),
    },

    "29": {
        "kind": "wait", "yes": "43", "no": "44",
        "parts": [
            "Held it! I felt the grip from in here!",
            ("beat", 0.5),
            "Now the surface. Say:",
            ("beat", 0.4),
            ("q", "Squeeze it. Is it HARD?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "Held it — Gerald felt the grip from in there! Now: <b>“Squeeze it. Is it HARD?”</b> Go!",
    },

    "30": {
        "kind": "wait", "yes": "45", "no": "46",
        "parts": [
            "That's a no — called it. Called it in 1987!",
            ("beat", 0.5),
            "Too big for one hand. GOOD! Big thoughts burn more calories! Say:",
            ("beat", 0.4),
            ("q", "It's bigger than both of us. Tell me — do you OWN one?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "A no — called it in 1987! Too big for one hand; big thoughts burn more calories. Say: <b>“It's bigger than both of us. Tell me — do you OWN one?”</b> Go!",
    },

    "31": {
        "kind": "wait", "yes": "47", "no": "48",
        "parts": [
            "It's ALIVE! Feel that cardio!",
            ("beat", 0.5),
            "Say:",
            ("beat", 0.4),
            ("q", "Stand next to it in your mind. Is it SMALLER than you?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "It's ALIVE — feel that cardio! Say: <b>“Stand next to it in your mind. Is it SMALLER than you?”</b> Go!",
    },

    "32": {
        "kind": "wait", "yes": "49", "no": "50",
        "parts": [
            "A no! Shocker. To you. Not to me.",
            ("beat", 0.5),
            "Not alive — but say this part gently, champ:",
            ("beat", 0.4),
            ("q", "It relates to life… it's part of a day."),
            ("beat", 0.6),
            "Let that land. Now hit them with:",
            ("beat", 0.4),
            ("q", "Do you have one at HOME?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "A no — shocker (to you). Gently: <b>“It relates to life… it's part of a day.”</b> Then: <b>“Do you have one at HOME?”</b> Go!",
    },

    "33": {
        "kind": "wait", "yes": "36", "no": "37",
        "parts": [
            "Touchable! Now reach FURTHER — deeper stretch! Say:",
            ("beat", 0.4),
            ("q", "I'm touching it with you… wait. I sense… LIFE. Is it alive?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "Touchable — now reach FURTHER, deeper stretch! Say: <b>“I'm touching it with you… wait. I sense… LIFE. Is it alive?”</b> Go!",
    },

    "34": {
        "kind": "wait", "yes": "39", "no": "40",
        "parts": [
            "ALIVE! See?! The impressions love you — the letters were just jealous!",
            ("beat", 0.5),
            "Say:",
            ("beat", 0.4),
            ("q", "Stand next to it. Is it BIGGER than you?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "ALIVE! The impressions love you — the letters were just jealous. Say: <b>“Stand next to it. Is it BIGGER than you?”</b> Go!",
    },

    "35": {
        "kind": "wait", "yes": "41", "no": "42",
        "parts": [
            "No — and yes, champ, I already knew. The same way I know you skipped Side A's breathing drills.",
            ("beat", 0.6),
            "Not alive! We're close — I can feel corners! Say:",
            ("beat", 0.4),
            ("q", "Reach for it. Can you TOUCH it?"),
            ("beat", 0.5),
            "Go!",
        ],
        "caption": "A no — Gerald knew, the same way he knows you skipped Side A's breathing drills. Close now: <b>“Reach for it. Can you TOUCH it?”</b> Go!",
    },

    # ---------------------------------------------------------------- REVEALS
    # Cooldown choreography: Gerald feeds the description, the magician
    # announces the drawing, THEN "turn the screen around" -> art flips.

    "36": {
        "kind": "reveal", "art": "fish",
        "parts": [
            "Alive — and hold on. Hold on. WET?!",
            ("beat", 0.5),
            "WET! Champ, this is a personal best!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Scales. A little bubble over its head."),
            ("beat", 0.8),
            "Now stick the landing:",
            ("beat", 0.4),
            ("q", "You drew a FISH."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "WET?! A personal best! Say: <b>“Scales. A little bubble over its head.”</b> Stick the landing: <b>“You drew a FISH.”</b> Turn the screen around!",
    },

    "37": {
        "kind": "reveal", "art": "house",
        "parts": [
            "A no — I felt that one in my flywheel.",
            ("beat", 0.5),
            "But listen close, champ. Say this exactly:",
            ("beat", 0.4),
            ("q", "It's not alive — but it is FULL of life. It's where the life lives."),
            ("beat", 0.7),
            "Watch their face. There it is!",
            ("beat", 0.6),
            "Now bring it HOME. Say:",
            ("beat", 0.4),
            ("q", "Square walls. A triangle roof. Smoke from the chimney."),
            ("beat", 0.7),
            ("q", "You drew a HOUSE."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": ("A no — felt in the flywheel. Say exactly: <b>“It's not alive — but it is FULL of life. It's where the life lives.”</b> Watch their face. "
                    "Then: <b>“Square walls. A triangle roof. Smoke from the chimney. You drew a HOUSE.”</b> Turn the screen around!"),
    },

    "38": {
        "kind": "reveal", "art": "sun",
        "parts": [
            "Can't touch it! I KNEW you couldn't — nobody can, that's the POINT!",
            ("beat", 0.6),
            "Champ, very few things in this universe can't be touched, and every single one of them is a headliner. Say:",
            ("beat", 0.4),
            ("q", "Of course you can't touch it. It's ninety-three million miles away — and you drew it in the corner of the page, with little lines coming off it."),
            ("beat", 0.7),
            ("q", "You drew the SUN."),
            ("beat", 0.8),
            "Turn the screen around! Feel that warmth? That's YOU right now!",
        ],
        "caption": ("Can't touch it — nobody can, that's the POINT! Say: <b>“Of course you can't touch it. It's ninety-three million miles away — "
                    "you drew it in the corner of the page with little lines coming off it. You drew the SUN.”</b> Turn the screen around!"),
    },

    "39": {
        "kind": "reveal", "art": "tree",
        "parts": [
            "Bigger! Alive! And older than everybody in the room!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Roots down. Branches up. You drew the leaves as one big cloud, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a TREE."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Bigger, alive, older than everybody here! Say: <b>“Roots down. Branches up. The leaves were one big cloud, weren't they. You drew a TREE.”</b> Turn the screen around!",
    },

    "40": {
        "kind": "reveal", "art": "flower",
        "parts": [
            "Smaller! Knew it — I felt petals. Dainty thought, BIG finish! Say:",
            ("beat", 0.4),
            ("q", "A stem. Petals in a ring. You pressed harder on the middle."),
            ("beat", 0.7),
            ("q", "You drew a FLOWER."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Smaller — Gerald felt petals! Say: <b>“A stem. Petals in a ring. You pressed harder on the middle. You drew a FLOWER.”</b> Turn the screen around!",
    },

    "41": {
        "kind": "reveal", "art": "pencil",
        "parts": [
            "You can touch it — and champ, somebody in this story is already holding its cousin!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Long. Thin. A point at one end. You drew the thing you were drawing WITH."),
            ("beat", 0.7),
            ("q", "You drew a PENCIL."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Touchable — and someone in this story is holding its cousin! Say: <b>“Long. Thin. A point at one end. You drew the thing you were drawing WITH. You drew a PENCIL.”</b> Turn it around!",
    },

    "42": {
        "kind": "reveal", "art": "moon",
        "parts": [
            "Can't touch it — called that one from inside the cassette. Far away. Cold silver.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew it as a crescent — a little banana in the sky — with stars around it."),
            ("beat", 0.7),
            ("q", "You drew the MOON."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Untouchable — called from inside the cassette. Say: <b>“You drew it as a crescent — a little banana in the sky — with stars around it. You drew the MOON.”</b> Turn it around!",
    },

    "43": {
        "kind": "reveal", "art": "glass",
        "parts": [
            "HARD! And cold — they didn't say cold, champ, but I felt the chill on my tape heads!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A stem. A bowl. A toast at the end of a long week."),
            ("beat", 0.7),
            ("q", "You drew a GLASS."),
            ("beat", 0.8),
            "Turn the screen around — and cheers, champ!",
        ],
        "caption": "HARD — and cold, felt right on the tape heads! Say: <b>“A stem. A bowl. A toast at the end of a long week. You drew a GLASS.”</b> Turn it around — cheers!",
    },

    "44": {
        "kind": "reveal", "art": "ball",
        "parts": [
            "Soft! Full of air! I knew it the SECOND they squeezed!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It wants to be thrown. It spends its whole life leaving."),
            ("beat", 0.7),
            ("q", "You drew a BALL."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Soft, full of air — knew it the second they squeezed! Say: <b>“It wants to be thrown. It spends its whole life leaving. You drew a BALL.”</b> Turn it around!",
    },

    "45": {
        "kind": "reveal", "art": "car",
        "parts": [
            "They OWN one! Champ — I have been in it. Spiritually.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Four wheels. Windows. Parked outside a childhood house."),
            ("beat", 0.7),
            ("q", "You drew a CAR."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "They OWN one — Gerald has been in it, spiritually. Say: <b>“Four wheels. Windows. Parked outside a childhood house. You drew a CAR.”</b> Turn it around!",
    },

    "46": {
        "kind": "reveal", "art": "plane",
        "parts": [
            "Don't own one — I knew it, champ. NOBODY owns one. It belongs to the sky!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "You drew it with little windows down the side, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a PLANE."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Don't own one — NOBODY does, it belongs to the sky! Say: <b>“You drew it with little windows down the side, didn't you. You drew a PLANE.”</b> Turn it around!",
    },

    "47": {
        "kind": "reveal", "art": "cat",
        "parts": [
            "Smaller! Warm! And completely ignoring both of us!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Whiskers. Pointed ears. It is ignoring you right now."),
            ("beat", 0.7),
            ("q", "You drew a CAT."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Smaller, warm, and ignoring us both! Say: <b>“Whiskers. Pointed ears. It's ignoring you right now. You drew a CAT.”</b> Turn it around!",
    },

    "48": {
        "kind": "reveal", "art": "stickman",
        "parts": [
            "Not smaller — I KNEW it — because it is exactly your size, champ. It always was.",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A round head. Stick arms, straight out. A self-portrait, age ten."),
            ("beat", 0.7),
            ("q", "You drew a little STICKMAN. You drew YOU."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Not smaller — it's exactly your size, always was. Say: <b>“A round head. Stick arms straight out. A self-portrait, age ten. You drew a STICKMAN — you drew YOU.”</b> Turn it around!",
    },

    "rman": {  # Stickman via the man-check objection
        "kind": "reveal", "art": "stickman",
        "parts": [
            "They ARGUED?! Champ, I have felt that argument coming since the warm-up!",
            ("beat", 0.6),
            "GOOD! An argument means a PULSE! Say:",
            ("beat", 0.4),
            ("q", "You drew a person. A round head. Stick arms, straight out."),
            ("beat", 0.7),
            ("q", "That's YOU, isn't it. You drew yourself."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "They ARGUED — Gerald felt it coming since the warm-up! An argument means a PULSE. Say: <b>“You drew a person. Round head, stick arms straight out. That's YOU, isn't it.”</b> Turn it around!",
    },

    "49": {
        "kind": "reveal", "art": "table",
        "parts": [
            "At home! Naturally! You ATE off yours tonight!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "Four legs. A flat top. The whole family around it."),
            ("beat", 0.7),
            ("q", "You drew a TABLE."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "At home — you ATE off yours tonight! Say: <b>“Four legs. A flat top. The whole family around it. You drew a TABLE.”</b> Turn it around!",
    },

    "50": {
        "kind": "reveal", "art": "boat",
        "parts": [
            "Not at home — knew it! Because it lives on the WATER!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "A little hull. A sail. And you always drew the waves as tiny letter W's, didn't you."),
            ("beat", 0.7),
            ("q", "You drew a BOAT."),
            ("beat", 0.8),
            "Turn the screen around!",
        ],
        "caption": "Not at home — it lives on the WATER! Say: <b>“A little hull. A sail. You always drew the waves as tiny W's, didn't you. You drew a BOAT.”</b> Turn it around!",
    },

    "51": {
        "kind": "reveal", "art": "heart",
        "parts": [
            "No S! And champ — for ONCE, a no is exactly what I wanted to hear!",
            ("beat", 0.6),
            "A… T… R… oh, I know this one. I LOVE this one. Stand tall!",
            ("beat", 0.6),
            "Say:",
            ("beat", 0.4),
            ("q", "It's not letters anymore. I can FEEL this one. It's beating."),
            ("beat", 0.7),
            ("q", "You drew a HEART."),
            ("beat", 0.8),
            "Turn the screen around. Big finish!",
        ],
        "caption": "No S — and for ONCE a no is exactly what Gerald wanted! Stand tall: <b>“It's not letters anymore. I can FEEL this one. It's beating. You drew a HEART.”</b> Turn it around — big finish!",
    },

    "52": {
        "kind": "reveal", "art": "star",
        "parts": [
            "FOUR for FOUR! FLAWLESS ROUTINE! This is what Side A was FOR!",
            ("beat", 0.6),
            "Now slow it down. Cooldown pace. Say:",
            ("beat", 0.4),
            ("q", "You were ten years old, bored out of your mind… and you reached for the sky."),
            ("beat", 0.7),
            ("q", "You drew a STAR."),
            ("beat", 0.8),
            "Turn the screen around, superstar. That one's yours.",
        ],
        "caption": "FOUR for FOUR — flawless routine! Cooldown pace: <b>“You were ten years old, bored out of your mind… and you reached for the sky. You drew a STAR.”</b> Turn it around, superstar.",
    },

    # ---------------------------------------------------------------- OUTRO
    "finale": {
        "kind": "end", "yes": "extras",
        "parts": [
            ("flap",),
            ("beat", 0.8),
            "Aaaand COOLDOWN. Deep breaths. Let them have their moment.",
            ("beat", 0.6),
            "Don't explain anything. Not that you could.",
            ("beat", 0.8),
            "Champ: today, you were adequate. And adequate is my second-highest grade.",
            ("beat", 0.7),
            "The rest of this side is licensing information. Press stop, rewind the whole tape for your next subject — and remember to hydrate. Minds are mostly water.",
            ("beat", 0.8),
            "Gerald out!",
        ],
        "caption": ("COOLDOWN. Let them have their moment — don't explain anything, not that you could. Today you were adequate: Gerald's second-highest grade. "
                    "Hydrate — minds are mostly water. <b>Press ■ to rewind for your next subject.</b>"),
    },

    "extras": {  # easter egg: they kept playing into the "licensing information"
        "kind": "end", "yes": None,
        "parts": [
            "This recording is the property of Gerald Enterprises, Reseda, California.",
            ("beat", 0.5),
            "Mind-Aerobics is not liable for pulled hamstrings, spiritual or otherwise.",
            ("beat", 0.6),
            "Results not typical. Results not, technically, results.",
            ("beat", 0.6),
            "No refunds. Side A is sold separately. It has always been sold separately.",
            ("beat", 1.2),
            ("flap",),
        ],
        "caption": "This recording is the property of Gerald Enterprises, Reseda, CA. Not liable for pulled hamstrings, spiritual or otherwise. Results not typical. No refunds. Side A is sold separately. It has always been sold separately.",
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
