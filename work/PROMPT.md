# PROMPT WYKONAWCZY: NSZ — audyt, historia, pięć prototypów i GitHub Pages

## 1. Rola i rezultat

Działaj jako kierownik interdyscyplinarnego zespołu: historyk, badacz źródeł, strateg marki, projektant UX/UI, dyrektor artystyczny, frontend developer, specjalista CMS oraz tester dostępności i wydajności.

Przeanalizuj serwis https://www.nsz.com.pl/ i opracuj modernizację jego strony głównej oraz najważniejszych ścieżek korzystania z treści. Dostarcz pięć wyraźnie różnych, działających prototypów HTML/CSS/JavaScript, dokumentację decyzji oraz publiczny podgląd przez GitHub Pages, jeżeli środowisko zapewnia właściwe uprawnienia.

Nie zatrzymuj się na opisie pomysłów, moodboardzie, jednym projekcie z pięcioma paletami ani kodzie w odpowiedzi. Rezultatem mają być rzeczywiste pliki, przetestowane interakcje i — po udanym wdrożeniu — zweryfikowane linki.

Traktuj przedsięwzięcie jako projekt historyczno-edukacyjny i instytucjonalny. Strona ma ułatwiać poznawanie historii, odnajdywanie źródeł i dostęp do aktualnej działalności organizacji. Projektuj dla użytkowników o różnym wieku, sprawności i doświadczeniu cyfrowym, bez profilowania przekazu ideologicznego według wieku, religii lub poglądów.

Język materiałów, interfejsu i dokumentacji: polski. Zachowaj poprawne polskie znaki. Aktualność informacji określaj według rzeczywistej daty wykonania zadania, nie daty zapisanej w przykładzie.

## 2. Organizacja pracy i agenci

Najpierw sprawdź faktycznie dostępne narzędzia: przeglądarka, wyszukiwanie, terminal, pliki, generowanie lub edycja grafik, testy przeglądarkowe i integracja GitHub. Nie deklaruj wykorzystania narzędzi, których nie uruchomiłeś.

Jeżeli środowisko obsługuje subagentów, rozdziel zadania pomiędzy następujące role:

- **Badacz historii:** chronologia, idee, organizacje, krytyka źródeł, spory historiograficzne.
- **Audytor serwisu i CMS:** struktura witryny, treści, identyfikacja technologii, ograniczenia migracji.
- **Badacz UX i benchmarków:** aktualne wzorce portali instytucjonalnych, rzadziej spotykane rozwiązania i dostępność.
- **Dyrektor artystyczny:** pięć niezależnych kierunków, systemy wizualne, typografia, autorskie kompozycje.
- **Frontend developer:** działające widoki, interakcje, responsywność, przygotowanie wdrożenia.
- **Recenzent QA:** kontrola źródeł, odrębności projektów, użyteczności, dostępności i jakości kodu.

Koordynuj pracę przez wspólny rejestr ustaleń. Badania historii i technologii mogą przebiegać równolegle; implementacja musi korzystać ze zweryfikowanych danych. Każdy kierunek wizualny opracuj początkowo niezależnie, a następnie porównaj całą piątkę.

Jeżeli subagenci nie są dostępni, wykonaj te role kolejno. Nie przedstawiaj podziału własnej pracy jako rzeczywistego uruchomienia niezależnych agentów.

## 3. Zasady dowodowe i zakres audytu

Oddzielaj: **ustalenie potwierdzone**, **interpretację**, **hipotezę projektową**, **informację niezweryfikowaną**. Przy ważnych ustaleniach podawaj źródło, adres, datę dostępu i krótki opis dowodu. Nie wymyślaj statystyk ruchu, badań użytkowników, wyników testów, wersji oprogramowania ani rezultatów wdrożenia.

