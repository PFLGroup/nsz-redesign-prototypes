# Audyt serwisu nsz.com.pl

**Data oględzin:** 13 października 2026 r.
**Metoda:** wyłącznie pasywne, publiczne odczyty: pobranie HTML (curl), publiczne endpointy WordPress REST API (`/wp-json/wp/v2/*`, tylko odczyt list i nagłówków `X-WP-Total`), mapy witryny Yoast, arkusze CSS oraz zrzuty ekranu z Chrome w trybie headless (1440 px i 390 px). Bez prób logowania, skanerów podatności i obchodzenia zabezpieczeń.
**Oznaczenia:** **[P]** ustalenie potwierdzone (bezpośredni dowód), **[I]** interpretacja, **[H]** hipoteza projektowa, **[N]** informacja niezweryfikowana.

Zrzuty ekranu: `work/screens/current-home-desktop.png`, `current-home-mobile.png`, `current-article-desktop.png`, `current-category-mobile.png`, `current-archiwum-desktop.png`.

---

## 1. Podmiot, cel i system powiązanych witryn

| Ustalenie | Status | Dowód |
|---|---|---|
| Serwis prowadzi **Związek Żołnierzy Narodowych Sił Zbrojnych (ZŻNSZ)**, KRS 0000153859, NIP 527-172-52-61, siedziba ul. 11 Listopada 17/19 lok. 115, Warszawa | [P] | https://www.nsz.com.pl/kontakt/ (zmod. 2025-03-24) |
| Redakcja portalu wskazana imiennie na stronie Kontakt; e-mail redakcja[at]nsz.com.pl | [P] | jw. |
| Deklarowany cel (strona „Wspieram”): „przywracać pamięć o Żołnierzach Wyklętych”, „kształtowanie patriotycznych postaw obywatelskich” | [P] | https://www.nsz.com.pl/wspieram-zznsz/ |
| Organizacja prowadzi też program „Akademia Kompetencji Cyfrowych” dla seniorów 60+ (współfinansowany z programu „Aktywni+”, edycja 2023) | [P] | https://www.nsz.com.pl/akademiacyfrowa/ |
| Strona „O NSZ” (1680 słów, ost. zmiana 2019-08-23) to tekst publicystyczno-historyczny w perspektywie Związku, bez przypisów | [P] / [I] | https://www.nsz.com.pl/o-nsz/ |
| **Cyfrowe Archiwum ZŻNSZ** to **osobna instalacja** WordPress 6.4.13 z motywem GeneratePress (+ GP Premium, Search & Filter Pro, wtyczka dostępności „pojo-accessibility”); 8 501 wpisów i 25 347 plików mediów wg REST | [P] | https://archiwumcyfrowe.nsz.com.pl/ — meta generator, ścieżki `themes/generatepress_child`, `X-WP-Total` |
| Integracja archiwum z portalem ogranicza się do linków w menu (brak wspólnego wyszukiwania, taksonomii, logowania) | [I] | menu obu witryn; brak wspólnych endpointów |
| Link „Archiwalna wersja strony NSZ” prowadzi do **stara-strona.nsz.com.pl** — osobna, starsza witryna na **Joomla!** (meta generator) | [P] | https://stara-strona.nsz.com.pl/ |
| Arkusz motywu potomnego odwołuje się do grafiki na `weryfikacja.nsz.com.pl`, która nie odpowiada (brak połączenia); reguła jest nadpisywana w „Dodatkowym CSS” | [P] | `wp-content/themes/magazine-nsz/style.css`, wiersz ~105; curl → kod 000 |

**Rozróżnienie historii od działalności bieżącej [I]:** serwis nie oddziela wyraźnie trzech warstw — (1) historii NSZ i pokrewnych formacji (NSZ, NZW, OW ZJ), (2) bieżącej działalności Związku (uroczystości, poczty sztandarowe, pielgrzymki, patronaty), (3) publicystyki i autoprezentacji. Wszystkie trafiają do tych samych kategorii (wpis może mieć jednocześnie „Aktualności”, „Wspomnienia” i „Życiorysy”). Strona „O NSZ” łączy opis historyczny z oceną współczesnej pamięci.

---

## 2. Inwentaryzacja adresów i zakres odczytu

