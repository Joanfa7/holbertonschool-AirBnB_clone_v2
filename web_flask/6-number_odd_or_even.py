#!/usr/bin/python3
'''Flask App'''

from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    ''' return Hello HBNB'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' return HBNB '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    ''' return a '''
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/(<text>)", strict_slashes=False)
def python(text='is cool'):
    ''' return python is cool'''
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<n>", strict_slashes=False)
def num(n):
    return "{} is a number".format(n.is_integer())


@app.route("/number/<int:n>", strict_slashes=False)
def numbr(n):
    ''' return a digit '''
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    ''' return html file'''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    ''' reutrn html file '''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
