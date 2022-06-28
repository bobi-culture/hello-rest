from flask import Flask
from flask import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><i>Hello, Dennis !</i></p>"

@app.route("/ping")
def ping():
    return "<p><i> pong!</i></p>"


@app.route('/summary')
def summary():
    data =  {
    "username": "admin",
    "email": "admin@localhost",
    "id": 42 
}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
