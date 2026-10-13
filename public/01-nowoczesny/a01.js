/* Wariant A — zachowania specyficzne: menu mobilne, indeks tematów (zakładki),
   wyszukiwarka z zakresem. Wspólne zachowania: ../assets/shared/proto.js */
(function () {
  'use strict';

  /* Menu mobilne: przycisk pokazuje/ukrywa główną nawigację (< 960 px). */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('a-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      nav.classList.toggle('is-open', open);
      var label = toggle.querySelector('.label-text');
      if (label) label.textContent = open ? 'Zamknij' : 'Menu';
      if (open) { var f = nav.querySelector('a, button'); if (f) f.focus(); }
    });
    nav.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { toggle.click(); toggle.focus(); }
    });
  }

  /* Wyszukiwarka z zakresem: przekazuje ?q= i ?kat= do listy materiałów.
     Słuchacz w fazie przechwytywania uruchamia się przed ogólnym z proto.js. */
  document.querySelectorAll('form.search-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      var q = (form.querySelector('input[name="q"]') || {}).value || '';
      var kat = form.querySelector('input[name="kat"]:checked');
      var url = form.getAttribute('action') + '?q=' + encodeURIComponent(q.trim());
      if (kat && kat.value !== 'all') url += '&kat=' + encodeURIComponent(kat.value);
      location.href = url;
    }, true);
  });

  /* Indeks tematów: wzorzec zakładek (strzałki, Home/End). Bez JS — wszystkie panele widoczne. */
  document.querySelectorAll('[data-topic-index]').forEach(function (box) {
    var tabs = Array.prototype.slice.call(box.querySelectorAll('.ti-tab'));
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute('aria-controls')); });
    var list = box.querySelector('.ti-tabs');
    if (list) {
      list.setAttribute('role', 'tablist');
      list.setAttribute('aria-orientation', 'vertical');
      list.setAttribute('aria-label', 'Tematy');
      Array.prototype.forEach.call(list.children, function (li) { li.setAttribute('role', 'presentation'); });
    }
    tabs.forEach(function (t, k) {
      t.setAttribute('role', 'tab');
      t.id = t.id || 'ti-tab-' + k;
      if (panels[k]) {
        panels[k].setAttribute('role', 'tabpanel');
        panels[k].setAttribute('aria-labelledby', t.id);
        panels[k].tabIndex = 0;
      }
    });
    box.classList.remove('no-js-ti');
    function select(i, focus) {
      tabs.forEach(function (t, k) {
        var on = k === i;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        if (panels[k]) panels[k].hidden = !on;
      });
      if (focus) tabs[i].focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i, false); });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') n = (i + 1) % tabs.length;
        if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') n = (i - 1 + tabs.length) % tabs.length;
        if (e.key === 'Home') n = 0;
        if (e.key === 'End') n = tabs.length - 1;
        if (n !== null) { e.preventDefault(); select(n, true); }
      });
    });
    var start = tabs.findIndex(function (t) { return location.hash && t.getAttribute('aria-controls') === location.hash.slice(1); });
    select(start > -1 ? start : 0, false);
  });
})();
