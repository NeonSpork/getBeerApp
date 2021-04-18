#!/bin/bash

xset s noblank
xset s off
xset -dpms

unclutter -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences

/usr/bin/bash start_server.sh
/usr/bin/chromium --noerrdialogs --disable-infobars --kiosk http://localhost:5000