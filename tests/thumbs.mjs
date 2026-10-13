// Miniatury do selektora: zrzut pierwszego ekranu każdego wariantu (1440×900, JPEG).
import { chromium } from 'playwright-core';
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const PUB = path.resolve('public');
const T = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png' };
const srv = http.createServer((q, r) => { let f = path.join(PUB, decodeURIComponent(q.url.split('?')[0])); if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html'); if (!fs.existsSync(f)) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': T[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r); }).listen(0);
const port = srv.address().port;
const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
for (const v of ['01-nowoczesny', '02-ultranowoczesny', '03-tradycyjny', '04-dziedzictwo', '05-awangardowy']) {
  await p.goto(`http://127.0.0.1:${port}/${v}/index.html`, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.querySelector('.proto-banner')?.remove());
  await p.screenshot({ path: `public/assets/thumbs/${v}.jpg`, type: 'jpeg', quality: 72 });
}
await b.close(); srv.close();
