# Wariant A „Instytucja 2.0” — notatki projektowe

Data: 13.10.2026. Status: prototyp koncepcyjny, statyczny HTML/CSS + niewielki JS.

## Koncepcja
Nowoczesny portal redakcyjny instytucji: ciepła biel (`#fbfaf7`), grafit (`#1d2024`), oszczędny karmin `#ad2727` z potwierdzonej obecnej identyfikacji (audyt) i granat `#091635` tylko w pasku narzędzi i stopce. Pierwszy ekran ma przypominać autorsko zaprojektowany portal, a nie landing page: zdanie o tożsamości Związku, asymetryczny „temat dnia” (zdjęcie + duży tytuł obok, z paskiem „Kontekst”) i kolumna „Najnowsze” z kalendarzem stałych dat rocznic.

## Widoki
- `index.html` — strona główna: tożsamość, temat dnia, najnowsze, kalendarz rocznic, **indeks tematów**, dokument (NZW, z uwagą redakcyjną o braku sygnatury), życiorys, mini-oś czasu, multimedia (placeholdery), blok „O Związku” z danymi rejestrowymi i kontaktem.
- `aktualnosci.html` — spis 8 materiałów: filtry rodzaju (przyciski `aria-pressed`), wyszukiwarka, licznik `aria-live`, stan pusty, „Wyczyść filtry”, obsługa `?q=` i `?kat=`.
- `artykul.html` — tekst demonstracyjny (wyraźnie oznaczony): okruszki, metryczka (data, brak podpisu autora + nota), lead, spis treści z podświetlaniem bieżącej sekcji, pasek postępu czytania, galeria 3 slajdów (przyciski, kropki, strzałki klawiatury, przeciąganie jako dodatek, bez autoodtwarzania), źródła z datą dostępu, „W tym temacie”, powiązane, nawigacja powrotna.
- `historia.html` — kontekst historyczny: oś czasu 11 dat ze źródłami, tabela nazw (NOW / ZJ / NSZ / NSZ-AK / NSZ-ZJ / NZW), zagadnienia sporne i trudne (Brygada Świętokrzyska, Wierzchowiny, Kraśnik, ideologia i mniejszości, liczebność) z etykietami potwierdzone / sporne / interpretacja.

## Element charakterystyczny: redakcyjny indeks tematów
Pięć tematów; każdy łączy trzy kolumny: **Teraz w serwisie** (bieżące wpisy) → **Kontekst historyczny** → **Źródła i opracowania**, plus ewentualną uwagę redakcyjną (np. rozbieżna liczebność, brak źródeł w tekście). Wzorzec zakładek pionowych (strzałki, Home/End; role ARIA dodaje JS). Bez JS wszystkie panele są widoczne jeden pod drugim. Temat wyróżniony w artykule („Temat 01 z indeksu”) domyka pętlę aktualność → historia → źródło.

## Nawigacja
Pasek narzędzi (Cyfrowe Archiwum, kontakt, przełącznik animacji) → nagłówek (znak tekstowy, przycisk „Szukaj”, przycisk „Menu” < 960 px) → pozioma nawigacja z panelem rozwijanym „Historia” (mega-panel: wprowadzenie, materiały, przykład). Wyszukiwarka w panelu z **wyborem zakresu** (Wszystko / Aktualności / Historia / Dokumenty), podpowiedziami na żywo i „często szukanymi”. Bez JS formularz działa jako zwykły GET do listy.

## Ruch (czasy)
- 120 ms — reakcje przycisków i strzałek („→” przesuwa się o 3 px), kolory.
- 180 ms — podkreślenie pozycji menu (scaleX), przełączenie panelu indeksu (fade + 4 px).
- 240 ms — rozwijanie mega-panelu, panelu wyszukiwania i menu mobilnego; zmiana slajdu.
Jedna animacja naraz, bez autoodtwarzania. `prefers-reduced-motion` i przełącznik „Animacje” w pasku narzędzi (zapamiętywany w `localStorage`).

## Typografia i fonty
Archivo (zmienna, 100–900), samodzielnie hostowana: `fonts/archivo-latin-wght-normal.woff2`, `fonts/archivo-latin-ext-wght-normal.woff2` z pakietu npm `@fontsource-variable/archivo` 5.3.0. Licencja: SIL Open Font License 1.1 — `fonts/OFL-Archivo.txt`. Zero zapytań do serwerów zewnętrznych w czasie działania strony. Zapas: Segoe UI / system-ui.

## Obrazy i logo
Brak fotografii — tylko oznaczone placeholdery z informacją o potrzebnej licencji. Emblemat ZŻNSZ celowo nieodtworzony: pole „[logo ZŻNSZ — oryginalny plik organizacji]”. Linki do materiałów prowadzą do nsz.com.pl.

## Dostępność
Link „Przejdź do treści”, `lang="pl"`, jeden `h1` na widok, widoczny fokus (3 px), cele dotykowe ≥ 44 px, `aria-current` w nawigacji i spisie treści, `aria-live` dla wyników i galerii, Escape zamyka panele, kontrast tekstu ≥ 4.5:1 (np. `#5b6068` na `#fbfaf7` ≈ 6:1).

## Testy wykonane (13.10.2026, headless Chrome)
- Zrzuty 390 i 1440 px wszystkich 4 widoków (`work/screens/A-*.png`), obejrzane; poprawiono: konflikt klas `.ctx`, nadpisanie marginesów bocznych, za mały znak logo, okruszki.
- Brak poziomego przewijania przy 360, 390, 768 px (pomiar `scrollWidth` w ramce iframe).
- Skryptowy test interakcji (`work/variant-A/itest.html`): menu mobilne, panel wyszukiwania, podpowiedzi, zakładki indeksu, `?kat=`, stan pusty, czyszczenie filtrów, `?q=`, galeria, przełącznik animacji — wszystkie przeszły, 0 błędów JS.
- Nie wykonano: Lighthouse, audytu czytnikiem ekranu, testów na fizycznym telefonie.

## Znane ograniczenia
- Link do raportu historycznego wskazuje przewidywany adres repozytorium `PFLGroup/nsz-redesign-prototypes` — działa dopiero po publikacji.
- Zestaw demonstracyjny ma tylko 8 materiałów; „Ludzie”, „Archiwum”, „Wydarzenia” w menu prowadzą do przefiltrowanej listy, nie do osobnych widoków.
- Kalendarz pokazuje stałe daty rocznic, nie zapowiedzi wydarzeń (nie wymyślamy terminów).
- Generator: `work/variant-A/build.py` (z `content.json`); po zmianie danych trzeba go uruchomić ponownie.
