# getBeerApp

### Overview

This is a simple app that serves up a web interface for a custom built kegerator, built with Python3 and Flask.

### Getting Started

You can simply run `python -m pip install -r requirements.txt` and pip will install the requirements for you. From there you just run `python app.py` to start the app.

Follow the steps laid out in `runMe.sh` to set up the kiosk environment. The shell script was written on a Windows machine and if you encounter errors, there is a HIGH likelyhood that there is a hidden `'\r'` character at the end of `kiosk.service` (i.e. it would actually look like `kiosk.service'\r'` and thus fail miserably since it has the wrong filename). You will have to manually rename it in that case: `sudo mv kiosk.service'\r' kiosk.service`.

### Hooking up the Pi

TODO: layout pin info

### Hooking up the Tinkerboard

TODO: layout pin info