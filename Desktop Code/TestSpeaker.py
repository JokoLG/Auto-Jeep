# WORKING
# we connected the speaker through the headphone port in the Raspberry Pi because the Bluetooth wasn’t working
# it was able to play the bicycle sound file on the Desktop

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
import pygame
 
kit = ServoKit(channels=16)
butPin = 16
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

pygame.mixer.init()
pygame.mixer.music.load("bicycle_bell.wav")

while (True):
    
    if GPIO.input(butPin) == False:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue