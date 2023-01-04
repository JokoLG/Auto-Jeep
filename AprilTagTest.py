# NOT wORKING! #
# code we got from the internet to try and recognize an april tag

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import apriltag as ap
#import threading
from threading import Thread

cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE )
video = cv2.VideoCapture(0)

class PiVideoStream:
    def __init__(self, resolution=(640,480), framerate=60):
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
            #self.rawCapture.truncate(0)
            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self.stopped:
                #self.stream.close()
                #self.rawCapture.close()
                #self.camera.close()
                return
                
    def read(self):
        # return the frame most recently read
        return self.frame
        
    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

#Start Camera Acquisition Thread
#cam = WebcamVideoStream(src=0).start() ##Used for USB camera
#cam = PiVideoStream().start()  #Used with Pi Camera

# define the AprilTags detector options and then detect the AprilTags
# in the input image
#print("[INFO] detecting AprilTags...")
options = ap.DetectorOptions(families="tag36h11")
detector = ap.Detector(options)

#Begin Image processing loop
while(True):
    success, img = video.read() #cam.read() # For USB camera or Pi Camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    results = detector.detect(gray)
    
    #for r in results:
    (ptA, ptB, ptC, ptD) = results.corners
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))
    
    cv2.line(gray, ptA, ptB, (0,255,0),2)
    cv2.line(gray, ptB, ptC, (0,255,0),2)
    cv2.line(gray, ptC, ptD, (0,255,0),2)
    cv2.line(gray, ptD, ptA, (0,255,0),2)
        
    print("[INFO] {} total AprilTags detected".format(len(results)))
    print (results.coordinates)
    
    cv2.imshow('Camera', img)

    k = cv2.waitKey(1) # wait xx ms for specified key to be pressed
    if k % 256 == 27: # "27" is the "Esc" key
        break # end the while loop

#When everything is finished, release capture and kill windows
cam.stop()
cv2.destroyAllWindows() # Close the display window