| Zasób | Liczba | Źródło |
|---|---|---|
| Wpisy (posts) | **1 518** (REST) / 1 519 w mapach | `X-WP-Total`, `post-sitemap.xml` (1001) + `post-sitemap2.xml` (518) |
| Strony (pages) | 13 (REST) / 12 w mapie | `page-sitemap.xml` |
| Kategorie | 29 (w tym 12 podkategorii miesięcy „kalendarium”) | `/wp-json/wp/v2/categories` |
| Tagi | 1 340 (REST) / 1 300 w mapach | `post_tag-sitemap*.xml` |
| Pliki mediów | 5 543 | `/wp-json/wp/v2/media` |
| Konta użytkowników widoczne w REST | 14 | `/wp-json/wp/v2/users` (nazw nie przenoszę do raportu) |
| **Odkryte adresy publiczne łącznie (mapy witryny)** | **≈ 2 860** (1 519 + 12 + 29 + 1 300), bez paginacji archiwów | mapy Yoast |

**Rozkład publikacji wg roku (REST, filtr `after/before`):**

| Rok | Wszystkie wpisy | w tym „Aktualności” |
|---|---|---|
| 2020 | 584 | 157 |
| 2021 | 686 | 175 |
| 2022 | 109 | 106 |
| 2023 | 64 | 62 |
| 2024 | 32 | 32 |
| 2025 | 31 | 31 |
| 2026 (do 13.10) | 12 | 12 |

[I] Szczyt 2020–2021 odpowiada przeniesieniu archiwum ze starej witryny (daty wpisów, przeniesione kalendarium 365 dni). Od 2022 r. publikowane są niemal wyłącznie aktualności — ok. 1 wpis miesięcznie w 2026 r. Działy historyczne nie są dziś rozwijane.

**Największe kategorie:** Aktualności 575, kalendarium 379, Życiorysy 200, Wydawnictwa 108, Inicjatywy ZŻNSZ 106, Filmy 105, Artykuły i opracowania 91, Kultura 51, Wspomnienia 36, Dokumenty 32, wiersze i pieśni 17, Patronaty 15, Propaganda komunistyczna 14, Wykazy odznaczonych 3, „Bez kategorii” 2, „do redakcji” 1.

**Faktycznie odczytane (pełna treść):** strona główna (HTML), 5 stron statycznych (O NSZ, Kontakt, Władze naczelne, Wspieram, Akademia Cyfrowa — przez REST), 8 wpisów (wspólny zestaw treści, przez REST), 1 wpis w pełnym HTML (Siedlce), lista kategorii Aktualności (strona 1 i 2 — kod 200), wyszukiwarka (`?s=Flame`), strona 404, strona główna Cyfrowego Archiwum, strona główna starej witryny. **Razem ok. 20 stron.**
**Typy widoków przeanalizowane:** 7 — strona główna, lista kategorii, pojedynczy wpis, strona statyczna, wyniki wyszukiwania, 404, strona główna archiwum (osobny system).
**Pominięte / niedostępne:** treść pozostałych ~1 510 wpisów (analiza próby, nie całości), szczegóły stron Okręgów i Patronatów, pliki PDF biuletynu „Szczerbiec”, galerie, filmy; `weryfikacja.nsz.com.pl` (brak odpowiedzi). Wnioski o całym archiwum są wnioskami z próby i z metadanych.

---

## 3. Strona główna — struktura i ocena

Kolejność bloków (desktop, zrzut 1440 px):
1. Pasek z datą i ikonami FB/Twitter/YouTube.
2. Nagłówek: granatowa grafika z emblematem ZŻNSZ (krzyż z literami N-S-Z) i nazwą Związku (H1).
3. Czerwony pasek menu: 11 pozycji + 2 rozwijane („Związek Żołnierzy NSZ”, „Biblioteka” — 14 pozycji).
4. Baner 1,5% podatku (grafika, tekst w obrazie).
5. Kalendarium dnia (grafika) + baner „Kalendarium NSZ”.
6. Slider + siatka 4 wyróżnionych wpisów.
7. 8 zielonych przycisków skrótów (Aktualności, Artykuły, Wspomnienia, Filmy, Życiorysy, Kalendarium, Grafiki, Archiwalna wersja strony).
8. Wydawnictwa (5 wpisów z 2020–2022) | Media + Wspieram (5 przycisków kwot) + kalendarz-widżet.
9. Dokumenty ZŻNSZ (4 wpisy, 2021–2023), Inicjatywy ZŻNSZ (karuzela)…

## 4. Problemy (obserwacja → dowód → konsekwencja → rekomendacja → priorytet)

