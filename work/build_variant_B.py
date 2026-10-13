# -*- coding: utf-8 -*-
"""Generator statycznego HTML wariantu B „Żywe Archiwum”.

Źródła danych: public/assets/data/content.json (wspólny zestaw treści)
oraz zweryfikowane punkty z work/history-for-design.md i reports/sources.csv.
Wynik: public/02-ultranowoczesny/{index,aktualnosci,artykul}.html — czysty
HTML (treść dostępna bez JS); explorer.js i ../assets/shared/proto.js tylko
rozszerzają działanie.
"""
import json
import pathlib
from html import escape as e

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "02-ultranowoczesny"
DATA = json.loads((ROOT / "public/assets/data/content.json").read_text(encoding="utf-8"))
ORG = DATA["organization"]
ITEMS = {it["id"]: it for it in DATA["items"]}
DEMO = DATA["demo_article"]

MONTHS = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca",
          "sierpnia", "września", "października", "listopada", "grudnia"]
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]


def pl_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def short_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)}.{m}.{y}"


# ---------------------------------------------------------------------------
# Źródła (URL odczytane przez badacza historii, dostęp 13.10.2026)
SRC = {
    "ipn-nsz": ("IPN — „Narodowe Siły Zbrojne 1942–1946”", "https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html"),
    "wnuk": ("R. Wnuk, „Dzieje Najnowsze” 2021, nr 1 (IH PAN)", "http://dx.doi.org/10.12775/DN.2021.1.05"),
    "dzieje-nzw": ("dzieje.pl — NSZ i NZW", "https://dzieje.pl/node/142103"),
    "dzieje-bs": ("dzieje.pl — Brygada Świętokrzyska", "https://dzieje.pl/node/159201"),
    "oko": ("OKO.press — tekst krytyczny wobec upamiętnień Brygady (publicystyka)", "https://oko.press/ipn-i-abw-uczcily-kolaborantow-z-brygady-swietokrzyskiej-nsz-wraca-deta-historia-o-holiszowie"),
    "ph-holiszow": ("Przystanek Historia (IPN) — Holiszów", "https://przystanekhistoria.pl/pa2/tematy/okupacja-niemiecka/43594,Jak-Brygada-Swietokrzyska-NSZ-ocalila-wiezniarki-niemieckiego-obozu-w-Holiszowie.html"),
    "zz-krasnik": ("„Zagłada Żydów. Studia i Materiały” 7/2011 (CBnZŻ IFiS PAN) — streszczenie", "https://zagladazydow.pl/index.php/zz/article/view/777"),
    "ipn-wierzch": ("„Pamięć i Sprawiedliwość” (IPN) — artykuł o Wierzchowinach", "https://czasopisma.ipn.gov.pl/index.php/pis/article/view/588"),
    "ipn-kasznica": ("IPN — biogram Stanisława Kasznicy", "https://ipn.gov.pl/pl/historia-z-ipn/225426,Stanislaw-Kasznica-19081948.html"),
    "dzieje-flame": ("dzieje.pl — Henryk Flame „Bartek”", "https://dzieje.pl/node/99089"),
    "dzieje-marszalek": ("dzieje.pl — ks. Rudolf Marszałek „Opoka”", "https://dzieje.pl/node/101936"),
    "ipn-kat": ("IPN Katowice — pogrzeb żołnierzy zgrupowania „Bartka”", "https://katowice.ipn.gov.pl/pl3/aktualnosci/241705,Uroczystosci-pogrzebowe-zolnierzy-NSZ-ze-zgrupowania-kpt-Henryka-Flamego-Bartka-.html"),
    "ipn-wracaja": ("IPN — „Wracają jako bohaterowie” (operacja „Lawina”)", "https://ipn.gov.pl/pl/aktualnosci/241489,Wracaja-jako-bohaterowie.html"),
    "eli-2011": ("Ustawa z 3 lutego 2011 r., Dz.U. 2011 poz. 160", "https://eli.gov.pl/eli/DU/2011/160/ogl/pol/pdf"),
    "eli-2012": ("Uchwała Sejmu z 9 listopada 2012 r., M.P. 2012 poz. 890", "https://eli.gov.pl/eli/MP/2012/890/ogl/pol/pdf"),
    "nsz-siedlce": ("nsz.com.pl — relacja ZŻNSZ o akcji w Siedlcach", ITEMS["siedlce-1944"]["url"]),
    "nsz-domana": ("nsz.com.pl — publikacja rozkazu „Domana”", ITEMS["rozkaz-domana"]["url"]),
    "nsz-nestor": ("nsz.com.pl — biogram (P. Łapiński, „Głos znad Narwi” 2/2021)", ITEMS["nestorowicz"]["url"]),
    "nsz-synteza": ("nsz.com.pl — przedruk R. Sierchuły („Biuletyn IPN” 8–9/2007)", ITEMS["nsz-1942-1946"]["url"]),
}

STATUS = {
    "p": "potwierdzone",
    "ps": "fakt potwierdzony · ocena sporna",
    "a": "potwierdzone w streszczeniu badań",
    "r": "relacja ZŻNSZ · bez bibliografii",
    "d": "do uzupełnienia: sygnatura",
}

FACETS = [
    ("czas", "Czas", "21 punktów 1942–2026"),
    ("miejsca", "Miejsca", "10 miejsc"),
    ("ludzie", "Ludzie", "8 osób"),
    ("dokumenty", "Dokumenty", "6 aktów i opracowań"),
]

# id, facet, rok/kolumna, data ISO lub None, etykieta daty, krótka etykieta, tytuł, opis, status, źródła, powiązania
N = []


def node(id, facet, title, desc, status, src, links="", year=None, iso=None, dlabel=None, short=None, sub=None, tough=False):
    N.append(dict(id=id, facet=facet, title=title, desc=desc, status=status, src=src.split(),
                  links=links.split(), year=year, iso=iso, dlabel=dlabel, short=short or title, sub=sub or "",
                  tough=tough))


# --- CZAS ---
node("t1942-09", "czas", "Rozkaz nr 1/42 płk. Ignacego Oziewicza — przyjęta data powstania NSZ",
     "Płk Ignacy Oziewicz „Czesław” ogłosił objęcie funkcji komendanta głównego. Proces tworzenia organizacji ruszył w lipcu 1942 r.; NSZ powstały z połączenia Związku Jaszczurczego i części Narodowej Organizacji Wojskowej.",
     "p", "ipn-nsz", "p-oziewicz d-rozkaz142", 1942, "1942-09-20", "20 IX 1942", "20 IX · Rozkaz 1/42")
