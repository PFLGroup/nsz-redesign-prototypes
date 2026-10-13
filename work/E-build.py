# Generator podstron wariantu E (aktualnosci.html, artykul.html) z content.json.
# Nagłówek, indeks i stopka są wycinane z index.html, by były identyczne na wszystkich widokach.
import json, html, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
E = os.path.join(ROOT, 'public', '05-awangardowy')
data = json.load(open(os.path.join(ROOT, 'public', 'assets', 'data', 'content.json'), encoding='utf-8'))
idx = open(os.path.join(E, 'index.html'), encoding='utf-8').read()
esc = html.escape
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
MON = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia',
       'września', 'października', 'listopada', 'grudnia']


def rdate(iso):
    y, m, d = iso.split('-')
    return '%d·%s' % (int(d), ROM[int(m) - 1]), y


def pldate(iso):
    y, m, d = iso.split('-')
    return '%d %s %s' % (int(d), MON[int(m) - 1], y)


head_start = idx[:idx.index('<title>')]
head_rest = idx[idx.index('<link rel="preload"'):idx.index('</head>')]
body_top = idx[idx.index('<body>'):idx.index('<main id="tresc"')]
footer = idx[idx.index('<footer class="foot">'):]


def fix_nav(top, current):
    for h in ('historia', 'teczki', 'zwiazek'):
        top = top.replace('href="#%s"' % h, 'href="index.html#%s"' % h)
    if current:
        top = top.replace('<a href="%s"><span class="num">' % current,
                          '<a href="%s" aria-current="page"><span class="num">' % current, 1)
    return top


def fix_foot(f):
    for h in ('historia', 'teczki'):
        f = f.replace('href="#%s"' % h, 'href="index.html#%s"' % h)
    return f


def page(title, desc, main, current=None):
    return (head_start + '<title>%s</title>\n<meta name="description" content="%s">\n' % (esc(title), esc(desc))
            + head_rest + '</head>\n' + fix_nav(body_top, current) + main + '\n' + fix_foot(footer))


TYPES = [('aktualnosc', 'Aktualności'), ('wydarzenie', 'Wydarzenia'), ('historia', 'Historia'),
         ('biogram', 'Biogramy'), ('dokument', 'Dokumenty')]
TLAB = {'aktualnosc': 'Aktualność', 'wydarzenie': 'Wydarzenie', 'historia': 'Opracowanie',
        'biogram': 'Biogram', 'dokument': 'Dokument'}
items = sorted(data['items'], key=lambda i: i['date'], reverse=True)
byid = {i['id']: i for i in data['items']}
demo = data['demo_article']


def row(it, num=None):
    dd, yy = rdate(it['date'])
    place = '<br>%s' % esc(it['place']) if it.get('place') else ''
    flag = '<span class="note">%s</span>' % esc(it['editorial_flag']) if it.get('editorial_flag') else ''
    n = '<span class="list-num">%02d</span>' % num if num is not None else ''
    red = ' red' if it['type'] == 'aktualnosc' else ''
    return ('<article class="row">\n  <p class="row-date">%s<b>%s</b>%s</p>\n'
            '  <div><h3><a class="ext" href="%s">%s</a></h3>\n  <p>%s</p>%s</div>\n'
            '  <p class="row-meta"><span class="tag%s">%s</span><br>%s%s<br>Autor: %s</p>\n</article>'
            % (n, dd, yy, esc(it['url']), esc(it['title']), esc(it['summary']), flag,
               red, TLAB[it['type']], esc(it['category']), place, esc(it['author'] or 'nie podano')))


rows = []
dd, yy = rdate(demo['date'])
rows.append('<li data-item data-cat="historia demo" data-text="%s"><article class="row">\n'
            '  <p class="row-date"><span class="list-num">00</span><b>%s</b>%s</p>\n'
            '  <div><h3><a href="artykul.html">%s</a></h3>\n  <p>%s</p><span class="note">%s.</span></div>\n'
            '  <p class="row-meta"><span class="tag red">Tekst demonstracyjny</span><br>Redakcja prototypu</p>\n</article></li>'
            % (esc(demo['title'] + ' ' + demo['lead'] + ' Bartek Kamesznica Lawina tekst demonstracyjny'),
               dd, yy, esc(demo['title']), esc(demo['lead']), esc(demo['label'])))
