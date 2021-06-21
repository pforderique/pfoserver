from flask import Blueprint, render_template, abort, Response
import cv2

opencv_views = Blueprint(
    'opencv_views',
    __name__,
)

camera = cv2.VideoCapture(0)

@opencv_views.route("/")
def home():
    return render_template("opencv_home.html")

@opencv_views.route("/video-feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' +
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
