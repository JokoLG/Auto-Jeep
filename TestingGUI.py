# Imports
from guizero import App, Text, PushButton, Slider
import subprocess

# Gui Variables
page = "Main"

# Color Variables
r1Up, g1Up, b1Up = (1,2,3)
r1Lo, g1Lo, b1Lo = (0,0,0)
r2Up, g2Up, b2Up = (0,0,0)
r2Lo, g2Lo, b2Lo = (0,0,0)

def copyToC(R, G, B):
    txt = "("+str(R)+", "+str(G)+", "+str(B)+")"
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def goTo(pageString):
    global page
    page = pageString

    updateGUI()

app = App(title="Jeep Testing UI", layout="grid", width=500)

def updateGUI():
    global app
    app.destroy()
    app = App(title="Jeep Testing UI", layout="grid", width=450, height=750)

    if (page == "Main"): 
        back = PushButton(app, grid=[0,0], command=lambda:goTo("Main"), text="Back", width="fill", height=1, align="left", pady=0)
        Title = Text(app, grid=[0,1], text="Main", size=70, width="fill")
        Testing_1 = PushButton(app, grid=[0,2], command=lambda:goTo("Testing_1"), text="Testing 1")
        Testing_2 = PushButton(app, grid=[1,2], command=lambda:goTo("Testing_2"), text="Testing 2")
        Testing_1.text_size = 30
        Testing_2.text_size = 30

    elif page == "Testing_1":
        back = PushButton(app, grid=[0,0], command=lambda:goTo("Main"), text="Back", width="fill", height=1, align="left", pady=0)
        
        Color_1 = Text(app, grid=[1,1], text="Color One: ", size=20)
        Copy_U_1 = PushButton(app, grid=[0,2], command=lambda:copyToC(r1Up, g1Up, b1Up), text="Copy", width="fill", height=1, align="left", pady=0)
        Upper_1 = Text(app, grid=[1,2], text="Upper: ", size=20, align="left")
        R_U_1 = Text(app, grid=[0,3], text="R: ", size=20)
        G_U_1 = Text(app, grid=[0,4], text="G: ", size=20)
        B_U_1 = Text(app, grid=[0,5], text="B: ", size=20)
        Copy_L_1 = PushButton(app, grid=[0,6], command=lambda:copyToC(r1Lo, g1Lo, b1Lo), text="Copy", width="fill", height=1, align="left", pady=0)
        Lower_1 = Text(app, grid=[1,6], text="Lower: ", size=20, align="left")
        R_L_1 = Text(app, grid=[0,7], text="R: ", size=20)
        G_L_1 = Text(app, grid=[0,8], text="G: ", size=20)
        B_L_1 = Text(app, grid=[0,9], text="B: ", size=20)

        Color_2 = Text(app, grid=[1,10], text="Color Two: ", size=20)
        Copy_U_2 = PushButton(app, grid=[0,11], command=lambda:copyToC(r2Up, g2Up, b2Up), text="Copy", width="fill", height=1, align="left", pady=0)
        Upper_2 = Text(app, grid=[1,11], text="Upper: ", size=20, align="left")
        R_U_2 = Text(app, grid=[0,12], text="R: ", size=20)
        G_U_2 = Text(app, grid=[0,13], text="G: ", size=20)
        B_U_2 = Text(app, grid=[0,14], text="B: ", size=20)
        Copy_L_2 = PushButton(app, grid=[0,15], command=lambda:copyToC(r2Lo, g2Lo, b2Lo), text="Copy", width="fill", height=1, align="left", pady=0)
        Lower_2 = Text(app, grid=[1,15], text="Lower: ", size=20, align="left")
        R_L_2 = Text(app, grid=[0,16], text="R: ", size=20)
        G_L_2 = Text(app, grid=[0,17], text="G: ", size=20)
        B_L_2 = Text(app, grid=[0,18], text="B: ", size=20)

    elif page == "Testing_2":
        back = PushButton(app, grid=[0,0], command=lambda:goTo("Main"), text="Back", width="fill", height=1, align="left", pady=0)
        Title = Text(app, grid=[0,1], text="Pi GUI Test: ", size=40)

    app.display()

updateGUI()