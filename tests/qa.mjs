// QA prototypów NSZ: serwer statyczny pod prefiksem repo + Playwright (systemowy Chrome) + axe-core.
// Uruchomienie: node tests/qa.mjs [--base=https://pflgroup.github.io/nsz-redesign-prototypes/] [--only=01-nowoczesny]
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright-core';

const here = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(here, '..');
const PUBLIC = path.join(ROOT, 'public');
const PREFIX = '/nsz-redesign-prototypes/';
const OUT = path.join(ROOT, 'work', 'qa');
const SHOTS = path.join(OUT, 'screens');
fs.mkdirSync(SHOTS, { recursive: true });

const args = Object.fromEntries(process.argv.slice(2).map(a => a.replace(/^--/, '').split('=')));
const VARIANTS = ['01-nowoczesny', '02-ultranowoczesny', '03-tradycyjny', '04-dziedzictwo', '05-awangardowy']
  .filter(v => !args.only || args.only.split(',').includes(v));
const PAGES = ['index.html', 'aktualnosci.html', 'artykul.html'];
const WIDTHS = [360, 390, 768, 1280, 1440];
const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const AXE = fs.readFileSync(path.join(here, 'node_modules', 'axe-core', 'axe.min.js'), 'utf8');

const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.webp': 'image/webp', '.woff2': 'font/woff2', '.woff': 'font/woff', '.txt': 'text/plain', '.md': 'text/plain' };

function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, r) => {
      let u = decodeURIComponent(req.url.split('?')[0]);
      if (!u.startsWith(PREFIX)) { r.writeHead(404); return r.end('outside prefix'); }
      let f = path.join(PUBLIC, u.slice(PREFIX.length));
      if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
      if (!f.startsWith(PUBLIC) || !fs.existsSync(f)) { r.writeHead(404); return r.end('404'); }
      r.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
      fs.createReadStream(f).pipe(r);
    });
    srv.listen(0, '127.0.0.1', () => res(srv));
  });
}

const srv = args.base ? null : await serve();
const BASE = args.base || `http://127.0.0.1:${srv.address().port}${PREFIX}`;
const browser = await chromium.launch({ executablePath: CHROME, headless: true });
const results = [];

async function auditPage(variant, pg, width) {
  const ctx = await browser.newContext({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  const errors = [], failed = [], external = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push(String(e)));
  page.on('requestfailed', q => failed.push(q.url()));
  page.on('response', resp => { if (resp.status() >= 400) failed.push(resp.status() + ' ' + resp.url()); });
  page.on('request', q => {
    const u = q.url();
    if (!u.startsWith(BASE.replace(/nsz-redesign-prototypes\/$/, '')) && !u.startsWith('data:')) external.push(u);
  });
  const url = BASE + variant + '/' + pg;
  await page.goto(url, { waitUntil: 'networkidle' });
  const m = await page.evaluate(() => {
    const de = document.documentElement;
    const overflowX = de.scrollWidth - de.clientWidth;
    const offenders = [];
    if (overflowX > 1) {
      document.querySelectorAll('body *').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.right > de.clientWidth + 1 && r.width > 0 && getComputedStyle(el).position !== 'fixed') offenders.push(el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : ''));
      });
    }
    const small = [];
    document.querySelectorAll('a[href], button, input, select, [role=button]').forEach(el => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      if (r.width === 0 || cs.visibility === 'hidden') return;
      // linki w akapitach tekstu są wyłączone z celu 44px (WCAG 2.5.8 wyjątek inline)
      if (el.tagName === 'A' && el.closest('p, li p, figcaption, td, dd') && cs.display === 'inline') return;
      if (r.height < 24 || r.width < 24) small.push((el.textContent || el.getAttribute('aria-label') || el.tagName).trim().slice(0, 30) + ` ${Math.round(r.width)}x${Math.round(r.height)}`);
    });
    const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => +h.tagName[1]);
    let skip = 0; for (let i = 1; i < hs.length; i++) if (hs[i] - hs[i - 1] > 1) skip++;
    return {
      overflowX, offenders: [...new Set(offenders)].slice(0, 8),
      smallTargets: small.slice(0, 12), smallCount: small.length,
      h1: hs.filter(h => h === 1).length, headingSkips: skip,
      imgNoAlt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
      brokenImg: [...document.images].filter(i => i.complete && i.naturalWidth === 0).length,
      skipLink: !!document.querySelector('a[href^="#"].skip-link, a.skip-link'),
      banner: /Prototyp koncepcyjny/.test(document.body.innerText),
      noindex: /noindex/.test(document.querySelector('meta[name=robots]')?.content || ''),
      lang: document.documentElement.lang,
      title: document.title,
    };
  });
  await page.addScriptTag({ content: AXE });
  const axe = await page.evaluate(async () => {
    const r = await window.axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } });
    return r.violations.map(v => ({ id: v.id, impact: v.impact, n: v.nodes.length, sample: v.nodes[0]?.target?.join(' ') }));
  });
  if (width === 390 || width === 1440) {
    await page.screenshot({ path: path.join(SHOTS, `${variant}_${pg.replace('.html', '')}_${width}.png`), fullPage: true });
  }
  await ctx.close();
  return { variant, page: pg, width, ...m, axe, errors, failed, external };
}

