from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "<html><body><h1>Test site running under Flask - Piero</h1></body></html>"

@app.route("/hello/<name>")
def hello(name):
    return f"hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
