#!/usr/bin/env python3
from flask import Flask, render_template, url_for
try:
    import RPi.GPIO as GPIO
    from hx711 import HX711
    from w1thermsensor import W1ThermSensor
except:
    print("No compatible SBC detected!")
    print("GPIO, hx711, w1thermsensor are NOT imported.")

app = Flask(__name__)

# TODO add custom name - requires messing about with /etc/hosts and adding an alias
# app.config['SERVER_NAME'] = 'getbeer:5000'
beerPin = 37
secretPin = 38
try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)  # Temp sensor DS18B20
    GPIO.setup(3, GPIO.IN)  # HX711 load sensor DT
    GPIO.setup(5, GPIO.IN)  # HX711 load sensor SDK
    GPIO.setup(beerPin, GPIO.OUT)  # Output pin to solenoid BEER valve
    GPIO.setup(secretPin, GPIO.OUT)  # Output pin to solenoid VODKA valve
except:
    class GPIO():
        def output(pin, status):
            print("Simulating gpio{}, status: {}".format(pin, status))
        HIGH = "GPIO.HIGH"
        LOW = "GPIO.LOW"

        def cleanup():
            print("Simulating GPIO.cleanup()")

try:
    hx = HX711(dout=3, pd_sck=5)
    hx.set_offset(8234508)  # This gets calibrated to zero the sensor
    hx.set_scale(-20.9993)
except:
    class hx():
        def get_grams(times=1):
            return "n/a"
try:
    sensor = W1ThermSensor()
except:
    class sensor():
        def get_temperature():
            return "n/a"


@app.route('/getTemp')
def getTemp():
    try:
        tempRead = sensor.get_temperature()
        temp = "{:.1f}".format(tempRead)
    except:
        temp = "n/a"
    return temp


@app.route('/getPints')
def getPints():
    try:
        grams = hx.get_grams(times=1)
        pints = int((grams - 4250)*0.002)  # dry weight of keg is ca. 4250g
        if pints < 0:
            pints = 0
        return pints
    except:
        return "n/a"


@app.route('/', methods=['GET'])
def default():
    temp = getTemp()
    pints = getPints()
    return render_template('default.html', temp=temp, pints=pints)


@app.route('/secret')
def secret():
    temp = getTemp()
    pints = getPints()
    return render_template('secret.html', temp=temp, pints=pints)


@app.route('/beginPour')
def beginPour():
    GPIO.output(beerPin, GPIO.HIGH)
    return 'nothing'


@app.route('/endPour')
def endPour():
    GPIO.output(beerPin, GPIO.LOW)
    return 'nothing'


@app.route('/beginPourSECRET')
def beginPourSECRET():
    GPIO.output(secretPin, GPIO.HIGH)
    return 'nothing'


@app.route('/endPourSECRET')
def endPourSECRET():
    GPIO.output(secretPin, GPIO.LOW)
    return 'nothing'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    GPIO.cleanup()
