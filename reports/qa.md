# Wyniki testów (QA)

**Data:** 13.10.2026. **Środowisko:** Windows Server 2025 (1 vCPU), Google Chrome (headless) sterowany przez `playwright-core`, `axe-core` (reguły WCAG 2.0/2.1/2.2 A i AA), Lighthouse 12 (profil mobilny, domyślne dławienie).
**Adres badany:** opublikowany podgląd https://pflgroup.github.io/nsz-redesign-prototypes/ (ostatni przebieg 08:01 UTC) oraz lokalny serwer pod prefiksem `/nsz-redesign-prototypes/` (przebiegi robocze).
**Skrypt:** `tests/qa.mjs` — wyniki surowe w `work/qa/qa-results.json`, zrzuty w `work/qa/screens/` (poza repozytorium).

> Wynik automatu nie dowodzi pełnej zgodności z WCAG. Nie przeprowadzono testu z czytnikiem ekranu (NVDA/VoiceOver) ani badań z użytkownikami.

## 1. Zakres

- 5 wariantów × 3 widoki (strona główna, aktualności, artykuł) × 5 szerokości (360, 390, 768, 1280, 1440 px) = **75 pomiarów stron** + selektor (390, 1440).
- Na każdym pomiarze: przewijanie poziome, błędy konsoli i JS, nieudane zasoby, zapytania do domen zewnętrznych, axe, liczba `h1`, przeskoki poziomów nagłówków, obrazy bez `alt`, link „Przejdź do treści”, baner prototypu, `noindex`.
- Interakcje (390 px): otwarcie menu i zamknięcie klawiszem Esc, pierwszy Tab, widoczny fokus, wyszukiwarka → stan pusty → „wyczyść”, filtr kategorii, parametr `?q=` w adresie, galeria (przycisk + strzałki klawiatury), spis treści, pasek postępu, wszystkie linki wewnętrzne (HTTP), widoczność treści **bez JavaScriptu**, `prefers-reduced-motion`, tekst powiększony 200%.
- Zrzuty 390 i 1440 px każdego widoku obejrzane przez zespół.

## 2. Wyniki automatyczne (podgląd opublikowany)

| Kontrola | A | B | C | D | E |
|---|---|---|---|---|---|
| Przewijanie poziome (360–1440 px) | brak | brak | brak | brak | brak |
| Naruszenia axe | 0 | 0 | 0 | 0 | 0 |
| Błędy konsoli / JS | 0 | 0 | 0 | 0 | 0 |
| Nieudane zasoby | 0 | 0 | 0 | 0 | 0 |
| Zapytania zewnętrzne | 0 | 0 | 0 | 0 | 0 |
| Martwe linki wewnętrzne | 0 / 32 | 0 / 29 | 0 / 33 | 0 / 23 | 0 / 18 |
| `h1` na stronę / przeskoki nagłówków | 1 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | 1 / 0 |
| Menu: otwiera / Esc zamyka | tak / tak | tak / tak | tak / tak | tak / tak | tak / tak |
| Pierwszy Tab = „Przejdź do treści”, fokus widoczny | tak | tak | tak | tak | tak |
| Stan pusty + „wyczyść” | tak | tak | tak | tak | tak |
| `?q=Holisz` → wynik | 1 | 1 | 1 | 1 | 1 |
| Galeria: przycisk / klawiatura | tak / tak | tak / tak | tak / tak | tak / tak | tak / tak |
| Lista materiałów bez JS | 8 / 8 | 9 / 9 | 8 / 8 | 8 / 8 | 9 / 9 |
| `prefers-reduced-motion` respektowane | tak | tak | tak | tak | tak |
| Elementy interaktywne < 24 px (maks. na stronę) | 2 | 1 | 0 | 0 | 5 |
| Przewijanie przy tekście 200% (390 px) | +157 px | 0 | 0 | +140 px | +46 px |

Selektor: 0 naruszeń axe, 0 błędów, brak przewijania poziomego.

## 3. Lighthouse (mobile, podgląd opublikowany)

