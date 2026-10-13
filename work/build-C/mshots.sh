#!/bin/sh
# Mobilne zrzuty i test przewijania poziomego wariantu C przez ramkę iframe (headless wymusza min. szerokość okna).
CH="/c/Program Files/Google/Chrome/Application/chrome.exe"
FR="file:///D:/Automatyzacje/nsz-redesign-prototypes/work/build-C/frame.html"
B="file:///D:/Automatyzacje/nsz-redesign-prototypes/public/03-tradycyjny"
OUT="D:/Automatyzacje/nsz-redesign-prototypes/work/screens"
UD="$TEMP/chrome-shots-C"
H=${H:-2400}
for p in ${PAGES:-index aktualnosci artykul}; do
  for w in ${WIDTHS:-360 390}; do
    U="$FR?w=$w&h=$H&src=$B/$p.html"
    "$CH" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files --user-data-dir="$UD" --virtual-time-budget=4000 \
      --dump-dom "$U" 2>/dev/null | grep -o '<title>[^<]*' | sed "s#<title>#$p@$w: #"
    [ "$w" = 390 ] && "$CH" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files --user-data-dir="$UD" --virtual-time-budget=4000 \
      --screenshot="$OUT/C-$p-390.png" --window-size=600,$H "$U" >/dev/null 2>&1
  done
done
