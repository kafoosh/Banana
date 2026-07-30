// AudioMaster™ 98 — one fake tape, many real branches.
// The illusion contract: everything on screen behaves like a dumb linear
// player. Branching happens ONLY through the transport buttons:
//   play at a wait-point  -> the "yes" continuation
//   rewind, then play     -> the "no" continuation (looks like re-listening)

import { ART, OUT_NAMES } from './art.js';

const $ = (id) => document.getElementById(id);
const win = $('win'), tbar = $('tbar'), nag = $('nag');
const tapeFace = $('tapeFace'), tapeArt = $('tapeArt'), artFrame = $('artFrame');
const lcdTime = $('lcdTime'), lcdStat = $('lcdStat'), lcdFile = $('lcdFile');
const progFill = $('progFill'), progThumb = $('progThumb'), toastEl = $('toast');
const btnPlay = $('btnPlay'), btnRew = $('btnRew'), btnStop = $('btnStop');
const playLabel = $('playLabel'), cc = $('cc'), ccText = $('ccText');
const insert = $('insert');

const TOTAL = 11 * 60 + 47;           // fake "11:47" side length
const BOOT_CAPTION = ccText.innerHTML;
const DEBUG = new URLSearchParams(location.search).has('debug');

let SEGS = {};                        // id -> {kind, play, rew, art, caption, file, dur}
let ctx = null, gain = null;
const buffers = new Map();            // id -> AudioBuffer | null (null = silent/timer mode)

const st = {
  mode: 'boot',                       // boot|ready|playing|waiting|paused|stopped|ended
  seg: null, offset: 0, pendingNo: false, fake: 0,
  src: null, segBase: 0, segStartCtx: 0, timerStart: 0, timerId: 0, runToken: 0,
};
let wakeLock = null;

/* ---------------- loading ---------------- */

async function boot() {
  try {
    const res = await fetch('data/segments.json');
    const data = await res.json();
    SEGS = data.segments;
    lcdFile.textContent = data.track || lcdFile.textContent;
  } catch {
    status('TAPE MISSING — SEE README');
    return;
  }
  ctx = new (window.AudioContext || window.webkitAudioContext)();
  gain = ctx.createGain();
  gain.connect(ctx.destination);

  const ids = Object.keys(SEGS);
  let done = 0;
  status(`LOADING TAPE… 0/${ids.length}`);
  await Promise.all(ids.map(async (id) => {
    try {
      const r = await fetch(SEGS[id].file);
      if (!r.ok) throw new Error();
      const ab = await r.arrayBuffer();
      buffers.set(id, await ctx.decodeAudioData(ab));
    } catch {
      buffers.set(id, null);          // silent-rehearsal fallback: captions + timer
    }
    done += 1;
    if (st.mode === 'boot') status(`LOADING TAPE… ${done}/${ids.length}`);
  }));
  st.mode = 'ready';
  status('READY — 1 TRACK LOADED');
  updateDebug();
}

/* ---------------- transport core ---------------- */

function stopSource() {
  st.runToken += 1;                   // invalidate pending onended / timers
  clearTimeout(st.timerId);
  if (st.src) { try { st.src.stop(); } catch {} st.src = null; }
}

function elapsed() {
  const buf = buffers.get(st.seg);
  if (buf) return st.segBase + (ctx.currentTime - st.segStartCtx);
  return (performance.now() - st.timerStart) / 1000;
}

function segDur(id) {
  const buf = buffers.get(id);
  return buf ? buf.duration : (SEGS[id]?.dur || 8);
}

function playSegment(id, offset = 0) {
  const seg = SEGS[id];
  if (!seg) return;
  stopSource();
  st.seg = id; st.offset = offset; st.mode = 'playing';
  setCaption(seg.caption);
  status('PLAYING');
  render();

  const token = st.runToken;
  const buf = buffers.get(id);
  if (buf) {
    const src = ctx.createBufferSource();
    src.buffer = buf;
    src.connect(gain);
    src.onended = () => { if (token === st.runToken) onSegmentEnd(); };
    st.segBase = offset; st.segStartCtx = ctx.currentTime;
    src.start(0, Math.min(offset, Math.max(0, buf.duration - 0.05)));
    st.src = src;
  } else {
    st.timerStart = performance.now() - offset * 1000;
    st.timerId = setTimeout(() => { if (token === st.runToken) onSegmentEnd(); },
      Math.max(200, (segDur(id) - offset) * 1000));
  }
  updateDebug();
}

