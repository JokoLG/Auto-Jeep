# Auto-Jeep
Github Repository for the Autonomous jeep code

# Libraries
this is a list of the libraries that most likely work
- opencv (import cv2)
- time 
- RPi.GPIO
- board
- adafruit_pca9685
- from adafruit_servokit import ServoKit
- busio
- numpy

# Basics of each library
Opencv (import cv2)
```
# import the library
import cv2

# set video capture to camera number 0 which is the pi's camera
video = cv2.VideoCapture(0)

# 
while True:
    success, img = video.read() # ignoring success cuz idk what its for img is set to your video capture
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # creates a cam that displays img and monitors colors in the HSV color format
    mask = cv2.inRange(image, lower1, upper1) # only shows colors within the upper and lower ranges

    # makes contours and looks for them in the mask 
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # kind of makes an array of the objects on screen that need a contour(box) around them and draws it if theyre big enough
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 100: # this 100 is the min size of the object on screen for it to have borders
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3) # drawing the box
                print (x)
                coord = x # x and y are the coordinates and u can guess what w and h are (width,height)
    cv2.imshow("mask", mask) # this basically makes a window displaying the camera/capture (here the mask)
    cv2.imshow("webcam", img) # ^^^ (here the main camera/capture(img))
    cv2.waitKey(1) # needeed idk what it really does though
```

numpy
```
import numpy as np
# we mainly use it to make arrays of numbers for the upper and lower color ranges
lower = np.array([15, 90, 80])
upper = np.array([30, 255, 225])
```
Time
```
import time
from time import sleep
# we use it for sleep(float seconds)
# which just stops running anything for that amount of time
```

RPi.GPIO/board/SCL/SDA/adafruit/busio
```
import RPi.GPIO as GPIO
import board
from board import SCL, SDA
import adafruit_pca9685
from adafruit_servokit import ServoKit
import busio

#basically this is all to control and get input/output from the pi itself, its gpio pins etc...
i dont fully understand it so... yeah but heres how we use it


i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
 
kit.continuous_servo[0].throttle = -.01 # drive time 
kit.continuous_servo[1].throttle = 0 # steering wheel
butPin = 16 # Broadcom pin 16 (P1 pin 36)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# and this is how we turn the motors
kit.continuous_servo[1].throttle = -.5 # after the equal goes a number between -1 and 1 for the speed
# the number right he^re is the motor number, 0 is the back wheel and 1 is the front rotation
```
we didnt do as much as the previous team with the sensors so check out the sensor scripts to learn about that d:
