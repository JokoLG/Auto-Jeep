import time
import RPi.GPIO as GPIO
import board
from board import SCL, SDA
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
 
kit.continuous_servo[0].throttle = -.01

butPin = 18 # Broadcom pin 18 (P1 pin 11)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

while (True):        
    if GPIO.input(butPin) == False: # false means button is pressed
        print ("works")
        break
        

#GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
timeout = 0.020


while 1:
        GPIO.setup(17, GPIO.OUT)
        #cleanup output
        GPIO.output(17, 0)

        time.sleep(0.05)

        #send signal
        GPIO.output(17, 1)

        time.sleep(0.05)

        GPIO.output(17, 0)

        GPIO.setup(17, GPIO.IN)
        
        goodread=True
        watchtime=time.time()
        while GPIO.input(17)==0 and goodread:
                starttime=time.time()
                if (starttime-watchtime > timeout):
                        goodread=False

        if goodread:
                watchtime=time.time()
                while GPIO.input(17)==1 and goodread:
                        endtime=time.time()
                        if (endtime-watchtime > timeout):
                                goodread=False
        
        if goodread:
                duration=endtime-starttime
                distance=duration*34000/2
                if distance < 50:
                    kit.continuous_servo[0].throttle = -.01
#                     print("BEGIN EVASIVE MANUEVERS!!!!")
                else:
                    kit.continuous_servo[0].throttle = -.3
                    print (distance)
                    
                    
        if GPIO.input(butPin) == False: # false means button is pressed
            print ("works")
            kit.continuous_servo[0].throttle = -.01
            break
                    
