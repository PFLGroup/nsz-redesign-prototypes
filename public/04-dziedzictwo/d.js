/* Wariant D — ścieżki pamięci „człowiek — miejsce — źródło — pamięć”.
 * Bez JS wszystkie ścieżki są widoczne jedna pod drugą.
 * Z JS: przyciski wyboru (aria-pressed), jedna ścieżka naraz, adres #sciezka-… */
(function () {
  'use strict';
  var wrap = document.querySelector('[data-paths]');
  if (!wrap) return;
  var picker = wrap.querySelector('.path-picker');
  var paths = Array.prototype.slice.call(wrap.querySelectorAll('.path'));
  var buttons = Array.prototype.slice.call(wrap.querySelectorAll('.path-btn'));
  var live = wrap.querySelector('[data-path-live]');
  if (!picker || !paths.length) return;
  picker.hidden = false;

  function show(id, focus) {
    var found = false;
    paths.forEach(function (p) {
      var on = p.id === id;
      if (on) found = true;
      p.hidden = !on;
      p.classList.remove('is-entering');
      if (on && !(window.NSZ && NSZ.reducedMotion && NSZ.reducedMotion())) {
        void p.offsetWidth;
        p.classList.add('is-entering');
      }
    });
    if (!found) return show(paths[0].id, focus);
    buttons.forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-path') === id ? 'true' : 'false');
    });
    var cur = document.getElementById(id);
    if (live && cur) live.textContent = 'Wybrano ścieżkę: ' + cur.querySelector('.path-title').textContent;
    if (focus && cur) cur.querySelector('.path-title').focus();
  }

  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var id = b.getAttribute('data-path');
      show(id, false);
      if (history.replaceState) history.replaceState(null, '', '#' + id);
    });
  });
  // Strzałki przełączają ścieżki, gdy fokus jest na przyciskach.
  picker.addEventListener('keydown', function (e) {
    var i = buttons.indexOf(document.activeElement);
    if (i < 0) return;
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { buttons[(i + 1) % buttons.length].focus(); e.preventDefault(); }
    if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { buttons[(i - 1 + buttons.length) % buttons.length].focus(); e.preventDefault(); }
  });
  var start = location.hash.slice(1);
  show(start && document.getElementById(start) && start.indexOf('sciezka-') === 0 ? start : paths[0].id, false);
})();