| Strona | Wydajność | Dostępność | Najl. praktyki | SEO* | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| Selektor | 100 | 100 | 100 | 63 | 1,3 s | 0 | 0 ms |
| A — strona główna | 88 | 100 | 100 | 60 | 1,7 s | 0,01 | 450 ms |
| A — artykuł | 91 | 99 | 100 | 60 | 1,8 s | 0,001 | 360 ms |
| B — strona główna | 94 | 100 | 100 | 60 | 2,1 s | 0 | 140 ms |
| C — strona główna | 88 | 100 | 100 | 60 | 2,5 s | 0 | 250 ms |
| C — aktualności | 95 | 100 | 100 | 60 | 2,0 s | 0 | 100 ms |
| D — strona główna | 94 | 100 | 100 | 60 | 1,7 s | 0,048 | 250 ms |
| E — strona główna | 69–97** | 100 | 100 | 63 | 1,8–4,0 s | 0–0,008 | 160–470 ms |

\* SEO obniża celowe `noindex, nofollow` — to oczekiwane w prototypie.
\*\* Dwa kolejne przebiegi tej samej wersji dały 69 i 97 pkt. Serwer testowy ma 1 vCPU, więc TBT i LCP są obarczone dużym szumem; wyniki traktować orientacyjnie. Cel projektowy (≈ 90 wydajności, ≈ 95 dostępności) osiągnięty dla dostępności we wszystkich stronach; dla wydajności — w B, D, C-aktualności, A-artykuł i selektorze, a A i C (88) są tuż poniżej.

## 4. Błędy znalezione i poprawione w trakcie testów

| Problem | Gdzie | Poprawka |
|---|---|---|
| CLS 0,38–0,98: panele nagłówka (menu, wyszukiwarka, indeks) widoczne do załadowania skryptów, potem zwijane | wszystkie warianty | krótki skrypt przed `<main>` ustawia od razu ten sam stan co `proto.js`; bez JS panele pozostają rozwinięte → CLS 0–0,05 |
| CLS 0,168: podmiana kroju etykiet w hero | E | `aspect-ratio` obrazów, `font-display: optional` dla IBM Plex Mono → CLS 0–0,008 |
| Esc nie zamykał menu, gdy fokus był na przycisku | wspólny `proto.js` | obsługa Esc na poziomie dokumentu |
| Wyszukiwarka nie znajdowała form odmienionych („Kamesznica” ≠ „Kamesznicy”) | wspólny `proto.js` | dopasowanie po rdzeniu słowa |
| Brak `h1`, niezgodność etykiety marki, `<ul>` z elementami o innej roli | C | poprawione przez autora wariantu |
| Przeskok poziomu nagłówka w karcie eksploratora, za mały odnośnik stały | B | `h2` w karcie, odnośnik min. 24 px |
| 404 na `favicon.ico` w konsoli | wszystkie | `<link rel="icon" href="data:,">` |
| Linki w stopkach i listach źródeł 16–22 px wysokości | A, B, D, E | wspólna reguła min. 24 px (`a11y.css`) |

## 5. Znane ograniczenia (otwarte)

1. **Tekst powiększony 200% przy 390 px** powoduje przewijanie poziome w A (+157 px), D (+140 px) i E (+46 px). Test jest ostrzejszy niż wymóg WCAG 1.4.10 (reflow przy 320 CSS px — przy 360 px brak przewijania), ale w produkcji należy zastąpić stałe szerokości elementów nagłówka jednostkami względnymi. Priorytet P1.
2. **Cele dotykowe < 24 px** w kilku linkach w treści (A: 2, B: 1, E: 5, m.in. „Zobacz rozdział 04” 14 px w E). axe ich nie zgłasza (wyjątek odstępu WCAG 2.5.8), ale nie spełniają projektowego celu 44 px. P2.
3. **Brak testu czytnikiem ekranu** i testów na fizycznych urządzeniach (iOS Safari, Android Chrome) — tylko emulacja w Chrome. P1 przed wdrożeniem.
4. **Eksplorator B** ma złożoną interakcję (zakładki + graf + lista); wymaga sprawdzenia z czytnikiem ekranu i użytkownikami.
5. **Pomiary Lighthouse** na 1 vCPU — powtórzyć na stabilnej maszynie lub przez PageSpeed Insights.
6. Ocena oznaczeń trudnych wątków historii (sformułowania, kontekst) wymaga recenzji historyka spoza zespołu.