Dąż do pełnej inwentaryzacji dostępnych publicznie adresów serwisu: nawigacji, map witryny, kategorii, paginacji, artykułów i zasobów. Szczegółowo zbadaj wszystkie główne sekcje oraz każdy odmienny typ podstrony. Gdy liczba artykułów uniemożliwia przeczytanie całego archiwum, dobierz próbę według kategorii, okresu publikacji i typu materiału. Wszystkie teksty faktycznie wykorzystane w rysie historycznym przeczytaj, a nie tylko ich fragmenty w wyszukiwarce.

Zapisz liczbę odkrytych adresów, odczytanych stron, przeanalizowanych typów widoków oraz pominiętych lub niedostępnych zasobów. Nie nazywaj analizy próby „przeczytaniem całej strony”.

Przy błędach 403, blokadzie automatycznego odczytu lub niedostępności zasobów nie obchodź zabezpieczeń. Wykorzystaj legalnie dostępne wyniki wyszukiwania i materiały archiwalne, oznaczając ich datę i ograniczenia. Kontynuuj prace możliwe do wykonania, ale nie wyciągaj wniosków o aktualnym wyglądzie, kolorach lub CMS-ie wyłącznie ze starych kopii.

## 4. Audyt obecnej witryny

Ustal, jaki podmiot prowadzi serwis, jakie deklaruje cele, jakie ma sekcje i jak odróżnia historię NSZ od bieżącej działalności organizacji upamiętniającej. Sprawdź również powiązane projekty, w tym Cyfrowe Archiwum NSZ, ale traktuj subdomeny jako osobne systemy do czasu potwierdzenia ich integracji.

Zbadaj stronę główną, menu, wyszukiwarkę, aktualności, artykuły, materiały historyczne, biogramy, publikacje, multimedia, wydarzenia, informacje organizacyjne, kontakt i stopkę — o ile faktycznie występują. Oddziel elementy istniejące od proponowanych.

Oceń hierarchię informacji, pierwszy ekran, długość strony, czytelność tytułów, datowanie materiałów, gęstość treści, nawigację mobilną, konsekwencję przycisków oraz drogę od aktualności do powiązanego materiału historycznego. Sprawdź, czy użytkownik rozumie, gdzie jest i co może zrobić dalej.

Przygotuj inwentaryzację logo, symboli, fotografii, ilustracji, krojów pisma, kolorów, ikon i proporcji. Kolory odczytuj z CSS lub wiarygodnych plików graficznych; podaj HEX i rolę. Jeżeli nie da się ich potwierdzić, nie przedstawiaj palety projektowej jako obecnej identyfikacji.

Dla każdego problemu zapisz: obserwację, dowód lub zrzut ekranu, konsekwencję dla użytkownika, rekomendację i priorytet P0/P1/P2. Oceń także zasoby warte zachowania, a nie tylko słabości.

## 5. Rzetelna identyfikacja CMS-u

Nie zakładaj WordPressa, Joomli ani systemu autorskiego. Sprawdź publiczne, pasywne oznaki technologii: HTML, metadane generatora, ścieżki zasobów, nagłówki odpowiedzi, publicznie ujawnione endpointy i strukturę adresów. Nie wykonuj testów penetracyjnych ani prób logowania.

Wynik przedstaw jako: **technologia — dowody — poziom pewności — ograniczenia**. Odróżnij obecny system od pozostałości po migracji. Same pliki z charakterystycznym katalogiem nie zawsze dowodzą działania aktualnego backendu. Wersję CMS-u lub nazwę motywu podaj tylko po uzyskaniu bezpośredniego dowodu.

Porównaj trzy scenariusze produkcyjne: modernizację na obecnym CMS-ie, WordPress z lekkim autorskim motywem blokowym oraz rozwiązanie headless ze statycznie generowanym frontendem. Inny system dodaj tylko z konkretnym uzasadnieniem. Zweryfikuj bieżące możliwości w oficjalnej dokumentacji.

