from flask import Blueprint, render_template, abort

views = Blueprint('views', __name__, template_folder='templates')

@views.route("/")
def home():
    return render_template('home.html')