#!/usr/bin/python3
'''Module 1-hbnb_route
A basic Flask app that writes "Hello, HBNB!" to the screen on route /
and "HBNB" on route /hbnb
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
