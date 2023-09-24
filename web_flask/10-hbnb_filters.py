#!/usr/bin/python3
"""simple flask app

    Returns:
        route: html file
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ

app = Flask(__name__)

@app.teardown_appcontext
def tear_down(exception=None):
    storage.close()
    
@app.route("/hbnb_filters", strict_slashes=False)
def states_cities_list():
    states = list(storage.all("State").values())
    states.sort(key=lamba x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