function holdSegment(nextMode, statText) {
  st.offset = Math.min(elapsed(), segDur(st.seg));
  stopSource();
  st.mode = nextMode;
  status(statText);
  render();
}

function onSegmentEnd() {
  const seg = SEGS[st.seg];
  st.src = null;
  if (seg.kind === 'wait') {
    st.mode = 'waiting'; st.offset = segDur(st.seg);
    status('PAUSED — AWAITING PERFORMANCE');
    render();
  } else if (seg.kind === 'auto') {
    playSegment(seg.play);
  } else if (seg.kind === 'reveal') {
    flipArt(seg.art);
    const token = st.runToken;
    st.timerId = setTimeout(() => { if (token === st.runToken) playSegment('finale'); }, 1600);
  } else { // end
    st.mode = 'ended';
    status(st.seg === 'finale' ? 'END OF SIDE — PRESS ■ TO REWIND' : 'END OF SIDE');
    render();
  }
  updateDebug();
}

function fullReset() {
  stopSource();
  st.mode = 'ready'; st.seg = null; st.offset = 0; st.fake = 0; st.pendingNo = false;
  tapeArt.hidden = true; tapeFace.hidden = false;
  setCaption(BOOT_CAPTION, true);
  status('READY — 1 TRACK LOADED');
  releaseWake();
  render(); updateDebug();
}

/* ---------------- the three buttons ---------------- */

btnPlay.addEventListener('click', () => {
  switch (st.mode) {
    case 'boot': status('LOADING TAPE… ONE MOMENT'); break;
    case 'ready':
      ctx.resume();
      requestWake();
      playSegment('intro');
      break;
    case 'playing':
      holdSegment('paused', 'PAUSED');
      break;
    case 'paused':
    case 'stopped':
      ctx.resume();
      playSegment(st.seg, st.offset);
      break;
    case 'waiting': {
      const seg = SEGS[st.seg];
      ctx.resume();
      if (st.pendingNo) {
        st.pendingNo = false;
        if (seg.rew) playSegment(seg.rew);
        else playSegment(st.seg, Math.max(0, segDur(st.seg) - 10)); // honest replay
      } else if (seg.play) {
        playSegment(seg.play);
      }
      break;
    }
    case 'ended': {
      const seg = SEGS[st.seg];
      if (seg && seg.play) playSegment(seg.play); // finale -> "licensing information"
      break;
    }
  }
});

btnRew.addEventListener('click', () => {
  switch (st.mode) {
    case 'playing': {
      const off = Math.max(0, elapsed() - 10);
      st.fake = Math.max(0, st.fake - 10);
      toast();
      playSegment(st.seg, off);
      break;
    }
    case 'paused':
    case 'stopped':
      st.offset = Math.max(0, st.offset - 10);
      st.fake = Math.max(0, st.fake - 10);
      toast();
      break;
    case 'waiting':
      st.pendingNo = true;            // the whole secret, part 2
      st.fake = Math.max(0, st.fake - 10);
      toast();
      break;
    case 'ended':
      fullReset();                    // "rewind the whole thing for your next subject"
      break;
  }
  render();                           // playhead jump must show even while stopped
  updateDebug();
});

btnStop.addEventListener('click', () => {
  switch (st.mode) {
    case 'playing':
    case 'paused':
    case 'waiting':
      holdSegment('stopped', 'STOPPED — PRESS ■ AGAIN TO REWIND');
      break;
    case 'stopped':
    case 'ended':
      fullReset();
      break;
  }
});

/* emergency: triple-tap the title bar rewinds the whole cassette */
let taps = [];
tbar.addEventListener('click', () => {
  const now = Date.now();
  taps = taps.filter((t) => now - t < 900).concat(now);
  if (taps.length >= 3) { taps = []; fullReset(); }
});

/* ---------------- reveal ---------------- */

function flipArt(key) {
  artFrame.innerHTML = ART[key] || '';
  tapeFace.hidden = true;
  tapeArt.hidden = false;
}

/* ---------------- chrome bits ---------------- */

function status(t) { lcdStat.textContent = t; }

function setCaption(html, dim = false) {
  ccText.innerHTML = html;
  ccText.classList.toggle('dim', dim);
  cc.scrollTop = 0;
}

