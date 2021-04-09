from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def default():
    temp = 10;
    return render_template('default.html', temp=temp)

@app.route('/secret')
def secret():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run(debug=True)
