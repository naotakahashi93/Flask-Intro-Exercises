from operations import add, sub, mult, div

from flask import Flask, request

# Put your app in here.
app = Flask(__name__)

@app.route("/add")
def add():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a+b  # or add(a, b)
    return str(result)

@app.route("/sub")
def sub():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a-b  # or sub(a, b)
    return str(result)

@app.route("/mult")
def mult():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a*b  # or mult(a, b)
    return str(result)

@app.route("/div")
def div():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a/b  # or div(a, b)
    return str(result)

