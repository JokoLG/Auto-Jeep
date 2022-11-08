import time
from time import sleep


posX = -200
print ("posX")
print (posX)

steering = (posX/(300*(1/0.5)))
print ("steering")
print (steering)

objSize = (3300)-150

speed = ((objSize/((3600-150)*(1/0.5)))-((0.5/10)*9))
if speed > 0:
    speed = 0
print("Speed")
print(speed)





