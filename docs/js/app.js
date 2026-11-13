// How to Read Minds: one tape after another.
//
// What it must look like: a cassette player with four keys.
// What happens: from tape 4 on, each tape has more than one recording, and the
// way NEXT is pressed chooses. A tap is yes. A press held until the key
// latches is no. Same key, same thumb, same place.

import { DOODLES } from './doodles.js';

const HOLD_MS = 420;      // held this long, the key latches by itself: "no"
const SWAP_MS = 760;      // one tape out, the next one in

const $ = (id) => document.getElementById(id);
const el = {
  case: $('case'), deck: $('deck'), cass: $('cass'), paper: $('paper'),
  num: $('lNum'), title: $('cassTitle'),
  packL: $('packL'), packR: $('packR'),
  next: $('kNext'), play: $('kPlay'), stop: $('kStop'), rew: $('kRew'),
  slip: $('slip'),
};
const DEBUG = new URLSearchParams(location.search).has('debug');

let SEGS = {};
let START = '';
let ctx = null;
const buffers = new Map();          // id or fx name -> AudioBuffer (absent = silent run-through)

const st = {
  mode: 'loading',                  // loading | idle | swap | playing | stopped | ended | done
  cur: null,                        // recording in the player
  from: null,                       // the recording whose answer chose `cur`, if it was a choice
  empty: false,                     // the tape was taken back out; the player is empty
  pos: 0,                           // where a stopped tape is
  turned: false,                    // the paper shows the drawing
  src: null, t0: 0, run: 0, timer: 0,
};

/* ------------------------------------------------------------ loading */

async function boot() {
  renderPaper();
  let data;
  try {
    data = await (await fetch('data/tapes.json')).json();
  } catch {
    return;
  }
  SEGS = data.segs; START = data.start;

  const AC = window.AudioContext || window.webkitAudioContext;
  ctx = new AC();
  try { if (navigator.audioSession) navigator.audioSession.type = 'playback'; } catch {}

  const jobs = Object.entries(SEGS).map(([id, s]) => [id, s.file]);
  for (const fx of ['key', 'stop', 'swap', 'rew']) jobs.push([fx, `audio/fx-${fx}.mp3`]);
  await Promise.all(jobs.map(async ([id, file]) => {
    try {
      const r = await fetch(file);
      if (!r.ok) throw 0;
      buffers.set(id, await ctx.decodeAudioData(await r.arrayBuffer()));
    } catch { /* silent run-through: timers stand in for audio */ }
  }));
  st.mode = 'idle';
  el.case.classList.remove('loading');
  render();
}

/* ------------------------------------------------------------ transport */

function fx(name) {
  const b = buffers.get(name);
  if (!b) return;
  const s = ctx.createBufferSource();
  s.buffer = b; s.connect(ctx.destination); s.start();
}

const dur = (id) => buffers.get(id)?.duration ?? SEGS[id].dur;

function elapsed() {
  if (st.mode !== 'playing') return st.pos;
  const now = buffers.has(st.cur) ? ctx.currentTime : performance.now() / 1000;
  return Math.min(now - st.t0, dur(st.cur));
}

function halt() {
  st.run += 1;
  clearTimeout(st.timer);
  if (st.src) { try { st.src.stop(); } catch {} st.src = null; }
}

function start(id, offset = 0) {
  halt();
  st.cur = id; st.mode = 'playing'; st.empty = false;
  if (offset === 0) st.turned = false;
  const run = st.run;
  const done = () => { if (run === st.run) onEnd(); };
  const b = buffers.get(id);
  if (b) {
    const s = ctx.createBufferSource();
    s.buffer = b; s.connect(ctx.destination); s.onended = done;
    st.t0 = ctx.currentTime - offset;
    s.start(0, Math.min(offset, b.duration - 0.02));
    st.src = s;
  } else {
    st.t0 = performance.now() / 1000 - offset;
    st.timer = setTimeout(done, Math.max(0, SEGS[id].dur - offset) * 1000);
  }
  wake(true);
  render();
}

function onEnd() {
  st.src = null;
  st.pos = dur(st.cur);
  st.mode = SEGS[st.cur].next ? 'ended' : 'done';
  if (st.mode === 'done') wake(false);
  render();
}

// Take the tape out, put `id` in, play it.
function change(id) {
  halt();
  st.mode = 'swap';
  fx('swap');
  st.empty = true;                  // the old tape slides out (if there is one)
  render();
  setTimeout(() => {
    st.cur = id; st.pos = 0; st.turned = false; st.empty = false;
    render();
  }, SWAP_MS * 0.45);
  setTimeout(() => { if (st.mode === 'swap') start(id); }, SWAP_MS);
}

