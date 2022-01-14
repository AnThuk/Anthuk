from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Response

import os
import cv2

app = Flask(__name__, template_folder="templates", static_url_path='/static')


# for ip camera use -
# rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
# for local webcam use 
# cv2.VideoCapture(0)


def gen_frames():
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        success, frame = webcam.read()  # read the camera frame
        if not success:
            break
        else:

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/localcam')
def localcam():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route('/webcam')
def webcam():
    return render_template('webcam.html')


@app.route('/test', methods=['GET'])
def test():
    return "hello world!"


@app.route('/submit', methods=['POST'])
def submit():
    image = request.args.get('image')

    print(type(image))
    return ""
