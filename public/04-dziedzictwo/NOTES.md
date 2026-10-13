# Wariant D — „Dziedzictwo i Wspólnota” — notatki projektowe

**Status:** prototyp koncepcyjny (13.10.2026). Nie jest oficjalnym serwisem ZŻNSZ.

## Koncepcja
Spokojny, „kamienny” portal pamięci: jasne tło `#f3efe6`, ciemna zieleń `#24412f` jako kolor główny i przygaszone złoto (tekst `#7a5c1e`, 5,4:1; linie `#b08d48` tylko dekoracyjnie). Dużo powietrza, cienkie linie, brak ornamentów i haseł. Ciemne tło występuje wyłącznie w bloku „Organizacja” (zieleń + biel, bez złota) — świadome odejście od zestawu „ciemne tło + złoto” znanego z MŻW (benchmarks.md).

## Widoki
- `index.html` — strona główna: opowieść (Kamesznica) z tekstem OBOK ilustracji + „Najnowsze w Związku” → trzy wejścia czasownikowe (Poznaj / Upamiętnij / Sięgnij do źródeł) → **ścieżki pamięci** → mozaika miejsc (aktualności i wydarzenia) → dokument + opracowanie + kalendarz pamięci → organizacja (dane, wsparcie, formularz demo).
- `aktualnosci.html` — lista 8 materiałów, filtr rodzaju (6 przycisków z licznikami), wyszukiwanie na żywo, `?q=` i `?kat=`, licznik `aria-live`, stan pusty z czyszczeniem.
- `artykul.html` — tekst demonstracyjny (etykieta), data, „brak autora”, lead, spis treści z bieżącą sekcją, pasek postępu, galeria 3 placeholderów (przyciski, kropki, strzałki, licznik), słowniczek, źródła z datą dostępu, ramka ścieżki pamięci, powiązane, powrót.

## Element charakterystyczny: ścieżki „człowiek — miejsce — źródło — pamięć”
Trzy ścieżki: kpt. H. Flame „Bartek”, ks. mjr R. Marszałek „Opoka”, ppłk W. Nestorowicz „Kalina”. Każda ma 4 stacje i wiersz „stan weryfikacji”. **Brakujące ogniwa są pokazane jako otwarte** (np. upamiętnienie „Kaliny”, inni kapelani) zamiast dopisane. Bez JS — wszystkie ścieżki jedna pod drugą; z JS — przyciski `aria-pressed`, strzałki klawiatury, adres `#sciezka-…`, komunikat `aria-live` (`d.js`).

## Typografia i fonty (samodzielnie hostowane, zero zapytań zewnętrznych)
- EB Garamond 400/500/400i — nagłówki, lead, cytaty. SIL OFL 1.1 (`fonts/LICENSE-EB-Garamond-OFL.txt`).
- Source Sans 3 400/600/400i — interfejs i tekst. SIL OFL 1.1 (`fonts/LICENSE-Source-Sans-3-OFL.txt`).
- Pliki z pakietów npm `@fontsource/eb-garamond@5.3.0`, `@fontsource/source-sans-3@5.3.1`, podzbiory latin + latin-ext (polskie znaki). ~416 KB łącznie, ładowane według `unicode-range`.

## Ruch
160 ms — stany przycisków/linków; 240 ms — zmiana ścieżki, slajd galerii; 300 ms — wejście panelu menu/wyszukiwarki. Brak autoodtwarzania. `prefers-reduced-motion` + przełącznik „Animacje” (zapamiętany w localStorage) wyłączają ruch.

## Dostępność (sprawdzone w Chrome headless 13.10.2026)
Link „Przejdź do treści”, landmarki, kolejność nagłówków, fokus 3 px, cele ≥44 px (poza linkami w tekście ciągłym), kontrast tekstu ≥5,4:1. Brak poziomego przewijania przy 360/390 px (scrollWidth = szerokość okna przy 390). Menu mobilne i przełączanie ścieżek przetestowane skryptem; stan pusty filtrów — zrzutem. **Nie wykonano** testu czytnikiem ekranu ani Lighthouse.

## Obrazy i prawa
Brak zdjęć i hotlinków. Ilustracje SVG oznaczone „Ilustracja koncepcyjna — nie fotografia”; placeholdery z opisem docelowego materiału i wymaganej licencji. Logo — tekstowy placeholder `[logo ZŻNSZ — oryginalny plik organizacji]`.

## Ograniczenia
- Linki materiałów prowadzą do nsz.com.pl (prototyp nie ma własnych podstron wpisów).
- Ścieżki opierają się na pojedynczych źródłach (dzieje.pl, biogram Łapińskiego); przed produkcją — weryfikacja redakcyjna.
- W CMS ścieżka = typ treści z 4 relacjami (osoba, miejsce, źródło, upamiętnienie) + pole „stan weryfikacji”.
