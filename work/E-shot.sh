#!/bin/sh
# użycie: E-shot.sh <strona.html> <szer> <wys> <plik-wyj>
C="/c/Program Files/Google/Chrome/Application/chrome.exe"
B="file:///D:/Automatyzacje/nsz-redesign-prototypes"
if [ "$2" -lt 600 ]; then U="$B/work/E-frame.html?w=$2&h=$3&src=../public/05-awangardowy/$1"; W=600; else U="$B/public/05-awangardowy/$1"; W=$2; fi
"$C" --headless=new --hide-scrollbars --disable-gpu --allow-file-access-from-files --virtual-time-budget=4000 --screenshot="D:/Automatyzacje/nsz-redesign-prototypes/work/screens/$4" --window-size=$W,$3 "$U" 2>/dev/null
