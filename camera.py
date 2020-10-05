# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:08:21 2020

@author: user
"""

import cv2
from imutils.video import WebcamVideoStream

class smilecamera(object):
    def __init__(self):
        self.stream=WebcamVideoStream(src=0).start()
        
    def __del__(self):
        self.stream.stop()
        
    def get_frame(self):
        image=self.stream.read()
        
        face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
        #smile detector
        smile_detector=cv2.CascadeClassifier('haarcascade_smile.xml')
        
        frame_grayscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        #detects all types of faces in frame first and puts rectangle around the detected object
        faces=face_detector.detectMultiScale(frame_grayscale)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(100,200,50),4)

            the_face=image[y:y+h,x:x+w]


            face_grayscale=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)


            smiles=smile_detector.detectMultiScale(face_grayscale,scaleFactor=1.7,minNeighbors=30)
        
            for (x_,y_,w_,h_) in smiles: 

            
            #draw rectangles around the smiles
                cv2.rectangle(the_face,(x_,y_),(x_+w_,y_+h_),(50,50,100),4)

            if len(smiles)>0:

                    cv2.putText(image,'smiling',(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))
        
        
        
        
        ret,jpeg=cv2.imencode('.jpg',image)
        data=[]
        data.append(jpeg.tobytes())
        return data
    
    
    
    
class eyecamera(object):
    def __init__(self):
        self.stream=WebcamVideoStream(src=0).start()
        
    def __del__(self):
        self.stream.stop()
        
    def get_frame(self):
        image=self.stream.read()
        
        face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
        #eye detector
        eye_detector=cv2.CascadeClassifier('haarcascade_eye.xml')
        
        frame_grayscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        #detects all types of faces in frame first and puts rectangle around the detected object
        faces=face_detector.detectMultiScale(frame_grayscale)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(100,200,50),4)

            the_face=image[y:y+h,x:x+w]


            face_grayscale=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)
            eyes=eye_detector.detectMultiScale(face_grayscale,scaleFactor=1.2,minNeighbors=30)


            for (x_,y_,w_,h_) in eyes:
                 cv2.rectangle(the_face,(x_,y_),(x_+w_,y_+h_),(225,225,225),4)

            if len(eyes)>0:

                    cv2.putText(image,'asian_eyes',(x,y+h+80),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))
   
        
        
        ret,jpeg=cv2.imencode('.jpg',image)
        data=[]
        data.append(jpeg.tobytes())
        return data