const pick = (id, answer) => {
  const n = SEGS[id].next;
  return typeof n === 'string' ? n : n[answer];
};

const canNext = () => st.mode === 'idle' || st.mode === 'ended';

// NEXT went down and latched. `answer` is how: 'yes' by a tap, 'no' by a hold.
function next(answer) {
  ctx?.resume();
  fx('key');
  if (st.mode === 'idle') { st.from = null; change(START); return; }
  const choice = typeof SEGS[st.cur].next !== 'string';
  const target = pick(st.cur, answer);
  st.from = choice ? st.cur : null;
  change(target);
}

// PLAY only ever resumes a tape that is in the player and not at its end.
function play() {
  ctx?.resume();
  if (st.mode !== 'stopped') return;
  fx('key');
  start(st.cur, st.pos);
}

function stop() {
  if (st.mode !== 'playing') return;
  st.pos = elapsed();
  halt();
  st.mode = 'stopped';
  fx('stop');
  render();
}

function rewind() {
  if (!st.cur || st.empty || st.mode === 'swap' || st.mode === 'loading') return;
  const at = elapsed();
  if (at === 0) return;
  const live = st.mode === 'playing' || st.mode === 'stopped';
  halt();
  fx('rew');
  el.case.classList.add('rewinding');
  setTimeout(() => el.case.classList.remove('rewinding'), 620);
  if (live && st.from && at < SEGS[st.cur].safe) {
    // The tape has only said its number. Take it back out, so NEXT can be
    // pressed again.
    st.cur = st.from; st.from = null;
    st.pos = dur(st.cur); st.mode = 'ended'; st.empty = true;
  } else {
    st.pos = 0; st.mode = 'stopped'; st.turned = false;
  }
  render();
}

function reset() {
  halt();
  Object.assign(st, { mode: 'idle', cur: null, from: null, empty: false, pos: 0, turned: false });
  wake(false);
  render();
}

/* ------------------------------------------------------------ the NEXT key */

let press = null;                   // { timer, latched }
let forced = null;                  // debug buttons

function nextDown() {
  if (press) return;
  el.next.classList.add('down');
  if (!canNext()) { press = { latched: true, timer: 0 }; return; }
  press = { latched: false, timer: 0 };
  press.timer = setTimeout(() => {
    if (!press) return;
    press.latched = true;
    next(forced ?? 'no');
    forced = null;
  }, HOLD_MS);
}

function nextUp(cancel = false) {
  if (!press) return;
  clearTimeout(press.timer);
  const latched = press.latched;
  press = null;
  el.next.classList.remove('down');
  if (!latched && !cancel && canNext()) { next(forced ?? 'yes'); forced = null; }
  ctx?.resume();
}

function bindKey(node, down, up) {
  node.addEventListener('pointerdown', (e) => {
    e.preventDefault();
    try { node.setPointerCapture(e.pointerId); } catch {}
    down();
  });
  node.addEventListener('pointerup', (e) => { e.preventDefault(); up(false); });
  node.addEventListener('pointercancel', () => up(true));
  node.addEventListener('contextmenu', (e) => e.preventDefault());
}
const simple = (node, action) => bindKey(node,
  () => { node.classList.add('down'); action(); },
  () => { node.classList.remove('down'); render(); });

bindKey(el.next, nextDown, nextUp);
simple(el.play, play);
simple(el.stop, stop);
simple(el.rew, rewind);

// Rehearsal at a desk: Space is NEXT (tap or hold), or resumes a stopped tape.
document.addEventListener('keydown', (e) => {
  if (e.repeat || !el.slip.hidden) return;
  if (e.code === 'Space' || e.code === 'Enter') { e.preventDefault(); if (st.mode === 'stopped') play(); else nextDown(); }
  else if (e.code === 'KeyS') stop();
  else if (e.code === 'KeyR' || e.code === 'ArrowLeft') rewind();
});
document.addEventListener('keyup', (e) => {
  if (e.code === 'Space' || e.code === 'Enter') { e.preventDefault(); nextUp(); }
});

/* ------------------------------------------------------------ drawing */

const esc = (t) => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');

// What the voice has said so far on this tape, typed out as it is spoken.
function typed(seg, t) {
  let html = '';
  for (const [from, to, text, say] of seg.lines) {
    if (t < from) break;
    const n = t >= to ? text.length : Math.ceil(text.length * (t - from) / (to - from));
    const body = esc(text.slice(0, n));
    html += say ? `<p class="say">&ldquo;${body}${n === text.length ? '&rdquo;' : ''}</p>` : `<p>${body}</p>`;
  }
  return html;
}

