# WORKING
# this is supposed to rotate the wheels to the left or right depending on where the color is detected in the camera view
# the wheels constantly move forward - they don’t stop running with a button yet

import cv2
import numpy as np

import time
import RPi.GPIO as GPIO
import board
from board import SCL, SDA
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
from adafruit_servokit import ServoKit
from time import sleep

lower = np.array([15, 90, 80])
upper = np.array([30, 255, 225])

coord = 300

video = cv2.VideoCapture(0)
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
 
kit.continuous_servo[0].throttle = -.01 # drive time 
kit.continuous_servo[1].throttle = 0 # steering wheel
butPin = 16 # Broadcom pin 16 (P1 pin 36)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

def turnRight():
    kit.continuous_servo[1].throttle = -.5
    print ("right")
    ##kit.continuous_servo[1].throttle = 0

def turnLeft():
    kit.continuous_servo[1].throttle = .5
    print ("left")
    ##kit.continuous_servo[1].throttle = 0

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
                coord = x
                

    if coord > 300:
        turnRight()
    if coord < 300:
        turnLeft()
    #cv2.imshow("mask", mask)
    #cv2.imshow("webcam", img)
    cv2.waitKey(1)