from flask import Flask, render_template, url_for
from hx711 import HX711
from ds18b20 import DS18B20

# try:
#     hx711 = HX711(
#         dout_pin=
#         pd_sck_pin=
#         channel='A',
#         gain=64
#     )

# def getTemp():


app = Flask(__name__)

@app.route('/')
def default():
    temp = 10
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