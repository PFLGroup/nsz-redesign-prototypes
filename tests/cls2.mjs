import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
for (const v of ['01-nowoczesny','02-ultranowoczesny','03-tradycyjny','04-dziedzictwo','05-awangardowy']) for (const w of [412, 1440]) {
  const p = await b.newPage({ viewport: { width: w, height: 900 } });
  await p.goto(`https://pflgroup.github.io/nsz-redesign-prototypes/${v}/`, { waitUntil: 'networkidle' });
  console.log(v, w, await p.evaluate(() => [...document.querySelectorAll('[data-disclosure]')].map(btn => { const id = btn.getAttribute('aria-controls'); const el = document.getElementById(id); return id + (el ? `(hidden=${el.hidden},disp=${getComputedStyle(el).display},btnVisible=${btn.offsetWidth>0})` : '(brak)'); }).join(' ')));
  await p.close();
}
await b.close();
