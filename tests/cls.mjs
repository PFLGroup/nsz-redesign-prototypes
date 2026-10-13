import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
for (const v of ['01-nowoczesny','02-ultranowoczesny','03-tradycyjny','04-dziedzictwo','05-awangardowy']) {
  const out = [];
  for (const js of [false, true]) {
    const c = await b.newContext({ javaScriptEnabled: js, viewport: { width: 412, height: 823 } });
    const p = await c.newPage();
    await p.goto(`http://127.0.0.1:${port}/${v}/`, { waitUntil: 'networkidle' });
    out.push(await p.evaluate(() => Math.round(document.querySelector('main').getBoundingClientRect().top)));
    if (!js) out.push(await p.evaluate(() => [...document.querySelectorAll('header [id], body > [id]')].filter(e => e.offsetHeight > 30 && !e.matches('main')).map(e => e.id + ':' + e.offsetHeight).join(',')));
    await c.close();
  }
  console.log(v, 'main.top noJS=', out[0], 'JS=', out[2], '| bloki bez JS:', out[1]);
}
await b.close();