| # | Obserwacja | Dowód | Konsekwencja dla użytkownika | Rekomendacja | P |
|---|---|---|---|---|---|
| 1 | **Przestarzałe oprogramowanie:** WordPress 6.2.14 (aktualna gałąź 7.1.3); motyw nadrzędny News Portal 1.3.5 (w katalogu WP.org: 1.6.0); zasoby wtyczek z parametrami `ver` sugerującymi starsze wydania (Shortcodes Ultimate 7.4.5 vs 7.9.1, Smush 3.16.5 vs 4.3.4) | meta generator; `api.wordpress.org/core/stable-check` zwraca dla 6.2.14 „outdated”; nagłówek `style.css` motywu; `?ver=` w HTML (parametr wskazuje, nie dowodzi wersji) | ryzyko bezpieczeństwa i niezgodności; WordPress.org deklaruje, że wspierana jest tylko ostatnia gałąź główna, a poprawki dla starszych są „courtesy”, bez gwarancji | aktualizacja rdzenia i wtyczek na kopii testowej; plan wymiany motywu; dotyczy także archiwum (WP 6.4.13 — „outdated”) | **P0** |
| 2 | **Nawigacja mobilna przepełnia ekran:** przy 390 px nazwa Związku w nagłówku i część przycisków skrótów wychodzą poza prawą krawędź; na liście „Aktualności” tekst zajawek jest ucięty | `current-home-mobile.png`, `current-category-mobile.png` (zrzuty headless; zalecane potwierdzenie na urządzeniu) | poziome przewijanie, ucięte treści, gorsza czytelność dla większości odwiedzających z telefonu | responsywny nagłówek (logo + krótka nazwa), zawijanie skrótów, `max-width:100%` dla mediów i tabel | **P0** |
| 3 | **Pierwszy ekran nie mówi, co jest nowego:** po nagłówku i menu użytkownik widzi baner 1,5%, grafiki kalendarium i dopiero potem wyróżnienia; najnowsza aktualność (20.09.2026) nie jest pierwszym elementem — w siatce wyróżnionych są wpisy z 2023–2024 | `current-home-desktop.png`; REST: najnowsze wpisy 2026-09-20/17 | wrażenie nieaktualnego serwisu; trudno znaleźć bieżącą działalność | wydzielić „Najnowsze” (3–5 pozycji z datą) nad zgięciem; wyróżnienia sterowane ręcznie z datą ważności | **P1** |
| 4 | **Slider na desktopie w zrzucie headless pozostał pusty** (lewa kolumna obok siatki wyróżnień); na mobile wyświetla się wpis „APEL” | `current-home-desktop.png` vs `current-home-mobile.png` | [N] może wynikać z leniwego ładowania w trybie headless — wymaga potwierdzenia w zwykłej przeglądarce; jeśli występuje — pusta przestrzeń w kluczowym miejscu | zastąpić slider statycznym tematem dnia (bez autoodtwarzania) | P1 (do weryfikacji) |
| 5 | **Tekst w grafikach:** baner 1,5% (z numerem KRS i celem szczegółowym), „Kalendarium 13 października”, „Kalendarium NSZ” to obrazy; obraz kalendarium ma `alt` „kalendarium NSZ 13 X”, baner 1,5% ma pusty `alt` | HTML strony głównej (`wp-image-16227 alt=""`) | treść niedostępna dla czytników ekranu i wyszukiwarki; nie da się skopiować numeru KRS | dane jako tekst HTML; grafika jako dekoracja | **P1** |
| 6 | **Menu bez hierarchii:** „Biblioteka” zawiera 14 pozycji o różnym charakterze (PDF jednego numeru biuletynu z 2022 r., kategorie, link do innej domeny, strona „Grafiki”); pozycje główne mieszają organizację (Władze), treści (Aktualności) i akcje (Wspieram) | `primary-menu` w HTML | użytkownik nie wie, gdzie szukać historii vs. działalności Związku | IA: Aktualności / Historia / Ludzie / Archiwum / Multimedia / Wydarzenia / Związek / Wesprzyj — z panelem rozwijanym | **P1** |
| 7 | **Autorstwo nieczytelne:** wpisy przypisane do kont z pseudonimami technicznymi (np. „Jaszczurka01”, „Mario66”), a faktyczni autorzy pojawiają się — jeśli w ogóle — w ostatnim akapicie tekstu (np. „Rafał Sierchuła, IPN Poznań”, „Piotr Łapiński w: Głos znad Narwi”) | REST `author` + końcówki treści 8 wpisów | odbiorca nie wie, kto odpowiada za tekst i czy to przedruk; utrudnia ocenę wiarygodności | pole „Autor/autorka” i „Pierwodruk” w modelu treści; konto redakcyjne ≠ autor | **P1** |
| 8 | **Brak aparatu źródłowego:** teksty historyczne (np. Siedlce 1944) bez przypisów i bibliografii; dokumenty bez sygnatur archiwalnych (np. rozkaz „Domana”) | treść wpisów 14658, 10062 | utrudniona weryfikacja; ryzyko utraty wiarygodności | pola „Źródła”, „Sygnatura”, „Zasób”; szablon przypisów | **P1** |
| 9 | **Uszkodzone slugi** po migracji: polskie znaki wycięte z adresów (np. `/55-rocznica-powstania-narodowych-si-zbrojnych/`, `/ycie-i-mier-dla-wolnej-polski-…/`) — co najmniej 17 takich adresów w mapach (wyszukiwanie po kilku wzorcach) | `post-sitemap*.xml`; sekcja „Powiązane wpisy” w artykule | nieczytelne linki; przy przebudowie trzeba je zachować lub przekierować | mapa przekierowań 301 przy migracji; nie poprawiać slugów bez przekierowań | P2 |
| 10 | **Publiczny endpoint użytkowników** `/wp-json/wp/v2/users` zwraca 14 kont (nazwy wyświetlane i slugi) | `X-WP-Total: 14` | ułatwia enumerację loginów (wektor ataków na hasła) | ograniczyć endpoint users dla anonimowych (filtr REST), nie wyłączać całego REST (dokumentacja WP odradza) | **P1** |
| 11 | **Ciężki front:** 15 arkuszy CSS (w tym dwie wersje Font Awesome — 4.7 z motywu i 5.15 z CDN), ~20 skryptów, 3 rodziny Google Fonts, ~480 pustych linii w HTML (143 KB HTML) | lista `<link rel=stylesheet>`, `<script>` w HTML | wolniejsze ładowanie na telefonach; podwójne ikony | jeden zestaw ikon (SVG), lokalne fonty, usunięcie nieużywanych wtyczek | P2 |
| 12 | **Kalendarz-widżet pod nagłówkiem „Najnowsze wpisy”** na stronie głównej (nagłówek nie odpowiada treści); kalendarz miesięczny jako nawigacja po archiwum | `current-home-desktop.png` | myląca etykieta; mała użyteczność | usunąć lub zastąpić listą najnowszych | P2 |
| 13 | **Tekst artykułu wyjustowany** z wąską interlinią w sidebarze; brak spisu treści w długich tekstach (np. biogram 3 300 słów) | `current-article-desktop.png`; REST (liczba słów) | trudniejsze czytanie, zwłaszcza dla starszych odbiorców i osób z dysleksją | wyrównanie do lewej, 65–75 znaków w wierszu, spis treści dla tekstów > 1200 słów | P2 |
| 14 | **Kategorie przeciążone kalendarium:** 12 podkategorii miesięcy (po ~30 wpisów) w drzewie kategorii | REST categories | zaśmiecona taksonomia, trudne filtrowanie | kalendarium jako osobny typ treści z polem daty (dzień-miesiąc) | P2 |
| 15 | Link do **dwóch kolejnych systemów** (Joomla — stara witryna, WP — archiwum) bez wyjaśnienia różnic | menu + przyciski | użytkownik trafia do 3 różnych interfejsów | jedna strona „Archiwum” opisująca zasoby i ich status | P2 |