async function interactions(variant) {
  const out = { variant };
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await ctx.newPage();
  const errs = []; page.on('pageerror', e => errs.push(String(e)));
  // Menu mobilne
  await page.goto(BASE + variant + '/index.html', { waitUntil: 'networkidle' });
  const menuBtn = page.locator('button[aria-controls][aria-expanded]:visible').first();
  if (await menuBtn.count()) {
    await menuBtn.click();
    out.menuOpens = (await menuBtn.getAttribute('aria-expanded')) === 'true';
    await page.keyboard.press('Escape');
    out.menuEscCloses = (await menuBtn.getAttribute('aria-expanded')) === 'false';
  } else out.menuOpens = 'brak przycisku aria-expanded widocznego w 390px';
  // Klawiatura: pierwszy Tab = skip link
  await page.goto(BASE + variant + '/index.html', { waitUntil: 'networkidle' });
  await page.keyboard.press('Tab');
  out.firstTab = await page.evaluate(() => (document.activeElement?.textContent || '').trim().slice(0, 40));
  out.focusVisible = await page.evaluate(() => {
    const el = document.activeElement; const cs = getComputedStyle(el);
    return cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0 || cs.boxShadow !== 'none';
  });
  // Filtry + stan pusty
  await page.goto(BASE + variant + '/aktualnosci.html', { waitUntil: 'networkidle' });
  const total = await page.locator('[data-item]').count();
  const search = page.locator('input[data-search]').first();
  if (await search.count()) {
    await search.fill('zzzqqq-brak');
    out.emptyState = await page.locator('[data-empty]').first().isVisible();
    const clear = page.locator('[data-clear-filters]:visible').first();
    if (await clear.count()) { await clear.click(); }
    out.afterClear = await page.locator('[data-item]:visible').count();
  }
  const fbtn = page.locator('[data-filter]:not([data-filter="all"])').first();
  if (await fbtn.count()) {
    await fbtn.click();
    out.filterReduces = `${await page.locator('[data-item]:visible').count()}/${total}`;
  }
  await page.goto(BASE + variant + '/aktualnosci.html?q=Holisz', { waitUntil: 'networkidle' });
  out.queryParam = await page.locator('[data-item]:visible').count();
  // Galeria
  await page.goto(BASE + variant + '/artykul.html', { waitUntil: 'networkidle' });
  const g = page.locator('[data-gallery]').first();
  if (await g.count()) {
    const before = await g.getAttribute('data-index');
    await g.locator('[data-next]').first().click();
    out.galleryNext = before + '→' + (await g.getAttribute('data-index'));
    await g.locator('[data-next]').first().focus();
    await page.keyboard.press('ArrowLeft');
    out.galleryKeyboard = await g.getAttribute('data-index');
  } else out.galleryNext = 'brak [data-gallery]';
  out.toc = await page.locator('[data-toc] a').count();
  out.progress = await page.locator('[data-reading-progress]').count();
  // Linki wewnętrzne
  const links = new Set();
  for (const pg of PAGES) {
    await page.goto(BASE + variant + '/' + pg, { waitUntil: 'domcontentloaded' });
    (await page.$$eval('a[href]', as => as.map(a => a.href))).forEach(h => links.add(h.split('#')[0]));
  }
  const broken = [];
  for (const l of links) {
    if (!l.startsWith(BASE.replace(/nsz-redesign-prototypes\/$/, '')) || !l.includes('nsz-redesign-prototypes')) continue;
    const r = await page.request.get(l); if (r.status() >= 400) broken.push(r.status() + ' ' + l);
  }
  out.internalLinks = links.size; out.brokenLinks = broken;
  // Bez JS treść widoczna
  const nojs = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  const p2 = await nojs.newPage();
  await p2.goto(BASE + variant + '/aktualnosci.html');
  out.noJsItemsVisible = await p2.locator('[data-item]:visible').count();
  await p2.goto(BASE + variant + '/artykul.html');
  out.noJsArticleWords = (await p2.locator('main').innerText()).split(/\s+/).length;
  await nojs.close();
  // Reduced motion
  const rm = await browser.newContext({ reducedMotion: 'reduce' });
  const p3 = await rm.newPage();
  await p3.goto(BASE + variant + '/index.html', { waitUntil: 'networkidle' });
  out.reducedMotionClass = await p3.evaluate(() => document.documentElement.classList.contains('reduce-motion'));
  await rm.close();
  // Powiększenie tekstu 200%
  await page.goto(BASE + variant + '/index.html', { waitUntil: 'networkidle' });
  out.zoom200overflow = await page.evaluate(() => { document.documentElement.style.fontSize = '200%'; return document.documentElement.scrollWidth - document.documentElement.clientWidth; });
  out.pageErrors = errs;
  await ctx.close();
  return out;
}

