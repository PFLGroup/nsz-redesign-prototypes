# -*- coding: utf-8 -*-
"""Generator statycznych widoków wariantu A „Instytucja 2.0”.

Czyta wspólny zestaw treści (public/assets/data/content.json) i zapisuje
gotowe pliki HTML do public/01-nowoczesny/. Wynik jest w pełni statyczny —
treść jest w HTML, JavaScript tylko ją rozszerza.
Uruchomienie: python work/variant-A/build.py
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "public" / "01-nowoczesny"
DATA = json.loads((ROOT / "public" / "assets" / "data" / "content.json").read_text(encoding="utf-8"))
ITEMS = {i["id"]: i for i in DATA["items"]}
ORG = DATA["organization"]
DEMO = DATA["demo_article"]

MONTHS = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca",
          "sierpnia", "września", "października", "listopada", "grudnia"]


def e(s):
    return html.escape(s or "", quote=True)


def pl_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


# Kategorie filtrów: wydarzenia liczą się też jako aktualności,
# biogramy i dokumenty — także jako historia (zakres wyszukiwania).
CATS = {
    "aktualnosc": "aktualnosc",
    "wydarzenie": "wydarzenie aktualnosc",
    "historia": "historia",
    "biogram": "biogram historia",
    "dokument": "dokument historia",
}
TYPE_LABEL = {
    "aktualnosc": "Aktualności",
    "wydarzenie": "Wydarzenie · relacja",
    "historia": "Historia",
    "biogram": "Życiorys",
    "dokument": "Dokument",
}

ICON = {
    "search": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4.2-4.2"/></svg>',
    "menu": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>',
    "chev": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    "prev": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>',
    "next": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>',
}

HISTORY_REPORT = "https://github.com/PFLGroup/nsz-redesign-prototypes/blob/main/reports/history-and-ideology.md"


def head(title, desc):
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)} — Wariant A „Instytucja 2.0” · prototyp</title>
<meta name="description" content="{e(desc)}">
<link rel="preload" href="fonts/archivo-latin-ext-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/shared/a11y.css">
<link rel="stylesheet" href="a01.css">
</head>
<body>
<a class="skip-link" href="#tresc">Przejdź do treści</a>
<div class="proto-banner" role="note"><strong>Prototyp koncepcyjny — nie jest oficjalnym serwisem.</strong> Wariant A „Instytucja 2.0”. Treści demonstracyjne; linki źródłowe prowadzą do nsz.com.pl. <a href="../index.html">Wróć do wyboru wariantów</a></div>
"""


def header(current):
    def cur(name):
        return ' aria-current="page"' if name == current else ""

    return f"""<div class="utility">
  <div class="wrap">
    <p class="org-line">Organizacja kombatancka · KRS {e(ORG['krs'])}</p>
    <ul>
      <li><a href="{e(ORG['related_systems'][0]['url'])}" class="ext">Cyfrowe Archiwum</a></li>
      <li><a href="index.html#organizacja">Kontakt</a></li>
      <li><button type="button" data-motion-toggle aria-pressed="false"><span data-motion-label>Animacje: włączone</span></button></li>
    </ul>
  </div>
</div>
<header class="masthead">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="logo-slot" title="[logo ZŻNSZ — oryginalny plik organizacji]" aria-hidden="true">[logo ZŻNSZ]</span>
      <span class="brand-name"><b>Związek Żołnierzy <em>NSZ</em></b><span>Historia · Źródła · Działalność</span></span>
    </a>
    <button class="search-toggle" type="button" data-disclosure data-modal aria-controls="search-panel">{ICON['search']}<span class="label-text">Szukaj</span></button>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="a-nav">{ICON['menu']}<span class="label-text">Menu</span></button>
  </div>
</header>
<nav class="primary-nav" id="a-nav" aria-label="Główna">
  <div class="wrap">
    <ul>
      <li><a href="aktualnosci.html"{cur('aktualnosci')}>Aktualności</a></li>
      <li>
        <button class="sub-toggle" type="button" data-disclosure aria-controls="mega-historia">Historia {ICON['chev']}</button>
        <div class="mega" id="mega-historia">
          <div class="wrap">
            <div class="mega-intro">
              <h2>Historia NSZ</h2>
              <p>Zwięzłe wprowadzenie, oś czasu, nazwy formacji i zagadnienia sporne — z odsyłaczami do źródeł.</p>
              <a class="btn btn-ghost" href="historia.html">Kontekst historyczny <span class="arrow" aria-hidden="true">→</span></a>
            </div>
            <div><h2>Na początek</h2><ul>
              <li><a href="historia.html#os-czasu">Oś czasu 1942–2012</a></li>
              <li><a href="historia.html#nazwy">NSZ, NSZ-AK, NSZ-ZJ, NZW — nazwy</a></li>
              <li><a href="historia.html#sporne">Zagadnienia sporne i trudne</a></li>
            </ul></div>
            <div><h2>Materiały</h2><ul>
              <li><a href="aktualnosci.html?kat=historia">Artykuły i opracowania</a></li>
              <li><a href="aktualnosci.html?kat=biogram">Życiorysy</a></li>
              <li><a href="aktualnosci.html?kat=dokument">Dokumenty</a></li>
            </ul></div>
            <div><h2>Przykład</h2><ul>
              <li><a href="artykul.html">Zgrupowanie „Bartka” 1945–1947 (tekst demonstracyjny)</a></li>
            </ul></div>
          </div>
        </div>
      </li>
      <li><a href="aktualnosci.html?kat=biogram">Ludzie</a></li>
      <li><a href="aktualnosci.html?kat=dokument">Archiwum</a></li>
      <li><a href="aktualnosci.html?kat=wydarzenie">Wydarzenia</a></li>
      <li><a href="index.html#organizacja"{cur('organizacja')}>Organizacja</a></li>
      <li><a href="historia.html"{cur('historia')}>Kontekst</a></li>
    </ul>
  </div>
</nav>
<div class="search-panel" id="search-panel">
  <div class="wrap">
    <form class="search-form" action="aktualnosci.html" method="get" role="search" data-quick-search data-list-href="aktualnosci.html">
      <div class="search-row">
        <label for="q-global">Szukaj w serwisie</label>
        <input id="q-global" name="q" type="search" placeholder="np. Kamesznica, Holiszów, NZW" autocomplete="off">
        <button class="btn" type="submit">Szukaj</button>
      </div>
      <fieldset class="scope">
        <legend>Zakres:</legend>
        <label><input type="radio" name="kat" value="all" checked> Wszystko</label>
        <label><input type="radio" name="kat" value="aktualnosc"> Aktualności</label>
        <label><input type="radio" name="kat" value="historia"> Historia</label>
        <label><input type="radio" name="kat" value="dokument"> Dokumenty</label>
      </fieldset>
      <p class="popular">Często szukane: <a href="aktualnosci.html?q=Kamesznica">Kamesznica</a> <a href="aktualnosci.html?q=Bartek">„Bartek”</a> <a href="aktualnosci.html?q=NZW">NZW</a> <a href="aktualnosci.html?q=Brygada">Brygada Świętokrzyska</a></p>
      <p class="sr-only" aria-live="polite" data-results-status></p>
      <ul class="quick-results" data-results></ul>
      <button class="btn btn-ghost search-close" type="button" data-close>Zamknij wyszukiwanie</button>
    </form>
  </div>
</div>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p><strong>Prototyp koncepcyjny modernizacji serwisu nsz.com.pl — wariant A „Instytucja 2.0”.</strong> Nie jest oficjalnym serwisem Związku Żołnierzy Narodowych Sił Zbrojnych. Tytuły, daty i adresy materiałów pochodzą z serwisu nsz.com.pl (odczyt 13.10.2026); zajawki i tekst demonstracyjny przygotowano na potrzeby prototypu.</p>
      <small>[logo ZŻNSZ — oryginalny plik organizacji]: w prototypie celowo nie odtworzono emblematu. Zdjęcia zastąpiono oznaczonymi miejscami — prawa do fotografii nie zostały potwierdzone. Bez analityki i plików cookie.</small>
    </div>
    <div><ul>
      <li><a href="aktualnosci.html">Aktualności</a></li>
      <li><a href="historia.html">Kontekst historyczny</a></li>
      <li><a href="artykul.html">Przykładowy artykuł</a></li>
    </ul></div>
    <div><ul>
      <li><a href="../index.html">Wszystkie warianty</a></li>
      <li><a href="https://www.nsz.com.pl/" class="ext">Obecny serwis nsz.com.pl</a></li>
    </ul></div>
  </div>
</footer>
<script src="../assets/data/content.js"></script>
<script src="../assets/shared/proto.js"></script>
<script src="a01.js"></script>
</body>
</html>
"""


