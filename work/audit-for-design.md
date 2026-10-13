# Audyt → wytyczne dla projektantów (skrót)

**Menu obecne (www.nsz.com.pl, 13.10.2026):** O NSZ · Związek Żołnierzy NSZ ▾ (Władze naczelne, Okręgi, Patronaty, Spis cyklicznych inicjatyw) · Aktualności · Biblioteka ▾ (biuletyn „Szczerbiec” PDF, Kalendarium, Artykuły i opracowania, Dokumenty, Wspomnienia, Propaganda komunistyczna, Filmy, Życiorysy, Wykazy odznaczonych, Wiersze i pieśni, Polecane witryny) · Wydawnictwa · Cyfrowe Archiwum ZŻNSZ (osobny WP) · Grafiki · Sekcja Proobronna · Kontakt · Akademia Cyfrowa · Wspieram.

**Proponowana mapa treści (max 6–7 pozycji głównych):**
1. **Aktualności** — relacje, zapowiedzi, komunikaty (filtr: relacja / zapowiedź / komunikat / wspomnienie pośmiertne).
2. **Historia** — wprowadzenie „NSZ w skrócie”, oś czasu, Artykuły i opracowania, Kalendarium dnia, Propaganda komunistyczna (jako temat).
3. **Ludzie** — Życiorysy (200), Wspomnienia, Wykazy odznaczonych.
4. **Archiwum** — Dokumenty, Cyfrowe Archiwum (link zewn. z opisem), stara witryna, Do pobrania/Grafiki.
5. **Multimedia** — Filmy, galerie, Wiersze i pieśni, Wydawnictwa/biuletyn.
6. **Wydarzenia** — kalendarz uroczystości (data, miejsce), Inicjatywy cykliczne, Patronaty.
7. **Związek** — O nas, Władze, Okręgi, Akademia Cyfrowa, Sekcja Proobronna, Kontakt. Przycisk **Wesprzyj** jako akcja w nagłówku, nie pozycja menu.

**Potwierdzona paleta (z CSS):** czerwień `#ad2727` (menu, akcenty), bordo `#530b0b`, granat `#091635`, prawie czarny `#05131e`/`#0b1626` (pasek górny, stopka), zieleń przycisków `#2b5c13` (do wycofania — niespójna), czerwień darowizn `#db3941`. Rdzeń: **granat + czerwień + srebro emblematu + biel**. Fonty obecne: Roboto, Roboto Condensed, Titillium Web.

**Zachować:** emblemat ZŻNSZ bez przekształceń (w prototypach — oznaczony placeholder, prawa niepotwierdzone); kalendarium „tego dnia” (jako HTML, nie grafika); fasetowe filtry wzorowane na Cyfrowym Archiwum (formacja, rodzaj dokumentu, data, województwo); dane organizacyjne (KRS, adres, e-mail redakcji) jako tekst; link pomijający.

**Unikać (z audytu):** tekstu w banerach, sliderów z autoodtwarzaniem, kalendarza-widżetu, mieszania aktualności z historią w jednej liście bez etykiety typu, ukrytego autorstwa, justowania.

**Wymagane pola w kartach/artykułach:** typ materiału, data publikacji (i data wydarzenia, jeśli inna), autor lub „brak podpisu autora”, pierwodruk, źródła, status zdjęcia (placeholder). Dane: `public/assets/data/content.json` / `content.js` (`window.NSZ_CONTENT`).

**Formacje — nie używać zamiennie:** NSZ (1942–), NZW (SN, od jesieni 1944), OW ZJ; materiał „Rozkaz Domana” dotyczy NZW.
