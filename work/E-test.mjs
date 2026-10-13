// Testy wariantu E przez Chrome DevTools Protocol (bez zależności; Node >= 22 ma globalny WebSocket).
// Uruchom: node work/E-test.mjs  (startuje własny headless Chrome na porcie 9339)
import { spawn } from 'node:child_process';
import { setTimeout as sleep } from 'node:timers/promises';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9339;
const BASE = (process.env.E_BASE || 'http://127.0.0.1:8765/') + '05-awangardowy/';
const prof = mkdtempSync(join(tmpdir(), 'e-cdp-'));
const proc = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${prof}`,
  '--disable-gpu', '--no-first-run', 'about:blank'], { stdio: 'ignore' });

let ws, id = 0; const pending = new Map(); const events = [];
async function connect() {
  for (let i = 0; i < 50; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${PORT}/json`)).json();
      const page = list.find(t => t.type === 'page');
      if (page) { ws = new WebSocket(page.webSocketDebuggerUrl); break; }
    } catch { }
    await sleep(200);
  }
  await new Promise(r => ws.addEventListener('open', r));
  ws.addEventListener('message', m => {
    const d = JSON.parse(m.data);
    if (d.id && pending.has(d.id)) { pending.get(d.id)(d); pending.delete(d.id); }
    else events.push(d);
  });
}
const send = (method, params = {}) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
async function ev(expr) {
  const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
  if (r.result.exceptionDetails) throw new Error(JSON.stringify(r.result.exceptionDetails));
  return r.result.result.value;
}
async function go(url, w) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 800 });
  events.length = 0;
  await send('Page.navigate', { url });
  await sleep(900);
}
async function key(k, code, kc) {
  await send('Input.dispatchKeyEvent', { type: 'keyDown', key: k, code, windowsVirtualKeyCode: kc });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code, windowsVirtualKeyCode: kc });
}
const results = []; const ok = (name, cond, info = '') => results.push({ name, pass: !!cond, info });

await connect();
await send('Page.enable'); await send('Runtime.enable'); await send('Log.enable');

const pages = ['index.html', 'aktualnosci.html', 'artykul.html'];
for (const p of pages) {
  for (const w of [360, 390, 768, 1280, 1440]) {
    await go(BASE + p, w);
    const r = await ev(`(() => {
      const de = document.documentElement;
      const over = de.scrollWidth - de.clientWidth;
      const wide = [...document.querySelectorAll('body *')].filter(e => { const b = e.getBoundingClientRect(); return b.width && b.right > de.clientWidth + 1 && getComputedStyle(e).position !== 'fixed'; })
        .slice(0, 5).map(e => e.tagName + '.' + e.className);
      const small = [...document.querySelectorAll('a, button, input, summary')].filter(e => {
        if (e.closest('[hidden]') || e.closest('p, li p, dd, .src, .note, .row h3, .crumbs, .foot, .sources, .layer, .ev h3, .file h3, .proto-banner, .org-links')) return false;
        const b = e.getBoundingClientRect(); return b.width > 0 && (b.height < 44 || b.width < 44);
      }).slice(0, 6).map(e => e.tagName + ':' + (e.textContent || e.id).trim().slice(0, 24) + ' ' + Math.round(e.getBoundingClientRect().width) + 'x' + Math.round(e.getBoundingClientRect().height));
      const imgs = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src);
      const h = [...document.querySelectorAll('h1,h2,h3,h4')].map(x => +x.tagName[1]);
      let skip = 0; for (let i = 1; i < h.length; i++) if (h[i] - h[i - 1] > 1) skip++;
      return { over, wide, small, imgs, h1: document.querySelectorAll('h1').length, skip };
    })()`);
    const errs = events.filter(e => e.method === 'Runtime.exceptionThrown' || (e.method === 'Log.entryAdded' && e.params.entry.level === 'error'));
    ok(`${p}@${w} brak poziomego przewijania`, r.over <= 0, r.over > 0 ? r.wide.join(', ') : '');
    ok(`${p}@${w} cele dotykowe >=44px (nawigacja/kontrolki)`, r.small.length === 0, r.small.join(' | '));
    if (w === 390) {
      ok(`${p} obrazy się ładują`, r.imgs.length === 0, r.imgs.join(', '));
      ok(`${p} jeden h1, bez przeskoków nagłówków`, r.h1 === 1 && r.skip === 0, `h1=${r.h1} skoki=${r.skip}`);
      ok(`${p} brak błędów konsoli`, errs.length === 0, errs.map(e => JSON.stringify(e.params).slice(0, 160)).join(' | '));
    }
  }
}

// Indeks: otwarcie, Esc, powrót fokusu
await go(BASE + 'index.html', 390);
await ev(`document.querySelector('.index-btn').click()`);
await sleep(350);
ok('Indeks otwiera się', await ev(`!document.getElementById('indeks').hidden && document.querySelector('.index-btn').getAttribute('aria-expanded')==='true'`));
ok('Fokus w indeksie po otwarciu', await ev(`document.getElementById('indeks').contains(document.activeElement)`));
await key('Escape', 'Escape', 27); await sleep(100);
ok('Esc zamyka indeks i oddaje fokus', await ev(`document.getElementById('indeks').hidden && document.activeElement===document.querySelector('.index-btn')`));
// szybka wyszukiwarka w indeksie
await ev(`document.querySelector('.index-btn').click()`); await sleep(200);
const qs = await ev(`(() => { const i=document.getElementById('qs-index'); i.value='NZW'; i.dispatchEvent(new Event('input')); return document.querySelectorAll('[data-results] li').length; })()`);
ok('Szybka wyszukiwarka zwraca wyniki', qs > 0, `wyniki=${qs}`);

