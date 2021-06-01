from flask import Flask, jsonify, request, render_template
from flask_restful import Api
from .config import SECRET_KEY
from .airchat import User

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

api = Api(app)
api.add_resource(User, "/user/", "/user/<id>")

@app.route("/")
def index():
    return "<html><body><h1>Test site running under Flask :) - Piero!</h1></body></html>"
