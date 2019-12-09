from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def input_par():
   return render_template('input.html')


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

if __name__ == "__main__":
   app.run(debug = False,host = '0.0.0.0', port = 5000)# -*- coding: utf-8 -*-