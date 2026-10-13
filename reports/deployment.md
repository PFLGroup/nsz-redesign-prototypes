# Publikacja (GitHub Pages)

Stan na 13.10.2026.

| Etap | Status | Dowód |
|---|---|---|
| Repozytorium utworzone | ✅ | https://github.com/PFLGroup/nsz-redesign-prototypes (publiczne, konto PFLGroup) |
| Kod wypchnięty | ✅ | gałąź `main` |
| Wdrożenie uruchomione | ✅ | GitHub Pages, źródło: gałąź `gh-pages`, katalog `/` |
| Wdrożenie zakończone | ✅ | API `pages/builds/latest` → `built` |
| Podgląd zweryfikowany | ✅ | HTTP 200 dla selektora, 5 wariantów, podstron, skryptów, fontów i miniatur; pełne QA i Lighthouse na adresie publicznym (`reports/qa.md`) |

## Adresy

- Selektor: https://pflgroup.github.io/nsz-redesign-prototypes/
- A · Instytucja 2.0: https://pflgroup.github.io/nsz-redesign-prototypes/01-nowoczesny/
- B · Żywe Archiwum: https://pflgroup.github.io/nsz-redesign-prototypes/02-ultranowoczesny/
- C · Kronika Niepodległości: https://pflgroup.github.io/nsz-redesign-prototypes/03-tradycyjny/
- D · Dziedzictwo i Wspólnota: https://pflgroup.github.io/nsz-redesign-prototypes/04-dziedzictwo/
- E · Archiwum Awangardowe: https://pflgroup.github.io/nsz-redesign-prototypes/05-awangardowy/

## Sposób publikacji

Publikowany jest **wyłącznie katalog `public/`**. Gałąź `gh-pages` powstaje z niego poleceniem:

```bash
git subtree split --prefix public -b gh-pages
git push origin gh-pages
```

Pierwotnie przewidziano publikację przez GitHub Actions (`work/ci/pages.yml.example`). Token CLI użyty do publikacji nie miał zakresu `workflow`, więc GitHub odrzucił wypchnięcie pliku w `.github/workflows/`. Zamiast prosić o rozszerzenie uprawnień, zastosowano publikację z gałęzi. Aby przejść na Actions: `gh auth refresh -s workflow`, przenieść plik do `.github/workflows/pages.yml` i w ustawieniach Pages wybrać „GitHub Actions”.

## Kontrole przed publikacją

- Skan sekretów (tokeny GitHub/OpenAI/AWS, klucze prywatne, `password=`, `api_key=`) — brak trafień.
- Adresy e-mail — brak w postaci jawnej; adresy organizacji zapisane jako `[at]`, tak jak w źródle.
- Dane osobowe — tylko publiczne dane rejestrowe organizacji (KRS, NIP, REGON, adres) oraz nazwiska historyków i postaci historycznych ze źródeł.
- Zrzuty cudzych serwisów (benchmarki, obecny nsz.com.pl) i pobrane HTML **wyłączone z repozytorium** (`.gitignore`).
- Licencje: fonty SIL OFL 1.1 z plikami licencji; brak zdjęć i logo z prawami nieustalonymi (`reports/assets-register.md`).
- Każda strona: baner „Prototyp koncepcyjny — nie jest oficjalnym serwisem”, `noindex, nofollow`, brak analityki i ciasteczek.

## Czego nie zrobiono

- Nie zmieniano istniejącej strony nsz.com.pl, jej DNS ani innych repozytoriów.
- Nie wykonywano `force push`.
- Nie skonfigurowano własnej domeny.