def ph(text, cls=""):
    return f'<div class="ph {cls}" role="img" aria-label="{e(text)}"><span>{e(text)}</span></div>'


def kicker(item):
    label = TYPE_LABEL[item["type"]]
    return f'<p class="kicker"><span class="cat">{e(label)}</span><time datetime="{item["date"]}">{pl_date(item["date"])}</time></p>'


def author_line(item):
    if item.get("author"):
        return f"Autor: {e(item['author'])}"
    return "Brak podpisu autora w źródle"


# ------------------------------------------------------------ strona główna
TOPICS = [
    {
        "id": "temat-bartek", "no": "01", "name": "Zgrupowanie „Bartka”", "range": "1945–1947 · pamięć 2026",
        "intro": "Powojenne zgrupowanie kpt. Henryka Flamego „Bartka” na Podbeskidziu, jego likwidacja w operacji UBP „Lawina” i tegoroczny pochówek ofiar w Kamesznicy.",
        "now": ["kamesznica-cmentarz", "defilada-wisla-80", "84-rocznica"],
        "ctx": [("artykul.html", "Od operacji „Lawina” do Kamesznicy", "tekst demonstracyjny z bibliografią")],
        "src": [("https://katowice.ipn.gov.pl/pl3/aktualnosci/241705,Uroczystosci-pogrzebowe-zolnierzy-NSZ-ze-zgrupowania-kpt-Henryka-Flamego-Bartka-.html", "IPN Katowice — uroczystości pogrzebowe", "komunikat instytucji"),
                ("https://ipn.gov.pl/pl/wydawnictwo/e-booki/241624,Poswiecic-swe-sily-majatek-a-nawet-zycie-Henryk-Flame-Bartek-i-jego-zolnierze.html", "IPN — e-book o „Bartku” i jego żołnierzach", "publikacja IPN")],
    },
    {
        "id": "temat-brygada", "no": "02", "name": "Brygada Świętokrzyska", "range": "1944–1945 · temat sporny",
        "intro": "Utworzona 11 sierpnia 1944 r. W styczniu 1945 r. wycofała się na zachód po uzgodnieniach z lokalnymi dowódcami Wehrmachtu — fakt porozumienia jest bezsporny, jego ocena pozostaje przedmiotem sporu historyków i publicystów.",
        "now": ["holiszow-81"],
        "ctx": [("historia.html#brygada", "Brygada Świętokrzyska — co jest pewne, co sporne", "kontekst w prototypie"),
                ("https://www.nsz.com.pl/narodowe-sily-zbrojne-1942-1946/", "Narodowe Siły Zbrojne (1942–1946)", "synteza R. Sierchuły w serwisie")],
        "src": [("https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html", "IPN — Narodowe Siły Zbrojne (1942–1946)", "synteza IPN"),
                ("https://przystanekhistoria.pl/pa2/tematy/okupacja-niemiecka/43594,Jak-Brygada-Swietokrzyska-NSZ-ocalila-wiezniarki-niemieckiego-obozu-w-Holiszowie.html", "Przystanek Historia — Holiszów 1945", "tekst popularnonaukowy IPN")],
    },
    {
        "id": "temat-struktury", "no": "03", "name": "Struktury i dowództwo NSZ", "range": "1942–1944",
        "intro": "Powstanie NSZ 20 września 1942 r., kierownictwo polityczne TNRP, scalenie z AK w marcu 1944 r. i rozłam na NSZ-AK oraz NSZ-ZJ. Liczebność formacji podajemy z przedziałem i źródłem.",
        "now": [],
        "ctx": [("https://www.nsz.com.pl/narodowe-sily-zbrojne-1942-1946/", "Narodowe Siły Zbrojne (1942–1946)", "synteza w serwisie"),
                ("https://www.nsz.com.pl/pplk-waclaw-nestorowicz-ps-kalina/", "Ppłk Wacław Nestorowicz „Kalina”", "życiorys komendanta Okręgu Białystok")],
        "src": [("https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html", "IPN — synteza o NSZ", "synteza IPN"),
                ("http://dx.doi.org/10.12775/DN.2021.1.05", "R. Wnuk, „Dzieje Najnowsze” 2021", "artykuł naukowy")],
        "note": "Liczebność w 1944 r.: 58–65 tys. według R. Wnuka; ok. 90 tys. według Związku. Rozbieżność pokazujemy jawnie.",
    },
    {
        "id": "temat-nazwy", "no": "04", "name": "NSZ, NOW, NZW — nazwy", "range": "terminologia",
        "intro": "Narodowe Zjednoczenie Wojskowe (NZW) to formacja powołana przez Stronnictwo Narodowe pod koniec 1944 r. — odrębna od NSZ. Rozkaz płk. „Domana” dotyczy NZW, nie NSZ.",
        "now": [],
        "ctx": [("historia.html#nazwy", "Tabela nazw i formacji", "kontekst w prototypie")],
        "src": [("https://www.nsz.com.pl/rozkaz-pplk-domana-komendanta-glownego-nzw/", "Rozkaz płk. „Domana” komendanta głównego NZW", "dokument w serwisie — bez sygnatury"),
                ("https://dzieje.pl/node/142103", "dzieje.pl — NSZ i NZW", "portal popularnonaukowy")],
    },
    {
        "id": "temat-1944", "no": "05", "name": "Konspiracja na Podlasiu", "range": "1944",
        "intro": "Akcja z 12 marca 1944 r., w której oddział NSZ uwolnił członków sztabu Okręgu XII „Podlasie” z niemieckiego więzienia w Siedlcach.",
        "now": [],
        "ctx": [("https://www.nsz.com.pl/akcja-odbicia-oficerow-nsz-z-niemieckiego-wiezienia-w-siedlcach/", "Akcja odbicia oficerów NSZ w Siedlcach", "artykuł w serwisie")],
        "src": [],
        "note": "Tekst w serwisie nie podaje źródeł — przed wyróżnieniem wymaga uzupełnienia bibliografii.",
    },
]


