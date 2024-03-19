#!/usr/bin/python3
"""The script starts a web application listening on
port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns an empty page"""
    return ("Hello HBNB")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays hbnb"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def variable_input(text):
    """displays variables inputed"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_variable(text="is cool"):
    """displays variables inputed"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def display_integers(n):
    """displays only when a number is an integer"""
    return ("{:d} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """displays the template when n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
