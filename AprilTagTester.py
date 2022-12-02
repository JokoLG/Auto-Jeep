# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import apriltag as ap
import threading
from threading import Thread
import time 
import math
from networktables import NetworkTables

t0 = 0.0 #Used for testing performance
t1 = 0.0 #Used for testing performance
tLast = 0.0
FlushRate = 100

cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE )

cond = threading.Condition()
notified = [False]


def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()


class PiVideoStream:
	def __init__(self, resolution=(640,480), framerate= 60):
		# initialize the camera and stream
		self.camera = PiCamera()
		self.camera.resolution = resolution
		#self.camera.framerate = framerate
		self.rawCapture = PiRGBArray(self.camera, size=resolution)
		self.stream = self.camera.capture_continuous(self.rawCapture,
			format="bgr", use_video_port=True)
		# initialize the frame and the variable used to indicate
		# if the thread should be stopped
		self.frame = None
		self.stopped = False
		
	def start(self):
		# start the thread to read frames from the video stream
		Thread(target=self.update, args=()).start()
		return self
		
	def update(self):
		# keep looping infinitely until the thread is stopped
		for f in self.stream:
			# grab the frame from the stream and clear the stream in
			# preparation for the next frame
			self.frame = f.array
			self.rawCapture.truncate(0)
			# if the thread indicator variable is set, stop the thread
			# and resource camera resources
			if self.stopped:
				self.stream.close()
				self.rawCapture.close()
				self.camera.close()
				return
				
	def read(self):
		# return the frame most recently read
		return self.frame
		
	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True

#Start Camera Acquisition Thread
#cam = WebcamVideoStream(src=0).start() ##Used for USB camera
cam = PiVideoStream().start()  #Used with Pi Camera

#Begin NetworkTables and wait until connected
NetworkTables.initialize(server='192.168.1.128') #Set NT Server IP, Roborio IP
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here
print("Connected!")

vs = NetworkTables.getTable('Vision') # Get the Vision NetworkTable

# define the AprilTags detector options and then detect the AprilTags
# in the input image
#print("[INFO] detecting AprilTags...")
options = ap.DetectorOptions(families="tag36h11")
detector = ap.Detector(options)

#Begin Image processing loop
while(True):
	t1 = time.perf_counter()#Used for testing performance
	#FPS = (1/(t1-t0))#Used for testing performance
	#vs.putNumber("FPS", FPS)
	Raw = cam.read() ## For USB camera or Pi Camera
	gray = cv2.cvtColor(Raw, cv2.COLOR_BGR2GRAY)
	

	results = detector.detect(gray)
	print("[INFO] {} total AprilTags detected".format(len(results)))
	
	
	# if ((t1-tLast) >= (1/FlushRate)): 
		# NetworkTables.flush()
		# tLast = t1
	
	
	
	cv2.putText(Raw,str(1/(t1 -t0)),(25,25),cv2.FONT_HERSHEY_PLAIN, .8, (255,255,255))
	#vs.putNumber("FPS", FPS)#Used for testing performance
	
	
	cv2.imshow('Camera', Raw)
	t0 = t1
	k = cv2.waitKey(1) # wait xx ms for specified key to be pressed
	if k % 256 == 27: # "27" is the "Esc" key
		break # end the while loop

##When everything is finished, release capture and kill windows
cam.stop()
cv2.destroyAllWindows() # Close the display window
