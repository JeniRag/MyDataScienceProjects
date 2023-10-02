# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:24:25 2023

@author: Sujeni
"""
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)

if __name__ == '__main__':
    app.run(debug = True)