// Warstwy montażu
const lay = await ev(`(() => { const b=[...document.querySelectorAll('[data-layer-btn]')]; b[2].click();
  return [b.map(x=>x.getAttribute('aria-expanded')).join(','), document.getElementById('w-zrodla').hidden, document.getElementById('w-kontekst').hidden]; })()`);
ok('Warstwy montażu przełączają się', lay[0] === 'false,false,true,false' && lay[1] === false && lay[2] === true, JSON.stringify(lay));
// Rozdziały historii (details)
ok('Rozdział historii rozwija się', await ev(`(() => { const d=document.querySelector('#ch-04'); d.querySelector('summary').click(); return d.open; })()`));
// Ograniczenie ruchu
ok('Przełącznik animacji', await ev(`(() => { const b=document.querySelector('.foot [data-motion-toggle]'); const a=document.documentElement.classList.contains('reduce-motion'); b.click(); return document.documentElement.classList.contains('reduce-motion')!==a && b.getAttribute('aria-pressed')===String(!a); })()`));
ok('Formularz demonstracyjny nie wysyła', await ev(`(() => { const f=document.querySelector('[data-demo-form]'); f.requestSubmit(); return location.href.endsWith('index.html') && /prototyp/i.test(f.querySelector('[data-demo-msg]').textContent); })()`));

// Lista: filtry, wyszukiwarka, stan pusty, czyszczenie, parametry URL
await go(BASE + 'aktualnosci.html', 390);
const vis = `[...document.querySelectorAll('[data-item]')].filter(x=>!x.hidden).length`;
ok('Lista: 9 materiałów na start', await ev(vis) === 9);
await ev(`document.querySelector('[data-filter="biogram"]').click()`);
ok('Filtr „Biogramy” = 1', await ev(vis) === 1);
await ev(`(() => { const i=document.getElementById('q'); i.value='xyzzy'; i.dispatchEvent(new Event('input')); })()`);
ok('Stan pusty widoczny', await ev(`!document.querySelector('[data-empty]').hidden && ${vis}===0`));
await ev(`document.querySelector('[data-empty] [data-clear-filters]').click()`);
ok('Wyczyść filtry przywraca 9', await ev(vis) === 9 && await ev(`document.querySelector('[data-filter="all"]').getAttribute('aria-pressed')==='true'`));
await go(BASE + 'aktualnosci.html?q=Holisz%C3%B3w', 390);
ok('Parametr ?q= filtruje', await ev(vis) === 1, `widoczne=${await ev(vis)}`);
await go(BASE + 'aktualnosci.html?kat=dokument', 390);
ok('Parametr ?kat= filtruje', await ev(vis) === 1);

// Artykuł: galeria, klawiatura, postęp
await go(BASE + 'artykul.html', 390);
ok('Galeria: start 1 z 3', await ev(`document.querySelector('[data-status]').textContent`) === 'Slajd 1 z 3');
await ev(`document.querySelector('[data-next]').click()`);
ok('Galeria: przycisk dalej', await ev(`document.querySelector('[data-status]').textContent`) === 'Slajd 2 z 3');
await ev(`document.querySelector('[data-gallery]').focus()`);
await key('ArrowRight', 'ArrowRight', 39);
ok('Galeria: strzałka klawiatury', await ev(`document.querySelector('[data-status]').textContent`) === 'Slajd 3 z 3');
await ev(`window.scrollTo(0, document.body.scrollHeight/2)`); await sleep(150);
ok('Pasek postępu czytania reaguje', +(await ev(`document.querySelector('[data-reading-progress]').getAttribute('aria-valuenow')`)) > 0);
const anchors = await ev(`[...document.querySelectorAll('.toc a[href^="#"]')].every(a => document.getElementById(a.getAttribute('href').slice(1)))`);
ok('Spis treści: wszystkie kotwice istnieją', anchors);

// Linki wewnętrzne we wszystkich widokach
for (const p of pages) {
  await go(BASE + p, 1280);
  const bad = await ev(`(async () => { const out=[]; for (const a of document.querySelectorAll('a[href]')) { const h=a.getAttribute('href'); if (/^(https?:|mailto:)/.test(h)) continue;
    const u=new URL(h, location.href); if (u.hash && u.pathname===location.pathname) { if (!document.getElementById(u.hash.slice(1))) out.push(h); continue; }
    try { const r = await fetch(u.href.split('#')[0]); if (!r.ok) out.push(h); } catch(e) { out.push(h+' ('+e.message+')'); } } return out; })()`);
  ok(`${p}: linki wewnętrzne`, bad.length === 0, bad.join(', '));
  const ext = await ev(`[...document.querySelectorAll('link[href],script[src],img[src]')].map(e=>e.getAttribute('href')||e.getAttribute('src')).filter(u=>/^(https?:)?\\/\\//.test(u))`);
  ok(`${p}: brak zasobów zewnętrznych`, ext.length === 0, ext.join(', '));
}

proc.kill();
const fail = results.filter(r => !r.pass);
for (const r of results) console.log((r.pass ? 'OK   ' : 'FAIL ') + r.name + (r.info ? '  — ' + r.info : ''));
console.log(`\n${results.length - fail.length}/${results.length} OK`);
process.exit(0);
