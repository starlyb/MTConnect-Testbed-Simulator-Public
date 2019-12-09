from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
#https://pythonspot.com/login-authentication-with-flask/
app = Flask(__name__)


    
@app.route('/')
def home():
    if not session.get('logged_in'):
        return (render_template('login.html'))
    else:
        return ('Hello Boss!  <a href="/logout">Logout</a>')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    
    if (request.form['password'] == 'password' and request.form['username'] == 'admin'):
        session['logged_in'] = True
        print("jj")
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()



if __name__ == "__main__":
    app.secret_key = os.urandom(4)
    app.run(debug=False,host='0.0.0.0', port=4000)