
This project contains my notes and summaries from the tutorials I have been following.
# Flask Quick Start

Tutorial: [https://pythonbasics.org/flask-rest-api/](https://pythonbasics.org/flask-rest-api/) and [https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp](https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp)

To see your programm results, enter the follwing URL in the browser:
```
localhost:5000
```
To run the application write one of the following in your terminal:
```
flask --app hello run
python hello.py
```
In an folder, where the scipt is described as app.py one of the following can be used:
```
flask --app app run
flask run
python app.py
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
With routing, the user can remember the URLs and is useful to acces the web page directly wihtout navigating from the Home page. It can be done using the route() or add_url_rule(). Routing maps the URLs to a specific function.
```
@app.route("/hello")

app.add_url_rule("/", "hello", hello_workd)
```
If user visits [http://localhost:5000/hello](http://localhost:5000/hello) the output of the hello_world() function will be shown in the browser.


## Variables in Flask

The URL can be build dynamically by adding the variables. The variable is passed as keyworkd argument.
For the hello_world_name() function in hello.py, the variable is passed as [http://localhost:5000/hello/Me](http://localhost:5000/hello/Me).
A converter converts the variable to a specific data type. Per defualt the string is set to a string variable.
<converter:variable_name>
possible converter:
* string
* int
* float
* path: like a string but accepts slashes
* uuid: accepts UUID strings.
* any: matches one of the itmes provided.
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
* GET: To get the data from server.
* POST: Submits data to server.
* PUT: Replaces current representation of target resource with URL. Modifies data on the server.
* DELETE: Deletes target resource of a given URL.
* PATCH: Similar to PUT request, but it modifies a part of the data. Only updates the content that you want to update.
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

Another example of the POST request is shown in the simple_post folder.
Run the app.py script and open login.html.

GET appends the data to the URL, POST doesn't. Two examples are shown in the get_example and post_example folder.
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
The message is the text to be displayed and category is optional.
...


## Redirecting URL
An example is given in the **redirect** folder. The example has two routes, the base route **\** and **\helloworld** route.
When the user hites the base URL, it will automatically redirect to **\helloworld**.

### Status Codes
While accessing a website, our browser sends a request to the server. The server replies with an HTTP status coce.
The different reasons for errors are:
* Unauthorized access or poor request.
* Unsupported media file types.
* Overload of the backend server.
* Internal hardware/connection error.

|Code | Status            |   
|-----|-------------------|
| 301 | Moved_permanently | 
| 302 | Found             |  
| 303 | See_other         |   
| 304 | Not_modified      | 
| 305 | Use_proxy         |  
| 306 | Reserved          |  
| 307 | Temporary_redirect|  


```
flask.redirect(location, code=302)
```
The location(str) is the location which URL directs to. code(int) is the status code fo Redirect. The default code is 302.
#Theory

## Flasks Errors
In case there is an error in the adress, or the URL doesn't exist, the **abort()** function can be used to exit with an error.
```
abord(code, message)
```
The code(int) is the code parameter and message(str) teh custom message error.

|Code | Error                  |   
|-----|------------------------|
| 400 | Bad request            | 
| 401 | Unauthenticated        |  
| 403 | Forbidden              |   
| 404 | Not Found              | 
| 406 | Not Acceptable         |  
| 415 | Unsopported Media Type |  
| 429 | Too Many Requests      |  


An example using **abort()** is shown in the **abort_example** folder.
http://localhost:5000/3ant will lead to the abort function.

## Changing the Port in Flask app
The default port for the Flask application is 5000.
If it is already occupied, we can change it by using the below command

```
if __name__=="__main__":
    app.run(debug=True, port=port-number)
```

## Changing Host IP Address in Flask
By defalut Flask applications listen on the local address. They can only be accessed from the same machine that the application is running on.
It is useful to access applications from other devices on the same network or form the internet. For this, the host IP address can be changed.
```
if __name__=="__main__":
    app.run(host=host_number)
```

Or we can change the IP from the command line:

```
set FLASK_APP=app.py
flask run

flask run --host=192.168.0.105 --port=5000
```
## Flask
Flask is a web framework, that allows developers to build lightweight web applications.
Source: [https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp](https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp)
 
## API
An API (Application Programming Interface) provides an interface to interact with different applications. With API we can retrieve, process and send data form other applications.

## Rest API
With REST (Representational State Transfer) API we send the server a request, unlike an APIi which respoinds with data.
One feature of REST API is it's statelessness, after the server completes one action, it forgets about it.


Source: [https://www.askpython.com/python-modules/flask/flask-rest-ap](https://www.askpython.com/python-modules/flask/flask-rest-api)

# Serve Templates and Static Files in Flask
The example in **template_and_static_files\template_example** containes an "wlcome.html" template. After passing the variable name in the render_template function, it is accessible in the template to render the variable.
In **template_and_static_files\inheritance_example** a Jinja Template Inheritance Example is shown. 
In the index.html, everything belows {% endblock %} and everything above {% block body%} tag is copied.
Absolute URLS are used with "{{}}"