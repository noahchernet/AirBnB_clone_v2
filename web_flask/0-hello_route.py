#!/usr/bin/python3
'''Module 0-hello_route
A basic Flask app that writes "Hello, HBNB!" to the screen
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index_route():
    '''Home page of the server'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
