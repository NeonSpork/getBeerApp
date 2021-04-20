# getBeerApp

### Overview

This is a simple app that serves up a web interface for a custom built kegerator, built with Python3 and Flask.

### Recommended OS

This works the _ABSOLUTE_ best on a minimalist, simple to set up distro like [DietPi](https://dietpi.com).

### Setting up DietPi for getBeerApp

First, download the image that correctly matches your SBC. Flash it to a micro SD using f.ex. balena etcher or similar. (Follow the instructions on the DietPi website if necessary)  

Follow the configuration steps to initialize and set up the DietPi, including wifi, etc.

#### Software to install
* 113 - Chromium
* 6 - X.Org X Server (possibly automatically installed with Chromium)
* 130 - Python 3 pip
* 16 - Build-Essentials
* 17 - Git Client

#### !!!!! KNOWN ISSUES !!!!!
Currently 1wire is not set up by default on DietPi for **TinkerBoard** and getting it work correctly is WIP.  
If temperature is essential, use an RPi as in all likelyhood the performance will be similar. (1wire is essential in order to use the DS18B20 temperature sensor, and the setup is much less of a hassle on RPi)

### Setting up getBeerApp
#### Step 1

Clone this repository:  
`git clone https://github.com/NeonSpork/getBeerApp.git`

---
**NOTE:** It is assumed you will set this up for **personal use** in an environment you trust. As such, the service file and automatic setup shell script (`flask.service` and `setup_getBeerApp.sh` respectively) assume you are acting as `root` and cloning the repository in `/root/` (the root home directory).  
If you intend to deploy this _anywhere_ where you do not trust the users, etc etc, you will need to modify those files, and your install location/user autologin/etc accordingly.  

It cannot be stressed enough that I take **_NO_** responsibility or liability for any and all use of this code or anything contained in this repository.

---

If using TinkerBoard, clone the ASUS.GPIO repository:  
`git clone https://github.com/TinkerBoard/gpio_lib_python.git`
Change directory to gpio_lib_python:
`cd /path_to_where_you_cloned_it/gpio_lib_python/`
Install the python lib:
`sudo python3 setup.py install`


#### Step 2
From within `/getBeerApp/` simply run `python3 -m pip install -r requirements.txt` and pip will install the requirements for you.  

Once the requirements are installed, run `sudo sh setup_getBeerApp.sh` to make `app.py` executable, and copy the service file to the correct location.

#### Step 3
Open DietPi-Services with the command `dietpi-services` and add `flask` to the services to start at launch.

#### Step 4
Open DietPi-AutoStart with the command `dietpi-autostart` and choose option `11 : Chromium - Dedicated use without desktop`
When prompted for the url to start in kiosk mode, enter the default address used by flask: `http://localhost:5000`


### GPIO pin layout
#### HX711 (load sensor)
* VCC: any 3.3V pin
* GNC: any ground pin
* DOUT: GPIO2
* PD_SDK: GPIO3

**NOTE!** Your HX711 _will_ need to be calibrated to show correct grams. Follow instructions online for simple python scripts to find the offset and scale, and adjust `app.py` lines 36 and 37 accordingly.

#### DS18B20 (temperature sensor)
* VCC: any 5v pin
* GND: any ground pin
* Data: GPIO4

**NOTE!** Remember to install the 4.7ohm resistor between VCC and Data, follow instructions online.