def topic_index():
    tabs, panels = [], []
    for t in TOPICS:
        n = len(t["now"]) + len(t["ctx"]) + len(t["src"])
        tabs.append(f'<li><button class="ti-tab" type="button" aria-controls="{t["id"]}"><span class="no">{t["no"]}</span><span class="name">{e(t["name"])}<small>{e(t["range"])}</small></span><span class="count">{n} mat.</span></button></li>')

        def col(cls, title, rows):
            if not rows:
                return f'<div class="ti-col {cls}"><h4>{title}</h4><p class="no-js-note" style="display:block">Brak bieżących materiałów w zestawie demonstracyjnym.</p></div>'
            return f'<div class="ti-col {cls}"><h4>{title}</h4><ul>{"".join(rows)}</ul></div>'

        now_rows = []
        for iid in t["now"]:
            it = ITEMS[iid]
            now_rows.append(f'<li><a href="{e(it["url"])}" class="ext">{e(it["title"])}</a><small>{pl_date(it["date"])} · nsz.com.pl</small></li>')
        ctx_rows = [f'<li><a href="{e(u)}"{" class=\"ext\"" if u.startswith("http") else ""}>{e(l)}</a><small>{e(s)}</small></li>' for u, l, s in t["ctx"]]
        src_rows = [f'<li><a href="{e(u)}" class="ext">{e(l)}</a><small>{e(s)}</small></li>' for u, l, s in t["src"]]
        note = f'<p class="flag">{e(t["note"])}</p>' if t.get("note") else ""
        panels.append(f"""<div class="ti-panel" id="{t['id']}">
  <p class="kicker"><span class="cat">Temat {t['no']}</span><span>{e(t['range'])}</span></p>
  <h3>{e(t['name'])}</h3>
  <p>{e(t['intro'])}</p>
  {note}
  <div class="ti-cols">
    {col('now', 'Teraz w serwisie', now_rows)}
    {col('ctx', 'Kontekst historyczny', ctx_rows)}
    {col('src', 'Źródła i opracowania', src_rows)}
  </div>
</div>""")
    return f"""<section class="topic-index" aria-labelledby="ti-title">
  <div class="wrap">
    <div class="ti-head">
      <h2 id="ti-title"><small>Indeks tematów</small>Od bieżącej wiadomości do źródła</h2>
      <p>Każdy temat łączy to, co dzieje się teraz — uroczystość, relację, zapowiedź — z kontekstem historycznym i opracowaniami. Tematy sporne oznaczamy wprost i pokazujemy różne stanowiska badaczy.</p>
    </div>
    <div class="ti no-js-ti" data-topic-index>
      <ul class="ti-tabs">{''.join(tabs)}</ul>
      <div class="ti-panels">{''.join(panels)}</div>
    </div>
  </div>
</section>"""