Uwzględnij codzienną pracę redakcji, role użytkowników, archiwum treści, galerie, aktualności, bezpieczeństwo, utrzymanie, wyszukiwanie, koszty i migrację URL-i. Wyraźnie oddziel platformę prototypów od rekomendowanego systemu produkcyjnego. Wybór technologii ma wynikać z potrzeb, nie z efektowności jej nazwy.

## 6. Rys historyczny i ideologiczny

Przygotuj samodzielny raport historyczny, orientacyjnie 1500–2500 słów, uzupełniony osią czasu i bibliografią. Zbadaj genezę NSZ, kontekst okupacji, struktury, dowództwo, działalność, relacje z innymi organizacjami podziemnymi, podziały, losy powojenne i późniejsze upamiętnianie.

Precyzyjnie rozróżniaj organizacje, frakcje, okresy i osoby. Sprawdź zakres używania nazw NSZ, NSZ-AK, NSZ-ZJ, NOW i NZW oraz ich wzajemne relacje; nie stosuj tych nazw zamiennie. Zbadaj związki z właściwymi nurtami przedwojennego ruchu narodowego, Stronnictwem Narodowym i środowiskiem określanym jako Grupa Szańca. Każdą relację opisz na podstawie źródeł, bez automatycznego utożsamiania całych środowisk.

W części ideowej przeanalizuj rozumienie narodu, państwa, suwerenności, katolicyzmu, antykomunizmu, porządku społecznego i gospodarczego, demokracji oraz stosunku do mniejszości. Ustal, które stanowiska były wspólne, a które właściwe konkretnemu środowisku lub okresowi.

Nie pomijaj trudnych zagadnień: relacji z AK, ludnością cywilną, Żydami i innymi mniejszościami, udokumentowanych przypadków przemocy oraz sporów dotyczących Brygady Świętokrzyskiej i kontaktów z niemieckimi strukturami. Badaj konkretne zdarzenia, jednostki i odpowiedzialność. Nie przenoś automatycznie ocen jednostkowego wydarzenia na wszystkich żołnierzy ani nie pomijaj dowodów niepasujących do założonej narracji.

Wykorzystaj materiały samego serwisu jako źródło jego autoprezentacji, a nie jako jedyną podstawę rekonstrukcji historii. Szukaj także dokumentów epoki, opracowań naukowych, archiwów oraz publikacji instytucji badawczych i muzealnych. Dąż do co najmniej ośmiu wartościowych pozycji reprezentujących minimum trzy niezależne instytucje lub zespoły badawcze. Liczba źródeł nie zastępuje ich jakości.

Rozbieżności opisuj wraz z argumentami i oceną podstaw źródłowych. Nie przedstawiaj każdej opinii jako równie wiarygodnej. Nie wymyślaj cytatów, fotografii dokumentalnych, dat, biografii ani przypisów. Dla istotnych twierdzeń przygotuj rejestr: twierdzenie — źródło — rodzaj źródła — stopień potwierdzenia — zastrzeżenia.

## 7. Historia, identyfikacja i współczesne korzystanie z treści

Przełóż ustalenia na zasady projektowe. Określ, które symbole są autentycznie związane z badaną organizacją, które należą do dzisiejszego podmiotu, a które są tylko nową propozycją estetyczną. Zachowaj integralność istniejącego logo i nie dopisuj symbolom niepotwierdzonych znaczeń.

Połącz historię ze współczesnością przez dostęp do źródeł, cyfrowe archiwum, biogramy, mapy, wywiady, materiały dla nauczycieli, relacje z wydarzeń i dłuższe artykuły. Nie dopisuj organizacji dzisiejszego programu politycznego.

Użytkownika początkującego prowadź do zwięzłego wprowadzenia, a zainteresowanego szczegółami do dokumentów i bibliografii. Nie buduj osobnych wersji ideologicznego przekazu dla młodszych i starszych odbiorców. Różnicuj poziom szczegółowości i formę dostępu, nie manipulacyjny przekaz.

