#!/usr/bin/python3
"""simple flask app

    Returns:
        route: html file
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

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text="is cool"):
    """ define python text """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
