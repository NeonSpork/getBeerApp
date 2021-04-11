from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO
from hx711 import HX711
from w1thermsensor import W1ThermSensor

# try:
#     hx711 = HX711(
#         dout_pin=
#         pd_sck_pin=
#         channel='A',
#         gain=64
#     )
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # temp sensor
GPIO.setup(2, GPIO.IN)  # weight sensor DT
GPIO.setup(3, GPIO.IN)  # weight sensor SDK

def getTemp():
    try:
        temp = W1ThermSensor().get_temperature()
    except:
        temp = "err"
    return temp


app = Flask(__name__)

@app.route('/')
def default():
    temp = getTemp()
    pints = 42
    return render_template('default.html', temp=temp, pints=pints)

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