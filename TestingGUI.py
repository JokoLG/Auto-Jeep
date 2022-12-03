# Imports
from guizero import App, Text, PushButton

# Gui Variables
number = 1
page = "Testing_1"

def valueUp():
    global number
    number += 1
    value = Text(app, grid=[2,1], text=number, width=2, size=35)
    app.display()

def valueDown():
    global number
    number -= 1
    value = Text(app, grid=[2,1], text=number, width=2, size=35)

app = App(title="Jeep Testing UI", layout="grid")

if (page == "Main"): 
    print("no")

elif page == "Testing_1":
    welcome = Text(app, grid=[0,1], text="Pi GUI Test: ", size=40, font="Arial", color="black")
    value_up = PushButton(app, grid=[1,1], command=valueUp, text="+")
    value = Text(app, grid=[2,1], text=number, width=2, size=35)
    value_down = PushButton(app, grid=[3,1], command=valueDown, text="-")



 
app.display()

