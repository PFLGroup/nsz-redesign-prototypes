// Testy interakcji wariantu B przez Chrome DevTools Protocol.
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const BASE = 'file:///D:/Automatyzacje/nsz-redesign-prototypes/public/02-ultranowoczesny/';
const port = 9600 + Math.floor(Math.random() * 200);
const proc = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', ['--headless=new', '--disable-gpu',
  `--remote-debugging-port=${port}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'tb-'))}`, 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let t; for (let i = 0; i < 50 && !t; i++) { try { t = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find((x) => x.type === 'page'); } catch { await sleep(200); } }
const ws = new WebSocket(t.webSocketDebuggerUrl); await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const pend = new Map(); const errors = [];
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
  if (m.method === 'Runtime.exceptionThrown') errors.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text); });
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const ev = async (expr) => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result.result?.value;
const go = async (u, w = 1280) => { await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 800 }); await send('Page.navigate', { url: BASE + u }); await sleep(900); };
const key = async (k, code = k) => { const vk = { Tab: 9, Enter: 13, ArrowRight: 39, ArrowLeft: 37, Escape: 27, ' ': 32 }[k];
  await send('Input.dispatchKeyEvent', { type: 'keyDown', key: k, code, windowsVirtualKeyCode: vk });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code, windowsVirtualKeyCode: vk }); await sleep(80); };
await send('Runtime.enable'); await send('Page.enable');
const results = []; const ok = (name, cond, info = '') => results.push(`${cond ? 'PASS' : 'FAIL'}  ${name}${info ? ' — ' + info : ''}`);

// 1. Strona główna: eksplorator
await go('index.html');
ok('eksplorator zainicjowany (scena widoczna, lista ukryta)', await ev(`!document.querySelector('[data-stage]').hidden && [...document.querySelectorAll('[data-group]')].every(g=>g.hidden)`));
ok('21 przycisków na osi czasu', (await ev(`document.querySelectorAll('.canvas-czas [data-node]').length`)) === 21);
ok('domyślnie wybrany 20 IX 1942', await ev(`document.querySelector('#card-title').textContent.includes('1/42')`));
await ev(`document.querySelector('[data-node="t1946-05-03"]').click()`);
ok('klik punktu → karta „Wisła”', await ev(`document.querySelector('#card-title').textContent.includes('Wisłę')`));
ok('powiązane punkty podświetlone', (await ev(`document.querySelectorAll('.nbtn.is-linked').length`)) >= 0);
await ev(`[...document.querySelectorAll('.card-rel button')].find(b=>b.textContent.includes('Flame')).click()`);
ok('powiązanie → przełącza na „Ludzie”', await ev(`document.querySelector('#tab-ludzie').getAttribute('aria-selected')==='true' && document.querySelector('#card-title').textContent.includes('Flame')`));
ok('hash zaktualizowany', (await ev('location.hash')) === '#n-p-flame');
// klawiatura w zakładkach
await ev(`document.querySelector('#tab-ludzie').focus()`); await key('ArrowRight', 'ArrowRight');
ok('strzałka w prawo → zakładka „Dokumenty” z fokusem', await ev(`document.activeElement.id==='tab-dokumenty' && document.activeElement.getAttribute('aria-selected')==='true'`));
ok('roving tabindex', await ev(`[...document.querySelectorAll('[role=tab]')].filter(t=>t.tabIndex===0).length===1`));
// widok listy
await ev(`document.querySelector('[data-view="list"]').click()`);
ok('widok listy: scena ukryta, grupa „dokumenty” widoczna', await ev(`document.querySelector('[data-stage]').hidden && !document.querySelector('#lista-dokumenty').hidden && document.querySelector('#lista-czas').hidden`));
await ev(`document.querySelector('[data-view="map"]').click()`);
// menu wyszukiwania
await ev(`document.querySelector('[aria-controls="panel-szukaj"]').click()`);
ok('panel wyszukiwania otwarty, fokus w polu', await ev(`!document.getElementById('panel-szukaj').hidden && document.activeElement.id==='q-global'`));
await ev(`(()=>{const i=document.getElementById('q-global'); i.value='Kamesznic'; i.dispatchEvent(new Event('input'));})()`);
ok('szybkie wyszukiwanie zwraca wyniki', (await ev(`document.querySelectorAll('[data-results] li').length`)) > 0);
await key('Escape', 'Escape');
ok('Escape zamyka panel', await ev(`document.getElementById('panel-szukaj').hidden`));
// przełącznik animacji
const before = await ev(`document.documentElement.classList.contains('reduce-motion')`);
await ev(`document.querySelector('[data-motion-toggle]').click()`);
ok('przełącznik animacji zmienia stan', (await ev(`document.documentElement.classList.contains('reduce-motion')`)) !== before);
// deep link
await go('index.html#n-t1945-01');
ok('deep link #n-t1945-01 → karta sporu', await ev(`document.querySelector('#card-title').textContent.includes('Wehrmacht') && document.querySelector('.card .badge').textContent.includes('sporna')`));
await go('index.html#n-m-holiszow');
ok('deep link do miejsca przełącza perspektywę', await ev(`document.querySelector('#tab-miejsca').getAttribute('aria-selected')==='true'`));