**Pozytywne (warte zachowania) [P/I]:**
- **Bogaty, unikatowy zasób:** 200 życiorysów, 379 wpisów kalendarium, 32 dokumenty, 105 filmów, 8 501 rekordów Cyfrowego Archiwum — to kapitał treści, którego nie ma wiele organizacji kombatanckich.
- **Kalendarium „tego dnia”** — dobry, powtarzalny pretekst do powrotu na stronę (warto przenieść do HTML).
- Cyfrowe Archiwum ma już **fasetowe filtry** (zespoły akt, formacje, rodzaje dokumentów, daty, województwa, koła) i formularz „Przekaż archiwalia” — wzorzec do zintegrowania z portalem.
- Rozpoznawalny **emblemat ZŻNSZ** i konsekwentna czerwień w nawigacji.
- Działający link pomijający (`skip-link`), `lang="pl-PL"`, Yoast SEO z mapami witryny, przekierowanie `http`→`https` i `nsz.com.pl`→`www`.
- Publiczne dane organizacyjne (KRS, NIP, konto, adresy) w jednym miejscu.

---

## 5. Identyfikacja wizualna (stan obecny)

**Logo / znaki [P]:** emblemat ZŻNSZ — srebrny krzyż z literami N, S, Z na ramionach, z biało-czerwoną wstęgą; plik `wp-content/uploads/2019/01/ZZNSZ-emblemat.jpg` (og:image). Logo PDF do pobrania na stronie Kontakt. Cyfrowe Archiwum używa **innego znaku** (stylizowane książki z literami N-S-Z). Tło nagłówka: grafika `nsz-bg.png` (orzeł i jaszczurka — motyw odwołujący się do Związku Jaszczurczego [I]). **Znaczenia symboli nie interpretuję bez źródła** — do potwierdzenia przez Związek.

