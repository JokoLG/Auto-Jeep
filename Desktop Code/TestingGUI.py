# WORKING
# created a user interface to make running programs easier
# the other testing gui script has a more in depth comment at the top

# Imports
from guizero import App, Text, PushButton, Slider
import subprocess
import numpy as np
import cv2

# Gui Variables
page = "Main"

# Color Variables
r1Up, g1Up, b1Up = (1,2,3)
r1Lo, g1Lo, b1Lo = (0,0,0)
r2Up, g2Up, b2Up = (0,0,0)
r2Lo, g2Lo, b2Lo = (0,0,0)

upper1 = np.array([r1Up, g1Up, b1Up])
lower1 = np.array([r1Lo, g1Lo, b1Lo])
upper2 = np.array([r2Up, g2Up, b2Up])
lower2 = np.array([r2Lo, g2Lo, b2Lo])

def goTo(pageString):
    global page
    if (page == "Testing_1"):
        cv2.destroyWindow("res")
        cv2.destroyWindow("img")
    page = pageString
    updateGUI()

app = App(title="Jeep Testing UI", layout="grid", width=450, height=775)

def updateGUI():
    global app
    app.destroy()
    app = App(title="Jeep Testing UI", layout="grid", width=450, height=775)

    if (page == "Main"): 
        back = PushButton(app, grid=[0,0], command=lambda:goTo("Main"), text="Back", width="fill", height=1, align="left", pady=0)
        Title = Text(app, grid=[0,1], text="Main", size=70, width="fill")
        Testing_1 = PushButton(app, grid=[0,2], command=lambda:goTo("Testing_1"), text="Testing 1")
        Testing_2 = PushButton(app, grid=[1,2], command=lambda:goTo("Testing_2"), text="Testing 2")
        Testing_1.text_size = 30
        Testing_2.text_size = 30

    elif page == "Testing_1":
        back = PushButton(app, grid=[0,0], command=lambda:goTo("Main"), text="Back", width="fill", height=1, align="left", pady=0)
        

        def copyToC(R, G, B):
            txt = "("+str(R)+", "+str(G)+", "+str(B)+")"
            cmd='echo '+txt.strip()+'|clip'
            return subprocess.check_call(cmd, shell=True)

        def updVal(useless):
            global r1Up, g1Up, b1Up
            useless = useless # a literally useless but required value
            r1Up, g1Up, b1Up = (R_U_1_S.value, G_U_1_S.value, B_U_1_S.value)
            r1Lo, g1Lo, b1Lo = (R_L_1_S.value, G_L_1_S.value, B_L_1_S.value)
            r2Up, g2Up, b2Up = (R_U_2_S.value, G_U_2_S.value, B_U_2_S.value)
            r2Lo, g2Lo, b2Lo = (R_L_2_S.value, G_L_2_S.value, B_L_2_S.value)

        Color_1 = Text(app, grid=[1,1], text="Color One: ", size=20)
        Copy_U_1 = PushButton(app, grid=[0,2], command=lambda:copyToC(R_U_1_S.value, G_U_1_S.value, B_U_1_S.value), text="Copy", width="fill", height=1, align="left", pady=0)
        Upper_1 = Text(app, grid=[1,2], text="Upper: ", size=20, align="left")
        R_U_1 = Text(app, grid=[0,3], text="R: ", size=20)
        R_U_1_S = Slider(app, grid=[1,3], end=255, command=updVal, width=300)
        G_U_1 = Text(app, grid=[0,4], text="G: ", size=20)
        G_U_1_S = Slider(app, grid=[1,4], end=255, command=updVal, width=300)
        B_U_1 = Text(app, grid=[0,5], text="B: ", size=20)
        B_U_1_S = Slider(app, grid=[1,5], end=255, command=updVal, width=300)
        Copy_L_1 = PushButton(app, grid=[0,6], command=lambda:copyToC(R_L_1_S.value, G_L_1_S.value, B_L_1_S.value), text="Copy", width="fill", height=1, align="left", pady=0)
        Lower_1 = Text(app, grid=[1,6], text="Lower: ", size=20, align="left")
        R_L_1 = Text(app, grid=[0,7], text="R: ", size=20)
        R_L_1_S = Slider(app, grid=[1,7], end=255, command=updVal, width=300)
        G_L_1 = Text(app, grid=[0,8], text="G: ", size=20)
        G_L_1_S = Slider(app, grid=[1,8], end=255, command=updVal, width=300)
        B_L_1 = Text(app, grid=[0,9], text="B: ", size=20)
        B_L_1_S = Slider(app, grid=[1,9], end=255, command=updVal, width=300)

        Color_2 = Text(app, grid=[1,10], text="Color Two: ", size=20)
        Copy_U_2 = PushButton(app, grid=[0,11], command=lambda:copyToC(R_U_2_S.value, G_U_2_S.value, B_U_2_S.value), text="Copy", width="fill", height=1, align="left", pady=0)
        Upper_2 = Text(app, grid=[1,11], text="Upper: ", size=20, align="left")
        R_U_2 = Text(app, grid=[0,12], text="R: ", size=20)
        R_U_2_S = Slider(app, grid=[1,12], end=255, command=updVal, width=300)
        G_U_2 = Text(app, grid=[0,13], text="G: ", size=20)
        G_U_2_S = Slider(app, grid=[1,13], end=255, command=updVal, width=300)
        B_U_2 = Text(app, grid=[0,14], text="B: ", size=20)
        B_U_2_S = Slider(app, grid=[1,14], end=255, command=updVal, width=300)
        Copy_L_2 = PushButton(app, grid=[0,15], command=lambda:copyToC(R_L_2_S.value, G_L_2_S.value, B_L_2_S.value), text="Copy", width="fill", height=1, align="left", pady=0)
        Lower_2 = Text(app, grid=[1,15], text="Lower: ", size=20, align="left")
        R_L_2 = Text(app, grid=[0,16], text="R: ", size=20)
        R_L_2_S = Slider(app, grid=[1,16], end=255, command=updVal, width=300)
        G_L_2 = Text(app, grid=[0,17], text="G: ", size=20)
        G_L_2_S = Slider(app, grid=[1,17], end=255, command=updVal, width=300)
        B_L_2 = Text(app, grid=[0,18], text="B: ", size=20)
        B_L_2_S = Slider(app, grid=[1,18], end=255, command=updVal, width=300)

    elif page == "Testing_2":
        back = PushButton(app, grid=[0,0], command=lambda:goTo("Main"), text="Back", width="fill", height=1, align="left", pady=0)
        Title = Text(app, grid=[0,1], text="Testing 2: ", size=40)

    app.display()
    
    video = cv2.VideoCapture(0)
    minSize = 150 # Minimum object size for recognition
        
    while True:
        success, img = video.read()
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        maskOne = cv2.inRange(image, lower1, upper1)
        maskTwo = cv2.inRange(image, lower2, upper2)
        res = cv2.bitwise_and(image, image, mask=maskOne+maskTwo)
        res[maskOne>0]=(0, 255, 0)
        res[maskTwo>0]=(255, 0, 0)
        resMask = cv2.inRange(res, (10,10,10), (255,255,255))
        contours, hierarchy = cv2.findContours(resMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours)!=0:
            for contour in contours:
                if cv2.contourArea(contour) > minSize:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
                    
        cv2.imshow("res", res)
        cv2.imshow("img", img)
        cv2.waitKey(1)

updateGUI()

print ("stuff")
