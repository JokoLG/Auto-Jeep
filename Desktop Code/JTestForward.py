# WORKING
# starts moving forward if the button is pressed

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
 
kit.continuous_servo[0].throttle = -0.1
# drive time 
kit.continuous_servo[1].throttle = 0 # steering wheel
butPin = 16 # Broadcom pin 16 (P1 pin 36)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

ButtonYes = -1

while (True):
    print(ButtonYes)
    if GPIO.input(butPin) == False:
        ButtonYes = -1*ButtonYes
    
#        if ButtonYes == False:
#            Buttonyes = True
#            print("poopy")
#        else:
#            ButtonYes = False
#            print("poopyyyyyyyyyyyy")

    if ButtonYes == 1:         #True:  false means button is pressed
        kit.continuous_servo[0].throttle = -1
        #print("poop")

    else: 
        kit.continuous_servo[0].throttle = -0.01
        #print("pooooop")







