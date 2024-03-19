#!/usr/bin/python3
"""The script starts a web application listening on
port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns an empty page"""
    return ("Hello HBNB")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
