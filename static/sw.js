importScripts('/static/js/cache-polyfill.js');

self.addEventListener('install', function(e) {
 e.waitUntil(
   caches.open('WRU').then(function(cache) {
     return cache.addAll([
       '/Upload',
       '/NewUser',
       '/AdminSearch',
       '/EmployeeSearch',
       '/AddEvent',
       '/DeleteEvent',
       '/Login',
       '/email',
       '/Pin',
       '/static/css/bootstrap.min.css',
       '/static/css/style.css',
       '/static/css/addEvent.css',
       '/static/css/navbar.css',
       '/static/css/slider.css',
       '/static/js/bootstrap.min.js',
       '/static/js/NewUser.js',
       '/static/js/slider.js',
       '/static/js/eventvalidation.js',
       '/static/js/submit.js',
       '/static/images/Welsh_Rugby_Union_logo.png'
     ]);
   })
 );
});

self.addEventListener('fetch', function(event) {
  console.log(event.request.url);
  event.respondWith(
    fetch(event.request).catch(function()
  { return caches.match(event.request)
  })
    // caches.match(event.request).then(function(response) {
    //   return response || fetch(event.request);
    // })
  );
});
