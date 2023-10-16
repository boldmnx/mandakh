# pip san olon mor kod bol % avdag
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/butsah')
def index():
    return render_template('index.html')


@app.route('/login')
@app.route('/jishee')
def log():
    return render_template('login.html')


app.run(debug=True)
