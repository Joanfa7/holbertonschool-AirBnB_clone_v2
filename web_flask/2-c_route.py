#!/usr/bin/python3
'''Flask App'''

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




if __name__ == "__main__":
    app.run(host="0.0.0.0")
