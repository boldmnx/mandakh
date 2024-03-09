from flask import Flask, request, redirect, render_template, abort, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            return abort(400)
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return '<h1> logged in succeed</h1>'


if __name__ == '__main__':
    app.run(debug=True)
