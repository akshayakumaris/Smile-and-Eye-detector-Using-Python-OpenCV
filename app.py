# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:11:18 2020

@author: user
"""
from flask import Flask,render_template,Response
from camera import smilecamera,eyecamera
import cv2


app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("flask_home_page.html") 

#@app.route('/smile_detector')
#def video_feed():
#    return Response(videocamera(),mimetype='multipart/x-mixed-replace; boundary=frame')
    


def gen(camera):
    while True:
        data=camera.get_frame()
        
        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +frame+ b'\r\n\r\n')
        
        
@app.route('/smile_detector')
def smile_feed():
    return Response(gen(smilecamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/eye_detector')
def eye_feed():
    return Response(gen(eyecamera()),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=="__main__":
    app.run(debug=True)