/* Wariant C — moduł „Kalendarium”: najbliższa rocznica z osi czasu.
 * Dane wyłącznie z zweryfikowanej osi czasu projektu (work/history-for-design.md).
 * Bez JS strona pokazuje statyczny wpis (9 listopada) — skrypt tylko go aktualizuje.
 */
(function () {
  'use strict';
  var M = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca',
    'sierpnia', 'września', 'października', 'listopada', 'grudnia'];
  var IPN = 'https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html';
  var DATES = [
    { m: 2, d: 3, y: 2011, t: 'Sejm uchwala ustawę o Narodowym Dniu Pamięci „Żołnierzy Wyklętych” (Dz.U. 2011 poz. 160).', s: 'Dziennik Ustaw', u: 'https://eli.gov.pl/eli/DU/2011/160/ogl' },
    { m: 2, d: 15, y: 1947, t: 'Aresztowanie ppłk. Stanisława Kasznicy, ostatniego komendanta NSZ-ZJ.', s: 'IPN', u: IPN },
    { m: 3, d: 7, y: 1944, t: 'Umowa scaleniowa NSZ z AK; jej skutkiem jest rozłam na NSZ-AK i NSZ-ZJ.', s: 'R. Wnuk, „Dzieje Najnowsze” 2021', u: 'https://doi.org/10.12775/DN.2021.1.05' },
    { m: 5, d: 3, y: 1946, t: 'Przemarsz zgrupowania kpt. Henryka Flamego „Bartka” przez Wisłę.', s: 'dzieje.pl', u: 'https://dzieje.pl/node/99089' },
    { m: 5, d: 5, y: 1945, t: 'Brygada Świętokrzyska uwalnia więźniarki obozu w Holiszowie (liczby w źródłach są rozbieżne).', s: 'IPN', u: IPN },
    { m: 5, d: 12, y: 1948, t: 'Egzekucja ppłk. Stanisława Kasznicy; wyrok unieważniono w 1992 r.', s: 'IPN', u: IPN },
    { m: 8, d: 1, y: 1943, t: 'Płk Tadeusz Kurcyusz obejmuje dowództwo NSZ.', s: 'R. Wnuk, „Dzieje Najnowsze” 2021', u: 'https://doi.org/10.12775/DN.2021.1.05' },
    { m: 8, d: 11, y: 1944, t: 'Utworzenie Brygady Świętokrzyskiej NSZ.', s: 'IPN', u: IPN },
    { m: 9, d: 20, y: 1942, t: 'Rozkaz nr 1/42 płk. Ignacego Oziewicza — powstanie Narodowych Sił Zbrojnych.', s: 'IPN', u: IPN },
    { m: 11, d: 9, y: 2012, t: 'Uchwała Sejmu RP w 70. rocznicę powstania NSZ (M.P. 2012 poz. 890).', s: 'Monitor Polski', u: 'https://eli.gov.pl/eli/MP/2012/890/ogl/pol/pdf' },
    { m: 12, d: 1, y: 1947, t: 'Śmierć kpt. Henryka Flamego „Bartka” w Zabrzegu.', s: 'dzieje.pl', u: 'https://dzieje.pl/node/99089' }
  ];

  function nearest(now) {
    var y = now.getFullYear();
    var today = new Date(y, now.getMonth(), now.getDate());
    var best = null, bestDiff = Infinity;
    DATES.forEach(function (e) {
      var dt = new Date(y, e.m - 1, e.d);
      if (dt < today) dt = new Date(y + 1, e.m - 1, e.d);
      var diff = Math.round((dt - today) / 864e5);
      if (diff < bestDiff) { bestDiff = diff; best = e; }
    });
    return { e: best, days: bestDiff };
  }

  function render() {
    var box = document.querySelector('[data-kalendarium]');
    if (!box) return;
    var r = nearest(new Date());
    var e = r.e;
    var label = r.days === 0 ? 'Tego dnia' : 'Najbliższa rocznica — za ' + r.days + (r.days === 1 ? ' dzień' : ' dni');
    box.querySelector('[data-kal-label]').textContent = label;
    box.querySelector('[data-kal-dm]').textContent = e.d;
    box.querySelector('[data-kal-m]').innerHTML = M[e.m - 1] + '<br>' + e.y + ' r.';
    box.querySelector('[data-kal-text]').textContent = e.t;
    var src = box.querySelector('[data-kal-src] a');
    src.textContent = e.s;
    src.href = e.u;
  }

  if (document.readyState !== 'loading') render();
  else document.addEventListener('DOMContentLoaded', render);
})();
