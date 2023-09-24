#!/usr/bin/python3
""" simple flask task """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ define the function hello """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ define the func hbnb """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
