from flask import Flask, render_template, request, redirect, url_for
from employee import Worker, Branch

app = Flask(__name__)
w = Worker()
b = Branch()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/branch')
def branch():
    return render_template('branch/branch.html', branches=b.getItems())


@app.route('/worker', methods=['POST', 'GET'])
def worker():
    if request.method == 'GET':
        wData = w.getItems()
        bData = b.getItems()
        return render_template('worker/worker.html', wData=wData, bData=bData)
    elif request.method == 'POST':
        name = request.form['name']
        b_id = request.form['b_id']
        w.addItem(name, b_id)
        return redirect(url_for('worker'))


if __name__ == '__main__':
    app.run(debug=True)
