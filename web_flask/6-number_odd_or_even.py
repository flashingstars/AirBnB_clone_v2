#!/usr/bin/python3
""" A script that starts a flask web application listening on
0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ A method to return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """ A method to return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cTxt(text):
    """ Displaying C and the value of the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonTxt(text="is cool"):
    """ Displays Python and the value of the text variable """
    return "Python " + text.replace('_', " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Displays n if it is an integer """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def rendering(n):
    """" Rendering a HTML document """
    return render_template("5-number.html", p=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def renderOddEven(n):
    """ Renders a html page that displays Odd or even """
    if n % 2 == 0:
        is_odd_or_even = "even"
    else:
        is_odd_or_even = "odd"
    return render_template("6-number_odd_or_even.html", p=n, v=is_odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
