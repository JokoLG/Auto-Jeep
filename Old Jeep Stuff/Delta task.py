#Delta task

import cv2
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera 
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
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
 
kit.continuous_servo[0].throttle = -.01
kit.continuous_servo[1].throttle = 0
butPin = 16 # Broadcom pin 16 (P1 pin 36)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up



def rgb2gray_approx(rgb_img):
    """
    Convert *linear* RGB values to *linear* grayscale values.
    """
    red = rgb_img[:, :, 0]
    green = rgb_img[:, :, 1]
    blue = rgb_img[:, :, 2]

    gray_img = (
        0.299 * red
        + 0.587 * green
        + 0.114 * blue)

    return gray_img

def turnRight():
    kit.continuous_servo[1].throttle = -.42
    sleep(.35)
    kit.continuous_servo[1].throttle = 0

def turnLeft():
    kit.continuous_servo[1].throttle = .29
    sleep(.35)
    kit.continuous_servo[1].throttle = 0

def nothing(x):
    pass
 
#cv2.namedWindow("Trackbars")
 
#cv2.createTrackbar("B", "Trackbars", 0, 255, nothing)
#cv2.createTrackbar("G", "Trackbars", 0, 255, nothing)
#cv2.createTrackbar("R", "Trackbars", 0, 255, nothing)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 3

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    image2 = rgb2gray_approx(image)
    left = 0
    right = 0
    
    distanceL = 0
    distanceR = 640
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([0,0,255])
    upper_green = np.array([255,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("frame", image)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    x = 0
    white = 0;
    while (x < 640):
        
        if (mask[150][x] == 255 and not right):
            white = white + 1
            if (white > 10):
                if (x < 320):
                    left = 1
                else:
                    right = 1
        else:
            if (left):
                white = 0
                distanceL = 320 - x
                left = 0
            elif (right):
                distanceR =  x - 330
                right = 0
                break
        
        x = x + 1
         
    print (distanceL)
    print (distanceR)
    
    if (distanceL > distanceR + 15):
        kit.continuous_servo[1].throttle = .29
        print ("left")
    elif (distanceR > distanceL + 15):
        kit.continuous_servo[1].throttle = -.42
        print("right")
    else:
        kit.continuous_servo[1].throttle = 0
        print("middle")
    
    key = cv2.waitKey(1)
    rawCapture.truncate(0)
    
    if key == 27:
        break


cv2.destroyAllWindows()