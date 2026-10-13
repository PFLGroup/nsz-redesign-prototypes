# Identyfikacja CMS i rekomendacja produkcyjna

**Data:** 13 października 2026 r. Wszystkie dowody pozyskano pasywnie (publiczny HTML, nagłówki, REST, mapy witryny). Oznaczenia: [P] potwierdzone, [I] interpretacja, [H] hipoteza, [N] niezweryfikowane.

## 1. Technologia — dowody — pewność — ograniczenia

| Technologia | Dowody | Pewność | Ograniczenia |
|---|---|---|---|
| **WordPress 6.2.14** (www.nsz.com.pl) | `<meta name="generator" content="WordPress 6.2.14">`; nagłówek `Link: <…/wp-json/>; rel="https://api.w.org/"`; `/wp-json/wp/v2/posts` zwraca 200 i `X-WP-Total: 1518`; zasoby `wp-includes/…?ver=6.2.14` | **Wysoka** | Meta generatora może być fałszowana lub pozostawiona po aktualizacji, ale zgodność z `?ver=` zasobów rdzenia ją wspiera. |
| Motyw **News Portal 1.3.5** (nadrzędny) + motyw potomny **magazine-nsz 1.0** (autor „NSZ”) | ścieżki `wp-content/themes/news-portal/…`, `…/magazine-nsz/style.css`; nagłówek arkusza (`Template: news-portal`, `Version: 1.0`); `style.css` motywu nadrzędnego: `Version: 1.3.5` | **Wysoka** | Wersja w katalogu WP.org: 1.6.0 (z 2026-09-07) — instalacja nieaktualna [P: api.wordpress.org/themes/info]. |
| Wtyczki: **Yoast SEO**, **AddToAny**, **Shortcodes Ultimate**, **Simple Lightbox**, **Smush** (WP Smush), **FileBird** (blok galerii), **Better Font Awesome** [I] | blok `# START YOAST BLOCK` w robots.txt i `sitemap_index.xml`; ścieżki `wp-content/plugins/…`; id stylów inline `filebird-block-…`, `bfa-font-awesome-v4-shim` | Wysoka dla obecności; **niska dla wersji** | Wersje odczytane z `?ver=` (np. Shortcodes Ultimate 7.4.5, Smush 3.16.5) — to parametr cache, nie dowód wersji. Lista nie jest pełna: wtyczki bez zasobów frontowych są niewidoczne. |
| Serwer **Apache** | nagłówek `Server: Apache` | Średnia | Brak wersji (ukryta); nie wiadomo, czy jest CDN/proxy. |
| **Cyfrowe Archiwum**: WordPress 6.4.13 + GeneratePress (+ potomny) + GP Premium + Search & Filter Pro + wtyczka dostępności (pojo-accessibility) + Yoast | meta generator; ścieżki; robots.txt; REST `X-WP-Total: 8501` wpisów, 25 347 mediów | Wysoka | **Osobna instalacja**, osobna baza. 6.4.13 również „outdated” wg `api.wordpress.org/core/stable-check`. |
| **Stara witryna**: Joomla! | `stara-strona.nsz.com.pl` → meta `generator: Joomla! - Open Source Content Management` | Wysoka dla systemu, brak wersji | Pozostałość po migracji, nadal publiczna. |
| Pozostałość: `weryfikacja.nsz.com.pl` | odwołanie w `magazine-nsz/style.css`; host nie odpowiada | Wysoka | Prawdopodobnie dawne środowisko testowe [I]. |

**Wniosek [I]:** obecny system to klasyczny WordPress z motywem magazynowym z 2019 r., rozwijanym przez „Dodatkowy CSS” i shortcody. Archiwum i stara witryna to odrębne systemy — każdy wymaga własnego utrzymania i aktualizacji.

## 2. Weryfikacja w oficjalnej dokumentacji (dostęp 13.10.2026)

