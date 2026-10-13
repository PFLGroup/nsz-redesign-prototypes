/*
 * Wariant B „Żywe Archiwum” — eksplorator czas / miejsca / ludzie / dokumenty.
 * Dane czytane z widoku listy w HTML (jedno źródło prawdy, działa bez JS).
 * Skrypt dodaje: zakładki perspektyw, oś lat, kartę punktu z powiązaniami
 * i przełącznik „Oś i powiązania / Lista”.
 */
(function () {
  'use strict';
  var root = document.querySelector('[data-explorer]');
  if (!root) return;
  var stage = root.querySelector('[data-stage]');
  var lists = root.querySelector('[data-lists]');
  var hint = root.querySelector('[data-explorer-hint]');
  var switcher = root.querySelector('[data-view-switch]');
  var facetLinks = Array.prototype.slice.call(document.querySelectorAll('[data-facets] a[data-facet]'));
  var FACET_NAMES = { czas: 'Czas', miejsca: 'Miejsca', ludzie: 'Ludzie', dokumenty: 'Dokumenty' };
  var narrow = window.matchMedia('(max-width: 760px)');

  /* ---------- Dane z HTML ---------- */
  var nodes = {};
  var order = [];
  root.querySelectorAll('li.node').forEach(function (li) {
    var id = li.getAttribute('data-id');
    nodes[id] = {
      id: id,
      el: li,
      facet: li.getAttribute('data-facet'),
      year: li.getAttribute('data-year'),
      status: li.getAttribute('data-status'),
      tough: li.classList.contains('is-tough'),
      short: li.getAttribute('data-short'),
      sub: li.getAttribute('data-sub'),
      title: li.querySelector('.node-title').textContent,
      links: (li.getAttribute('data-links') || '').split(/\s+/).filter(Boolean)
    };
    order.push(id);
  });
  // powiązania symetryczne
  order.forEach(function (id) {
    nodes[id].links.forEach(function (l) {
      if (nodes[l] && nodes[l].links.indexOf(id) < 0) nodes[l].links.push(id);
    });
  });

  var state = { facet: 'czas', view: 'map', selected: 'n/a' };

  /* ---------- Zakładki perspektyw (z linków-kotwic) ---------- */
  var tablist = document.querySelector('[data-facets]');
  tablist.setAttribute('role', 'tablist');
  tablist.setAttribute('aria-label', 'Perspektywa eksploracji');
  facetLinks.forEach(function (a) {
    a.parentNode.setAttribute('role', 'presentation');
    a.setAttribute('role', 'tab');
    a.setAttribute('aria-controls', 'explorer-panel');
    a.id = 'tab-' + a.getAttribute('data-facet');
    a.addEventListener('click', function (ev) {
      ev.preventDefault();
      setFacet(a.getAttribute('data-facet'), true);
    });
    a.addEventListener('keydown', function (ev) {
      var i = facetLinks.indexOf(a);
      var n = null;
      if (ev.key === 'ArrowRight' || ev.key === 'ArrowDown') n = (i + 1) % facetLinks.length;
      if (ev.key === 'ArrowLeft' || ev.key === 'ArrowUp') n = (i - 1 + facetLinks.length) % facetLinks.length;
      if (ev.key === 'Home') n = 0;
      if (ev.key === 'End') n = facetLinks.length - 1;
      if (ev.key === ' ') { ev.preventDefault(); a.click(); return; }
      if (n === null) return;
      ev.preventDefault();
      facetLinks[n].focus();
      setFacet(facetLinks[n].getAttribute('data-facet'), true);
    });
  });
  root.id = 'explorer-panel';
  root.setAttribute('role', 'tabpanel');

  /* ---------- Szkielet sceny ---------- */
  stage.innerHTML =
    '<div class="stage-canvas" data-canvas></div>' +
    '<section class="card" data-card aria-live="polite" aria-labelledby="card-title">' +
    '<div class="card-main" data-card-main></div>' +
    '<div class="card-rel"><h2 class="card-rel-title">Powiązania</h2><div data-card-rel></div></div>' +
    '<p class="card-back"><button type="button" class="btn btn-ghost" data-back>Wróć do wyboru punktów</button></p>' +
    '</section>';
  var canvas = stage.querySelector('[data-canvas]');
  var cardMain = stage.querySelector('[data-card-main]');
  var cardRel = stage.querySelector('[data-card-rel]');
  stage.querySelector('[data-back]').addEventListener('click', function () {
    var b = canvas.querySelector('[data-node="' + state.selected + '"]');
    if (b) b.focus();
  });

  function nodeButton(n) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'nbtn st-' + n.status + (n.tough ? ' is-tough' : '');
    b.setAttribute('data-node', n.id);
    b.setAttribute('aria-pressed', 'false');
    var label = document.createElement('span');
    label.className = 'nb-label';
    if (n.facet === 'czas') {
      var parts = n.short.split(' · ');
      label.innerHTML = '<span class="nb-date"></span><span class="nb-text"></span>';
      label.firstChild.textContent = parts[0];
      label.lastChild.textContent = parts.slice(1).join(' · ') || n.short;
    } else {
      label.innerHTML = '<span class="nb-text"></span><span class="nb-sub"></span>';
      label.firstChild.textContent = n.title;
      label.lastChild.textContent = n.sub + ' · powiązań: ' + n.links.length;
    }
    b.appendChild(label);
    if (n.tough) {
      var t = document.createElement('span');
      t.className = 'sr-only';
      t.textContent = ' (trudny wątek)';
      b.appendChild(t);
    }
    if (n.status === 'ps') {
      var s = document.createElement('span');
      s.className = 'sr-only';
      s.textContent = ' (ocena sporna)';
      b.appendChild(s);
    }
    b.addEventListener('click', function () { select(n.id, false); });
    return b;
  }

  function renderCanvas() {
    canvas.innerHTML = '';
    canvas.className = 'stage-canvas canvas-' + state.facet;
    var ids = order.filter(function (id) { return nodes[id].facet === state.facet; });
    if (state.facet === 'czas') {
      var years = [];
      ids.forEach(function (id) {
        var y = nodes[id].year;
        if (years.indexOf(y) < 0) years.push(y);
      });
      var ol = document.createElement('ol');
      ol.className = 'years';
      ol.setAttribute('aria-label', 'Oś czasu, lata od 1942 do 2026');
      years.forEach(function (y, k) {
        if (k > 0 && +y - +years[k - 1] > 5) {
          var gap = document.createElement('li');
          gap.className = 'year-gap';
          gap.innerHTML = '<span aria-hidden="true">⋯</span><span class="sr-only">przerwa w skali: lata </span>' +
            (+years[k - 1] + 1) + '–' + (+y - 1);
          ol.appendChild(gap);
        }
        var li = document.createElement('li');
        li.className = 'year';
        var h = document.createElement('p');
        h.className = 'year-label';
        h.textContent = y;
        li.appendChild(h);
        var ul = document.createElement('ul');
        ul.className = 'year-nodes';
        ids.filter(function (id) { return nodes[id].year === y; }).forEach(function (id) {
          var item = document.createElement('li');
          item.appendChild(nodeButton(nodes[id]));
          ul.appendChild(item);
        });
        li.appendChild(ul);
        ol.appendChild(li);
      });
      canvas.appendChild(ol);
    } else {
      var grid = document.createElement('ul');
      grid.className = 'node-grid';
      grid.setAttribute('aria-label', FACET_NAMES[state.facet]);
      ids.forEach(function (id) {
        var li = document.createElement('li');
        li.appendChild(nodeButton(nodes[id]));
        grid.appendChild(li);
      });
      canvas.appendChild(grid);
    }
    markSelected();
  }

  function markSelected() {
    canvas.querySelectorAll('[data-node]').forEach(function (b) {
      var on = b.getAttribute('data-node') === state.selected;
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.classList.toggle('is-linked', !on && nodes[state.selected] &&
        nodes[state.selected].links.indexOf(b.getAttribute('data-node')) > -1);
    });
  }

  function renderCard() {
    var n = nodes[state.selected];
    if (!n) return;
    var clone = n.el.cloneNode(true);
    var meta = clone.querySelector('.node-meta');
    var title = clone.querySelector('.node-title');
    var h = document.createElement('h2');
    h.id = 'card-title';
    h.tabIndex = -1;
    h.textContent = title.textContent;
    var facet = document.createElement('p');
    facet.className = 'card-facet';
    facet.textContent = FACET_NAMES[n.facet];
    cardMain.innerHTML = '';
    cardMain.appendChild(facet);
    cardMain.appendChild(meta);
    cardMain.appendChild(h);
    cardMain.appendChild(clone.querySelector('.node-desc'));
    cardMain.appendChild(clone.querySelector('.node-src'));
    var perma = document.createElement('p');
    perma.className = 'card-perma';
    perma.innerHTML = '<a href="#n-' + n.id + '">Stały odnośnik do punktu</a>';
    cardMain.appendChild(perma);

    cardRel.innerHTML = '';
    if (!n.links.length) {
      cardRel.innerHTML = '<p class="muted">Brak powiązań w zbiorze demonstracyjnym.</p>';
    }
    ['czas', 'miejsca', 'ludzie', 'dokumenty'].forEach(function (f) {
      var rel = n.links.filter(function (id) { return nodes[id].facet === f; });
      if (!rel.length) return;
      var p = document.createElement('p');
      p.className = 'rel-facet';
      p.textContent = FACET_NAMES[f];
      var ul = document.createElement('ul');
      ul.className = 'rel-list';
      rel.forEach(function (id) {
        var li = document.createElement('li');
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'chip chip-btn';
        b.textContent = nodes[id].facet === 'czas' ? nodes[id].short : nodes[id].title;
        b.addEventListener('click', function () { select(id, true); });
        li.appendChild(b);
        ul.appendChild(li);
      });
      cardRel.appendChild(p);
      cardRel.appendChild(ul);
    });
    stage.querySelector('[data-card]').classList.remove('is-fresh');
    void stage.offsetWidth;
    stage.querySelector('[data-card]').classList.add('is-fresh');
  }

  /* ---------- Akcje ---------- */
  function setFacet(f, keepSelection) {
    state.facet = f;
    facetLinks.forEach(function (a) {
      var on = a.getAttribute('data-facet') === f;
      a.setAttribute('aria-selected', on ? 'true' : 'false');
      a.tabIndex = on ? 0 : -1;
    });
    root.setAttribute('aria-labelledby', 'tab-' + f);
    if (!keepSelection || !nodes[state.selected] || nodes[state.selected].facet !== f) {
      var first = order.filter(function (id) { return nodes[id].facet === f; })[0];
      state.selected = first;
      renderCard();
    }
    renderCanvas();
    renderLists();
    updateHint();
  }

  function select(id, moveFocus) {
    if (!nodes[id]) return;
    var changedFacet = nodes[id].facet !== state.facet;
    state.selected = id;
    if (changedFacet) {
      state.facet = nodes[id].facet;
      setFacet(state.facet, true);
    } else {
      markSelected();
    }
    renderCard();
    try { history.replaceState(null, '', '#n-' + id); } catch (e) {}
    if (state.view !== 'map') return;
    if (narrow.matches) {
      var h = stage.querySelector('#card-title');
      if (h) h.focus();
    } else if (moveFocus) {
      var b = canvas.querySelector('[data-node="' + id + '"]');
      if (b) b.focus();
    }
  }

  function renderLists() {
    lists.querySelectorAll('[data-group]').forEach(function (g) {
      g.hidden = state.view === 'list' ? g.getAttribute('data-group') !== state.facet : true;
    });
  }

  function updateHint() {
    var count = order.filter(function (id) { return nodes[id].facet === state.facet; }).length;
    hint.textContent = state.view === 'map'
      ? FACET_NAMES[state.facet] + ': ' + count + ' punktów. Wybierz punkt, aby zobaczyć kartę i powiązania.'
      : FACET_NAMES[state.facet] + ': ' + count + ' punktów w widoku listy, ze źródłami.';
  }

  function setView(v) {
    state.view = v;
    switcher.querySelectorAll('[data-view]').forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-view') === v ? 'true' : 'false');
    });
    stage.hidden = v !== 'map';
    renderLists();
    updateHint();
  }
  switcher.hidden = false;
  switcher.querySelectorAll('[data-view]').forEach(function (b) {
    b.addEventListener('click', function () { setView(b.getAttribute('data-view')); });
  });

  function fromHash() {
    var m = /^#n-(.+)$/.exec(location.hash);
    if (m && nodes[m[1]]) {
      setView('map');
      select(m[1], false);
      var target = document.getElementById('eksplorator');
      if (target) target.scrollIntoView();
      var b = canvas.querySelector('[data-node="' + m[1] + '"]');
      if (b) b.focus({ preventScroll: true });
      return true;
    }
    var f = /^#lista-(\w+)$/.exec(location.hash);
    if (f && FACET_NAMES[f[1]]) { setFacet(f[1], false); setView('list'); return true; }
    return false;
  }

  root.classList.add('is-enhanced');
  setView('map');
  setFacet('czas', false);
  fromHash();
  window.addEventListener('hashchange', fromHash);
})();
