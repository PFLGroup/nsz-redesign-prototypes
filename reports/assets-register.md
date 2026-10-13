# Rejestr zasobów i licencji

Stan: 13.10.2026. Zasada: do publicznego podglądu trafiają wyłącznie zasoby z potwierdzonym prawem użycia. **Żadna fotografia, skan ani logo z nsz.com.pl, Cyfrowego Archiwum lub IPN nie została skopiowana ani hotlinkowana.**

## 1. Zasoby użyte w prototypach

| Plik / grupa | Pochodzenie | Autor | Licencja / podstawa | Wymagany podpis | Status |
|---|---|---|---|---|---|
| `01-nowoczesny/fonts/archivo-*.woff2` | npm `@fontsource-variable/archivo` 5.3.0 | Omnibus-Type | SIL OFL 1.1 (`fonts/OFL-Archivo.txt`) | nie | potwierdzona |
| `02-ultranowoczesny/fonts/space-grotesk-*`, `ibm-plex-mono-*` | npm `@fontsource/space-grotesk`, `@fontsource/ibm-plex-mono` 5.3.0 | F. Marcantonio; IBM | SIL OFL 1.1 (`fonts/LICENSE-*.txt`) | nie | potwierdzona |
| `03-tradycyjny/fonts/playfair-display-*`, `source-serif-4-*` | npm `@fontsource/playfair-display` 5.3.0, `@fontsource/source-serif-4` 5.3.1 | C. Forsythe; Adobe | SIL OFL 1.1 | nie | potwierdzona |
| `04-dziedzictwo/fonts/eb-garamond-*`, `source-sans-3-*` | npm `@fontsource/eb-garamond` 5.3.0, `@fontsource/source-sans-3` 5.3.1 | G. Duffner, O. Pardo; Adobe | SIL OFL 1.1 | nie | potwierdzona |
| `05-awangardowy/fonts/archivo-*`, `newsreader-*`, `ibm-plex-mono-*` | npm `@fontsource-variable/*`, `@fontsource/ibm-plex-mono` | Omnibus-Type; Production Type; IBM | SIL OFL 1.1 (`fonts/OFL-*.txt`) | nie | potwierdzona |
| `05-awangardowy/img/ht-*.svg` | wygenerowane na potrzeby prototypu (raster półtonowy) | zespół prototypu | własne, do swobodnego użycia w projekcie | „Ilustracja koncepcyjna, nie fotografia” | oznaczone na stronie |
| Ilustracje SVG inline (A, B, D: tła, krzyż/pejzaż w D, osie) | wykonane w kodzie prototypu | zespół prototypu | własne | „Ilustracja koncepcyjna” tam, gdzie mogłyby być wzięte za obraz | oznaczone |
| `assets/thumbs/*.jpg` | zrzuty ekranu prototypów (Playwright) | zespół prototypu | własne | nie | — |
| `assets/data/content.json`, `content.js` | tytuły, daty, kategorie i adresy 8 materiałów z nsz.com.pl (odczyt 13.10.2026) + własne zajawki | ZŻNSZ (metadane); zespół (zajawki) | prawo cytatu metadanych z linkiem do źródła; zajawki własne | link do źródła przy każdym materiale | zweryfikowane z REST API serwisu |
| Tekst „Od operacji »Lawina« do Kamesznicy” | opracowanie własne na podstawie IPN, dzieje.pl, nsz.com.pl | zespół prototypu | własne | etykieta „tekst demonstracyjny — nie jest publikacją ZŻNSZ” | oznaczony w każdym wariancie |

## 2. Placeholdery i plan podmiany

| Miejsce | Docelowy materiał | Właściciel praw (do potwierdzenia) | Działanie |
|---|---|---|---|
| Logo w nagłówkach (`[logo ZŻNSZ — oryginalny plik organizacji]`) | oryginalny emblemat Związku w SVG | ZŻNSZ | uzyskać plik wektorowy i zasady użycia; **nie przerysowywać** |
| Zdjęcia z uroczystości (Kamesznica, Wisła, Holiszów) | fotografie z relacji w serwisie | autorzy zdjęć / ZŻNSZ / IPN | ustalić autora i zgodę dla każdego pliku, dodać podpis z autorem |
| Portrety (np. ppłk W. Nestorowicz „Kalina”) | fotografie archiwalne | archiwa rodzinne, IPN | licencja + sygnatura archiwalna |
| Skany dokumentów (rozkaz „Domana”) | skan z sygnaturą | archiwum przechowujące oryginał | ustalić sygnaturę (obecnie brak w źródle) |
| Galerie w artykułach (3 slajdy) | zdjęcia cmentarza w Kamesznicy, Baraniej Góry, dokumentu | IPN Katowice / ZŻNSZ | jw. |
| Multimedia (wideo) | nagrania z uroczystości | autorzy nagrań | zgoda na osadzenie; nie osadzać bez zgody |

## 3. Czego nie użyto i dlaczego

- Zdjęć z nsz.com.pl i Cyfrowego Archiwum — publiczna dostępność nie oznacza zgody na ponowną publikację.
- Znaków i oznak NSZ — nie potwierdzono ich w źródle muzealnym (zob. `work/history-for-design.md`).
- Generowanych portretów i „archiwaliów” — zakaz fabrykowania materiałów historycznych.
- Zewnętrznych CDN, Google Fonts, analityki i trackerów — prototypy nie wysyłają żadnych zapytań poza własną domeną (potwierdzone testem, `reports/qa.md`).

## 4. Zależności narzędziowe (poza opublikowanym podglądem)

| Pakiet | Zastosowanie | Licencja |
|---|---|---|
| `playwright-core` | testy przeglądarkowe (`tests/qa.mjs`, `tests/thumbs.mjs`) | Apache-2.0 |
| `axe-core` | automatyczna kontrola dostępności | MPL-2.0 |
| `lighthouse` (uruchamiany przez `npx`) | pomiar pomocniczy | Apache-2.0 |