for n, it in enumerate(items, 1):
    text = ' '.join([it['title'], it['summary'], it.get('place', ''), ' '.join(it.get('tags', [])),
                     it['category'], TLAB[it['type']]])
    rows.append('<li data-item data-cat="%s" data-text="%s">%s</li>' % (it['type'], esc(text), row(it, n)))

filters = '\n      '.join('<button type="button" data-filter="%s" aria-pressed="false">%s</button>' % kv for kv in TYPES)
main = '''<main id="tresc" tabindex="-1">
<div class="wrap" data-filter-scope>
  <header class="page-head">
    <nav class="crumbs" aria-label="Okruszki"><a href="index.html">Strona główna</a> / Aktualności i materiały</nav>
    <h1>Aktualności <span class="red">i materiały</span></h1>
    <p>Indeks materiałów prototypu: bieżąca działalność Związku i opracowania historyczne. Tytuły ze strzałką (↗) prowadzą do serwisu źródłowego nsz.com.pl; tekst demonstracyjny — do przykładowego artykułu.</p>
  </header>
  <div class="tools">
    <fieldset class="filters">
      <legend>Rodzaj materiału</legend>
      <button type="button" data-filter="all" aria-pressed="true">Wszystkie</button>
      %s
    </fieldset>
    <form class="search" role="search">
      <label for="q">Szukaj w materiałach</label>
      <div class="qs-row qs"><input id="q" type="search" name="q" data-search autocomplete="off" placeholder="np. Kamesznica, NZW, Holiszów"><button type="submit">Szukaj</button></div>
    </form>
  </div>
  <div class="status-row"><p data-count role="status" style="margin:12px 0">Materiały: %d</p><button type="button" class="clear-btn" data-clear-filters>Wyczyść filtry</button></div>
  <h2 class="sr-only" id="lista-h">Lista materiałów</h2>
  <ol class="ledger" aria-labelledby="lista-h">
%s
  </ol>
  <div class="empty" data-empty hidden>
    <p>Brak materiałów dla tych kryteriów.</p>
    <span>Zmień słowo lub rodzaj materiału albo </span><button type="button" class="clear-btn" data-clear-filters>wyczyść filtry</button>
  </div>
  <a class="big-link" href="index.html#historia" style="margin:48px 0 72px"><span>Rozdziały historii 01–07</span><span aria-hidden="true">→</span></a>
</div>
</main>''' % (filters, len(rows), '\n'.join(rows))
open(os.path.join(E, 'aktualnosci.html'), 'w', encoding='utf-8').write(
    page('Aktualności i materiały — wariant E | Prototyp NSZ',
         'Lista materiałów z filtrem i wyszukiwarką — prototyp koncepcyjny E.', main, 'aktualnosci.html'))


# ---------- artykuł ----------
def slug(s):
    s = s.lower()
    for a, b in zip('ąćęłńóśźż', 'acelnoszz'):
        s = s.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


secs = demo['sections']
toc = '\n'.join('        <li><a href="#%s"><span class="n">%02d</span>%s</a></li>' % (slug(s['heading']), i, esc(s['heading']))
                for i, s in enumerate(secs, 1))
imgs = [('img/ht-pole.svg', 960, 640), ('img/ht-gora.svg', 960, 640), ('img/ht-dokument.svg', 720, 960)]
gal = demo['gallery']
slides = '\n'.join(
    '  <figure data-slide><img src="%s" width="%d" height="%d" alt="%s — ilustracja koncepcyjna." loading="lazy">'
    '<figcaption><span class="mono">%02d / %02d · ilustracja koncepcyjna</span>%s</figcaption></figure>'
    % (imgs[k][0], imgs[k][1], imgs[k][2], esc(g['alt']), k + 1, len(gal), esc(g['caption'])) for k, g in enumerate(gal))
