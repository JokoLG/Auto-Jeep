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
 
kit.continuous_servo[0].throttle = -.01 # drive time 
kit.continuous_servo[1].throttle = 0 # steering wheel
butPin = 16 # Broadcom pin 16 (P1 pin 36)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

def turnRight(Rpower):
    kit.continuous_servo[1].throttle = Rpower
    sleep(.35)
    kit.continuous_servo[1].throttle = 0

def turnLeft(Lpower):
    kit.continuous_servo[1].throttle = Lpower
    sleep(.35)
    kit.continuous_servo[1].throttle = 0

def calibrate(number):
    added = .05
    turnLeft(added*number)
    sleep(2)
    turnRight(-.7)
    sleep(2)

while (True):
    
    if GPIO.input(butPin) == False:
        ButtonYes = True

    else:
        ButtonYes = False

    if ButtonYes == True: # false means button is pressed
        testnum = 1
        print("poop")
        turnRight(-.7)
        sleep(2)
        while testnum < 11:
            calibrate(testnum)
            testnum += 1


    else: 
        kit.continuous_servo[1].throttle = 0
        print("pooooop")
