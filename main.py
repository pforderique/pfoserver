from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from pymongo import MongoClient
from config import SECRET_KEY, MONGO_URI
from apis.airchat import wassup

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
cluster = MongoClient(MONGO_URI)

airchat_db = cluster['airchat']
users = airchat_db['users']

@app.route("/")
def index():
    return "<html><body><h1>Test site running under Flask - Piero!</h1></body></html>"

@app.route("/see-users")
def see_users():
    output = [{'name':user.get('name'), 'age':user.get('age')} for user in users.find()]
    return jsonify({'result': output})

@app.route("/hello/<name>")
def hello(name):
    users.insert({'name':name, 'age':10})
    # out = [{"name":user.get("name"), "age":user.get("age")} for user in results]
    return jsonify({"response":"user added"})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
