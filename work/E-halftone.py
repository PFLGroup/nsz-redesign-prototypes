# Generator abstrakcyjnych ilustracji półtonowych dla wariantu E (ilustracje koncepcyjne, nie fotografie).
import math, random, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'public', '05-awangardowy', 'img')
def svg(name, w, h, step, fn, fg='#0d0d0c', bg='none', title=''):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">',
           f'<title>{title}</title>']
    if bg != 'none': out.append(f'<rect width="{w}" height="{h}" fill="{bg}"/>')
    out.append(f'<g fill="{fg}">')
    for y in range(step//2, h, step):
        for x in range(step//2, w, step):
            v = max(0.0, min(1.0, fn(x / w, y / h)))
            r = v * step * 0.62
            if r > 0.35: out.append(f'<circle cx="{x}" cy="{y}" r="{r:.1f}"/>')
    out.append('</g></svg>')
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write('\n'.join(out))
random.seed(7)
def ridge(u, v):
    line = 0.48 + 0.16*math.sin(u*5.1) + 0.07*math.sin(u*13+1) - 0.18*math.exp(-((u-0.62)/0.12)**2)
    if v < line: return 0.10 + 0.25*(1 - v/line)*0.4
    return 0.35 + 0.65*min(1, (v-line)*2.4)
def sheet(u, v):
    inside = 0.18 < u < 0.82 and 0.08 < v < 0.94
    if not inside: return 0.85
    if 0.16 < v < 0.20 and u < 0.6: return 0.55
    row = (v - 0.28) / 0.045
    if v > 0.26 and v < 0.86 and abs(row - round(row)) < 0.18 and u < 0.78 - 0.1*(round(row) % 3 == 2):
        return 0.38
    return 0.04
def field(u, v):
    hz = 0.42 + 0.03*math.sin(u*9)
    if v < hz: return 0.06 + 0.5*max(0, 1 - abs(u-0.3)/0.25)*max(0, (v-0.1))/0.4
    return 0.25 + 0.6*((v-hz)/(1-hz)) + 0.1*math.sin(u*40)*((v-hz)/(1-hz))
svg('ht-gora.svg', 960, 640, 12, ridge, title='Ilustracja koncepcyjna: półtonowy zarys pasma górskiego (nie jest fotografią)')
svg('ht-dokument.svg', 720, 960, 12, sheet, title='Ilustracja koncepcyjna: półtonowy zarys kartki dokumentu (nie jest reprodukcją archiwalną)')
svg('ht-pole.svg', 960, 640, 12, field, title='Ilustracja koncepcyjna: półtonowy krajobraz z horyzontem (nie jest fotografią)')
print('ok')