gallery = '''<section class="gallery" data-gallery aria-labelledby="gal-h" tabindex="0">
  <div class="gallery-head"><h2 id="gal-h" style="font:inherit;margin:0">Galeria · miejsca na materiały</h2><span data-status aria-live="polite"></span></div>
%s
  <div class="gallery-ctrl"><button type="button" data-prev aria-label="Poprzedni slajd">←</button><div class="dots" data-dots></div><button type="button" data-next aria-label="Następny slajd">→</button></div>
</section>''' % slides
body = []
for i, s in enumerate(secs, 1):
    sid = slug(s['heading'])
    gloss = s['heading'] == 'Słowniczek'
    ps = []
    for p in s['paragraphs']:
        if gloss and ' — ' in p:
            term, rest = p.split(' — ', 1)
            ps.append('<p><b>%s</b> — %s</p>' % (esc(term), esc(rest)))
        else:
            ps.append('<p>%s</p>' % esc(p))
    body.append('<section id="%s" aria-labelledby="h-%s"%s><h2 id="h-%s"><span class="n" aria-hidden="true">%02d</span><span>%s</span></h2>\n%s\n</section>'
                % (sid, sid, ' class="gloss"' if gloss else '', sid, i, esc(s['heading']), '\n'.join(ps)))
    if i == 2:
        body.append(gallery)
srcs = '\n'.join('<li><a class="ext" href="%s">%s</a> <span class="mono">dostęp %s</span></li>'
                 % (esc(x['url']), esc(x['label']), pldate(x['accessed'])) for x in demo['sources'])
rel = ''.join('<li>%s</li>' % row(byid[r]) for r in ['kamesznica-cmentarz', 'defilada-wisla-80', '84-rocznica'])
main = '''<div class="progress" data-reading-progress role="progressbar" aria-label="Postęp czytania" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"></div>
<main id="tresc" tabindex="-1">
<article>
  <header class="art-head wrap">
    <nav class="crumbs" aria-label="Okruszki"><a href="index.html">Strona główna</a> / <a href="aktualnosci.html">Aktualności i materiały</a> / Artykuł</nav>
    <p class="art-label">%s</p>
    <h1>%s</h1>
    <dl class="art-meta">
      <div><dt>Data</dt><dd><time datetime="%s">%s</time></dd></div>
      <div><dt>Autor</dt><dd>brak podpisu autora — %s</dd></div>
      <div><dt>Dział</dt><dd>Historia · Ludzie · Pamięć</dd></div>
      <div><dt>Czas czytania</dt><dd>ok. 4 min</dd></div>
    </dl>
    <p class="art-lead">%s</p>
  </header>
  <div class="wrap art-grid">
    <nav class="toc" data-toc aria-labelledby="toc-h">
      <h2 id="toc-h">Spis rozdziałów</h2>
      <ol>
%s
        <li><a href="#zrodla"><span class="n">§</span>Źródła</a></li>
      </ol>
      <a class="back" href="aktualnosci.html">← Wróć do listy materiałów</a>
    </nav>
    <div class="art-body" data-article-body>
%s
      <section class="sources" id="zrodla" aria-labelledby="zr-h">
        <h2 id="zr-h">Źródła</h2>
        <ol>
%s
        </ol>
      </section>
      <section class="related" aria-labelledby="rel-h">
        <h2 id="rel-h">Powiązane materiały</h2>
        <ol class="ledger">%s</ol>
      </section>
      <nav class="art-nav" aria-label="Nawigacja po materiałach">
        <a href="aktualnosci.html"><small>Wróć</small>Wszystkie materiały</a>
        <a href="index.html#historia"><small>Dalej</small>Rozdziały historii NSZ</a>
      </nav>
    </div>
  </div>
</article>
</main>''' % (esc(demo['label']), esc(demo['title']), demo['date'], pldate(demo['date']), esc(demo['author_note']),
              esc(demo['lead']), toc, '\n'.join(body), srcs, rel)
open(os.path.join(E, 'artykul.html'), 'w', encoding='utf-8').write(
    page('Od operacji „Lawina” do Kamesznicy — wariant E | Prototyp NSZ',
         'Przykładowy artykuł (tekst demonstracyjny) — prototyp koncepcyjny E.', main))
print('ok')
