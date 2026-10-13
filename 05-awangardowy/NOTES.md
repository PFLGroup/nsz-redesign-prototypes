# Wariant E — „Archiwum Awangardowe”

Prototyp koncepcyjny, nie jest oficjalnym serwisem. Stan: 13.10.2026.

## Koncepcja

Serwis zbudowano jak edytorski montaż: tytuł, data, dokument i fotografia zestawione w kontrolowanej asymetrii, w czerni, złamanej bieli i dozowanej czerwieni. Radykalna jest tylko kompozycja: skala, numery rozdziałów i przycięcia siatki. Treść jest analityczna, z oznaczeniem pewności ustaleń. Wariant nie zawiera haseł, symboli organizacyjnych (falanga, miecz itp.), estetyki plakatu werbunkowego ani gloryfikacji przemocy.

## Widoki

| Plik | Zawartość |
|---|---|
| `index.html` | Montaż dnia (00), aktualności w układzie księgi (01), siedem rozwijanych rozdziałów historii (02), kontekst ideowy nurtu narodowo-radykalnego z przypisami (03), teczki z dokumentem NZW i biogramem (04), wydarzenia i multimedia (05), Związek z kontaktem i formularzem demonstracyjnym (06) |
| `aktualnosci.html` | Indeks 9 materiałów: 8 ze wspólnego zestawu i tekst demonstracyjny. Filtr rodzaju, wyszukiwarka, licznik, stan pusty, „Wyczyść filtry”, obsługa `?q=` i `?kat=` |
| `artykul.html` | Tekst demonstracyjny o zgrupowaniu „Bartka”: etykieta, data, informacja o braku autora, lead, spis rozdziałów z bieżącą pozycją, pasek postępu, galeria 3 slajdów z podpisami, źródła z datą dostępu, materiały powiązane i nawigacja powrotna |

Podstrony generuje `work/E-build.py` z `content.json`. Nagłówek, indeks i stopkę skrypt wycina z `index.html`, więc trzy widoki mają identyczną nawigację. Wynik jest zwykłym statycznym HTML-em. Generator służy tylko do utrzymania wariantu i nie jest potrzebny do hostowania.

## Element charakterystyczny: montaż z odsłanianiem warstw

Na pierwszym ekranie data (3·V·1946), półtonowa „fotografia”, karta dokumentu i tytuł nachodzą na siebie. Pod montażem są cztery przyciski warstw: A Dokument, B Kontekst, C Źródła, D Pamięć.

- Przyciski mają `aria-expanded` i `aria-controls`, a strzałki, Home i End przenoszą fokus między nimi. Otwarta jest jedna warstwa naraz.
- Bez JavaScriptu wszystkie warstwy są widoczne jedna pod drugą.
- Warstwa „Dokument” mówi otwarcie, że reprodukcji nie pokazujemy bez sygnatury i podstawy prawnej.

## Nawigacja

- **Pasek:** typograficzne pozycje z numerami rozdziałów, na telefonie skrócone do „Aktualności”.
- **Wysuwany „Indeks”:** spis rozdziałów 00–06 i szybka wyszukiwarka. Esc zamyka panel i oddaje fokus przyciskowi, fokus jest uwięziony w panelu, tło przyciemnione. Bez JS indeks jest zwykłym blokiem na stronie.
- **Rozdziały historii:** natywne `<details>`, działają bez skryptu. Każde zdanie ma oznaczenie Potwierdzone, Interpretacja lub Spór oraz źródło.

## Typografia i kolor

- **Archivo Variable** (oś szerokości 62–125%): monumentalne, zwężone nagłówki i numery.
- **Newsreader:** tekst ciągły, szeryf dla czytelności długich akapitów.
- **IBM Plex Mono:** metadane, daty, podpisy, etykiety.
- **Kolory:** `#0d0d0c` czerń, `#f2eee6` złamana biel, `#ad2727` czerwień potwierdzona w CSS serwisu (na papierze 5,9:1), `#ff6a5c` czerwień na czerni (7,0:1), `#4d4942` i `#b9b3a7` tekst drugorzędny (≥ 8:1).
- Daty zapisano cyframi rzymskimi miesięcy (20·IX), co nawiązuje do druku dokumentów. W `<time>` i treści daty mają pełny zapis.

