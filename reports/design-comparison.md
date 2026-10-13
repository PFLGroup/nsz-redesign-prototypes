# Porównanie pięciu wariantów

Data: 13.10.2026. Oceny poniżej są **ekspertyzą zespołu projektowego** (oględziny zrzutów 360–1440 px i wyniki testów automatycznych z `reports/qa.md`), **nie wynikiem badań z użytkownikami** — takich badań nie przeprowadzono.

## 1. Profil wariantów w ośmiu obszarach

| Obszar | A · Instytucja 2.0 | B · Żywe Archiwum | C · Kronika Niepodległości | D · Dziedzictwo i Wspólnota | E · Archiwum Awangardowe |
|---|---|---|---|---|---|
| **1. Pierwszy ekran** | Asymetryczny „temat dnia” (zdjęcie + duży tytuł) obok kolumny „Najnowsze” i kalendarza rocznic | Eksplorator: 4 perspektywy (Czas / Miejsca / Ludzie / Dokumenty) i oś czasu — bez banera | Winieta gazety + „rozkładówka numeru” w trzech kolumnach (aktualność / dokument / komentarz) | Jedna opowieść (Kamesznica) z tekstem obok ilustracji + „Najnowsze w Związku” | Plakatowy tytuł wersalikami, monumentalna data 3·V·1946, montaż ilustracji i dokumentu |
| **2. Nawigacja** | Poziome menu z panelem rozwijanym „Historia”, wyszukiwarka z zakresem | Krótkie menu + zakładki perspektyw eksploratora, przełącznik oś/lista | Indeks działów + rozwijany „Indeks działów i tematów”, wyszukiwarka w nagłówku | Menu z podpisami pod pozycjami, trzy wejścia czasownikowe „Poznaj / Upamiętnij / Sięgnij do źródeł” | Typograficzny spis rozdziałów 01–07 + wysuwany indeks (przycisk „Indeks”) |
| **3. Kompozycja aktualności** | Numerowana lista 01–03 w kolumnie bocznej + temat dnia | Siatka 2×2 z wielką datą-cyfrą i przyciskiem „Kontekst w eksploratorze” | Lista z plakietką dnia/miesiąca, kicker działu, „Uroczystości 2026” w bocznej kolumnie | Mozaika miejsc (Kamesznica / Wisła / Holiszów / Siedlce) — aktualności według miejsc | Rozdział „01 Aktualności”: wiersze z datą w zapisie rzymskim i metadanymi w kolumnie mono |
| **4. Typografia** | Archivo (grotesk), duże pogrubienia | Space Grotesk + IBM Plex Mono (etykiety, daty) | Playfair Display + Source Serif 4 (szeryfy, inicjał) | EB Garamond + Source Sans 3 | Archivo (wąskie wersaliki) + Newsreader + IBM Plex Mono |
| **5. Fotografia / obraz** | Duże kadry redakcyjne (placeholdery z opisem licencji) | Brak zdjęcia na starcie; obraz tylko w kartach i artykule | Zdjęcia w ramkach gazetowych z podpisem i sygnaturą | Jedna spokojna ilustracja koncepcyjna, dużo przestrzeni | Raster półtonowy SVG, przycięcia i nałożenia (montaż) |
| **6. Eksploracja historii** | Indeks tematów (5 zakładek: teraz / kontekst / źródła) + osobny widok `historia.html` | Oś czasu i graf powiązań na 45 punktach ze statusem wiarygodności | Kalendarium „najbliższa rocznica” + pełna oś w rozwijanym bloku | Ścieżki „człowiek — miejsce — źródło — pamięć” dla 3 postaci, z ogniwami otwartymi | 7 rozdziałów w `<details>` z oznaczeniem pewności, montaż odsłaniany warstwami |
| **7. Język animacji** | 120–240 ms, przesunięcia strzałek, panel mega-menu | 120–240 ms, wejście karty, płynna zmiana kontekstu | Tylko rozwijanie (200 ms) i przenikanie galerii | 160–300 ms, łagodne zmiany ścieżki | Wipe `clip-path` 240 ms, wysunięcie indeksu 300 ms |
| **8. Układ artykułu** | Klasyczny redakcyjny: metryka w tabeli, spis treści, galeria | Jasny tryb czytania na ciemnym serwisie, notki marginesowe odsyłające do eksploratora | Gazetowy: inicjał, kolumna „Na marginesie”, słowniczek | Spokojny, szeroki margines, „W tym tekście” w ramce | Wersalikowy tytuł, numerowany „Spis rozdziałów”, metadane mono |

