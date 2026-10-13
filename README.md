# NSZ — audyt serwisu i pięć prototypów strony

Studium modernizacji serwisu [nsz.com.pl](https://www.nsz.com.pl/) (Związek Żołnierzy Narodowych Sił Zbrojnych): audyt obecnej witryny i CMS-u, rys historyczny z rejestrem źródeł, benchmarki oraz pięć działających prototypów HTML/CSS/JS.

> **Prototyp koncepcyjny — nie jest oficjalnym serwisem.** Repozytorium nie jest powiązane ze Związkiem Żołnierzy NSZ. Tytuły, daty i adresy materiałów pochodzą z nsz.com.pl; zajawki i tekst przykładowego artykułu przygotowano na potrzeby prototypu. Zdjęcia i logo zastąpiono oznaczonymi miejscami, bo prawa do ich ponownej publikacji nie zostały potwierdzone.

**Podgląd:** https://pflgroup.github.io/nsz-redesign-prototypes/

| Wariant | Katalog | Charakter |
|---|---|---|
| A · Instytucja 2.0 | `public/01-nowoczesny/` | nowoczesny portal redakcyjny, indeks tematów |
| B · Żywe Archiwum | `public/02-ultranowoczesny/` | eksplorator czas / miejsca / ludzie / dokumenty |
| C · Kronika Niepodległości | `public/03-tradycyjny/` | tradycyjny układ gazetowy, rozkładówka numeru |
| D · Dziedzictwo i Wspólnota | `public/04-dziedzictwo/` | ścieżki „człowiek — miejsce — źródło — pamięć” |
| E · Archiwum Awangardowe | `public/05-awangardowy/` | plakatowa typografia, montaż edytorski |

Każdy wariant zawiera co najmniej: `index.html` (strona główna), `aktualnosci.html` (lista z filtrami i wyszukiwarką, parametry `?q=` i `?kat=`) oraz `artykul.html` (artykuł z galerią, spisem treści i źródłami). Opis decyzji: `NOTES.md` w katalogu wariantu.

## Raporty

| Plik | Zawartość |
|---|---|
| [`reports/audit.md`](reports/audit.md) | audyt serwisu: struktura, inwentaryzacja, problemy P0–P2, identyfikacja |
| [`reports/cms-recommendation.md`](reports/cms-recommendation.md) | identyfikacja CMS (dowody, pewność), 3 scenariusze, MVP, migracja |
| [`reports/history-and-ideology.md`](reports/history-and-ideology.md) | rys historyczny i ideowy, oś czasu, spory, bibliografia |
| [`reports/sources.csv`](reports/sources.csv) | rejestr twierdzeń: źródło, rodzaj, stopień potwierdzenia, zastrzeżenia |
| [`reports/benchmarks.md`](reports/benchmarks.md) | 16 serwisów instytucji i redakcji, wzorce, odrzucone schematy |
| [`reports/design-comparison.md`](reports/design-comparison.md) | macierz odrębności 10 par, oceny, rekomendacja |
| [`reports/qa.md`](reports/qa.md) | wyniki testów (szerokości, axe, klawiatura, Lighthouse) |
| [`reports/assets-register.md`](reports/assets-register.md) | rejestr zasobów, licencje, plan podmiany placeholderów |
| [`reports/deployment.md`](reports/deployment.md) | publikacja na GitHub Pages i jej weryfikacja |

## Uruchomienie lokalne

Prototypy są statyczne, ale wymagają serwera HTTP (fonty nie ładują się z `file://`):

```bash
cd public
python -m http.server 8000
# otwórz http://localhost:8000/
```

Wszystkie ścieżki są względne, więc strona działa zarówno w katalogu głównym, jak i pod prefiksem `/nsz-redesign-prototypes/`.

## Testy

```bash
cd tests
npm install            # playwright-core, axe-core
cd ..
node tests/qa.mjs                    # lokalnie, serwer pod prefiksem /nsz-redesign-prototypes/
node tests/qa.mjs --base=https://pflgroup.github.io/nsz-redesign-prototypes/   # na opublikowanym podglądzie
```

Skrypt używa zainstalowanego Google Chrome (`C:/Program Files/Google/Chrome/Application/chrome.exe`; zmień ścieżkę w `tests/qa.mjs` na innym systemie). Wyniki trafiają do `work/qa/`.

## Struktura

```
public/          # jedyny katalog publikowany na GitHub Pages
  index.html     # selektor pięciu wariantów
  assets/        # dane (content.js), wspólne helpery zachowań i dostępności, miniatury
  01-…05-…/      # warianty: własny HTML, CSS, fonty (SIL OFL), NOTES.md
reports/         # raporty i rejestry
tests/           # testy Playwright + axe
work/            # materiały robocze (skrypty generujące, wyciągi dla projektantów)
.github/workflows/pages.yml   # publikacja katalogu public/
```

## Zasady

- Bez analityki, ciasteczek, zewnętrznych CDN i fontów z serwerów trzecich.
- `noindex, nofollow` na każdej stronie (to nie jest zabezpieczenie dostępu).
- Formularze są demonstracyjne — nie wysyłają ani nie zapisują danych.
- Trudne i sporne wątki historii NSZ są oznaczone i odesłane do źródeł; nazwy kierunków opisują kontekst i estetykę, nie program polityczny.
