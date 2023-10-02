
Tutorial: [https://pythonbasics.org/flask-rest-api/](https://pythonbasics.org/flask-rest-api/) 

To see your programm results, enter the follwing URL in the browser:
```
localhost:5000
```
To run the application write the following in your terminal:
```
python hello.py
```

``` 
run() 
``` 
starts the flask application. This method should be restarted manually for any changes in the code. But you can enable the debug suport to track any error.

```
app.debug = True
app.run()
app.run(debug = True)
```
One can run hello.py by writing 
``` 
python hello.py 
``` 
into the terminal and accessing [http://127.0.0.1:5000](http://127.0.0.1:5000).
With routing, the user can remember the URLs and is useful to acces the web page directly wihtout navigating from the Home page. It can be done using the route() or add_url_rule()
```
@app.route("/hello")

app.add_url_rule("/", "hello", hello_workd)
```
If user visits http://localhost:5000/hello the output of the hello_world() function will be shown in the browser.


## Variables in Flask
The URL can be build dynamically by adding the variables. The variable is passed as keyworkd argument.
For the hello_world_name() function in hello.py, the variable is passed as [http://localhost:5000/hello/Me](http://localhost:5000/hello/Me).
Floats and integers are defined as
```
<float:revNo>
<int:postID>
```

## Building URL in Flask
url_for() can be used for hte dynamic building of the URL for a specific function. The first argument is the name of the function, the following arguments the keyword arguments.

```
http://localhost:5000/user/admin
http://localhost:5000/user/Jura
```

##HTTPS protocols for data retrieval

There are six commonly used HTTP request methods:
* GET: To get the data.
* POST: Sends the form data to server.
* PUT: Replaces current representation of target resource with URL.
* DELETE: Deletes target resource of a given URL.
* PATCH
* HEAD: proivdes response body to the form.

```
@app.route("/", methods=["POST"])
@app.rout("/", methods=["DELETE"])
```
Use the methods defined in the flask application in request_methods.py:
* GET Method to retrieve data:

```
http://localhost:5000/?name=Hello Kitty
```
## Static Files
Javascript or CSS file might be required for we applications to render the display.
An example is provided in the static_files folder.
render_template() searches for files stored in a templates folder. The javascript is located in the static folder.

## Cookies
A cookie is a form of text file, which is stored on a client's computer.
An example is provided in the cookies folder.

## Session in Flask
In Session, the data is stored on Server. Each user has a specific Session ID.
```
Flask.redirect(location, statuscode, response) // returns the response of an object and redirects the user to another target location with specified status code.
Flask.abort(code) //404: For Not Found
```

## File Uploading in Flask
...

## Sending Form Data to the HTML File of Server
In sending_form, an HTML form is used to collect information and forwarded and stored on the server. 

## Message Flashing
A pop-up or dialog box, which is used to inform the user.
```
flash(message, category)
```
The message is the text to be displayyed and category is optional.

...

#Theory
## Flask
Flask is a web framework, that allows developers to build lightweight web applications.
Source: [https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp](https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp)
 
## API
An API (Application Programming Interface) provides an interface to interact with different applications. With API we can retrieve, process and send data form other applications.

## Rest API
With REST (Representational State Transfer) API we send the server a request, unlike an APIi which respoinds with data.
One feature of REST API is it's statelessness, after the server completes one action, it forgets about it.


Source: [https://www.askpython.com/python-modules/flask/flask-rest-ap](https://www.askpython.com/python-modules/flask/flask-rest-api)