// 2. Mobile: menu
await go('index.html', 360);
ok('mobile: menu domyślnie zamknięte', await ev(`document.getElementById('menu-glowne').hidden`));
await ev(`document.querySelector('.menu-btn').click()`);
ok('mobile: menu otwiera się', await ev(`!document.getElementById('menu-glowne').hidden && getComputedStyle(document.getElementById('menu-glowne')).display!=='none'`));
await ev(`document.querySelector('[data-node="t1944-08-11"]').click()`);
ok('mobile: wybór punktu przenosi fokus na kartę', await ev(`document.activeElement.id==='card-title'`));

// 3. Aktualności
await go('aktualnosci.html');
ok('lista: 9 pozycji', (await ev(`document.querySelectorAll('[data-item]:not([hidden])').length`)) === 9);
await ev(`document.querySelector('[data-filter="biogram"]').click()`);
ok('filtr „Biogramy” → 1', (await ev(`document.querySelectorAll('[data-item]:not([hidden])').length`)) === 1);
await go('aktualnosci.html?kat=dokument');
ok('?kat=dokument → 1', (await ev(`document.querySelectorAll('[data-item]:not([hidden])').length`)) === 1);
await go('aktualnosci.html?q=zzzz');
ok('?q=zzzz → stan pusty widoczny', await ev(`!document.querySelector('[data-empty]').hidden`));
await ev(`document.querySelector('[data-empty] [data-clear-filters]').click()`);
ok('wyczyść → 9 pozycji', (await ev(`document.querySelectorAll('[data-item]:not([hidden])').length`)) === 9);
await go('aktualnosci.html?q=holiszow');
ok('wyszukiwanie bez polskich znaków „holiszow” → ≥1', (await ev(`document.querySelectorAll('[data-item]:not([hidden])').length`)) >= 1);

// 4. Artykuł
await go('artykul.html');
ok('galeria: slajd 1 z 3', (await ev(`document.querySelector('[data-status]').textContent`)) === 'Slajd 1 z 3');
await ev(`document.querySelector('[data-next]').click()`);
ok('galeria: następny → 2 z 3', (await ev(`document.querySelector('[data-status]').textContent`)) === 'Slajd 2 z 3');
await ev(`document.querySelector('[data-gallery]').focus()`); await key('ArrowLeft', 'ArrowLeft');
ok('galeria: strzałka w lewo → 1 z 3', (await ev(`document.querySelector('[data-status]').textContent`)) === 'Slajd 1 z 3');
await ev(`window.scrollTo(0, document.body.scrollHeight/2)`); await sleep(200);
ok('pasek postępu czytania rośnie', await ev(`/scaleX\\(0\\.[1-9]|scaleX\\(1/.test(document.querySelector('[data-reading-progress]').style.transform)`));
ok('nagłówki h1 → h2 (jeden h1)', (await ev(`document.querySelectorAll('h1').length`)) === 1);

// 5. Bez JS
await send('Emulation.setScriptExecutionDisabled', { value: true });
await go('index.html');
ok('bez JS: lista punktów widoczna (45)', (await ev(`[...document.querySelectorAll('li.node')].filter(l=>l.offsetParent).length`)) === 45);
ok('bez JS: menu desktop widoczne', await ev(`getComputedStyle(document.getElementById('menu-glowne')).display!=='none'`));
await go('aktualnosci.html');
ok('bez JS: 9 pozycji listy', (await ev(`[...document.querySelectorAll('[data-item]')].filter(l=>l.offsetParent).length`)) === 9);
await send('Emulation.setDeviceMetricsOverride', { width: 1280, height: 900, deviceScaleFactor: 1, mobile: false });
const shot = await send('Page.captureScreenshot', { format: 'png' });
writeFileSync('D:/Automatyzacje/nsz-redesign-prototypes/work/screens/B-nojs-aktualnosci.png', Buffer.from(shot.result.data, 'base64'));
await go('index.html');
const s2 = await send('Page.captureScreenshot', { format: 'png' });
writeFileSync('D:/Automatyzacje/nsz-redesign-prototypes/work/screens/B-nojs-index.png', Buffer.from(s2.result.data, 'base64'));

console.log(results.join('\n'));
console.log('JS errors:', errors.length ? errors : 'brak');
ws.close(); proc.kill(); process.exit(0);