node("t1942-krasnik", "czas", "Okolice Kraśnika: zabójstwa zbiegów pochodzenia żydowskiego",
     "Według badań opublikowanych w „Zagładzie Żydów” oddział NOW-AN działający pod Kraśnikiem (później w strukturach NSZ) był sprawcą śmierci kilkudziesięciu zbiegów pochodzenia żydowskiego. Odpowiedzialność dotyczy konkretnego oddziału — w prototypie przywołana na podstawie streszczenia artykułu.",
     "a", "zz-krasnik", "m-krasnik", 1942, None, "1942", "1942 · Kraśnik", tough=True)
node("t1943-08", "czas", "Płk Tadeusz Kurcyusz „Żegota” dowódcą NSZ",
     "Po aresztowaniu Oziewicza przez Niemców zwierzchnictwo polityczne (TNRP) wybrało nowego dowódcę — zaprzysiężonego oficera AK.",
     "p", "wnuk", "p-kurcyusz", 1943, "1943-08-01", "1 VIII 1943", "1 VIII · Kurcyusz")
node("t1944-03-07", "czas", "Umowa scaleniowa z AK i rozłam: NSZ-AK oraz NSZ-ZJ",
     "Część NSZ podporządkowała się Armii Krajowej (NSZ-AK); środowisko związane z Grupą „Szańca” pozostało poza scaleniem (NSZ-ZJ). Od tej daty nazw tych nie należy stosować zamiennie.",
     "p", "wnuk dzieje-nzw", "d-wnuk", 1944, "1944-03-07", "7 III 1944", "7 III · Scalenie i rozłam")
node("t1944-03-12", "czas", "Odbicie oficerów NSZ z niemieckiego więzienia w Siedlcach",
     "Według relacji opublikowanej w serwisie ZŻNSZ oddział NSZ uwolnił członków sztabu Okręgu XII „Podlasie”. Tekst nie podaje źródeł — w prototypie oznaczony jako relacja do weryfikacji.",
     "r", "nsz-siedlce", "m-siedlce", 1944, "1944-03-12", "12 III 1944", "12 III · Siedlce")
node("t1944-08", "czas", "Udział żołnierzy NSZ w Powstaniu Warszawskim",
     "Synteza IPN podaje, że w powstaniu walczyło ok. 3,5 tys. żołnierzy NSZ (liczba według jednego źródła).",
     "p", "ipn-nsz", "m-warszawa", 1944, "1944-08", "VIII 1944", "VIII · Powstanie")
node("t1944-08-11", "czas", "Utworzenie Brygady Świętokrzyskiej",
     "Brygadę utworzono na Kielecczyźnie pod dowództwem kpt. Antoniego Dąbrowskiego-Szackiego „Bohuna”; w grudniu 1944 r. liczyła 822 ludzi.",
     "p", "ipn-nsz dzieje-bs", "p-bohun m-kielecczyzna", 1944, "1944-08-11", "11 VIII 1944", "11 VIII · Brygada")
node("t1944-nzw", "czas", "Powstaje Narodowe Zjednoczenie Wojskowe (NZW)",
     "NZW utworzono z inicjatywy Stronnictwa Narodowego pod koniec 1944 r.; działało do połowy lat 50. To formacja odrębna od NSZ.",
     "p", "dzieje-nzw", "d-domana p-danilewicz", 1944, None, "koniec 1944", "XII · NZW")
node("t1945-01", "czas", "Brygada Świętokrzyska wycofuje się na zachód na podstawie porozumienia z Wehrmachtem",
     "Fakt porozumienia z lokalnymi dowódcami Wehrmachtu jest potwierdzony w wielu źródłach. Jego ocena pozostaje sporna: synteza IPN opisuje manewr ewakuacyjny, inni autorzy i raporty AK wskazują na formy współpracy. Szczegóły i argumenty — w raporcie historycznym projektu.",
     "ps", "ipn-nsz oko", "p-bohun t1945-05-05", 1945, "1945-01", "I 1945", "I · Porozumienie", tough=True)
node("t1945-05-05", "czas", "Uwolnienie więźniarek obozu w Holiszowie",
     "Oddziały Brygady uwolniły więźniarki niemieckiego obozu w Holiszowie (dzis. Czechy). Liczby podawane w źródłach różnią się — prototyp ich nie podaje.",
     "p", "ph-holiszow", "m-holiszow p-bohun", 1945, "1945-05-05", "5 V 1945", "5 V · Holiszów")
node("t1945-06-06", "czas", "Wierzchowiny: zabójstwo mieszkańców wsi",
     "Oddział NSZ (PAS) dowodzony przez „Szarego” zabił ok. 194–196 cywilów. Fakt potwierdzają badania publikowane przez IPN; ocena dotyczy konkretnego oddziału i jego dowódcy.",
     "p", "ipn-wierzch", "m-wierzchowiny", 1945, "1945-06-06", "6 VI 1945", "6 VI · Wierzchowiny", tough=True)
node("t1945-07-22", "czas", "Rozkaz nr 312 płk. Tadeusza Danilewicza „Domana” (NZW)",
     "Dokument komendanta głównego NZW opublikowany we fragmencie w serwisie ZŻNSZ — bez sygnatury archiwalnej.",
     "d", "nsz-domana", "d-domana p-danilewicz", 1945, "1945-07-22", "22 VII 1945", "22 VII · Rozkaz 312")
node("t1946-05-03", "czas", "Przemarsz oddziału „Bartka” przez Wisłę",
     "W rocznicę Konstytucji 3 Maja zgrupowanie kpt. Henryka Flamego zajęło Wisłę i przemaszerowało przez miasto.",
     "p", "dzieje-flame", "p-flame m-wisla", 1946, "1946-05-03", "3 V 1946", "3 V · Wisła")
node("t1946-lawina", "czas", "Operacja UB „Lawina”",
     "Aparat bezpieczeństwa zorganizował rzekomy przerzut partyzantów na Zachód; żołnierzy zgrupowania przewieziono na Opolszczyznę i zamordowano.",
     "p", "ipn-wracaja", "p-flame m-opolszczyzna t2026-05-07", 1946, None, "jesień 1946", "jesień · „Lawina”")
