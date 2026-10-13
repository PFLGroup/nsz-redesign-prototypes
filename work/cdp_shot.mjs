// Zrzuty z emulacją szerokości przez Chrome DevTools Protocol (headless Chrome
// sam nie schodzi poniżej ~484 px). Użycie:
//   node cdp_shot.mjs <url> <out.png> <width> [height=900] [fullPage=1]
// Wypisuje JSON: szerokość dokumentu vs okna (wykrycie poziomego przewijania),
// błędy konsoli i wyjątki.
import { spawn } from 'node:child_process';
import { writeFileSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const [url, out, w = '390', h = '900', full = '1'] = process.argv.slice(2);
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const port = 9341 + Math.floor(Math.random() * 200);
const prof = mkdtempSync(join(tmpdir(), 'cdpshot-'));
const proc = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', `--remote-debugging-port=${port}`,
  `--user-data-dir=${prof}`, '--allow-file-access-from-files', 'about:blank'], { stdio: 'ignore' });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let target;
for (let i = 0; i < 50 && !target; i++) {
  try {
    const list = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
    target = list.find((t) => t.type === 'page');
  } catch { await sleep(200); }
}
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const pending = new Map(); const logs = [];
ws.addEventListener('message', (ev) => {
  const m = JSON.parse(ev.data);
  if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  if (m.method === 'Runtime.consoleAPICalled' && ['error', 'warning'].includes(m.params.type))
    logs.push(m.params.type + ': ' + m.params.args.map((a) => a.value ?? a.description).join(' '));
  if (m.method === 'Runtime.exceptionThrown') logs.push('exception: ' + (m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text));
  if (m.method === 'Log.entryAdded' && m.params.entry.level === 'error') logs.push('log: ' + m.params.entry.text + ' ' + (m.params.entry.url || ''));
});
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
await send('Runtime.enable'); await send('Log.enable'); await send('Page.enable');
const W = +w, H = +h;
await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: W < 800 });
await send('Page.navigate', { url });
await sleep(1500);
const ev = await send('Runtime.evaluate', { returnByValue: true, expression: `(() => {
  const de = document.documentElement;
  const wide = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth + 1 && r.width > 0 && getComputedStyle(e).position !== 'fixed'; }).slice(0, 8).map(e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : '') + ' r=' + Math.round(e.getBoundingClientRect().right));
  const small = [...document.querySelectorAll('a, button, input, [role=tab]')].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && (r.height < 24 || r.width < 24); }).length;
  const imgs = [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.src);
  return { scrollW: de.scrollWidth, innerW: innerWidth, docH: de.scrollHeight, overflow: de.scrollWidth > innerWidth, wide, smallTargets: small, brokenImgs: imgs };
})()` });
const info = ev.result.result.value;
let clip;
if (full === '1') {
  const hh = Math.min(info.docH, 16000);
  await send('Emulation.setDeviceMetricsOverride', { width: W, height: hh, deviceScaleFactor: 1, mobile: W < 800 });
  await sleep(400);
  clip = { x: 0, y: 0, width: W, height: hh, scale: 1 };
}
const shot = await send('Page.captureScreenshot', { format: 'png', ...(clip ? { clip, captureBeyondViewport: true } : {}) });
writeFileSync(out, Buffer.from(shot.result.data, 'base64'));
console.log(JSON.stringify({ url, width: W, ...info, logs }));
ws.close(); proc.kill();
process.exit(0);