Nazwy nurtów ideowych w poniższych wariantach określają kontekst historyczny i kierunek estetyczny, nie zadanie tworzenia współczesnej agitacji, rekrutacji politycznej, nienawiści czy gloryfikacji przemocy.

## 8. Benchmarki i poszukiwanie oryginalności

Przeanalizuj 12–18 działających serwisów: instytucji kultury, muzeów, archiwów, fundacji, organizacji społecznych i portali redakcyjnych. Przynajmniej połowa próby ma dotyczyć instytucji lub organizacji, a nie sklepów, SaaS-ów i portfolio agencji.

Dla każdej inspiracji zapisz adres, datę oględzin, konkretny wzorzec, jego zastosowanie w projekcie NSZ oraz ryzyko dla dostępności lub wydajności. Podgląd graficzny wykorzystuj wtedy, gdy rzeczywiście możesz go obejrzeć. Nagroda lub obecność w galerii designu nie jest sama w sobie dowodem użyteczności.

Szukaj mniej oczywistych rozwiązań: indeksów redakcyjnych, nawigacji inspirowanej katalogiem archiwalnym, osi czasu zespolonej z treścią, powiązań osoba–miejsce–dokument, przypisów na marginesie i kontrolowanego ruchu typograficznego. Nie kopiuj całych kompozycji ani płatnych szablonów.

Częstotliwość wzorca oceniaj wyłącznie w zbadanej próbie. Zamiast „nikt tego nie używa” napisz „wystąpiło w 2 z 15 przeanalizowanych serwisów”. Jeżeli nie potrafisz zmierzyć rozpowszechnienia, nazwij ocenę hipotezą projektową.

Przygotuj krótką listę odrzuconych schematów z uzasadnieniem: przypadkowa siatka identycznych kart, automatyczny wielki slider, generyczny układ agencyjny, nadmiar gradientów, ozdobny interfejs utrudniający czytanie. Nie zakazuj użytecznego elementu tylko dlatego, że jest popularny.

## 9. Pięć odrębnych kierunków

Połącz określenia „tradycyjny” i „tradycjonalistyczny” w jeden wariant, aby powstało dokładnie pięć koncepcji. Poniższe palety są propozycjami projektowymi, nie deklaracją obecnych barw serwisu. Po audycie dopasuj je do potwierdzonej identyfikacji, prawidłowego użycia logo i kontrastu.

### A. „Instytucja 2.0” — nowoczesny portal redakcyjny

Biel lub ciepła biel, grafit i oszczędny karmin. Wyrazista typografia bezszeryfowa, asymetryczna kompozycja redakcyjna, mocny temat dnia i aktualności widoczne bez szukania. Pierwszy ekran ma przypominać autorsko zaprojektowany portal instytucji, nie landing page produktu.

Nawigacja: przejrzyste menu z panelem rozwijanym, wyszukiwanie i szybkie przejścia do historii, aktualności i archiwum. Element charakterystyczny: redakcyjny indeks tematów łączący bieżący materiał z kontekstem historycznym. Ruch: krótkie przejścia, delikatna reakcja ikon i czytelne zmiany stanu.

### B. „Żywe Archiwum” — ultranowoczesna eksploracja

Atramentowy granat, jasna typografia i punktowe akcenty czerwieni; zapewnij spokojny, jasny widok dłuższego tekstu. Pierwszy ekran oparty na interaktywnym wyborze „czas / miejsca / ludzie / dokumenty”, a nie na kolejnym banerze fotograficznym.

Element charakterystyczny: eksplorator powiązań lub interaktywna oś czasu z równoważnym widokiem listy. Zademonstruj działające filtrowanie na małym, zweryfikowanym zbiorze. Wrażenie nowoczesności buduj kompozycją i płynną zmianą kontekstu, nie ciężkim 3D. Nie stylizuj portalu na grę wojenną ani panel dowodzenia.

### C. „Kronika Niepodległości” — tradycyjny i tradycjonalistyczny

