#!/usr/bin/python3
'''Module 2-c_route
A basic Flask app that writes "Hello, HBNB!" to the screen on route /
and "HBNB" on route /hbnb
and shows the text passed in the route c/<text>
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
    return "C {}\n".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
