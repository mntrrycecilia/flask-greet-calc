from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = add(a,b)

    return str(total)



@app.route('/sub')
def sub_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = sub(a,b)

    return str(total)

@app.route('/mult')
def mult_numbers():
    a = int(request.args.get("a"))
    b = int(request.args("b"))
    total = mult(a,b)

    return str(total)

@app.route('/div')
def div_numbers():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = div(a,b)

    return str(total)
