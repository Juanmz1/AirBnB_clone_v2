#!/usr/bin/python3
"""simple flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ define hello """
    return "Hello HBNB!"

@app.route('/bhnb', strict_slashes=False)
def hbnb():
    """ define hbnb """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ define c_text """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
