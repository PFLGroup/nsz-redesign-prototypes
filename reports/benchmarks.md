# Benchmarki UX — serwisy instytucjonalne i redakcyjne

**Data oględzin:** 2026-10-13 (wszystkie pozycje)
**Wykonawca:** badacz UX i benchmarków (subagent)
**Metoda:**
- **Zrzut** — headless Chrome (`--headless=new --window-size=1440,1800 --virtual-time-budget=8000`), widok desktop, pierwszy ekran + ok. 2 ekrany przewinięcia. Zrzuty: `work/screens/bench-*.png`. Każdy zrzut obejrzany.
- **HTML** — pasywny odczyt kodu strony głównej (`curl`), pliki: `work/bench-html/*.html`. Sprawdzono: atrybut `lang`, heurystycznie obecność linku pomijającego nawigację (wzorce tekstowe „skip / przejdź do treści / pomiń”), biblioteki sliderów (swiper/slick/splide/glide/owl/flickity), meta `generator`.

**Ograniczenia (jawne):**
- Oglądano tylko stronę główną (plus Rijksmuseum „Stories”) w jednej szerokości (1440 px). Wersji mobilnych benchmarków nie testowano — wnioski o RWD to hipotezy.
- Zrzut z headless Chrome nie wykonuje interakcji (menu, filtry, slider) — zachowania interaktywne opisano tylko tam, gdzie widać je na zrzucie lub w HTML.
- Heurystyka „skip link” może dawać fałszywe trafienia/pominięcia; to wskaźnik, nie audyt WCAG.
- Banery cookie zasłaniały część zrzutów (Guardian, NFP, Atavist, Stiftung, Rijksmuseum) — ocena dotyczy widocznej części.

## Próba

Zbadano **16 serwisów** (15 ze zrzutem + IPN tylko z HTML). **13 z 16 to instytucje** (muzea, archiwa, biblioteki, fundacje, instytuty badawcze), 3 to portale redakcyjne.

**Niedostępne / odrzucone z próby (nie obchodzono zabezpieczeń):**

| Serwis | Wynik | Uwagi |
|---|---|---|
| polin.pl | 403 + strona wyzwania Cloudflare („Just a moment…”) | brak oceny |
| iwm.org.uk | 403 | brak oceny |
| nytimes.com | 403 | brak oceny |
| muzeum1939.pl | HTTP 200, ale zrzut pusty (strona renderuje się po JS „index-loading”) | brak oceny wizualnej |
| ipn.gov.pl | HTTP 200, zrzut pusty | tylko odczyt HTML (lang=pl, przełącznik `data-theme`) |
| annefrank.org | brak odpowiedzi w limicie czasu | brak oceny |
| dzieje.pl | HTTP 400 | brak oceny |
| podziemiezbrojne.blox.pl | brak odpowiedzi | serwis prawdopodobnie nieistniejący |

## Tabela benchmarków

