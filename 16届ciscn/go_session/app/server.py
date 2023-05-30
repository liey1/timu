from flask import Flask
from flask import request

import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get('name')

    return "hello " + name


if __name__ == "__main__":
    app.run(debug=True,port=5000)