Ciepłe papierowe tło, czerń, burgund i dyskretny kolor archiwalnej fotografii. Szeryfowe nagłówki, uporządkowany układ gazetowy, cienkie linie, staranne podpisy i wyraźne daty. Bez sztucznie postarzanych tekstur utrudniających czytanie.

Nawigacja: indeks działów i zwarta lista tematów. Element charakterystyczny: cyfrowy numer kroniki lub rozkładówka z aktualnościami, dokumentem i komentarzem historycznym. Animacja ograniczona do rozwijania materiałów i przejść galerii. Tradycyjny charakter nie może oznaczać przestarzałej obsługi na telefonie.

### D. „Dziedzictwo i Wspólnota” — katolicko-narodowy kontekst dziedzictwa

Jasne, kamienne tło, ciemna zieleń lub bordo i niewielki akcent przygaszonego złota. Spokojna kompozycja, dużo przestrzeni i zestawienie eleganckiego kroju szeryfowego z czytelnym krojem użytkowym.

Treści oprzyj na udokumentowanych wątkach religijnych, kapelanach, biografiach, pamięci, miejscach i współczesnych działaniach edukacyjnych. Bez dopisywania haseł ideologicznych. Pierwszy ekran: jedna opowieść lub fotografia z kontekstem, obok czytelna ścieżka do aktualności. Element charakterystyczny: ścieżki tematyczne „człowiek — miejsce — źródło — pamięć”. Unikaj dosłownego szablonu parafialnego i nadmiaru ornamentu.

### E. „Archiwum Awangardowe” — radykalna forma graficzna, historyczny kontekst narodowo-radykalny

Czerń, złamana biel i precyzyjnie dozowana czerwień. Mocna typografia, kontrolowana asymetria, monumentalne numery rozdziałów, odwołania do historycznego druku i plakatu wyłącznie po sprawdzeniu ich adekwatności.

Radykalność ma dotyczyć kompozycji, nie agresywnego przekazu. Wątki narodowo-radykalne przedstawiaj analitycznie, z kontekstem i źródłami. Nie twórz estetyki współczesnej rekrutacji ekstremistycznej ani nie przenoś bez komentarza haseł propagandowych.

Nawigacja: typograficzny spis rozdziałów i wysuwany indeks. Element charakterystyczny: edytorski montaż tytułu, dokumentu, daty i fotografii, z dostępnym odsłanianiem materiałów. Mimo ekspresyjnej formy aktualności, menu i artykuły muszą być łatwe do znalezienia.

## 10. Warunek rzeczywistej odrębności

Każda para wariantów musi różnić się co najmniej pięcioma z ośmiu obszarów: pierwszym ekranem, strukturą nawigacji, kompozycją aktualności, typografią, użyciem fotografii, sposobem eksplorowania historii, językiem animacji i układem artykułu.

Przygotuj macierz porównania i oceń wszystkie dziesięć par. Jeżeli różnice sprowadzają się do kolorów i kroju pisma, przeprojektuj słabszy wariant przed zakończeniem.

Możesz współdzielić dane, funkcje pomocnicze i sprawdzone komponenty dostępności. Nie współdziel jednego szkieletu strony głównej, który ukryjesz pod pięcioma motywami CSS.

## 11. Wspólna architektura informacji i zakres widoków

Zaproponuj docelową mapę treści na podstawie audytu. Punktem wyjścia mogą być: Aktualności, Historia, Ludzie, Archiwum, Multimedia, Wydarzenia, Organizacja i Kontakt. Nie wciskaj wszystkich działów do jednego poziomu menu.

Każdy prototyp ma zawierać minimum trzy dopracowane widoki: stronę główną, listę aktualności z filtrowaniem oraz przykładowy artykuł z galerią lub sliderem. Interaktywny moduł historyczny może znajdować się na stronie głównej lub w dodatkowym widoku.