node("t1947-02-15", "czas", "Aresztowanie ppłk. Stanisława Kasznicy",
     "Aresztowanie ostatniego komendanta NSZ-ZJ uznaje się za symboliczny koniec NSZ.",
     "p", "ipn-nsz", "p-kasznica", 1947, "1947-02-15", "15 II 1947", "15 II · Kasznica")
node("t1947-12-01", "czas", "Śmierć Henryka Flamego w Zabrzegu",
     "Po ujawnieniu się w ramach amnestii z 1947 r. Flame zginął zastrzelony przez milicjanta.",
     "p", "dzieje-flame", "p-flame", 1947, "1947-12-01", "1 XII 1947", "1 XII · Zabrzeg")
node("t1948-03-10", "czas", "Egzekucja ks. mjr. Rudolfa Marszałka „Opoki”",
     "Duszpasterz VII Okręgu Śląskiego NSZ, aresztowany w grudniu 1946 r., został skazany na śmierć i stracony.",
     "p", "dzieje-marszalek", "p-marszalek", 1948, "1948-03-10", "10 III 1948", "10 III · ks. Marszałek")
node("t1948-05-12", "czas", "Egzekucja ppłk. Stanisława Kasznicy",
     "Wykonana w więzieniu mokotowskim; wyrok unieważniono w 1992 r.",
     "p", "ipn-kasznica", "p-kasznica m-warszawa", 1948, "1948-05-12", "12 V 1948", "12 V · Kasznica")
node("t2011-02-03", "czas", "Ustawa ustanawiająca Narodowy Dzień Pamięci „Żołnierzy Wyklętych”",
     "1 marca jako święto państwowe.", "p", "eli-2011", "d-ustawa2011", 2011, "2011-02-03", "3 II 2011", "3 II · Ustawa")
node("t2012-11-09", "czas", "Uchwała Sejmu w 70. rocznicę powstania NSZ",
     "Akt okolicznościowy Sejmu RP — źródło wiedzy o współczesnej polityce pamięci, nie o przebiegu wydarzeń.",
     "p", "eli-2012", "d-uchwala2012", 2012, "2012-11-09", "9 XI 2012", "9 XI · Uchwała")
node("t2026-05-07", "czas", "Pogrzeb żołnierzy zgrupowania „Bartka” i otwarcie cmentarza w Kamesznicy",
     "Szczątki ofiar operacji „Lawina” odnalezione przez IPN pochowano na nowym cmentarzu wojennym.",
     "p", "ipn-kat", "m-kamesznica p-flame", 2026, "2026-05-07", "7 V 2026", "7 V · Kamesznica")

# --- MIEJSCA ---
node("m-warszawa", "miejsca", "Warszawa", "Powstanie Warszawskie 1944; więzienie mokotowskie (1948).", "p", "ipn-nsz", sub="mazowieckie")
node("m-siedlce", "miejsca", "Siedlce", "Akcja z 12 marca 1944 r. w relacji ZŻNSZ.", "r", "nsz-siedlce", sub="Okręg XII „Podlasie”")
node("m-kielecczyzna", "miejsca", "Kielecczyzna", "Miejsce utworzenia Brygady Świętokrzyskiej (VIII 1944).", "p", "ipn-nsz", sub="świętokrzyskie")
node("m-holiszow", "miejsca", "Holiszów (Holýšov)", "Niemiecki obóz dla kobiet, dziś w Czechach.", "p", "ph-holiszow", sub="Czechy")
node("m-krasnik", "miejsca", "Okolice Kraśnika", "Trudny wątek z 1942 r. — zob. oś czasu.", "a", "zz-krasnik", sub="lubelskie")
node("m-wierzchowiny", "miejsca", "Wierzchowiny", "Trudny wątek z 6 czerwca 1945 r. — zob. oś czasu.", "p", "ipn-wierzch", sub="lubelskie")
node("m-wisla", "miejsca", "Wisła", "Przemarsz oddziału „Bartka” 3 maja 1946 r.; współczesne obchody.", "p", "dzieje-flame", "t1946-05-03", sub="Beskid Śląski")
node("m-opolszczyzna", "miejsca", "Opolszczyzna", "Miejsca mordu ofiar operacji „Lawina” i poszukiwań IPN.", "p", "ipn-wracaja", sub="opolskie")
node("m-kamesznica", "miejsca", "Kamesznica", "Cmentarz wojenny otwarty 7 maja 2026 r.; obchody 84. rocznicy NSZ.", "p", "ipn-kat", sub="pow. żywiecki")
node("m-bialystok", "miejsca", "Białystok", "Okręg NSZ, którym dowodził ppłk Wacław Nestorowicz.", "r", "nsz-nestor", "p-nestorowicz", sub="podlaskie")

# --- LUDZIE ---
node("p-oziewicz", "ludzie", "płk Ignacy Oziewicz „Czesław”", "Pierwszy komendant główny NSZ (1942), aresztowany przez Niemców.", "p", "ipn-nsz", sub="komendant główny 1942–43")
node("p-kurcyusz", "ludzie", "płk Tadeusz Kurcyusz „Żegota”", "Dowódca NSZ od 1 sierpnia 1943 r., zaprzysiężony oficer AK.", "p", "wnuk", sub="dowódca od 1943")
node("p-bohun", "ludzie", "kpt. Antoni Dąbrowski-Szacki „Bohun”", "Dowódca Brygady Świętokrzyskiej; zm. 1992.", "p", "ipn-nsz", sub="Brygada Świętokrzyska")
node("p-kasznica", "ludzie", "ppłk Stanisław Kasznica (1908–1948)", "Ostatni komendant NSZ-ZJ; stracony w 1948 r., wyrok unieważniony w 1992 r.", "p", "ipn-kasznica", sub="komendant NSZ-ZJ")
node("p-flame", "ludzie", "kpt. Henryk Flame „Bartek” (1918–1947)", "Dowódca zgrupowania na Podbeskidziu i Górnym Śląsku 1945–1946.", "p", "dzieje-flame ipn-kat", sub="zgrupowanie „Bartka”")
node("p-marszalek", "ludzie", "ks. mjr Rudolf Marszałek „Opoka”", "Kapelan oddziałów AK, od lipca 1945 r. duszpasterz VII Okręgu Śląskiego NSZ.", "p", "dzieje-marszalek", sub="duszpasterz")
node("p-nestorowicz", "ludzie", "ppłk Wacław Nestorowicz „Kalina”", "Komendant Okręgu NSZ Białystok (ur. 1891); biogram w serwisie ZŻNSZ.", "r", "nsz-nestor", "m-bialystok", sub="Okręg Białystok")
node("p-danilewicz", "ludzie", "płk Tadeusz Danilewicz „Doman”", "Komendant główny NZW — formacji odrębnej od NSZ.", "d", "nsz-domana", sub="komendant główny NZW")

