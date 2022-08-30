#Detects only white and bright colors

import cv2
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera 

vid = cv2.VideoCapture(0)
vid.set(10,.05)

#vid = PiCamera()
#vid.resolution = (640, 480)
#vid.framerate = 60

#rawCapture = PiRGBArray(vid, size=(640, 480))


while(True):
    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([200,200,200])
    upper_green = np.array([255,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('orig',frame)
    cv2.imshow('fff',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()