// The paper: the cover before anything is played, the transcript while a tape
// plays, and the drawing at the end.
function renderPaper() {
  const seg = st.cur && !(st.empty && st.mode !== 'swap') && SEGS[st.cur];
  let html = '', kind = 'type';
  if (!st.cur) {
    kind = 'cover';
    html = '<h1>How to<br>Read Minds</h1>';
  } else if (seg && st.turned) {
    kind = 'leaf';
    html = DOODLES[seg.art] + (st.mode === 'done' ? '<button class="again" type="button">Start over</button>' : '');
  } else if (seg && st.mode !== 'swap') {
    html = typed(seg, elapsed());
  }
  if (el.paper.dataset.sig === html) return;
  el.paper.dataset.sig = html;
  el.paper.className = `paper ${kind}`;
  el.paper.innerHTML = html;
  el.paper.querySelector('.again')?.addEventListener('click', reset);
}

function render() {
  const seg = st.cur && SEGS[st.cur];
  const tape = seg ? seg.tape : 1;
  el.num.textContent = tape;
  el.title.textContent = `Tape ${tape}`;
  el.case.classList.toggle('playing', st.mode === 'playing');
  el.cass.classList.toggle('away', !st.cur || st.empty);
  if (st.mode === 'playing') el.play.classList.add('down');
  else if (!el.play.matches(':active')) el.play.classList.remove('down');
  renderPaper();
  renderDebug();
}

function frame() {
  if (st.cur && !st.empty) {
    const t = elapsed();
    const seg = SEGS[st.cur];
    const p = Math.min(1, t / dur(st.cur));
    el.packL.setAttribute('r', (42 - 19 * p).toFixed(1));
    el.packR.setAttribute('r', (23 + 19 * p).toFixed(1));
    if (seg.page && !st.turned && st.mode === 'playing' && t >= seg.page) st.turned = true;
    if (st.mode === 'playing') renderPaper();
  }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);

/* ------------------------------------------------------------ the slip */

const seen = () => { try { return localStorage.getItem('tr-slip') === '2'; } catch { return false; } };
const openSlip = () => { el.slip.hidden = false; };
$('slipClose').addEventListener('click', () => {
  el.slip.hidden = true;
  try { localStorage.setItem('tr-slip', '2'); } catch {}
});
$('slipReset').addEventListener('click', () => { reset(); el.slip.hidden = true; });
if (!seen() && !DEBUG) openSlip();

let slipTimer = 0;
el.deck.addEventListener('pointerdown', () => { slipTimer = setTimeout(openSlip, 1000); });
for (const ev of ['pointerup', 'pointerleave', 'pointercancel']) {
  el.deck.addEventListener(ev, () => clearTimeout(slipTimer));
}
el.deck.addEventListener('contextmenu', (e) => e.preventDefault());

/* ------------------------------------------------------------ odds and ends */

let lock = null;
async function wake(on) {
  try {
    if (on && !lock) lock = await navigator.wakeLock?.request('screen');
    if (!on && lock) { await lock.release(); lock = null; }
  } catch { lock = null; }
}
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && st.mode === 'playing') { lock = null; wake(true); }
});

function outs(id, found = new Set()) {
  const s = SEGS[id];
  if (s.art) found.add(s.art);
  else for (const t of typeof s.next === 'string' ? [s.next] : Object.values(s.next)) outs(t, found);
  return found;
}

function renderDebug() {
  if (!DEBUG || !START) return;
  const left = [...outs(st.cur || START)];
  $('dbgInfo').textContent =
    `${st.cur ?? '-'} ${st.mode}${st.empty ? ' empty' : ''} from=${st.from ?? '-'}\n${left.length}: ${left.join(' ')}`;
}

if (DEBUG) {
  $('debug').hidden = false;
  const tap = (a) => { forced = a; nextDown(); nextUp(); };
  $('dbgYes').addEventListener('click', () => tap('yes'));
  $('dbgNo').addEventListener('click', () => tap('no'));
  $('dbgEnd').addEventListener('click', () => {
    if (st.mode === 'playing') start(st.cur, Math.max(0, dur(st.cur) - 0.4));
  });
  window.__tr = { st, SEGS: () => SEGS };
}

if ('serviceWorker' in navigator && location.protocol !== 'file:' && !DEBUG) {
  navigator.serviceWorker.register('./sw.js').catch(() => {});
}
boot();
