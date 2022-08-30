#this code interacts with the vex falcon motor controllers as if they were servos
#It uses functions specific to the PWM hat 

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
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

def turnRight():
    kit.continuous_servo[0].throttle = -.42
    sleep(.35)
    kit.continuous_servo[0].throttle = 0

def turnLeft():
    kit.continuous_servo[0].throttle = .29
    sleep(.35)
    kit.continuous_servo[0].throttle = 0

sleep(.1)
turnRight()
sleep(1)
turnLeft()
sleep(3)
turnLeft()
sleep(1)
turnRight()
