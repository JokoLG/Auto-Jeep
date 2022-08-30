#this code is a test to recieve acurate distances from a 3 pin ultrasonic sensor

import RPi.GPIO as GPIO
import time


try:
  # Setup
  GPIO.setmode(GPIO.BOARD)

  while(1):
    GPIO.setup(17, GPIO.OUT)
    # Set to low
    GPIO.output(17, False)

    # Sleep 2 micro-seconds
    time.sleep(0.000002)

    # Set high
    GPIO.output(17, True)

    # Sleep 5 micro-seconds
    time.sleep(0.000005)

    # Set low
    GPIO.output(17, False)

    # Set to input
    GPIO.setup(17, GPIO.IN)

    # Count microseconds that SIG was high
    while GPIO.input(17) == 0:
      starttime = time.time()

    while GPIO.input(17) == 1:
      endtime = time.time()

    duration = endtime - starttime
    # The speed of sound is 340 m/s or 29 microseconds per centimeter.
    # The ping travels out and back, so to find the distance of the
    # object we take half of the distance travelled.
    # distance = duration / 29 / 2
    distance = duration * 34000 / 2
    print (distance + "cm")
    time.sleep(0.5)

#finally:
  #GPIO.cleanup()