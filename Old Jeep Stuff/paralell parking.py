#charlie task

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

def createSensor(pin):
    
        GPIO.setup(pin, GPIO.OUT)
        #cleanup output
        GPIO.output(pin, 0)

        time.sleep(0.05)

        #send signal
        GPIO.output(pin, 1)

        time.sleep(0.05)

        GPIO.output(pin, 0)

        GPIO.setup(pin, GPIO.IN)
        
        goodread=True
        watchtime=time.time()
        while GPIO.input(pin)==0 and goodread:
                starttime=time.time()
                if (starttime-watchtime > timeout):
                        goodread=False

        if goodread:
                watchtime=time.time()
                while GPIO.input(pin)==1 and goodread:
                        endtime=time.time()
                        if (endtime-watchtime > timeout):
                                goodread=False
        
        if goodread:
                duration=endtime-starttime
                distance=duration*34000/2
                
        return distance
    
def paralellPark(lenght, depth):
    
    kit.continuous_servo[0].throttle = -.01
    sleep(1)
    turnRight()
    sleep(1)
    kit.continuous_servo[0].throttle = .1
    sleep(5)
    turnLeft()
    turnLeft()
    sleep(4)
    turnRight()
    kit.continuous_servo[0].throttle = -.01
    


while (True):
    
    if GPIO.input(butPin) == False: # false means button is pressed
        print ("works")
        sleep(2)
        break

GPIO.setwarnings(False)
timeout = 1
depth = 0
length = 0
x=0

while 1:
        
        distanceFront = createSensor(17)
        distanceBack = createSensor(18)
        
        print (distanceFront)
        print (distanceBack)
        
        if (distanceFront < distanceBack +5 and distanceFront > distanceBack -5):
            print("move forward")
            kit.continuous_servo[0].throttle = -.2
            if (x==1):
                paralellPark(length, depth)
                while 1:
                    distanceF = createSensor(22)
                    distanceB = createSensor(23)
                    if(distanceF > distanceB - 10 and distanceF < distanceB + 10):
                        kit.continuous_servo[0].throttle = -.01
                        break
                    elif(distanceF < distanceB - 10):
                        kit.continuous_servo[0].throttle = .1
                    elif(distanceF > distanceB + 10):
                        kit.continuous_servo[0].throttle = -.1
                break
        elif (distanceFront > distanceBack +10):
            depth = distanceBack
            kit.continuous_servo[0].throttle = -.15
            lenngth = length + 1
        elif (distanceFront + 20 < distanceBack):
            x =1
        
        
        if GPIO.input(butPin) == False: # false means button is pressed
            print ("End Code")
            kit.continuous_servo[0].throttle = -.01
            break
                                                                                                                                                                                                                                                                                                                                                                         