| # | Serwis (adres) | Typ | Metoda | Konkretny wzorzec | Zastosowanie w NSZ (wariant) | Ryzyko a11y / wydajność |
|---|---|---|---|---|---|---|
| 1 | Muzeum Powstania Warszawskiego — https://www.1944.pl/ | muzeum | zrzut + HTML | Menu rozłożone w 4 kolumnach od razu widoczne w nagłówku (bez hamburgera na desktopie); pasek dostępności (PJM, A/A/A, wysoki kontrast) w nagłówku; pod sliderem pas 4 bloków „praktycznych” (godziny, ceny, warunki, adres). | A — widoczne menu redakcyjne + pas „informacji organizacyjnych” zamiast ukrywania ich w stopce | Pełnoekranowy slider z 7 kropkami i strzałkami (slider w HTML: 8 trafień) — ryzyko auto-rotacji; kropki to małe cele dotykowe |
| 2 | Fundacja Ośrodka KARTA — https://karta.org.pl/ | fundacja / archiwum | zrzut + HTML (Drupal 7) | Stała lewa kolumna nawigacji (ciemna), sekcje oznaczone tytułem wersalikowym na grubej linii; okrągłe „wejścia” (Archiwum, Edukacja, Wydawnictwo) nałożone na archiwalne zdjęcie; podpisy zdjęć z autorem i sygnaturą archiwum. | C — sekcje z „belką” tytułową jak w gazecie; podpisy z sygnaturą; E — kolumna-spis rozdziałów | Okręgi na fotografii obniżają kontrast tekstu; Drupal 7 to platforma po EOL (obserwacja, nie ocena bezpieczeństwa) |
| 3 | Europeana — https://www.europeana.eu/pl | agregator dziedzictwa | zrzut + HTML | Pierwszy ekran = jedno pole wyszukiwania z liczbą obiektów w placeholderze („Przeszukaj ponad 60 milionów…”) na tonowanym zdjęciu. | B — wejście przez wyszukiwanie/eksplorację, nie baner | Tekst na zdjęciu; pełnoekranowe zdjęcie = ciężki LCP |
| 4 | Rijksmuseum — https://www.rijksmuseum.nl/en (+ /en/stories) | muzeum | zrzut + HTML | Monumentalny wordmark na całą szerokość jako element kompozycji; „Stories” — pełnoekranowy obiekt jako okładka opowieści. | E — monumentalna typografia nagłówka; D — jedna opowieść/obiekt na pierwszym ekranie | Niski kontrast szarego wordmarka na granacie; ciężkie obrazy pełnoekranowe |
| 5 | National Archives (NARA) — https://www.archives.gov/ | archiwum państwowe | zrzut + HTML | 5 kafli „ścieżek odbiorców” (badacze, weterani, nauczyciele, odwiedzający, dokumenty założycielskie) + kolumna „I Want To…” w stopce; dokument (list) jako wyróżniony materiał. | A, D — ścieżki „dla kogo / co chcę zrobić”; wszystkie — „dokument tygodnia” | Kolorowe nakładki na zdjęciach — biały tekst o zmiennym kontraście |
| 6 | US Holocaust Memorial Museum — https://www.ushmm.org/ | muzeum / instytucja pamięci | zrzut + HTML | Główne menu jako 3 czasowniki z podtytułami (Learn About / Remember / Confront); pytanie jako tytuł pierwszego ekranu („Who did the Nazis target?”); wydarzenia z dużą plakietką daty (mies./dzień). | B — wejście przez pytanie badawcze; C — plakietka daty wydarzenia; D — trzy czasowniki („Poznaj / Upamiętnij / Zbadaj źródła”) | Teksturowane tło, ok. Dużo zdjęć archiwalnych — wymagają podpisów i alt |
| 7 | The Guardian — https://www.theguardian.com/international | portal redakcyjny | zrzut + HTML | Siatka z etykietą działu nad tytułem (czerwony „kicker”), względny czas publikacji, szeryfowe tytuły, linie podziału kolumn. | A, C — kicker kategorii + data przy każdej zajawce | Ciężka strona (HTML ~1,3 MB), reklamy i CMP |
| 8 | Notes from Poland — https://notesfrompoland.com/ | portal redakcyjny (WordPress 6.9) | zrzut + HTML | Asymetryczny „lead” (zdjęcie + tytuł obok) i prawa kolumna „Latest insights” z autorami; kategorie spacjowanymi wersalikami. | A — temat dnia + kolumna analiz obok aktualności | Brak wykrytego skip linku (heurystyka); WordPress — dowód, że redakcyjny układ jest wykonalny w WP |
| 9 | Instytut Pileckiego — https://instytutpileckiego.pl/pl | instytut badawczy | zrzut + HTML | Duży materiał wiodący + obok panel „Kalendarz wydarzeń” w tym samym rzędzie; karty z kategorią (WYDARZENIE / AKTUALNOŚCI NAUKOWE) i datą pod krótką kreską. | A — wydarzenia obok tematu dnia; wszystkie — rozróżnienie typów materiału etykietą | Obcinanie tytułów wielokropkiem („…”) utrudnia zrozumienie; poza tym czysto |
| 10 | Szukaj w Archiwach (NAC) — https://www.szukajwarchiwach.gov.pl/ | portal archiwalny | zrzut (HTML = powłoka JS 949 B) | Karty obiektów archiwalnych z metadanymi: tytuł, data, **Zespół**, **Archiwum**; przełącznik „tylko zdjęcia i skany”; zakładki Polecane / Aktualizacje / Najczęściej szukane; liczniki zasobów. | B — karta dokumentu z metadanymi archiwalnymi; C — sygnatura/zespół w podpisie; wszystkie — filtr „tylko ze skanem” | Treść dostępna wyłącznie po JS (powłoka 949 B) — antywzorzec dla prototypów (wymóg: treść bez JS) |
| 11 | Muzeum Żołnierzy Wyklętych — https://www.muzeumzolnierzywykletych.pl/ | muzeum tematycznie pokrewne | zrzut + HTML | Ciemny motyw ze złotym akcentem; obok listy wydarzeń siatka kalendarza miesięcznego z zaznaczonymi dniami; pasek dostępności (rozmiar, kontrast). | D — kalendarz z zaznaczonymi dniami jako widok alternatywny wydarzeń; ostrzeżenie przed zbyt podobną estetyką (ciemny + złoto) w wariancie D | Slider na pierwszym ekranie (2 kropki); siatka kalendarza wymaga etykiet dostępnych dla czytników |
| 12 | Muzeum Historii Polski — https://muzhp.pl/ | muzeum | zrzut + HTML | Plakatowa, typograficzna kompozycja z rastrem półtonowym i przyciętymi literami; widoczne przyciski **pauzy i wyciszenia** animacji; krój monospace w przyciskach. | E — raster, przycinanie typografii, plakat; wszystkie — jawna pauza animacji | Animowany pierwszy ekran (slider w HTML: 95 trafień); treść tytułu przycięta („…A STOI?”) — czytelność cierpi |
| 13 | Stiftung Denkmal für die ermordeten Juden Europas — https://www.stiftung-denkmal.de/ | fundacja / miejsce pamięci | zrzut + HTML (WordPress) | Mozaika 5 zdjęć miejsc pamięci zamiast jednego bannera; moduł **„#An diesem Tag”** (tego dnia) obok aktualności; kolorowe bloki sekcji. | D — mozaika miejsc pamięci; B, C — moduł „Tego dnia w historii” | Pomarańczowe tło z białym tekstem — kontrast do sprawdzenia; brak wykrytego skip linku |
| 14 | The Atavist Magazine — https://magazine.atavist.com/ | magazyn long-read (WordPress) | zrzut + HTML | Minimalna lewa kolumna (Subscribe/About/Archive) i jedna wielka okładka opowieści; kolaż fotograficzny z czerwonym wycięciem w kolejnych materiałach. | E — montaż zdjęcie+czerwień; C/D — jedna opowieść na pierwszym ekranie | Tekst na ciemnym zdjęciu; bardzo ciężkie obrazy |
| 15 | Library of Congress — https://www.loc.gov/ | biblioteka narodowa | zrzut + HTML | Wyszukiwarka z wyborem zakresu („Everything”) w nagłówku; „Top Searches” jako linki-skróty; slider z licznikiem „1/5” i przyciskiem odtwarzania. | A — wyszukiwanie z zakresem (Aktualności / Historia / Archiwum); B — „najczęściej szukane” jako skróty | Slider na pierwszym ekranie (licznik 1/5 to dobry wzorzec, auto-play — ryzyko) |
| 16 | Instytut Pamięci Narodowej — https://ipn.gov.pl/ | instytucja państwowa | tylko HTML (zrzut pusty) | `data-theme="light"` w `<html>` — wbudowany przełącznik motywu; wykryty skip link (heurystyka). | wszystkie — przełącznik jasny/ciemny dla dłuższego czytania (szczególnie B) | Brak oceny wizualnej |