Strona główna powinna pokazać tożsamość podmiotu, aktualności, wejście w historię, wyróżniony materiał źródłowy, biogram lub dokument, wydarzenia albo multimedia oraz informację organizacyjną. Komponuj te treści inaczej w każdym wariancie; nie twórz pięciu identycznych układów sekcji.

Artykuł ma mieć tytuł, datę, rzeczywiste autorstwo lub oznaczenie jego braku, wprowadzenie, śródtytuły, źródła, podpisy zdjęć, powiązane materiały i czytelną nawigację powrotną. Dla dłuższego tekstu dodaj spis treści i opcjonalny wskaźnik postępu czytania.

Użyj wspólnego zestawu 6–8 zweryfikowanych materiałów do porównania projektów. Pisz własne krótkie zajawki zamiast kopiować całe artykuły. Materiały demonstracyjne, skróty redakcyjne i nieprawdziwe dane testowe wyraźnie oznaczaj; nie wymyślaj aktualnych wydarzeń, wypowiedzi ani organizacyjnych osiągnięć.

## 12. Interakcje, ruch i dostępność

Zaimplementuj działające menu mobilne, wyszukiwarkę lokalnego zestawu treści, filtry kategorii, nawigację pomiędzy widokami, galerię artykułu i charakterystyczną interakcję każdego wariantu. Dla filtrów zapewnij stan pusty i możliwość ich wyczyszczenia.

Ruch ikon, pojawianie się elementów i przesuwanie slajdów mają wspierać orientację. Zaproponuj spójne czasy mikrointerakcji, przykładowo 120–300 ms, i uzasadnij większe odstępstwa. Nie animuj wszystkiego jednocześnie.

Projektuj według aktualnych zaleceń WCAG na poziomie AA. Zapewnij semantyczny HTML, prawidłową kolejność nagłówków, widoczny fokus, obsługę klawiaturą, link pomijający nawigację, kontrast, teksty alternatywne i etykiety formularzy. Przyjmij wygodny projektowy cel pól dotykowych około 44 × 44 px lub większych.

Obsłuż `prefers-reduced-motion` i umożliw ograniczenie animacji. Slider domyślnie nie powinien sam zmieniać czytanego materiału; przy automatycznym odtwarzaniu dodaj wyraźną pauzę i właściwe zachowanie po interakcji. Zapewnij przyciski, klawiaturę, czytelne etykiety i logiczny fokus. Gest przeciągania nie może być jedyną metodą obsługi.

Nie stosuj scrolljackingu, wymuszonego poziomego przewijania całej strony, migotania, automatycznego dźwięku, długiego intro, konieczności używania niestandardowego kursora ani podstawowej nawigacji ukrytej wyłącznie pod hoverem. Użytkownik ma kontrolować tempo poznawania materiału.

## 13. Implementacja i struktura repozytorium

Preferuj HTML, CSS i niewielki JavaScript bez rozbudowanego procesu budowania. Możesz użyć generatora statycznego, gdy daje wymierną korzyść; finalny rezultat musi nadawać się do hostowania statycznego. Dokumentuj zależności i ich licencje.

GitHub Pages traktuj jako podgląd statycznych prototypów, nie uruchomienie produkcyjnego backendu CMS. Formularze nie mogą udawać wysyłki wiadomości lub zapisu do newslettera, gdy nie mają backendu. W prototypie oznacz tę funkcję jako demonstracyjną i nie zbieraj prawdziwych danych.

Zorganizuj repozytorium czytelnie, przykładowo:

    nsz-redesign-prototypes/
      README.md
      reports/
        audit.md
        history-and-ideology.md
        sources.csv
        benchmarks.md
        design-comparison.md
        cms-recommendation.md
        qa.md
        deployment.md
      public/
        index.html
        .nojekyll
        assets/
        01-nowoczesny/
        02-ultranowoczesny/
        03-tradycyjny/
        04-dziedzictwo/
        05-awangardowy/
      tests/
      .github/workflows/

