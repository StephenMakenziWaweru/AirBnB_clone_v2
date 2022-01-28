#!/usr/bin/python3
"""Module: Starts a Flask web app and fetches data from storage engine"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(cls):
    """Closes session"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """lists states from storage engine"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda  state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
