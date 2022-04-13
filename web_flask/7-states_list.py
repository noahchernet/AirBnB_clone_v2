#!/usr/bin/python3
'''
Module 7-states_list
Starts a Flask web application
The route /states_list gets all states in storage and prints them
'''
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Render template with states
    Gets all the states and prints their ids and names
    '''
    path = '7-states_list.html'
    states = storage.all(State)
    # sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    '''Clean-up session
    Reloads the session to refresh the objects in the session, from the database
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
