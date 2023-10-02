# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 21:57:54 2023

@author: Sujeni
"""

from flask import Flask, render_template
app = Flask(__name__)
  
@app.route("/")
def index():
   return render_template("./index.html")
  
if __name__ == '__main__':
   app.run(debug = True)