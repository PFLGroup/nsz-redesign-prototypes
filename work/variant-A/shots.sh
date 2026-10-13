#!/bin/sh
# Zrzuty wariantu A: desktop bezpośrednio, mobile przez ramkę iframe (headless wymusza min. szerokość okna).
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
ROOTF="file:///D:/Automatyzacje/nsz-redesign-prototypes"
BASE="$ROOTF/public/01-nowoczesny"
OUTW='D:\Automatyzacje\nsz-redesign-prototypes\work\screens'
for p in ${PAGES:-index aktualnosci artykul historia}; do
  "$CH" --headless=new --hide-scrollbars --disable-gpu --virtual-time-budget=3000 \
    --screenshot="$OUTW\A-$p-1440.png" --window-size=1440,2400 "$BASE/$p.html" 2>/dev/null
  for w in 390; do
    "$CH" --headless=new --hide-scrollbars --disable-gpu --allow-file-access-from-files --virtual-time-budget=4000 \
      --screenshot="$OUTW\A-$p-$w.png" --window-size=600,2400 "$ROOTF/work/variant-A/frame.html?w=$w&src=$BASE/$p.html" 2>/dev/null
  done
done