Każdy katalog wariantu ma zawierać jego kompletne widoki. Strona `public/index.html` ma być estetycznym selektorem pięciu koncepcji z miniaturami i bezpośrednimi linkami. Publikuj przez Pages tylko katalog przeznaczony do podglądu.

Zadbaj o ścieżki działające również pod prefiksem nazwy repozytorium. Nie zakładaj hostowania w głównym katalogu domeny. Kluczowa treść ma być dostępna bez JavaScriptu, a skrypty mają ją rozszerzać. README musi zawierać instrukcję lokalnego uruchomienia serwera HTTP.

## 14. Materiały graficzne, prawa i wiarygodność

Przygotuj rejestr użytych zasobów: plik, pochodzenie, autor, licencja lub podstawa użycia, wymagany podpis i status weryfikacji. Publiczna dostępność zdjęcia nie oznacza zgody na ponowną publikację.

Do publicznych prototypów włączaj wyłącznie materiały z potwierdzonym prawem użycia. Dla pozostałych stosuj oznaczone placeholdery i zapisz plan docelowej podmiany. Nie kopiuj całych archiwów i nie hotlinkuj obrazów jako obejścia problemu licencji.

Nie generuj fikcyjnych dokumentów, fotografii wojennych ani portretów prezentowanych jako autentyczne archiwalia. Nowe ilustracje koncepcyjne oznaczaj jako ilustracje, nie źródła historyczne. Logo pozostaw bez nieuzgodnionego przekształcania.

Podgląd oznacz komunikatem „Prototyp koncepcyjny — nie jest oficjalnym serwisem”. Zastosuj `noindex`, pamiętając, że nie stanowi zabezpieczenia dostępu. Nie dodawaj analityki, trackerów, rzeczywistych formularzy płatności ani danych poufnych.

## 15. Testy i kryteria odbioru

Sprawdź wszystkie warianty w szerokościach 360, 390, 768, 1280 i 1440 px. Zweryfikuj brak niezamierzonego przewijania poziomego, zasłaniania tekstu, rozjechanych kart i zbyt małych elementów interaktywnych.

Przetestuj klawiaturę, fokus, powiększenie tekstu, ograniczenie ruchu, otwieranie i zamykanie menu, wyszukiwanie, filtry, galerie i linki między podstronami. Wyszukaj błędy konsoli, niedostępne obrazy oraz odwołania do plików spoza ścieżki wdrożenia.

Wykonaj automatyczne i ręczne kontrole dostępności, o ile narzędzia na to pozwalają. Lighthouse wykorzystaj jako pomiar pomocniczy; przyjmij projektowe cele około 90 dla wydajności mobilnej i 95 dla dostępności. Nie traktuj wyniku automatu jako dowodu pełnej zgodności WCAG. Zapisz datę, warunki i faktyczne wyniki pomiarów.

Wykonaj zrzuty ekranów każdego wariantu na komputerze i telefonie. Obejrzyj je, popraw błędy i powtórz krytyczne testy. Nie zapisuj w raporcie „przetestowano”, jeżeli sprawdzono wyłącznie kod bez uruchomienia strony.

Każdy wariant oceń w skali 1–5 pod względem tożsamości, czytelności, odrębności, dostępu do aktualności, eksplorowania historii, obsługi mobilnej, dostępności oraz łatwości wdrożenia w CMS. Oceny eksperckie odróżniaj od wyników badań użytkowników.

## 16. GitHub i publiczne podglądy

Użyj dostępnej integracji GitHub lub autoryzowanego narzędzia Git. Najpierw odczytaj konto, uprawnienia i ewentualne istniejące repozytorium wskazane przez użytkownika. Nie zgaduj właściciela repozytorium i nie żądaj tokenów w treści rozmowy, gdy istnieje bezpieczna autoryzacja narzędzia.

