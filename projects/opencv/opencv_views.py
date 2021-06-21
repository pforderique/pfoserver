from flask import Blueprint, render_template, abort

opencv_views = Blueprint(
    'opencv_views',
    __name__,
)

@opencv_views.route("/")
def opencv_home():
    return render_template("opencv_home.html")