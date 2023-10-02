
Tutorial: [https://pythonbasics.org/flask-rest-api/](https://pythonbasics.org/flask-rest-api/)

To see your programm results, enter the follwing URL in the browser:
```
localhost:5000
```
To run the application write the following in your terminal:
```
pyhton simple_task.py
```
There are six commonly used HTTP request methods:
* GET
* POST
* PUT
* DELETE
* PATCH
* HEAD
```
@app.route("/", methods=["POST"])
@app.rout("/", methods=["DELETE"])
```
Use the methods defined in the flask application in request_methods.py:
* GET Method to retrieve data:
```
http://localhost:5000/?name=Hello Kitty
```
