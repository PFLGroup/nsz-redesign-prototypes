#!/bin/sh
# Zrzuty wariantu C: 390 i 1440 px dla trzech widoków.
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
B="file:///D:/Automatyzacje/nsz-redesign-prototypes/public/03-tradycyjny"
OUT="D:/Automatyzacje/nsz-redesign-prototypes/work/screens"
UD="$TEMP/chrome-shots-C"
H=${H:-2400}
for p in index aktualnosci artykul; do
  for w in 390 1440; do
    "$CH" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$UD" --virtual-time-budget=3000 \
      --screenshot="$OUT/C-$p-$w.png" --window-size=$w,$H "$B/$p.html" >/dev/null 2>&1
  done
done
ls -la "$OUT" | grep " C-"
