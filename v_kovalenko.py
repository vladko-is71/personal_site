import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/myself')
def myself():
    return render_template('myself.html')


@app.route('/congratulations', methods=('POST', ))
def congratulations():
    data = request.form['name']
    conn = sqlite3.connect('sitedb.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO names(Name) VALUES(?);', (data, ))
    conn.commit()
    return render_template('congratulations.html')


if __name__ == '__main__':
    app.run(port=80)
