# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:22:48 2023

@author: Sujeni
"""
import json
from flask import Flask, jsonify

"""basic Flask web application that returns JSON data"""

#craete flask application instant
app = Flask(__name__) 

#define root URL
@app.route("/") 

#when user acess root URL, index function will be called
def index():
    #return json.dumps({"name": "HelloKitty", "age": 39}) #this would return a html
    return jsonify({"name": "HelloKitty","age": 39}) #this returns a json

app.run()