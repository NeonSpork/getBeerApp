#!/bin/bash

# be new
apt-get update

# get software
apt-get install \
	unclutter \
    xorg \
    chromium \
    openbox \
    lightdm \
    locales \
    -y \
    --allow-change-held-packages

# dir
mkdir -p /home/linaro/.config/openbox

# # create group
# groupadd kiosk

# # create user if not exists
# id -u kiosk &>/dev/null || useradd -m kiosk -g kiosk -s /bin/bash 

# # rights
# chown -R kiosk:kiosk /home/kiosk

# remove virtual consoles
if [ -e "/etc/X11/xorg.conf" ]; then
  mv /etc/X11/xorg.conf /etc/X11/xorg.conf.backup
fi
cat > /etc/X11/xorg.conf << EOF
Section "ServerFlags"
    Option "DontVTSwitch" "true"
EndSection
EOF

# create config
if [ -e "/etc/lightdm/lightdm.conf" ]; then
  mv /etc/lightdm/lightdm.conf /etc/lightdm/lightdm.conf.backup
fi
cat > /etc/lightdm/lightdm.conf << EOF
[SeatDefaults]
autologin-user=linaro
EOF

# create autostart
if [ -e "/home/linaro/.config/openbox/autostart" ]; then
  mv /home/linaro/.config/openbox/autostart /home/linaro/.config/openbox/autostart.backup
fi
cat > /home/linaro/.config/openbox/autostart << EOF
#!/bin/bash
unclutter -idle 0.1 -grab -root &
&sudo python3 /home/linaro/getBeerApp/app.py &
while :
do
  chromium \
    --no-first-run \
    --start-maximized \
    --window-position=0,0 \
    --window-size=1024,600 \
    --disable \
    --disable-translate \
    --disable-infobars \
    --disable-suggestions-service \
    --disable-save-password-bubble \
    --disable-session-crashed-bubble \
    --incognito \
    --kiosk "localhost:5000"
  sleep 5
done &
EOF

echo "Done!"