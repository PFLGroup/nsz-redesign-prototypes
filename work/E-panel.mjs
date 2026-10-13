import { spawn } from 'node:child_process'; import { setTimeout as sleep } from 'node:timers/promises'; import { writeFileSync, mkdtempSync } from 'node:fs'; import { tmpdir } from 'node:os'; import { join } from 'node:path';
const P=9340; const pr=spawn('C:/Program Files/Google/Chrome/Application/chrome.exe',['--headless=new',`--remote-debugging-port=${P}`,`--user-data-dir=${mkdtempSync(join(tmpdir(),'e2-'))}`,'about:blank'],{stdio:'ignore'});
let ws,id=0;const pend=new Map();
for(let i=0;i<50&&!ws;i++){try{const l=await (await fetch(`http://127.0.0.1:${P}/json`)).json();const p=l.find(t=>t.type==='page');if(p)ws=new WebSocket(p.webSocketDebuggerUrl);}catch{}await sleep(200);}
console.log('ws',!!ws);if(ws.readyState!==1)await new Promise(r=>ws.addEventListener('open',r));console.log('open');ws.addEventListener('message',m=>{const d=JSON.parse(m.data);if(d.id&&pend.has(d.id)){pend.get(d.id)(d);pend.delete(d.id);}});
const send=(method,params={})=>new Promise(r=>{const i=++id;pend.set(i,r);ws.send(JSON.stringify({id:i,method,params}));});
async function shot(url,w,h,js,file,full){console.log('shot',file);await send('Emulation.setDeviceMetricsOverride',{width:w,height:h,deviceScaleFactor:1,mobile:w<800});await send('Page.navigate',{url});await sleep(1000);if(js)await send('Runtime.evaluate',{expression:js});await sleep(500);
 const r=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:!!full});writeFileSync(file,Buffer.from(r.result.data,'base64'));}
const B='http://127.0.0.1:8765/05-awangardowy/';
await shot(B+'index.html',390,844,"document.querySelector('.index-btn').click();document.getElementById('qs-index').value='NZW';document.getElementById('qs-index').dispatchEvent(new Event('input'))",'work/screens/E-indeks-390.png');
await shot(B+'index.html',390,844,"window.scrollTo(0,document.body.scrollHeight)",'work/screens/E-foot-390.png');
await shot(B+'aktualnosci.html',390,844,"(()=>{const i=document.getElementById('q');i.value='xyzzy';i.dispatchEvent(new Event('input'));document.querySelector('[data-empty]').scrollIntoView()})()",'work/screens/E-empty-390.png');
await shot(B+'index.html',1440,900,"document.querySelector('#ch-06 summary').click();document.querySelector('#ch-06').scrollIntoView()",'work/screens/E-chap-1440.png');
pr.kill();process.exit(0);