# --- DOKUMENTY ---
node("d-rozkaz142", "dokumenty", "Rozkaz nr 1/42 (1942)", "Znany z opracowań; skan nie jest dołączony do prototypu.", "p", "ipn-nsz", sub="dokument epoki · przez opracowanie")
node("d-domana", "dokumenty", "Rozkaz nr 312 „Domana” (1945)", "Fragment opublikowany przez ZŻNSZ; brak sygnatury archiwalnej.", "d", "nsz-domana", sub="dokument epoki · NZW")
node("d-sierchula", "dokumenty", "R. Sierchuła, „Narodowe Siły Zbrojne (1942–1946)”", "Synteza z „Biuletynu IPN” 8–9/2007, przedrukowana w serwisie ZŻNSZ.", "p", "nsz-synteza", "t1942-09 p-oziewicz", sub="opracowanie")
node("d-wnuk", "dokumenty", "R. Wnuk, artykuł w „Dziejach Najnowszych” (2021)", "Artykuł naukowy o relacjach NSZ i AK; podaje liczebność 58–65 tys.", "p", "wnuk", "p-kurcyusz", sub="artykuł naukowy")
node("d-ustawa2011", "dokumenty", "Ustawa z 3 lutego 2011 r.", "Dz.U. 2011 poz. 160.", "p", "eli-2011", sub="akt prawny")
node("d-uchwala2012", "dokumenty", "Uchwała Sejmu z 9 listopada 2012 r.", "M.P. 2012 poz. 890.", "p", "eli-2012", sub="akt Sejmu")

IDS = {n["id"] for n in N}
for n in N:
    for l in n["links"]:
        assert l in IDS, (n["id"], l)
    for s in n["src"]:
        assert s in SRC, (n["id"], s)

# ---------------------------------------------------------------------------
ICONS = {
    "search": '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "menu": '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path d="M3 7h18M3 12h18M3 17h12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "motion": '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path d="M3 12h4l2-5 4 10 2-5h6" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
    "close": '<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "ext": '<svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14"><path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
}


def head(title, desc, page_class):
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="color-scheme" content="dark light">
<link rel="preload" href="fonts/space-grotesk-latin-ext-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/shared/a11y.css">
<link rel="stylesheet" href="style.css">
</head>
<body class="{page_class}">
<a class="skip-link" href="#tresc">Przejdź do treści</a>
<div class="proto-banner" role="note"><strong>Prototyp koncepcyjny — nie jest oficjalnym serwisem.</strong> Wariant B „Żywe Archiwum”. Treści demonstracyjne; materiały źródłowe prowadzą do nsz.com.pl i instytucji badawczych. <a href="../index.html">Wróć do wyboru wariantów</a></div>
"""


def header(current):
    links = [("index.html#eksplorator", "Historia", "historia"), ("aktualnosci.html", "Aktualności", "aktualnosci"),
             ("index.html#ludzie-dokumenty", "Zasób", "ludzie"), ("index.html#archiwum", "Archiwum", "archiwum"),
             ("index.html#zwiazek", "Związek", "zwiazek")]
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if k == current else ""}>{t}</a></li>' for h, t, k in links)
    return f"""<header class="site-header">
  <div class="hdr-inner">
    <a class="brand" href="index.html">
      <span class="brand-logo" role="img" aria-label="Miejsce na logo ZŻNSZ — oryginalny plik organizacji">[logo ZŻNSZ]</span>
      <span class="brand-text"><span class="brand-org">Związek Żołnierzy<br>Narodowych Sił Zbrojnych</span><span class="brand-sub">Żywe Archiwum · prototyp</span></span>
    </a>
    <nav class="main-nav" aria-label="Główna">
      <button class="icon-btn menu-btn" type="button" data-disclosure aria-controls="menu-glowne">{ICONS['menu']}<span>Menu</span></button>
      <ul id="menu-glowne" class="menu">{nav}</ul>
    </nav>
    <div class="hdr-tools">
      <button class="icon-btn" type="button" data-disclosure data-modal aria-controls="panel-szukaj">{ICONS['search']}<span>Szukaj</span></button>
      <button class="icon-btn motion-btn" type="button" data-motion-toggle aria-pressed="false">{ICONS['motion']}<span data-motion-label>Animacje: włączone</span></button>
    </div>
  </div>
  <div id="panel-szukaj" class="search-panel" data-quick-search data-list-href="aktualnosci.html">
    <form class="search-form" role="search" action="aktualnosci.html" method="get">
      <label for="q-global">Szukaj w materiałach serwisu</label>
      <div class="search-row">
        <input id="q-global" name="q" type="search" autocomplete="off" placeholder="np. Kamesznica, NZW, Bartek">
        <button class="btn" type="submit">Szukaj</button>
        <button class="icon-btn" type="button" data-close>{ICONS['close']}<span class="sr-only">Zamknij wyszukiwanie</span></button>
      </div>
    </form>
    <p class="search-status" data-results-status aria-live="polite"></p>
    <ul class="search-results" data-results></ul>
  </div>
</header>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="ftr-inner">
    <div>
      <p class="ftr-org">{e(ORG['name'])}</p>
      <p>{e(ORG['address'])}<br>KRS {e(ORG['krs'])}</p>
    </div>
    <ul class="ftr-links">
      <li><a href="index.html#eksplorator">Eksplorator historii</a></li>
      <li><a href="aktualnosci.html">Aktualności</a></li>
      <li><a href="artykul.html">Przykładowy artykuł</a></li>
      <li><a href="../index.html">Wszystkie warianty prototypu</a></li>
    </ul>
    <p class="ftr-note">Prototyp koncepcyjny — nie jest oficjalnym serwisem ZŻNSZ. Paleta, kroje i układ są propozycją projektową, nie obecną identyfikacją. Kroje: Space Grotesk i IBM Plex Mono (SIL OFL 1.1), hostowane lokalnie. Bez analityki i plików cookie.</p>
  </div>
