# Wariant C — „Kronika Niepodległości” (tradycyjny i tradycjonalistyczny)

Stan na 13 października 2026 r. Prototyp koncepcyjny, nie oficjalny serwis.

## Koncepcja
Serwis jako starannie złożona gazeta: winieta z nazwą Związku, data wydania, indeks działów, kolumny rozdzielone cienkimi liniami, tytuły sekcji na grubej linii. Tradycja dotyczy formy (szeryf, papier, porządek łamu), nie przekazu. Na telefonie układ przechodzi w jedną kolumnę bez utraty hierarchii.

## Widoki
- `index.html` — winieta, rozkładówka numeru, „Z życia Związku”, dział historyczny + tekst numeru, kolumna boczna (Kalendarium, Ludzie, Uroczystości 2026, Multimedia), pas „Archiwum i źródła”, blok „O Związku” z danymi organizacji.
- `aktualnosci.html` — 8 materiałów ze wspólnego zestawu; filtry działów (przyciski `aria-pressed`, liczniki), wyszukiwarka, stan pusty, „Wyczyść filtry”, obsługa `?kat=` i `?q=`. Data publikacji w osobnej kolumnie, data wydarzenia pod nią.
- `artykul.html` — tekst demonstracyjny (generowany z `demo_article` skryptem `work/build-C/build_article.py`): okruszki, etykieta „tekst demonstracyjny”, lead, data, autorstwo (jawny brak podpisu), czas czytania, spis treści z podświetleniem bieżącej sekcji, pasek postępu, inicjał, galeria 3 placeholderów z podpisami, słowniczek, źródła z datą dostępu, kolumna „Na marginesie”, powiązane materiały, nawigacja powrotna.

## Element charakterystyczny
**Rozkładówka numeru** — trzy kolumny I. Aktualność / II. Dokument / III. Komentarz historyczny. Wiadomość Związku (84. rocznica, 20.09.2026) zestawiono z dokumentem z serwisu (rozkaz „Domana”, NZW, 1945) i komentarzem, który wyjaśnia datę rocznicy (rozkaz 1/42 z 20.09.1942) oraz różnicę NSZ ≠ NZW. Dokument ma jawną flagę braku sygnatury.
Uzupełnia ją **Kalendarium** — najbliższa rocznica liczona w JS z 11 zweryfikowanych dat (`kronika.js`, źródła: IPN, Wnuk 2021, dzieje.pl, ELI); bez JS widać statyczny wpis i pełną oś czasu w rozwijanym bloku.

## Nawigacja
Pasek działów (desktop ≥ 980 px) + przycisk „Indeks działów i tematów” otwierający panel z opisanymi działami i listą tematów (linki do wyszukiwania). Na telefonie pasek działów jest ukryty, a przycisk prowadzi do tego samego panelu. Esc zamyka panel i przywraca fokus. Bez JS panel jest zwykłą sekcją pod nagłówkiem.

## Typografia i kolor
- Playfair Display 700/900 — winieta, tytuły; Source Serif 4 400/400i/600/700 — tekst i interfejs. Obie SIL OFL 1.1, pliki w `fonts/` (podzbiory latin + latin-ext, polskie znaki), licencje `fonts/LICENSE-*.txt`. Źródło: pakiety npm @fontsource/playfair-display 5.3.0 i @fontsource/source-serif-4 5.3.1. Zero zapytań zewnętrznych.
- Papier `#f6f1e6`, czerń `#1d1a16`, tekst pomocniczy `#4f463c`, burgund `#7a1c24` (linki, etykiety). Potwierdzona czerwień ZŻNSZ `#ad2727` (z audytu CSS) użyta tylko w ozdobnikach: flagi redakcyjne, pasek postępu. Bez tekstur postarzających.

## Ruch (czasy)
- 120 ms — kolor linków i przycisków;
- 200 ms — rozwijanie materiałów (`details`) i panelu indeksu (krótkie przesunięcie + przenikanie);
- 240 ms — przenikanie slajdu galerii (bez przesuwu, bez autoodtwarzania).
Przełącznik „Animacje” w górnym pasku + `prefers-reduced-motion` (wspólne `proto.js`/`a11y.css`). Brak animacji przy przewijaniu poza paskiem postępu (odwzorowuje pozycję, nie animuje).

## Dostępność
`lang="pl"`, link „Przejdź do treści”, semantyczne `header/nav/main/aside/footer`, jedna H1 na podstronach, widoczny fokus (3 px burgund; jasny na ciemnym tle), cele dotykowe ≥ 44 px, etykiety formularzy, `aria-live` dla liczby wyników i galerii, galeria obsługiwana przyciskami, kropkami i strzałkami (przeciąganie tylko dodatkowo). Placeholdery fotografii mają `role="img"` i opis. Formularz biuletynu jest demonstracyjny — nie wysyła danych.

## Wykonane testy (13.10.2026, Chrome headless, lokalne pliki)
- Zrzuty: `work/screens/C-{index,aktualnosci,artykul}-{390,1440}.png` — obejrzane, poprawiono: zjadane marginesy (`padding` nadpisujący `.wrap`), przepełnienie spisu treści w artykule (grid `min-width`), wyrównanie okruszków, proporcje galerii.
- Brak przewijania poziomego przy 360 i 390 px dla wszystkich 3 widoków (pomiar `scrollWidth` w ramce iframe — headless wymusza minimalną szerokość okna, więc zrzut 390 px robiony jest przez ramkę `work/build-C/frame.html`).
- Filtry: `?kat=dokument` → 1, `?q=zzzz` → 0 + stan pusty widoczny, `?q=Bartek` → 2, `?kat=historia&q=Siedlce` → 1. Galeria inicjuje się („Slajd 1 z 3”, 3 kropki).
- NIE testowano: czytnika ekranu, rzeczywistej obsługi klawiaturą w przeglądarce z interfejsem, szerokości 768/1280, Lighthouse, powiększenia tekstu 200%.

## Ograniczenia
- Brak fotografii i logo — oznaczone miejsca; wymagają plików i licencji od ZŻNSZ/IPN.
- Linki z listy prowadzą do pełnych wpisów w nsz.com.pl; tylko tekst numeru ma lokalny widok artykułu.
- Uroczystości 2026 to wydarzenia minione — nie wymyślano zapowiedzi.
- Ciemny motyw nie został przygotowany (świadoma decyzja dla „papierowego” wariantu; do rozważenia w produkcji).
