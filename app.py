from flask import Flask, render_template, url_for
import time

app = Flask(__name__)
# TODO add custom name - requires messing about with /etc/hosts and adding an alias
# app.config['SERVER_NAME'] = 'getbeer:5000'

@app.route('/getTemp')
def getTemp():
    try:
        t = time.localtime()
        temp = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
    except Exception as e:
        temp = e.__name__
    return temp

@app.route('/getPints')
def getPints():
    try:
        t = time.localtime()
        pints = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
    except Exception as e:
        pints = e.__name__
    return pints

@app.route('/', methods= ['GET'])
def default():
    temp = getTemp()
    pints = getPints()
    return render_template('default.html', temp = temp, pints = pints)

@app.route('/secret')
def secret():
    return render_template('secret.html')

@app.route('/beginPour')
def beginPour():
    print('Starting pour...')
    return 'nothing'

@app.route('/endPour', methods= ['GET'])
def endPour():
    temp = getTemp()
    pints = getPints()
    # return false
    return render_template('default.html', temp = temp, pints = pints)

if __name__ == '__main__':
    app.run(debug=True)