</footer>
<script src="../assets/data/content.js"></script>
<script src="../assets/shared/proto.js"></script>
"""


def src_html(keys):
    return "; ".join(f'<a href="{e(SRC[k][1])}" rel="noopener">{e(SRC[k][0])}</a>' for k in keys)


def node_li(n):
    attrs = (f'id="n-{n["id"]}" class="node st-{n["status"]}{" is-tough" if n["tough"] else ""}" data-id="{n["id"]}" '
             f'data-facet="{n["facet"]}" data-status="{n["status"]}" data-short="{e(n["short"])}" '
             f'data-links="{" ".join(n["links"])}" data-sub="{e(n["sub"])}"')
    if n["year"]:
        attrs += f' data-year="{n["year"]}"'
    meta = []
    if n["dlabel"]:
        meta.append(f'<time{" datetime=" + chr(34) + n["iso"] + chr(34) if n["iso"] else ""}>{e(n["dlabel"])}</time>')
    elif n["sub"]:
        meta.append(f'<span>{e(n["sub"])}</span>')
    meta.append(f'<span class="badge">{STATUS[n["status"]]}</span>')
    if n["tough"]:
        meta.append('<span class="badge badge-tough">trudny wątek</span>')
    return (f'<li {attrs}><p class="node-meta">{" ".join(meta)}</p>'
            f'<h4 class="node-title">{e(n["title"])}</h4><p class="node-desc">{e(n["desc"])}</p>'
            f'<p class="node-src"><span>Źródło:</span> {src_html(n["src"])}</p></li>')


TYPE_LABEL = {"aktualnosc": "Aktualność", "wydarzenie": "Wydarzenie", "historia": "Historia",
              "biogram": "Biogram", "dokument": "Dokument"}
ITEM_NODE = {"84-rocznica": "t1942-09", "kamesznica-cmentarz": "t2026-05-07", "defilada-wisla-80": "t1946-05-03",
             "holiszow-81": "t1945-05-05", "nsz-1942-1946": "d-sierchula", "nestorowicz": "p-nestorowicz",
             "rozkaz-domana": "d-domana", "siedlce-1944": "t1944-03-12"}


def author_line(it):
    if it.get("author"):
        return f'Autor: {e(it["author"])}'
    return 'Autor: nie wskazano w serwisie'


# ---------------------------------------------------------------------------
def build_index():
    by_facet = {f: [n for n in N if n["facet"] == f] for f, _, _ in FACETS}
    facet_links = "".join(
        f'<li><a class="facet" href="#lista-{f}" data-facet="{f}"><span class="facet-name">{lab}</span>'
        f'<span class="facet-count">{cnt}</span></a></li>' for f, lab, cnt in FACETS)
    lists = "".join(
        f'<section class="node-group" id="lista-{f}" data-group="{f}" aria-labelledby="h-{f}"><h3 id="h-{f}">{lab}</h3>'
        f'<ol class="node-list">{"".join(node_li(n) for n in by_facet[f])}</ol></section>' for f, lab, _ in FACETS)

    news = sorted([it for it in DATA["items"] if it["type"] in ("aktualnosc", "wydarzenie")],
                  key=lambda x: x["date"], reverse=True)

    def news_row(it):
        d = it["date"].split("-")
        return f"""<li class="stream-item">
  <p class="stream-date"><time datetime="{it['date']}"><span class="sd-day">{int(d[2])}</span><span class="sd-month">{ROMAN[int(d[1]) - 1]} {d[0]}</span></time></p>
  <div class="stream-body">
    <p class="kicker">{TYPE_LABEL[it['type']]}{' · ' + e(it['place']) if it.get('place') else ''}</p>
    <h3><a href="{e(it['url'])}" rel="noopener">{e(it['title'])}<span class="sr-only"> (otwiera serwis nsz.com.pl)</span></a></h3>
    <p>{e(it['summary'])}</p>
    <p class="stream-links"><a class="chip" href="#n-{ITEM_NODE[it['id']]}">Kontekst w eksploratorze</a>{' <a class="chip" href="artykul.html">Opracowanie: zgrupowanie „Bartka”</a>' if it['id'] in ('kamesznica-cmentarz', 'defilada-wisla-80') else ''}</p>
  </div>
</li>"""

    domana = ITEMS["rozkaz-domana"]
    nest = ITEMS["nestorowicz"]
    synt = ITEMS["nsz-1942-1946"]
    html = head("Żywe Archiwum — Związek Żołnierzy NSZ (prototyp B)",
                "Prototyp koncepcyjny strony głównej: eksplorator historii NSZ przez czas, miejsca, ludzi i dokumenty.",
                "page-home")
    html += header("historia")
    html += f"""<main id="tresc">
<section class="explore" id="eksplorator" aria-labelledby="explore-title">
  <div class="explore-intro">
    <p class="eyebrow">Historia NSZ · 1942–1948 · pamięć po 1989</p>
    <h1 id="explore-title">Wejdź do historii przez czas, miejsca, ludzi albo&nbsp;dokumenty</h1>
    <p class="lede">Każdy punkt ma źródło i status wiarygodności. Spory historyków i trudne wątki są oznaczone, nie pominięte. Wybierz perspektywę, a potem przechodź po powiązaniach.</p>
  </div>
  <ul class="facets" data-facets>{facet_links}</ul>
  <div class="explorer" data-explorer>
    <div class="explorer-bar">
      <p class="explorer-hint" data-explorer-hint>Widok listy — wszystkie punkty ze źródłami.</p>
      <div class="view-switch" data-view-switch hidden>
        <span class="vs-label" id="vs-label">Widok:</span>
        <div role="group" aria-labelledby="vs-label">
          <button type="button" data-view="map" aria-pressed="true">Oś i powiązania</button>
          <button type="button" data-view="list" aria-pressed="false">Lista</button>
        </div>
      </div>
    </div>
    <div class="explorer-stage" data-stage hidden></div>
    <div class="node-lists" data-lists>
      <h2 class="sr-only">Wszystkie punkty eksploratora — widok listy</h2>
      {lists}
    </div>
    <p class="legend"><span class="lg lg-p">potwierdzone</span> <span class="lg lg-ps">fakt potwierdzony · ocena sporna</span> <span class="lg lg-r">relacja ZŻNSZ do weryfikacji</span> <span class="lg lg-tough">trudny wątek</span> — zbiór demonstracyjny ({len(N)} punktów) z raportu historycznego projektu; dostęp do źródeł 13.10.2026.</p>
  </div>
