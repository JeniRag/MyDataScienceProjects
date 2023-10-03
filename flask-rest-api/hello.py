# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 21:01:21 2023

@author: Sujeni
"""

# an object of WSGI application
from flask import Flask, redirect, url_for   
app = Flask(__name__)   # Flask constructor
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/')      
def hello():
    return 'HELLO'

@app.route('/hello/')      
def hello_world():
    return 'hello world' 

#app.add_url_rule('/', 'hello', hello_world)

def show_animal(animalname):
   return f"Hello {animalname}"
app.add_url_rule("/animal/<animalname>", "show_animal", show_animal)
#http://localhost:5000/animal/Cat

"""Variables"""
@app.route('/hello/<name>')      
def hello_world_name(name):
    return 'hello world %s ' % name 

@app.route('/float/<float:revNo>')
def show_float(revNo):
    return 'The float number is: %f' % revNo

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID


"""url_for()"""
@app.route('/admin')  #decorator for route(argument) function
def hello_admin():     #binding to hello_admin call
   return 'Hello Admin'    
  
@app.route('/guest/<guest>')
def hello_guest(guest):    #binding to hello_guest call
   return 'Hello %s as Guest' % guest
  
@app.route('/user/<name>')
def hello_user(name):    
   if name =='admin':  #dynamic binding of URL to function
      return redirect(url_for('hello_admin'))  
   else:
      return redirect(url_for('hello_guest', guest = name))


  
if __name__=='__main__':
   app.run(debug=True) #flask application started by 