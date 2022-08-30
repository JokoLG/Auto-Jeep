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

def turnRight():
    kit.continuous_servo[1].throttle = -.42
    sleep(.35)
    kit.continuous_servo[1].throttle = 0

def turnLeft():
    kit.continuous_servo[1].throttle = .29
    sleep(.35)
    kit.continuous_servo[1].throttle = 0

while (True):
    
    #if GPIO.input(butPin) == False: # false means button is pressed
        print ("works")
        print("print (\"This jeep works\")")
        print("cout<<\"Hello World!\"<<endl);")
        print("System.out.println(\"Hello World!\");")
        
        GPIO.input(butPin) == True
        
        #sleep(2)
        #break

while 1:
    
    kit.continuous_servo[0].throttle = -.3
    sleep(3)
    turnRight()
    sleep(3)
    kit.continuous_servo[0].throttle = -.01
    turnLeft()
    kit.continuous_servo[0].throttle = -.3
    sleep(3)
    kit.continuous_servo[0].throttle = -.01
    break
    
      
    