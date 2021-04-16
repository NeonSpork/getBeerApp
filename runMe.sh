#!/bin/bash

# Remove some junk that is only going to slow down the Pi if present
sudo apt purge wolfram-engine scratch scratch2 nuscratch sonic-pi idle3 -y
sudo apt purge smartsim java-common minecraft-pi libreoffice* -y

# Clean up the package cache
sudo apt clean
sudo apt autoremove -y

# Update the system as needed
sudo apt update
sudo apt upgrade

# Ensure we have the tools we need to run as a kiosk
sudo apt install xdotool unclutter sed chromium

# Ensure the necessary python packages are installed
sudo python3 -m pip install -r requirements.txt

# Install the files into the correct locations
sudo mv kiosk.service /lib/systemd/system/kiosk.service

# Enable the new kiosk service
sudo systemctl enable kiosk.service

# Alert the user what we have done and what the next steps are
echo "Kegerator kiosk mode activated. Please reboot the Pi or run 'sudo systemctl start kiosk.service' to start the kiosk now."