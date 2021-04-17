from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO
from hx711 import HX711
from w1thermsensor import W1ThermSensor

app = Flask(__name__)

# TODO add custom name - requires messing about with /etc/hosts and adding an alias
# app.config['SERVER_NAME'] = 'getbeer:5000'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)  # Temp sensor DS18B20
GPIO.setup(3, GPIO.IN)  # HX711 load sensor DT
GPIO.setup(5, GPIO.IN)  # HX711 load sensor SDK
beerPin = 37
secretPin = 38
GPIO.setup(beerPin, GPIO.OUT)  # Output pin to solenoid BEER valve
GPIO.setup(secretPin, GPIO.OUT)  # Output pin to solenoid VODKA valve

hx = HX711(dout=3, pd_sck=5)
hx.set_offset(8234508)  # This gets calibrated to zero the sensor
hx.set_scale(-20.9993)
sensor = W1ThermSensor()

@app.route('/getTemp')
def getTemp():
    try:
        temp = sensor.get_temperature()
    except Exception as e:
        temp = e.__name__
    return temp

@app.route('/getPints')
def getPints():
    try:
        grams = hx.get_grams(times=1)
        pints = int((grams - 4250)*0.5)  # dry weight of keg is ca. 4250g
        if pints < 0:
            pints = 0
    except Exception as e:
        pints = e
    return pints

@app.route('/', methods= ['GET'])
def default():
    temp = getTemp()
    pints = getPints()
    return render_template('default.html', temp = temp, pints = pints)

@app.route('/secret')
def secret():
    temp = getTemp()
    pints = getPints()
    return render_template('secret.html', temp = temp, pints = pints)

@app.route('/beginPour')
def beginPour():
    GPIO.output(beerPin, True)
    return 'nothing'

@app.route('/endPour')
def endPour():
    GPIO.output(beerPin, False)
    return 'nothing'

@app.route('/beginPourSECRET')
def beginPourSECRET():
    GPIO.output(secretPin, True)
    return 'nothing'

@app.route('/endPourSECRET')
def endPourSECRET():
    GPIO.output(secretPin, False)
    return 'nothing'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    GPIO.cleanup()