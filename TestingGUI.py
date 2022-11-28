from guizero import App, Text, PushButton

def say_my_name():
    welcome_message.value = "f**k apriltags"

app = App(title="Ur Mom.")

welcome_message = Text(app, text="Pi GUI Test", 
                       size=40, font="Arial", 
                       color="black")
button_test = PushButton(app, command=say_my_name, text="Test")

app.display()
