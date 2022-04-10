#!/usr/bin/python3
'''Module 6-number_odd_or_even
A basic Flask app that writes "Hello, HBNB!" to the screen on route /
and "HBNB" on route /hbnb
and shows the text passed in the route c/<text>
and shows the text passed in the route python/<text>, if nothing is passed
"Python is cool" is printed
/number/<n> displays a number only if it's an integer
/number_template/<n> displays an HTML page with the number passed, if it's an
int, or 404 if it is not
/number_odd_or_even/<n> tells if n is even or odd
'''
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def print_int(n):
    '''Prints the integer passed to it, it fails if n is not a n int'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def int_template(n):
    '''Renders an HTML page with the parameter integer n'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    '''Renders an HTML page with the parameter integer n
    and tells if it is even or odd'''
    affinity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, affinity=affinity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
