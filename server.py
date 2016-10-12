#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, redirect, url_for, escape, request
from flask_socketio import SocketIO, emit
from hashlib import md5
import MySQLdb
import input_mod, time

app = Flask(__name__, static_url_path = '/static')
socketio = SocketIO(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username = escape(session['username']).capitalize())
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'username' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur.execute("SELECT password FROM users WHERE username = %s;", [username])
        pwhex = None
        try:
            pwhex = cur.fetchone()[0]
        except:
            error = 'invalid credential'

        if md5(password).hexdigest() == pwhex:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'invalid credential'

    return render_template('login.html', error = error)

<<<<<<< 8fc495ce952f37ef3c5c9da6ba75d16d2a543211
@socketio.on('connection')
def connection(data):
    print data["data"]

@socketio.on('getstatus')
def status():
    print 'getstatus received'
    while True:
        ev = input_mod.readContact()
        print ev
        try:
            emit('status', ev)
        except:
            print 'error'
        time.sleep(5)

=======
>>>>>>> add login system
if __name__ == '__main__':
    db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'AngusYoung', db = 'prodb')
    cur = db.cursor()
    app.config['SECRET_KEY'] = 'AngusYoung'
<<<<<<< 8fc495ce952f37ef3c5c9da6ba75d16d2a543211
    socketio.run(app, host = '0.0.0.0', port=8080)
=======
    app.run(host = '0.0.0.0', port=8080)
>>>>>>> add login system