def page_index():
    lead = ITEMS["84-rocznica"]
    latest = ["defilada-wisla-80", "holiszow-81", "kamesznica-cmentarz"]
    latest_html = []
    for iid in latest:
        it = ITEMS[iid]
        extra = ""
        if iid == "holiszow-81":
            extra = ' · <a href="historia.html#brygada">kontekst: temat sporny</a>'
        latest_html.append(f"""<li><div>
  <h3><a href="{e(it['url'])}">{e(it['title'])}</a></h3>
  <p><time datetime="{it['date']}">{pl_date(it['date'])}</time> · {e(it.get('place', ''))}{extra}</p>
</div></li>""")
    doc = ITEMS["rozkaz-domana"]
    bio = ITEMS["nestorowicz"]
    body = f"""<main id="tresc">
<section class="identity wrap" aria-label="O serwisie">
  <h1><strong>{e(ORG['name'])}</strong> — historia formacji, źródła i bieżąca działalność Związku w jednym miejscu.</h1>
</section>
<div class="wrap front">
  <article class="lead-story" aria-labelledby="lead-title">
    {ph('Miejsce na fotografię z obchodów w Kamesznicy — wymaga licencji od ZŻNSZ lub IPN')}
    <div>
      <p class="kicker"><span class="cat">Temat dnia · Aktualności</span><time datetime="{lead['date']}">{pl_date(lead['date'])}</time></p>
      <h2 id="lead-title"><a href="{e(lead['url'])}">{e(lead['title'])}</a></h2>
      <p class="summary">{e(lead['summary'])}</p>
      <div class="context-strip">
        <b>Kontekst</b>
        <span>Za datę powstania NSZ przyjmuje się 20 września 1942 r. — dzień rozkazu nr 1/42 płk. Ignacego Oziewicza „Czesława”.</span>
        <a href="historia.html#os-czasu">Oś czasu 1942–2012 <span class="arrow" aria-hidden="true">→</span></a>
      </div>
    </div>
  </article>
  <aside class="side" aria-label="Najnowsze i kalendarz">
    <section aria-labelledby="latest-title">
      <div class="rule-title"><h2 id="latest-title">Najnowsze</h2><a href="aktualnosci.html">Wszystkie <span class="arrow" aria-hidden="true">→</span></a></div>
      <ol class="latest">{''.join(latest_html)}</ol>
    </section>
    <section aria-labelledby="anniv-title">
      <div class="rule-title"><h2 id="anniv-title">Kalendarz rocznic</h2></div>
      <ul class="anniv">
        <li><span class="date-badge"><b>1</b><small>mar</small></span><p>Narodowy Dzień Pamięci „Żołnierzy Wyklętych”<span>ustanowiony ustawą z 3 lutego 2011 r.</span></p></li>
        <li><span class="date-badge"><b>3</b><small>maj</small></span><p>Rocznica przemarszu zgrupowania „Bartka” przez Wisłę<span>3 maja 1946 r.</span></p></li>
        <li><span class="date-badge"><b>5</b><small>maj</small></span><p>Rocznica uwolnienia więźniarek w Holiszowie<span>5 maja 1945 r. · <a href="historia.html#brygada">kontekst</a></span></p></li>
        <li><span class="date-badge"><b>20</b><small>wrz</small></span><p>Rocznica powstania NSZ<span>20 września 1942 r.</span></p></li>
      </ul>
      <p class="no-js-note" style="display:block;margin-top:10px">Stałe daty rocznic. Terminy i miejsca uroczystości ogłasza Związek w aktualnościach.</p>
    </section>
  </aside>
</div>
{topic_index()}
<div class="wrap trio">
  <section aria-labelledby="doc-title">
    <div class="rule-title"><h2 id="doc-title">Ze źródeł</h2><a href="aktualnosci.html?kat=dokument">Dokumenty <span class="arrow" aria-hidden="true">→</span></a></div>
    <article class="doc-card">
      <p class="kicker"><span class="cat">Dokument · NZW</span></p>
      <h3><a href="{e(doc['url'])}" class="ext">{e(doc['title'])}</a></h3>
      <dl class="doc-meta">
        <dt>Data dokumentu</dt><dd>22 lipca 1945 r. (rozkaz nr 312)</dd>
        <dt>Formacja</dt><dd>Narodowe Zjednoczenie Wojskowe — odrębne od NSZ</dd>
        <dt>Publikacja</dt><dd>{pl_date(doc['date'])}, nsz.com.pl</dd>
        <dt>Sygnatura</dt><dd>brak w źródle</dd>
      </dl>
      <p>{e(doc['summary'])}</p>
      <p class="flag">Uwaga redakcyjna: przed prezentacją jako źródło wymaga uzupełnienia sygnatury archiwalnej.</p>
    </article>
  </section>
  <section aria-labelledby="bio-title">
    <div class="rule-title"><h2 id="bio-title">Życiorys</h2><a href="aktualnosci.html?kat=biogram">Ludzie <span class="arrow" aria-hidden="true">→</span></a></div>
    <article class="bio">
      {ph('Miejsce na portret — wymaga licencji')}
      <div>
        <h3><a href="{e(bio['url'])}" class="ext">{e(bio['title'])}</a></h3>
        <p>{e(bio['summary'])}</p>
        <p class="no-js-note" style="display:block">Autor: {e(bio['author'])}. {e(bio['author_note'])}</p>
      </div>
    </article>
  </section>
  <section aria-labelledby="tl-title">
    <div class="rule-title"><h2 id="tl-title">W datach</h2><a href="historia.html#os-czasu">Pełna oś <span class="arrow" aria-hidden="true">→</span></a></div>
    <ol class="mini-timeline">
      <li><b>20 IX 1942</b>powstanie NSZ</li>
      <li><b>7 III 1944</b>umowa scaleniowa z AK; rozłam na NSZ-AK i NSZ-ZJ</li>
      <li><b>11 VIII 1944</b>utworzenie Brygady Świętokrzyskiej</li>
      <li><b>koniec 1944</b>powstaje NZW (odrębna formacja)</li>
      <li><b>15 II 1947</b>aresztowanie ppłk. S. Kasznicy</li>
    </ol>
  </section>
</div>
<section class="wrap" aria-labelledby="media-title">
  <div class="rule-title"><h2 id="media-title">Multimedia</h2><a href="https://www.nsz.com.pl/" class="ext">Galerie w serwisie</a></div>
  <div class="media-row">
    <figure class="media-item">{ph('Galeria z Wisły, 3 maja 2026 — fotografie w serwisie źródłowym, licencja do potwierdzenia')}<figcaption>Relacja z 80. rocznicy defilady w Wiśle. <a href="{e(ITEMS['defilada-wisla-80']['url'])}" class="ext">Galeria w serwisie</a></figcaption></figure>
    <figure class="media-item">{ph('Miejsce na nagranie wideo z uroczystości — wymaga zgody autora')}<figcaption>Nagrania z uroczystości — moduł do zasilenia z kanału organizacji.</figcaption></figure>
    <figure class="media-item">{ph('Miejsce na skan z Cyfrowego Archiwum — osobny system, integracja do potwierdzenia')}<figcaption>Wybór z <a href="{e(ORG['related_systems'][0]['url'])}" class="ext">Cyfrowego Archiwum ZŻNSZ</a>.</figcaption></figure>
  </div>
</section>
<section class="org" id="organizacja" aria-labelledby="org-title">
  <div class="wrap org-grid">
    <div>
      <h2 id="org-title">O Związku</h2>
      <p>{e(ORG['mission'])}</p>
      <p>Serwis oddziela historię formacji z lat 1942–1947 od bieżącej działalności Związku — organizacji, która tę historię upamiętnia.</p>
    </div>
    <div>
      <h3>Dane</h3>
      <dl>
        <dt>KRS</dt><dd>{e(ORG['krs'])}</dd>
        <dt>NIP</dt><dd>{e(ORG['nip'])}</dd>
        <dt>REGON</dt><dd>{e(ORG['regon'])}</dd>
        <dt>Siedziba</dt><dd>{e(ORG['address'])}</dd>
      </dl>
    </div>
    <div>
      <h3>Kontakt i serwisy</h3>
      <dl>
        <dt>Zarząd</dt><dd>{e(ORG['email_board'])}</dd>
        <dt>Redakcja</dt><dd>{e(ORG['email_editorial'])}</dd>
        <dt>Korespondencja</dt><dd>{e(ORG['correspondence'])}</dd>
      </dl>
      <ul style="margin-top:10px">
        {''.join(f'<li><a href="{e(s["url"])}" class="ext">{e(s["name"])}</a></li>' for s in ORG['related_systems'])}
      </ul>
    </div>
  </div>
</section>
</main>
"""
    return head("Strona główna", "Prototyp strony głównej — redakcyjny portal instytucji z indeksem tematów.") + header("") + body + footer()


