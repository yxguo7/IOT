from guizero import App, Box, Text, TextBox, PushButton, Slider
from grovepi import *
import time

myLED1 = 5 # red
pinMode(myLED1, "OUTPUT")

def exitProgram():
    digitalWrite(myLED1, 0)
    app.destroy()

def sliderToggleLED1(slider_value):
    analogWrite(myLED1, int(slider_value))

def led1Toggle():
    button_status = digitalRead(myLED1)
    if (button_status == 0):
        digitalWrite(myLED1, 1)
        ledButton1.text = "Turn OFF"
        ledButton1.bg = "green"
        ledButton1.text_color = "white"
        textLED1.text_color = "green"
    else:
        digitalWrite(myLED1, 0)
        ledButton1.text = "Turn ON"
        ledButton1.bg = "red"
        textLED1.color = "black"

app = App(title="TCSS573: IoT Activity 02", height=300, width=500)
main = Text(app, text="LED Fading", size=14, font="Times New Roman", color="navy")
box = Box(app, layout="grid", grid=[1, 0])

textLED1 = Text(box, text="RED", align="left", grid=[0, 0])
ledButton1 = PushButton(box, command=led1Toggle, text="Turn ON", grid=[1, 0])
sliderLED1 = Slider(box, start=0, end=255, command=sliderToggleLED1, grid=[4, 0])
exitButton = PushButton(box, command=exitProgram, text="Exit", grid=[2, 8])
app.display()

