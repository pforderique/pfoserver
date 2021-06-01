from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

#db = MonoClient()

app = Flask(__name__)
#app.config['MONGO_URI'] =
cluster = MongoClient("mongodb://localhost:27017")
#mongo = PyMongo(app)

#db = mongo.db
#users = db.users
db = cluster['pfoserver']
users = db['users']


@app.route("/")
def index():
    return "<html><body><h1>Test site running under Flask - Piero</h1></body></html>"

@app.route("/hello/<name>")
def hello(name):
    results = users.find({'name':name})
    out = [{"name":user.get("name"), "age":user.get("age")} for user in results]
    return jsonify({"result":out})

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