</section>

<section class="now" aria-labelledby="now-title">
  <div class="sec-head">
    <h2 id="now-title"><span class="sec-num" aria-hidden="true">02</span> Teraz w Związku</h2>
    <a class="more" href="aktualnosci.html">Wszystkie aktualności i materiały</a>
  </div>
  <ol class="stream">{''.join(news_row(it) for it in news)}</ol>
</section>

<section class="records" id="ludzie-dokumenty" aria-labelledby="rec-title">
  <div class="sec-head">
    <h2 id="rec-title"><span class="sec-num" aria-hidden="true">03</span> Z zasobu: dokument, biogram, opracowanie</h2>
  </div>
  <div class="record-grid">
    <article class="record record-doc">
      <p class="kicker">Dokument epoki · NZW</p>
      <h3><a href="{e(domana['url'])}" rel="noopener">{e(domana['title'])}</a></h3>
      <dl class="meta-table">
        <div><dt>Data dokumentu</dt><dd><time datetime="1945-07-22">22 lipca 1945</time></dd></div>
        <div><dt>Formacja</dt><dd>NZW — odrębna od NSZ</dd></div>
        <div><dt>Sygnatura</dt><dd class="warn">brak — do uzupełnienia</dd></div>
        <div><dt>Publikacja</dt><dd>nsz.com.pl, <time datetime="{domana['date']}">{short_date(domana['date'])}</time></dd></div>
      </dl>
      <p>{e(domana['summary'])}</p>
      <p><a class="chip" href="#n-d-domana">Powiązania w eksploratorze</a></p>
    </article>
    <article class="record">
      <p class="kicker">Biogram</p>
      <h3><a href="{e(nest['url'])}" rel="noopener">{e(nest['title'])}</a></h3>
      <dl class="meta-table">
        <div><dt>Funkcja</dt><dd>komendant Okręgu NSZ Białystok</dd></div>
        <div><dt>Autor</dt><dd>{e(nest['author'])}</dd></div>
        <div><dt>Pierwodruk</dt><dd>„Głos znad Narwi” 2/2021</dd></div>
      </dl>
      <p>{e(nest['summary'])}</p>
      <p><a class="chip" href="#n-p-nestorowicz">Powiązania w eksploratorze</a></p>
    </article>
    <article class="record">
      <p class="kicker">Opracowanie · punkt wejścia</p>
      <h3><a href="{e(synt['url'])}" rel="noopener">{e(synt['title'])}</a></h3>
      <dl class="meta-table">
        <div><dt>Autor</dt><dd>{e(synt['author'])}</dd></div>
        <div><dt>Pierwodruk</dt><dd>„Biuletyn IPN” 8–9/2007</dd></div>
      </dl>
      <p>{e(synt['summary'])}</p>
    </article>
  </div>
</section>

<section class="archive" id="archiwum" aria-labelledby="arch-title">
  <div class="sec-head">
    <h2 id="arch-title"><span class="sec-num" aria-hidden="true">04</span> Zasoby Związku w liczbach</h2>
  </div>
  <ul class="stats">
    <li><span class="stat-n">200</span><span class="stat-l">życiorysów</span></li>
    <li><span class="stat-n">379</span><span class="stat-l">wpisów kalendarium</span></li>
    <li><span class="stat-n">105</span><span class="stat-l">filmów</span></li>
    <li><span class="stat-n">32</span><span class="stat-l">dokumenty</span></li>
    <li><span class="stat-n">8&nbsp;501</span><span class="stat-l">rekordów Cyfrowego Archiwum</span></li>
  </ul>
  <p class="stat-src">Liczby wpisów według kategorii odczytane z publicznego API serwisu nsz.com.pl i archiwumcyfrowe.nsz.com.pl, 13.10.2026. Cyfrowe Archiwum to dziś osobny system — w docelowym serwisie wyszukiwanie obejmowałoby oba zasoby.</p>
  <p><a class="btn btn-ghost" href="{e(ORG['related_systems'][0]['url'])}" rel="noopener">Otwórz Cyfrowe Archiwum ZŻNSZ</a></p>
</section>

<section class="org" id="zwiazek" aria-labelledby="org-title">
  <div class="sec-head">
    <h2 id="org-title"><span class="sec-num" aria-hidden="true">05</span> Związek Żołnierzy NSZ</h2>
  </div>
  <div class="org-grid">
    <div>
      <p class="org-lede">{e(ORG['mission'])}</p>
      <p class="org-note">Historia formacji z lat 1942–1948 i działalność dzisiejszego Związku to dwie różne warstwy serwisu — w tym prototypie są rozdzielone.</p>
    </div>
    <dl class="meta-table org-data">
      <div><dt>Siedziba</dt><dd>{e(ORG['address'])}</dd></div>
      <div><dt>Korespondencja</dt><dd>{e(ORG['correspondence'])}</dd></div>
      <div><dt>Zarząd</dt><dd>{e(ORG['email_board'])}</dd></div>
      <div><dt>Redakcja</dt><dd>{e(ORG['email_editorial'])}</dd></div>
      <div><dt>KRS · NIP</dt><dd>{e(ORG['krs'])} · {e(ORG['nip'])}</dd></div>
    </dl>
    <form class="demo-form" data-demo-form>
      <h3>Powiadomienia o nowych materiałach</h3>
      <p class="form-flag">Funkcja demonstracyjna — formularz niczego nie wysyła ani nie zapisuje.</p>
      <label for="demo-email">Adres e-mail</label>
      <input id="demo-email" type="email" autocomplete="off" placeholder="nie wpisuj prawdziwego adresu">
      <button class="btn" type="submit">Zapisz (demo)</button>
      <p class="demo-msg" data-demo-msg aria-live="polite"></p>
    </form>
  </div>