## Częstotliwość wzorców w zbadanej próbie

Liczone **tylko w obrębie próby**. Dla wzorców wizualnych N = 15 (serwisy ze zrzutem); dla wskaźników HTML N = 16, przy czym Szukaj w Archiwach (powłoka JS) jest nierozstrzygnięty.

| Wzorzec | Wystąpienie |
|---|---|
| Duże zdjęcie / animacja dominuje pierwszy ekran | 9 z 15 (MPW, Europeana, Rijksmuseum, USHMM, MŻW, MHP, Stiftung, Atavist, LoC) |
| Slider/karuzela widoczna na pierwszym ekranie (strzałki lub kropki) | 5 z 15 (MPW, MŻW, LoC, Szukaj w Archiwach, MHP) |
| Biblioteka slidera w HTML strony głównej | 6 z 16 (MPW, Europeana, MHP, Stiftung, LoC, + Szukaj nierozstrzygnięty) |
| Widoczny przycisk pauzy animacji/slidera | 2 z 15 (MHP pauza+wycisz, LoC odtwórz) |
| Pole wyszukiwania widoczne od razu (nie tylko ikona) | 5 z 15 (Europeana, KARTA, NARA, Szukaj w Archiwach, LoC) |
| Siatka kart aktualności z datą | 8 z 15 (MPW, KARTA, USHMM, Guardian, NFP, Pilecki, MŻW, LoC) |
| Etykieta typu/kategorii nad tytułem karty | 6 z 15 (Guardian, NFP, Pilecki, LoC, Szukaj w Archiwach, Stiftung) |
| Wejścia według odbiorcy lub zadania („dla nauczycieli”, „chcę…”) | 4 z 15 (NARA, USHMM, LoC, KARTA) |
| Wydarzenia jako osobny panel/kalendarz obok aktualności | 3 z 15 (Pilecki, MŻW, USHMM) |
| Pasek dostępności (rozmiar tekstu / kontrast) widoczny w nagłówku | 3 z 15 (MPW, MŻW, MHP-ikona) |
| Karta obiektu archiwalnego z metadanymi (zespół, archiwum, data) | 1 z 15 (Szukaj w Archiwach) |
| Moduł „tego dnia w historii” | 1 z 15 (Stiftung) |
| Stała boczna kolumna nawigacji | 2 z 15 (KARTA, Atavist) |
| Monumentalna typografia jako główny element kompozycji | 3 z 15 (Rijksmuseum, LoC, MHP) |
| Oś czasu na stronie głównej | **0 z 15** |
| Eksplorator powiązań osoba–miejsce–dokument na stronie głównej | **0 z 15** |
| Przypisy/źródła na marginesie widoczne na stronie głównej | **0 z 15** (artykułów nie badano — nie wiadomo, czy występują w podstronach) |
| Wykryty skip link (heurystyka HTML) | 11 z 16 (KARTA, Europeana, Rijks, NARA, USHMM, Guardian, Pilecki, MHP, Atavist, LoC, IPN); brak trafienia: MPW, NFP, MŻW, Stiftung; Szukaj w Archiwach nierozstrzygnięty (powłoka JS) |
| Baner cookie / CMP zasłaniający treść | 12 z 15 |