- **Wsparcie wersji WordPress** — „The only current officially supported version is the last major release of WordPress… Security updates are only backported to older branches as a courtesy. There is no guarantee and no timeframe.” — https://wordpress.org/documentation/article/supported-versions/ (aktualizacja 2026-01-07). Bieżące wydanie: **7.1.3** (https://api.wordpress.org/core/version-check/1.7/).
- **Motywy blokowe** — „Block themes are the modern method of building WordPress themes… Both creators and users can edit the templates in the Site Editor”; motywy klasyczne „still supported”. — https://developer.wordpress.org/themes/getting-started/what-is-a-theme/
- **REST API jako źródło dla frontendu** — „Any programming language which can make HTTP requests and interpret JSON can use the REST API to interact with WordPress” — https://developer.wordpress.org/rest-api/
- **Nie wyłączać REST, lecz ograniczać** — FAQ REST API: wyłączenie „will break WordPress Admin functionality”; zalecane wymaganie uwierzytelnienia przez filtr — https://developer.wordpress.org/rest-api/using-the-rest-api/frequently-asked-questions/
- **Role redakcyjne** (Administrator, Editor, Author, Contributor, Subscriber) — https://wordpress.org/documentation/article/roles-and-capabilities/ (aktualizacja 2026-09-02)
- **Headless z Astro** — REST API domyślnie publiczne; generowanie statyczne przez `getStaticPaths()`; CPT trzeba udostępnić w REST — https://docs.astro.build/en/guides/cms/wordpress/

## 3. Trzy scenariusze produkcyjne

| Kryterium | A. Modernizacja obecnego WP (News Portal + potomny) | **B. WordPress + lekki autorski motyw blokowy** | C. Headless WordPress + statyczny frontend (np. Astro) |
|---|---|---|---|
| Praca redakcji | bez zmian (znany edytor) | znany panel; nowe wzorce bloków i pola (autor, pierwodruk, źródła, sygnatura) | panel WP bez podglądu „na żywo” bez dodatkowej konfiguracji; publikacja = przebudowa strony (minuty) |
| Role | domyślne WP | domyślne WP + rola „Redaktor źródeł” (opcjonalnie) | jw. + uprawnienia do uruchamiania przebudowy |
| Model treści | ograniczony motywem (kategorie mieszają typy) | CPT: Aktualność, Materiał historyczny, Biogram, Dokument, Wydarzenie, Kalendarium; taksonomie: Formacja, Okręg, Miejsce, Okres | jak B (ten sam backend) |
| Wyszukiwanie | wbudowane WP (słabe) | wbudowane + filtry fasetowe (np. wtyczka lub własne zapytania); docelowo wspólny indeks z Archiwum | indeks statyczny (np. Pagefind) — szybki, bez serwera; wymaga przebudowy |
| Archiwum cyfrowe | osobno | osobno, wspólny nagłówek/stopka i odsyłacze; etap 2: wspólne wyszukiwanie | możliwe pobieranie danych z obu instalacji w jeden front |
| Bezpieczeństwo | wymaga natychmiastowych aktualizacji; stary motyw = dług | aktualny rdzeń, mniej wtyczek (bez Shortcodes Ultimate, Font Awesome x2) | najmniejsza powierzchnia ataku frontu (statyczne pliki), backend można ukryć |
| Utrzymanie | najtańsze teraz, najdroższe w dłuższym okresie | umiarkowane; standard WP | najwyższe: dwa systemy + pipeline build/deploy; wymaga developera |
| Migracja URL | brak | zachowanie permalinków `/%postname%/` i `/kategorie/…`; 301 dla zmienionych | jak B + mapowanie w generatorze |
| Wydajność | słaba (15 CSS, ~20 JS) | dobra przy lekkim motywie | bardzo dobra |
| Ryzyko wdrożenia | niskie | średnie | wysokie dla organizacji z wolontariacką redakcją [I] |

**Szacunki pracochłonności (założenia):** zespół 1 developer + 1 projektant, treści migruje się automatycznie (ta sama baza WP), redakcja Związku dostarcza decyzje i akceptacje w ciągu tygodnia; bez kosztów hostingu (nie podaję cen usług — wymagają aktualnego zapytania ofertowego).