</section>
</main>
"""
    html += footer()
    html += '<script src="explorer.js"></script>\n</body>\n</html>\n'
    (OUT / "index.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
def build_news():
    items = sorted(DATA["items"], key=lambda x: x["date"], reverse=True)
    filters = [("all", "Wszystkie"), ("aktualnosc", "Aktualności"), ("wydarzenie", "Wydarzenia"),
               ("historia", "Historia"), ("biogram", "Biogramy"), ("dokument", "Dokumenty")]
    fbtns = "".join(f'<li><button type="button" class="fbtn" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t}</button></li>' for k, t in filters)

    def row(it):
        flag = f'<p class="flag">Uwaga redakcyjna prototypu: {e(it["editorial_flag"])}</p>' if it.get("editorial_flag") else ""
        when = f' · wydarzenie: <time datetime="{it["event_date"]}">{pl_date(it["event_date"])}</time>' if it.get("event_date") else ""
        text = " ".join([it["title"], it["summary"], it.get("place") or "", " ".join(it.get("tags", [])), it["category"], TYPE_LABEL[it["type"]]])
        extra = ' <a class="chip" href="artykul.html">Opracowanie: zgrupowanie „Bartka”</a>' if it["id"] in ("kamesznica-cmentarz", "defilada-wisla-80", "84-rocznica") else ""
        return f"""<li class="rec-item" data-item data-cat="{it['type']}" data-text="{e(text)}">
  <div class="rec-when"><time datetime="{it['date']}">{short_date(it['date'])}</time><span class="type-tag t-{it['type']}">{TYPE_LABEL[it['type']]}</span></div>
  <div class="rec-body">
    <h2 class="rec-title"><a href="{e(it['url'])}" rel="noopener">{e(it['title'])}<span class="sr-only"> (otwiera serwis nsz.com.pl)</span></a></h2>
    <p>{e(it['summary'])}</p>
    <p class="rec-meta">{author_line(it)}{' · ' + e(it['place']) if it.get('place') else ''}{when} · kategoria w serwisie: {e(it['category'])}</p>
    {flag}
    <p class="stream-links"><a class="chip" href="index.html#n-{ITEM_NODE[it['id']]}">Kontekst w eksploratorze</a>{extra}</p>
  </div>
</li>"""

    demo = f"""<li class="rec-item rec-demo" data-item data-cat="historia" data-text="{e(DEMO['title'] + ' ' + DEMO['lead'] + ' Bartek Flame Lawina Kamesznica opracowanie')}">
  <div class="rec-when"><time datetime="{DEMO['date']}">{short_date(DEMO['date'])}</time><span class="type-tag t-historia">Historia</span></div>
  <div class="rec-body">
    <h2 class="rec-title"><a href="artykul.html">{e(DEMO['title'])}</a></h2>
    <p>{e(DEMO['lead'])}</p>
    <p class="rec-meta flag">{e(DEMO['label'])}</p>
  </div>
</li>"""

    html = head("Aktualności i materiały — Żywe Archiwum (prototyp B)",
                "Lista aktualności i materiałów z filtrowaniem — prototyp koncepcyjny.", "page-news")
    html += header("aktualnosci")
    html += f"""<main id="tresc" class="news-main">
<nav class="crumbs" aria-label="Okruszki"><ol><li><a href="index.html">Strona główna</a></li><li><span aria-current="page">Aktualności i materiały</span></li></ol></nav>
<div class="news-layout" data-filter-scope>
  <aside class="news-side" aria-labelledby="news-title">
    <p class="eyebrow">Strumień materiałów</p>
    <h1 id="news-title">Aktualności i materiały</h1>
    <form class="filter-search" role="search">
      <label for="q-list">Szukaj w tym zestawie</label>
      <input id="q-list" type="search" data-search autocomplete="off" placeholder="np. Holiszów, biogram, 1945">
    </form>
    <fieldset class="filters">
      <legend>Rodzaj materiału</legend>
      <ul>{fbtns}</ul>
    </fieldset>
    <p class="count" data-count aria-live="polite" role="status">Znaleziono {len(items) + 1} materiałów</p>
    <button type="button" class="btn btn-ghost" data-clear-filters>Wyczyść filtry</button>
    <p class="side-note">Zestaw demonstracyjny: 8 rzeczywistych wpisów z nsz.com.pl (tytuły, daty i autorstwo według serwisu; zajawki napisane na potrzeby prototypu) oraz 1 tekst demonstracyjny.</p>
  </aside>
  <section class="news-list" aria-label="Wyniki">
    <ol class="rec-list">{demo}{''.join(row(it) for it in items)}</ol>
    <div class="empty" data-empty hidden>
      <h2>Brak materiałów dla tych kryteriów</h2>
      <p>Zmień słowo wyszukiwania albo rodzaj materiału. Możesz też zacząć od eksploratora historii.</p>
      <p><button type="button" class="btn" data-clear-filters>Wyczyść filtry</button> <a class="btn btn-ghost" href="index.html#eksplorator">Otwórz eksplorator</a></p>
    </div>
  </section>