Wniosek (interpretacja): w tej próbie oś czasu, eksplorator powiązań i karta dokumentu z metadanymi archiwalnymi na stronie głównej są rzadkie (0–1 z 15) — to przestrzeń wyróżnienia dla NSZ. Twierdzenie, że „w polskich serwisach historycznych nikt tego nie używa”, byłoby nieuprawnione; to **hipoteza projektowa** oparta na 15 stronach głównych.

## Odrzucone schematy (z uzasadnieniem)

1. **Automatyczny pełnoekranowy slider jako pierwszy ekran** — 5 z 15 serwisów go używa, ale ukrywa 4–6 z 7 komunikatów, rotuje treść w trakcie czytania i ma małe kropki-cele (MPW, MŻW). Dopuszczalny tylko jako galeria w artykule: bez auto-play, z przyciskami, klawiaturą i licznikiem „1/5” (wzorzec LoC).
2. **Przypadkowa siatka identycznych kart** (np. 3×N kart o tym samym rozmiarze) — nie komunikuje hierarchii ani typu materiału. Zastępujemy: lead + lista, etykieta typu, różne rozmiary według wagi.
3. **Generyczny układ agencyjny / landing produktu** (hero z hasłem + 3 ikony „korzyści” + CTA) — nie pasuje do instytucji pamięci; żaden z 13 serwisów instytucjonalnych go nie stosował.
4. **Tekst bezpośrednio na pełnym zdjęciu** (Europeana, Atavist, Rijks, NARA) — zmienny kontrast. Jeżeli stosujemy, to z jednolitym panelem pod tekstem albo tekst obok zdjęcia.
5. **Nadmiar gradientów i kolorowych nakładek** (NARA: 5 różnych kolorów nakładek) — rozmywa identyfikację. Odrzucamy jako zasadę; kolor tylko do znaczenia (typ materiału, stan).
6. **Ozdobna typografia przycinająca treść tytułu** (MHP „…A STOI?”) — efektowna, ale użytkownik nie przeczyta komunikatu. W wariancie E przycinamy wyłącznie dekoracyjne numery rozdziałów, nigdy tytuły.
7. **Treść wyłącznie po JavaScripcie** (Szukaj w Archiwach — powłoka 949 B, muzeum1939 — pusty zrzut) — sprzeczne z wymogiem dostępności treści bez JS i z SEO.
8. **Ciemny motyw + złoto jako „estetyka pamięci”** — MŻW (pokrewna tematyka) już go stosuje; powtórzenie osłabiłoby odrębność. Wariant D celowo idzie w jasny kamień i zieleń/bordo.
9. **Estetyka „panelu dowodzenia” / gry wojennej** (HUD, celowniki, radar) — wprost wykluczona briefem; nie zaobserwowana w próbie instytucjonalnej.