## 2. Macierz par — w ilu z 8 obszarów warianty się różnią

Różnica = odmienne rozwiązanie strukturalne (nie tylko kolor lub krój). Próg z briefu: ≥ 5 z 8.

| Para | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Suma | Uwagi |
|---|---|---|---|---|---|---|---|---|---|---|
| A–B | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | **7** | ruch podobny w skali czasów |
| A–C | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **8** | |
| A–D | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ~ | **6** | artykuły podobne strukturą (metryka → spis → tekst) |
| A–E | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | **7** | oba używają Archivo, ale w innym kroju/rejestrze |
| B–C | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **8** | |
| B–D | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | **7** | |
| B–E | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | **7** | oba używają IBM Plex Mono do metadanych |
| C–D | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ~ | **6** | oba szeryfowe; D spokojniejszy, C gazetowy |
| C–E | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **8** | |
| D–E | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **8** | |

✓ = wyraźna różnica, ~ = różnica częściowa (nie liczona). Wszystkie 10 par przekracza próg 5/8; najbliżej progu są A–D i C–D (6/8). Słabszym obszarem całej piątki jest **układ artykułu na telefonie** — w 390 px wszystkie warianty prowadzą sekwencją tytuł → metryka → spis treści → tekst. To naturalny wymóg czytelności, ale w produkcji warto zróżnicować np. spis treści jako przyklejony przycisk.

Wspólne są wyłącznie: dane (`assets/data/content.js`), helpery zachowań (`assets/shared/proto.js`: menu, filtry, galeria, postęp czytania) i reguły dostępności (`assets/shared/a11y.css`). Każdy wariant ma własny HTML i CSS — nie ma jednego szkieletu ukrytego pod pięcioma motywami.

## 3. Oceny eksperckie (1–5)

| Kryterium | A | B | C | D | E |
|---|---|---|---|---|---|
| Tożsamość (zgodność z granatem/czerwienią i charakterem ZŻNSZ) | 4 | 4 | 4 | 3 | 3 |
| Czytelność | 5 | 4 | 4 | 5 | 3 |
| Odrębność | 4 | 5 | 4 | 4 | 5 |
| Dostęp do aktualności | 5 | 4 | 4 | 4 | 4 |
| Eksplorowanie historii | 4 | 5 | 3 | 4 | 4 |
| Obsługa mobilna | 5 | 4 | 4 | 4 | 4 |
| Dostępność (wynik testów + ocena) | 5 | 4 | 5 | 5 | 4 |
| Łatwość wdrożenia w CMS (WordPress, motyw blokowy) | 5 | 2 | 4 | 3 | 3 |
| **Suma** | **37** | **32** | **32** | **32** | **30** |

Uzasadnienia skrótowo:
- **A** wypada najlepiej jako baza produkcyjna: mapuje się na standardowe typy treści WordPressa (wpis, kategoria, tag „temat”), a indeks tematów to taksonomia + zapytanie. Ryzyko: najmniej charakterystyczny wizualnie.
- **B** ma najsilniejszy element eksploracji, ale eksplorator wymaga osobnego modelu danych (punkty, relacje, status wiarygodności) i redakcji — najwyższy koszt wdrożenia i utrzymania.
- **C** jest bardzo czytelny dla starszych odbiorców, ale „rozkładówka numeru” wymaga stałej pracy redakcyjnej; przy obecnym rytmie publikacji (ok. 1 aktualność/mies. w 2026 r., zob. audyt) grozi pustymi numerami.
- **D** — najlepszy spokój czytania; ścieżki pamięci są wartościowe, ale tożsamość odchodzi od obecnego granatu/czerwieni ku zieleni.
- **E** — najbardziej wyrazisty; dłuższa strona główna (ok. 8800 px przy 1440) i wersaliki obniżają czytelność; wymaga dyscypliny, by forma nie była odbierana jako przekaz.

## 4. Rekomendacja

**Kierunek bazowy: A „Instytucja 2.0”** — najlepszy stosunek czytelności, dostępu do aktualności i kosztu wdrożenia przy zgodności z potwierdzoną identyfikacją (`#091635`, `#ad2727`).

**Wariant hybrydowy (opcjonalny): A + moduł osi czasu z B + ścieżki „człowiek — miejsce — źródło — pamięć” z D jako drugi etap.** Oś B w uproszczonej formie (lista z filtrem okresu, bez grafu) można zasilić z tej samej taksonomii co indeks tematów A; ścieżki D to typ treści z czterema relacjami. Szczegóły MVP i etapów: `reports/cms-recommendation.md`.
