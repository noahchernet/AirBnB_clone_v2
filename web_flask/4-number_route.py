#!/usr/bin/python3
'''Module 4-number_route
A basic Flask app that writes "Hello, HBNB!" to the screen on route /
and "HBNB" on route /hbnb
and shows the text passed in the route c/<text>
and shows the text passed in the route python/<text>, if nothing is passed
"Python is cool" is printed
/number/<n> displays a number only if it's an integer
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index_route():
    '''Home page of the server'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    '''Prints "HBNB" only'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text_print(text):
    '''Prints the text passed in the route'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
def python_is_cool():
    '''Default route returns Python is Cool text'''
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_text_print(text):
    '''Prints the text passed in the route'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def print_int(n):
    '''Prints the integer passed to it, it fails if n is not a n int'''
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
