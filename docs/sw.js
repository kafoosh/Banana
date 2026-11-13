/* Offline copy of the whole case, so a performance never depends on a signal. */
const VERSION = 'tr-4';
const CORE = [
  './', './index.html', './css/app.css', './js/app.js', './js/doodles.js',
  './data/tapes.json', './icon.svg', './manifest.webmanifest',
  './fonts/libre-franklin-latin-500-normal.woff2', './fonts/libre-franklin-latin-800-normal.woff2',
  './fonts/courier-prime-latin-400-normal.woff2', './fonts/courier-prime-latin-700-normal.woff2',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

/* Cache first. The page fetches every recording on load, which fills the cache. */
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then((hit) => hit || fetch(e.request).then((res) => {
      if (res.ok && new URL(e.request.url).origin === location.origin) {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(e.request, copy));
      }
      return res;
    }))
  );
});
