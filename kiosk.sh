#!/bin/bash

xset s noblank
xset s off
xset -dpms

unclutter -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences

python3 app.py &
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:5000