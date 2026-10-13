# Wariant B „Żywe Archiwum” — notatki projektowe

Prototyp koncepcyjny, a nie oficjalny serwis. Stan na 13.10.2026.

## Koncepcja
To ciemny portal eksploracyjny. Zamiast banera fotograficznego pierwszy ekran zajmuje **eksplorator historii** z czterema perspektywami: **Czas / Miejsca / Ludzie / Dokumenty**. Każdy punkt ma źródło i status wiarygodności. Użytkownik przechodzi między perspektywami po powiązaniach, np. data → osoba → miejsce. Długi tekst czyta się w jasnym, spokojnym trybie (`artykul.html`).

## Widoki
- `index.html`. Kolejność sekcji:
  - eksplorator (oś lat albo siatka punktów, karta punktu z powiązaniami, przełącznik „Oś i powiązania / Lista”);
  - „Teraz w Związku”: strumień z dużymi datami;
  - rekordy z zasobu: dokument NZW z metryką i brakiem sygnatury, biogram, opracowanie;
  - liczby zasobu (REST API, 13.10.2026) i link do Cyfrowego Archiwum;
  - dane Związku i formularz demonstracyjny.
- `aktualnosci.html`. Lewa kolumna to wyszukiwarka, filtry rodzaju materiału, licznik i przycisk „Wyczyść”. Prawa kolumna to oś dat z rekordami. Strona obsługuje stan pusty oraz parametry `?q=` i `?kat=` (`aktualnosc|wydarzenie|historia|biogram|dokument`).
- `artykul.html`. Tekst demonstracyjny z etykietą, autorstwo oznaczone jako niewskazane. Zawiera spis treści z podświetleniem bieżącej sekcji, pasek postępu czytania, notki marginesowe „W eksploratorze” (odsyłacze `index.html#n-<id>`), galerię z trzema oznaczonymi placeholderami, źródła, powiązane materiały i nawigację powrotną.

## Element charakterystyczny
- **Dane eksploratora** to 45 punktów: 21 dat, 10 miejsc, 8 osób, 6 dokumentów i opracowań. Pochodzą z `work/history-for-design.md` i `reports/sources.csv`, a każdy punkt ma URL źródła.
- **Statusy punktów:** potwierdzone, fakt potwierdzony z oceną sporną (porozumienie Brygady Świętokrzyskiej z Wehrmachtem), relacja ZŻNSZ bez bibliografii, brak sygnatury, potwierdzone w streszczeniu badań.
- **Trudne wątki** (Kraśnik 1942, Wierzchowiny 1945) są oznaczone i przypisane konkretnym oddziałom.
- **Holiszów** jest opisany bez liczb, bo źródła podają różne.
- **NZW** jest konsekwentnie odróżniane od NSZ.
- **Jedno źródło danych:** dane siedzą w HTML jako lista `li.node` (`data-facet`, `data-links`, `data-status`). Bez JS ta lista jest widokiem równoważnym. `explorer.js` buduje z niej zakładki ARIA (strzałki, Home, End, roving tabindex), oś lat ze zaznaczonymi przerwami w skali, kartę punktu (aria-live), symetryczne powiązania i stałe odnośniki `#n-<id>`.
- **Na telefonie** wybór punktu przenosi fokus na kartę, a karta ma przycisk powrotu.

## Ruch
- Czasy: 120 ms (hover, kolor), 180 ms (tło zakładek, przyciski), 240 ms (podkreślenie zakładki, wejście karty, przejście slajdu). Krzywa `cubic-bezier(.2,.7,.2,1)`.
- Nic nie odtwarza się samo, nie ma scrolljackingu, a galeria nie przewija się automatycznie.
- `prefers-reduced-motion` oraz przełącznik „Animacje” (współdzielony `proto.js`) skracają ruch do 1 ms.

## Typografia i kolor (propozycja projektowa)
- **Space Grotesk 500/700** w nagłówkach, **IBM Plex Mono 400/500** w metadanych, datach i etykietach, systemowy krój bezszeryfowy w tekście.
- Fonty są hostowane lokalnie w `fonts/` (podzbiory latin i latin-ext) i nie wysyłają zewnętrznych zapytań. Licencja SIL OFL 1.1: `fonts/LICENSE-SpaceGrotesk.txt` i `fonts/LICENSE-IBMPlexMono.txt`, źródło npm `@fontsource/*` 5.3.0.
- **Kolory:**
  - atramentowy granat `#0a1430`, nawiązujący do potwierdzonego `#091635` z obecnego nagłówka;
  - tekst `#eef1f8`, przytłumiony `#b8c1da`;
  - punktowa czerwień `#ff7a6e` na granacie i `#b0261f` na papierze;
  - statusy: turkus `#7fd1c7` (potwierdzone) i bursztyn `#f2c14e` (sporne);
  - tryb czytania: papier `#f6f4ef`, tekst `#1a1f2e`.
- **Kontrast** policzony dla 22 par kolorów: najniższy wynik to 6,08:1 (czerwień na papierze), więc AA jest spełnione.

## Dostępność
- Link „Przejdź do treści”, `lang="pl"`, `noindex`, baner prototypu w HTML.
- Widoczny fokus `#ffd75e`; w trybie czytania `#1c3fa8`.
- Cele dotykowe mają co najmniej 44 px, z wyjątkiem linków w tekście.
- Jeden `h1` na stronę, logiczne `h2`–`h4`.
- Formularz newslettera jest demonstracyjny i niczego nie wysyła.
- Bez JS ukrywane są tylko kontrolki wymagające skryptu.

## Testy (13.10.2026, Chrome headless przez CDP, `work/cdp_shot.mjs`, `work/test_B.mjs`)
- **Szerokości 360, 390, 768, 1280 i 1440 px:** brak poziomego przewijania, brak błędów konsoli i brak niezaładowanych obrazów we wszystkich trzech widokach.
- **Testy interakcji: 33 z 33 PASS.** Obejmują zakładki i klawiaturę, kartę i powiązania, deep linki, widok listy, panel wyszukiwania z Escape, przełącznik ruchu, menu mobilne z fokusem karty, filtry, `?kat=`, `?q=`, stan pusty z czyszczeniem, wyszukiwanie bez polskich znaków, galerię (przyciski i strzałki), pasek postępu oraz tryb bez JS.
- **Zrzuty:** `work/screens/B-*.png` (oglądane i poprawione).
- **Nie wykonano:** Lighthouse, axe ani testu z czytnikiem ekranu. Uwaga: headless Chrome bez emulacji nie schodzi poniżej ~484 px, dlatego zrzuty mobilne robione są przez `Emulation.setDeviceMetricsOverride`.

## Ograniczenia
- Fotografie to oznaczone placeholdery, bo prawa nie są potwierdzone. Logo to placeholder tekstowy.
- Wspólna wyszukiwarka (`proto.js`) dopasowuje podciągi, a nie formy fleksyjne: „Kamesznica” nie znajdzie „Kamesznicy”. W produkcji potrzebny jest stemming lub wyszukiwarka pełnotekstowa dla języka polskiego.
- Zbiór eksploratora jest demonstracyjny. Wątek katolicki i gospodarczy oraz lista kapelanów (potwierdzony tylko ks. Marszałek) wymagają dalszych badań.
- Generator HTML: `work/build_variant_B.py`. Po zmianie danych trzeba go uruchomić ponownie.