**Kolory odczytane z CSS [P]:**

| HEX | Rola | Plik / selektor |
|---|---|---|
| `#ad2727` | główna czerwień: pasek menu, akcenty, obramowania | „Dodatkowy CSS” (`.unclickable > a:hover`, wiele reguł); `magazine-nsz/style.css` |
| `#530b0b` | ciemny bordo: hover ikon społecznościowych | `magazine-nsz/style.css` |
| `#091635` | granat tła nagłówka z logo | `magazine-nsz/style.css` `.np-logo-section-wrapper` |
| `#05131e` / `#0b1626` | prawie czarny granat: pasek górny i stopka | „Dodatkowy CSS” (`.np-top-header-wrap`, `#colophon`) |
| `#2b5c13` / `#1b3d0b` | zieleń przycisków skrótów (stan zwykły / hover) | „Dodatkowy CSS” `.cgreen` |
| `#db3941` | czerwień przycisków darowizn (obrys, tekst) | „Dodatkowy CSS” `.nav-donate` |
| `#d62828` / `#a40000` | etykieta kategorii „Aktualności” | inline style motywu (`.np-cat-19`) |
| `#a98467` | etykieta „Artykuły i opracowania” | `.np-cat-35` |
| `#029fb2` | domyślny turkus motywu News Portal (pozostałość w arkuszu motywu nadrzędnego) | `news-portal/style.css` |
| `#00a9e0` / `#0077ae` | domyślny błękit etykiet większości kategorii (np. „Inicjatywy ZŻNSZ”) | inline style motywu (`.np-cat-31` i in.) |
| `#0b325a`, `#152345` | ikony okręgów, obramowanie stopki | „Dodatkowy CSS” |

[I] Paleta jest **niespójna**: obok granatu i czerwieni występują zieleń przycisków, turkus i błękit z domyślnych ustawień motywu oraz pomarańcz `.myButton` (`#d0451b`). Rdzeń tożsamości to **granat + czerwień + srebro emblematu + biel**.

**Kroje [P]:** Roboto (tekst), Roboto Condensed i Titillium Web (Google Fonts, ładowane z CDN Google); Font Awesome 4.7 i 5.15; lokalnie Arial w podpisach lightboxa (fix polskich znaków), Ubuntu i „Times New Roman” w pojedynczych regułach. Cyfrowe Archiwum: Ubuntu (GeneratePress).

**Fotografie [P/I]:** fotografie archiwalne portretowe (czarno-białe), fotorelacje z uroczystości (kolor; część z podpisem źródła, np. znak wodny portalu lokalnego), grafiki okolicznościowe z tekstem. **Prawa do ponownej publikacji nie są oznaczone** w sposób systematyczny — dlatego prototypy nie wykorzystują żadnych zdjęć z serwisu (placeholdery).

---

## 6. Wnioski dla projektu [H]

1. Strona główna powinna zaczynać się od **tożsamości + najnowszych 3–5 wydarzeń z datą**, a dopiero potem otwierać wejścia w historię.
2. Potrzebny jest **model treści**, który rozdziela: aktualność Związku, materiał historyczny, biogram, dokument (z sygnaturą), wydarzenie (z datą i miejscem), kalendarium.
3. Autorstwo i pierwodruk to pola, nie akapit na końcu tekstu.
4. Cyfrowe Archiwum zasługuje na **wspólne wejście** („Archiwum”) i — docelowo — wspólne wyszukiwanie.
5. Każdy redesign wymaga **mapy przekierowań** ~2 860 adresów, w tym uszkodzonych slugów.
