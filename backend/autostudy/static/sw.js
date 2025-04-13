const CACHE_NAME = 'autostudy-v1';
const ASSETS = [
  '/',
  '/manifest.json',
  '/static/css/styles.css'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/register')) {
    // Não cachear requisições de registro
    event.respondWith(fetch(event.request));
    return;
  }
  
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});