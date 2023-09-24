#!/usr/bin/python3
"""simple flask ap
"""
from flask import Flask
from flask import render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception=None):
    """ close the storage """
    storage.close()
    
@app.route("/states_list", strict_slashes=False)
@app.route('/states_list/<state_id>', strict_slashes=False)
def states_list():
    """ display the states """
    states = list(storage.all("State").values())
    states.sort(key=lamba x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
