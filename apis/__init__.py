from flask import Flask, jsonify, request, render_template
from flask_restful import Api
from pymongo import MongoClient
from .config import SECRET_KEY
from .airchat import User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    api = Api(app)

    @app.route("/")
    def index():
        return "<html><body><h1>Test site running under Flask :) - Piero!</h1></body></html>"

    api.add_resource(User, "/user/", "/user/<id>")

    return app