## Ruch

| Czas | Zastosowanie |
|---|---|
| 120 ms | podkreślenia, zmiana tła przycisków |
| 180 ms | ikona menu |
| 240 ms | odsłonięcie warstwy montażu i rozdziału (wipe `clip-path`), slajd galerii |
| 300 ms | wysunięcie indeksu |

Nie ma autoodtwarzania ani animacji przy przewijaniu. `prefers-reduced-motion` i przełącznik „Animacje” (w indeksie i stopce) wyłączają ruch: wspólna klasa `reduce-motion` jest zapamiętywana w localStorage.

## Fonty i licencje

Wszystkie trzy kroje (latin i latin-ext, `font-display: swap`) są hostowane lokalnie w `fonts/`. Pochodzą z pakietów `@fontsource-variable/archivo`, `@fontsource-variable/newsreader` i `@fontsource/ibm-plex-mono`. Licencja SIL OFL 1.1 — teksty w `fonts/OFL-*.txt`. Wariant nie wysyła żadnych zapytań zewnętrznych poza linkami do źródeł.

## Obrazy

- `img/ht-*.svg` to własne, generowane półtony (`work/E-halftone.py`). Każdy podpis oznacza je jako „ilustracja koncepcyjna, nie fotografia” lub jako miejsce na materiał z licencją.
- Nie ma zdjęć z nsz.com.pl ani hotlinków.
- Logo zastępuje oznaczone pole „logo ZŻNSZ” (atrybut title: „[logo ZŻNSZ — oryginalny plik organizacji]”).

## Testy (13.10.2026, Chrome headless przez CDP, serwer HTTP)

`node work/E-test.mjs` przy działającym `python -m http.server 8765` w `public/` daje 64/64 OK. Testy sprawdzają:

- brak poziomego przewijania przy szerokościach 360, 390, 768, 1280 i 1440 px na 3 widokach;
- cele dotykowe ≥ 44 px dla nawigacji i kontrolek (linki w akapitach testowo pominięte);
- ładowanie obrazów, jeden h1 i brak przeskoków nagłówków, brak błędów konsoli;
- indeks: otwarcie, fokus, Esc, powrót fokusu, szybkie wyszukiwanie;
- warstwy montażu, `<details>`, przełącznik animacji, formularz demonstracyjny;
- filtry, stan pusty, czyszczenie, `?q=` i `?kat=`;
- galeria: przyciski i strzałki klawiatury;
- pasek postępu, kotwice spisu treści, linki wewnętrzne, brak zasobów zewnętrznych.

Zrzuty są w `work/screens/E-*.png` (390 i 1440 px oraz stany: indeks, stan pusty, rozwinięty rozdział).

## Ograniczenia

- Lighthouse i automatyczny audyt axe nie były uruchamiane. Kontrasty policzono ręcznie dla par tokenów, a nie dla każdego elementu.
- Na `file://` przeglądarka blokuje fonty (CORS), więc strona pokazuje kroje zastępcze. Podgląd trzeba otwierać przez serwer HTTP.
- Wspólna szybka wyszukiwarka (`proto.js`) porównuje ciągi znaków bez odmiany. „Kamesznica” nie znajdzie „Kamesznicy”, a „Kamesz” znajdzie. Rozwiązanie produkcyjne: stemming albo wyszukiwarka CMS.
- Treść ideowa i trudne zagadnienia pochodzą z `reports/history-and-ideology.md`. Część prac (Libionka, Zajączkowski) odczytano tylko w abstraktach — wariant to oznacza.
- Montaż jest najbardziej czytelny od 760 px. Na telefonie warstwy układają się pionowo, a karta dokumentu nachodzi na ilustrację tylko częściowo.
- Wysuwany indeks nie przenosi listy rozdziałów do `aria-modal="true"`: pułapka fokusu jest zaimplementowana, ale strony pod spodem nie oznaczono atrybutem `inert`.