**Nie odrzucamy** elementów popularnych, które działają: siatki kart z datą (8 z 15) w widoku listy aktualności, widocznego pola wyszukiwania (5 z 15), etykiet kategorii (6 z 15).

## Rekomendacje mikrointerakcji i ruchu

Wspólna skala czasów (tokeny CSS, propozycja):

| Token | Czas | Krzywa | Zastosowanie |
|---|---|---|---|
| `--t-instant` | 120 ms | `ease-out` | stan hover/fokus przycisków i linków, zmiana koloru ikony, podkreślenie |
| `--t-quick` | 180 ms | `cubic-bezier(.2,.7,.2,1)` | rozwinięcie akordeonu, pojawienie się podpowiedzi wyszukiwarki, przełączenie filtra (fade listy) |
| `--t-base` | 240 ms | `cubic-bezier(.2,.7,.2,1)` | panel menu rozwijanego, szuflada menu mobilnego, przejście slajdu galerii |
| `--t-slow` | 300 ms | `cubic-bezier(.2,.7,.2,1)` | zmiana kontekstu w eksploratorze (B), odsłonięcie dokumentu (E) |

Odstępstwa powyżej 300 ms — tylko z uzasadnieniem: np. 400–450 ms dla przewinięcia osi czasu do wybranego roku (B), bo dystans jest duży i użytkownik musi zachować orientację; nigdy dla elementów blokujących interakcję.

Zasady:
- Animuj `transform` i `opacity`, nie `height/top/left` (wydajność, brak przeskoków layoutu).
- Jedna animacja naraz w danym obszarze; pojawianie się listy po filtrze — co najwyżej przesunięcie 20–30 ms między elementami, maks. 6 elementów (reszta bez opóźnienia).
- `@media (prefers-reduced-motion: reduce)` → czasy 0–1 ms, brak przesunięć; dodatkowo przełącznik „Ogranicz animacje” w interfejsie (zapis w `localStorage` w try/catch).
- Slider/galeria: bez auto-play domyślnie; jeżeli auto-play — widoczny przycisk pauzy (wzorzec MHP), zatrzymanie po fokusie/hoverze/interakcji, licznik „n/N” (wzorzec LoC), strzałki ≥ 44×44 px, obsługa ←/→.
- Ikony: reakcja maks. przesunięcie 2–3 px lub obrót ≤ 90° (strzałka akordeonu) w `--t-instant`/`--t-quick`.
- Fokus: widoczny obrys 2–3 px z odstępem (`outline-offset`), bez animacji (natychmiastowy).
