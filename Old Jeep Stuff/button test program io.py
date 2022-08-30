# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:

butPin = 18 # Broadcom pin 18 (P1 pin 11)


# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme


GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up


while (True):        
    if GPIO.input(butPin) == False: # false means button is pressed
        print ("Works")
        time.sleep(1)


