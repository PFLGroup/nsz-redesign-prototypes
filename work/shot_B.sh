#!/bin/bash
# zrzuty wariantu B: shot_B.sh [suffix]
C="/c/Program Files/Google/Chrome/Application/chrome.exe"
B="file:///D:/Automatyzacje/nsz-redesign-prototypes/public/02-ultranowoczesny"
O="D:/Automatyzacje/nsz-redesign-prototypes/work/screens"
for p in index aktualnosci artykul; do
  for s in "390,2400" "1440,2400"; do
    w=${s%,*}
    "$C" --headless=new --hide-scrollbars --disable-gpu --virtual-time-budget=3000 --screenshot="$O/B-$p-$w$1.png" --window-size=$s "$B/$p.html" 2>/dev/null
  done
done
ls "$O" | grep "^B-"
