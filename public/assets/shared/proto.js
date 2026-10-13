/*
 * Wspólne helpery prototypów NSZ (bez zależności, ~ES2018).
 * Zawiera WYŁĄCZNIE logikę zachowań: menu, wyszukiwanie, filtry, galerię,
 * przełącznik ograniczenia ruchu, pasek postępu i baner prototypu.
 * Każdy wariant ma własny HTML i CSS — ten plik nie narzuca układu.
 * Treść stron jest w HTML; skrypt tylko ją rozszerza (progressive enhancement).
 */
(function () {
  'use strict';
  var NSZ = (window.NSZ = window.NSZ || {});
  var root = document.documentElement;
  root.classList.add('js');

  /* ---------- Ograniczenie ruchu ---------- */
  var MOTION_KEY = 'nsz-proto-reduce-motion';
  function storedMotion() {
    try { return localStorage.getItem(MOTION_KEY); } catch (e) { return null; }
  }
  function applyMotion(reduce) {
    root.classList.toggle('reduce-motion', !!reduce);
    document.querySelectorAll('[data-motion-toggle]').forEach(function (b) {
      b.setAttribute('aria-pressed', reduce ? 'true' : 'false');
      var label = b.querySelector('[data-motion-label]');
      if (label) label.textContent = reduce ? 'Animacje: ograniczone' : 'Animacje: włączone';
    });
  }
  NSZ.reducedMotion = function () { return root.classList.contains('reduce-motion'); };
  var sys = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var st = storedMotion();
  applyMotion(st === null ? sys : st === '1');
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-motion-toggle]');
    if (!b) return;
    var next = !NSZ.reducedMotion();
    applyMotion(next);
    try { localStorage.setItem(MOTION_KEY, next ? '1' : '0'); } catch (err) {}
  });

  /* ---------- Baner prototypu (dopisywany, jeśli strona go nie ma) ---------- */
  function ensureBanner() {
    if (document.querySelector('.proto-banner')) return;
    var d = document.createElement('div');
    d.className = 'proto-banner';
    d.setAttribute('role', 'note');
    d.innerHTML = '<strong>Prototyp koncepcyjny — nie jest oficjalnym serwisem.</strong> ' +
      'Treści demonstracyjne; linki źródłowe prowadzą do nsz.com.pl.';
    document.body.insertBefore(d, document.body.firstChild);
  }

  /* ---------- Menu / panele rozwijane (przycisk aria-controls) ---------- */
  function initDisclosures() {
    document.querySelectorAll('[data-disclosure]').forEach(function (btn) {
      var id = btn.getAttribute('aria-controls');
      var panel = id && document.getElementById(id);
      if (!panel) return;
      var modal = btn.hasAttribute('data-modal');
      btn.setAttribute('aria-expanded', 'false');
      panel.hidden = true;
      function close(returnFocus) {
        btn.setAttribute('aria-expanded', 'false');
        panel.hidden = true;
        root.classList.remove('has-open-' + id);
        if (returnFocus) btn.focus();
      }
      function open() {
        btn.setAttribute('aria-expanded', 'true');
        panel.hidden = false;
        root.classList.add('has-open-' + id);
        var f = panel.querySelector('input, a, button');
        if (modal && f) f.focus();
      }
      btn.addEventListener('click', function () {
        btn.getAttribute('aria-expanded') === 'true' ? close(false) : open();
      });
      document.addEventListener('keydown', function (e) {
        if (e.key !== 'Escape' || btn.getAttribute('aria-expanded') !== 'true') return;
        if (panel.contains(document.activeElement) || btn === document.activeElement) close(true);
      });
      panel.querySelectorAll('[data-close]').forEach(function (c) {
        c.addEventListener('click', function () { close(true); });
      });
      document.addEventListener('click', function (e) {
        if (btn.getAttribute('aria-expanded') !== 'true') return;
        if (panel.contains(e.target) || btn.contains(e.target)) return;
        if (panel.hasAttribute('data-keep-open')) return;
        close(false);
      });
    });
  }

  /* ---------- Filtry + wyszukiwarka na liście [data-filter-list] ----------
   * Elementy listy: [data-item] z data-cat="a b" i data-text (opcjonalnie).
   * Kontrolki: [data-filter="kat"] (przyciski aria-pressed), input[data-search],
   * [data-clear-filters], [data-empty] (stan pusty), [data-count] (aria-live).
   */
  function norm(s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ł/g, 'l');
  }
  /* Dopasowanie odporne na odmianę: każde słowo zapytania przycinane do rdzenia
   * (bez 1–2 końcowych liter), więc „Kamesznica” znajdzie „Kamesznicy”. */
  function stems(q) {
    return norm(q).split(/[^a-z0-9]+/).filter(Boolean).map(function (w) {
      return w.length > 6 ? w.slice(0, w.length - 2) : w.length > 4 ? w.slice(0, w.length - 1) : w;
    });
  }
  function matches(text, q) {
    var t = norm(text);
    return stems(q).every(function (st) { return t.indexOf(st) > -1; });
  }
  NSZ.matches = matches;

  function initFilterLists() {
    document.querySelectorAll('[data-filter-scope]').forEach(function (scope) {
      var items = Array.prototype.slice.call(scope.querySelectorAll('[data-item]'));
      var buttons = scope.querySelectorAll('[data-filter]');
      var search = scope.querySelector('input[data-search]');
      var empty = scope.querySelector('[data-empty]');
      var count = scope.querySelector('[data-count]');
      var active = 'all';
      var params = new URLSearchParams(location.search);
      if (params.get('kat')) active = params.get('kat');
      if (params.get('q') && search) search.value = params.get('q');

      function update() {
        var q = search ? search.value.trim() : '';
        var n = 0;
        items.forEach(function (it) {
          var cats = (it.getAttribute('data-cat') || '').split(/\s+/);
          var text = it.getAttribute('data-text') || it.textContent;
          var ok = (active === 'all' || cats.indexOf(active) > -1) && (!q || matches(text, q));
          it.hidden = !ok;
          if (ok) n++;
        });
        buttons.forEach(function (b) {
          b.setAttribute('aria-pressed', b.getAttribute('data-filter') === active ? 'true' : 'false');
        });
        if (empty) empty.hidden = n !== 0;
        if (count) count.textContent = n === 1 ? 'Znaleziono 1 materiał' :
          'Znaleziono ' + n + (n > 1 && n < 5 ? ' materiały' : ' materiałów');
      }
      buttons.forEach(function (b) {
        b.addEventListener('click', function () { active = b.getAttribute('data-filter'); update(); });
      });
      if (search) {
        search.addEventListener('input', update);
        var form = search.closest('form');
        if (form) form.addEventListener('submit', function (e) { e.preventDefault(); update(); });
      }
      scope.querySelectorAll('[data-clear-filters]').forEach(function (c) {
        c.addEventListener('click', function () {
          active = 'all';
          if (search) search.value = '';
          update();
          if (search) search.focus();
        });
      });
      update();
    });
  }

  /* ---------- Szybka wyszukiwarka globalna [data-quick-search] ----------
   * input + lista wyników <ul data-results>; dane z window.NSZ_CONTENT.
   * Odnośnik do wyniku: atrybut data-href-base + slug lub URL źródła.
   */
  function initQuickSearch() {
    var data = (window.NSZ_CONTENT && window.NSZ_CONTENT.items) || [];
    document.querySelectorAll('[data-quick-search]').forEach(function (wrap) {
      var input = wrap.querySelector('input');
      var out = wrap.querySelector('[data-results]');
      var status = wrap.querySelector('[data-results-status]');
      var listHref = wrap.getAttribute('data-list-href') || 'aktualnosci.html';
      if (!input || !out) return;
      function render() {
        var q = input.value.trim();
        out.innerHTML = '';
        if (q.length < 2) { if (status) status.textContent = ''; return; }
        var hits = data.filter(function (it) {
          return matches([it.title, it.summary, it.category, it.place || ''].join(' '), q);
        }).slice(0, 6);
        hits.forEach(function (it) {
          var li = document.createElement('li');
          var a = document.createElement('a');
          a.href = listHref + '?q=' + encodeURIComponent(input.value.trim());
          a.textContent = it.title;
          var s = document.createElement('span');
          s.textContent = ' — ' + (it.category || '') + (it.date ? ', ' + NSZ.formatDate(it.date) : '');
          li.appendChild(a); li.appendChild(s);
          out.appendChild(li);
        });
        if (status) status.textContent = hits.length ? 'Wyniki: ' + hits.length :
          'Brak wyników dla „' + input.value.trim() + '”. Spróbuj innego słowa.';
      }
      input.addEventListener('input', render);
      var form = input.closest('form');
      if (form) form.addEventListener('submit', function (e) {
        e.preventDefault();
        location.href = listHref + '?q=' + encodeURIComponent(input.value.trim());
      });
    });
  }

  NSZ.formatDate = function (iso) {
    var m = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca',
      'sierpnia', 'września', 'października', 'listopada', 'grudnia'];
    var d = new Date(iso);
    if (isNaN(d)) return iso;
    return d.getDate() + ' ' + m[d.getMonth()] + ' ' + d.getFullYear();
  };

  /* ---------- Galeria / slider [data-gallery] ----------
   * Struktura: [data-gallery] > [data-track] > [data-slide]*, przyciski
   * [data-prev]/[data-next], opcjonalnie [data-dots], [data-status] (aria-live).
   * Bez autoodtwarzania. Strzałki klawiatury, przeciąganie jako dodatek.
   */
  function initGalleries() {
    document.querySelectorAll('[data-gallery]').forEach(function (g) {
      var slides = Array.prototype.slice.call(g.querySelectorAll('[data-slide]'));
      if (!slides.length) return;
      var i = 0;
      var status = g.querySelector('[data-status]');
      var dots = g.querySelector('[data-dots]');
      g.setAttribute('aria-roledescription', 'galeria');
      slides.forEach(function (s, k) {
        s.setAttribute('role', 'group');
        s.setAttribute('aria-roledescription', 'slajd');
        s.setAttribute('aria-label', (k + 1) + ' z ' + slides.length);
      });
      if (dots) {
        slides.forEach(function (s, k) {
          var b = document.createElement('button');
          b.type = 'button';
          b.className = 'gallery-dot';
          b.setAttribute('aria-label', 'Pokaż slajd ' + (k + 1));
          b.addEventListener('click', function () { go(k); });
          dots.appendChild(b);
        });
      }
      function go(n) {
        i = (n + slides.length) % slides.length;
        slides.forEach(function (s, k) {
          var on = k === i;
          s.classList.toggle('is-active', on);
          s.hidden = !on;
        });
        if (dots) Array.prototype.forEach.call(dots.children, function (d, k) {
          d.setAttribute('aria-current', k === i ? 'true' : 'false');
        });
        if (status) status.textContent = 'Slajd ' + (i + 1) + ' z ' + slides.length;
        g.setAttribute('data-index', i);
      }
      var prev = g.querySelector('[data-prev]');
      var next = g.querySelector('[data-next]');
      if (prev) prev.addEventListener('click', function () { go(i - 1); });
      if (next) next.addEventListener('click', function () { go(i + 1); });
      g.addEventListener('keydown', function (e) {
        if (e.target.closest('input, textarea')) return;
        if (e.key === 'ArrowLeft') { go(i - 1); e.preventDefault(); }
        if (e.key === 'ArrowRight') { go(i + 1); e.preventDefault(); }
      });
      var x0 = null;
      g.addEventListener('pointerdown', function (e) { x0 = e.clientX; });
      g.addEventListener('pointerup', function (e) {
        if (x0 === null) return;
        var dx = e.clientX - x0; x0 = null;
        if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1));
      });
      go(0);
    });
  }

  /* ---------- Pasek postępu czytania [data-reading-progress] ---------- */
  function initProgress() {
    var bar = document.querySelector('[data-reading-progress]');
    var art = document.querySelector('[data-article-body]');
    if (!bar || !art) return;
    function upd() {
      var r = art.getBoundingClientRect();
      var total = r.height - window.innerHeight;
      var p = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : 1;
      bar.style.transform = 'scaleX(' + p + ')';
      bar.setAttribute('aria-valuenow', Math.round(p * 100));
    }
    window.addEventListener('scroll', upd, { passive: true });
    window.addEventListener('resize', upd);
    upd();
  }

  /* ---------- Spis treści: podświetlenie bieżącej sekcji ---------- */
  function initToc() {
    var links = document.querySelectorAll('[data-toc] a[href^="#"]');
    if (!links.length || !('IntersectionObserver' in window)) return;
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.removeAttribute('aria-current'); });
        var a = map[en.target.id];
        if (a) a.setAttribute('aria-current', 'location');
      });
    }, { rootMargin: '0px 0px -70% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  }

  /* ---------- Formularze demonstracyjne: nie wysyłają danych ---------- */
  function initDemoForms() {
    document.querySelectorAll('form[data-demo-form]').forEach(function (f) {
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var msg = f.querySelector('[data-demo-msg]');
        if (msg) msg.textContent = 'To tylko prototyp — formularz nie wysyła ani nie zapisuje żadnych danych.';
      });
    });
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    ensureBanner();
    initDisclosures();
    initFilterLists();
    initQuickSearch();
    initGalleries();
    initProgress();
    initToc();
    initDemoForms();
    applyMotion(NSZ.reducedMotion());
  });
})();
