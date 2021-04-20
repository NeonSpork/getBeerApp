#!/bin/bash

# Install necessary python packages are installed
sudo python3 -m pip install -r requirements.txt

# Install the files into the correct locations
sudo mv flask.service /etc/systemd/system/flask.service

# Ensure app.py is executable
sudo chmod +x app.py