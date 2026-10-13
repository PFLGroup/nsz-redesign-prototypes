# Generuje artykul.html wariantu C z demo_article (content.json); nagłówek/stopkę wstawia potem inject.py.
import json, re, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
V = ROOT / 'public' / '03-tradycyjny'
data = json.loads((ROOT / 'public/assets/data/content.json').read_text(encoding='utf-8'))
a = data['demo_article']
items = {i['id']: i for i in data['items']}
e = html.escape
NL = '\n'


def slug(s):
    t = s.lower()
    for x, y in zip('ąćęłńóśźż„”', 'acelnoszz  '):
        t = t.replace(x, y)
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


secs = a['sections']
toc = NL.join(f'            <li><a href="#{slug(s["heading"])}">{e(s["heading"])}</a></li>' for s in secs)
body = []
for n, s in enumerate(secs):
    sid = slug(s['heading'])
    if s['heading'] == 'Słowniczek':
        dl = []
        for p in s['paragraphs']:
            term, _, desc = p.partition(' — ')
            dl.append(f'          <dt>{e(term)}</dt><dd>{e(desc)}</dd>')
        inner = '        <dl class="glossary">' + NL + NL.join(dl) + NL + '        </dl>'
    else:
        inner = NL.join(f'        <p>{e(p)}</p>' for p in s['paragraphs'])
    body.append(f'        <section aria-labelledby="{sid}">{NL}          <h2 id="{sid}">{e(s["heading"])}</h2>{NL}{inner}{NL}        </section>')
    if n == 1:  # galeria po drugiej sekcji
        slides = []
        for g in a['gallery']:
            slides.append(
                '          <div data-slide>' + NL +
                '            <figure class="photo-ph">' + NL +
                f'              <div class="ph" role="img" aria-label="{e(g["alt"])}">Miejsce na fotografię archiwalną — wymaga licencji</div>' + NL +
                f'              <figcaption>{e(g["caption"])}. <span class="cred">Autor: do ustalenia · licencja: nieustalona</span></figcaption>' + NL +
                '            </figure>' + NL +
                '          </div>')
        body.append(
            '        <section class="gallery" aria-labelledby="h-gal" data-gallery>' + NL +
            '          <div class="gallery-head">' + NL +
            '            <h2 id="h-gal">Galeria</h2>' + NL +
            '            <p class="status" data-status aria-live="polite">3 ilustracje</p>' + NL +
            '          </div>' + NL +
            '          <div class="gallery-track" data-track>' + NL + NL.join(slides) + NL + '          </div>' + NL +
            '          <div class="gallery-controls">' + NL +
            '            <button type="button" class="btn" data-prev aria-label="Poprzednia ilustracja">←<span class="lbl"> Poprzednia</span></button>' + NL +
            '            <div data-dots></div>' + NL +
            '            <button type="button" class="btn" data-next aria-label="Następna ilustracja"><span class="lbl">Następna </span>→</button>' + NL +
            '          </div>' + NL +
            '          <p class="no-js-note">Bez JavaScriptu wszystkie ilustracje są widoczne jedna pod drugą.</p>' + NL +
            '        </section>')

src = NL.join(f'            <li><a href="{e(s["url"])}">{e(s["label"])}</a> <span class="acc">(dostęp: {e(s["accessed"])})</span></li>' for s in a['sources'])
rel = []
for r in ['kamesznica-cmentarz', 'defilada-wisla-80', 'nsz-1942-1946']:
    i = items[r]
    d = i['date']
    rel.append(
        '        <li>' + NL +
        f'          <p class="kicker">{e(i["category"])}</p>' + NL +
        f'          <h3><a href="{e(i["url"])}">{e(i["title"])}</a></h3>' + NL +
        f'          <p class="dateline"><time datetime="{d}">{int(d[8:10])}.{d[5:7]}.{d[:4]}</time></p>' + NL +
        '        </li>')
words = sum(len(p.split()) for s in secs for p in s['paragraphs']) + len(a['lead'].split())
mins = max(1, round(words / 200))
note = a['author_note']
note = note[0].lower() + note[1:]

page = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<link rel="icon" href="data:,">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Tekst numeru: zgrupowanie „Bartka” · Kronika · Wariant C · Prototyp ZŻNSZ</title>
<meta name="description" content="{e(a['lead'][:155])}">
<link rel="preload" href="fonts/playfair-display-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/source-serif-4-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../assets/shared/a11y.css">
<link rel="stylesheet" href="kronika.css">
</head>
<body>
<div class="progress" data-reading-progress role="progressbar" aria-label="Postęp czytania" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"></div>
<!--HEADER-->

<main id="tresc" tabindex="-1">
  <article aria-labelledby="art-title">
    <div class="wrap">
    <header class="article-head">
      <nav class="crumbs" aria-label="Okruszki">
        <ol><li><a href="index.html">Strona główna</a></li><li><a href="aktualnosci.html?kat=historia">Historia</a></li><li aria-current="page">Tekst numeru</li></ol>
      </nav>
      <p class="kicker">Dział historyczny · Tekst numeru <span class="demo-tag">tekst demonstracyjny</span></p>
      <h1 id="art-title">{e(a['title'])}</h1>
      <p class="lead">{e(a['lead'])}</p>
      <ul class="art-meta">
        <li><strong>Data:</strong> <time datetime="{a['date']}">13 października 2026</time></li>
        <li><strong>Autor:</strong> brak podpisu — {e(note)}</li>
        <li><strong>Czas czytania:</strong> ok. {mins} min</li>
      </ul>
      <p class="demo-notice"><strong>{e(a['label'])}.</strong> Opracowanie przygotowano do porównania projektów; nie zawiera cytatów ani danych spoza wymienionych źródeł.</p>
    </header>

    <div class="article-layout">
      <nav class="toc" aria-label="Spis treści" data-toc>
        <details open>
          <summary>W tym tekście</summary>
          <ol>
{toc}
            <li><a href="#zrodla">Źródła</a></li>
          </ol>
        </details>
      </nav>

      <div class="article-body" data-article-body>
{NL.join(body)}
        <section class="sources" aria-labelledby="zrodla">
          <h2 id="zrodla">Źródła</h2>
          <ol>
{src}
          </ol>
        </section>
        <div class="backnav">
          <a class="btn" href="aktualnosci.html">← Wróć do listy materiałów</a>
          <a class="btn" href="index.html">Strona główna</a>
        </div>
      </div>

      <aside class="margin-col" aria-label="Na marginesie">
        <div class="note">
          <h2>Na marginesie</h2>
          <p>NSZ i NZW to różne formacje. Oddział „Bartka” literatura określa jako zgrupowanie NSZ.</p>
        </div>
        <div class="note">
          <h2>Daty w tekście</h2>
          <p><time datetime="1946-05-03">3 V 1946</time> — przemarsz przez Wisłę<br>
          <time datetime="1947-12-01">1 XII 1947</time> — śmierć H. Flamego<br>
          <time datetime="2026-05-07">7 V 2026</time> — pogrzeb w Kamesznicy</p>
        </div>
        <div class="note">
          <h2>Uwaga redakcyjna</h2>
          <p>Relacje Związku potraktowano jako źródło o upamiętnieniu, nie jako podstawę rekonstrukcji wydarzeń z lat 1945–1947.</p>
        </div>
      </aside>
    </div>
    </div>
  </article>

  <section class="related" aria-labelledby="h-rel">
    <div class="wrap">
      <h2 class="sec-title" id="h-rel">Powiązane materiały</h2>
      <ul class="related-grid">
{NL.join(rel)}
      </ul>
    </div>
  </section>
</main>

<!--FOOTER-->

<script src="../assets/data/content.js"></script>
<script src="../assets/shared/proto.js"></script>
</body>
</html>
'''
(V / 'artykul.html').write_text(page, encoding='utf-8', newline='\n')
print('artykul.html ok,', words, 'słów,', mins, 'min')