# ------------------------------------------------------------ lista aktualności
def page_list():
    rows = []
    for it in sorted(DATA["items"], key=lambda x: x["date"], reverse=True):
        cats = CATS[it["type"]]
        text = " ".join([it["title"], it["summary"], it.get("place", ""), " ".join(it.get("tags", [])), it["category"]])
        flag = f'<p class="flag">{e(it["editorial_flag"])}</p>' if it.get("editorial_flag") else ""
        ev = f' · wydarzenie: {pl_date(it["event_date"])}' if it.get("event_date") else ""
        ctx = ' <a href="historia.html#brygada">Kontekst: temat sporny</a>' if it["id"] == "holiszow-81" else ""
        rows.append(f"""<li class="news-row" data-item data-cat="{cats}" data-text="{e(text)}">
  <div class="when"><span class="cat-label">{e(TYPE_LABEL[it['type']])}</span><time datetime="{it['date']}">{pl_date(it['date'])}</time></div>
  <div>
    <h2><a href="{e(it['url'])}">{e(it['title'])}</a></h2>
    <p>{e(it['summary'])}</p>
    {flag}
    <p class="meta"><span>{author_line(it)}</span><span>Kategoria w serwisie: {e(it['category'])}{ev}</span></p>
    <p class="links"><a href="{e(it['url'])}" class="ext">Czytaj w serwisie nsz.com.pl</a>{ctx}</p>
  </div>
</li>""")
    filt = [("all", "Wszystkie"), ("aktualnosc", "Aktualności"), ("wydarzenie", "Wydarzenia"),
            ("historia", "Historia"), ("biogram", "Życiorysy"), ("dokument", "Dokumenty")]
    btns = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in filt)
    body = f"""<main id="tresc">
<div class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Okruszki"><ol><li><a href="index.html">Strona główna</a></li><li><span aria-current="page">Aktualności i materiały</span></li></ol></nav>
    <h1>Aktualności i materiały</h1>
    <p>Aktualności Związku oraz artykuły, życiorysy i dokumenty — w jednym, filtrowanym spisie. Zestaw demonstracyjny: 8 materiałów z serwisu nsz.com.pl.</p>
  </div>
</div>
<div class="wrap list-layout" data-filter-scope>
  <aside class="filters" aria-label="Filtry">
    <form class="filter-search" role="search" action="aktualnosci.html" method="get">
      <label for="q-list">Szukaj w materiałach</label>
      <input id="q-list" name="q" type="search" data-search placeholder="np. Siedlce">
    </form>
    <div>
      <h2 id="f-title">Rodzaj materiału</h2>
      <div class="filter-btns" role="group" aria-labelledby="f-title">{btns}</div>
    </div>
    <button class="btn btn-ghost" type="button" data-clear-filters>Wyczyść filtry</button>
  </aside>
  <section aria-label="Wyniki">
    <div class="results-bar"><p data-count aria-live="polite">8 materiałów</p><a href="artykul.html">Przykładowy artykuł <span class="arrow" aria-hidden="true">→</span></a></div>
    <ol class="news-list">{''.join(rows)}</ol>
    <div class="empty" data-empty hidden>
      <h2>Brak materiałów dla wybranych kryteriów</h2>
      <p>Spróbuj innego słowa (np. „Kamesznica”, „NZW”) albo pokaż wszystkie materiały.</p>
      <button class="btn" type="button" data-clear-filters>Pokaż wszystkie</button>
    </div>
  </section>
</div>
</main>
"""
    return head("Aktualności i materiały", "Lista aktualności z filtrami i wyszukiwarką — wariant A.") + header("aktualnosci") + body + footer()


