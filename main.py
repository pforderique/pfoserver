from flask import Flask, jsonify, request, render_template
from views import views
from projects import opencv_views

import sys
sys.path.append("/home/pi/pfoserver2/apis")

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(opencv_views, url_prefix="/opencv")

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)