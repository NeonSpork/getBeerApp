from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO
from hx711 import HX711
from w1thermsensor import W1ThermSensor

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # temp sensor
GPIO.setup(2, GPIO.IN)  # weight sensor DT
GPIO.setup(3, GPIO.IN)  # weight sensor SDK

hx = HX711(dout_pin=2,
           pd_sck_pin=3,
           channel='A',
           gain=64)
hx.set_offset(8234508)  # This gets calibrated to zero the sensor
hx.set_scale_ratio(-20.9993)

@app.route('/getTemp')
def getTemp():
    try:
        temp = W1ThermSensor.get_temperature()
    except Exception as e:
        temp = e
    return temp

@app.route('/getPints')
def getPints():
    try:
        hx.reset()
        pints = hx.get_raw_data()
    except Exception as e:
        pints = e.__name__
    return pints

@app.route('/')
def default():
    temp = getTemp()
    pints = getPints()
    return render_template('default.html', temp = temp, pints = pints)

@app.route('/secret')
def secret():
    return render_template('secret.html')

@app.route('/beginPour')
def beginPour():
    # valveOperator.openValve(20)
    print('Starting pour...')
    return 'nothing'

@app.route('/endPour')
def endPour():
    # valveOperator.closeValve(20)
    print('Pour finished.')
    return 'nothing'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    GPIO.cleanup()