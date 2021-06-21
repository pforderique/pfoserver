from flask import Flask, jsonify, request, render_template
from views import views

import sys
sys.path.append("/home/pi/pfoserver2/apis")

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)