from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
#https://pythonspot.com/login-authentication-with-flask/
app = Flask(__name__)

def string2int(string):
    sum=0
    for i in string:
        sum+=ord(i)
    return(sum)
    

def controlPanel(ORGS,MACHS,SEED):
    f=open("control_panel.py","w")
    f.write(f"""ORGS={ORGS}
MACHS={MACHS}
seed={SEED}""")
    f.close()
    
@app.route('/home',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     
      ORGS=int(request.form["org"])
      Low=int(request.form["low"])
      High=int(request.form["high"])
      MACHS=[Low,High]
      SEED=string2int(request.form["seed"])
      controlPanel(ORGS,MACHS,SEED)
      
      estime= ORGS*High/10
      result = {'Orgs': ORGS, 'Range of Machines':str(MACHS),'Random Seed':str(SEED),'Estimated Seconds to start':estime}
      return render_template("home.html",result = result)
    
@app.route('/')
def home():
    if not session.get('logged_in'):
        return (render_template('login.html'))
    else:
        return render_template('input.html')
        #return ('Hello Boss!  <a href="/logout">Logout</a>')
 
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