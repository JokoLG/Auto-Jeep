import cv2
import numpy as np
import time
from time import sleep
import RPi.GPIO as GPIO
import board
from board import SCL, SDA
import adafruit_pca9685
from adafruit_servokit import ServoKit
import busio

# Board and hat
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# Color detection color range (BGR format)
lower = np.array([15, 90, 80])
upper = np.array([30, 255, 225])

# Video capture for color detection
video = cv2.VideoCapture(0)

# Variables
posX = 0 # Current object's x position (-Left +Right)
Speed = -.01 # Current forward Speed (-.01 is default, otherwise it moves)
maxSpeed = 0.5 # Max forward speed
steering = 0 # Current steering Speed (-right +left)
maxSteer = 0.5 # Max steering speed
objSize = 0 # Current size of color detected object
minSize = 150 # Minimum object size for recognition

kit.continuous_servo[0].throttle = speed #Forward
kit.continuous_servo[1].throttle = steering #Steering 

# Setup for Pins
butPin = 16 # Broadcom pin 16 (P1 pin 36) (Button)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

while True:
    success, img = video.read()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > minSize:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
                posX = x-300
                print (posX)
                steering = (posX/(300*(1/maxSteer)))
                objSize = (cv2.contourArea(contour))-minSize
                speed = ((objSize/((3600-minSize)*(1/0.5)))-((maxSpeed/10)*9))
                if speed > 0:
                    speed = 0
                kit.continuous_servo[0].throttle = speed
                kit.continuous_servo[1].throttle = steering

    if posX < 0:
        print ("Left")
    elif posX > 0:
        print("Right")
    else:
        print("Center/out")

    cv2.imshow("mask", mask)
    cv2.imshow("webcam", img)
    cv2.waitKey(1)
# End of code ._.   