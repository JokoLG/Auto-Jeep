from gpiozero import Button
from signal import pause

def say_hello():
    #print("Hello, Button 1!")
    return lambda: print("Hello, Button 1!")


def say_goodbye():
    #print("Goodbye!")
    return lambda: print("Goodbye!")

def buttPressed():
    print("YOU PUSHED IT")

button1 = Button(18)

while (True):
    button1.wait_for_press()
    buttPressed()
    print("The button was pressed!")
    button1.when_pressed = say_hello()
    button1.when_released = say_goodbye()

    pause()