from flask import Flask, render_template, url_for, request, redirect, flash
from classes import Alban

app = Flask(__name__)
app.secret_key = 'asas'
albanC = Alban()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alban', methods=['GET', 'POST'])
def list_alban():
    if request.method == 'GET':
        datas = albanC.getRecords()
        return render_template('alban/list.html', datas=datas)
    elif request.method == 'POST':
        aname = request.form['aname']
        albanC.add(aname)
        flash('amjilttai hadgallaa', 'success')
        return redirect(url_for('list_alban'))


@app.route('/alban/delete/<int:id>')
def delete_alban(id):
    albanC.delete(id)
    flash('amjilttai usgalaa', 'success')
    return redirect(url_for('list_alban'))


if __name__ == '__main__':
    app.run(debug=True)