</div>
</main>
"""
    html += footer()
    html += "</body>\n</html>\n"
    (OUT / "aktualnosci.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
def slug(s):
    import re, unicodedata
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode().replace("ł", "l")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


SIDE = {
    "Dowódca i oddział": [("p-flame", "Osoba: kpt. Henryk Flame „Bartek”"), ("t1946-05-03", "Oś czasu: 3 V 1946 — Wisła")],
    "Operacja „Lawina”": [("t1946-lawina", "Oś czasu: jesień 1946 — „Lawina”"), ("t1947-12-01", "Oś czasu: 1 XII 1947 — Zabrzeg")],
    "Poszukiwania i identyfikacja": [("m-opolszczyzna", "Miejsce: Opolszczyzna")],
    "Pogrzeb 7 maja 2026 r.": [("t2026-05-07", "Oś czasu: 7 V 2026 — Kamesznica"), ("m-kamesznica", "Miejsce: Kamesznica")],
}


def placeholder_svg(i):
    paths = [
        '<path d="M0 260 C120 200 200 230 300 170 S520 120 640 160 L640 360 L0 360Z" fill="#c9cede"/><path d="M0 300 C160 250 260 290 380 240 S560 220 640 250 L640 360 L0 360Z" fill="#aeb5c9"/>',
        '<path d="M0 280 L140 150 L230 230 L330 90 L450 210 L540 140 L640 230 L640 360 L0 360Z" fill="#b6bdd0"/><path d="M0 320 L180 240 L300 300 L460 230 L640 300 L640 360 L0 360Z" fill="#9aa3bb"/>',
        '<rect x="170" y="40" width="300" height="280" fill="#e9e6dc" stroke="#9aa3bb" stroke-width="3"/><g stroke="#9aa3bb" stroke-width="6" stroke-linecap="round"><path d="M210 100h220M210 140h200M210 180h220M210 220h160M210 260h190"/></g>',
    ]
    return f'<svg viewBox="0 0 640 360" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice"><rect width="640" height="360" fill="#dde1ea"/>{paths[i]}</svg>'


def build_article():
    secs = DEMO["sections"]
    toc = "".join(f'<li><a href="#{slug(s["heading"])}">{e(s["heading"])}</a></li>' for s in secs)
    body = ""
    for i, s in enumerate(secs):
        side = SIDE.get(s["heading"])
        aside = ""
        if side:
            aside = '<aside class="margin-note" aria-label="Powiązane punkty w eksploratorze"><p class="mn-title">W eksploratorze</p><ul>' + "".join(
                f'<li><a href="index.html#n-{nid}">{e(lbl)}</a></li>' for nid, lbl in side) + "</ul></aside>"
        paras = "".join(f"<p>{e(p)}</p>" for p in s["paragraphs"])
        body += f'<section class="art-sec" aria-labelledby="{slug(s["heading"])}"><h2 id="{slug(s["heading"])}">{e(s["heading"])}</h2>{aside}{paras}</section>'
        if i == 1:
            slides = "".join(
                f'<figure class="slide" data-slide><div class="ph" role="img" aria-label="{e(g["alt"])}">{placeholder_svg(k)}<span class="ph-tag">Miejsce na materiał — ilustracja zastępcza</span></div>'
                f'<figcaption>{e(g["caption"])}</figcaption></figure>' for k, g in enumerate(DEMO["gallery"]))
            body += f"""<section class="gallery" data-gallery aria-labelledby="gal-title" tabindex="-1">
  <div class="gal-head"><h2 id="gal-title" class="gal-title">Galeria materiałów</h2><p class="gal-status" data-status aria-live="polite"></p></div>
  <div class="gal-track" data-track>{slides}</div>
  <div class="gal-ctrl">
    <button type="button" class="btn btn-ghost" data-prev><span aria-hidden="true">←</span> Poprzedni</button>
    <div class="gal-dots" data-dots></div>
    <button type="button" class="btn btn-ghost" data-next>Następny <span aria-hidden="true">→</span></button>
  </div>
  <p class="gal-note">Galeria nie przewija się sama. Obsługa: przyciski, strzałki klawiatury, przeciągnięcie. Fotografie zastąpione oznaczonymi miejscami — prawa do zdjęć nie zostały potwierdzone.</p>
</section>"""
    sources = "".join(f'<li><a href="{e(s["url"])}" rel="noopener">{e(s["label"])}</a> <span class="acc">dostęp {short_date(s["accessed"])}</span></li>' for s in DEMO["sources"])
    rel = [ITEMS["kamesznica-cmentarz"], ITEMS["defilada-wisla-80"], ITEMS["84-rocznica"]]
    related = "".join(f'<li><p class="kicker">{TYPE_LABEL[r["type"]]} · <time datetime="{r["date"]}">{short_date(r["date"])}</time></p><a href="{e(r["url"])}" rel="noopener">{e(r["title"])}</a></li>' for r in rel)

    html = head("Od operacji „Lawina” do Kamesznicy — Żywe Archiwum (prototyp B)",
                "Przykładowy artykuł w trybie czytania — tekst demonstracyjny prototypu.", "page-article")
    html += header("aktualnosci")
    html += f"""<div class="progress" aria-hidden="true"><div class="progress-bar" data-reading-progress></div></div>
<main id="tresc" class="article-main">
<nav class="crumbs" aria-label="Okruszki"><ol><li><a href="index.html">Strona główna</a></li><li><a href="aktualnosci.html">Aktualności i materiały</a></li><li><span aria-current="page">Zgrupowanie „Bartka”</span></li></ol></nav>
<article class="article">
  <header class="art-head">
    <p class="demo-label">{e(DEMO['label'])}</p>
    <p class="eyebrow">Historia · opracowanie</p>
    <h1>{e(DEMO['title'])}</h1>
    <dl class="art-meta">
      <div><dt>Data</dt><dd><time datetime="{DEMO['date']}">{pl_date(DEMO['date'])}</time></dd></div>
      <div><dt>Autorstwo</dt><dd>nie wskazano autora — {e(DEMO['author_note'])}</dd></div>
      <div><dt>Czas czytania</dt><dd>ok. 4 min</dd></div>
    </dl>
    <p class="art-lead">{e(DEMO['lead'])}</p>
  </header>
  <div class="art-layout">
    <nav class="toc" data-toc aria-labelledby="toc-title">
      <p id="toc-title" class="toc-title">Spis treści</p>
      <ol>{toc}<li><a href="#zrodla">Źródła</a></li></ol>
    </nav>
    <div class="art-body" data-article-body>
      {body}
      <section class="sources" aria-labelledby="zrodla"><h2 id="zrodla">Źródła</h2><ol>{sources}</ol>
      <p class="src-note">Pełna bibliografia projektu i rejestr twierdzeń: raport historyczny (reports/history-and-ideology.md, reports/sources.csv w repozytorium prototypów).</p></section>
    </div>
  </div>
  <footer class="art-foot">
    <section aria-labelledby="rel-title"><h2 id="rel-title">Powiązane materiały w serwisie ZŻNSZ</h2><ul class="related">{related}</ul></section>
    <nav class="back-nav" aria-label="Nawigacja powrotna">
      <a class="btn" href="aktualnosci.html"><span aria-hidden="true">←</span> Wróć do aktualności i materiałów</a>
      <a class="btn btn-ghost" href="index.html#n-p-flame">Zobacz „Bartka” w eksploratorze</a>
    </nav>
  </footer>
</article>
</main>
"""
    html += footer()
    html += "</body>\n</html>\n"
    (OUT / "artykul.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build_index()
    build_news()
    build_article()
    print("OK", len(N), "nodes")