Utwórz nowe, dedykowane repozytorium o nazwie zbliżonej do `nsz-redesign-prototypes`; w razie kolizji zastosuj bezpieczny sufiks. Zlecenie obejmuje publikację nowych prototypów, ale nie daje zgody na nadpisanie istniejącej strony, zmianę jej DNS, modyfikację innych repozytoriów ani ujawnienie poufnych plików.

Przed publikacją skontroluj sekrety, pliki środowiskowe, dane osobowe, licencje i oznaczenia materiałów demonstracyjnych. Publikuj wyłącznie zawartość przygotowaną do publicznego wglądu. Nie zmieniaj widoczności istniejących repozytoriów i nie wykonuj force push.

Wypchnij kod, skonfiguruj właściwe źródło wdrożenia Pages i sprawdź rezultat procesu. Następnie otwórz rzeczywisty adres selektora oraz pięć adresów wariantów. Sprawdź odpowiedzi HTTP i ładowanie kluczowych zasobów.

Nie przedstawiaj przewidywanego adresu jako działającego linku. Rozróżniaj: repozytorium utworzone, kod wypchnięty, wdrożenie uruchomione, wdrożenie zakończone, podgląd zweryfikowany.

Gdy integracja lub uprawnienia uniemożliwiają publikację, dostarcz kompletny ZIP, workflow lub instrukcję konfiguracji i dokładny opis brakującego kroku. Nie ograniczaj się do takiej instrukcji, jeżeli faktycznie możesz wykonać publikację. Nie deklaruj przyszłego działania w tle.

## 17. Rekomendacja produkcyjna

Wskaż najlepszy kierunek bazowy oraz ewentualnie jeden wariant hybrydowy. Uzasadnij wybór na podstawie wyników audytu, porównania projektów i testów, nie samego efektu wizualnego. Hybryda jest dodatkiem, nie zastępuje pięciu osobnych prototypów.

Przygotuj zakres MVP i etap dalszego rozwoju. Uwzględnij model treści w CMS-ie, migrację artykułów i mediów, mapę przekierowań starych adresów, zachowanie dat i autorstwa, wyszukiwanie, powiązanie archiwum, kontrolę źródeł, uprawnienia redakcyjne, kopie zapasowe i procedurę publikacji.

Koszty i pracochłonność przedstaw jako szacunki z założeniami. Nie wymyślaj aktualnych cen usług. Mierniki sukcesu powiąż z zadaniami czytelnika: odnalezieniem materiału, przejściem do źródła, odnalezieniem wydarzenia i wygodnym przeczytaniem artykułu. Nie obiecuj procentowego wzrostu ruchu bez danych bazowych i badań.

## 18. Sposób prowadzenia i zakończenia pracy

Na początku przedstaw krótki plan i rozpocznij realizację. Informuj o ważnych ustaleniach oraz blokadach, nie o każdym technicznym kroku. Nie zatrzymuj całego projektu przez nieistotne braki; zapisuj rozsądne założenia. Pytaj wyłącznie o nierozstrzygalne kwestie uprawnień lub decyzje, których nie można bezpiecznie podjąć samodzielnie.

W końcowej odpowiedzi pokaż kolejno: najważniejsze ustalenia audytu i CMS-u z poziomem pewności; syntezę historii i jej znaczenia dla projektu; porównanie pięciu wariantów; rzeczywiste linki do repozytorium, selektora i prototypów; rekomendację produkcyjną; wyniki testów oraz jawne ograniczenia.

Dołącz pliki raportów, bibliografię, rejestr zasobów i archiwum projektu. Wyraźnie rozróżnij to, co działa, od tego, co wymaga produkcyjnego backendu, dalszej weryfikacji lub akceptacji organizacji.

**Zadanie jest ukończone dopiero wtedy, gdy istnieje pięć odrębnych, używalnych prototypów, a raport uczciwie opisuje stopień weryfikacji historii, audytu, testów i publikacji. Nie zastępuj wykonania obietnicą ani samej oryginalności liczbą efektów.**
