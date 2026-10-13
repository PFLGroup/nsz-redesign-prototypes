/* Wariant E — interakcje własne: warstwy montażu i pułapka fokusu indeksu.
 * Bez JS wszystkie warstwy są widoczne jedna pod drugą. */
(function () {
  'use strict';

  /* Warstwy montażu: przyciski aria-expanded + aria-controls; otwarta jedna naraz. */
  document.querySelectorAll('[data-layers]').forEach(function (box) {
    var btns = Array.prototype.slice.call(box.querySelectorAll('[data-layer-btn]'));
    function show(target, focusPanel) {
      btns.forEach(function (b) {
        var on = b === target;
        var p = document.getElementById(b.getAttribute('aria-controls'));
        b.setAttribute('aria-expanded', on ? 'true' : 'false');
        if (p) p.hidden = !on;
        if (on && p && focusPanel) p.focus();
      });
    }
    btns.forEach(function (b, i) {
      b.addEventListener('click', function () {
        if (b.getAttribute('aria-expanded') === 'true') return;
        show(b, false);
      });
      b.addEventListener('keydown', function (e) {
        var k = e.key, j = null;
        if (k === 'ArrowRight') j = (i + 1) % btns.length;
        if (k === 'ArrowLeft') j = (i - 1 + btns.length) % btns.length;
        if (k === 'Home') j = 0;
        if (k === 'End') j = btns.length - 1;
        if (j !== null) { e.preventDefault(); btns[j].focus(); }
      });
    });
    var start = btns.filter(function (b) { return b.hasAttribute('data-default'); })[0] || btns[0];
    show(start, false);
  });

  /* Pułapka fokusu w wysuwanym indeksie (panel #indeks). */
  var panel = document.getElementById('indeks');
  if (panel) {
    panel.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || panel.hidden) return;
      var f = panel.querySelectorAll('a[href], button:not([disabled]), input:not([disabled])');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    /* Kliknięcie w link kotwicy wewnątrz indeksu zamyka panel. */
    panel.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#"], a[href*="index.html#"]');
      if (!a) return;
      var c = panel.querySelector('[data-close]');
      if (c) c.click();
    });
  }
})();
