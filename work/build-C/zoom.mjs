// Diagnoza przepełnienia przy font-size 200% (wariant C).
import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
for (const w of [390, 1280]) {
  const p = await b.newPage({ viewport: { width: w, height: 900 } });
  for (const pg of ['index', 'aktualnosci', 'artykul']) {
    await p.goto('file:///D:/Automatyzacje/nsz-redesign-prototypes/public/03-tradycyjny/' + pg + '.html');
    const r = await p.evaluate(() => {
      document.documentElement.style.fontSize = '200%';
      const cw = document.documentElement.clientWidth, out = [];
      document.querySelectorAll('body *').forEach(el => { const r = el.getBoundingClientRect(); if ((r.right > cw + 1 || el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflowX==='visible' && el.clientWidth>0 && el.scrollWidth>cw) && r.width) out.push(el.tagName + '.' + el.className + ' ' + Math.round(r.right)); });
      return { over: document.documentElement.scrollWidth - cw, els: out.slice(0, 12) };
    });
    console.log(w, pg, JSON.stringify(r));
  }
}
await b.close();
