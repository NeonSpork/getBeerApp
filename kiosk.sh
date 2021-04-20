#!/bin/bash

# Run this script in display 0 - the monitor
export DISPLAY=:0

# Hide the mouse from the display
unclutter &

# If Chromium crashes (usually due to rebooting), clear the crash flag so we don't have the annoying warning bar
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/getbeer/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/getbeer/.config/chromium/Default/Preferences

# Start flask server
/home/getbeer/getBeerApp/app.py &

# Run Chromium and open tabs
/usr/bin/chromium-browser --window-size=1024,600 --kiosk --window-position=0,0 localhost:5000/ &

# # Start the kiosk loop. This keystroke changes the Chromium tab
# # To have just anti-idle, use this line instead:
# # xdotool keydown ctrl; xdotool keyup ctrl;
# # Otherwise, the ctrl+Tab is designed to switch tabs in Chrome
# # #
# while (true)
#   do
#     xdotool keydown ctrl; xdotool keyup ctrl;
#     sleep 15
# done