# ------------------------------------------------------------ artykuł
def slug(i):
    return f"sekcja-{i + 1}"


def page_article():
    toc = "".join(f'<li><a href="#{slug(i)}">{e(s["heading"])}</a></li>' for i, s in enumerate(DEMO["sections"]))
    secs = []
    for i, s in enumerate(DEMO["sections"]):
        paras = "".join(f"<p>{e(p)}</p>" for p in s["paragraphs"])
        secs.append(f'<h2 id="{slug(i)}">{e(s["heading"])}</h2>{paras}')
        if i == 0:
            slides = "".join(
                f'<figure data-slide>{ph(g["alt"])}<figcaption>{e(g["caption"])}</figcaption></figure>'
                for g in DEMO["gallery"])
            secs.append(f"""<section class="gallery" data-gallery aria-label="Galeria ilustracji do artykułu" tabindex="0">
  <div class="gallery-viewport">{slides}</div>
  <div class="gallery-controls">
    <span data-status aria-live="polite">Galeria: 3 ilustracje</span>
    <button class="nav-btn" type="button" data-prev aria-label="Poprzednia ilustracja">{ICON['prev']}</button>
    <span data-dots></span>
    <button class="nav-btn" type="button" data-next aria-label="Następna ilustracja">{ICON['next']}</button>
  </div>
</section>""")
    sources = "".join(f'<li><a href="{e(s["url"])}" class="ext">{e(s["label"])}</a> — dostęp {pl_date(s["accessed"])}</li>' for s in DEMO["sources"])
    rel = []
    for iid in ["kamesznica-cmentarz", "defilada-wisla-80", "84-rocznica"]:
        it = ITEMS[iid]
        rel.append(f'<article>{kicker(it)}<h3><a href="{e(it["url"])}" class="ext">{e(it["title"])}</a></h3><p>{e(it["summary"])}</p></article>')
    body = f"""<div class="progress" data-reading-progress role="progressbar" aria-label="Postęp czytania" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"></div>
<main id="tresc">
<header class="article-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Okruszki"><ol><li><a href="index.html">Strona główna</a></li><li><a href="historia.html">Historia</a></li><li><span aria-current="page">Zgrupowanie „Bartka”</span></li></ol></nav>
    <div class="grid">
      <div>
        <p class="demo-label">{e(DEMO['label'])}</p>
        <p class="kicker"><span class="cat">Historia · Temat 01 z indeksu</span></p>
        <h1>{e(DEMO['title'])}</h1>
      </div>
      <div class="byline">
        <dl>
          <dt>Data</dt><dd><time datetime="{DEMO['date']}">{pl_date(DEMO['date'])}</time></dd>
          <dt>Autor</dt><dd>brak podpisu — {e(DEMO['author_note'])}</dd>
          <dt>Czas czytania</dt><dd>ok. 4 min</dd>
        </dl>
      </div>
    </div>
  </div>
</header>
<div class="wrap article-body">
  <nav class="toc" data-toc aria-labelledby="toc-title">
    <h2 id="toc-title">Spis treści</h2>
    <ol>{toc}<li><a href="#zrodla">Źródła</a></li></ol>
  </nav>
  <article class="prose" data-article-body>
    <p class="lead">{e(DEMO['lead'])}</p>
    {''.join(secs)}
    <section class="sources" id="zrodla" aria-labelledby="zrodla-h">
      <h2 id="zrodla-h">Źródła</h2>
      <ol>{sources}</ol>
      <p>Szerszy kontekst, w tym zagadnienia sporne: <a href="historia.html">Kontekst historyczny</a>.</p>
    </section>
    <nav class="back-nav" aria-label="Nawigacja powrotna">
      <a class="btn btn-ghost" href="aktualnosci.html"><span aria-hidden="true">←</span> Wróć do listy materiałów</a>
      <a class="btn btn-ghost" href="index.html#ti-title">Indeks tematów</a>
    </nav>
  </article>
  <aside class="aside-col" aria-label="W tym temacie">
    <div class="aside-box">
      <h2>W tym temacie</h2>
      <ul>
        <li><a href="{e(ITEMS['kamesznica-cmentarz']['url'])}" class="ext">Zapowiedź otwarcia cmentarza w Kamesznicy</a></li>
        <li><a href="{e(ITEMS['defilada-wisla-80']['url'])}" class="ext">Relacja z Wisły, 3 maja 2026</a></li>
      </ul>
    </div>
    <div class="aside-box">
      <h2>Jak powstał ten tekst</h2>
      <p>Opracowanie demonstracyjne na podstawie publikacji IPN i dzieje.pl. Relacje Związku traktowano jako źródło informacji o upamiętnieniu, nie o przebiegu wydarzeń z lat 1945–1947.</p>
    </div>
  </aside>
</div>
<section class="related" aria-labelledby="rel-title">
  <div class="wrap">
    <div class="rule-title"><h2 id="rel-title">Powiązane materiały</h2><a href="aktualnosci.html">Wszystkie <span class="arrow" aria-hidden="true">→</span></a></div>
    <div class="related-grid">{''.join(rel)}</div>
  </div>
</section>
</main>
"""
    return head(DEMO["title"], "Przykładowy artykuł z galerią, spisem treści i źródłami — wariant A.") + header("") + body + footer()


