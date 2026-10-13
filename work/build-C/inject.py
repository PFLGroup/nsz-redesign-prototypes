# Wstawia nagłówek i stopkę z index.html wariantu C do pozostałych widoków (<!--HEADER--> / <!--FOOTER-->).
import pathlib

V = pathlib.Path(__file__).resolve().parents[2] / 'public' / '03-tradycyjny'
idx = (V / 'index.html').read_text(encoding='utf-8')
head = idx[idx.index('<a class="skip-link"'):idx.index('</header>') + len('</header>')]
foot = idx[idx.index('<footer class="site-footer'):idx.index('</footer>') + len('</footer>')]

for name in ['aktualnosci.html', 'artykul.html']:
    p = V / name
    s = p.read_text(encoding='utf-8')
    if '<!--HEADER-->' not in s:
        print(name, 'pominięty (brak znacznika)')
        continue
    h = head
    if name == 'artykul.html':
        h = h.replace('<li><a href="aktualnosci.html?kat=historia">Historia</a></li>',
                      '<li><a href="aktualnosci.html?kat=historia" aria-current="true">Historia</a></li>', 1)
    else:
        h = h.replace('<li><a href="aktualnosci.html?kat=aktualnosc">Aktualności</a></li>',
                      '<li><a href="aktualnosci.html?kat=aktualnosc" aria-current="true">Aktualności</a></li>', 1)
    for a in ('archiwum', 'zwiazek', 'multimedia'):
        h = h.replace(f'href="#{a}"', f'href="index.html#{a}"')
    s = s.replace('<!--HEADER-->', h).replace('<!--FOOTER-->', foot)
    p.write_text(s, encoding='utf-8', newline='\n')
    print(name, 'ok')
