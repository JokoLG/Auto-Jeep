# WORKING
# this detects the yellow ball with its current color values
# this creates a mask that shows the parts of the image that are detected in white

import cv2
import numpy as np

lower = np.array([-255, -255, -255])
upper = np.array([30, 30, 30])

video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
                print (x)
                
    
    cv2.imshow("mask", mask)
    cv2.imshow("webcam", img)
    
    cv2.waitKey(1)
    