# ------------------------------------------------------------ kontekst historyczny
TIMELINE = [
    ("1942-09-20", "20 IX 1942", "Rozkaz nr 1/42 płk. Ignacego Oziewicza „Czesława” — umowna data powstania NSZ; formowanie trwało od lipca 1942 r.", "IPN — synteza", "https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html"),
    ("1943-08-01", "1 VIII 1943", "Płk Tadeusz Kurcyusz „Żegota” dowódcą NSZ.", "R. Wnuk, Dzieje Najnowsze 2021", "http://dx.doi.org/10.12775/DN.2021.1.05"),
    ("1944-03-07", "7 III 1944", "Umowa scaleniowa NSZ z AK; rozłam na NSZ-AK i NSZ-ZJ.", "R. Wnuk 2021", "http://dx.doi.org/10.12775/DN.2021.1.05"),
    ("1944-08", "VIII 1944", "Ok. 3,5 tys. żołnierzy NSZ w Powstaniu Warszawskim.", "IPN — synteza", "https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html"),
    ("1944-08-11", "11 VIII 1944", "Utworzenie Brygady Świętokrzyskiej.", "IPN — synteza", "https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html"),
    ("1944-12", "koniec 1944", "Stronnictwo Narodowe powołuje NZW — formację odrębną od NSZ.", "dzieje.pl", "https://dzieje.pl/node/142103"),
    ("1945-05-05", "5 V 1945", "Uwolnienie więźniarek podobozu w Holiszowie; liczby i przebieg sporne.", "Przystanek Historia (IPN)", "https://przystanekhistoria.pl/pa2/tematy/okupacja-niemiecka/43594,Jak-Brygada-Swietokrzyska-NSZ-ocalila-wiezniarki-niemieckiego-obozu-w-Holiszowie.html"),
    ("1947-02-15", "15 II 1947", "Aresztowanie ppłk. Stanisława Kasznicy, ostatniego komendanta NSZ-ZJ.", "IPN — synteza", "https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html"),
    ("1948-05-12", "12 V 1948", "Egzekucja Kasznicy; wyrok unieważniony w 1992 r.", "IPN — biogram", "https://ipn.gov.pl/pl/historia-z-ipn/225426,Stanislaw-Kasznica-19081948.html"),
    ("2011-02-03", "3 II 2011", "Ustawa ustanawiająca 1 marca Narodowym Dniem Pamięci „Żołnierzy Wyklętych” (dotyczy całego podziemia).", "Dz.U. 2011 poz. 160", "https://eli.gov.pl/eli/DU/2011/160/ogl/pol/pdf"),
    ("2012-11-09", "9 XI 2012", "Uchwała Sejmu w 70. rocznicę NSZ — ocena polityczna, nie ustalenie naukowe.", "M.P. 2012 poz. 890", "https://eli.gov.pl/eli/MP/2012/890/ogl/pol/pdf"),
]


