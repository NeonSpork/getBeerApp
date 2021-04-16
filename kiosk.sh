#!/bin/bash

xset s noblank
xset s off
xset -dpms

unclutter -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

$sudo python3 /home/pi/getBeerApp/app.py
/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:5000