for (const v of VARIANTS) {
  for (const pg of PAGES) for (const w of WIDTHS) {
    try { results.push(await auditPage(v, pg, w)); }
    catch (e) { results.push({ variant: v, page: pg, width: w, fatal: String(e) }); }
  }
}
const inter = [];
for (const v of VARIANTS) { try { inter.push(await interactions(v)); } catch (e) { inter.push({ variant: v, fatal: String(e) }); } }
// Selektor
const sel = await auditPage('', 'index.html', 390).catch(e => ({ fatal: String(e) }));
const sel2 = await auditPage('', 'index.html', 1440).catch(e => ({ fatal: String(e) }));

await browser.close(); srv?.close();
const report = { date: new Date().toISOString(), base: BASE, results, interactions: inter, selector: [sel, sel2] };
fs.writeFileSync(path.join(OUT, 'qa-results.json'), JSON.stringify(report, null, 1));

// Skrót
const lines = [];
for (const v of VARIANTS) {
  const rs = results.filter(r => r.variant === v);
  const fatal = rs.filter(r => r.fatal);
  const ov = rs.filter(r => r.overflowX > 1).map(r => `${r.page}@${r.width}(+${r.overflowX}px: ${r.offenders?.join(',')})`);
  const axeIds = {}; rs.forEach(r => (r.axe || []).forEach(a => { axeIds[a.id] = (axeIds[a.id] || 0) + a.n; }));
  const errs = [...new Set(rs.flatMap(r => r.errors || []))];
  const fails = [...new Set(rs.flatMap(r => r.failed || []))];
  const ext = [...new Set(rs.flatMap(r => r.external || []))];
  const small = Math.max(0, ...rs.map(r => r.smallCount || 0));
  lines.push(`## ${v}`,
    `- fatal: ${fatal.length ? fatal.map(f => f.page + '@' + f.width + ' ' + f.fatal).join('; ') : 0}`,
    `- przewijanie poziome: ${ov.length ? ov.join('; ') : 'brak'}`,
    `- axe: ${Object.keys(axeIds).length ? Object.entries(axeIds).map(([k, n]) => k + '×' + n).join(', ') : 'brak naruszeń'}`,
    `- błędy konsoli: ${errs.length ? errs.join(' | ') : 'brak'}`,
    `- nieudane zasoby: ${fails.length ? fails.join(' | ') : 'brak'}`,
    `- zapytania zewnętrzne: ${ext.length ? ext.join(' | ') : 'brak'}`,
    `- max elementów <24px: ${small} ${small ? '(' + rs.find(r => r.smallCount === small)?.smallTargets.join('; ') + ')' : ''}`,
    `- h1/strona: ${rs.map(r => r.h1).join(',')} | przeskoki nagłówków: ${Math.max(0, ...rs.map(r => r.headingSkips || 0))} | img bez alt: ${Math.max(0, ...rs.map(r => r.imgNoAlt || 0))} | skip: ${rs.every(r => r.skipLink)} | baner: ${rs.every(r => r.banner)} | noindex: ${rs.every(r => r.noindex)}`,
    `- interakcje: ${JSON.stringify(inter.find(i => i.variant === v))}`, '');
}
lines.push('## selektor', JSON.stringify([sel, sel2].map(s => ({ w: s.width, overflowX: s.overflowX, axe: s.axe, errors: s.errors, failed: s.failed, external: s.external, banner: s.banner, noindex: s.noindex }))));
fs.writeFileSync(path.join(OUT, 'qa-summary.md'), `# QA ${report.date}\nBase: ${BASE}\n\n` + lines.join('\n'));
console.log(lines.join('\n'));