def page_history():
    tl = "".join(f'<li><time datetime="{d}">{lab}</time><p>{e(t)}<small>Źródło: <a href="{e(u)}" class="ext">{e(s)}</a></small></p></li>' for d, lab, t, s, u in TIMELINE)
    body = f"""<main id="tresc">
<div class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Okruszki"><ol><li><a href="index.html">Strona główna</a></li><li><span aria-current="page">Kontekst historyczny</span></li></ol></nav>
    <h1>Kontekst historyczny</h1>
    <p>Krótkie wprowadzenie dla osób, które zaczynają. Każdy fakt ma źródło, a kwestie sporne opisujemy z podaniem stanowisk. Szczegóły: <a href="{HISTORY_REPORT}" class="ext">raport historyczny projektu</a>.</p>
  </div>
</div>
<div class="wrap ctx-layout">
  <section aria-labelledby="os-czasu">
    <div class="rule-title"><h2 id="os-czasu">Oś czasu</h2></div>
    <ol class="timeline">{tl}</ol>
  </section>
  <div>
    <section aria-labelledby="nazwy">
      <div class="rule-title"><h2 id="nazwy">Nazwy i formacje</h2></div>
      <table class="names-table">
        <caption class="sr-only">Nazwy organizacji i ich znaczenie</caption>
        <thead><tr><th scope="col">Skrót</th><th scope="col">Znaczenie</th></tr></thead>
        <tbody>
          <tr><th scope="row">NOW</th><td>Narodowa Organizacja Wojskowa Stronnictwa Narodowego; główny nurt scalał się z AK, część weszła do NSZ.</td></tr>
          <tr><th scope="row">ZJ</th><td>Organizacja Wojskowa Związek Jaszczurczy — struktura wojskowa Grupy „Szańca” (ONR „ABC”).</td></tr>
          <tr><th scope="row">NSZ</th><td>Narodowe Siły Zbrojne, od 1942 r. — z połączenia ZJ i części NOW.</td></tr>
          <tr><th scope="row">NSZ-AK</th><td>Część NSZ, która po umowie z 7 marca 1944 r. weszła do AK.</td></tr>
          <tr><th scope="row">NSZ-ZJ</th><td>Środowisko ONR „ABC”, które odrzuciło scalenie i działało dalej samodzielnie.</td></tr>
          <tr><th scope="row">NZW</th><td>Narodowe Zjednoczenie Wojskowe, powołane przez SN pod koniec 1944 r. — odrębne od NSZ.</td></tr>
        </tbody>
      </table>
      <p class="no-js-note" style="display:block;margin-top:8px">Źródła: IPN — synteza o NSZ; R. Wnuk 2021; dzieje.pl. Historia NSZ to nie to samo co dzisiejszy Związek Żołnierzy NSZ.</p>
    </section>
    <section class="issues" aria-labelledby="sporne" style="margin-top:36px">
      <div class="rule-title"><h2 id="sporne">Zagadnienia sporne i trudne</h2></div>
      <p><span class="legend-tag p">potwierdzone</span><span class="legend-tag s">sporne</span><span class="legend-tag i">interpretacja</span></p>
      <details id="brygada" open>
        <summary>Brygada Świętokrzyska i porozumienie z Wehrmachtem (1945)</summary>
        <div>
          <p><span class="legend-tag p">potwierdzone</span>W styczniu 1945 r. Brygada wycofała się na zachód na podstawie uzgodnień z lokalnymi dowódcami Wehrmachtu — potwierdzają to wszystkie odczytane źródła, w tym IPN.</p>
          <p><span class="legend-tag s">sporne</span>Ocena tego kroku: IPN podkreśla, że Brygada nie walczyła u boku Niemców przeciw Armii Czerwonej; publicystyka krytyczna (OKO.press, 2021), powołując się na raporty AK, kwalifikuje to jako kolaborację. Przebieg i liczby z Holiszowa (od „kilkuset” do ok. 1000 uwolnionych) również różnią się między źródłami.</p>
          <p><a href="https://ipn.gov.pl/pl/historia-z-ipn/229851,Narodowe-Sily-Zbrojne-19421946.html" class="ext">IPN — synteza</a> · <a href="https://oko.press/ipn-i-abw-uczcily-kolaborantow-z-brygady-swietokrzyskiej-nsz-wraca-deta-historia-o-holiszowie" class="ext">OKO.press — stanowisko krytyczne</a></p>
        </div>
      </details>
      <details>
        <summary>Przemoc wobec ludności cywilnej</summary>
        <div>
          <p><span class="legend-tag p">potwierdzone</span>Wierzchowiny, 6 czerwca 1945 r.: oddział NSZ (PAS) pod dowództwem Mieczysława Pazderskiego „Szarego” zabił ok. 194–196 cywilów, głównie prawosławnych Ukraińców. <span class="legend-tag s">sporne</span>Odpowiedzialność dowództwa pozostaje przedmiotem badań.</p>
          <p><span class="legend-tag p">potwierdzone</span>Okolice Kraśnika, 1942: według D. Libionki oddział NOW-AN, później włączony do NSZ, był sprawcą śmierci kilkudziesięciu zbiegów pochodzenia żydowskiego.</p>
          <p><a href="https://czasopisma.ipn.gov.pl/index.php/pis/article/view/588" class="ext">M. Zajączkowski, „Pamięć i Sprawiedliwość” 2006</a> · <a href="https://zagladazydow.pl/index.php/zz/article/view/777" class="ext">D. Libionka, „Zagłada Żydów” 7/2011</a></p>
          <p>Oceny konkretnych zdarzeń przypisujemy konkretnym oddziałom — bez przenoszenia ich na wszystkich żołnierzy i bez przemilczeń.</p>
        </div>
      </details>
      <details>
        <summary>Ideologia i stosunek do mniejszości</summary>
        <div>
          <p><span class="legend-tag p">potwierdzone</span>Badacze (m.in. S. Bębenek, K. Kaczmarski, R. Wnuk) wskazują na antysemityzm w propagandzie i światopoglądzie środowiska Grupy „Szańca”; jej starania o uznanie rządu RP w latach 1939–1941 nie powiodły się m.in. z powodu zarzutów antysemityzmu.</p>
          <p><span class="legend-tag i">interpretacja</span>Według R. Wnuka liderzy ONR „ABC” byli wrodzy demokracji i parlamentaryzmowi, co było jedną z przyczyn odrzucenia scalenia z AK przez NSZ-ZJ.</p>
        </div>
      </details>
      <details>
        <summary>Liczebność NSZ</summary>
        <div>
          <p><span class="legend-tag s">sporne</span>W 1944 r.: 58–65 tys. według R. Wnuka („Dzieje Najnowsze” 2021); ok. 90 tys. według Związku Żołnierzy NSZ. Podajemy oba ujęcia ze źródłem.</p>
        </div>
      </details>
    </section>
  </div>
</div>
</main>
"""
    return head("Kontekst historyczny", "Oś czasu, nazwy formacji i zagadnienia sporne — wariant A.") + header("historia") + body + footer()


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    pages = {
        "index.html": page_index(),
        "aktualnosci.html": page_list(),
        "artykul.html": page_article(),
        "historia.html": page_history(),
    }
    for name, content in pages.items():
        (OUT / name).write_text(content, encoding="utf-8", newline="\n")
        print("zapisano", name, len(content))