| Scenariusz | Pracochłonność (osobodni) | Uwagi |
|---|---|---|
| A | 5–10 | aktualizacje, poprawki mobilne, porządek menu — bez zmiany modelu treści |
| B | 30–50 | motyw blokowy, CPT i pola, migracja kategorii → typy, przekierowania, szkolenie redakcji |
| C | 45–80 | jak B + frontend statyczny, pipeline, wyszukiwarka, podgląd publikacji |

## 4. Rekomendacja

**Etap 0 (natychmiast, niezależnie od redesignu):** kopia zapasowa, aktualizacja rdzenia WP na obu instalacjach na środowisku testowym, przegląd wtyczek, ograniczenie `/wp-json/wp/v2/users` dla anonimowych, decyzja co do starej witryny Joomla (statyczny zrzut lub wygaszenie z przekierowaniami).

**Rekomendowany scenariusz: B — WordPress z lekkim autorskim motywem blokowym.** Uzasadnienie: redakcja zna WordPressa; treści (1 518 wpisów, 5 543 media) zostają w tej samej bazie, więc migracja sprowadza się do przekształcenia taksonomii i szablonów; motyw blokowy pozwala zakodować komponenty z prototypów jako wzorce bloków; koszt utrzymania nie rośnie o drugi system. Scenariusz C ma sens dopiero, gdy pojawi się stały developer i potrzeba wspólnego frontu dla portalu i Archiwum.

**Prototypy z tego repozytorium** to statyczny HTML/CSS/JS na GitHub Pages — **nie są** rekomendowaną platformą produkcyjną, tylko materiałem do decyzji o kierunku wizualnym i modelu treści.

## 5. MVP i dalszy rozwój

**MVP (scenariusz B):**
1. Motyw blokowy z wybranym kierunkiem; szablony: strona główna, lista z filtrami, artykuł (spis treści, źródła, galeria), biogram, dokument, wydarzenie, kalendarium dnia.
2. Model treści: CPT + pola (autor/autorka, pierwodruk, źródła, sygnatura i zasób archiwalny, prawa do zdjęć, status weryfikacji).
3. Migracja: kategorie → typy treści i taksonomie; zachowanie dat publikacji i autorstwa (przeniesienie podpisów z końca tekstów do pól — półautomatycznie, z kontrolą redakcji).
4. Mapa przekierowań 301 dla ~2 860 adresów (posty, strony, kategorie, tagi) oraz uszkodzonych slugów; test 404 po wdrożeniu.
5. Dostępność WCAG 2.2 AA w szablonach; dane z banerów (1,5%, KRS) jako tekst.
6. Procedura publikacji: Autor → Redaktor (kontrola źródeł i praw do zdjęć) → publikacja; kopie zapasowe dzienne poza serwerem.

**Etap 2:** wspólne wyszukiwanie portal + Cyfrowe Archiwum; strony osób/miejsc łączące biogramy, dokumenty i wydarzenia; mapa miejsc pamięci; materiały dla nauczycieli; ewentualnie headless.

## 6. Mierniki sukcesu (powiązane z zadaniami czytelnika)

Bez danych bazowych nie obiecuję wzrostu ruchu. Proponowane mierniki (do zebrania przed i po wdrożeniu):
- **Odnalezienie materiału:** odsetek uczestników testu zadaniowego (5–8 osób, różne grupy wiekowe), którzy w < 60 s znajdą biogram wskazanej osoby.
- **Przejście do źródła:** odsetek odsłon artykułów historycznych z kliknięciem w źródło lub dokument w Archiwum.
- **Odnalezienie wydarzenia:** czas dotarcia z wejścia na stronę główną do daty i miejsca najbliższej uroczystości.
- **Wygodne czytanie:** wynik ankiety po lekturze + udział przewinięć artykułu > 75% (tylko przy analityce zgodnej z RODO, wdrożonej przez Związek).
- **Jakość redakcyjna:** odsetek nowych materiałów historycznych z wypełnionym polem „Źródła” i autorem.
