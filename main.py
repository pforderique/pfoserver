from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/pfoserver"
mongo = PyMongo(app)

db = mongo.db
users = db.users

@app.route("/")
def index():
  return "<html><body><h1>Test site running under Flask - Piero</h1></body></html>"

@app.route("/hello/<name>")
def hello(name):
  return f"hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
