#!/usr/bin/python3
"""simple flask app

    Returns:
        route: html file
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def tear_down(exception=None):
    storage.close()
    
@app.route("/states_list", strict_slashes=False)
def states_list():
    states = list(storage.all("State").values())
    states.sort(key=lamba x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