let toastId = 0;
function toast() {
  toastEl.hidden = false;
  clearTimeout(toastId);
  toastId = setTimeout(() => { toastEl.hidden = true; }, 950);
}

function fmt(s) {
  s = Math.max(0, Math.floor(s));
  return `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
}

function render() {
  win.classList.toggle('playing', st.mode === 'playing');
  const icon = { playing: '▶', waiting: '||', paused: '||', stopped: '■', ended: '■' }[st.mode] || '■';
  lcdTime.textContent = `${icon} ${fmt(st.fake)} / 11:47`;
  const pct = Math.min(100, (st.fake / TOTAL) * 100);
  progFill.style.width = pct + '%';
  progThumb.style.left = `calc(${pct}% - ${pct / 12}px)`;
  // pause "icon" is two CSS bars — the ⏸ glyph is missing from some fonts
  btnPlay.innerHTML = st.mode === 'playing' ? '<span class="pbars"><i></i><i></i></span>' : '▶';
  btnPlay.classList.toggle('lit', st.mode !== 'playing');
  btnRew.classList.toggle('lit', st.mode === 'waiting' && st.pendingNo);
  playLabel.textContent =
    st.mode === 'playing' ? 'pause' :
    st.mode === 'ready' ? 'play' : 'resume';
}

/* fake playhead: advances only while "the tape rolls" */
let lastT = performance.now();
function tick(now) {
  const dt = (now - lastT) / 1000;
  lastT = now;
  if (st.mode === 'playing') { st.fake += dt; render(); }
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);

/* ---------------- menus + insert ---------------- */

$('m-help').addEventListener('click', () => { insert.style.display = 'flex'; });
$('m-file').addEventListener('click', flashNag);
$('m-eq').addEventListener('click', flashNag);
$('m-playback').addEventListener('click', () => {
  const off = cc.classList.toggle('ccoff');
  try { localStorage.setItem('am98cc', off ? '0' : '1'); } catch {}
});
function flashNag() {
  nag.classList.remove('flash');
  void nag.offsetWidth;
  nag.classList.add('flash');
}

$('insertHide').addEventListener('click', () => {
  insert.style.display = 'none';
  try { localStorage.setItem('am98insert', '1'); } catch {}
});
try {
  if (localStorage.getItem('am98insert') === '1') insert.style.display = 'none';
  if (localStorage.getItem('am98cc') === '0') cc.classList.add('ccoff');
} catch {}

/* ---------------- wake lock ---------------- */

async function requestWake() {
  try { wakeLock = await navigator.wakeLock?.request('screen'); } catch {}
}
function releaseWake() {
  try { wakeLock?.release(); } catch {}
  wakeLock = null;
}
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && st.mode === 'playing') requestWake();
});

/* ---------------- debug (?debug=1) ---------------- */

function outsFrom(id) {
  const seg = SEGS[id];
  if (!seg) return [];
  if (seg.kind === 'reveal') return [OUT_NAMES[id] || seg.art?.toUpperCase()];
  const outs = new Set();
  if (seg.play) outsFrom(seg.play).forEach((o) => outs.add(o));
  if (seg.rew) outsFrom(seg.rew).forEach((o) => outs.add(o));
  return [...outs];
}

function updateDebug() {
  if (!DEBUG) return;
  const outs = st.seg ? outsFrom(st.seg) : outsFrom('20');
  $('dbgInfo').textContent =
    `seg=${st.seg ?? '–'} mode=${st.mode} pendingNo=${st.pendingNo}\n` +
    `outs(${outs.length}): ${outs.join(', ')}`;
}

if (DEBUG) {
  $('debug').hidden = false;
  $('dbgYes').addEventListener('click', () => { if (st.mode === 'waiting') { st.pendingNo = false; btnPlay.click(); } });
  $('dbgNo').addEventListener('click', () => { if (st.mode === 'waiting') { btnRew.click(); btnPlay.click(); } });
  $('dbgSkip').addEventListener('click', () => {
    if (st.mode === 'playing') playSegment(st.seg, Math.max(0, segDur(st.seg) - 0.8));
  });
  $('dbgMute').addEventListener('click', () => {
    if (!gain) return;
    gain.gain.value = gain.gain.value ? 0 : 1;
  });
}

/* ---------------- go ---------------- */

if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  navigator.serviceWorker.register('./sw.js').catch(() => {});
}
boot();
