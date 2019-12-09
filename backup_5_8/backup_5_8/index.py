# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:09:21 2019

@author: smehdi@ncsu.edu
"""
from flask import Flask,Response

from flask import render_template

app = Flask(__name__)
@app.route('/view')
def show_map():
    return render_template('view.html')



if __name__ == "__main__":

    app.run(debug=False,host='0.0.0.0',port=5500, threaded=True)